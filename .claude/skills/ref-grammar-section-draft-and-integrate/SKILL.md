---
name: ref-grammar-section-draft-and-integrate
description: Draft new sections for the descriptive reference grammar (language_reference.md, phonology.md, orthography.md, verbal-system.md, ideophones.md) or integrate an approved draft into them. Use when the user says "let's draft a section," "let's write up X for the grammar," "let's integrate this," or "fold this into the reference."
---

# Reference Grammar: Section Drafting and Integration

**Version:** v1 (June 2026)
**Status:** Skill file. Lives in `.claude/skills/ref-grammar-section-draft-and-integrate/`. Invoked by the user; see Trigger.

A single skill with two workflows — **Workflow A: Draft a section** and **Workflow B: Integrate a section** — sharing one house-style canon. The two workflows share the canon deliberately: drafting must anticipate integration (where the text will live, what terminology it uses, what depth it is written at), and integration must verify the same standards drafting wrote to. Splitting them into two skills would duplicate the canon and let the copies drift.

This skill governs the descriptive reference documents: `language_reference.md`, `verbal-system.md`, `phonology.md`, `orthography.md`, and any future siblings (e.g., `nominal-system.md`). It does **not** govern `dictionary.md` (see the `dictionary-updater` skill).

---

## Trigger

- **Workflow A** — the user says "let's draft a section," "let's write up X for the grammar," "let's sketch the Y section," or similar.
- **Workflow B** — the user says "let's integrate this," "fold this into the reference," "add this section to `verbal-system.md`," or similar.
- A session may run A then B back-to-back; the handoff point is the user's explicit approval of the draft.

If the user's request is ambiguous between the two, ask which they want. Do not assume a draft is approved for integration.

---

## Required reading before acting

Before either workflow:

1. `terminology-registry.md` — the canonical registry of terms. **Every term used in new prose must match its registry entry.**
2. The destination document's table of contents and §Versioning Notes (to know its current state and numbering).
3. The neighboring sections of the destination location (the section before and after where the new text will sit).
4. Any sibling-document sections the new text will summarize, point at, or be summarized by. Use Grep/Glob over `docs/` to find them; do not rely on memory of the documents.

If any project file has changed since this skill was last edited, the file takes precedence over this skill's description of it.

---

# Part 1 — House-style canon

Both workflows write and check against the following standards. They apply to all new prose; existing text is brought into conformance opportunistically (when a section is touched, fix it), not by mass rewrite.

This canon governs **altitude and placement** — audience, voice, what belongs where, and how much. **Sentence- and paragraph-level prose discipline** (concision, thesis-first ordering, strong verbs, calibrated hedging, the anti-patterns that bloat drafted text) lives in the separate prose canon, `writing-style.md`. When drafting or integrating, write to both: this skill decides *whether a sentence belongs and at what depth*; `writing-style.md` decides *how it reads*. The two are kept separate so neither restates the other.

## 1.1 Audience contract

The reference grammar addresses an **educated general reader with no linguistics background**.

- Linguistic terms are used sparingly. On first use in a document, a term gets a one-clause plain-language paraphrase (e.g., "a *mora* — the unit of syllable weight, roughly 'one beat of vowel'"). After that, use it freely.
- Apparatus that the whole grammar relies on (the asterisk convention for GA etyma, interlinear glossing, status tags, morae) is explained once in a front-matter "How to read this grammar" section of `language_reference.md`, and nowhere else.
- Heavier analytical machinery (typological parallels, literature citations, feeding/bleeding talk) is licensed only inside quarantine containers (§1.3) or in `phonology.md` §4's rule apparatus, which is inherently technical.
- Test: a sentence that a careful non-linguist could not parse on first reading is rewritten or moved into a quarantine container.

## 1.2 Synchronic-first voice

Body prose describes the language **as it is**, in the present tense, as a fact about the language — not as a fact about the project.

Two distinct kinds of "history" exist, and they are handled differently:

- **Language history (diachrony)** — sound changes, grammaticalization paths, GA sources. This is legitimate supporting content. It belongs in: (a) a marked **Origin** subsection within a chapter, (b) etymology lines attached to forms, or (c) the dedicated diachronic chapter (`phonology.md` §4 is the model). A brief source mention in body prose ("grammaticalized from GA *go ahead and-*") is fine; extended diachronic narrative is not.
- **Project history (construction)** — what earlier drafts said, which terms were considered, which session decided what, what was renamed. This **never** appears in body prose. It lives only in quarantine containers (§1.3).

Diagnostic phrases that signal a violation: "earlier drafts called this…", "was developed in previous work…", "the term was chosen because…", "[New in v2…]", "this revision…", "pending reconciliation with…" (the last is acceptable only inside a status tag or quarantine container). When drafting or integrating, sweep for these.

## 1.3 Quarantine containers

Project history, design deliberation, and analytical justification are valuable and are preserved — in exactly four places:

1. **§Versioning Notes** — what changed, when, why. This is the *only* place revision narration lives. The document opener carries the version line and a one-sentence scope statement, nothing more; openers do not narrate the latest revision.
2. **Analytical-note blocks** — a blockquote beginning `> *Analytical note.*` for justification of an analysis, literature pointers, or rejected alternatives, when keeping them adjacent to the description genuinely helps. Keep these short; if one exceeds a paragraph, move the content to (1) or (4).
3. **Origin subsections** — diachronic background, clearly headed, skippable.
4. **`terminology-registry.md`** — the full history of every term: alternatives considered, why rejected, supersessions.

Rule of thumb: a reader who skips every quarantine container should still get a complete, correct, usable description of the language.

## 1.4 The telescope template

Every chapter and major section opens wide and zooms in. The canonical order (omit stages that don't apply; never reorder):

1. **Overview** — one paragraph, plain language, stating what the system does and why it matters, with **one emblematic example**.
2. **Forms** — the inventory: tables, paradigms, surface shapes.
3. **Function** — what the forms mean; semantics and pragmatics.
4. **Distribution** — where the forms occur; syntax, restrictions, blocked combinations.
5. **Interactions** — how this system meets the others (each interaction one short paragraph plus pointer).
6. **Origin** — diachronic background, marked as skippable.
7. **Glossing** — conventions specific to this system, if any.
8. **Open questions** — explicitly tagged, scoped to this section.

`language_reference.md` §3.7 (topic particles) instantiates this template well and may be used as the in-project exemplar.

## 1.5 One home per fact

Every fact has exactly one canonical location. Everywhere else it appears as a **summary-plus-pointer**: at most a few sentences, written to be true even if the detail changes, ending in a cross-reference.

- **Depth rule for `language_reference.md`:** any section whose subject has (or is slated for) a sibling document is a summary of roughly a page or less. If a `lang_ref` section grows past that, it is a candidate for spin-out or trimming — flag it to the user.
- **Repetition within a document is a defect.** A system's motivation, asymmetry argument, or key example should appear once in full; later sections that need it point back rather than restate.
- Summaries never introduce facts absent from the canonical home.

## 1.6 The example convention

Every grammatical claim earns at least one example. The canonical format is four lines:

> *conlang surface form in working orthography, diacritics included*
> /IPA/
> morpheme-by-morpheme gloss (Leipzig-style; registry gloss tags)
> "free translation"

Rules:

- **Placeholder examples are allowed but must be flagged.** When the conlang surface form is not yet derivable (lexicon gap, undecided rule), a GA-calque example may stand in, marked `[Placeholder: conlang surface form pending — depends on <what>]`. Unflagged calques are a defect.
- Reuse the **example lexicon** (recurring forms: *beussou*, *rhiiynii*, *hoiom*, *hoʔnʔnts*, *ŕe*, the *americano*/*Emma*/*Alice* cast, …) wherever possible, so examples reinforce each other across chapters. Before inventing a new example word, check `dictionary.md` for an attested one.
- Examples introducing a form not in `dictionary.md` get a flag: `[Lexicon: <form> not yet entered]`. Do not silently coin vocabulary in grammar prose; the dictionary-updater skill owns entries.

## 1.7 Terminology rules

- **One name per concept.** Prose uses each concept's canonical registry term, exactly. Double-naming ("gnomic/habitual", "non-volitive ~ modulated") is a defect in new prose.
- **Spell terms out; lean descriptive and long.** Opaque abbreviations (PH, PS, AB, INC, LVC.TAM) do not appear in body prose. Registry shorthands (e.g., *go-ahead*, *get-oneself*) are permitted after the full term has appeared in the section.
- **Gloss lines are a separate channel.** Compact tags (VOL, REC, ITER, VIS…) are conventional in interlinear glosses and remain there; each tag maps to a registry entry.
- **New terms enter through the registry first.** A draft proposing a term adds a `[Proposed]` registry entry (term, shorthand, gloss tag, plain definition, alternatives considered); the user promotes it to `[Settled]` or rejects it. Prose may use a `[Proposed]` term, tagged as such at first use.
- Renames are executed registry-first: update the entry (old term → History), then sweep documents opportunistically, recording the sweep in each document's §Versioning Notes.

## 1.8 Status tags and changelog protocol

- **[Settled] / [Provisional] / [Open]** tags are used exactly as established. Every Open question lives in its section's Open-questions stage and, if grammar-wide, is also listed in `language_reference.md` §7.
- Contested decisions are recorded **with reasoning**, in a quarantine container — never silently resolved.
- Every integration ends with a §Versioning Notes entry (date, summary, reasoning where a decision was made) and a propagation checklist (§B.7).

---

# Part 2 — Workflow A: Draft a section

The output of Workflow A is an **approved draft snippet**, refined in conversation. Workflow A does not write into the reference documents; that is Workflow B's job.

## A.1 Scope the section with the user

Confirm before drafting:

- **Topic and boundaries** — what's in, what's explicitly out.
- **Destination** — which document, and whether this will be the **canonical home** (full telescope) or an **upward summary** (summary-plus-pointer). This decides the depth.
- **Epistemic state** — which claims are Settled, Provisional, Open. If the user hasn't said, propose a partition and confirm.
- **Mode** — *sketch-and-discuss* (default: outline and key decisions discussed in chat before full prose, per the project's predictions-first habit) or *straight-to-draft* if the user says the material is already worked out.

## A.2 Do the required reading

Per the Required-reading list: registry, destination neighbors, related sibling sections. Additionally Grep `docs/` for the topic itself — earlier sessions often left partial treatments, open-question flags, or `[New rule needed: …]` markers that the draft must honor or close.

Report briefly what was found before drafting ("the topic is touched in `verbal-system.md` §X and flagged Open in §Y; the draft will…").

## A.3 Draft to the canon

- Telescope order (§1.4). Overview paragraph first — if the overview can't be written plainly, the section isn't understood yet; surface that.
- Synchronic voice; quarantine anything autobiographical (§1.2–1.3).
- Registry terminology only; new coinages drafted as `[Proposed]` registry entries alongside the snippet (§1.7).
- Every claim exampled; placeholders flagged (§1.6).
- Status tags on every commitment-bearing claim.
- House formatting: asterisked italic GA etyma (*sodium*), conlang forms in italics, phonemes in slashes, section numbering matching the destination, Leipzig glosses.

## A.4 Self-check before presenting

Run the draft against this checklist and state the result:

1. Could a non-linguist parse every body sentence? (§1.1)
2. Any project-history voice outside quarantine? (§1.2)
3. Overview-first telescope order intact? (§1.4)
4. Does anything restate a fact whose home is elsewhere? Replace with pointer. (§1.5)
5. Every claim exampled or placeholder-flagged? (§1.6)
6. Every term registry-conformant; new terms registered as Proposed? (§1.7)
7. Every open question tagged and listed in the section's Open-questions stage? (§1.8)

## A.5 Refine in conversation

Present the draft in chat (or as a working file if long). Iterate with the user. Preserve rejected alternatives **with reasons** in the draft's quarantine containers or proposed registry entries — future sessions need to see what was considered.

Workflow A ends at the user's explicit approval. Then, if the user wants it folded in, proceed to Workflow B.

---

# Part 3 — Workflow B: Integrate a section

Input: an approved snippet (from Workflow A or supplied by the user). Output: updated reference document(s), versioning notes, and a propagation checklist.

## B.1 Placement plan

Decide and present to the user before editing:

- **Canonical home** — which document and section number. Apply the document hierarchy: phonological detail → `phonology.md`; spelling → `orthography.md`; verbal system → `verbal-system.md`; nominal/discourse/syntax/lexicon framework → `language_reference.md` (pending spin-outs).
- **Upward summary** — if the canonical home is a sibling document, does `language_reference.md` need a new or updated summary-plus-pointer? Draft it (a few sentences, per §1.5).
- **Downward displacement** — if the snippet lands in `language_reference.md` but exceeds the depth rule (§1.5), flag the spin-out question to the user rather than silently deepening the top-level document.
- **Numbering impact** — does insertion renumber existing sections? List every cross-reference that will need updating (search all sibling documents for `§N` references to the affected document, plus the registry's "canonical home" column).

Wait for the user's confirmation of the plan.

## B.2 Repetition sweep

Search the destination document (and the upward-summary location) for content overlapping the snippet — same argument, same example, same motivation paragraph. For each overlap, propose: keep the canonical statement, convert the other to a pointer, or delete. Present the proposals; do not silently delete existing prose.

## B.3 Terminology and conformance pass

- Verify every term in the snippet against the registry; flag mismatches.
- If the snippet carries `[Proposed]` registry entries, confirm the user's verdict and update `terminology-registry.md` accordingly **before** writing the snippet in.
- Run the §A.4 checklist once more on the snippet *in its destination context* (a snippet that was fine standalone may now duplicate a neighbor's overview).

## B.4 Cross-reference and numbering pass

Apply the renumbering identified in B.1: in-document references first, then sibling documents, then the registry's canonical-home column. Prefer citing sections as `§N (Section Name)` — the name survives renumbering and makes stale numbers detectable.

## B.5 Show-then-confirm

Present the full set of proposed changes — new/changed sections, converted pointers, cross-reference updates, registry updates, the draft §Versioning Notes entry — before writing anything. Iterate until the user approves.

## B.6 Write

On approval, write the changes directly to the canonical files under `docs/` with the Edit/Write tools. Verify the written state matches the approved diff.

## B.7 Versioning notes and propagation checklist

- Append the §Versioning Notes entry to every document touched: date, version bump, what changed, reasoning for any decision made, cross-document consequences.
- Produce a **propagation checklist** for the user: sibling documents whose summaries are now stale, open questions opened or closed elsewhere, dictionary entries implied but not made (`[Lexicon: …]` flags), and any `[New rule needed: …]` items parked for a dedicated phonology session.
- Do **not** edit `phonology.md`'s rule inventory outside a dedicated phonology session; park pressure as flags, consistent with the dictionary-updater rule.

---

## What this skill does NOT do

- It does **not** add dictionary entries (`skills/dictionary-updater.md` owns that). Grammar text that needs a new lexical item flags it.
- It does **not** revise `phonology.md`'s sound-change rules outside dedicated phonology sessions; it parks flags.
- It does **not** rename terminology unilaterally. Renames are user decisions executed registry-first (§1.7).
- It does **not** mass-rewrite existing documents to the canon. Conformance is opportunistic: fix what you touch; larger cleanups are their own user-initiated sessions.
- It does **not** treat a Workflow-A draft as approved for integration without the user saying so.

## Open improvements (for later)

- A front-matter "How to read this grammar" section for `language_reference.md` does not exist yet; drafting it is a natural early use of Workflow A.
- A scripted cross-reference checker (grep all `§N` references against current tables of contents) would make B.4 mechanical.
- An example-sentence registry (the recurring cast and their attested example sentences) would strengthen §1.6; for now the dictionary and existing sections serve.
- Existing documents predate this canon; a one-time conformance sweep per document (changelog-leak removal, repetition consolidation, quarantining) can be run as dedicated sessions, one document at a time.
