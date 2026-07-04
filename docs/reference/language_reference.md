# Language Reference: Working Sketch

**Version:** v3.11 (June 2026)
**Predecessor:** v2.7 and earlier — see §9 (Versioning Notes).

A starting-point descriptive grammar for the conlang, an a priori language derived from General American English (GA) through a designed cascade of regular sound changes and grammaticalizations. Many features are still under analysis; this document captures current commitments and flags open questions. It is the top-level document of a set — see §8 for the full document hierarchy.

---

## How to read this document set

Conventions used throughout this document and its siblings:

- **GA reconstructions** are written in italics with an asterisk (*sodium*), marking them as the proto-form. **Conlang surface forms** appear in plain italics (working orthography, diacritics included) or in slashes /…/ for phonological discussion.
- **Status tags:** **[Settled]** — committed; downstream design depends on it. **[Provisional]** — current best analysis, expected to hold but open to revision. **[Open]** — explicitly undecided, flagged for future commitment.
- **Examples** aim for a four-line format: conlang orthography, IPA, morpheme-by-morpheme gloss (Leipzig conventions), free translation. Where the conlang surface form is not yet derivable, a GA-calque stand-in is used and flagged `[Placeholder: …]` — unflagged calques are errors, not data.
- **Co-speech gesture** is notated with the channel marker **χ** (Greek *kheir*, "hand"): in an interlinear example, a line prefixed χ after the gloss describes a conventionalized gesture accompanying the form. The convention is defined and used in `ideophones.md` §6.
- **Glossing** uses the compact tags registered in `terminology-registry.md` (VOL, NVOL, REC, ITER, VIS, NVIS, HAP, SELF.BEN, THRESH, BACK, …). Running prose spells terms out; each spelled-out term and its gloss tag are paired in the registry.
- **Terminology** follows `terminology-registry.md`, the canonical registry of the conlang's descriptive terms, their shorthands, and their naming history. A term marked there as retired may appear in older versioning notes but not in current prose.
- A **mora** — the unit of syllable weight, roughly one beat of vowel — appears throughout prosodic discussion: a short vowel is one mora, a long vowel two, a syllabic consonant one.
- **Abstracts and stubs.** Each sibling deep-dive document opens with an architecture-level **Abstract**. Sections of this document whose topic has a sibling contain only an assembly directive and a copy of that Abstract (an *orientation abstract* — non-normative, regenerated from the sibling, never hand-edited). The full grammar PDF is assembled as Part-per-document concatenation; cross-references are filename-based and survive assembly.
- **Analytical notes** (blockquotes beginning *Analytical note* or *Origin*) carry justification, history, and diachronic background. They are skippable: the body prose alone is a complete synchronic description.

---

## 1. Design Philosophy

The conlang is an a priori language derived from GA through a designed cascade of regular sound changes and grammaticalizations: sound shifts handle the vocabulary, which is therefore *latent* rather than novel, while the intellectual ambition lives in the grammar, which reshapes the semantic space. The phonology is largely settled in its rule set; the grammar is more open and is being refined as design proceeds.

The project's design goals — the relationship it cultivates to GA, and what counts as success — are collected in **Appendix A.1**.

---

## 2. Phonology and Orthography

<!-- assemble: phonology.md -->

> **Orientation abstract** — canonical content in `phonology.md`. This text is copied from that document's Abstract; edit it there, never here.
>
> The phonology derives from General American English through a designed cascade of regular sound changes, frozen at a synchronic stage. Its character: a small, reorganized consonant inventory; widespread vowel clusters and long vowels from intervocalic elision; permissive onsets against restricted codas; post-stress syllabic-consonant material housed in a prosodic appendix; and pitch dissociated from stress, analyzed as the residue of GA prominence after stress migrated to the word-final position. Suprasegmentals — pitch, length, nasalization, breathy voice — do as much expressive work as segments. This document is the canonical reference for the inventories, the syllable and metrical structure, the rule cascade with worked derivations, and the phonological open-questions backlog.

<!-- assemble: orthography.md -->

> **Orientation abstract** — canonical content in `orthography.md`. This text is copied from that document's Abstract; edit it there, never here.
>
> The writing system is Latin script with load-bearing diacritics in the manner of Vietnamese: the marks are not decorative, and ignoring them collapses minimal pairs. Diacritics and digraphs encode vowel length, nasalization, consonant devoicing, gemination, pitch, stress, and pitch-stress coincidence. Several conventions deliberately invert what a GA-literate reader expects, including position-dependent letter values and doubled vowels marking hiatus rather than length. This document is the canonical reference for the grapheme inventory, the diacritic placement rules, and the open spelling questions.

## 3. Morphology

This section is more provisional than the phonology, though several pieces are now settled enough to commit. The verb system is treated as a sibling document (`verbal-system.md`); §3.4 below is its orientation stub.

The noun-side subsections (§3.2 Nouns, §3.3 Adjectives, §3.5 Pronouns, §3.6 Adpositions, §3.7 Demonstratives and topic particles) currently live in this document. If they reach maturity together — most are still light or open — they may spin out into a sibling `nominal-system.md` parallel to `verbal-system.md`. §3.7 is the most developed of the set and the natural anchor for that future grouping; pending the spin-out, §3.7 is the *canonical home* for the visibility-particle system and is therefore deeper than this document's usual summary altitude.

### 3.1 Word-Class Inventory

The major content classes — nouns, verbs, adjectives — are inherited from GA and largely intact, though boundaries blur where grammaticalization has fused phrases.

A closed class of grammaticalized markers carries volition, aspect, polarity, and defective person/number agreement (agreement that is real but does not distinguish every person/number combination). These appear bound to verbs in the **frame** (technically, the light verb complex) and behave as inflection rather than as independent words. A second grammaticalized pair — the **recognitional marker** (from GA *the*) and the **iterative marker** (from GA plural *-s*) — operates on deverbal nominals: morphology in §3.2.1, the construction they build with the frames in `verbal-system.md` §7 and §13.

Alongside these sits an **expressive class** — the **ideophones** — words that depict the manner of an event (paradigmatically a speech act) rather than naming it: phonotactically marginal, verbalizable, and paired with co-speech gesture. They are treated as a sibling document (§3.9).

### 3.2 Nouns

Noun morphology in the working draft is light. Number marking is consistent and largely transparent (deriving from GA *-s* and irregular plurals); irregular plurals tend to be preserved or have undergone independent sound changes that obscure the alternation. No derived plural forms have yet been entered in the dictionary to exemplify this. **[Open: example plural pairs pending dictionary work]**

GA's mass/count line is not inherited wholesale: some GA mass nouns are reanalyzed as **count**. *riųś* "news" takes the article and pluralizes on the "a news / the newses" pattern, behaving as an ordinary count noun. **[Provisional]** `[Lexicon: riųś pending]`

Possession and case-like marking are still under design. Likely candidates for grammaticalization:

- A possessive marker from a fused GA *of*-construction. (Attested possession-adjacent items — *bauyǫ* "my own," *obii* "go by (a name)" — await dictionary entry. `[Lexicon: bauyǫ, obii pending]`)
- Locative/directional case-like elements from prepositions that have phonologically fused with their nominal heads (especially likely given the heavy elision processes).

These remain open pending further design work. A distributive element *-au* (from GA *all*) is attested fused onto object marking (*ŕeushiię·au* "cherishing it all"); its place in number marking is **[Open]**. `[Lexicon: -au pending]`

#### 3.2.1 The recognitional and iterative markers

Two grammaticalized morphemes operate on **deverbal nominals** — a verb's action treated as a noun:

- **Recognitional marker (REC)** — descended from GA *the*. Marks shared-knowledge type reference: "you know the kind." Not a definite article (`verbal-system.md` §7.3). Surface forms: *þ* before consonants, *y* /i/ before etymological vowels, inheriting the GA allomorphy.
- **Iterative marker (ITER)** — descended from plural *-s*. Adds a repeated-instances reading on top of the type-marking. Surface form: *-ś*.

They stack productively — REC alone gives shared-knowledge type reference; REC + ITER adds iterated instantiation — and are attested together in *þ rishś* "the dishes (you know the chore)." Glossing pattern: REC-stem-ITER. The verbal frames engage this nominal through the **possession construction** (`verbal-system.md` §13), where the helper-verb syntax is described; `verbal-system.md` §7 now points back here, the construction being analyzed as nominal/determiner morphology. The etymological-doublet origin is given below (§3.2.2).

Open questions, scoped to the morphology:

- **Does REC occur without ITER productively?** Bare REC (shared-knowledge type, non-iterative) is predicted licit; examples needed. **[Open]**
- **Does ITER occur without REC?** Bears on whether the two morphemes are independent or whether ITER requires REC as a host. **[Open]**
- **Scope of REC and ITER relative to other nominal morphology** (case-like marking, possession). **[Open]**

#### 3.2.2 Definiteness

The GA definite article *the* has not survived as such, and no general definite article has re-emerged. Instead, definiteness is recapitulated across several smaller systems — syntax and pragmatics doing the work GA morphology did:

- **The merged article *o*.** GA *the* (in its referential use) and *a* collapsed into a single article *o*, neutral for definiteness: *Ritm o rhémstwè* "(I) got them the book." Its recognitional sibling *þ ~ y* is the other half of the doublet (§3.2.1).
- **The definite-object suffix *-et*** (from GA *it*), fused onto the verb, presupposing an already-established referent: *beųheun nou·et* "went ahead and committed it to memory." **[Provisional — distribution to be confirmed]** `[Lexicon: -et pending]`
- **The visibility particles** (§3.7) carry referent-tracking and shared-reference signaling through a [±VIS] dimension rather than a [±DEFINITE] one.
- **Dislocated topics are definite.** A topic postposed by right dislocation retains definite coloring even with its visibility particle stripped (§3.7.3).

The result is a definiteness *ecology* rather than a definiteness *category*: no single morpheme answers GA *the*, and learners coming from GA must redistribute its functions across the article, the object suffix, the particles, and topic syntax. **[Provisional as a system statement]**

> *Origin.* GA *the* is an **etymological doublet** in the conlang: its referential use weakened and merged with *a* into the article *o*, while its recognitional use fused onto the nominal and kept its segmental integrity as *þ ~ y* — divergent reduction paths from one etymon, on the pattern of Latin *ille* yielding both the Romance articles and the third-person pronouns. The recognitional marker is named from the determiner-typology literature (Himmelmann and others) for its "you-know-the-one" function; the path *definite article → recognitional marker* is well-attested cross-linguistically.

### 3.3 Adjectives and Descriptive Modification

Adjective forms inherit largely from GA. Comparative and superlative formation is open. Adjective ordering and stacking conventions are open.

**Adjectival predication** uses the "on the X side" pattern: *aų* X *hii* — attested in *piies aų nibii hii* "it appears on the nippy side." The pattern combines with both volition axes ("going ahead toward the sick side" vs. "got ourselves on the sick side" — deliberate decline vs. happenstance affliction). `[Placeholder: volition-axis examples pending conlang surface forms]` The closing element *hii* is plausibly the regular reflex of GA *side* (/s/ → /h/ debuccalization, /aɪ/ → *ii*, final /d/ elided), which would make it homophonous with the see-particle; an alternative reflex *sii* also appears in working notes. **[Open: analysis of predicative *hii/sii* and its homophony with the see-particle]** Because *hii* carries the phrase-final stress, the adjective itself escapes the usual final-stress pattern. `[New rule needed: adjective stress under the stress-bearing predicative element]`

### 3.4 Verbs

<!-- assemble: verbal-system.md -->

> **Orientation abstract** — canonical content in `verbal-system.md`. This text is copied from that document's Abstract; edit it there, never here.
>
> The verbal system grammaticalizes the subject's relationship to the event: every framed verb commits to either the volitional go-ahead frame (the subject deliberately undertook the event) or the non-volitional get-oneself frame (the subject's relationship to the event is qualified in some other way). The go-ahead side is deliberately compact; the get-oneself side is richer, hosting four readings — happenstance, effortful self-benefit, threshold, and backdrop — selected jointly by frame aspect, concord shape, and the verb's own event structure. The frames do not stand alone: they combine with a pronominal system in which pronouns are aspect carriers, while the language's only tense lives in a small class of matrix particles that scaffold whole clauses with modal meaning. A possession construction derives having, getting, choosing, and giving from frame-plus-nominal combination, with the recognitional-iterative nominal as its deverbal special case; three stative-domain strategies carry the meanings the morphology cannot host. This document is the canonical reference for all of these systems; the verb-lexicon-building methodology lives in `language_reference.md` Appendix B.

### 3.5 Pronouns

The pronominal system's canonical home is `verbal-system.md` §5: pronouns are aspect carriers — fusing aspect, modality, and negation — in weak (clitic) and strong (tonic) paradigms, with left dislocation and a resumptive pronoun as the route by which full noun phrases reach the system. No further content is held here; the §3.4 assembly directive covers the whole verbal-system document.

### 3.6 Adpositions and Spatial Language

Many GA prepositions have phonologically fused with their hosts and are on a path toward case-like behavior. The full system remains open.

A specific case worth flagging: *with* in the frame's complement structure (see `verbal-system.md` §13) appears to have grammaticalized from a preposition into a verbal-complementizer-like role. Whether this generalizes to other prepositions, and whether a productive case-like system emerges, is **[Open]**.

### 3.7 Demonstratives and topic particles

The conlang has a closed set of two **visibility particles**, grammaticalized from the imperatives of GA *see* and *know*: the **see-particle** and the **know-particle**. They mark a fronted topic constituent for a [±VIS] feature, where VIS encodes presence and perceptibility while NVIS covers absent, abstract, generic, and discourse-given referents.

This is the second of the language's flagged grammatical innovations on the nominal/discourse side, alongside the recognitional-iterative nominal (`verbal-system.md` §7). The two systems are orthogonal: REC/ITER is verbal-system morphology operating on deverbal nominals, while the visibility particles are pure information-structure marking on any topic constituent. They can co-occur on the same noun phrase without interaction.

#### 3.7.1 Inventory and forms

The particles are **fossilized**: not verbs, not imperatives, not inflecting. They show a single morphological alternation — a fossilized portmanteau pattern reflecting historical incorporation of the GA article — but speakers do not synchronically decompose the long forms.

| Particle | Gloss | Bare form | Article-incorporating form | Clausal form |
|---|---|---|---|---|
| **See-particle** (present, perceptible) | VIS | *hii* /hi/ | *hiie* /hiɛ/ | *hiho* /hiho/ |
| **Know-particle** (absent, abstract, generic) | NVIS | *no* /no/ | *nou* /noː/ | *noho* /noho/ |

The bare form occurs before article-less nominals (proper nouns, pronouns, bare nouns where no article would have been present). The article-incorporating form occurs before what was historically an article-bearing nominal. The clausal form introduces a clausal topic.

The know-particle is homophonous with the **know-that matrix particle** (`verbal-system.md` §11) but syntactically distinct: matrix *no* takes a noun phrase or a full clause and yields a complete sentence, while topic *no/noho* raises a topic the listener expects elaborated. The two can co-occur — *No Báuyà, no Báuyà* "You know Báuyà? (Well,) I know Báuyà" — topic first, assertion second.

> *Origin.* The GA article *the/a* reduced to schwa in pre-conlang colloquial speech and cliticized onto the preceding particle, where it was absorbed as length (and, for *hii*, as a quality-shifted second mora); the article did not survive as an independent morpheme, and this alternation is its only grammatical residue. The clausal forms arose from fusion with GA *how* (*know how Christmas is coming up*, *see how the americano is steaming*); the fused form is a single unit, unrelated to the article-incorporation pattern. Etymological notes on the individual forms: *no* /no/ < GA *know* /noʊ/ shows shortening below the regular /oʊ/ → /oː/ reflex, attributable to high-frequency function-word reduction (parallel to the reduction of GA *the* itself). *hii* /hi/ < GA *see* /siː/ shows regular /s/ → /h/ debuccalization (`phonology.md` §4.1) and the GA-/iː/-as-gliding-/i/ pattern (`orthography.md` §3.3). *hiie* /hiɛ/ shows /i/-fronting of the absorbed schwa to /ɛ/; the orthographic shape is the first attestation of a diphthongal long vowel (`orthography.md` §3.3). *noho* and *hiho* preserve the /h/ of GA *how*, which was a strong onset-/h/ of a stressed syllable at the time of fusion.

#### 3.7.2 Function

The particles mark a fronted topic for visibility-deictic information.

**See-particle (*hii*, *hiie*)** — the topic referent is present and perceptible to the discourse participants, typically visually but extending to other modalities. Functions as a proximal demonstrative pointing-to-the-immediate, with topic-marking as its discourse role.

**Know-particle (*no*, *nou*)** — the topic referent is absent, abstract, generic, or discourse-given. Functions as a distal/abstract demonstrative or "as-for" topicalizer.

The contrast can do real disambiguating work on the same noun phrase, distinguishing physical referent from abstract type:

> *hiie nou·rítuiitsã* — `[Placeholder: the form of "violin" awaits dictionary work; the example illustrates the particle contrast]`
> VIS-REC violin
> "see the violin" — the physical instrument in the room, perceptible

> *nou nou·rítuiitsã* — `[Placeholder: as above]`
> NVIS-REC violin
> "know the violin" — the violin-as-skill or violin-as-instrument-type, abstract

Worked examples from each form:

> *hiie* americano today, it would be immaculate — `[Placeholder: only the particle is conlang surface]`
> VIS-REC americano today, ...
> "(see) the americano today, it would be immaculate" — the americano is on the counter, visible.

> *no* Alice, she is also learning the violin — `[Placeholder: only the particle is conlang surface]`
> NVIS Alice, ...
> "(know) Alice, she is also learning the violin" — Alice as topic, not present.

> *noho* Christmas is coming up, ... — `[Placeholder: only the particle is conlang surface]`
> NVIS-CLAUSAL Christmas is coming up, ...
> "(know how) Christmas is coming up, ..." — clausal topic, abstract / discourse-introduced proposition.

Pragmatic extensions of the know-particle toward "discourse-given" / "as-we've-been-discussing" readings are expected to develop, parallel to the trajectory of Japanese *wa* and similar topic particles, but are not yet committed.

#### 3.7.3 Syntax and scope

- **Position:** strictly clause-initial. The particle precedes the topic constituent, which precedes the comment — and the whole topic phrase precedes any matrix particle: **topic particle > matrix particle > clause** (`verbal-system.md` §11.3).
- **Scope:** marks a single topic constituent — a noun phrase or a clause (the latter via the clausal forms *noho*/*hiho*).
- **Stacking:** multiple topic-particle phrases in sequence are licensed, allowing chained topics with mixed visibility (*hiie* X, *no* Y, ...). Worked examples await further data.
- **Negation, questioning, embedding:** the particles do not combine with negation, do not occur in questions, and do not embed under matrix predicates. They are root-clause information-structure marking.
- **Right periphery:** the particles are **left-periphery-only**. A topic postposed after the clause (right dislocation) cannot carry a visibility particle; it is tagged instead with the strong-pronoun *on-X-end* phrase and retains definite coloring (`verbal-system.md` §5.4). **[Provisional — wants worked conlang examples]**
- **Topic discontinuity:** whether the topic constituent can be discontinuous (split between particle and comment by intervening material) is **[Open]**.

#### 3.7.4 Interaction with other systems

- **Recognitional-iterative nominal (`verbal-system.md` §7):** orthogonal. A topic constituent can independently bear REC and/or ITER on a deverbal nominal head. The particles do not select for or block them.
- **Volition (`verbal-system.md` §2–3):** orthogonal. Topic-particle marking is on the topic noun phrase or clause, not on the predicate; volition is on the predicate's frame. They co-occur freely.
- **Definiteness:** the visibility particles handle a substantial portion of what GA conveys with the definite article — referent-tracking and shared-reference signaling — but through a [±VIS] dimension rather than a [±DEFINITE] one. The conlang has no definite article and is not expected to develop one; the wider ecology is §3.2.2.
- **Matrix particles (`verbal-system.md` §11):** the topic phrase precedes the matrix particle, and under the **guess particle** *reś* (the general indirect evidential) the choice of visibility particle carries an **evidential division of labor** — *hiie ossii, reś aų nibii hii* "look at the outside — it *looks* nippy" (perceptible evidence) versus *nou ossii, reś aų nibii hii* "you know the outside — it *seems* nippy" (non-perceptible evidence). The GA *look*/*seem* contrast survives as this particle choice rather than as two verbs; *reś* itself stays neutral between perception and inference, the topic particle supplying the perceptibility.

#### 3.7.5 Origin

The grammaticalization path *imperative-of-perception-verb → demonstrative / topic particle* is well-attested cross-linguistically (Latin *ecce*, French *voici/voilà*, similar uses in Mandarin and elsewhere). The visibility distinction is also typologically standard for demonstrative systems with deictic-perceptual marking.

The recruitment of GA *know* into the particle system, rather than into the verbal lexicon, had a side effect on the verb side: the canonical GA stative *know* did not survive as a lexical verb. The gap is filled not by a stative strategy but by a **second, independent grammaticalization of the same etymon** — the know-that matrix particle (`verbal-system.md` §11), which covers both know-that (full clause) and know-person/thing (noun phrase) with one device. GA *know* thus grammaticalized twice, into the topic layer and the matrix layer, and survives as a verb in neither.

#### 3.7.6 Glossing

- **VIS** — see-particle (perceptible / present topic).
- **NVIS** — know-particle (non-perceptible / abstract / generic topic).

The bare and article-incorporating forms are not separately glossed at the morpheme level — the alternation is fossilized. Where the article-incorporating form occurs, it may optionally be noted as `VIS+art` or `NVIS+art` in pedagogical contexts to flag the historical structure. The clausal forms are glossed `VIS-CLAUSAL` and `NVIS-CLAUSAL`.

A separate `TOP` gloss is not used: these particles are inherently topic-marking, and stacking `TOP.VIS` would be redundant. If the conlang later develops a topic-marking construction without visibility, `TOP` may be added then.

#### 3.7.7 Open questions

- **Pragmatic know-particle extensions.** Discourse-given vs. discourse-new readings, expected to develop but not yet committed.
- **Stacking patterns.** Worked examples needed to determine whether mixed-visibility chained topics are pragmatically natural and what the ordering constraints are.
- **Topic discontinuity.** Whether material can intervene between the particle-marked topic and the comment.
- **Phonemic status of medial /h/.** See `orthography.md` §6 history and `phonology.md` §2.3. Bears on whether *noho* / *hiho* need disambiguating notation.
- **Clausal-form productivity.** Whether *noho* and *hiho* are the only fused-with-*how* clausal particles, or whether further fusions (with *what*, *that*, etc.) might exist or develop.

### 3.8 Connective particles

A small inventory of discourse connectives has grammaticalized from the perception/attention verbs of the *nouś/not* convergent pair fused with GA *though* and *how* — the same fusion pattern that produced the clausal topic forms *noho/hiho* (§3.7.1):

| Particle | GA source | Function |
|---|---|---|
| *notto* | *note though* | adversative — "but, mind you" |
| *nousso* | *notice though* | additive — "furthermore, and notice" |
| *not·ho* | *note how* | presentative — "voilà, there you have it" |
| *nousso* | *notice how* | presentative for new, small, or hard-to-perceive referents |

The two *nousso* are homophones from distinct fusions; context and what follows (clause vs. referent) disambiguate. **[Provisional — inventory expected to grow]** `[Lexicon: notto, nousso (×2), not·ho pending]` `[New rule needed: intervocalic glottal stop in notto]`

> *Origin.* The path parallels §3.7.5: high-frequency perception verbs grammaticalize into discourse particles. Where the visibility particles fossilized imperatives, the connectives fossilize whole hedging collocations (*note though …*), preserving the convergent pair's two stems in their frozen forms.

A second, functionally distinct set links **clauses** rather than flagging stance toward one:

| Linker | GA source | Function |
|---|---|---|
| *rhishisben* | *which is when / which has been* | simultaneity / background — "while, as" |
| *kyii* | *cue* | succession with a mild causal tint — "and then, whereupon"; can carry irony or sarcasm |

These join a clause to its neighbor (*…rhishisben ei retmseto baurzıĩ* "…while she barged in"); unlike the *nousso*-type connectives above, which mark the speaker's stance toward a single clause, the clause linkers express a relation *between* two clauses. **[Provisional — inventory expected to grow]** `[Lexicon: rhishisben, kyii pending]` `[New rule needed: the *which is when / which has been* convergence in *rhishisben* — phonology session]`

### 3.9 Ideophones

<!-- assemble: ideophones.md -->

> **Orientation abstract** — canonical content in `ideophones.md`. This text is copied from that document's Abstract; edit it there, never here.
>
> Ideophones are a productive expressive word class that depicts the manner of an event — paradigmatically a speech act — in vivid, often sound-symbolic form. The class is phonotactically marginal, able to break constraints binding on the core lexicon; verbalizable, its members taking a frame and concord to serve as predicates; and multimodal, its members pairing with conventionalized co-speech gesture. An ideophone is obligatory after the quotative verb when no words are quoted, and supplies onomatopoeia elsewhere. This document is the canonical reference for the class — its inventory, phonotactics, gesture notation, and grammatical interfaces; the quotative construction that hosts it is in `verbal-system.md` §12.

---

## 4. Syntax

Largely deferred. Working assumptions:

- Word order is broadly SVO, inherited from GA, but topic-prominent fronting may be more common than in GA.
- Question formation beyond yes/no (see `verbal-system.md` §5.5), relative clauses, and complement clauses are open.
- The interaction of volition marking with subordinate clauses is a question of particular interest — does an embedded verb inherit volition from the matrix, or carry its own? **[Open]** First adjacent data: a clause scaffolded by the end-up matrix particle keeps its own frame but surrenders its **aspect** to the particle's government (`verbal-system.md` §11.3).
- **Periphery asymmetry:** left dislocation is marked with a visibility particle; right dislocation strips it and is tagged with the strong-pronoun *on-X-end* phrase (§3.7.3; `verbal-system.md` §5.4). **[Provisional]**
- The argument structure of the frame: bare-nominal complements vs. preposition-mediated complements. **[Open]** See `verbal-system.md` §4.1.
- **Reciprocity** has no dedicated marker in the first data: on a we-subject, the get-oneself frame carries the mutual reading by itself (*riauseto bekw* "we bickered with each other"; `verbal-system.md` §3). Whether reciprocity is ever overtly marked, and the fate of an *each other* exponent, is **[Open]**.

Two constructions are settled enough to commit:

**Existential and presentational clauses.** The language has a dedicated **existential particle** *pons* (< GA *(there is) upon us*) for "there is / there are," presenting a referent or asserting existence without an agent — comparable to French *il y a*, Spanish *hay*:

<!-- example: E019 -->
<!-- preview E019 · auto-generated from examples.md · do not edit -->
> *pons rheĩ.*  
> EXIST rain  
> "There is rain."  
<!-- /preview -->

This is the **unmarked** way to predicate of an inanimate or weather subject; casting such a subject as an active framed verb instead is never neutral, coloring the event with inconvenience, fate, or unexpectedness (`verbal-system.md` §4.1). `[Lexicon: pons pending]` `[New rule needed: irregular development of *pons* < *upon us* — grammatical-word quirk, phonology session]`

**Information structure.** A **definite object resists the core object slot**: rather than sitting in situ, it is displaced to an information-structure position — fronted as a topic or appended as a clarification — with a resumptive element (the definite-object clitic *-et* "it," §3.2.2) holding the position in the clause. The pattern recurs across the transfer/possession construction: "I told her the news" keeps the definite *riųś* outside the object slot (`verbal-system.md` §13.2). **[Provisional]** Relatedly, the enclitic ***-wiis*** (< GA *-wise*) marks what a clause is *about* — "moneywise," "weatherwise" — backgrounding its host as the frame against which the comment is asserted. `[Lexicon: -wiis pending]` **[Provisional]**

---

## 5. Semantics and the Lexicon

### 5.1 The Etymological Engine

The lexicon is generated, not listed: each entry is fundamentally a GA etymon plus a gloss, with semantic-drift notes and irregular-form overrides, and its surface form is produced by running the etymon through the sound-change cascade. The dictionary (`dictionary.md`) is the canonical lexicon record; the descriptive-grammar side of the verb lexicon is `verbal-system.md` §8. The construction method itself — how the engine is operated — is **Appendix A.2**, and the verb-side building recipe is **Appendix B**.

### 5.2 The lexicon inherits GA verb uses, not GA verbs

The conlang's verb territory is carved differently from GA: what survives are specific GA *constructions* — shaped by selection (frequency, colloquial grammaticalization, fit with conlang grammar), reanalysis into the conlang's systems, and loss-with-replacement where sound change collapses forms. Homophonous merger from sound change is itself a productive lexical source: the frames and the reading grid do the disambiguating work GA did segmentally. The canonical treatment is `verbal-system.md` §8.4.

### 5.3 Productive Semantic Drift

The lexicon is *not* a one-to-one mapping of GA words to conlang forms. Drift surfaces in several patterns: **narrowing** (*countenance* → *hoʔnʔnts*, "face" specifically), **broadening** (*rhiiynii* extends GA *need* to also cover "want"), **specialization driven by grammar**, and **accretion of grammatical material** into stems (the *rhiiy-* prefix from bleached *really* — fully grammaticalized in *rhiiynii* "to need" and *rhiiysseunnou* "to be different," still transparent in *rhiiyeplii* "to apply oneself" — is the worked example of this stratification). The shift patterns are treated canonically in `verbal-system.md` §8.4. Two lexicon-design notes that turn drift to the conlang's advantage — productive false friends and the "untranslatable"-word inventory — are in **Appendix A.4.1**.

### 5.4 Cultural Embedding

The conlang is spoken by anthropomorphic-animal residents of a planet, whose still-being-designed culture should be reflected in the lexicon's organization — greeting and politeness vocabulary, domain-specific richness, and volition- and recognitional-iterative idioms that reveal cultural attitudes. The design intent for cultural embedding is in **Appendix A.4.2**.

---

## 6. Sample Forms

A small handful of attested derivations to anchor the system — **illustrative only**: the canonical records are `dictionary.md` and the `phonology.md` §4.5 worked-derivation tables, and this table is regenerated from them rather than maintained independently.

| GA etymon | Conlang | Gloss | Notes |
|---|---|---|---|
| *sodium* | *hoiiǫ* | "salt" | /s/ → /h/; intervocalic /d/ elision; labial /m/ colors schwa to /o/, then elides leaving nasalization |
| *countenance* | *hoʔnʔnts* | "face" | Heavy schwa elision; prosodic appendix with multiple syllabic-consonant nuclei |
| *Rochester* | *ritsstw* | (toponym) | /st/ → /ts/; vowel elision; appendix /w̩/ |
| *carrot* | *ŕeut* | "carrot" | M1 rhotic metathesis; /h/ as devoicing feature on tap |
| *today* | *ŕe* | "today" / "now!" | Light-monosyllabic foot; high-frequency irregular shifts |
| *pass out* | *beussou* | "to fall asleep" | Geminate /sː/ at stressed-syllable boundary; lexical /ʔ/-drop |
| *really need* | *rhiiynii* | "to need / want" | /ɪji/-smoothing → /iː/; bleached *really* prefix |

---

## 7. Open Questions and Next Commitments

Areas where the grammar is not yet committed:

- **Pitch contrastiveness** (placement is settled); the `phonology.md` §5 backlog, including the /ai/ conditioning bucket and the compound-junction rules.
- **Number marking** and basic noun morphology. **Politeness register** and greeting forms. **Numerals.**
- **Adjective system**, ordering, and modification.
- **Locative/directional case-like marking**; **motion verb morphology.**
- **Imperatives**; sequential connectives (a first connective inventory is at §3.8; sequencing/then-words remain open).
- **Nominal possession marking** (predicative possession is settled — `verbal-system.md` §13), **relative-clause-like constructions**, **descriptive extension.**
- **Aspect system** in extended discourse.
- **Volition paradigm refinement** (reading-inventory unification, self-benefit billing, stative-strategy frequency); **polarity reconciliation** with the cell × reading structure; the **concord affix feature inventory** (the *surface* forms are now settled — see below); **frame argument structure**; **nested negation glossing convention**. See `verbal-system.md` §9 and §10.
- **Written register**, formal vs. casual contrasts.

Each commitment, once made, is recorded in the affected document's §"Versioning Notes" entry with date and reasoning, and its consequences are propagated through the lexicon engine.

---

## 8. The document set

The project's current document set (the rationale for treating it as a working specification is **Appendix A.5**):

- **`language_reference.md`** (this document) — top-level descriptive grammar. Carries the front matter, the design philosophy, orientation stubs for the sibling documents, and canonical content for topics without a sibling (nominal morphology, syntax, the lexicon framework, the visibility particles).
- **`phonology.md`** — full phonological reference. Inventory, sound-change rules, derivational cascade, metrical analysis.
- **`orthography.md`** — full orthographic reference. Diacritic conventions, length and gemination conventions, pitch and nasalization placement.
- **`verbal-system.md`** — full reference for the verbal system. Go-ahead and get-oneself paradigms and frame forms (§2–§4); the pronominal system (§5); stative-domain strategies (§6); recognitional-iterative nominal (§7); verbs and the verbal system (§8); open questions (§9); polarity and negation (§10); matrix particles (§11); quotation (§12); possession construction (§13); mood (§14); assembled clauses (§15). Its verb-lexicon-building methodology has been folded into this document's Appendix B.
- **`ideophones.md`** — full reference for the expressive layer: the ideophone word class, its phonotactic marginality, the multimodal gesture convention (χ), and its grammatical interfaces. The youngest sibling.
- **`terminology-registry.md`** — canonical registry of descriptive terminology: each term's shorthand, gloss tag, plain-language definition, status, and full naming history.
- **`dictionary.md`** — the lexicon, with per-entry sound-change derivations and a running changelog.
- **`verb-paradigm-verdict.md`** — sibling working note: cell-by-cell predictions and analytical history for the verbal-system paradigm.
- **`translation-frequency-task.md`** — instrument for gathering usage-weighted data on stative-strategy frequency, reading-inventory unification, and other open questions in `verbal-system.md` §9.

### Superseded documents

- **`verb-terminology.md`** (May 2026, retired) — superseded by `verbal-system.md`. The terminology committed there is preserved through `terminology-registry.md`, which also records the subsequent renames. The file is no longer maintained.

---

## Appendix A: The Design and Construction of the Conlang

The body of this document and its siblings describes the conlang synchronically, with diachronic development from General American English (GA) supplied in marked *Origin* and *Analytical note* blocks. This appendix collects material of a different kind — the project's design goals, its construction method, its typological models, and its lexicon-design intentions. None of it is needed to use or learn the language; it is design context, gathered here so the descriptive body stays free of it.

### A.1 Design philosophy and goals

The conlang's relationship to GA is not one of disguise but of *evolution under controlled conditions*. The intent is that:

- A native GA speaker who hears the conlang cold should not perceive it as English. The phonological distance should sit at roughly the French–Sicilian or Dutch–Swiss-German range, well beyond Spanish–Portuguese.
- The same speaker, given the GA cognate after the fact, should reach an *aha* — a sense that the form follows from regular processes.
- Sound shifts handle vocabulary; vocabulary is therefore *latent* rather than novel. The intellectual ambition lives in the grammar.
- Grammar reshapes the semantic space. New categories — the volitional go-ahead / non-volitional get-oneself system, polarity, and the recognitional-iterative nominal — emerge from grammaticalized GA function-words and phrases, slicing meaning differently than GA does.

The phonology is largely settled in its rule set, though some reanalyses are still being worked through. The grammar is more open and is being refined as design proceeds.

### A.2 The construction method: the etymological engine

The lexicon is generated, not listed. Each entry is fundamentally:

- A **GA etymon** (the proto-form).
- A **gloss** (intended conlang meaning, which may or may not match the GA word's meaning).
- **Semantic drift notes** where the conlang meaning has diverged.
- **Irregular form overrides** for the small number of forms that resist regular derivation.

Surface forms are produced by running the etymon through the sound-change applier. Adjusting a sound rule regenerates surface forms across the lexicon. The dictionary (`dictionary.md`) is the canonical lexicon record; the descriptive-grammar side of the verb lexicon is `verbal-system.md` §8, and the verb-side building methodology is Appendix B.

### A.3 Typological position and natural-language precedents

The system is naturalistic but unusual. Each component sits in attested typological territory; the assembly is not exactly matched by any single natural language.

The closest precedents:

- **Tashlhiyt Berber** for the segment inventory in syllabic-consonant position. Tashlhiyt licenses almost any segment, including voiceless obstruents, as a syllabic nucleus (*tkkst stt*, *tftktstt*). The conlang's appendix nuclei /s, θ, ʔ/ sit in the same low-sonority range that has driven Tashlhiyt's analytical literature.
- **Nuxalk (Bella Coola)** for the upper bound on appendix length. Nuxalk's all-consonant words (*xłpʼχʷłtʰłpʰłːskʷʰt͡sʼ*) demonstrate that low-sonority syllabicity is attested at substantial length. The conlang's *countenance* /ˈhoʔn̩ʔn̩ts/ — four post-stress nuclei depending on parse — sits within this range.
- **English and Slavic languages** for the structural mechanism. English *rhythm* /ˈɹɪð.m̩/, *button* /ˈbʌʔ.n̩/, *little* /ˈlɪɾ.l̩/, plus Czech and Polish post-stress syllabic liquids, are the direct structural parallel: weight-bearing post-stress syllabic-sonorant material that does not compete for stress. The standard analysis is *appendix adjunction* (Selkirk, Itô-Mester), the same mechanism `phonology.md` §3.5 adopts.
- **Ancient Greek** for the segmental-prosodic combination. Greek's /s/-debuccalization (*hex* < *seks*), pitch accent on a vowel-quantity-contrasting system, and cluster-permissive-onsets-with-strict-codas asymmetry are the closest segmental-and-prosodic parallel to the conlang's overall shape.

Other resonances that surface in the design but aren't structural matches: Hawaiian and Japanese for vowel-cluster tolerance; Latin → Modern Parisian French as a diachronic-feel model (dramatic reduction producing a barely-recognizable daughter); Vietnamese for the orthographic philosophy of load-bearing diacritics; Swedish for the prosodic-overlay sensibility (geminates and pitch coexisting on a stress system); Arapaho and Minnesota Ojibwe for the small-inventory + length + pitch combination.

The combination most distinctive to the conlang — Polynesian-style vowel hiatus and small consonant inventory **with** Salishan-style syllabic obstruents and clusters **with** Swedish-style pitch overlay **with** Vietnamese-style diacritic load — is hard to find a direct natural-language match for. Each piece has clear precedent; the assembly is unusual.

**On stability.** Languages with rich post-stress syllabic-consonant tails tend to evolve in one of two directions: further reduction (the appendix nuclei elide or merge into the preceding coda) or secondary-stress development (some appendix nucleus acquires its own foot). Old English's *-ende* participles reduced to modern *-ing*; Latin post-stress material became Spanish secondary stress. The conlang's current state is best read as a **synchronic snapshot of a language mid-restabilization** — captured at a moment after aggressive schwa elision has produced the appendix material, but before the typologically-expected next step has occurred. This framing aligns with the conlang's stated diachronic origin story (regular sound changes from GA producing the surface forms) and gives the description a coherent answer to "is this naturalistic?"

For a conlang fixed at a synchronic stage, this is no defect: the diachronic story supplies exactly the right origin — regular sound changes from a recognizable source, stopped before they ran to completion.

### A.4 Lexicon design

#### A.4.1 Productive drift as identity

Drift is encouraged where it serves the conlang's identity. Two lexicon-design notes carry the principle (the drift typology itself — narrowing, broadening, grammar-driven specialization, accretion — is §5.3):

- **Productive false friends.** Words that look like their GA cognates but have meaningfully shifted, occasionally in misleading directions. Pedagogically useful: they punish lazy back-translation and reward genuine engagement with the conlang's meanings.
- **Untranslatable words.** A small inventory of concepts the conlang lexicalizes that GA does not — a design priority. These anchor the cultural texture of the conlang's setting and require learners to acquire concepts rather than mappings.

#### A.4.2 Cultural embedding

The conlang is spoken by anthropomorphic-animal residents of a planet. Their culture, customs, and social structures are still being designed, but should be reflected in the lexicon's organization:

- Greeting and politeness vocabulary tied to time of day, social distance, or occasion.
- Specialized vocabulary for whatever this culture cares about (a space-station town might have rich vocabulary for travel, weather, supplies, longing).
- Volition-marked idioms that reveal cultural attitudes toward intentionality, accident, and obligation.
- Recognitional-iterative idioms that reveal what shared-knowledge events the speakers treat as cultural touchstones.

### A.5 The document set as a working specification

This document set is a living specification, refined as design proceeds and explicitly versioned. It serves three purposes simultaneously: a working reference for the designer, the canonical context to feed into LLM-assisted conlang reasoning, and the seed of an eventual full descriptive grammar. The document manifest itself — the file-by-file map of the set — is §8.

---

## Appendix B: Building the Verb Lexicon — A Methodology

A working procedure for fleshing out the conlang's verb lexicon in a way that showcases the grammar's divergence from GA, rather than producing one-to-one translations of GA verbs. Methodology, not descriptive grammar. Descriptive facts the recipe relies on live in `verbal-system.md` §3, §6, §7, and §8; this appendix points there rather than restating them. (Folded in from `verbal-system.md`'s former Appendix A, June 2026.)

### B.1 Goal

Build a verb stock that:

- Foregrounds the **verbal system as a whole** — the frames, the four readings, the stative-domain strategies, and the recognitional-iterative nominal — as the language's distinctive expressive tools.
- Does **not** map cleanly onto GA verbs. The conlang's verb territory should be carved differently — sometimes finer, sometimes coarser, sometimes shifted laterally.
- Lets the conlang's grammar do real expressive work that GA does clunkily or not at all.
- Provides a small set of **showcase verbs** for pedagogical illustration, alongside a much larger set of **workhorse verbs** for everyday use.
- Loads the lexicon with verbs that light up the get-oneself paradigm across multiple readings, not just verbs that produce one shining cell and four muted ones.

### B.2 The two selection axes

Each candidate verb sits on two independent dimensions; both inform whether to recruit it and how to flesh it out.

#### B.2.1 Axis A — verb-volition category

Where the verb sits with respect to the go-ahead/get-oneself contrast at the *outer* level. The three categories — **polysemy-resolving**, **aspectual-shift**, **attitudinal** — are described in `verbal-system.md` §8.1. Recipe-relevant additions:

- Polysemy-resolving is **closed and found, not constructed** — don't manufacture polysemy GA didn't supply. Expected size: 15–40 verbs. Role: showcase verbs for pedagogical materials.
- Aspectual-shift: secondary showcase — demonstrates the system doing meaningful work even where GA supplies no ready-made polysemy.
- Attitudinal: the everyday expressive tool — claiming credit, deflecting responsibility, signaling agency or its absence. Most of the verb stock.

#### B.2.2 Axis B — get-oneself paradigm coverage

How richly the verb populates the four readings. This is the *inner* level of selection and is independent of Axis A. Coverage is described as **rich**, **medium**, or **thin** based on how many of the four readings yield productive, non-coerced uses. What each reading wants from a verb:

##### B.2.2.1 Happenstance

Hosted by HABITUAL and PAST with progressive-shaped concord. Wants verbs where the event can plausibly happen to the subject without their agency. Broadest of the four — almost any verb hosts happenstance if the event can be construed as befalling the subject. Achievements (*fall, find, notice, realize, catch*) host it richly because the moment of the event is naturally non-agentive. Activities (*think, wander, hum, doodle*) host it richly when they can drift into existence without intention. Verbs that *only* make sense as deliberate (*sign a contract, vote, file taxes*) host it poorly.

##### B.2.2.2 Effortful self-benefit

Hosted by HABITUAL (marked) and PAST with infinitive-shaped concord. The most selective reading. Wants (a) action-host semantics so the subject can do the thing, (b) plausible benefit to the subject, and (c) effort or self-direction in the doing. *get up, get going, get clean, get organized, get fed, get to bed, get out of the rain* host it extremely well. Verbs that benefit others (*give, help, comfort*) host it poorly. Verbs that are bad for the subject (*catch a cold, get lost, fall*) host it only under coerced negative-evaluation readings — a live question (`verbal-system.md` §9.3, `verb-paradigm-verdict.md` §1.5).

##### B.2.2.3 Threshold

Hosted by PROGRESSIVE + infinitive-shaped concord. Wants verbs with a natural onset — events with a "becoming-such-that" build-up phase. Threshold-event verbs (*fall asleep, doze off, walk out, leave, give up, break down, melt down, cave*) host it paradigmatically. Graded approaches to a state (*warm up, calm down, tire out, perk up, sober up*) also work. Punctual achievements without build-up (*find, notice, realize*) host it poorly.

##### B.2.2.4 Backdrop

Hosted by PERFECT + progressive-shaped concord. Wants verbs producing a durative event whose ongoing-ness is discourse-relevant. Activity verbs work well (*read, walk, cook, watch, listen, talk, write, drive*). Cognitive activities (*think, wonder, worry, dream, daydream*) are paradigmatic. Achievements host it poorly; telic accomplishments work only mid-event.

#### B.2.3 The two axes in combination

Each verb gets a two-coordinate label: an Axis A category and an Axis B coverage profile (rich / medium / thin, optionally with reading detail like *rich on happenstance and backdrop, thin on self-benefit and threshold*). The combined profile drives recruitment priority (§B.8). The two axes are orthogonal: Axis A is a typology of what the outer frame contrast does for a verb; Axis B is a typology of inner-paradigm richness. Any Axis A category can carry any Axis B profile.

### B.3 The stative domain

Statives (*be happy, like, want, need, hurt*) sit outside the frames proper (`verbal-system.md` §3.6, §8.2). The three strategies of `verbal-system.md` §6 are, from the recipe's standpoint, three different ways of recruiting a GA stative meaning into the lexicon.

#### B.3.1 Activity-coercion

Recruit an activity verb whose typical correlate of the GA stative meaning carries the load: GA *be happy* → conlang *smile, laugh, grin*; GA *be sad* → *frown, sigh*. When a GA stative meaning is on the recruitment list, look for the GA activity verbs that correlate with it and prioritize *those*. The stative itself may need no conlang entry at all.

#### B.3.2 Stimulus-promotion

Recruit a verb that frames the stimulus as the grammatical subject acting on the experiencer (`verbal-system.md` §6.2). GA experiencer-object verbs (*charm, captivate, soothe, bore, annoy, fascinate*) are the natural targets: their conlang counterparts host the go-ahead frame productively because the stimulus can be construed as an actor.

#### B.3.3 Causative

Recruit the *get X to V* shape with a third-party causer (`verbal-system.md` §6.3). The causative needs an action-host main verb, so it composes with activity-coercion: the speaker still picks an externalizable activity correlate of the internal state. The two strategies are deployed together for many GA stative meanings.

#### B.3.4 What this means for stative-domain recruitment

For each GA stative meaning the conlang needs to express:

1. Identify the activity verbs that correlate with it (for activity-coercion).
2. Identify the stimulus-frame verbs that can host it (for stimulus-promotion).
3. Decide whether the bare stative — the *rhiiynii*-class lexical stative, accessed through happenstance/threshold/backdrop — also needs an entry, or whether the strategies cover the territory.

For most GA statives the answer to (3) will be that the strategies cover it. A small number warrant bare entries for the irreducibly internal cases (*rhiiynii* "need/want" being the paradigm example).

### B.4 Semantic territories to prioritize

High Axis B coverage clusters in specific semantic regions of GA. These are the highest-yield recruitment targets for a richly colored verbal system.

#### B.4.1 Tier 1 — verbs that should light up across all four readings

The gold of the lexicon; recruit aggressively.

- **Self-care and bodily-state activities.** *fall asleep, wake up, doze, rest, settle in, settle down, calm down, perk up, sober up, get up, get going, ease into, lean back, sink down, sit up, get dressed, shower, eat, drink, settle.* Hits self-benefit (self-directed effortful action), happenstance (can happen without intention), threshold (natural onsets), backdrop (durative and experientially salient).
- **Cognitive activities.** *think, wonder, worry, dream, daydream, brood, ruminate, reflect, ponder, mull.* Hits backdrop paradigmatically (the I-was-thinking-about-it-when-X reading), happenstance richly (thoughts arrive uninvited), threshold for the ones with onset, self-benefit by coercion ("I got myself to think about it").
- **Threshold-transition verbs.** *walk out, drift off, slip away, give up, break down, cave, melt down, slip into, ease into, sink down, lean back.* Hits threshold paradigmatically, happenstance richly, backdrop for the durative ones, self-benefit for deliberate-self-positioning uses.

#### B.4.2 Tier 2 — verbs that light up three of the four richly

Strong targets; expect one reading to be thin.

- **Daily-life social-texture activities.** *chit-chat, wander, hang out, putter, tinker, fuss, dawdle, browse, mosey, lounge.* Strong on happenstance and backdrop. Self-benefit coerced but available. Threshold weak — no natural onsets.
- **State-onset cognitive/perceptual verbs.** *realize, notice, recognize, remember, learn, understand, see, hear, feel.* Strong on happenstance (the moment of noticing is non-agentive), threshold (becoming-aware), and backdrop (the durative state of remembering). Self-benefit weak unless the verb has a deliberate effortful use. These double as Axis A aspectual-shift verbs, layering inner and outer richness.

#### B.4.3 Tier 3 — strong happenstance/backdrop pairings, less elsewhere

Useful for filling out the lexicon, but not anchors of the paradigm.

- **Durative perceptual/experiential activities.** *watch, listen, read, watch over, look out, keep an eye on, follow along, observe.* Strong on happenstance and backdrop; threshold and self-benefit weak.
- **Mid-process accomplishments.** *cook, write, work on, sort through, get through, build, repair, clean up.* Backdrop strong mid-event; happenstance possible; self-benefit and threshold mostly weak or coerced.

#### B.4.4 What to deprioritize

Thin-paradigm verbs are still worth recruiting eventually, but not first if richness is the goal.

- **Pure-deliberate action verbs** (*sign, vote, build, pay, file, ratify, declare*). Belong in the go-ahead frame; mostly coerced or marked on the get-oneself side.
- **Other-directed verbs** (*give, help, teach, comfort, serve, deliver*). Self-benefit and threshold weak; happenstance and backdrop coerced.
- **Pure achievements without onset** (*win, lose, hit, arrive, die* — though *die* has cultural weight that may justify exception). Host only happenstance cleanly.
- **Punctual transitive achievements** (*catch, find, notice* — the polysemy-resolving class). Dramatic Axis A contrasts, but the get-oneself cells themselves are thin.

#### B.4.5 A design-strategy note

The Tier 1 convergence zone clusters heavily in the **self-state / cognitive / threshold-transition** territory. This is not accidental: it is exactly where a system grammaticalizing non-straightforward agency *should* be richest, because that is where straightforward agency is most often qualified.

A consequence: a lexicon loaded preferentially with these verbs gives the conlang a distinctive *texture* — speech will lean toward introspective, processual, transition-aware framings. Whether that fits the conlang's cultural and aesthetic profile is a deliberate design question; the current default assumption is yes, but the assumption is flagged rather than naturalized.

### B.5 How GA history drives the lexicon

The selection / reanalysis / loss-with-replacement processes and the three semantic shift patterns are described in `verbal-system.md` §8.4. The recipe consequence: when working a candidate verb, list its GA construction inventory, predict which uses survive selection, and watch for the merger phenomena `verbal-system.md` §8.4 describes — they are recruitment opportunities, not noise.

### B.6 The deverbal nominal layer

The recognitional-iterative construction and its per-verb diagnostic are described in `verbal-system.md` §7 and §8.3. Recipe consequence: test *the V-ing* and *the V-ings* for every candidate. Verbs with both rich deverbal nominalization and rich frame contrasts and reading coverage are the highest-value targets — flesh these out first. This layer is orthogonal to both axes and adds a third dimension to the verb's expressive profile.

### B.7 The diagnostic questions

For any candidate verb, work through these five questions in order. Verbs that yield satisfying answers across all five are the ones to build out first; thin answers signal candidates to defer.

1. **Which GA constructions did it participate in, and which survived?** List the GA uses; mark which are high-frequency, colloquial, formal. Predict which survive selection (`verbal-system.md` §8.4).
2. **Where does it sit on Axis A?** Polysemy-resolving, aspectual-shift, or attitudinal (`verbal-system.md` §8.1)?
3. **Where does it sit on Axis B?** Test the four readings. Which cells are productive, coerced, blocked? Record a coverage profile (rich / medium / thin), optionally with reading detail.
4. **Does it have a salient deverbal nominal, and what is the recognitional-iterative reading?** Test *the V-ing* and *the V-ings*. Is the shared-knowledge reading natural? The iterative reading? Is the verb register-flexible or register-bound?
5. **Are there cognates or competitors in GA that the conlang's phonology has merged or distinguished?** Check for near-homophones the sound changes will collapse, semantic neighbors the conlang may force into specialization, and GA polysemy the conlang may split across multiple verbs.

Questions 2 and 3 give the two-axis profile; 1, 4, and 5 give the diachronic and morphological context.

### B.8 Two-axis building order

Recruitment priority combines the Axis A and Axis B profiles. A verb that is rich on Axis B and poly-resolving or aspectual-shift on Axis A is the highest-priority target — it lights up both the outer contrast and the inner reading grid.

#### B.8.1 Priority 1 — flagship verbs

High on both axes (poly-resolving or aspectual-shift; rich coverage). The showcase: the frame contrast does dramatic work *and* the paradigm fills out across all four readings. Examples: *fall asleep* (poly-resolving via GA *pass out*, Tier 1 self-care/threshold), *remember* (aspectual-shift, Tier 1 cognitive), *walk out* (poly-resolving or attitudinal, Tier 1 threshold-transition). First batch.

#### B.8.2 Priority 2 — workhorse verbs

High on Axis B, plain on Axis A (attitudinal; rich or medium-rich coverage). The everyday vocabulary that gives the get-oneself paradigm its expressive weight in normal speech: most cognitive activities, self-care verbs, daily-life social-texture activities. *think, wonder, chit-chat, wander, putter, doze*.

#### B.8.3 Priority 3 — secondary showcase

High on Axis A, plain on Axis B (poly-resolving or aspectual-shift; medium or thin coverage). Dramatic outer contrasts, thin inner paradigms. Useful pedagogically because the contrast is sharp and easy to teach. *catch, find, notice*.

#### B.8.4 Priority 4 — long-tail vocabulary

Plain on both axes. The bulk of the lexicon; recruit as needed for breadth.

#### B.8.5 Priority 5 — stative-domain recruitment

Run alongside Priorities 1–4: for each GA stative meaning the conlang needs, identify activity-coercion, stimulus-promotion, and causative recruitments per §B.3.4. Bare stative entries (*rhiiynii*-class) only for the irreducibly internal cases.

### B.9 Avoiding GA-mapped lexicon

Specific tactics for keeping the conlang's verb territory genuinely divergent:

- **Don't ask "what's the conlang word for X."** Ask "what's the conlang's whole vocabulary for the territory X covers in GA," and expect the answer to involve multiple verbs splitting GA's range differently, plus possibly a stative-domain strategy.
- **Look for GA polysemy to split.** *Run* covers physical running, machines operating, organizations being directed, water flowing, candidates campaigning. The conlang's *run*-cognate may take only one, with the others recruited to different verbs entirely.
- **Look for GA distinctions to merge.** Where GA distinguishes two verbs the phonology collapses, the merged form may be enriched by frame disambiguation, or one sense may take over.
- **Identify GA volitional twins.** Pairs like *fall/drop*, *forget/put-out-of-mind*, *sleep/go-to-bed*, *learn/find-out* — does the conlang preserve both, merge them, or recruit them to different paradigm sides of a single verb?
- **Watch for sound-change-driven mergers.** When working derivations, flag cases where two semantically related GA stems will produce identical conlang forms. These are dictionary entries with multiple GA etyma — record both, with notes on which senses came from which source.
- **Check the deverbal nominal slot.** A verb without a recognitional-iterative paradigm is missing one dimension of its expressive range. Either find a GA construction that supplies one, or note that the verb lives in the frame dimensions only.
- **Look for GA stative meanings the strategies can recruit.** Before adding a stative entry, ask which activity-coercion, stimulus-promotion, or causative recruitments cover the territory. Often the entry isn't needed.
- **Default to the Tier 1 convergence zone** (self-care, cognitive activity, threshold-transition) when uncertain where to recruit next — these pay back recruitment effort with the highest expressive dividend.

### B.10 Polarity — held aside

The get-oneself paradigm and reading inventory have been worked out for positive polarity. Negative polarity is held in `verbal-system.md` §10 pending reconciliation. For diagnostic question 3 (Axis B coverage), apply only to the positive-polarity grid for now, recording negative-polarity behavior as observations rather than systematizing it. When the `verbal-system.md` §10 reconciliation is done, §B.2.2 will be updated. This is a known incompleteness, not a hidden assumption.

### B.11 What to record per verb

Beyond the dictionary's standard schema, verb entries should include:

- **Two-axis profile.** Axis A category and Axis B coverage (rich/medium/thin, with reading detail if useful).
- **GA construction inventory** — which GA uses survived, died, were reanalyzed.
- **Get-oneself paradigm coverage** — for each of the six productive cells, is it productive, coerced, or blocked? Which reading does the productive cell host? Example sentences for productive cells.
- **Go-ahead paradigm coverage** — for the three cells, productive, marked, or blocked?
- **Recognitional-iterative paradigm** — whether *the V-ing* and *the V-ings* are licensed, and the readings.
- **Stative-domain recruitment** (if applicable) — which activity-coercion / stimulus-promotion / causative recruitments share territory with this verb.
- **Mergers and competitors** — other GA verbs whose territory this verb has absorbed or shares.
- **Register notes** — intimate/formal, frequent/rare, marked uses.

This is more apparatus than current dictionary entries carry, and most of it can be deferred to a Notes section. But the two-axis profile and the two paradigm-coverage records should be in the entry from the start: they justify the verb's place in the lexicon and define how it interacts with the rest of the grammar.

---

## 9. Versioning Notes

### v3.11, June 2026 — existential example migrated to the centralized corpus (roadmap B1b)

The §4 existential example *pons rheĩ* "there is rain" was replaced with a `<!-- example: E019 -->` transclusion token, now sourced from `examples.md` and rendered at build time. No content change; the placeholder IPA line drops from display (greedy render). E019 was added to the corpus in the same B1b pass (a first-pass survey had missed it). See `examples.md` v0.4.

### v3.10, June 2026 — §3.4 orientation abstract regenerated; §8 skill bullets removed

**§3.4 orientation abstract** regenerated to match the corrected `verbal-system.md` Abstract (its v2.12): "the verb-lexicon-building methodology lives in its Appendix A" → "...in `language_reference.md` Appendix B." The copy had inherited the sibling Abstract's stale cross-reference.

**§8 "The document set"** — removed the two skill-file bullets (`skills/dictionary-updater.md`, `skills/reference-grammar-section-drafting-and-integration.md`). Those are authoring tooling, not part of the descriptive document set; they are documented in `CLAUDE.md`'s "Skills" section (and now live under `.claude/skills/`). Their paths were also stale post-migration. The manifest now lists only the canonical docs and out-of-tree working notes.

### v3.9, June 2026 — writing-style pass (front matter, §3.2.2, Appendix A)

Line-editing pass applying the writing-style prose canon; no content, claims, or status tags changed, and the orientation abstracts (§2, §3.4, §3.9) were left untouched per their never-hand-edit rule. **Front matter:** "for the conlang: an a priori conlang derived" → "for the conlang, an a priori language derived" (V4 — close *conlang/conlang* echo). **§3.2.2:** "has not survived as a definite article, and no general definite article" → "has not survived as such, and no general definite article" (V4 — *definite article* ×3 in one sentence). **Appendix A:** condensed the redundant second paragraph of the A.3 "On stability" discussion into one sentence (V4 restatement — it re-said the prior paragraph's "right origin / regular sound changes" point); parallelized the A intro's four-item scope list ("the method by which the language is constructed" → "its construction method", V5/V8); and gave the A.4.1 "untranslatable words" bullet a label-first shape matching its sibling bullet (V8). §1, §4–§8, and Appendix B reviewed and found conformant.

### v3.8, June 2026 — design/process content consolidated into Appendices A and B

**New Appendix A: The Design and Construction of the Conlang.** Conlanging-process content — design goals, construction method, typological models, lexicon-design intent — is pulled out of the descriptive body into a single design-context appendix, so the body is a synchronic description that references only diachronic development from GA. Relocations: **§1 Design Philosophy** → A.1 (§1 reduced to a one-paragraph premise + pointer); the **§5.1** etymological-engine methodology → A.2 (§5.1 trimmed to the descriptive lexicon-record statement); **§5.3**'s two lexicon-design notes (false friends, untranslatables) and the "drift serves identity" framing → A.4.1 (§5.3 keeps the drift typology, reworded from design-intent to description); **§5.4 Cultural Embedding** → A.4.2 (§5.4 reduced to a pointer); the **§8** "living specification / three purposes / LLM context" framing → A.5. §8 retitled "The document set" and keeps the manifest. Also relocated **in**: `phonology.md` §1.3 (typological precedents and stability) → A.3.

**New Appendix B: Building the Verb Lexicon — A Methodology.** `verbal-system.md`'s former Appendix A (the verb-lexicon-building recipe) is folded in here as Appendix B, rebased A.→B.; its bare `§N` references (to `verbal-system.md` §3/§6/§7/§8/§9/§10) are now filename-qualified. Inbound pointers updated: §5.1 and the §8 manifest now point at Appendix B; `verbal-system.md` §8/§16 and `terminology-registry.md` repointed in their own versioning notes. Companion bumps: `phonology.md` v4.7, `verbal-system.md` v2.10, `terminology-registry.md`. No body section was renumbered; quickrefs unaffected.

### v3.7, June 2026 — concord surface forms settled (B12); §7 closure

§7's highest-priority example gap, **"surface forms of the concord endings,"** is removed: the B12 elicitation settled the two principal shapes — PROG /‑ıĩ/, PRET coronal /‑ɾi ~ ‑t/ — now the fossil-resurrection morphophonology of `phonology.md` §4.4.14 and `verbal-system.md` §4.2.2 (v2.9). The surviving open item is narrowed to the **concord affix feature inventory** (what concord marks beyond shape). The §3.4 Verbs assembler (orientation abstract) still reads accurately — it names "concord shape" only at the summary level — so it is unchanged; the detail stays in the sibling. Minor propagation from the same B12 batch: §5.3's *rhiiyepplii* respelled *rhiiyeplii* (the *epplii* → *eplii* reanalysis; `dictionary.md` 2026-06-23, `phonology.md` v4.5).

### v3.6, June 2026 — ideophones spun out as a sibling (Session I, SAYING round)

New sibling `ideophones.md` created for the expressive layer (the SAYING round's largest finding; home ratified 2026-06-20). A §3.4-style stub was added as **§3.9 Ideophones** (assembly directive + orientation abstract); §3.1's word-class inventory now names the expressive class; the §8 document list and the "How to read" set were updated, the latter with the new **χ** gesture-channel convention (Greek *kheir*, "hand"). The forward-references planted in `verbal-system.md` §12.4, §4.2.3, and §10 now resolve. Source: `phase4-triage-saying-2026-06.md` §2.5.

### v3.5, June 2026 — syntax: existential pons, information structure, reciprocity (Session L, SAYING round)

**§4** gains: the **existential particle** *pons* (< *upon us*; "there is," the unmarked inanimate/weather predication, against which active framing is the marked, non-neutral option); an **information-structure** note (definite objects displaced from the core object slot, resumed by the *-et* clitic, cross-referencing the *þilnn* transfer case at `verbal-system.md` §13.2; the aboutness enclitic *-wiis* < *-wise*); and a **reciprocity** stub [Open] (we-subject get-oneself carries the mutual reading unmarked). Closes the Session-L round-2 work. Source: `phase4-triage-saying-2026-06.md` §3.10/§3.8/§3.13/§3.14.

### v3.4, June 2026 — discourse: reś evidential, clause linkers (Session L, SAYING round)

**§3.7.4** evidential-division-of-labor bullet updated from the retired appears particle *piies* to the **guess particle** *reś* (the general indirect evidential; the perceptible/non-perceptible split rides on visibility-particle choice, *reś* itself neutral between perception and inference). **§3.8** gains the **clause linkers** *rhishisben* (simultaneity/background, < *which is when / which has been*) and *kyii* (succession + mild causal, < *cue*), a clause-linking class distinct from the *nousso*-type stance connectives. Source: `phase4-triage-saying-2026-06.md` §1.2/§2.2/§3.12.

### v3.3, June 2026 — nominal/determiner: REC-ITER demotion landing (Session L, SAYING round)

**§3.2** made the canonical home for the demoted recognitional-iterative construction's determiner morphology: §3.2.1's frame-engagement reworded to route through the possession construction (`verbal-system.md` §13), with §7 now a back-pointer; the **etymological-doublet origin** (GA *the* → article *o* / recognitional *þ ~ y*; the Latin *ille* parallel) **moved here** from `verbal-system.md` §7.3 as a §3.2.2 Origin note. §3.2 Nouns gains the mass→count reanalysis (*riųś* "news" as a count noun) [Provisional]. A stale §3.1 cross-reference (§12 → §13) left over from the Quotation renumber was fixed. Header reconciled (was lagging at v3 while §9 carried v3.1/v3.2). Source: `phase4-triage-saying-2026-06.md` §2.3/§3.21. (Companion edit: `verbal-system.md` v2.8 reduces §7.3's Origin to a pointer here.)

### v3.2, June 2026 — nominal and discourse integration (Session L)

**§3.2** gains §3.2.1 (REC/ITER morphology — canonical home migrated from `verbal-system.md` §7.1/§7.4 per the demotion decision; surface forms *þ ~ y*, *-ś*; the three morphology-scoped open questions travel with it) and §3.2.2 (the definiteness ecology: merged article *o*, definite-object suffix *-et* [Provisional], visibility-particle givenness, definite coloring of dislocated topics). Possession bullet gains attested-items flags; distributive *-au* flagged. **§3.3** gains the *aų* X *hii* adjectival-predication pattern with the *hii* < *side* analysis flagged [Open] and the adjective-stress rule flagged for phonology. **§3.7**: homophony note for the know-that matrix particle (3.7.1); topic > matrix particle ordering and the right-periphery restriction (3.7.3); matrix-particle interaction bullet with the evidential division of labor (3.7.4); the verb-side *know* gap **closed** in 3.7.5 (filled by the know-that matrix particle — GA *know* grammaticalized twice and survives as a verb in neither layer) and removed from 3.7.7. **New §3.8** connective particles (*notto*, *nousso* ×2, *not·ho*). **§4** gains the periphery asymmetry and the matrix-government data point. §3.1, §3.6 pointers updated; §7 list adjusted (connectives, possession). Spin-out to `nominal-system.md` deliberately **not** executed: §3's own trigger ("the noun-side subsections reach maturity together") is unmet — possession, case, and plurals remain open. Sources: 2026-06-10 translation exercise; `phase4-triage-2026-06.md` §3; verbal-system v2.1.

### v3.1, June 2026 — cross-reference sweep for verbal-system v2.1

Cross-references to `verbal-system.md` updated for its v2.1 renumbering (former §11–§14 → §13–§16, accommodating new §11 The matrix particles and §12 The possession construction): §7 open-questions list (REC/ITER surface-form gap removed — closed by verbal-system v2.1; concord-endings gap retained), §8 document list, §9 prior-note pointer (§14 → §16). The §3.4 stub regenerated by re-copying the revised verbal-system Abstract (which the source document had lost while the stub retained the v2 copy — drift incident recorded in verbal-system v2.1). The REC/ITER morphology migration remains with the nominal-side session.


### v3, June 2026 — conformance pass: house-style canon and terminology registry adopted

**Stub-abstract model adopted (second pass on this draft, user decision June 2026).** §2 (retitled "Phonology and Orthography") and §3.4 converted from hand-maintained summaries to generated stubs — an assembly directive plus a copy of the sibling document's new Abstract; §3.5 converted to a plain pointer stub (the §3.4 directive covers `verbal-system.md` §5). Internal references into the removed §2.x/§3.4.x subsections retargeted at the siblings. §6 marked illustrative-only. The model is specified in skill v1.1 §1.5; the assembly script is pending.

**Front matter added.** A new unnumbered "How to read this document set" section consolidates the reading apparatus (etymon convention, status tags, four-line example format, gloss-tag channel, registry pointer, mora paraphrase, analytical-note convention). Section numbering is unchanged.

**Terminology.** All prose normalized to `terminology-registry.md` (June 2026 batch): *volitional go-ahead* / *non-volitional get-oneself* (shorthands *go-ahead* / *get-oneself*) replace *volitive* / *non-volitive*; *frame* and *frame aspect* replace prose *LVC* and *LVC.TAM*; the four readings are named *happenstance*, *effortful self-benefit*, *threshold*, *backdrop* (replacing PH/AB/INC/PS); *iterative marker* (ITER) replaces nominal *HAB*; §3.4.5 retitled *recognitional-iterative*; the visibility particles gain the prose names *see-particle* and *know-particle* (gloss tags VIS/NVIS unchanged); *prosodic appendix* used where document appendices are in scope.

**Voice.** Project-history narration removed from body prose: the document opener no longer narrates the latest revision; the *sesquisyllabic* retirement parenthetical is dropped from §2.2 (record remains in `phonology.md`); §3.7's etymological and grammaticalization material is consolidated under marked *Origin* blocks (§3.7.1, §3.7.5). A surviving mini-game reference in §4 ("storyteller, mystery, and letter-writing games") is removed, completing the v2.3 cleanup.

**Deduplication.** §5.2 and §5.3 trimmed to summaries pointing at the new canonical home `verbal-system.md` §8.4 (selection/reanalysis/loss and the semantic shift patterns); §5.3 retains only the lexicon-design notes specific to this document (false friends, untranslatables) and the *rhiiy-* worked example.

**Examples and flags.** GA-calque examples flagged `[Placeholder: …]` throughout (§3.4.3, §3.4.5, §3.7.2). New [Open] flags: example plural pairs (§3.2); REC/ITER and concord surface forms promoted into §7 as the highest-priority example gaps. §3.4.3's worked example upgraded to use the attested pronoun and frame forms.

**§8 document set updated.** Added `terminology-registry.md` and `skills/reference-grammar-section-drafting-and-integration.md`; `verbal-system.md` entry updated to its v2 section layout; superseded-documents entry simplified to point at the registry.

**Staleness repairs.** §2.1, §2.4, and §7 updated to reflect the `phonology.md` v2.3 closures (single phonemes /ɪ/ and /ɑ/ with [ɨ]/[ɔ] allophones; nasalization phonemic; breathy voice allophonic) that the v2.x summaries had not absorbed; the *sodium* headword updated from stale *hoiom* to the committed *hoiiǫ* /ˈhoiõ/ in §2.2 and §6.

**Cross-references.** `verbal-system.md` §A.3 references updated to §6/§A.3 per that document's v2; §3.7.5's strategy pointer now cites §6. No section renumbering in either document.

### v2.7, May 2026 — pronominal system summary added; verbal-system cross-references updated

**§3.5 Pronouns expanded.** The two-sentence placeholder is replaced by a proper high-level summary pointing at `verbal-system.md` §5 (The Pronominal System, added in verbal-system v1.3). Commitments documented: weak vs. strong pronoun paradigms; pronouns as aspect carriers; GO-AHEAD animacy agreement vs. GET-ONESELF person/number agreement; bare, imperfect, modal (would/could), and n't.quite negative fusions; restriction of modal fusions to pronouns; 2PL/3PL syncretism at modal/negative cells; strong pronoun three-reading system from GA *on [POSS] end*; intonation-only interrogative with *ea* particle [Provisional]; left dislocation with resumptive pronouns [Settled]; pro-drop and WERE irrealis [Open].

**Cross-references to `verbal-system.md` updated throughout** to reflect v1.3 renumbering (former §5–§13 shifted to §6–§14 to accommodate new §5): §6→§7 (recognitional-habitual), §7→§8 (verbs and verbal system), §8→§9 (open questions), §9→§10 (polarity), §13→§14 (versioning notes). Updated in §3.2, §3.4.4, §3.4.5, §5.1, §7, §8 document list, §8 superseded docs, and prior versioning notes.

### v2.6, May 2026 — pitch-residue summary propagation; skill pointer

**§2.2 pitch summary updated.** Propagates the v2.2 pitch-residue reframing from `phonology.md` §3.4. The placement claim (pitch on the syllable that carried GA primary stress) is unchanged. The summary now: drops the "separate prosodic dimension" framing; mentions the residue analysis (pitch as F0 residue of GA-style prominence after loudness and length transfer to the final vowel under final-stress); makes the etymologically-determined / not-synchronically-derivable distinction explicit, with the English lexical-stress comparison; and notes that low minimal-pair density is structurally expected under the residue analysis and is not on its own evidence about contrastiveness. Detail is held in `phonology.md` §3.4 per the no-duplication-upward rule; the §2.2 entry stays high-level.

**§8 document set list updated.** `dictionary-updater.md` was previously listed as out-of-tree. It is now in-tree as `skills/dictionary-updater.md` and the entry is repointed accordingly with a brief note pointing at `CLAUDE.md`'s "Skills" section for invocation.

### v2.5, May 2026 — verb-recipe folded into verbal-system Appendix A

**Cross-references repointed.** `verb-recipe.md` (formerly out-of-tree sibling working note) is now folded into `verbal-system.md` as Appendix A (see `verbal-system.md` v1.2 changelog). Repointed in lang_ref:
- §5.1 methodology pointer: "in `verb-recipe.md`" → "in `verbal-system.md` Appendix A".
- §3.7.5 stative-strategy reference: `verb-recipe-v2.md` §3 → `verbal-system.md` §A.3.
- §3.7.7 verb-side gap question: same.
- §8 document set list: `verb-recipe.md` line removed (no longer a sibling).

### v2.4, May 2026 — cross-document propagation and nominal-spinout placeholder

**§2.1 long-vowel summary updated.** Reflects the diphthongal long-vowel admission from `orthography.md` v2.1 and propagates the parallel inventory addition in `phonology.md` v2.1: long vowels are now framed as bimoraic nuclei in two surface types (monophthongal /iː, ɛː, oː, aː, ɨː/ and diphthongal /iɛ/).

**§3 lead paragraph anticipates a nominal-system spinout.** Notes that §3.4 is the verb-side summary pointing to `verbal-system.md` and that the noun-side subsections (§3.2, §3.3, §3.5, §3.6, §3.7) may eventually spin out into a sibling `nominal-system.md` once they mature together. §3.7 is identified as the natural anchor for that grouping; it stays in lang_ref pending the rest catching up.

### v2.3, May 2026 — pedagogical-game references stripped

**Rationale.** The grammar is now treated as a self-standing descriptive reference rather than as the language layer of an in-development game. References to the game, its mini-games, the player, and the in-world setting are removed throughout. The substantive content — open questions, design priorities, cultural-embedding gestures — is preserved on its own terms.

**§7 restructured.** The numbered list "in roughly the order they will be forced by the mini-game build sequence" is converted to a bulleted list of "areas where the grammar is not yet committed." Question groupings are preserved verbatim; the parenthetical mini-game labels (*phonology mini-game*, *ice cream shop*, *market*, *delivery*, *kitchen*, *lost-and-found*, *storyteller*, *mystery / witness*, *letter-writing*) are removed. The closing sentence on changelog protocol is rewritten to reference §"Versioning Notes" entries directly rather than the mini-game cadence.

**Smaller deletions.** Sentences referencing mini-game forcing are removed or reworded in §2.3, §3.2, §3.3, §3.5, §3.6, §5.3, and §5.4. The §8 closing reference to "in-world artifacts the player can read in the game's school and library" is dropped.

**v2.2 changelog entry trimmed.** The §3.7 changelog bullet on open questions is reworded to drop the "mini-game build sequence" framing while preserving the substance (questions are scoped to §3.7, not promoted to §7).

**Cross-document consequences.** Parallel cleanup is applied to `CLAUDE.md`, `orthography.md` §5, `verbal-system.md` (three open-question entries), and a `dictionary.md` entry note. See each affected file's own §"Versioning Notes" where applicable.

### v2.2, May 2026 — visibility-marked topic particles

**New §3.7 Demonstratives and topic particles.** Documents a closed set of two visibility-marked topic particles, grammaticalized from the imperatives of GA *see* and *know* and marking a fronted topic for [±VIS] (perceptibility-deictic). The set has fossilized bare, article-incorporating, and clausal forms (*hii*/*hiie*/*hiho*; *no*/*nou*/*noho*), reflecting historical incorporation of the GA article and of *how*. Sits alongside the recognitional-habitual nominal (§3.4.5) as the second flagged grammatical innovation on the nominal/discourse side; the two systems are orthogonal.

**§3.2 definiteness paragraph revised.** The closing sentence on definite reference is rewritten to point at the visibility-particle system as handling a substantial portion of the work, with the [Open] tag removed since a real mechanism is now in place.

**Open questions added.** Six new questions are flagged in §3.7.7: pragmatic NVIS extensions, stacking patterns, topic discontinuity, the *know*-as-stative verb-side gap, phonemic status of medial /h/ (cf. `orthography.md` §6), and clausal-form productivity. They are scoped to §3.7 and not promoted to §7.

**Cross-document propagation.** The orthographic shape *hiie* /iɛ/ forced the diphthongal long-vowel admission in `orthography.md` v2.1 (§3.3) — a generalization of the long-vowel system to two surface types (monophthongal and diphthongal). The *noho*/*hiho* medial-/h/ pattern raised a new open question on phonemic /h/ vs. breathy voice in `orthography.md` §6.

### v2.1, May 2026 — verbal-system spinout

**Verbal system spun out to sibling document.** A new document `verbal-system.md` has been created as a sibling to `phonology.md` and `orthography.md`. The verbal-system-description session of May 2026 produced a substantially refined paradigm structure (volitive vs. non-volitive, with four sub-modalities, two structurally blocked cells, and three stative-domain strategies) that warrants treatment as an independent reference.

**§3.4 Verbs trimmed to high-level summary.** Five subsections (§3.4.1–§3.4.5): tense-as-aspect; the volition system; the LVC and concord; polarity (new flag); the recognitional-habitual nominal. The verb-volition typology, deverbal nominal layer, and mood subsection from v2 §3.4 moved to `verbal-system.md`.

**Terminology shift: involitive → non-volitive.** The v2 document used *involitive* (sourced from Sinhala) as the marked term opposite *volitive*. The May 2026 verbal-system-description session worked with *modulated* as a positively-named alternative. v2.1 adopts *non-volitive* — privatively named for readability, with the principled-asymmetry argument preserved in prose framing rather than encoded in the term. See `verbal-system.md` §16 for the full terminology history.

**Polarity preserved with reconciliation flag.** v2 §3.4.2 had a four-cell VOL/INVOL × POS/NEG grid as the central organizing structure. In v2.1, polarity is preserved as a separate grammatical dimension (§3.4.4) but flagged as needing reconciliation with the cell × sub-modality structure described in `verbal-system.md`. The polarity discussion proper lives in `verbal-system.md` §10.

**Recognitional-habitual moved.** The full discussion of REC and HAB, including the DEF → REC grammaticalization and its open questions, has moved to `verbal-system.md` §7. A summary remains in language reference §3.4.5.

**Document set list updated (§8).** Added `verbal-system.md`, `verb-paradigm-verdict.md`, and `translation-frequency-task.md` to the sibling-document list. Marked `verb-terminology.md` as superseded; `verb-recipe.md` confirmed as sibling working note.

**Open questions list updated (§7).** Item 8 (mystery/witness commitments) expanded to reflect the new structure: sub-modality unification, AB billing, stative-strategy frequency, polarity reconciliation, concord affix inventory, LVC argument structure, nested negation glossing.

### v2, May 2026

Verb-terminology integration (volitive/involitive committed; LVC, concord affixes, REC/HAB committed); pitch-revision integration; phonology summary harmonized with `phonology.md` v2 and `orthography.md` v2. See full v2 changelog in earlier versions.

### v1 (original)

Original document. Established the design philosophy (§1), the phonology summary (§2), the morphology sketch (§3) with volition system and nested negation, the lexicon framing (§5), and the sample-forms anchor (§6).
