---
name: writing-style
description: Apply the prose canon (sentence- and paragraph-level writing discipline) to the conlang's descriptive documents. Use when the user says "tighten this," "edit for style," "de-bloat," "cut this down," or "apply the writing style." Also referenced by the ref-grammar-section-draft-and-integrate skill while drafting.
---

# Reference Grammar: Writing Style (Prose Canon)

**Version:** v0 (June 2026) — exemplar-anchored core. Awaiting the author's own before/after bank (see Part 5).
**Status:** Skill file. Lives in `.claude/skills/writing-style/`. Invoked directly by the user (see Trigger) and referenced as the **prose canon** by the `ref-grammar-section-draft-and-integrate` skill.

This skill governs **sentence- and paragraph-level prose discipline** for the descriptive documents (`language_reference.md`, `phonology.md`, `orthography.md`, `verbal-system.md`, `ideophones.md`, and future siblings). It is the *line-editing* layer. The *structural* layer — what goes where, at what altitude, audience contract, synchronic voice, quarantine containers — lives in the drafting/integration skill's House-style canon. When the two overlap, that skill owns altitude and this skill owns the sentence; neither restates the other.

The problem this skill exists to fix: drafted prose (Claude's especially) bloats — preambles, restatement, hedge-stacking, the reflexive "not X but Y," nominalized verbs, empty intensifiers. This canon is partly a guardrail against its own author.

---

## Trigger

- **Editing mode** — the user says "tighten this," "edit for style," "de-bloat," "cut this down," "apply the writing style," or similar, pointing at existing text.
- **Drafting mode** — invoked by the drafting/integration skill while writing new prose, or when the user says "draft this *in the house style*."
- If the user asks for a style edit but the change is really structural (wrong altitude, detail in the wrong document), say so and route to the drafting/integration skill.

---

## The register caveat (read before extracting anything new)

The reference exemplars are **linguistics papers for linguists** (Mithun, Nichols, Lahiri et al.). The grammar addresses an **educated non-linguist** (the drafting skill's audience contract). So transfer the *virtues*, not the *register*.

- **Transfer:** economy, thesis-first ordering, examples carrying the argument, strong verbs, calibrated hedging, parallel structure, define-once terminology, rule-then-complication narration, distilled rule statements.
- **Do not transfer:** citation apparatus (`Dahl 2004, 2017`), literature-positioning ("an assumption that still appears in the literature…"), theory-internal framing (Constructive vs. Abstractive models), undefined jargon density.

**One calibrated exception — orientation.** Lahiri et al. open with a roadmap paragraph ("The first part of this chapter focuses on Germanic… In the final section, we summarize the changes and speculate on the causes"). That is the academic "in this chapter we will" genre that V2 otherwise flags. For a document long enough to need orientation, map the *content* — what the language does, in what order — not your *intentions*, and prefer the existing **orientation-abstract / assembler** mechanism over hand-written "in this section we will" prose. Keep it to content; keep it short.

When adding a new principle from further reading, classify it as virtue or register first. Only virtues enter this canon.

---

# Part 1 — The virtues

Each principle: the rule, a real exemplar from the references, and the anti-pattern to scan for.

### V1. State the claim first, then support it.
Lead with the finding. Evidence, examples, and qualification follow.
> "This paper argues that Russian is a fluid-S language of the same type as most of the American and Pacific ones." — Nichols 2006

**Anti-pattern:** building up to the claim through context the reader can't yet use; burying the topic sentence at the end of the paragraph.

### V2. Open on substance, not throat-clearing.
The first sentence does work — names the puzzle, states the fact, sets the stakes.
> "As linguists, we love discovering order in chaos. Grammatical complexity provides us puzzles to play with… But closer attention to what speakers actually do raises the question of whether complexity is in fact the same for the analyst, the speaker, and the language learner." — Mithun 2020 (the entire introduction; the thesis arrives in four sentences)

**Anti-pattern / scan for:** "It is important to note," "It is worth noting," "It should be mentioned," "In this section we will," "Let us now turn to," "First, some background."

### V3. Let the example carry the argument; keep the comment short.
Present the data, then interpret in one or two tight declaratives. The example does the explaining.
> "The verb is certainly morphologically complex, but it is highly frequent. Speaker 4 did not assemble it online: she selected it as a fully-formed lexical item." — Mithun 2020

**Anti-pattern:** explaining the example before showing it, then re-explaining after; paraphrasing the gloss back to the reader.

### V4. One claim, stated once.
Say it, then move. No restating the heading as the first sentence; no paragraph-closing sentence that re-says the opener; no "In summary" that repeats what's still on the page.

**Anti-pattern / scan for:** the section heading echoed verbatim in sentence 1; "As we have seen," "In summary," "To reiterate," "In other words" followed by no new information.

### V5. Concrete subject + strong verb. Active, present tense.
Make the grammatical subject the thing acting, and put the meaning in the verb.
> "Verbs can show other kinds of morphological elaboration… including specification of means/manner, location/direction, various kinds of verbal number…" — Mithun 2020

**Anti-pattern / scan for:** nominalized verbs — "serves to eliminate" → *eliminates*; "provides a specification of" → *specifies*; "functions to mark" → *marks*; "plays a role in," "is responsible for," "acts as a." Also existential "There is/are…" openers that bury the verb, and agentless passives where the agent matters.

### V6. Calibrate hedges. One precise modal when uncertain; commit when sure.
Uncertainty gets exactly one marker, chosen for degree. Certainty gets a flat declarative.
> Uncertain: "Small communities, with dense social networks which persist over long periods of time, **might** foster an increase in complexity." — Mithun 2020
> Certain: "Of course this is no surprise. The child knew the full question as a chunk…" — Mithun 2020

**Anti-pattern / scan for:** hedge stacks — "may perhaps," "could potentially," "tends to generally," "it seems likely that it might"; reflexive softeners "somewhat," "rather," "fairly," "arguably" added to claims you actually hold. (Respect the docs' real `[Provisional]`/`[Open]` tags — those are calibrated uncertainty, not hedging.)

### V7. Quarantine caveats in parentheses or subordinate clauses.
Keep the main clause clean; park the qualification where it won't slow the sentence.
> "(In (14) the reflexive and non-reflexive verbs are not cognate.)" — Nichols 2006

**Anti-pattern:** stuffing every exception into the main clause so the core claim arrives hedged and late.

### V8. Parallel content gets parallel structure.
When you list properties, distinctions, or environments, make them grammatically parallel and, where there are several, enumerate them. The same scales up: a long section or chapter can close on its findings as a standalone numbered list (Lahiri et al. recapitulate their entire chapter this way).
> "First, … they tend to occur with negation… Second, while (14)-(17) have objects… Third, the dative-S construction has a distinctive semantics… Fourth, … Fifth, the dative-S construction is highly productive…" — Nichols 2006

**Anti-pattern:** a list whose items switch grammatical shape (noun phrase, then full clause, then gerund); "Additionally… Also… Another thing…" as connective filler instead of a clean enumeration.

### V9. Define a term once, operationally, then reuse the exact term.
Stipulate the term where it first earns its keep; afterward use it verbatim. No elegant variation.
> "I will use P for the more patient-like or theme-like object and G for the more goal-like object." — Nichols 2006

**Anti-pattern:** synonym-swapping a defined term for "freshness" (this also violates the terminology-registry rule); redefining a term the registry already fixes.

### V10. Resist the "not X but Y" reflex — reserve it for a load-bearing contrast.
Assert Y directly. Use the contrastive frame only when the *negation itself* is the finding — when the reader expected X and the point is that it's actually Y.
> Legitimate (the contrast is the discovery): "The barrier was not the individual morphemes, nor their patterns of combination… but vocabulary, the pre-formed chunks." — Mithun 2020

**Anti-pattern:** "not X but Y" as default emphasis where plain "Y" carries the same content ("this is not merely a spelling choice but a phonological one" when you simply mean "this spelling marks a phonological contrast").

### V11. For a rule, give the simple version first, then complicate with data, then account for it.
Lead with the clean statement of the rule; show where it breaks on real forms; then give the conditioning that resolves the exceptions. Narrate change with compact source-to-outcome notation (*form* < *source*), per the GA-reconstruction convention.
> "The standard description of this rule is that all consonants except *r* were doubled when preceded by a short stressed syllable and followed by the front glide *j*… The actual context was more complex… The fact that words like OE *cynne* < *cynje* 'race, DAT SG'… did undergo gemination while *wīte* < *wītje* 'punishment, DAT SG'… did not, can be accounted for if we consider the West Germanic foot." — Lahiri, Riad & Jacobs

**Anti-pattern:** front-loading every exception and condition into the first statement so the rule never lands cleanly; narrating a change without showing the source > outcome forms.

### V12. Close a rule with one sentence that captures its conditioning.
After the data and the account, distill the rule to a single statement the reader can carry away. (Directly applicable to `phonology.md` §4 rule statements and the dictionary's **Sound changes** lines.)
> "Gemination occurred everywhere except where it would have adversely affected the head of the foot." — Lahiri, Riad & Jacobs

**Anti-pattern:** leaving a rule as an unsummarized pile of conditions; making the reader reconstruct the generalization themselves.

---

# Part 2 — The anti-pattern scan (quick checklist)

For an editing pass, scan for these surface tells first; each maps to a virtue above.

- Throat-clearing openers: *It is important/worth noting, It should be mentioned, In this section, Let us turn, Notably, Interestingly,* (overused) → **V2**
- Heading echoed in the first sentence → **V4**
- Closing restatement: *In summary, As we have seen, To reiterate, In other words* (+ no new info) → **V4**
- Nominalized verbs: *serves to, functions to, acts as, plays a role in, is responsible for, provides a … of, the … of X is …* → **V5**
- Existential openers: *There is/are/exists* burying the real verb → **V5**
- Hedge stacks: *may perhaps, could potentially, tends to generally, somewhat, rather, fairly, arguably* → **V6**
- Empty intensifiers: *very, really, quite, actually, simply, of course* (overused) → **V6**
- "not X but Y" / "not merely … but" as filler → **V10**
- Elegant variation on a registry term → **V9**
- Listing alternatives the text won't pursue ("it could be argued that…") → **V1/V6**
- A rule stated with every exception front-loaded, never landing cleanly → **V11**
- A rule or derivation left without a one-sentence distillation → **V12**

A flagged tell is a prompt to check, not an automatic cut — V10's legitimate use and Mithun's deliberate "Of course" show the same surface form can be earned.

---

# Part 3 — Drafting mode procedure

1. Write the claim sentence first; confirm it states the finding, not the context (**V1, V2**).
2. Attach the example/data directly under it; interpret in ≤2 declaratives (**V3**).
3. Read each sentence for subject + verb: is the subject the actor, the meaning in the verb? (**V5**)
4. For any qualification, decide: load-bearing → keep in clause; secondary → parenthesis/subordinate (**V7**); genuinely uncertain → one calibrated modal or a status tag (**V6**).
5. Pass once for the Part 2 tells before declaring the draft done.

# Part 4 — Editing mode procedure

1. **Scan** the passage against the Part 2 checklist; mark every tell.
2. **Cut** preambles and restatements outright (**V2, V4**) — these almost never carry meaning.
3. **Rewrite** nominalizations to verbs, passives to active where the agent matters (**V5**).
4. **De-stack** hedges to a single calibrated marker; flatten softeners on claims actually held (**V6**).
5. **Verify meaning survived.** Re-read original vs. edit; confirm no claim, qualification, or `[Settled]/[Provisional]/[Open]` status was dropped. Concision must not silently resolve a hedge the author meant (see drafting skill's editing posture). Flag, don't resolve.
6. Bring text into conformance **opportunistically** — fix what you touch; do not mass-rewrite settled sections without being asked.

---

# Part 5 — Before/after example bank  *(to be filled by the author — step 2)*

This section is the canon's growing half. Principles above are stable; examples accrete here. Pull genuinely bloated passages from `docs/`, rewrite them, and record each as a tagged pair so future edits have concrete precedent.

Format for each entry:

```
### EX-NN — <short label>  [tags: V2, V5]
Source: <doc> §<n> (version at time of edit)

Before:
> <verbatim bloated passage>

After:
> <rewritten passage>

Why: <one line — which tell was cut, what meaning was preserved>
```

(No entries yet — add the first batch after the first hand-editing session.)

---

## Note on dogfooding

This file is written to its own canon. If a future edit to it adds a preamble, a restatement, or a hedge stack, that edit is wrong by V2/V4/V6. Keep it tight.
