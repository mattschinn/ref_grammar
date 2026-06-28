// Parsers that turn the canonical Markdown into the JSON link artifacts.
// Anchors are computed with github-slugger, the same slugger Starlight's
// rehype-slug uses, so the slugs here match the IDs in the rendered HTML.
//
// IMPORTANT: the build strips the leading H1 and any `{#custom-id}` from
// heading lines before rendering (see build-content.mjs). These parsers must
// slug the SAME post-strip heading text, in document order, so a fresh
// GithubSlugger per document reproduces the rendered anchors exactly.

import GithubSlugger from 'github-slugger';

// Uppercase tokens that surface in gloss-tag lines but are NOT linkable gloss
// tags: GA is the source-language abbreviation (pervasive in prose); CLAUSAL is
// only ever a composite fragment (VIS-CLAUSAL), never a standalone tag.
const NON_TAGS = new Set(['GA', 'CLAUSAL']);

const HEADING = /^(#{1,6})\s+(.*?)\s*$/;
const CUSTOM_ID = /\s*\{#[^}]+\}\s*$/;
const FENCE = /^\s*```/;

// Strip a trailing `{#id}` and surrounding space from heading text.
function cleanHeadingText(text) {
  return text.replace(CUSTOM_ID, '').trim();
}

// Strip inline Markdown emphasis/code markers for plain-text card display.
function stripInline(s) {
  return s
    .replace(/`([^`]*)`/g, '$1')
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/\*([^*]+)\*/g, '$1')
    .replace(/_([^_]+)_/g, '$1')
    .trim();
}

// Walk heading lines (skipping fenced code and the leading H1) yielding
// { level, text, slug } with slugs assigned in order by a shared slugger.
function* headings(md) {
  const slugger = new GithubSlugger();
  let inCode = false;
  let sawH1 = false;
  for (const raw of md.split(/\r?\n/)) {
    if (FENCE.test(raw)) { inCode = !inCode; continue; }
    if (inCode) continue;
    const m = raw.match(HEADING);
    if (!m) continue;
    const level = m[1].length;
    if (level === 1 && !sawH1) { sawH1 = true; continue; } // stripped from body
    const text = cleanHeadingText(m[2]);
    yield { level, text, slug: slugger.slug(text) };
  }
}

// Derive the section-number / EID key a heading contributes to headings.json,
// or null if its text starts with neither. Shared by the per-file and the
// assembled-stream paths so both key headings identically.
export function headingKey(text) {
  const num = text.match(/^(\d+(?:\.\d+)*[a-z]?)\b/);
  if (num) return num[1];
  const eid = text.match(/^(E\d{3})\b/);
  if (eid) return eid[1];
  return null;
}

// headings.json entry for one doc: { "<section-number-or-EID>": "<slug>" }
export function parseHeadings(md) {
  const map = {};
  for (const { text, slug } of headings(md)) {
    const key = headingKey(text);
    if (key) map[key] = slug;
  }
  return map;
}

// Slug an ordered heading stream with a SINGLE shared slugger. Used when several
// canonical docs are inlined onto one rendered page: Starlight's rehype-slug runs
// one slugger over the combined page in document order, so collisions across the
// inlined docs (multiple "Abstract", "Versioning Notes", …) must be deduped the
// same way to reproduce the rendered anchors. `stream` items are
// { sourceDoc, text } (already cleaned of leading H1 and `{#id}`), in final order.
// Returns the same items with a `slug` added.
export function slugHeadingStream(stream) {
  const slugger = new GithubSlugger();
  return stream.map((h) => ({ ...h, slug: slugger.slug(h.text) }));
}

// Dictionary entries (under "## 4. Entries"): one record per `### headword`.
export function parseDictionary(md) {
  const slugger = new GithubSlugger();
  const entries = [];
  let inCode = false;
  let sawH1 = false;
  let inEntries = false;
  let cur = null;
  const push = () => { if (cur) { entries.push(cur); cur = null; } };

  for (const raw of md.split(/\r?\n/)) {
    if (FENCE.test(raw)) { inCode = !inCode; continue; }
    if (inCode) continue;

    const h = raw.match(HEADING);
    if (h) {
      const level = h[1].length;
      if (level === 1 && !sawH1) { sawH1 = true; continue; }
      const text = cleanHeadingText(h[2]);
      const slug = slugger.slug(text);
      if (level === 2) {
        push();
        inEntries = /^4\.?\s+Entries/i.test(text);
      } else if (level === 3 && inEntries) {
        push();
        cur = { headword: text, slug, pos: '', ipa: '', foot: '', shortDef: '' };
      }
      continue;
    }

    if (!cur) continue;
    if (!cur.pos && /\*\*Part of speech:\*\*/.test(raw)) {
      const pos = raw.match(/\*\*Part of speech:\*\*\s*(.+?)\s*(?:\*\*|$)/);
      const ipa = raw.match(/\*\*IPA:\*\*\s*(.+?)\s*(?:\*\*|$)/);
      const foot = raw.match(/\*\*Foot:\*\*\s*(.+?)\.?\s*$/);
      if (pos) cur.pos = stripInline(pos[1]);
      if (ipa) cur.ipa = stripInline(ipa[1]);
      if (foot) cur.foot = stripInline(foot[1]);
    }
    if (!cur.shortDef) {
      // Drop an example transclusion token (and its trailing " — " separator / any
      // HTML comment) so the short def is the gloss, not the token.
      const line = raw.replace(/<!--[\s\S]*?-->/g, '').replace(/\s*—\s*$/, '');
      const d = line.match(/^\s*1\.\s+(.+?)\s*$/);
      if (d) cur.shortDef = stripInline(d[1]);
    }
  }
  push();
  return entries;
}

// Gloss tags from terminology-registry.md. Each `### Term` block lists a
// `- **Gloss tag:** X` and a `- **Definition:** …`. Tag order precedes the
// definition in the schema, so accumulate per term and finalize at block end.
export function parseGlosses(md) {
  const slugger = new GithubSlugger();
  const map = {};
  let inCode = false;
  let sawH1 = false;
  let cur = null; // { term, slug, def, tags: [] }
  const finalize = () => {
    if (!cur) return;
    for (const tag of cur.tags) {
      if (!map[tag]) map[tag] = { term: cur.term, def: cur.def, slug: cur.slug };
    }
    cur = null;
  };

  for (const raw of md.split(/\r?\n/)) {
    if (FENCE.test(raw)) { inCode = !inCode; continue; }
    if (inCode) continue;

    const h = raw.match(HEADING);
    if (h) {
      const level = h[1].length;
      if (level === 1 && !sawH1) { sawH1 = true; continue; }
      const text = cleanHeadingText(h[2]);
      const slug = slugger.slug(text);
      finalize();
      if (level === 3) cur = { term: text, slug, def: '', tags: [] };
      continue;
    }
    if (!cur) continue;

    const g = raw.match(/^- \*\*Gloss tag:\*\*\s*(.+?)\s*$/);
    if (g) {
      const tags = (g[1].match(/\b[A-Z][A-Z]+(?:\.[A-Z]+)*\b/g) || []).filter(
        (t) => !NON_TAGS.has(t)
      );
      cur.tags.push(...tags);
    }
    const d = raw.match(/^- \*\*Definition:\*\*\s*(.+?)\s*$/);
    if (d && !cur.def) cur.def = d[1].trim();
  }
  finalize();
  return map;
}

// Example sentences from examples.md: EID -> { conlang, translation, slug }.
// The Conlang and Etymological lines are `|`-delimited into aligned chunks: chunk
// i of one corresponds to chunk i of the other (the unit a renderer highlights or
// pads into a column). IPA and Translation stay free. The record is an open schema
// — future fields (audio, notes) slot in without changing consumers. Back-compat:
// the joined `conlang` string + `translation` + `slug` keep the existing hovercard
// working until the rich renderers (roadmap G) consume `segments`.
const exChunks = (s) => s.split('|').map((x) => x.trim()).filter(Boolean);
const stripQuotes = (s) => s.replace(/^"([\s\S]*)"$/, '$1').trim();

export function parseExamples(md) {
  const slugger = new GithubSlugger();
  const map = {};
  let inCode = false;
  let sawH1 = false;
  let cur = null; // { id, slug, conlangRaw, etymRaw, ipa, translation, tags }

  const finalize = () => {
    if (!cur) return;
    const cl = cur.conlangRaw ? exChunks(cur.conlangRaw) : [];
    const etym = cur.etymRaw ? exChunks(cur.etymRaw) : [];
    if (cl.length && etym.length && cl.length !== etym.length) {
      throw new Error(
        `examples.md ${cur.id}: Conlang splits into ${cl.length} chunks but Etymological into ` +
          `${etym.length}. The two aligned lines must have equal '|'-chunk counts.`
      );
    }
    const n = Math.max(cl.length, etym.length);
    const segments = [];
    for (let i = 0; i < n; i++) segments.push({ cl: cl[i] ?? '', etym: etym[i] ?? '' });
    map[cur.id] = {
      conlang: cl.join(' '), // back-compat joined surface form
      segments,
      ipa: cur.ipa,
      translation: cur.translation,
      tags: cur.tags,
      slug: cur.slug,
    };
    cur = null;
  };

  const fieldVal = (raw, label) => {
    const m = raw.match(new RegExp(`^- \\*\\*${label}:\\*\\*\\s*(.+?)\\s*$`));
    return m ? m[1].trim() : null;
  };

  for (const raw of md.split(/\r?\n/)) {
    if (FENCE.test(raw)) { inCode = !inCode; continue; }
    if (inCode) continue;

    const h = raw.match(HEADING);
    if (h) {
      const level = h[1].length;
      if (level === 1 && !sawH1) { sawH1 = true; continue; }
      const text = cleanHeadingText(h[2]);
      const slug = slugger.slug(text);
      finalize();
      const eid = text.match(/^(E\d{3})\b/);
      if (level === 3 && eid) {
        cur = { id: eid[1], slug, conlangRaw: '', etymRaw: '', ipa: '', translation: '', tags: [] };
      }
      continue;
    }
    if (!cur) continue;

    let v;
    if ((v = fieldVal(raw, 'Conlang')) != null && !cur.conlangRaw) cur.conlangRaw = v;
    else if ((v = fieldVal(raw, 'Etymological')) != null && !cur.etymRaw) cur.etymRaw = v;
    else if ((v = fieldVal(raw, 'IPA')) != null && !cur.ipa) cur.ipa = v;
    else if ((v = fieldVal(raw, 'Translation')) != null && !cur.translation) cur.translation = stripQuotes(v);
    else if ((v = fieldVal(raw, 'Tags')) != null && !cur.tags.length) {
      cur.tags = v.split(/\s+/).map((t) => t.replace(/^#/, '')).filter(Boolean);
    }
  }
  finalize();
  return map;
}
