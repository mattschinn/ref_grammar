// Content compiler: reads the canonical Markdown under ../../docs, injects
// Starlight-ready frontmatter, strips leading H1s and heading `{#id}` markers,
// writes render-ready copies into src/content/docs/ (a gitignored build
// artifact), and emits the JSON link artifacts the remark plugin consumes.

import { readFile, writeFile, mkdir, rm, readdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import {
  parseHeadings,
  parseDictionary,
  parseGlosses,
  parseExamples,
  headingKey,
  slugHeadingStream,
} from './parse.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const siteRoot = path.resolve(__dirname, '..');
const repoRoot = path.resolve(siteRoot, '..');
const docsRoot = path.join(repoRoot, 'docs');
const outRoot = path.join(siteRoot, 'src', 'content', 'docs');
const genRoot = path.join(siteRoot, 'src', 'generated');

const SECTIONS = ['reference', 'dictionary', 'quickref'];

// Must match `base` in astro.config.mjs.
const BASE = '/ref_grammar';
const pageUrl = (rel) => `${BASE}/${rel.replace(/\\/g, '/').replace(/\.md$/, '')}/`;

const ORDER = {
  'reference/language_reference.md': 1,
  'reference/phonology.md': 2,
  'reference/orthography.md': 3,
  'reference/verbal-system.md': 4,
  'reference/terminology-registry.md': 6,
};
const LABEL = { 'reference/terminology-registry.md': 'Glossary' };

// Docs parsed for their artifacts (examples.json) but NOT written as pages.
// examples.md is build-time transclusion source only — never its own page.
const SKIP_PAGE = new Set(['examples.md']);

const yamlStr = (s) => JSON.stringify(s);

function extractTitle(md, fallback) {
  const m = md.match(/^﻿?#\s+(.+?)\s*$/m);
  return m ? m[1].trim() : fallback;
}

const FENCE_RE = /^\s*```/;
const ASSEMBLE_RE = /^<!--\s*assemble:\s*([A-Za-z0-9_.-]+)\s*-->\s*$/;
const HEADING_RE = /^(#{1,6})\s+(.*?)\s*$/;
// `<!-- example: E001 -->` or `<!-- example: E001 | dictionary -->` — transcludes
// an examples.md record. Style defaults from the host doc (dictionary vs grammar),
// overridable after `|`.
const EXAMPLE_TOKEN_RE = /<!--\s*example:\s*(E\d{3})\s*(?:\|\s*([A-Za-z]+)\s*)?-->/g;

// Strip the single leading H1 (Starlight renders the frontmatter title as the
// page heading) and any trailing `{#id}` on remaining heading lines (so anchors
// are the deterministic github-slugger slugs the parsers compute).
function stripDoc(md) {
  let body = md.replace(/^﻿?#\s+.+?(\r?\n)+/, '');
  body = body.replace(/^(#{2,6}\s+.*?)\s*\{#[^}]+\}\s*$/gm, '$1');
  return body;
}

// Shift every heading in `body` down by `delta` levels (capped at h6) so an
// inlined sibling nests under its host section. Records each heading in
// `headingStream` (tagged with `sourceDoc`) in document order for later slugging.
function demoteHeadings(body, delta, sourceDoc, headingStream) {
  const out = [];
  let inCode = false;
  for (const line of body.split(/\r?\n/)) {
    if (FENCE_RE.test(line)) { inCode = !inCode; out.push(line); continue; }
    const m = !inCode && line.match(HEADING_RE);
    if (m) {
      const level = Math.min(6, m[1].length + delta);
      const text = m[2].trim();
      headingStream.push({ sourceDoc, text });
      out.push('#'.repeat(level) + ' ' + text);
    } else {
      out.push(line);
    }
  }
  return out.join('\n');
}

// Turn the parent doc into one continuous document: inline each
// `<!-- assemble: sibling.md -->` directive's target in place (headings demoted
// to nest under the host section), dropping the now-redundant orientation-abstract
// blockquote that follows the directive. Returns the assembled body plus the
// ordered, provenance-tagged heading stream (parent + inlined) for slugging.
function assembleParent(parentBase, parentMd, rawByBase) {
  const lines = stripDoc(parentMd).split(/\r?\n/);
  const out = [];
  const headingStream = [];
  let hostLevel = 2;
  let inCode = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (FENCE_RE.test(line)) { inCode = !inCode; out.push(line); continue; }

    const dir = !inCode && line.match(ASSEMBLE_RE);
    if (dir) {
      const name = dir[1];
      // Skip the following orientation-abstract blockquote (a regenerated copy of
      // the sibling's own Abstract, which we are about to inline in full).
      let j = i + 1;
      while (j < lines.length && lines[j].trim() === '') j++;
      if (j < lines.length && /^>\s/.test(lines[j]) && /Orientation abstract/i.test(lines[j])) {
        while (j < lines.length && (lines[j].trim() === '' || /^>/.test(lines[j]))) j++;
        i = j - 1; // resume after the blockquote
      }
      const sib = rawByBase[name];
      if (!sib) {
        out.push(`> **Full reference:** \`${name}\` _(not found)_`);
        continue;
      }
      const sibBody = stripDoc(sib);
      out.push('', demoteHeadings(sibBody, hostLevel - 1, name, headingStream), '');
      continue;
    }

    const hm = !inCode && line.match(HEADING_RE);
    if (hm) {
      hostLevel = hm[1].length;
      headingStream.push({ sourceDoc: parentBase, text: hm[2].trim() });
    }
    out.push(line);
  }
  return { body: out.join('\n'), headingStream };
}

// Expand `<!-- example: EID -->` tokens in a doc body against the examples map.
// Dictionary host -> inline `*conlang* "translation"`; grammar host -> a simple
// stacked blockquote (conlang / etym / translation). The rich interactive gloss
// (HTML) is a later milestone (roadmap G1); this is the plain transclusion.
export function expandExamples(body, hostRel, examples) {
  const dictionary = hostRel.replace(/\\/g, '/').startsWith('dictionary/');
  const render = (eid, style) => {
    const ex = examples[eid];
    if (!ex) return `**[missing example ${eid}]**`;
    const s = (style || (dictionary ? 'dictionary' : 'grammar')).toLowerCase();
    if (s === 'dictionary') return `*${ex.conlang}* "${ex.translation}"`;
    const etym = ex.segments.map((seg) => seg.etym).join(' ');
    return `\n> *${ex.conlang}*  \n> ${etym}  \n> "${ex.translation}"\n`;
  };
  // Skip fenced code blocks and inline code spans, so prose can mention a token
  // literally (e.g. in `<!-- example: E001 -->`) without it being expanded.
  const out = [];
  let inFence = false;
  for (const line of body.split('\n')) {
    if (FENCE_RE.test(line)) { inFence = !inFence; out.push(line); continue; }
    if (inFence) { out.push(line); continue; }
    out.push(
      line
        .split(/(`[^`]*`)/)
        .map((part) => (part.startsWith('`') ? part : part.replace(EXAMPLE_TOKEN_RE, (_m, eid, style) => render(eid, style))))
        .join('')
    );
  }
  return out.join('\n');
}

function buildFrontmatter(relPath, title) {
  const lines = ['---', `title: ${yamlStr(title)}`];
  const order = ORDER[relPath];
  const label = LABEL[relPath];
  if (order != null || label != null) {
    lines.push('sidebar:');
    if (order != null) lines.push(`  order: ${order}`);
    if (label != null) lines.push(`  label: ${yamlStr(label)}`);
  }
  lines.push('---', '', '');
  return lines.join('\n');
}

async function listMarkdown(dirAbs, relPrefix) {
  let out = [];
  let entries;
  try {
    entries = await readdir(dirAbs, { withFileTypes: true });
  } catch {
    return out;
  }
  for (const e of entries) {
    const rel = relPrefix ? `${relPrefix}/${e.name}` : e.name;
    if (e.isDirectory()) out = out.concat(await listMarkdown(path.join(dirAbs, e.name), rel));
    else if (e.isFile() && e.name.endsWith('.md')) out.push(rel);
  }
  return out;
}

async function run() {
  for (const s of SECTIONS) await rm(path.join(outRoot, s), { recursive: true, force: true });
  await mkdir(genRoot, { recursive: true });

  const headings = {}; // docFilename -> { sectionNumber|EID: slug }

  // Pass 1: read every doc, capture title + heading map + raw body.
  const files = [];
  const rawByBase = {}; // basename -> raw markdown
  for (const section of SECTIONS) {
    for (const rel of await listMarkdown(path.join(docsRoot, section), section)) {
      const md = await readFile(path.join(docsRoot, rel), 'utf8');
      const base = path.basename(rel);
      const title = extractTitle(md, path.basename(rel, '.md'));
      headings[base] = parseHeadings(md);
      rawByBase[base] = md;
      files.push({ rel, base, md, title });
    }
  }

  // Examples corpus (chunk-aligned records), needed to expand `<!-- example: -->`
  // transclusion tokens during Pass 2. Parsed once from the raw body.
  const examplesMap = parseExamples(rawByBase['examples.md'] || '');

  // Identify the assembler parent (the doc carrying `<!-- assemble: -->`
  // directives) and the siblings it inlines. Inlined siblings are NOT written as
  // standalone pages — they live inside the parent's single page.
  let parentRel = null;
  const inlined = new Set();
  for (const f of files) {
    const names = [...f.md.matchAll(/<!--\s*assemble:\s*([A-Za-z0-9_.-]+)\s*-->/g)].map((m) => m[1]);
    if (names.length) {
      parentRel = f.rel;
      names.forEach((n) => inlined.add(n));
    }
  }

  // Pass 2: transform + write. The parent is assembled (siblings inlined); other
  // docs are stripped as-is; inlined siblings are skipped.
  let pages = 0;
  for (const { rel, base, md, title } of files) {
    if (inlined.has(base) || SKIP_PAGE.has(base)) continue;

    let body;
    if (rel === parentRel) {
      const asm = assembleParent(base, md, rawByBase);
      body = asm.body;
      // Re-slug the combined heading stream with one slugger and rebuild the
      // per-doc number/EID maps for the parent + every inlined sibling, so cross
      // refs to those docs resolve to anchors on the assembled page.
      const combinedMaps = {};
      for (const h of slugHeadingStream(asm.headingStream)) {
        const key = headingKey(h.text);
        if (!key) continue;
        (combinedMaps[h.sourceDoc] ||= {})[key] = h.slug;
      }
      for (const [doc, map] of Object.entries(combinedMaps)) headings[doc] = map;
    } else {
      body = stripDoc(md);
    }

    body = expandExamples(body, rel, examplesMap);

    const out = buildFrontmatter(rel, title) + body;
    const destAbs = path.join(outRoot, rel);
    await mkdir(path.dirname(destAbs), { recursive: true });
    await writeFile(destAbs, out, 'utf8');
    pages++;
  }

  const read = (rel) => readFile(path.join(docsRoot, rel), 'utf8');
  const entries = parseDictionary(await read('dictionary/dictionary.md'));
  const glosses = parseGlosses(await read('reference/terminology-registry.md'));
  const examples = examplesMap;

  // entries-by-headword for O(1) lookup in the plugin.
  const entryMap = {};
  for (const e of entries) entryMap[e.headword] = e;

  const artifacts = {
    headings,
    entries: entryMap,
    glosses,
    examples,
  };
  for (const [name, data] of Object.entries(artifacts)) {
    await writeFile(path.join(genRoot, `${name}.json`), JSON.stringify(data, null, 2) + '\n', 'utf8');
  }

  console.log(
    `[build-content] ${pages} pages | ${entries.length} entries | ` +
      `${Object.keys(glosses).length} gloss tags | ${Object.keys(examples).length} examples`
  );
}

// Run only when invoked directly (so the module can be imported for unit tests).
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  run().catch((err) => {
    console.error('[build-content] failed:', err);
    process.exit(1);
  });
}
