// Shared example-rendering core (roadmap G0a/G0b). Imported by both the content
// compiler (build-content.mjs) and the preview-sync step (sync-previews.mjs), so
// there is exactly ONE renderer. A `<!-- example: EID | spec -->` token transcludes
// an examples.md record; `renderExample` turns the record into markdown, choosing
// which layers to show; `buildToken` wraps a token with its regenerated preview;
// `stripExamples` collapses token+preview back to just the rendered content (what a
// build emits). The preview is the on-disk, SSOT-deferring copy authors edit beside.

const EX_LAYERS = ['conlang', 'etym', 'ipa', 'leipzig', 'gesture', 'translation'];
const EX_PRESETS = new Set(['dictionary', 'grammar']);

const FENCE_RE = /^\s*```/;

// Token: `<!-- example: E001 -->` with optional `| spec` (preset / whitelist /
// blacklist). The spec capture grabs everything between `|` and `-->`.
export const EXAMPLE_TOKEN_RE = /<!--\s*example:\s*(E\d{3})\s*(?:\|\s*([^>]*?)\s*)?-->/g;

// A field counts as absent if empty, a dash/slash placeholder (`/—/`, `—`), or a
// "pending …" note — so a not-yet-filled IPA/etym never renders.
const isPlaceholderVal = (s) => !s || /pending/i.test(s) || /^[\s/—–-]*$/.test(s);

const exEtym = (ex) => (ex.segments || []).map((s) => s.etym).join(' ').trim();

// Layers a record actually has content for, in canonical order.
function presentLayers(ex) {
  const has = {
    conlang: !!(ex.conlang && ex.conlang.trim()),
    etym: !!exEtym(ex),
    ipa: !isPlaceholderVal(ex.ipa),
    leipzig: !!(ex.leipzig && ex.leipzig.trim()),
    gesture: !!(ex.gesture && ex.gesture.trim()),
    translation: !!(ex.translation && ex.translation.trim()),
  };
  return EX_LAYERS.filter((l) => has[l]);
}

// Resolve a token's `| spec` against host + present layers → { layers, inline }.
export function resolveExampleSpec(spec, host, present) {
  const tokens = (spec || '').trim().split(/\s+/).filter(Boolean);
  const presets = tokens.filter((t) => EX_PRESETS.has(t));
  const bare = tokens.filter((t) => EX_LAYERS.includes(t));
  const neg = tokens.filter((t) => t.startsWith('-') && EX_LAYERS.includes(t.slice(1))).map((t) => t.slice(1));
  const preset = presets[0] || (host === 'dictionary' ? 'dictionary' : 'grammar');

  let layers;
  if (bare.length) {
    layers = EX_LAYERS.filter((l) => bare.includes(l) && present.includes(l));
    if (!layers.includes('conlang') && present.includes('conlang')) layers = ['conlang', ...layers];
  } else if (preset === 'dictionary') {
    layers = ['conlang', 'translation'].filter((l) => present.includes(l));
  } else {
    layers = present.slice();
  }
  if (neg.length) layers = layers.filter((l) => l === 'conlang' || !neg.includes(l));

  // Inline form when the dictionary preset is in force, or only conlang/translation survive.
  const inline = preset === 'dictionary' || layers.every((l) => l === 'conlang' || l === 'translation');
  return { layers, inline };
}

function renderExampleLayer(ex, layer) {
  switch (layer) {
    case 'conlang': return `*${ex.conlang}*`;
    case 'etym': return exEtym(ex);
    case 'ipa': return ex.ipa;
    case 'leipzig': return ex.leipzig;
    case 'gesture': return `χ ${ex.gesture}`;
    case 'translation': return `"${ex.translation}"`;
    default: return '';
  }
}

// Render an example record for transclusion. host = 'dictionary' | 'grammar'.
// Inline → `*conlang* "translation"` (flows in prose); block → a stacked blockquote
// (leading + trailing newline). The block/inline shape also drives preview placement.
export function renderExample(ex, spec, host) {
  if (!ex) return null;
  const { layers, inline } = resolveExampleSpec(spec, host, presentLayers(ex));
  if (!layers.length) return `*${ex.conlang || ''}*`;
  if (inline) {
    const out = [];
    if (layers.includes('conlang')) out.push(`*${ex.conlang}*`);
    if (layers.includes('translation')) out.push(`"${ex.translation}"`);
    return out.join(' ');
  }
  return `\n${layers.map((l) => `> ${renderExampleLayer(ex, l)}  `).join('\n')}\n`;
}

export const hostOf = (rel) => (rel.replace(/\\/g, '/').includes('dictionary/') ? 'dictionary' : 'grammar');

// Build the canonical `token + preview` text for a record. The preview is the
// rendered markdown wrapped in `<!-- preview … -->` / `<!-- /preview -->`, placed
// inline (after an inline render) or on its own lines (after a block render). The
// build later collapses this back to just the rendered content (stripExamples).
export function buildToken(eid, spec, host, ex) {
  const token = `<!-- example: ${eid}${spec ? ` | ${spec}` : ''} -->`;
  const open = `<!-- preview ${eid} · auto-generated from examples.md · do not edit -->`;
  const close = `<!-- /preview -->`;
  const rendered = ex ? renderExample(ex, spec, host) : `**[missing example ${eid}]**`;
  // Block renders start with a newline; give the preview its own lines.
  if (rendered.startsWith('\n')) return `${token}\n${open}${rendered}${close}`;
  return `${token}${open}${rendered}${close}`;
}

// Apply `fn` to text outside fenced code blocks and inline code spans, so a token
// can be documented literally (in a code fence/span) without being touched. Unlike
// a line-by-line pass, this hands fn each non-code region as a MULTI-LINE string, so
// a regex can match a block preview that spans several lines.
function outsideCode(body, fn) {
  const lines = body.split('\n');
  const out = [];
  let inFence = false;
  let buf = [];
  const flush = () => {
    if (!buf.length) return;
    // Within a non-code region, still protect single-line inline code spans.
    const text = buf.join('\n');
    out.push(text.split(/(`[^`\n]*`)/).map((p) => (p.startsWith('`') ? p : fn(p))).join(''));
    buf = [];
  };
  for (const line of lines) {
    if (FENCE_RE.test(line)) { flush(); out.push(line); inFence = !inFence; continue; }
    if (inFence) { out.push(line); continue; }
    buf.push(line);
  }
  flush();
  return out.join('\n');
}

// Match a token plus its (optional) existing preview, so sync can replace the
// preview and the build can collapse the pair. Group 1 = eid, 2 = spec, 3 = the
// preview region (incl. markers) if present. Multiline: a block preview spans lines.
const TOKEN_WITH_PREVIEW = /<!--\s*example:\s*(E\d{3})\s*(?:\|\s*([^>]*?)\s*)?-->([ \t]*\n?<!--\s*preview\b[^>]*-->[\s\S]*?<!--\s*\/preview\s*-->)?/g;

// Regenerate (or insert) the preview after every token in `body`, from `examples`.
// host is derived from the doc's path. Code fences/spans are skipped.
export function syncBody(body, host, examples) {
  return outsideCode(body, (segment) =>
    segment.replace(TOKEN_WITH_PREVIEW, (_m, eid, spec) => buildToken(eid, (spec || '').trim() || null, host, examples[eid]))
  );
}

// Collapse `token + preview` to just the rendered content (the preview body). This
// is what a build emits: the on-disk preview IS the render, so the build needs no
// renderer — only this strip. Code fences/spans are skipped.
export function stripExamples(body) {
  return outsideCode(body, (segment) =>
    segment.replace(
      /<!--\s*example:[^>]*-->[ \t]*\n?<!--\s*preview\b[^>]*-->([\s\S]*?)<!--\s*\/preview\s*-->/g,
      '$1'
    )
    // A bare token with no preview yet (e.g. just authored, pre-sync): leave a marker.
    .replace(EXAMPLE_TOKEN_RE, (_m, eid) => `**[example ${eid} — run preview sync]**`)
  );
}
