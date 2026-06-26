# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A working specification for an a priori conlang derived from General American English (GA) through a designed cascade of regular sound changes and grammaticalizations. The canonical deliverable is the Markdown documents themselves; "work" here means careful editing, cross-document reconciliation, and version-noting. Two build pipelines consume the docs as read-only input: a pandoc→tectonic PDF build (`pdf/`) and an Astro + Starlight interactive HTML site (`site/`). Neither pipeline edits the docs.

## Repository layout

The canonical documents live under `docs/`; everything else is tooling or assets that consume them.

- **`docs/reference/`** — the grammar backbone (`language_reference.md`) and its sibling deep-dives (`phonology.md`, `orthography.md`, `verbal-system.md`, `ideophones.md`, `examples.md`, `terminology-registry.md`).
- **`docs/dictionary/`** — `dictionary.md` (the lexicon).
- **`docs/quickref/`** — generated snapshots (`phonology-quickref.md`, `orthography-quickref.md`, `dictionary-index.md`); rebuilt by the quickref-updater skill, never hand-authored.
- **`data/paradigms/`** — paradigm tables as CSV.
- **`pdf/`** — the PDF pipeline: `build.ps1` / `build-dictionary.ps1` (+ `.cmd` wrappers), `assets/` (fonts, LaTeX preambles, title page), `out/` (built PDFs), `build_tmp/` (scratch, gitignored).
- **`site/`** — the Astro + Starlight HTML site (the deterministic Markdown→HTML compiler).
- **`tools/`** — standalone author tools (`diacritic-typer/diacritic_typer.html`).
- **`drafts/`**, **`skills/`** — unchanged (proposal inbox/archive; formalized procedures).

**Cross-references between docs are filename-based** (`phonology.md §4.1`, `examples.md §E001`), not path-based, and remain valid regardless of which folder a doc sits in. Do not rewrite them to include paths.

`language_reference.md` is being refactored into an **assembler**: a section whose topic has a sibling holds a `<!-- assemble: sibling.md -->` directive plus a non-normative *orientation abstract* (a regenerated copy of the sibling's opening **Abstract** — never hand-edited). Both the PDF build (Part-per-document concatenation) and the site compiler honor this model.

## Document hierarchy

The documents are not peers — they have a defined parent/sibling relationship. Edit accordingly.

- **`language_reference.md`** — top-level descriptive grammar. Holds design philosophy and high-level summaries. Sections that summarize a sibling document (phonology §2, verbs §3.4, orthography §2.3) must stay consistent with the sibling but should not duplicate detail. When a sibling commits a new rule, update the summary; do not move detail upward.
- **`phonology.md`** — canonical source for inventories, sound-change rules (§4), the derivational cascade, and metrical analysis. Status tags `[Settled] / [Provisional] / [Open]` are used throughout and load-bearing.
- **`orthography.md`** — canonical source for the writing system. Diacritics are load-bearing (Vietnamese-style), not decorative.
- **`verbal-system.md`** — sibling reference for the verbal system. Supersedes the retired `verb-terminology.md`. Hosts the volitive / non-volitive paradigm, the four sub-modalities, the recognitional-habitual nominal, and the polarity reconciliation flag.
- **`ideophones.md`** — sibling reference for the expressive layer: the ideophone word class, its phonotactic marginality, the multimodal **χ** gesture convention, and its interfaces with the quotative construction (`verbal-system.md` §12). Spun out June 2026 (the SAYING translation round); the youngest sibling.
- **`dictionary.md`** — the lexicon, in conlang collation order (§2). Each entry's **Sound changes** field cites rules from `phonology.md` §4 by reference; new derivations may surface phonology gaps that need propagating upward.

Several documents reference siblings that are not in this directory: `verb-paradigm-verdict.md`, `translation-frequency-task.md`. Treat as out-of-tree (held elsewhere or planned). `verb-terminology.md` is **retired** — do not edit it; route changes to `verbal-system.md` and consult its §13 for supersession history. `verb-recipe.md` (formerly out-of-tree) has been folded in as Appendix A of `verbal-system.md` (see `drafts/integrated/2026-05-05-verb-recipe-v2.md` for the original draft). `dictionary-updater.md` (formerly out-of-tree) is now in-tree as a skill — see "Skills" below.

## Skills

Procedural workflows the author has formalized as standalone skill files live in `skills/`. Treat them as authoritative procedures: when a user invocation matches a skill's trigger, follow the skill's steps in order rather than improvising.

- **`skills/dictionary-updater.md`** — procedure for adding entries to `dictionary.md`. **Trigger:** the user says "Let's update the dictionary" or a close variant ("let's add a word," "I want to add an entry"). The skill walks through required reading, headword-collision checks, IPA/orthography sanity-checking against `orthography.md`, sound-change sanity-checking against `phonology.md`, and writing the entry plus a changelog line. Also has a **stub mode** (invoked from `example-adder.md`, not directly by the user) that writes a minimal flagged entry when a word surfaces in a gloss without a dictionary entry. The skill explicitly **does not** edit `phonology.md`, `orthography.md`, or `language_reference.md` — phonological or orthographic gaps surfaced during entry-building are flagged in the entry's Notes and the dictionary changelog, then resolved in separate sessions.

- **`skills/example-adder.md`** — procedure for adding glossed example sentences to `examples.md`. **Trigger:** the user says "Let's add an example" or a close variant ("let's gloss X," "I want to add a gloss," "let's add a sentence"). The skill confirms the minimum required gloss fields (Conlang, Etymological, Translation), assigns the next E-ID, writes the entry, then checks each content word against `dictionary.md`: adding inline examples to existing entries, and handing off to `dictionary-updater.md` stub mode for words not yet in the dictionary. Functional/grammatical words and words with 2+ existing examples are skipped. The skill explicitly **does not** edit `phonology.md`, `orthography.md`, or `language_reference.md`.

- **`skills/quickref-updater.md`** — procedure for rebuilding the three companion quick-reference files from the canonical reference documents. **Trigger:** the user says "Let's update the quickrefs" or a close variant ("rebuild the quickrefs," "refresh the quickrefs"). Also appropriate to invoke after any session that meaningfully updates `phonology.md §4`, `orthography.md §2–4`, or `dictionary.md §4`. Produces: `phonology-quickref.md` (§4.4 rule tables only), `orthography-quickref.md` (§2–4 grapheme tables only), `dictionary-index.md` (flat headword index in collation order). These files are snapshots — they do not replace the canonical documents; rebuild them when a source changes.

## Drafts workflow

The author periodically drops update-proposal markdowns into the repository — content that revises one or more reference docs.

- **`drafts/`** — inbox for incoming proposal markdowns. New drafts land here.
- **`drafts/integrated/`** — archive of drafts that have been merged into the reference docs. Files are renamed with a date prefix at archive time (e.g. `2026-05-04-visibility-particles.md`).

Integration procedure: read the draft, apply the edits to the named target documents, bump versions and write `§"Versioning Notes"` entries for each affected doc, then move the draft to `drafts/integrated/` with a `YYYY-MM-DD-` prefix. The archive preserves the draft's original framing/wording — useful months later when the integrated text has been compressed or rewritten.

## Cross-document propagation

Edits routinely require coordinated changes across documents. Before considering an edit complete, check downstream:

- **A new sound rule discovered while writing a dictionary entry** → propose the rule in the entry's Notes, then propagate to `phonology.md` §4 and (if it changes inventories or summaries) to `language_reference.md` §2. Examples already in-flight: geminate /sː/ at stressed-syllable boundary; initial unstressed /ə/ → /ɛ/; lexical /ʔ/-drop in grammaticalized particles. See `dictionary.md` entries *beussou* and *epplii*.
- **A new orthographic convention** → confirm in the entry, then propagate to `orthography.md`. Example: doubled-consonant-as-geminate (`ss`, `nn`, `pp`) began dictionary-internal and has since been propagated to `orthography.md` §2.4.
- **A grammar commitment** → update both `verbal-system.md` (or the relevant sibling) and the matching summary in `language_reference.md` §3. Keep the summary high-level; do not duplicate the sibling's detail.
- **Terminology shifts** must be applied consistently across all documents and noted in the affected files' §"Versioning Notes". The most recent example: *involitive* → *non-volitive* (May 2026).

## Conventions

- **GA reconstructions** are written in italics with a leading asterisk: *sodium*, *go ahead and-*, *the*. **Conlang surface forms** appear in plain italics or in slashes for phonological discussion: *hoiom*, /ˈhoiom/.
- **Status tags** `[Settled]`, `[Provisional]`, `[Open]` are used in `phonology.md` and `verbal-system.md` and downstream readers depend on them. Do not commit `[Open]` items to `[Settled]` without an explicit decision and a versioning-note entry.
- **Glossing** follows Leipzig conventions where possible. New gloss conventions (e.g., for nested negation) are tracked as open questions — see `verbal-system.md` §8 / §9.
- **Versioning is explicit.** Each major document has a header `**Version:**` line and a §"Versioning Notes" section at the end. Substantive edits update both — bump the version (e.g., v2 → v2.1), and add a dated changelog entry explaining what moved and why. Match the existing style; the changelogs are designed to be skimmable for designers returning months later.
- **Open questions** are listed in `language_reference.md` §7. When closing a question, remove it from §7 and record the resolution in the §"Versioning Notes" entry of the affected doc.

## Editing posture

- This is a living specification, refined deliberately. The author has flagged uncertainty extensively; respect it. Do not silently resolve `[Open]` questions, "clean up" hedged language, or impose internal consistency by overwriting one document's claim with another's — flag the conflict instead.
- The documents are also intended as LLM-feedable context. Keep prose tight, terminology consistent, and cross-references explicit (`§3.4.2 of language_reference.md`, `phonology.md §4.1`).
- The retired `verb-terminology.md` may still be referenced from external notes — leave the supersession trail intact rather than deleting history.
