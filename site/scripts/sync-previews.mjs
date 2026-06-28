// Preview auto-regeneration (roadmap G0b). Rewrites the canonical docs in place so
// that every `<!-- example: EID | spec -->` token is followed by a regenerated
// preview block — the on-disk, SSOT-deferring rendered copy authors see while
// editing prose, and the exact markdown both builds emit (after stripExamples).
//
// Unidirectional: examples.md → docs. The preview never feeds back. Idempotent:
// re-running replaces existing previews rather than stacking them.
//
// Runs automatically at the start of build-content.mjs (so the site build, dev
// server, and PDF builds all refresh previews); also runnable standalone:
//   node scripts/sync-previews.mjs

import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { parseExamples } from './parse.mjs';
import { syncBody, hostOf } from './examples-render.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..', '..');
const docsRoot = path.join(repoRoot, 'docs');

// examples.md is the source — never a transclusion host (and it documents the token
// literally), so it is excluded from the sweep.
const SKIP = new Set(['examples.md']);

async function listMarkdown(dirAbs) {
  let out = [];
  let entries;
  try {
    entries = await readdir(dirAbs, { withFileTypes: true });
  } catch {
    return out;
  }
  for (const e of entries) {
    const abs = path.join(dirAbs, e.name);
    if (e.isDirectory()) out = out.concat(await listMarkdown(abs));
    else if (e.isFile() && e.name.endsWith('.md') && !SKIP.has(e.name)) out.push(abs);
  }
  return out;
}

// Refresh previews across all docs. Returns the number of files changed.
export async function syncPreviews({ root = docsRoot, examples } = {}) {
  const map = examples || parseExamples(await readFile(path.join(docsRoot, 'reference', 'examples.md'), 'utf8'));
  let changed = 0;
  for (const abs of await listMarkdown(root)) {
    const rel = path.relative(root, abs);
    const before = await readFile(abs, 'utf8');
    if (!/<!--\s*example:/.test(before)) continue; // no tokens — skip untouched
    const after = syncBody(before, hostOf(rel), map);
    if (after !== before) {
      await writeFile(abs, after, 'utf8');
      changed++;
    }
  }
  return changed;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  syncPreviews()
    .then((n) => console.log(`[sync-previews] refreshed previews in ${n} file(s)`))
    .catch((err) => {
      console.error('[sync-previews] failed:', err);
      process.exit(1);
    });
}
