// Standalone link-check: reports unresolved §section / §example references in
// the canonical docs, using the same resolution rules as the remark plugin but
// independent of Astro/Vite caching (so the report is always complete).
//
//   node scripts/link-check.mjs           # report, exit 0
//   node scripts/link-check.mjs --strict  # exit 1 if any unresolved refs
//
// Run `npm run content` first so the JSON artifacts are current.

import { readFile, readdir } from 'node:fs/promises';
import { readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const siteRoot = path.resolve(__dirname, '..');
const repoRoot = path.resolve(siteRoot, '..');
const docsRoot = path.join(repoRoot, 'docs');
const genDir = path.join(siteRoot, 'src', 'generated');

const load = (n) => JSON.parse(readFileSync(path.join(genDir, `${n}.json`), 'utf8'));
const HEADINGS = load('headings');
const EXAMPLES = load('examples');

const BARE_FALLBACK = { 'dictionary.md': 'phonology.md' };
const SECTIONS = ['reference', 'dictionary', 'quickref'];

// Strip fenced code blocks and heading lines (the plugin ignores both).
function scannableText(md) {
  const out = [];
  let inCode = false;
  for (const line of md.split(/\r?\n/)) {
    if (/^\s*```/.test(line)) { inCode = !inCode; continue; }
    if (inCode) continue;
    if (/^#{1,6}\s/.test(line)) continue;
    out.push(line);
  }
  return out.join('\n');
}

function resolveBare(docFile, num) {
  if (HEADINGS[docFile]?.[num]) return true;
  const fb = BARE_FALLBACK[docFile];
  return Boolean(fb && HEADINGS[fb]?.[num]);
}

async function listMd(dir, prefix) {
  let out = [];
  let entries;
  try { entries = await readdir(dir, { withFileTypes: true }); } catch { return out; }
  for (const e of entries) {
    const rel = prefix ? `${prefix}/${e.name}` : e.name;
    if (e.isDirectory()) out = out.concat(await listMd(path.join(dir, e.name), rel));
    else if (e.name.endsWith('.md')) out.push(rel);
  }
  return out;
}

async function run() {
  const strict = process.argv.includes('--strict');
  const report = {}; // docFile -> Map(ref -> count)
  let total = 0;

  for (const section of SECTIONS) {
    for (const rel of await listMd(path.join(docsRoot, section), section)) {
      const docFile = path.basename(rel);
      const text = scannableText(await readFile(path.join(docsRoot, rel), 'utf8'));
      const misses = new Map();
      const miss = (ref) => { misses.set(ref, (misses.get(ref) || 0) + 1); total++; };

      // Cross-doc `file.md §X` (plain text or backtick — backticks survive as text here).
      const seen = new Set();
      for (const m of text.matchAll(/`?([A-Za-z][\w-]*\.md)`?\s+§\s?(\d+(?:\.\d+)*[a-z]?)/g)) {
        seen.add(m.index);
        if (!HEADINGS[m[1]]?.[m[2]]) miss(`${m[1]} §${m[2]}`);
      }
      // Example refs.
      for (const m of text.matchAll(/§\s?(E\d{3})/g)) {
        if (!EXAMPLES[m[1]]) miss(`§${m[1]}`);
      }
      // Bare section refs (skip those already consumed by a cross-doc match).
      for (const m of text.matchAll(/§\s?(\d+(?:\.\d+)*[a-z]?)/g)) {
        // crude: skip if a `.md §` precedes immediately
        const before = text.slice(Math.max(0, m.index - 40), m.index);
        if (/\.md`?\s*$/.test(before)) continue;
        if (!resolveBare(docFile, m[1])) miss(`§${m[1]}`);
      }

      if (misses.size) report[docFile] = misses;
    }
  }

  const docs = Object.keys(report).sort();
  if (!docs.length) {
    console.log('[link-check] ✓ all §section / §example references resolve.');
    return;
  }
  console.log(`[link-check] ${total} unresolved reference(s) across ${docs.length} document(s):\n`);
  for (const doc of docs) {
    const misses = report[doc];
    const items = [...misses.entries()].sort((a, b) => b[1] - a[1]);
    console.log(`  ${doc} (${[...misses.values()].reduce((a, b) => a + b, 0)}):`);
    for (const [ref, n] of items) console.log(`    ${ref}${n > 1 ? ` ×${n}` : ''}`);
    console.log('');
  }
  console.log(
    'Many of these are expected while language_reference.md is mid-assembly-refactor\n' +
      '(bare refs to verbal-system sections that the assembler will inline). Resolve as\n' +
      'the assembly model lands; genuine typos show up here too.'
  );
  if (strict) process.exit(1);
}

run().catch((err) => {
  console.error('[link-check] failed:', err);
  process.exit(1);
});
