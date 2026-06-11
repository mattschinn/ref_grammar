# Terminology Registry

**Version:** v1 (June 2026)
**Status:** Canonical registry of the conlang's descriptive terminology. Maintained under `skills/reference-grammar-section-drafting-and-integration.md` §1.7. Prose in the reference documents must match the canonical terms here; this file is also the home for term history, so rejected alternatives never need to be re-litigated in body prose.

---

## 1. Rules of use

1. **One name per concept.** Body prose uses the canonical term exactly. Double-naming ("gnomic/habitual", "non-volitive ~ modulated") is a defect in new prose.
2. **Lean descriptive and long.** Spelled-out, self-explanatory terms are preferred over short opaque ones, even at the cost of wordiness. Opaque abbreviations (PH, PS, AB, INC, LVC.TAM) do not appear in body prose.
3. **Shorthands are licensed, not default.** A registered shorthand (e.g., *go-ahead*) may be used after the full term has appeared in the section.
4. **Gloss lines are a separate channel.** Interlinear glosses use the compact gloss tags registered here, per Leipzig convention. A gloss tag without a registry entry is a defect.
5. **New terms enter here first.** A draft proposing a term adds a `[Proposed]` entry; the user promotes or rejects it. Renames are executed registry-first, then swept through documents opportunistically.
6. **Statuses:** **[Settled]** — committed, in force. **[Provisional]** — in force, expected to hold, revisable when a named open question settles. **[Proposed]** — drafted by a session, awaiting the user's verdict. **[Retired]** — must not appear in new prose; listed in §6 so it is recognized in old text.

Entry schema: **Term** (canonical, full) · Shorthand · Gloss tag · Plain-language definition · Status · Canonical home · History & alternatives.

---

## 2. The verbal system

### Volitional go-ahead
- **Shorthand:** *go-ahead* (as in "the go-ahead frame", "go-ahead paradigm").
- **Gloss tag:** VOL.
- **Definition:** The paradigm side framing the event as deliberately undertaken by the subject. Grammaticalized from GA *go ahead and-*.
- **Status:** **[Settled]** (user decision, June 2026).
- **Canonical home:** `verbal-system.md` §2.
- **History & alternatives:** *volitive* (May 2026 term; retired in favor of the spelled-out, source-anchored form). The GA-source name is deliberately part of the term: it is the most intuitive handle for a general reader.

### Non-volitional get-oneself
- **Shorthand:** *get-oneself*.
- **Gloss tag:** NVOL.
- **Definition:** The paradigm side framing the subject's relationship to the event as qualified in some way other than straightforward agency; hosts the four readings (§ below). Grammaticalized from GA *get oneself-*.
- **Status:** **[Settled]** (user decision, June 2026).
- **Canonical home:** `verbal-system.md` §3.
- **History & alternatives:** *involitive* (rejected: privative name for the structurally richer side) → *modulated* (positive but opaque) → *non-volitive* (readable but clipped) → current form. The principled-asymmetry argument lives in `verbal-system.md` §8 prose, not in the term.

### Frame
- **Shorthand:** — (already short).
- **Gloss tag:** none (glosses name the specific frame: VOL / NVOL).
- **Definition:** The grammaticalized auxiliary unit that places the event in an attitudinal context: the go-ahead frame or the get-oneself frame. Carries volition, frame aspect, and (defective) person/number agreement.
- **Status:** **[Proposed]** — promote *frame* from informal synonym to the primary prose term, with *light verb complex* retained as the technical term for morphological discussion.
- **Canonical home:** `verbal-system.md` §4.
- **History & alternatives:** *light verb complex (LVC)* was the primary term (May 2026). It remains correct and is kept for morphology-internal prose; *frame* is more transparent for everything else, and the user has endorsed the source-anchored style it enables ("the go-ahead frame").

### Light verb complex
- **Shorthand:** LVC (gloss lines and morphology-internal prose only).
- **Gloss tag:** LVC (within composite tags, e.g., `LVC.VOL.HAB`).
- **Definition:** The technical name for the frame as a morphological object — the fused auxiliary cluster derived from the GA periphrases.
- **Status:** **[Settled]**, with prose preference shifting to *frame* (see previous entry).
- **Canonical home:** `verbal-system.md` §4.

### Frame aspect
- **Shorthand:** —.
- **Gloss tag:** the cell name (HAB, PROG, PST, PRF) within the composite frame tag.
- **Definition:** The tense/aspect cell carried by the frame: habitual, progressive, past, or (get-oneself only) perfect.
- **Status:** **[Proposed]** — replaces *LVC.TAM* in prose.
- **Canonical home:** `verbal-system.md` §2–3.
- **History & alternatives:** *LVC.TAM* (retired from prose: opaque acronym stack, and "TAM" is half-misleading — mood lives in the volition axis, not in these cells). The composite gloss notation (`LVC.VOL.HAB`) is unaffected.

### Habitual (frame aspect cell)
- **Gloss tag:** HAB.
- **Definition:** The frame aspect cell covering habitual and timeless/general statements.
- **Status:** **[Proposed]** — single name; the double-name *gnomic/habitual* is dropped, with "covers timeless/general statements" carried in the definition instead.
- **Canonical home:** `verbal-system.md` §2.4, §3.7.
- **History & alternatives:** *gnomic/habitual* (paradigm tables, May 2026). *Gnomic* alone rejected as jargon. Collision with the nominal "habitual marker" is resolved by renaming the latter (see *iterative marker*).

### Reading (of the get-oneself frame)
- **Shorthand:** —.
- **Gloss tag:** none (the individual readings carry tags).
- **Definition:** One of the four meanings hosted by the productive cells of the get-oneself paradigm, selected by the combination of frame aspect and concord shape.
- **Status:** **[Proposed]** — *reading* as the primary class term in prose ("the four readings of the get-oneself frame"), with *sub-modality* retained as the technical synonym where the paradigm-structural angle matters.
- **Canonical home:** `verbal-system.md` §3.3.
- **History & alternatives:** *sub-modality* (May 2026, kept as technical synonym); *modulation cell* (orphaned by the *modulated* → *non-volitive* rename; retired).

### Happenstance reading
- **Shorthand:** *happenstance*.
- **Gloss tag:** HAP.
- **Definition:** The subject finds themselves doing the verb without agency or effort — things that simply befall the subject. The default reading of the get-oneself frame. Hosted by habitual + progressive-shaped concord and past + progressive-shaped concord.
- **Status:** **[Proposed]** (rename of prose term; semantics unchanged).
- **Canonical home:** `verbal-system.md` §3.3.
- **History & alternatives:** *PH / pure happenstance* (May 2026). The name was already the best of the four; the change is dropping the opaque abbreviation from prose and registering a transparent gloss tag.

### Effortful self-benefit reading
- **Shorthand:** *self-benefit*.
- **Gloss tag:** SELF.BEN.
- **Definition:** The subject brought the event about on their own behalf, with effort; carries effortful and evaluative coloring (it took work; it served the subject). Inherits the dative-of-interest force of GA *myself*. Hosted by habitual + infinitive-shaped concord (marked) and past + infinitive-shaped concord.
- **Status:** **[Proposed]**.
- **Canonical home:** `verbal-system.md` §3.3.
- **History & alternatives:** *AB / auto-benefactive* (May 2026). *Auto-benefactive* is retained as the typological synonym for analytical notes (it is the literature's term), but it is jargon to a general reader. *Self-serving* rejected (pejorative connotation); *own-behalf* considered, less natural in running prose. The "equal billing" question for this reading (`verbal-system.md` §9.3) is unaffected by the rename; if it is later demoted to a marked emphatic, the term can narrow with it.

### Threshold reading
- **Shorthand:** *threshold*.
- **Gloss tag:** THRESH.
- **Definition:** The subject is in the process of becoming such that the verb will happen — on the approach to a tipping point. The progressive frame supplies the becoming; the infinitive-shaped concord keeps the verb prospective. Hosted by progressive + infinitive-shaped concord.
- **Status:** **[Proposed]**.
- **Canonical home:** `verbal-system.md` §3.3.
- **History & alternatives:** *INC / inchoative–threshold* (May 2026). *Inchoative* retained as the typological synonym for analytical notes; *threshold* was already half the working name and is the transparent half.

### Backdrop reading
- **Shorthand:** *backdrop*.
- **Gloss tag:** BACK.
- **Definition:** The verb's ongoing activity is the discourse-relevant backdrop — the *I-was-V-ing-when-X* framing, with experiential or narrative coloring. Hosted by perfect + progressive-shaped concord.
- **Status:** **[Proposed]**.
- **Canonical home:** `verbal-system.md` §3.3.
- **History & alternatives:** *PS / pragmatic-stative / experiential* (May 2026) — three names, none of which evoked the function, and *stative* collided with two unrelated uses of the word (stative verbs; stative-domain strategies). *Scene-setting* considered; *backdrop* is shorter and equally transparent. Note: this reading's analytical status (agency-modulation vs. co-grammaticalized discourse function, `verbal-system.md` §9.1) is open; the descriptive name is deliberately neutral between the two views.

### Concord affix
- **Shorthand:** *concord* ("infinitive-shaped concord", "progressive-shaped concord").
- **Gloss tag:** CONCORD.
- **Definition:** The affix on the main verb showing concordance with the frame. In the get-oneself paradigm, the concord shape — infinitive-shaped vs. progressive-shaped — selects the reading.
- **Status:** **[Provisional]** — the term commits only to the agreement function; revisable if lexical-aspect or pragmatic-salience effects prove to do independent grammatical work (open question, `verbal-system.md` §4.2).
- **Canonical home:** `verbal-system.md` §4.2.
- **History & alternatives:** candidates held in reserve: *echo affixes* (if primarily feature-copying), *linker morphology* (if marking the frame–verb relation), *stem extensions* (maximally noncommittal), *coloring* (informal). The shape names *infinitive-derived / progressive-derived* are reworded to *-shaped* in prose — the suffix describes what the form looks like, which is the synchronic fact; "-derived" is the diachronic claim and belongs in the Origin subsection.

### Recognitional marker
- **Shorthand:** —.
- **Gloss tag:** REC.
- **Definition:** The morpheme descended from GA *the*, marking shared-knowledge type reference on a deverbal nominal — "you know the kind." Not a definite article.
- **Status:** **[Settled]** (term sourced from the determiner-typology literature; Himmelmann).
- **Canonical home:** `verbal-system.md` §7.
- **History & alternatives:** glossing as DEF rejected — etymologically accurate, functionally misleading.

### Iterative marker
- **Shorthand:** —.
- **Gloss tag:** ITER.
- **Definition:** The plural *-s* morpheme on a deverbal nominal, adding a repeated-instances reading on top of the recognitional marker.
- **Status:** **[Proposed]** — rename of the *habitual marker (HAB)*.
- **Canonical home:** `verbal-system.md` §7.
- **History & alternatives:** *habitual marker / HAB* (May 2026). Retired to resolve the collision with the habitual frame aspect cell — two different "habituals" in one verbal system is a trap for any reader. The existing prose already glossed this morpheme's contribution as "iterative / repeated-instances," so the rename follows the documents' own description.

### Recognitional-iterative nominal construction
- **Shorthand:** *the recognitional nominal* (when the iterative layer is not at issue).
- **Gloss tag:** composite: REC-stem-ITER.
- **Definition:** The construction stacking the recognitional marker and (optionally) the iterative marker on a deverbal nominal: shared-knowledge type reference, optionally with iterated instantiation.
- **Status:** **[Proposed]** (follows automatically if *iterative marker* is adopted).
- **Canonical home:** `verbal-system.md` §7.
- **History & alternatives:** *recognitional-habitual nominal construction* (May 2026).

### Deverbal nominal
- **Definition:** A verb's action treated as a noun — the territory GA covers with the gerund (*the running*, *the eating*).
- **Status:** **[Settled]**; standard term, but the plain-language paraphrase above accompanies first use in each document.
- **Canonical home:** `verbal-system.md` §7.

### Stative-domain strategies
- **Shorthand:** *the three strategies*.
- **Definition:** The three constructional routes for expressing states (feelings, attitudes, internal conditions), which the frames cannot host directly: **activity-coercion** (pick an activity verb that correlates with the state), **stimulus-promotion** (make the stimulus the subject and the experiencer the object), and **causative** (reuse the *get X to V* shape with an external causer).
- **Status:** **[Provisional]** — class name revisable when `verbal-system.md` §9.2 (core grammar vs. sibling resource) settles; the three member names are descriptive and **[Settled]**.
- **Canonical home:** `verbal-system.md` §6.

### Weak pronoun / strong pronoun
- **Gloss tags:** standard person/number tags.
- **Definition:** Weak (clitic) pronouns are the default subject expression and carry the grammatical fusions (aspect, modal, negation) — they are the system's **aspect carriers**. Strong (tonic) pronouns, from GA *on [POSS] end*, carry emphatic, possessive, and topic-frame readings and take no fusions.
- **Status:** **[Settled]**.
- **Canonical home:** `verbal-system.md` §5.

### Nested negation
- **Definition:** Stacking a get-oneself negative over a go-ahead negative — "failing to deliberately decline" — to yield obligation ("must do").
- **Status:** **[Settled]** as a phenomenon name; glossing convention **[Open]** (`verbal-system.md` §10.1).
- **Canonical home:** `verbal-system.md` §10.

---

## 3. Discourse and the nominal side

### Visibility particles
- **Definition:** The closed two-member class of topic particles marking a fronted topic for perceptibility.
- **Status:** **[Settled]** as the class name.
- **Canonical home:** `language_reference.md` §3.7 (pending nominal-system spin-out).

### See-particle
- **Shorthand:** —. **Forms:** *hii* / *hiie* / *hiho*.
- **Gloss tag:** VIS (clausal form VIS-CLAUSAL).
- **Definition:** The visibility particle marking the topic as present and perceptible; from the imperative of GA *see*.
- **Status:** **[Proposed]** — descriptive member name for prose; the gloss tags are unchanged.
- **History & alternatives:** prose previously used the bare gloss tags ("VIS (*hii*, *hiie*)") as names; the source-anchored name follows the go-ahead/get-oneself pattern.

### Know-particle
- **Shorthand:** —. **Forms:** *no* / *nou* / *noho*.
- **Gloss tag:** NVIS (clausal form NVIS-CLAUSAL).
- **Definition:** The visibility particle marking the topic as absent, abstract, generic, or discourse-given; from the imperative of GA *know*.
- **Status:** **[Proposed]** (parallel to *see-particle*).

---

## 4. Phonology and prosody

### Appendix (prosodic appendix)
- **Definition:** Post-stress syllabic-consonant material adjoined to the prosodic word above the foot — weight-bearing but invisible to stress.
- **Status:** **[Settled]**. Use the disambiguated form *prosodic appendix* wherever document appendices (e.g., `verbal-system.md` Appendix A) are in scope.
- **Canonical home:** `phonology.md` §3.5.
- **History & alternatives:** *sesquisyllabic* — **[Retired]**, borrowed-but-misapplied (it names a left-edge phenomenon; the conlang's is right-edge). Retirement record: `phonology.md` §6 glossary.

### Pitch residue
- **Definition:** The analysis of pitch as the F0 left behind on the GA etymon's stressed syllable after loudness and length migrated to the final vowel under the conlang's final-stress rule — rather than an independently assigned prosodic feature.
- **Status:** **[Settled]** as the analytical framing (placement settled; contrastiveness **[Open]**).
- **Canonical home:** `phonology.md` §3.4.

### Mora
- **Definition:** The unit of syllable weight — roughly, one beat of vowel. A short vowel is one mora, a long vowel two, a syllabic consonant one.
- **Status:** **[Settled]**; standard term, paraphrase accompanies first use per document.
- **Canonical home:** `phonology.md` §3.1.

### Debuccalization
- **Definition:** A consonant losing its mouth posture and surfacing as bare /h/ — the path GA /s/ and onset /k/ took.
- **Status:** **[Settled]**; standard term, paraphrase accompanies first use per document.
- **Canonical home:** `phonology.md` §4.4.1.

---

## 5. Proposed-batch summary (June 2026) — awaiting user verdict

For quick review, the `[Proposed]` entries above: **frame** (prose-primary over *light verb complex*) · **frame aspect** (over *LVC.TAM*) · **habitual** (single name, over *gnomic/habitual*) · **reading** (class term, over prose *sub-modality*) · **happenstance reading** (HAP) · **effortful self-benefit reading** (SELF.BEN) · **threshold reading** (THRESH) · **backdrop reading** (BACK) · **infinitive-shaped / progressive-shaped concord** (over *-derived*) · **iterative marker** (ITER, over nominal *HAB*) · **recognitional-iterative nominal construction** · **see-particle / know-particle**.

Each can be accepted or rejected independently, except: *iterative marker* and *recognitional-iterative nominal* travel together, and the four reading names travel with the retirement of the PH/AB/INC/PS abbreviations.

---

## 6. Retired terms

Must not appear in new prose; listed so they are recognized in older text and session history.

| Retired term | Replaced by | Where the record lives |
|---|---|---|
| *involitive* | non-volitional get-oneself | `verbal-system.md` §14 |
| *modulated* | non-volitional get-oneself | `verbal-system.md` §14 |
| *volitive* | volitional go-ahead | this file (June 2026) |
| *non-volitive* | non-volitional get-oneself | this file (June 2026) |
| *modulation cell* | reading (sub-modality) | `verbal-system.md` §9.5 |
| *sesquisyllabic* | appendix | `phonology.md` §6 |
| *PH, AB, INC, PS* (in prose) | the four reading names | this file (pending verdict) |
| *LVC.TAM* (in prose) | frame aspect | this file (pending verdict) |
| *gnomic* (in prose) | habitual (cell), with timeless coverage stated in the definition | this file (pending verdict) |
| *HAB* (nominal morpheme) | iterative marker (ITER) | this file (pending verdict) |
| DEF (as gloss for the *the*-morpheme) | REC | `verbal-system.md` §7.3 |

---

## 7. Versioning notes

### v1, June 2026 — registry created

Seeded from the May 2026 terminology state across `verbal-system.md` §14/§9.5, `phonology.md` §6, and `language_reference.md`. Incorporates the user's June 2026 decisions: spelled-out descriptive terms preferred over abbreviations; *volitional go-ahead* and *non-volitional get-oneself* adopted as full paradigm-side names with *go-ahead* / *get-oneself* as shorthands. The §5 proposed batch implements the same descriptive-and-long principle across the rest of the verbal-system terminology; each item awaits the user's verdict.
