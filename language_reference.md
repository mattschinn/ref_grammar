# Language Reference: Working Sketch

**Version:** v3 (June 2026)
**Predecessor:** v2.7 and earlier — see §9 (Versioning Notes).

A starting-point descriptive grammar for the conlang: an a priori conlang derived from General American English (GA) through a designed cascade of regular sound changes and grammaticalizations. Many features are still under analysis; this document captures current commitments and flags open questions. It is the top-level document of a set — see §8 for the full document hierarchy.

---

## How to read this document set

Conventions used throughout this document and its siblings:

- **GA reconstructions** are written in italics with an asterisk (*sodium*), marking them as the proto-form. **Conlang surface forms** appear in plain italics (working orthography, diacritics included) or in slashes /…/ for phonological discussion.
- **Status tags:** **[Settled]** — committed; downstream design depends on it. **[Provisional]** — current best analysis, expected to hold but open to revision. **[Open]** — explicitly undecided, flagged for future commitment.
- **Examples** aim for a four-line format: conlang orthography, IPA, morpheme-by-morpheme gloss (Leipzig conventions), free translation. Where the conlang surface form is not yet derivable, a GA-calque stand-in is used and flagged `[Placeholder: …]` — unflagged calques are errors, not data.
- **Glossing** uses the compact tags registered in `terminology-registry.md` (VOL, NVOL, REC, ITER, VIS, NVIS, HAP, SELF.BEN, THRESH, BACK, …). Running prose spells terms out; each spelled-out term and its gloss tag are paired in the registry.
- **Terminology** follows `terminology-registry.md`, the canonical registry of the conlang's descriptive terms, their shorthands, and their naming history. A term marked there as retired may appear in older versioning notes but not in current prose.
- A **mora** — the unit of syllable weight, roughly one beat of vowel — appears throughout prosodic discussion: a short vowel is one mora, a long vowel two, a syllabic consonant one.
- **Abstracts and stubs.** Each sibling deep-dive document opens with an architecture-level **Abstract**. Sections of this document whose topic has a sibling contain only an assembly directive and a copy of that Abstract (an *orientation abstract* — non-normative, regenerated from the sibling, never hand-edited). The full grammar PDF is assembled as Part-per-document concatenation; cross-references are filename-based and survive assembly.
- **Analytical notes** (blockquotes beginning *Analytical note* or *Origin*) carry justification, history, and diachronic background. They are skippable: the body prose alone is a complete synchronic description.

---

## 1. Design Philosophy

The conlang's relationship to GA is not one of disguise but of *evolution under controlled conditions*. The intent is that:

- A native GA speaker who hears the conlang cold should not perceive it as English. The phonological distance should sit at roughly the French–Sicilian or Dutch–Swiss-German range, well beyond Spanish–Portuguese.
- The same speaker, given the GA cognate after the fact, should reach an *aha* — a sense that the form follows from regular processes.
- Sound shifts handle vocabulary; vocabulary is therefore *latent* rather than novel. The intellectual ambition lives in the grammar.
- Grammar reshapes the semantic space. New categories — the volitional go-ahead / non-volitional get-oneself system, polarity, and the recognitional-iterative nominal — emerge from grammaticalized GA function-words and phrases, slicing meaning differently than GA does.

The phonology is largely settled in its rule set, though some reanalyses are still being worked through. The grammar is more open and is being refined as design proceeds.

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

A closed class of grammaticalized markers carries volition, aspect, polarity, and defective person/number agreement (agreement that is real but does not distinguish every person/number combination). These appear bound to verbs in the **frame** (technically, the light verb complex) and behave as inflection rather than as independent words. A second grammaticalized pair — the **recognitional marker** (from GA *the*) and the **iterative marker** (from GA plural *-s*) — operates on deverbal nominals: morphology in §3.2.1, the construction they build with the frames in `verbal-system.md` §7 and §12.

### 3.2 Nouns

Noun morphology in the working draft is light. Number marking is consistent and largely transparent (deriving from GA *-s* and irregular plurals); irregular plurals tend to be preserved or have undergone independent sound changes that obscure the alternation. No derived plural forms have yet been entered in the dictionary to exemplify this. **[Open: example plural pairs pending dictionary work]**

Possession and case-like marking are still under design. Likely candidates for grammaticalization:

- A possessive marker from a fused GA *of*-construction. (Attested possession-adjacent items — *bauyǫ* "my own," *obii* "go by (a name)" — await dictionary entry. `[Lexicon: bauyǫ, obii pending]`)
- Locative/directional case-like elements from prepositions that have phonologically fused with their nominal heads (especially likely given the heavy elision processes).

These remain open pending further design work. A distributive element *-au* (from GA *all*) is attested fused onto object marking (*ŕeushiię·au* "cherishing it all"); its place in number marking is **[Open]**. `[Lexicon: -au pending]`

#### 3.2.1 The recognitional and iterative markers

Two grammaticalized morphemes operate on **deverbal nominals** — a verb's action treated as a noun:

- **Recognitional marker (REC)** — descended from GA *the*. Marks shared-knowledge type reference: "you know the kind." Not a definite article (`verbal-system.md` §7.3). Surface forms: *þ* before consonants, *y* /i/ before etymological vowels, inheriting the GA allomorphy.
- **Iterative marker (ITER)** — descended from plural *-s*. Adds a repeated-instances reading on top of the type-marking. Surface form: *-ś*.

They stack productively — REC alone gives shared-knowledge type reference; REC + ITER adds iterated instantiation — and are attested together in *þ rishś* "the dishes (you know the chore)." Glossing pattern: REC-stem-ITER. The construction they build with the verbal frames, and the helper-verb syntax it requires, are described at `verbal-system.md` §7 and §12; the etymological-doublet origin (GA *the* → referential *o*, recognitional *þ ~ y*) is at `verbal-system.md` §7.3.

Open questions, scoped to the morphology:

- **Does REC occur without ITER productively?** Bare REC (shared-knowledge type, non-iterative) is predicted licit; examples needed. **[Open]**
- **Does ITER occur without REC?** Bears on whether the two morphemes are independent or whether ITER requires REC as a host. **[Open]**
- **Scope of REC and ITER relative to other nominal morphology** (case-like marking, possession). **[Open]**

#### 3.2.2 Definiteness

The GA definite article *the* has not survived as a definite article, and no general definite article has re-emerged. Instead, definiteness is recapitulated across several smaller systems — syntax and pragmatics doing the work GA morphology did:

- **The merged article *o*.** GA *the* (in its referential use) and *a* collapsed into a single article *o*, neutral for definiteness: *Ritm o rhémstwè* "(I) got them the book." Its recognitional sibling *þ ~ y* is the other half of the doublet (§3.2.1).
- **The definite-object suffix *-et*** (from GA *it*), fused onto the verb, presupposing an already-established referent: *beųheun nou·et* "went ahead and committed it to memory." **[Provisional — distribution to be confirmed]** `[Lexicon: -et pending]`
- **The visibility particles** (§3.7) carry referent-tracking and shared-reference signaling through a [±VIS] dimension rather than a [±DEFINITE] one.
- **Dislocated topics are definite.** A topic postposed by right dislocation retains definite coloring even with its visibility particle stripped (§3.7.3).

The result is a definiteness *ecology* rather than a definiteness *category*: no single morpheme answers GA *the*, and learners coming from GA must redistribute its functions across the article, the object suffix, the particles, and topic syntax. **[Provisional as a system statement]**

### 3.3 Adjectives and Descriptive Modification

Adjective forms inherit largely from GA. Comparative and superlative formation is open. Adjective ordering and stacking conventions are open.

**Adjectival predication** uses the "on the X side" pattern: *aų* X *hii* — attested in *piies aų nibii hii* "it appears on the nippy side." The pattern combines with both volition axes ("going ahead toward the sick side" vs. "got ourselves on the sick side" — deliberate decline vs. happenstance affliction). `[Placeholder: volition-axis examples pending conlang surface forms]` The closing element *hii* is plausibly the regular reflex of GA *side* (/s/ → /h/ debuccalization, /aɪ/ → *ii*, final /d/ elided), which would make it homophonous with the see-particle; an alternative reflex *sii* also appears in working notes. **[Open: analysis of predicative *hii/sii* and its homophony with the see-particle]** Because *hii* carries the phrase-final stress, the adjective itself escapes the usual final-stress pattern. `[New rule needed: adjective stress under the stress-bearing predicative element]`

### 3.4 Verbs

<!-- assemble: verbal-system.md -->

> **Orientation abstract** — canonical content in `verbal-system.md`. This text is copied from that document's Abstract; edit it there, never here.
>
> The verbal system grammaticalizes the subject's relationship to the event: every framed verb commits to either the volitional go-ahead frame (the subject deliberately undertook the event) or the non-volitional get-oneself frame (the subject's relationship to the event is qualified in some other way). The go-ahead side is deliberately compact; the get-oneself side is richer, hosting four readings — happenstance, effortful self-benefit, threshold, and backdrop — selected jointly by frame aspect, concord shape, and the verb's own event structure. The frames do not stand alone: they combine with a pronominal system in which pronouns are aspect carriers, while the language's only tense lives in a small class of matrix particles that scaffold whole clauses with modal meaning. A possession construction derives having, getting, choosing, and giving from frame-plus-nominal combination, with the recognitional-iterative nominal as its deverbal special case; three stative-domain strategies carry the meanings the morphology cannot host. This document is the canonical reference for all of these systems; the verb-lexicon-building methodology lives in its Appendix A.

### 3.5 Pronouns

The pronominal system's canonical home is `verbal-system.md` §5: pronouns are aspect carriers — fusing aspect, modality, and negation — in weak (clitic) and strong (tonic) paradigms, with left dislocation and a resumptive pronoun as the route by which full noun phrases reach the system. No further content is held here; the §3.4 assembly directive covers the whole verbal-system document.

### 3.6 Adpositions and Spatial Language

Many GA prepositions have phonologically fused with their hosts and are on a path toward case-like behavior. The full system remains open.

A specific case worth flagging: *with* in the frame's complement structure (see `verbal-system.md` §12) appears to have grammaticalized from a preposition into a verbal-complementizer-like role. Whether this generalizes to other prepositions, and whether a productive case-like system emerges, is **[Open]**.

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
- **Matrix particles (`verbal-system.md` §11):** the topic phrase precedes the matrix particle, and under the appears particle the choice of visibility particle carries an **evidential division of labor** — *hiie ossii, piies aų nibii hii* "look at the outside — it *looks* nippy" (perceptible evidence) versus *nou ossii, piies aų nibii hii* "you know the outside — it *seems* nippy" (non-perceptible evidence). The GA *look*/*seem* contrast survives as particle choice rather than as two verbs.

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

---

## 4. Syntax

Largely deferred. Working assumptions:

- Word order is broadly SVO, inherited from GA, but topic-prominent fronting may be more common than in GA.
- Question formation beyond yes/no (see `verbal-system.md` §5.5), relative clauses, and complement clauses are open.
- The interaction of volition marking with subordinate clauses is a question of particular interest — does an embedded verb inherit volition from the matrix, or carry its own? **[Open]** First adjacent data: a clause scaffolded by the end-up matrix particle keeps its own frame but surrenders its **aspect** to the particle's government (`verbal-system.md` §11.3).
- **Periphery asymmetry:** left dislocation is marked with a visibility particle; right dislocation strips it and is tagged with the strong-pronoun *on-X-end* phrase (§3.7.3; `verbal-system.md` §5.4). **[Provisional]**
- The argument structure of the frame: bare-nominal complements vs. preposition-mediated complements. **[Open]** See `verbal-system.md` §4.1.

---

## 5. Semantics and the Lexicon

### 5.1 The Etymological Engine

The lexicon is generated, not listed. Each entry is fundamentally:

- A **GA etymon** (the proto-form).
- A **gloss** (intended conlang meaning, which may or may not match the GA word's meaning).
- **Semantic drift notes** where the conlang meaning has diverged.
- **Irregular form overrides** for the small number of forms that resist regular derivation.

Surface forms are produced by running the etymon through the sound-change applier. Adjusting a sound rule regenerates surface forms across the lexicon. The dictionary (`dictionary.md`) is the canonical lexicon record; the methodology for building its verb side is in `verbal-system.md` Appendix A, with the descriptive-grammar side in `verbal-system.md` §8.

### 5.2 The lexicon inherits GA verb uses, not GA verbs

The conlang's verb territory is carved differently from GA: what survives are specific GA *constructions* — shaped by selection (frequency, colloquial grammaticalization, fit with conlang grammar), reanalysis into the conlang's systems, and loss-with-replacement where sound change collapses forms. Homophonous merger from sound change is itself a productive lexical source: the frames and the reading grid do the disambiguating work GA did segmentally. The canonical treatment is `verbal-system.md` §8.4.

### 5.3 Productive Semantic Drift

The lexicon is *not* a one-to-one mapping of GA words to conlang forms. Drift is encouraged where it serves the conlang's identity: **narrowing** (*countenance* → *hoʔnʔnts*, "face" specifically), **broadening** (*rhiiynii* extends GA *need* to also cover "want"), **specialization driven by grammar**, and **accretion of grammatical material** into stems (the *rhiiy-* prefix from bleached *really* — fully grammaticalized in *rhiiynii* "to need" and *rhiiysseunnou* "to be different," still transparent in *rhiiyepplii* "to apply oneself" — is the worked example of this stratification). The shift patterns are treated canonically in `verbal-system.md` §8.4; two lexicon-design notes specific to this document:

- **Productive false friends.** Words that look like their GA cognates but have meaningfully shifted, occasionally in misleading directions. Pedagogically useful: they punish lazy back-translation and reward genuine engagement with the conlang's meanings.
- A small inventory of **"untranslatable" words** — concepts the conlang lexicalizes that GA does not — is a design priority. These anchor the cultural texture of the conlang's setting and require learners to acquire concepts rather than mappings.

### 5.4 Cultural Embedding

The conlang is spoken by anthropomorphic-animal residents of a planet. Their culture, customs, and social structures are still being designed, but should be reflected in the lexicon's organization:

- Greeting and politeness vocabulary tied to time of day, social distance, or occasion.
- Specialized vocabulary for whatever this culture cares about (a space-station town might have rich vocabulary for travel, weather, supplies, longing).
- Volition-marked idioms that reveal cultural attitudes toward intentionality, accident, and obligation.
- Recognitional-iterative idioms that reveal what shared-knowledge events the speakers treat as cultural touchstones.

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
- **Nominal possession marking** (predicative possession is settled — `verbal-system.md` §12), **relative-clause-like constructions**, **descriptive extension.**
- **Aspect system** in extended discourse.
- **Volition paradigm refinement** (reading-inventory unification, self-benefit billing, stative-strategy frequency); **polarity reconciliation** with the cell × reading structure; **concord affix inventory and surface forms**; **frame argument structure**; **nested negation glossing convention**. See `verbal-system.md` §9 and §10.
- **Surface forms of the concord endings** — the highest-priority example gap (`verbal-system.md` §4.2, §14).
- **Written register**, formal vs. casual contrasts.

Each commitment, once made, is recorded in the affected document's §"Versioning Notes" entry with date and reasoning, and its consequences are propagated through the lexicon engine.

---

## 8. Methodological Note

This document is a living specification, refined as design proceeds and explicitly versioned. It serves three purposes simultaneously: a working reference for the designer, the canonical context to feed into LLM-assisted conlang reasoning, and the seed of an eventual full descriptive grammar.

The project's current document set:

- **`language_reference.md`** (this document) — top-level descriptive grammar. Carries the front matter, the design philosophy, orientation stubs for the sibling documents, and canonical content for topics without a sibling (nominal morphology, syntax, the lexicon framework, the visibility particles).
- **`phonology.md`** — full phonological reference. Inventory, sound-change rules, derivational cascade, metrical analysis.
- **`orthography.md`** — full orthographic reference. Diacritic conventions, length and gemination conventions, pitch and nasalization placement.
- **`verbal-system.md`** — full reference for the verbal system. Go-ahead and get-oneself paradigms and frame forms (§2–§4); the pronominal system (§5); stative-domain strategies (§6); recognitional-iterative nominal (§7); verbs and the verbal system (§8); open questions (§9); polarity and negation (§10); matrix particles (§11); possession construction (§12); mood (§13); assembled clauses (§14); verb-lexicon methodology (Appendix A).
- **`terminology-registry.md`** — canonical registry of descriptive terminology: each term's shorthand, gloss tag, plain-language definition, status, and full naming history.
- **`dictionary.md`** — the lexicon, with per-entry sound-change derivations and a running changelog.
- **`skills/dictionary-updater.md`** — the procedure for adding dictionary entries. Invoked with "Let's update the dictionary"; see `CLAUDE.md` "Skills."
- **`skills/reference-grammar-section-drafting-and-integration.md`** — the procedure for drafting and integrating reference-grammar sections, including the house-style canon this document set follows.
- **`verb-paradigm-verdict.md`** — sibling working note: cell-by-cell predictions and analytical history for the verbal-system paradigm.
- **`translation-frequency-task.md`** — instrument for gathering usage-weighted data on stative-strategy frequency, reading-inventory unification, and other open questions in `verbal-system.md` §9.

### Superseded documents

- **`verb-terminology.md`** (May 2026, retired) — superseded by `verbal-system.md`. The terminology committed there is preserved through `terminology-registry.md`, which also records the subsequent renames. The file is no longer maintained.

---

## 9. Versioning Notes

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
