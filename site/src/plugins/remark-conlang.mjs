// remark plugin: turns the conlang's plain-text cross-reference conventions into
// resolved links, and attaches hover-card data for dictionary / gloss / example
// references. Consumes the JSON artifacts emitted by scripts/build-content.mjs.
//
// Reference forms handled (see CLAUDE.md "Cross-references"):
//   - `*headword*`         italic conlang form that exactly matches a dictionary
//                          headword            -> dictionary entry + hover-card
//   - `file.md §4.1`       cross-document section reference (plain text)
//   - `§4.1`               bare section reference -> resolves within current doc
//   - `§E001`              example reference   -> examples page + hover-card
//   - VOL, LVC.VOL.HAB     registered gloss tags (composites split on `.`)
//                          -> glossary + hover-card
//
// Unresolved §/example references are reported to stderr (the link-check pass).

import { readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { findAndReplace } from 'mdast-util-find-and-replace';
import { visit } from 'unist-util-visit';

const genDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', 'generated');
const load = (name) => {
  try {
    return JSON.parse(readFileSync(path.join(genDir, `${name}.json`), 'utf8'));
  } catch {
    console.warn(`[conlang-links] missing artifact ${name}.json — run 'npm run content' first; links disabled.`);
    return {};
  }
};

const HEADINGS = load('headings'); // docFile -> { sectionNumber|EID: slug }
const ENTRIES = load('entries'); //   headword -> { slug, pos, ipa, foot, shortDef }
const GLOSSES = load('glosses'); //   tag -> { term, def, slug }
const EXAMPLES = load('examples'); // EID -> { conlang, translation, slug }

// Must match `base` in astro.config.mjs.
const BASE = '/ref_grammar';

// phonology / orthography / verbal-system are inlined into the language_reference
// page (see scripts/build-content.mjs assembleParent), so refs to them resolve to
// anchors on that single page rather than standalone pages.
const ASSEMBLED_PAGE = '/reference/language_reference/';
const DOC_URL = {
  'language_reference.md': ASSEMBLED_PAGE,
  'phonology.md': ASSEMBLED_PAGE,
  'orthography.md': ASSEMBLED_PAGE,
  'verbal-system.md': ASSEMBLED_PAGE,
  'examples.md': '/reference/examples/',
  'terminology-registry.md': '/reference/terminology-registry/',
  'dictionary.md': '/dictionary/dictionary/',
  'phonology-quickref.md': '/quickref/phonology-quickref/',
  'orthography-quickref.md': '/quickref/orthography-quickref/',
  'dictionary-index.md': '/quickref/dictionary-index/',
};

// When a bare `§X` doesn't resolve in the current document, fall back to a
// conventional sibling. The dictionary cites phonology rules as bare `§4.4.1`.
const BARE_FALLBACK = { 'dictionary.md': 'phonology.md' };

const url = (docFile, slug) => `${BASE}${DOC_URL[docFile]}${slug ? `#${slug}` : ''}`;

function linkNode(href, children, className, card) {
  const hProperties = { className };
  if (card) {
    hProperties['data-card-title'] = card.title;
    hProperties['data-card-body'] = card.body;
  }
  return {
    type: 'link',
    url: href,
    title: null,
    data: { hProperties },
    children,
  };
}

const textRun = (value) => ({ type: 'text', value });

// A non-link inline span carrying hover-card data — for references whose target
// has no page (examples.md is build-time source only). Rendered as <span> via the
// mdast hName escape hatch; hovercard.js binds to `.cl-ref[data-card-title]`.
function cardSpan(children, className, card) {
  const hProperties = { className, tabindex: '0' };
  if (card) {
    hProperties['data-card-title'] = card.title;
    hProperties['data-card-body'] = card.body;
  }
  return { type: 'emphasis', data: { hName: 'span', hProperties }, children };
}

function emphasisText(node) {
  let s = '';
  visit(node, 'text', (t) => {
    s += t.value;
  });
  return s;
}

export default function remarkConlang() {
  return (tree, file) => {
    const docFile = path.basename(file.path || file.history?.[0] || '');
    const docHeadings = HEADINGS[docFile] || {};
    const dangling = [];

    // 1. Dictionary headwords: italic conlang forms that exactly match a headword.
    //    Replace the emphasis node with a link wrapping it (preserves italics).
    visit(tree, 'emphasis', (node, index, parent) => {
      if (!parent || index == null) return;
      if (parent.type === 'link') return; // already linked
      const word = emphasisText(node).trim();
      const entry = ENTRIES[word];
      if (!entry) return;
      const card = {
        title: word,
        body: [entry.pos, entry.ipa].filter(Boolean).join(' · ') +
          (entry.shortDef ? ` — ${entry.shortDef}` : ''),
      };
      const link = linkNode(url('dictionary.md', entry.slug), [node], ['cl-ref', 'cl-dict'], card);
      parent.children[index] = link;
      return ['skip', index + 1];
    });

    // 2. Cross-document refs where the filename is a code span: `phonology.md` §4.1.
    //    These span two sibling nodes (inlineCode + text), so findAndReplace
    //    (which sees one text node at a time) can't catch them.
    visit(tree, (node) => {
      const kids = node.children;
      if (!Array.isArray(kids)) return;
      for (let i = 0; i < kids.length - 1; i++) {
        const a = kids[i];
        const b = kids[i + 1];
        if (a.type !== 'inlineCode' || !/^[\w-]+\.md$/.test(a.value) || b.type !== 'text') continue;
        const m = b.value.match(/^(\s*)§\s?(\d+(?:\.\d+)*[a-z]?)/);
        if (!m) continue;
        const fileRef = a.value;
        const slug = HEADINGS[fileRef]?.[m[2]];
        if (!slug) {
          dangling.push(`${fileRef} §${m[2]}`);
          continue;
        }
        const replacement = [textRun(m[1]), linkNode(url(fileRef, slug), [textRun(`§${m[2]}`)], ['cl-ref', 'cl-section'])];
        const rest = b.value.slice(m[0].length);
        if (rest) replacement.push(textRun(rest));
        kids.splice(i + 1, 1, ...replacement);
        i += replacement.length - 1;
      }
    });

    // 3. Text-node reference patterns, in priority order.
    findAndReplace(
      tree,
      [
        // Cross-document section reference: `phonology.md §4.1`
        [
          /([A-Za-z][\w-]*\.md)\s+§\s?(\d+(?:\.\d+)*[a-z]?)/g,
          (whole, fileRef, num) => {
            const slug = HEADINGS[fileRef]?.[num];
            if (!slug) {
              dangling.push(`${fileRef} §${num}`);
              return false;
            }
            return [textRun(`${fileRef} `), linkNode(url(fileRef, slug), [textRun(`§${num}`)], ['cl-ref', 'cl-section'])];
          },
        ],
        // Example reference: `§E001`. examples.md has no page (build-time source
        // only), so this is a hover-card span, not a link.
        [
          /§\s?(E\d{3})/g,
          (whole, eid) => {
            const ex = EXAMPLES[eid];
            if (!ex) {
              dangling.push(`§${eid}`);
              return false;
            }
            const card = {
              title: eid,
              body: `${ex.conlang} ${ex.translation}`.trim(),
            };
            return cardSpan([textRun(`§${eid}`)], ['cl-ref', 'cl-example'], card);
          },
        ],
        // Registered gloss tags (composite split on `.`).
        [
          /\b[A-Z][A-Z]+(?:\.[A-Z]+)*\b/g,
          (whole) => {
            const parts = whole.split('.');
            if (!parts.some((p) => GLOSSES[p])) return false; // none registered
            const out = [];
            parts.forEach((p, i) => {
              if (i > 0) out.push(textRun('.'));
              const g = GLOSSES[p];
              if (g) {
                out.push(
                  linkNode(url('terminology-registry.md', g.slug), [textRun(p)], ['cl-ref', 'cl-gloss'], {
                    title: g.term,
                    body: g.def,
                  })
                );
              } else {
                out.push(textRun(p));
              }
            });
            return out;
          },
        ],
        // Bare section reference: resolve within the current document, then
        // against the document's conventional fallback sibling.
        [
          /§\s?(\d+(?:\.\d+)*[a-z]?)/g,
          (whole, num) => {
            if (docHeadings[num]) {
              return linkNode(url(docFile, docHeadings[num]), [textRun(`§${num}`)], ['cl-ref', 'cl-section']);
            }
            const fb = BARE_FALLBACK[docFile];
            if (fb && HEADINGS[fb]?.[num]) {
              return linkNode(url(fb, HEADINGS[fb][num]), [textRun(`§${num}`)], ['cl-ref', 'cl-section']);
            }
            dangling.push(`§${num} (in ${docFile})`);
            return false;
          },
        ],
      ],
      { ignore: ['heading', 'link'] }
    );

    if (dangling.length) {
      console.warn(`[conlang-links] ${docFile}: ${dangling.length} unresolved ref(s): ${dangling.join('; ')}`);
    }
  };
}
