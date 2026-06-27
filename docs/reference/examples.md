# Examples

**Version:** v0.2 (June 2026)
**Status:** Sibling reference document, parallel to `phonology.md`, `orthography.md`, `verbal-system.md`, and `dictionary.md`. Holds a single source of truth for glossed example sentences; other reference documents and dictionary entries cite by ID rather than reproducing glosses inline.

A working corpus of glossed example sentences in the conlang. Each entry is a numbered, dated block with five gloss layers (Conlang, IPA, Etymological, Leipzig, Translation) plus metadata. The corpus is not a translation set or a teaching grammar — it is a record of material that surfaced something interesting about phonology, morphology, syntax, or pragmatics, retained so the observation is recoverable later.

---

## 1. Purpose

Centralizing examples serves three ends:

1. **Single source of truth.** A given sentence is fully glossed in exactly one place. Dictionary entries and grammar discussions reference the entry by ID (`examples.md §E001`); they do not duplicate the gloss.
2. **LLM-feedable context.** A flat, structured corpus is easier to load as context than examples scattered across siblings.
3. **Diachronic record.** Entries are dated at creation, and substantive revisions to an entry are logged inside the entry. The corpus doubles as a record of how analysis has shifted — useful when a gloss is revised because of a downstream phonology or grammar decision.

---

## 2. Entry format

Each entry is a Markdown subsection headed `### EXXX {#EXXX}` (the explicit anchor enables stable linking) with the following fields, in order:

- **Conlang** — orthographic surface form, sentence-cased and punctuated as written. **Chunked with `|`** into alignment units (see *Chunk alignment* below); each chunk carries its own trailing punctuation.
- **Etymological** — word-for-word English etymological transcription, **chunked with `|` in lockstep with the Conlang line**: equal chunk counts, and chunk *i* glosses Conlang chunk *i*. See §3 for within-chunk notation.
- **IPA** — broad phonemic transcription. Use `‖` for sentence break, `|` for clause break, `.` for syllable break only where ambiguous. Stress marked with `ˈ`. Conform to `phonology.md` §4. This is a **free** line — *not* chunked; a `|` here is a clause break, never an alignment delimiter.
- **Leipzig** — *(deferred)* standard Leipzig interlinear gloss. Held dormant: the gloss labels/terms have not settled, so no renderer emits this line yet. Existing Leipzig lines are preserved but not displayed; omit on new entries until the gloss inventory is committed.
- **Translation** — idiomatic English translation in double quotes. A **free** line (not chunked); rendered whole beneath the gloss.
- **Tags** — `#`-prefixed keywords for grouping (phenomena, semantic fields, constructions). See §4.
- **Cited from** — backlinks to siblings or dictionary entries that reference this example. Maintained manually; `—` if none.
- **Added** — ISO date (YYYY-MM-DD) of first inclusion.
- **Revised** — dated bullets describing substantive changes to the entry. Use `—` until first revision. Format: `- YYYY-MM-DD: <what changed and why>`. Trivial fixes (typos, formatting) do not require an entry.
- **Notes** — optional. Open questions, contested glosses, layer-confidence flags, pointers to the discussion that generated the example.

IDs are assigned sequentially and zero-padded to three digits (`E001`, `E002`, …). They are stable and never reused, even if an entry is retired. A retired entry's block is kept in place with the body replaced by `**Retired YYYY-MM-DD:** <reason>` and the original content moved to the Revised log.

**Chunk alignment.** The Conlang and Etymological lines are split on `|` into aligned chunks — chunk *i* of one corresponds to chunk *i* of the other. A chunk is the unit a renderer highlights (HTML hover) or pads into a column (PDF). The build **requires equal chunk counts** on the two lines and fails the build loudly on a mismatch. Keep chunks at a sensible grain — usually one conlang word and its etymological gloss — and let punctuation ride with its chunk (`noê.`). The Translation and IPA lines are free; they are never chunked.

**Open schema.** The fields above are the current set, but a record is **extensible**: later milestones may add fields (e.g. `Audio`, per-chunk `Notes`/`Footnotes`) without changing existing entries. Parsers ignore fields they don't recognize.

**This document is build-time source only.** It is not published as an HTML page or a PDF chapter. Citing documents pull examples in at compile time via the `<!-- example: EXXX -->` transclusion token; an inline `§EXXX` mention resolves to a hover-card on the site. See §6.

---

## 3. Etymological-gloss conventions

The Etymological line is conlang-specific and not part of standard Leipzig conventions. Its purpose is to make the diachronic derivation visible at a glance — what GA material each conlang word descends from. Conventions in current use:

- `today.is` — periods join elements that descend from separate GA morphemes but surface as a single conlang word. The dot is read as "fused with."
- `(a)bit.more` — parentheses mark a GA element that has been phonologically reduced to the point of unrecoverability or fully lost, but is etymologically present. The parenthesized material is what the GA reading would supply; it is not pronounced.
- `nippy.side` — applies to compounds: GA open compounds that surface as a single conlang word are joined with `.`.
- `rĩbii·hii` (in the **Conlang** line, not the Etymological line) — the middle dot `·` marks an internal morpheme boundary that the orthography fuses but that the etymology preserves. Use sparingly, only when the boundary is load-bearing for a discussion or a cross-reference.

The Etymological line is not a Leipzig gloss substitute. When grammatical role is what matters (case, TAM, agreement), use the Leipzig line. The Etymological line answers a different question: "what GA material is this?"

---

## 4. Tag registry

Tags are open-class and added as needed. Maintain the flat list here when introducing a new tag, so tag drift stays visible and consolidation is possible later.

- `#weather` — weather and atmospheric description
- `#comparative` — comparative and superlative constructions
- `#hedging` — epistemic / pragmatic hedging
- `#recognitional-habitual` — uses of the recognitional-habitual nominal (see `verbal-system.md` §6)

---

## 5. Entries

### E001 {#E001}

- **Conlang:** Ŕeus | bémmo | oų | rĩbii·hii. | Oų | riis·hii | o | noê.
- **IPA:** /ɾ̥ɛ:s bɛm:o õ: ɾɪbihi. õ: ɾis:i o no'ɛ/
- **Etymological:** Today.is | (a)bit.more | on.the | nippy.side. | On.the | nice.side | though | (i)n.a.way.
- **Leipzig:** today\COP bit-CMPR on-DEF nippy-NMLZ ‖ on-DEF nice-NMLZ though in-DEF-way
- **Translation:** "It's a little more chillier today, in a pleasant kind of way."
- **Tags:** #weather #comparative #hedging
- **Cited from:** `dictionary.md` (ŕe)
- **Added:** 2026-05-10
- **Revised:**
  - 2026-06-26: Re-encoded the Conlang and Etymological lines into `|`-aligned chunks (v0.2 format). Content, IPA, and analysis unchanged.
- **Notes:** Seed entry for the corpus. The IPA and Leipzig layers are first-pass and pending author review. Specific items flagged: (a) the realization of `Ŕ` (acute over r) is transcribed as voiceless /r̥/ on placeholder grounds and needs reconciliation with `phonology.md`; (b) the nasalization marked by `ų` is transcribed as a coda /ŋ/ rather than vowel nasalization — also pending reconciliation with `phonology.md` §4; (c) the morpheme-boundary middle dot in `rĩbii·hii` and `riis·hii` is treated as orthographic-only and is not reflected in the IPA; (d) the Leipzig glosses `NMLZ` for `-hii` and the analysis of `o noê` as `in-DEF-way` are tentative and will firm up as the recognitional-habitual and adverbial constructions are committed.

---

## 6. Display conventions

This document holds the canonical record (§2). Citing documents do **not** reproduce it; they pull it in at build time with a transclusion token, and each pipeline renders it in the style that context wants. The token:

```
<!-- example: E001 -->
```

The build expands it in place, resolving the style from the host document (overridable as `<!-- example: E001 | dictionary -->`). The three target styles:

- **Dictionary (inline).** Conlang + Translation only, flowing inline in the entry's prose — conlang italicized, translation in double quotes — so the dictionary body stays dense. No block, no ID, no gloss.

  > *Ŕeus bémmo oų rĩbii·hii. Oų riis·hii o noê.* "It's a little more chillier today, in a pleasant kind of way."

- **Reference grammar, HTML.** The aligned Conlang and Etymological chunks render as an **interactive** two-row gloss: hovering a chunk highlights its counterpart on the other row, each chunk in a distinct color. The Translation runs free below. (Leipzig is held dormant — §2.)
- **Reference grammar, PDF.** The same two rows, set in a fixed-width face with **deterministic column padding** so the chunks align in print. Translation free below.

The `|`-chunk alignment in §2 is what makes both the HTML highlight and the PDF columns possible — chunk *i* of the two rows is one unit. The renderers themselves are built in a later milestone (see `planning/examples-system-roadmap.md`, Milestones A2/G); this section fixes the contract they implement.

An inline `§E001` *mention* (as opposed to the transclusion token) resolves to a hover-card on the site, not a rendered block.

---

## Versioning notes

### v0.2, June 2026 — chunk-aligned, open-schema, build-time source

Data-model overhaul for the centralized-examples system (`planning/examples-system-roadmap.md`, Milestone A1). Changes:

- **`|`-chunk alignment (§2).** The Conlang and Etymological lines are now split on `|` into aligned chunks (chunk *i* ↔ chunk *i*), the unit renderers highlight (HTML) or pad into columns (PDF). The build requires equal chunk counts and fails loudly on a mismatch. E001 re-encoded; content/analysis unchanged.
- **Leipzig deferred (§2).** Held dormant — no renderer emits it until the gloss inventory settles. Existing lines preserved, not displayed.
- **Open schema (§2).** Records are extensible; future fields (audio, per-chunk notes) add without migration. Parsers ignore unknown fields.
- **Build-time source only (§2, §6).** This document is no longer published as an HTML page or PDF chapter. Citing docs transclude via `<!-- example: EXXX -->`; `§EXXX` mentions resolve to a site hover-card. §6's reference-grammar display, formerly `[Open]`, is now specified: interactive aligned gloss (HTML), monospace columns (PDF), inline conlang+translation (dictionary).
- **Parser (`site/scripts/parse.mjs`).** `parseExamples` now emits `{ conlang, segments[], ipa, translation, tags, slug }` (the joined `conlang` kept for the existing hover-card). The transclusion renderers and the site-page removal land in Milestone A2.

### v0.1, May 2026 — initial scaffold

Document created as a sibling reference, parallel to `phonology.md`, `orthography.md`, `verbal-system.md`, and `dictionary.md`. Established:

- **Sibling-doc status.** This document is the single source of truth for glossed example sentences. Other documents cite entries by ID (`examples.md §EXXX`) rather than reproducing glosses inline.
- **Entry format (§2).** Five gloss layers (Conlang, IPA, Etymological, Leipzig, Translation) plus metadata fields (Tags, Cited from, Added, Revised, Notes). Stable zero-padded IDs (`E001`, `E002`, …); IDs never reused.
- **Etymological-gloss conventions (§3).** Periods for fused morphemes, parentheses for phonologically lost GA material, middle dot `·` in the Conlang line for fused-orthography morpheme boundaries.
- **Tag registry (§4).** Seeded with `#weather`, `#comparative`, `#hedging`, `#recognitional-habitual`.
- **Per-entry change tracking.** `Added` field for creation date; `Revised` field for substantive-change log inside the entry. Doc-level versioning notes here track structural changes to the document itself, not per-entry edits.

Corpus seeded with **E001** (weather / comparative / hedging). E001's IPA and Leipzig layers are flagged in its Notes as first-pass and pending author review.

**Not yet propagated.** No sibling document yet cites this file. When the first cross-reference is added, update `language_reference.md` §8 (doc set list) and `CLAUDE.md` (Document hierarchy) to register `examples.md` as a sibling reference.
