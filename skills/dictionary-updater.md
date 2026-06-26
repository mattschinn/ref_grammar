# Dictionary Updater

A procedure for adding entries to `dictionary.md`. Invoked explicitly by the user with "Let's update the dictionary" (or close paraphrase).

This skill walks through a fixed sequence of steps, gathering information from the user, sanity-checking proposed forms against the project's phonology and orthography references, and writing a new entry once everything is confirmed.

---

## Invocation modes

This skill has two modes:

- **Full mode** — user-triggered, interactive. All steps (1–7) run in order. This is the default.
- **Stub mode** — invoked from `example-adder.md` (Step 5, Case A) when a word surfaces in a gloss but lacks a dictionary entry. Abbreviated; non-interactive. See **Stub Mode** section at the end of this file.

---

## Trigger

The user invokes this skill with **"Let's update the dictionary"** or close variants ("let's add a word," "I want to add an entry," etc.). When invoked in full mode, follow the steps below in order. Do not skip steps; do not reorder.

---

## Required Reading Before Acting

Before doing anything else, read these files in the project:

1. `dictionary.md` — to know what's already there, the schema, and the collation order.
2. `orthography.md` — to sanity-check IPA ↔ orthographic mappings.
3. `phonology.md` — to sanity-check sound-change derivations, especially §4 (rule inventory) and §5 (cascade).

If any of these files have changed since the last invocation, the changes take precedence over anything in this skill file.

**Available tool — `spell2ipa`.** A deterministic spelling→IPA drafter (`skills/spell2ipa.py`, documented in `spell2ipa-skill.md`, pinned to `orthography.md` v3). Importable: `from spell2ipa import convert; convert("rhiiynii")`. Use it to *accelerate* IPA drafting and as a forward sanity-check in Step 4 — it is a **drafter, not an oracle**. It never consults the lexicon, which is fine: duplication/homophone checks are this skill's own job (Steps 2–3), not the converter's. Treat its output as a draft a human confirms, and discount its documented divergences (Step 4) before flagging a mismatch.

---

## Step 1: Confirm minimum required info

The two required fields to start an entry are:

- **Headword** (surface orthographic form)
- **At least one definition**

If either is missing, ask the user for it. Do not proceed until both are provided.

All other fields (etymon, IPA, foot, sound changes, examples, morphology, notes) are optional. The user may leave them open-ended; respect that.

---

## Step 2: Check for headword collision

Before going further, search `dictionary.md` for the proposed headword.

- **If the headword does not exist:** proceed to Step 3.
- **If the headword exists:** stop and surface the collision to the user. Show them the existing entry. Ask whether they want to:
  - (a) Add a new sense to the existing entry (treat as polysemy)
  - (b) Treat as homophones — two distinct entries with the same surface form (note: this requires a disambiguation convention we haven't established yet; flag this and ask the user how to handle)
  - (c) Modify the proposed headword
  - (d) Abandon

Wait for the user's decision before continuing.

---

## Step 3: Gather and sanity-check the definition

Confirm the definition(s) with the user. Then scan `dictionary.md` for entries with similar meanings and surface any that look related — semantic neighbors, potential synonyms, drift-note overlaps. Use judgment for now; this is the agent-reasoning version of what will eventually be a dedicated similarity-search tool.

If similar definitions exist, show them to the user briefly and ask whether the new entry is genuinely distinct, or whether it might be better folded into an existing entry.

---

## Step 4: Sanity-check IPA against orthography (if provided)

If the user provided an IPA form:

0. **Forward check first:** run `convert(headword)` (the `spell2ipa` converter) to get a predicted IPA, and compare it to the user's IPA. This is the fast pass. Before treating any difference as a real discrepancy, discount the converter's **documented, non-error divergences**: pitch is *added* from the acute (not matched); primary stress is always emitted on the final syllable; final-stop glottalization (`t` → [ʔ], e.g. *nobêt* /noˈbɛʔ/) is not modelled; `iu` = /ɪː/; a bare word-final `s` is rendered /z/ (per `orthography.md` §2.2 — no word-final devoicing); `ŕ` = /ɾ̥/ and `ę` = /ɛ̃/. A residue after discounting these is a genuine discrepancy — carry it into the reverse-walk below.
1. Walk the IPA back through the rules in `orthography.md` to predict what the headword *should* spell as.
2. Compare against the headword the user gave.
3. If they match: proceed.
4. If they don't match: surface the discrepancy. Show the user both the IPA-predicted spelling and the headword they gave, and ask which is correct. Common causes of mismatch:
   - Typo in headword or IPA
   - A new orthographic convention not yet in `orthography.md` (e.g., the `ei` for `/ei/` clarification that surfaced during entry-building)
   - A genuine ambiguity in the orthography that needs resolution

If the cause is a new orthographic convention or an ambiguity, **do not edit `orthography.md`**. Instead, note the issue in the entry's `Notes` field and add a line to the changelog (Step 7) flagging the open orthographic question.

If the user did not provide IPA, offer to derive it from the headword and the orthography rules — seed the draft with `convert(headword)` and present it as a *draft for confirmation*, not a final value (correcting the documented divergences above). The user may accept, decline, or ask to leave it `[Open]`.

---

## Step 5: Sanity-check sound changes against phonology (if provided)

If the user provided a sound-change history:

1. Check each step against the rule inventory in `phonology.md` §4.
2. Check the rule ordering against the cascade in `phonology.md` §5.
3. Verify that the derivation actually produces the IPA form claimed.

If everything checks out: proceed.

If there are problems, surface them clearly. Distinguish between:

- **Bookkeeping errors** (a rule was misnamed, a step was skipped) — fix and confirm with the user.
- **New sound changes or nuances** — rules not in `phonology.md` §4, ordering not in §5, or exceptions to existing rules. **Do not edit `phonology.md`.** Instead:
  - Note the issue inline in the Sound changes line as a brief `[Open: description]` tag — not in a `### Notes` section.
  - Add a line to the changelog (Step 7) flagging the open phonological question.
  - Confirm with the user that this is the right way to handle it, and that they understand the rule isn't being added to `phonology.md` in this session.

The goal: dictionary entries surface phonological pressure, but actual revisions to `phonology.md` are done deliberately in separate sessions.

If the user did not provide sound changes, offer to derive them from the GA etymon (if given) and the existing rules. The user may accept, decline, or leave the field `[Open]`.

---

## Step 6: Show the proposed entry; wait for approval

Before writing anything to the file, present the full proposed entry to the user in the dictionary's current schema format (see `dictionary.md` §1): `#### Etymology` section, labeled form line (`**Part of speech:**`, `**IPA:**`, `**Foot:**`), Phonological development line, then `#### Definition`. Mark `[Open]` where the user chose to leave fields unresolved.

Wait for explicit approval ("looks good," "go ahead," "write it," etc.) before proceeding to Step 7. The user may request changes; iterate until approved.

---

## Step 7: Write the entry and update the changelog

Once approved:

1. **Insert the entry into `dictionary.md`** at the correct position per the collation order in `dictionary.md` §2. Be careful here — the collation rules are not vanilla Latin alphabetical:
   - Bare letters in the order: a, b, ð, e, h, i, ii, k, l, m, n, o, œ, p, r, rh, s, t, þ, w, y
   - Within a base letter's region, undiacriticked sequences sort first by Latin order on subsequent characters; diacriticked forms follow.
   - `ii` and `rh` are distinct phonemes with their own slots after the `i`-region and `r`-region respectively.
   - Consonant diacritic forms (`ḿ`, `ń`, `ŕ`, `ś`, `š`, `w̃`, `ỹ`) follow their bare letter immediately.
   - `æ` slots after the `a`-region; `œ` slots after the `o`-region.

2. **Add a changelog entry** to the `## 5. Changelog` section at the bottom of `dictionary.md` (create the section if it doesn't exist yet — see template below). Each changelog entry has:
   - Date (use the `user_time_v0` tool to get today's date)
   - A one-line summary of what was added
   - Any flagged open questions (orthographic, phonological) surfaced during this session

3. **Show the user the diff** — what was added to the entries section, and what was added to the changelog. Confirm the file is in the expected state.

---

## Changelog Section Template

If `## 5. Changelog` doesn't yet exist in `dictionary.md`, create it at the bottom of the file with this structure:

```markdown
---

## 5. Changelog

A running record of additions and changes to the dictionary, with dates and any open questions surfaced.

### YYYY-MM-DD

- Added entry *headword* ("gloss"). [Any flags: e.g., "Open phonological question: <description>". Or: "Open orthographic question: <description>".]
```

For subsequent invocations, append new entries under new date headings (or under an existing date heading if same day).

---

## What this skill does NOT do

- It does **not** edit `phonology.md`, `orthography.md`, or `language_reference.md`. New rules and nuances are flagged inline in the Sound changes line and in the changelog; revisions to those files happen in separate, deliberate sessions.
- It does **not** force the user to fill every field. If the user wants to leave IPA, sound changes, foot, or examples open-ended, mark them `[Open]` and proceed.
- It does **not** auto-resolve headword collisions, similar-definition collisions, or IPA/orthography mismatches. All of those surface to the user for a decision.

---

---

## Stub Mode

Invoked from `example-adder.md` when a word appears in a gloss but has no dictionary entry. The caller passes: the headword, the GA etymological source (from the Etymological gloss), a provisional definition (inferred from context), and the E-ID of the source example.

**Steps in stub mode:**

1. **Check for headword collision** (same as full-mode Step 2). If the headword exists, surface the collision to the calling skill and do not create a duplicate. The example-adder will handle the collision result.

2. **Write a stub entry** at the correct collation position in `dictionary.md` §4. Use this template:

   ```
   ### headword

   #### Etymology
   *GA etymon* — [Open: stub — sourced from examples.md §EXXX; full derivation pending].

   **Part of speech:** [Open]  **IPA:** [Open]  **Foot:** [Open].

   Phonological development: [Open].

   #### Definition

   1. [provisional, from context of examples.md §EXXX] provisional definition text.
   ```

   Replace bracketed placeholders with whatever the caller provided. Keep all unresolved fields as `[Open]`. Do not ask the user for additional data — that is deferred to a dedicated full-mode session.

3. **Add a changelog entry** to `dictionary.md §5. Changelog` noting the stub and its source: `- Added stub entry *headword* (sourced from examples.md §EXXX; full derivation pending).`

4. **Return** the headword and collation position to the calling skill so it can complete its own workflow (updating `Cited from:` in examples.md, etc.).

Stub mode does **not** run the IPA/orthography sanity check (Step 4) or sound-change sanity check (Step 5) — those require data the stub doesn't have. They run when the stub is promoted to a full entry in a dedicated session.

---

## Open improvements (for later)

- The "scan for similar definitions" step (Step 3) is currently agent-reasoning. Replace with a dedicated semantic-search tool when the dictionary grows past ~50 entries.
- The collation-order insertion (Step 7.1) could be made more reliable with a small sort script that takes the existing entry list and the new headword and returns the correct insertion point. Worth considering once the dictionary is large enough that manual placement becomes error-prone.
- A "batch mode" for adding multiple entries in a single session would reduce repeated overhead. Not needed yet.