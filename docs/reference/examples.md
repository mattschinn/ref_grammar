# Examples

**Version:** v0.1 (May 2026)
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

- **Conlang** — orthographic surface form, sentence-cased and punctuated as written.
- **IPA** — broad phonemic transcription. Use `‖` for sentence break, `|` for clause break, `.` for syllable break only where ambiguous. Stress marked with `ˈ`. Conform to `phonology.md` §4.
- **Etymological** — word-for-word English etymological transcription. See §3 for notation.
- **Leipzig** — standard Leipzig interlinear gloss, marking grammatical roles. Optional but encouraged once the relevant grammar is committed in a sibling doc.
- **Translation** — idiomatic English translation in double quotes.
- **Tags** — `#`-prefixed keywords for grouping (phenomena, semantic fields, constructions). See §4.
- **Cited from** — backlinks to siblings or dictionary entries that reference this example. Maintained manually; `—` if none.
- **Added** — ISO date (YYYY-MM-DD) of first inclusion.
- **Revised** — dated bullets describing substantive changes to the entry. Use `—` until first revision. Format: `- YYYY-MM-DD: <what changed and why>`. Trivial fixes (typos, formatting) do not require an entry.
- **Notes** — optional. Open questions, contested glosses, layer-confidence flags, pointers to the discussion that generated the example.

IDs are assigned sequentially and zero-padded to three digits (`E001`, `E002`, …). They are stable and never reused, even if an entry is retired. A retired entry's block is kept in place with the body replaced by `**Retired YYYY-MM-DD:** <reason>` and the original content moved to the Revised log.

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

- **Conlang:** Ŕeus bémmo oų rĩbii·hii. Oų riis·hii o noê.
- **IPA:** /ɾ̥ɛ:s bɛm:o õ: ɾɪbihi. õ: ɾis:i o no'ɛ/
- **Etymological:** Today.is (a)bit.more on.the nippy.side. On.the nice.side though, (i)n.a.way.
- **Leipzig:** today\COP bit-CMPR on-DEF nippy-NMLZ ‖ on-DEF nice-NMLZ though in-DEF-way
- **Translation:** "It's a little more chillier today, in a pleasant kind of way."
- **Tags:** #weather #comparative #hedging
- **Cited from:** `dictionary.md` (ŕe)
- **Added:** 2026-05-10
- **Revised:** —
- **Notes:** Seed entry for the corpus. The IPA and Leipzig layers are first-pass and pending author review. Specific items flagged: (a) the realization of `Ŕ` (acute over r) is transcribed as voiceless /r̥/ on placeholder grounds and needs reconciliation with `phonology.md`; (b) the nasalization marked by `ų` is transcribed as a coda /ŋ/ rather than vowel nasalization — also pending reconciliation with `phonology.md` §4; (c) the morpheme-boundary middle dot in `rĩbii·hii` and `riis·hii` is treated as orthographic-only and is not reflected in the IPA; (d) the Leipzig glosses `NMLZ` for `-hii` and the analysis of `o noê` as `in-DEF-way` are tentative and will firm up as the recognitional-habitual and adverbial constructions are committed.

---

## 6. Display conventions

The entry format (§2) defines the canonical record for each example. How that record surfaces in citing documents depends on context.

**Dictionary style.** The `#### Examples` subsection of a dictionary entry shows only the Conlang and Translation layers, as free-flowing prose. No ID link, no IPA, no Etymological gloss, no Leipzig. The example reads like a dictionary sentence: conlang surface form in italics, followed by the idiomatic English translation in double quotes.

> *Ŕeus bémmo oų rĩbii·hii. Oų riis·hii o noê.* "It's a little more chillier today, in a pleasant kind of way."

**Reference grammar style.** [Open — display mechanics unsettled] Discussions in `language_reference.md` or sibling grammar documents show Conlang, Etymological, Leipzig, and Translation layers — IPA is omitted from inline display but lives in the `examples.md` entry for reference. The three gloss lines (Conlang, Etymological, Leipzig) should form an "invisible table" — no borders, but corresponding words align vertically across lines, as in standard linguistic interlinear typography. The Translation line runs below as a free line. The markdown mechanics for achieving this alignment are not yet settled.

---

## Versioning notes

### v0.1, May 2026 — initial scaffold

Document created as a sibling reference, parallel to `phonology.md`, `orthography.md`, `verbal-system.md`, and `dictionary.md`. Established:

- **Sibling-doc status.** This document is the single source of truth for glossed example sentences. Other documents cite entries by ID (`examples.md §EXXX`) rather than reproducing glosses inline.
- **Entry format (§2).** Five gloss layers (Conlang, IPA, Etymological, Leipzig, Translation) plus metadata fields (Tags, Cited from, Added, Revised, Notes). Stable zero-padded IDs (`E001`, `E002`, …); IDs never reused.
- **Etymological-gloss conventions (§3).** Periods for fused morphemes, parentheses for phonologically lost GA material, middle dot `·` in the Conlang line for fused-orthography morpheme boundaries.
- **Tag registry (§4).** Seeded with `#weather`, `#comparative`, `#hedging`, `#recognitional-habitual`.
- **Per-entry change tracking.** `Added` field for creation date; `Revised` field for substantive-change log inside the entry. Doc-level versioning notes here track structural changes to the document itself, not per-entry edits.

Corpus seeded with **E001** (weather / comparative / hedging). E001's IPA and Leipzig layers are flagged in its Notes as first-pass and pending author review.

**Not yet propagated.** No sibling document yet cites this file. When the first cross-reference is added, update `language_reference.md` §8 (doc set list) and `CLAUDE.md` (Document hierarchy) to register `examples.md` as a sibling reference.
