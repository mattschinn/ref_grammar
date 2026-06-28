# Roadmap: Centralized Examples System

**Status:** active · **Opened:** 2026-06-26 · **Owner:** author (Matt) + Claude

A multi-session plan to turn `examples.md` from a one-entry scaffold into the single source of truth for glossed example sentences — authored once, transcluded into the dictionary and reference grammar at build time, and grown over time with richer assets. Check tasks off as they land; the **Current focus** pointer says what's next.

How to use: tasks are `- [ ]` (todo) / `- [x]` (done). Keep the **Decisions locked** section authoritative so later sessions don't relitigate settled calls. When a milestone closes, note the date next to its heading.

---

## Why centralize (the load-bearing reasons)

Settled after weighing inline-vs-central. Inline authoring cannot give these; a central corpus can:

1. **Update propagation.** The conlang shifts constantly. Inline examples rot and must be hunted across docs; a central source re-propagates every citation on the next build from one edit.
2. **Amortizing expensive per-example assets.** Audio recordings, deep annotations, and footnotes are costly to produce once and worthless to duplicate. Created against an E-ID, every transcluding surface inherits them.
3. **Corpus-level operations.** Tag-and-enumerate all examples to audit which grammatical functions are under-demonstrated and drive a backlog (Milestones C–D).

The cost worry is real but mis-aimed: **centralization is cheap; the rich rendering is the expensive part, and they're separable.** Milestone A delivers the benefits above with minimal machinery; the fancy rendering (G) and rich assets (H) are deferred and incremental.

---

## Decisions locked

- **Centralize** examples in `examples.md` as the single source of truth. ✔
- **Alignment:** conlang ↔ pseudo-etymological lines are chunked and aligned (interactive on the site); the GA translation stays a **free line** (not chunked). No traditional Leipzig line yet (labels unsettled).
- **Chunk delimiter:** `|`. Aligned lines must have **equal chunk counts**; the parser errors loudly on mismatch.
- **`examples.md` is backend-only.** Not published as an HTML page, not a PDF chapter — it exists solely as the transclusion source.
- **`§E001` inline mentions** become **hovercard-only** (no link target, since there's no examples page). The block token `<!-- example: E001 -->` is what renders an example in place.
- **Open-schema record.** The per-example JSON record is extensible from day one, so `audio:`, `notes:`, `footnotes:` slot in later with zero migration.
- **Draft-import bar (for Milestone B2):** import each `/drafts` sentence as `[Provisional]` with a pointer to its source draft; reconcile spelling/IPA against current `phonology.md`/`orthography.md`; stub-check words against `dictionary.md`; never let a draft's old form overwrite current canon (flag conflicts, don't resolve); author reviews each before it lands.
- **Grammar-example tokenization is deferred (decided 2026-06-28, B1, "Option A").** The grammar examples' visible payload is the Leipzig interlinear (which the format defers from display), and their primary Etymological gloss line cannot be authored until the source words land (dictionary batch D4). So B1 **centralizes the data now** but **leaves the inline prose copies in place**; the `<!-- example: -->` token swap waits on D4 (to author Etymological lines) and/or a grammar renderer that emits the preserved interlinear (Milestone G). Tokenizing earlier would replace rich interlinears with thinner conlang+translation blocks.

Maps to the author's original nine items: #1→A1 · #4→A2+G · #2→B1 · #3→B2 · #5→C · #6→D1 · #7→D2 · #8→E · #9→F.

---

## Current focus

➡ **Milestone A COMPLETE. B1 data-port COMPLETE (2026-06-28); B1 tokenization deferred (Option A).** The 16 grammar examples are centralized in `examples.md` (E002–E017), two cross-doc duplicates collapsed, inline prose copies retained. The token swap (B1b) is parked behind the D4 dictionary batch. Next live task: **B2** (import `/drafts` translation exercises per the draft-import bar) or **C1** (codify examples pacing) — both author-facing.

---

## Milestone A — Centralization core (Slice 1) — the cheap, high-value foundation

Delivers propagation + reuse. Everything below A depends on A1.

- [x] **A1. Data model.** ✓ 2026-06-26. `examples.md` §2/§6 rewritten to the `|`-chunked, open-schema, build-time-source format; `parseExamples` now emits `{conlang, segments[], ipa, translation, tags, slug}` with a loud equal-count guard (verified to throw); E001 re-encoded to 8 aligned segments; `examples.json` shape confirmed.
- [x] **A2. Plain transclusion.** ✓ 2026-06-26. `<!-- example: EID -->` token (style auto-resolves by host doc, overridable as `| dictionary`) expanded in all three render paths: site (`build-content.mjs` `expandExamples`), grammar PDF (`build.ps1`), dictionary PDF (`build-dictionary.ps1`). Dictionary = inline `*conlang* "translation"`; grammar = stacked blockquote. `examples.md` page removed (compiler `SKIP_PAGE`; 7→6 pages); `§EID` now a hover-card span (`remark-conlang.mjs` `cardSpan`). Site verified by running the compiler; PDF verified at the logic level (parse+expand), not a full pandoc/tectonic run. Known minor edge: the dead `DOC_URL['examples.md']` entry would dead-link if a doc ever cross-refs an `examples.md §<number>` section (none do today).
- [x] **A3. Enforce SSOT.** ✓ 2026-06-26. `example-adder` Step 5 (Cases B/C) + Step 4 rewritten to emit `<!-- example: EID -->` tokens, never paste example text. E001's inline copy in the *ŕe* entry migrated to a token; dictionary entry-format note + a changelog entry added. `parseDictionary` now strips the token from the hover-card short-def (verified: *ŕe* → "(adv.) today."). **Also fixed an A2 bug:** all three expanders now skip fenced code + inline code spans, so a token can be documented literally (e.g. the changelog) without expanding — verified bare-expands / code-literal in JS and PowerShell.
- [x] **A4. Register the change.** ✓ 2026-06-26. `CLAUDE.md` updated: `examples.md` described as a build-time transclusion source (not a published sibling), `example-adder` skill-table row notes the token mechanism. Versioning already covered by examples.md v0.2 + the dictionary changelog. **Milestone A complete.**

## Milestone B — Corpus population (needs A1)

- [x] **B1a. Port existing grammar examples (data).** ✓ 2026-06-28. Swept `verbal-system.md` + `ideophones.md` for standalone glossed blocks; ported 16 as **E002–E017** preserving Conlang (chunked), IPA, Leipzig, χ gesture, Translation, and `[Placeholder]` caveats (→ Notes). Collapsed the two cross-doc duplicates (E003, E010) to single records. GA-English paraphrases and all-placeholder skeletons (§4.3, §15) excluded. Etymological lines deferred (D4). `examples.md` v0.3; parser + site compiler verified (17 examples, no guard trip). Inline prose copies **retained**.
- [ ] **B1b. Tokenize grammar examples (prose).** Deferred (Option A). Replace the retained inline blocks with `<!-- example: EXXX -->` tokens once the Etymological lines can be authored (D4) and/or the grammar renderer emits the preserved interlinear (G). Until then the inline copies stand and `examples.md` is the flagged single source.
- [ ] **B2. Import draft translations.** Carefully promote `/drafts` translation-exercise sentences into `examples.md` per the locked draft-import bar. Author reviews each before it lands.

## Milestone C — Editorial standard (needs `data/writing-style-references`)

- [ ] **C1. Codify examples pacing.** Mine the reference papers for how strong linguistics writing paces examples against argument; write the principle into the `writing-style` skill (fits its register-caveat / Part-5 structure).

## Milestone D — Coverage audit & worklist (needs B + C)

- [ ] **D1. Audit.** Walk the grammar with the C1 principle; mark where arguments are under-exemplified.
- [ ] **D2. Worklist.** Produce a structured list of needed example/gloss sentences, each keyed to the grammatical function it must demonstrate. Author takes this **offline** to write.

## Milestone E — Coordinated-ingestion skill (needs A)

- [ ] **E1. Orchestrator skill.** Formalize the multi-doc fan-out: a new sentence may carry new grammar (→ reference docs), new words (→ `dictionary-updater` stub), new sound rules (→ flag for phonology), plus the example (→ `examples.md`) and its tokens. Build over `example-adder` / `dictionary-updater` with propagation rules baked in.

## Milestone F — Run the loop (needs E + author's offline work)

- [ ] **F1. Ingest.** Feed the author's offline-written examples through the E1 skill, coordinated across docs.

## Milestone G — Rendering polish (Slice 2) — deferred, presentation-only

- [ ] **G1. HTML interactive gloss.** Color-coded, hover-linked chunk alignment (extend `hovercard.js` + a transform). Conlang ↔ etym highlight on hover, distinct color per chunk.
- [ ] **G2. PDF grammar gloss.** Deterministic monospace column padding (measure *display* width, not codepoint count — diacritics/IPA misalign on naïve length).

## Milestone H — Rich assets (Slice 3) — future

- [ ] **H1. Audio.** Add an `audio:` field + asset pipeline; renderers opt in.
- [ ] **H2. Annotations.** Add `notes:` / `footnotes:` fields; renderers opt in.

---

## Dependency map

```
A1 ─┬─ A2 ─ A3 ─ A4        (core; do first)
    ├─ B1, B2              (population; parallel after A1)
    ├─ E1 ─ F1             (skill, then loop)
    └─ G1, G2              (polish; deferred)
C1 ─ D1 ─ D2               (editorial; D needs B + C)
H1, H2                     (future; need A1's open schema)
```

## Session log

- 2026-06-26 — Roadmap opened. Decisions locked (centralize; conlang↔etym interactive + free translation; `|` delimiter; backend-only; open schema; draft-import bar). Phase-0 format + `examples.json` shape specced and agreed.
- 2026-06-26 — **A1 done.** `examples.md` v0.2 (chunk-aligned, open-schema, build-time-source), `parseExamples` rewritten + equal-count guard, E001 re-encoded. Parser verified against the live doc (8 segments) and the guard verified to throw on mismatch. Touched: `docs/reference/examples.md`, `site/scripts/parse.mjs`. Committed (ded5e50). Next: A2.
- 2026-06-26 — **A2 done.** `<!-- example: EID -->` transclusion live in all three render paths (site + both PDF builds), `examples.md` page removed, `§EID` → hover-card span. Expansion verified in JS and PowerShell; both PDF scripts syntax-checked; site compiler re-run clean (6 pages). Touched: `site/scripts/build-content.mjs`, `site/src/plugins/remark-conlang.mjs`, `pdf/build.ps1`, `pdf/build-dictionary.ps1`. Committed (ce34165). Next: A3.
- 2026-06-26 — **A3 done.** SSOT enforced: `example-adder` emits tokens; E001's *ŕe* inline copy migrated to a token; `parseDictionary` strips the token from short-defs. Fixed an A2 code-span bug (all three expanders now skip code fences/spans). Verified by rebuild ("chillier" appears once; changelog token stays literal) + PS behavior test. Touched: `site/scripts/parse.mjs`, `site/scripts/build-content.mjs`, `pdf/build.ps1`, `pdf/build-dictionary.ps1`, `docs/dictionary/dictionary.md`, `.claude/skills/example-adder/SKILL.md`. Committed (d0f0ad8).
- 2026-06-28 — **B1a done (data port); B1b deferred (Option A).** Swept the reference docs: 16 standalone glossed blocks ported into `examples.md` as E002–E017 (v0.3), two cross-doc duplicates (E003, E010) collapsed, Gesture (χ) + deferred-Etymological conventions + 9 tags added. Decision recorded: tokenizing now would drop the visible Leipzig interlinear and the etym line can't be authored pre-D4, so inline prose copies are retained and the token swap waits (Decisions-locked + B1b). Verified: parseExamples ingests 17 with no equal-chunk trip; site compiler clean (6 pages, 17 examples). Touched: `docs/reference/examples.md`. Docs unchanged. Next: B2 or C1.
- 2026-06-26 — **A4 done. MILESTONE A COMPLETE.** `CLAUDE.md` records examples.md as backend-only transclusion source + the token mechanism in the skill table. The centralized-examples infrastructure (data model → transclusion → SSOT enforcement) is fully in place. Remaining: content/editorial milestones B–F and deferred rendering G/H. PDF expansion still unverified by a real pandoc/tectonic run (logic-verified only).
