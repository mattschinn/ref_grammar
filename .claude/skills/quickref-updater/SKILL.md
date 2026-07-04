---
name: quickref-updater
description: Rebuild the three quick-reference snapshots in docs/quickref/ (phonology rules, orthography tables, dictionary index) from the canonical docs. Use when the user says "let's update the quickrefs," "rebuild the quickrefs," or "refresh the quickrefs."
---

# Quickref Updater

A procedure for building and rebuilding three companion quick-reference files from the canonical reference documents. These files extract the most frequently-consulted tables into lightweight documents, reducing session-startup overhead when the full reference docs are too large to hold in context.

## What this skill produces

- **`phonology-quickref.md`** — §4.3 cascade tables + §4.4 sound-change rule inventory (all five rule groups), stripped of prose. Extracted from `phonology.md`.
- **`orthography-quickref.md`** — All grapheme↔IPA tables and diacritic rules (§2–§4 of `orthography.md`), stripped of prose.
- **`dictionary-index.md`** — A flat table of every entry in `dictionary.md §4`: headword | IPA | POS | gloss | collation region, in collation order.

These files **do not replace** the canonical documents. When a quickref conflicts with its source, the source wins. Rebuild when a source changes.

## Trigger

**"Let's update the quickrefs"** or close variants ("rebuild the quickrefs," "refresh the quickrefs," "update the quick references"). Also appropriate after any session that meaningfully updates `phonology.md §4`, the grapheme tables in `orthography.md §2–4`, or adds entries to `dictionary.md §4`.

---

## Required Reading

Before writing, read the following sections. Skip any that are already in the current session context.

1. `docs/reference/phonology.md` §4.3 (cascade tables) and §4.4 (sound-change inventory).
2. `docs/reference/orthography.md` §2 (consonants), §3 (vowels), §4 (quick reference table).
3. `docs/dictionary/dictionary.md §4` (all entries) — extract headword, IPA, POS, and first-sense gloss from each entry.

---

## Step 1: Build `phonology-quickref.md`

**Content to include:**
- One-line header noting source version (e.g., `Extracted from phonology.md v2.3`).
- The CVCVC cascade table from §4.3: Step | Rule | Condition | Output.
- All five rule-group tables from §4.4:
  - §4.4.1 Consonantal mergers and shifts (GA source | Conlang reflex | Notes).
  - §4.4.2 Vocalic mergers (GA source | Conlang reflex).
  - §4.4.3 Elision rules — convert the prose descriptions (E1–E5) to a compact table: Rule | Trigger | Output | Notes.
  - §4.4.4 Rhotic rules — compact table: Rule | Trigger | Output | Notes.
  - §4.4.5 Suprasegmental rules — compact table: Rule | Trigger | Output | Status.

**Content to exclude:** §4.1 overview, §4.2 cascade prose, §4.3 generalizations and bleeding/feeding prose, §4.5 worked derivations, §4.6 probes, §5 open questions.

**Keep:** `[Settled]`/`[Provisional]`/`[Open]` tags inline where they appear in the source tables.

---

## Step 2: Build `orthography-quickref.md`

**Content to include:**
- One-line header noting source version.
- §2.1 Single-letter and digraph consonants table.
- §2.2 The `s`/`ś`/`ss` system — compact three-row summary table (Form | Reads as | Context).
- §2.3 Devoicing diacritic table.
- §2.4 Gemination table.
- §3.1 Short vowels table.
- §3.2 Long vowels: the Vu digraph table + iiy compressed to a one-line note.
- §3.3 Hiatus — the four-row table (Grapheme | IPA | Type | Morae).
- §3.4 `ei` diphthong — one line.
- §3.6 Nasalization — tilde table, ogonek table, long-nasal-ogonek table.
- §3.7 Pitch and stress — the three-diacritic summary, the `ii`-digraph diacritic rule as one sentence, and the worked-examples table.
- §4 Quick reference table (copy verbatim).

**Content to exclude:** §1 design principles, §2.5 approximants/syllabicity prose, §3.3 explanatory prose about `iie`/`ea`, §3.5 interpunct, §5 pedagogical implications, §6 open questions, §7 versioning notes.

---

## Step 3: Build `dictionary-index.md`

**Format:**

```
# Dictionary Index

*N entries. Source: dictionary.md [version]. Collation order: a, ą, b, ð, e, ę, æ, h, i, ii, k, l, m, ḿ, n, ń, o, ǫ, œ, p, r, rh, ŕ, s, ś, š, t, þ, w, w̃, y, ỹ.*

| Headword | IPA | POS | Gloss | Region |
|---|---|---|---|---|
```

**Rules:**
- One row per **entry headword** (not per sense). Use the first numbered sense's gloss, compressed to one clause.
- For entries with `[Open]` IPA: write `[Open]` in the IPA column.
- **Region** = the collation-order letter the headword sorts under. For digraph-letter regions (`rh`, `ii`, `ŕ`): write the digraph.
- Sort rows in collation order per `dictionary.md §2`. Preserve the existing order from the source file — do not re-derive it.
- Header note states the entry count and source version.

---

## Step 4: Write the files

Write all three files to `docs/quickref/` (their canonical location since the June 2026 reorg). Do not place them in the project root or in `drafts/`.

File paths:
- `docs/quickref/phonology-quickref.md`
- `docs/quickref/orthography-quickref.md`
- `docs/quickref/dictionary-index.md`

After writing, confirm to the user: entry count in the index and the version tags used.

---

## What this skill does NOT do

- Does not edit the canonical documents (`phonology.md`, `orthography.md`, `dictionary.md`).
- Does not carry worked derivations, probes, open-question lists, versioning notes, or explanatory prose into the quickrefs.
- Does not resolve `[Open]` items — copies them verbatim.
- Does not add analytical content — only extracts and compresses what is already in the source.

---

## Maintenance

Rebuild after any session that:
- Adds or revises rules in `phonology.md §4`.
- Adds or revises grapheme tables in `orthography.md §2–4`.
- Adds or revises entries in `dictionary.md §4`.

The quickrefs are a snapshot, not a live view. A stale quickref is better than no quickref, but note in the session when a rebuild is needed.
