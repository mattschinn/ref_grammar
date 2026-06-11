# Example Adder

A procedure for adding glossed example sentences to `examples.md`. Invoked explicitly by the user with "Let's add an example" or close variants ("let's gloss X," "I want to add a sentence," "let's add a gloss").

This skill walks through a fixed sequence of steps: confirming the gloss fields, writing the entry to `examples.md`, then checking each content word against `dictionary.md` and updating dictionary examples or flagging missing entries. When a missing entry needs to be created, this skill hands off to `dictionary-updater.md` in stub mode.

---

## Trigger

**"Let's add an example"** or close variants ("let's gloss X," "I want to add a gloss," "let's add a sentence," etc.). When invoked, follow the steps below in order. Do not skip steps; do not reorder.

---

## Required Reading Before Acting

Before doing anything else, read:

1. `examples.md` — to know the current highest E-ID (§5), the entry format (§2), the etymological-gloss conventions (§3), and the tag registry (§4).
2. `dictionary.md` — to look up content words (§4 Entries) and to know the collation order (§2) for any stub insertions.

---

## Step 1: Confirm minimum required fields

The three required fields are:

- **Conlang** — orthographic surface form
- **Etymological** — word-for-word GA etymological transcription
- **Translation** — idiomatic English translation in double quotes

Optional fields:

- **IPA** — broad phonemic transcription (may be left `[Open]`)
- **Leipzig** — interlinear grammatical gloss (may be left `[Open]` or omitted entirely if the relevant grammar isn't committed yet)
- **Tags** — suggest at least one from the tag registry in `examples.md` §4; offer to add a new tag if none fits

If any required field is missing, ask for it before proceeding. Do not proceed until all three are provided.

---

## Step 2: Assign ID and show proposed entry

1. Read `examples.md` §5 to find the highest existing E-ID. Assign the next one in sequence (zero-padded to three digits).
2. Set **Added** to today's date (ISO format).
3. Set **Revised** to `—`.
4. Set **Cited from** to `—` (this will be filled in at Step 4 as dictionary entries are linked).
5. Compose the full proposed entry block in the format defined by `examples.md` §2.
6. Show it to the user and wait for explicit approval before writing anything. The user may request changes; iterate until approved.

---

## Step 3: Write entry to examples.md

Once approved:

1. Append the entry to `examples.md` §5, after the last existing entry, separated by `---`.
2. Add a brief line to `examples.md` Versioning notes — only if this session also introduces a new tag or a format change. Routine additions (entry only, no structural change) do not require a versioning-notes update; the `Added:` date field in the entry is the record.

---

## Step 4: Identify content words

Using the Etymological gloss as a guide, align each whitespace-delimited conlang token with its etymological counterpart. This alignment tells you what dictionary headword each surface form corresponds to, even when inflection or phonological reduction has obscured the surface form.

For each aligned pair, decide whether to proceed to Step 5:

**Skip the word if any of the following apply:**
- The etymological gloss marks it as a function word: preposition, article, particle, conjunction, auxiliary, pronoun, clitic, or bound morpheme. Typical markers: `on.the`, `in.a`, `though`, `the`, `a(n)`.
- The dictionary entry (if it exists) lists its POS as one of the above.
- The dictionary entry already has two or more inline examples across its definitions.

**Proceed to Step 5** for all other content words.

---

## Step 5: For each content word — lookup and decision

Look up the dictionary headword (derived from Step 4 alignment) in `dictionary.md` §4.

### Case A: Word is not in dictionary.md

Surface it to the user: "X (from GA source Y) is not in the dictionary. Would you like to (a) create a stub entry now, (b) flag it for a dedicated session, or (c) skip?"

- **(a) Stub now:** Invoke `dictionary-updater.md` stub mode (see that skill file), passing: the headword, the etymological source (from the Etymological gloss), a provisional definition (inferred from the example context), and the examples.md E-ID for cross-referencing. The stub entry will be inserted at the correct collation position and flagged `[Open: stub]`.
- **(b) Flag for later:** Add the word to the **Notes** field of the current examples.md entry: "Not yet in dictionary: X (GA: Y)." No changes to `dictionary.md`.
- **(c) Skip:** No action.

Wait for the user's choice before proceeding to the next word.

### Case B: Word is in dictionary.md, no existing inline example

Identify the definition the example best illustrates. Add the inline example immediately after that definition line, following the dictionary's inline format:

> *conlang sentence.* "idiomatic English translation."

Also update the **Cited from** field in the examples.md entry to include `dictionary.md (headword)`. Add a line to `dictionary.md §5. Changelog` noting the example was added.

### Case C: Word is in dictionary.md, has an existing inline example

Read the existing example(s). Assess which of the following applies:

- **Different sense or use:** The new sentence illustrates a distinct definition, a different grammatical environment, or a pragmatic/register nuance not shown by the existing example. → Propose appending the new example to the relevant definition.
- **Better illustration of the same sense:** The new sentence is clearer, more natural, or more representative than the existing one. → Propose replacing the existing example.
- **Redundant:** The new sentence adds nothing the existing example doesn't already show. → Propose skipping.

Present your assessment and recommendation to the user. Wait for their decision before making any change.

---

## Step 6: Session summary

After all content words have been processed, show the user a brief summary:

- E-ID assigned and written to `examples.md`
- Dictionary entries where an example was added or updated (list headwords)
- Dictionary entries where a stub was created (list headwords)
- Words flagged for a dedicated session (list, if any)

If any dictionary entries were touched, confirm that `dictionary.md §5. Changelog` has been updated for each one.

---

## What this skill does NOT do

- It does **not** edit `phonology.md`, `orthography.md`, or `language_reference.md`. Phonological or orthographic gaps surfaced during glossing are flagged in the examples.md entry's Notes field; they are resolved in separate sessions.
- It does **not** auto-resolve ambiguities in word identification, definition matching, or example assessment. All judgment calls surface to the user.
- It does **not** create full dictionary entries autonomously. New entries go through `dictionary-updater.md` (stub mode or full mode), which handles headword-collision checks and sanity-checking.
- It does **not** commit `[Open]` fields in existing dictionary or examples entries. If a word's IPA or sound changes are open, they stay open.

---

## Relationship to dictionary-updater.md

This skill invokes `dictionary-updater.md` in stub mode (Step 5, Case A). The stub mode is documented in that skill file. The dictionary-updater's full interactive mode (Steps 1–7) remains independently triggerable by the user and is unchanged in purpose.
