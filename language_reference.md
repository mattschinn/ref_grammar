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

## 2. Phonology

This section is a high-level summary. The full phonological reference is `phonology.md`, the canonical source for inventory details, sound-change rules, the derivational cascade, and the metrical analysis.

### 2.1 Inventories at a glance

**Vowels.** Short /i, ɪ~ɨ, ɛ, o, ɑ~ɔ/ plus diphthongs /ei, oe, ia/. Long vowels are bimoraic nuclei in two surface types: *monophthongal* /iː, ɛː, oː, aː, ɨː/ (with /iː/ established as a phoneme arising principally from /ɪji/-smoothing), and *diphthongal* /iɛ/ (the second mora supplies a distinct vowel quality rather than length). See `phonology.md` §2.2 and `orthography.md` §3.2–3.3.

Vowels also contrast in nasalization, breathy voice, and pitch in some environments. Nasalization, breathy voice, and (placement-of) pitch are robustly attested; their full phonemic status is still being analyzed.

**Consonants.** A reduced inventory relative to GA, reorganized: stops /b, t, ʔ/ (no /k/ as phoneme — surface [k] is allophonic /h/ before glide); fricatives /θ, h, ts, s/; nasals /n, m/; liquids/tap /r, l, ɻ/; glides /w, j/ (also serving as syllabic consonants in appendix position). A geminate sub-inventory /sː, nː, pː/ is attested.

Coda /ʔ/ is the most stable coda segment. /k/ and /l/ occur only in clusters. Voiceless sonorants /n̥, m̥, ɾ̥/ surface from elided coda obstruents and from the M1 / C-Coal mechanism.

**Notable inversions relative to GA.** /s/ debuccalizes to /h/ in most positions — that is, the consonant loses its mouth posture and surfaces as a bare /h/; /d, dʒ, n, j, g, v/ all merge into the alveolar tap /ɾ/; /m, p/ merge with /b/ in onset; /f/ merges with /θ/; /w, j/ merge with /ɻ/; /ɻ/ then assimilates to /r/ near another /r/. Most of the remaining sounds occur in GA; the strangeness is in their patterning.

### 2.2 Syllable structure, foot, stress, pitch

The language permits both substantial vowel clusters (*hoiom* "salt") and substantial consonant clusters (*hoʔnʔnts* "face"; *ritsstw* "Rochester"). Vowel clusters arise from intervocalic consonant elision; consonant clusters from systematic schwa elision in unstressed positions.

Syllabic consonants (/n, m, s, θ, ʔ, w, j/, possibly /r/) serve as syllable nuclei. They occur predominantly in **prosodic appendix position** — material adjoined to the prosodic word at a level above the foot, weight-bearing but stress-invisible. *countenance* /ˈhoʔn̩ʔn̩ts/ has up to four post-stress nuclei in this appendix zone. See `phonology.md` §3.5.

**Stress** falls on the final vocalic position of a word, where "vocalic" includes syllabic consonants but not appendix material. Feet are trochaic (left-headed) and built right-to-left; the rightmost foot is the head foot and bears primary stress. **Light-monosyllabic feet are licensed** (cf. *ŕe* /ˈr̥ɛ/ "today").

**Pitch** falls on the syllable that carried primary stress in the GA etymon, regardless of where conlang stress has migrated to. Pitch and stress are usually on **different** syllables — most multisyllabic GA etyma had initial stress, which has migrated rightward while pitch stayed put. This dissociation produces the characteristic prosodic shape: *Emma* /ɛma/ has pitch on /ɛ/, stress on /a/. The current analysis (per `phonology.md` §3.4) treats pitch as the **phonetic residue of GA-style prominence** after loudness and length transfer to the final vowel under the final-stress rule, rather than an independently assigned prosodic dimension. Placement is settled and etymologically determined, but it is not synchronically derivable from the surface form — the same epistemic status English lexical stress has. Whether placement is contrastive — whether minimal pairs distinguishable only by pitch placement actually exist — is **[Open]** pending audio-recorded verification; under the residue analysis, low minimal-pair density is structurally expected and not in itself evidence about contrastiveness.

### 2.3 Orthography

Latin script with diacritics, in the manner of Vietnamese — diacritics are load-bearing rather than decorative. They encode vowel length, vowel nasalization, breathy voice, consonant devoicing, consonant gemination, pitch (always written), stress (predictable, normally unwritten; marked in formal/pedagogical text), and pitch-stress coincidence. The full orthographic reference is `orthography.md`.

A pedagogical implication: ignoring diacritics produces homophone collisions. The earliest learning materials are built around minimal pairs distinguished only by these marks.

### 2.4 Open phonological questions

A short list; the full list lives in `phonology.md` §5.

- **Phonemic vs. allophonic status** of /ɪ~ɨ/, /ɑ~ɔ/, nasalization, breathy voice. (Pitch *placement* is settled; pitch *contrastiveness* remains open as a separate question.)
- **Conditioning of /ai/**, now a three-way reflex /iː/ ~ /eː/ ~ /i/.
- **Coda /l/ elision paths.** Multiple paths flagged; full description deferred.
- **Appendix system details.** Licensing conditions, internal structure, interaction with pitch.

---

## 3. Morphology

This section is more provisional than the phonology, though several pieces are now settled enough to commit. The verb system is treated as a sibling document (`verbal-system.md`); §3.4 below summarizes and points there.

The noun-side subsections (§3.2 Nouns, §3.3 Adjectives, §3.5 Pronouns, §3.6 Adpositions, §3.7 Demonstratives and topic particles) currently live in this document. If they reach maturity together — most are still light or open — they may spin out into a sibling `nominal-system.md` parallel to `verbal-system.md`. §3.7 is the most developed of the set and the natural anchor for that future grouping; pending the spin-out, §3.7 is the *canonical home* for the visibility-particle system and is therefore deeper than this document's usual summary altitude.

### 3.1 Word-Class Inventory

The major content classes — nouns, verbs, adjectives — are inherited from GA and largely intact, though boundaries blur where grammaticalization has fused phrases.

A closed class of grammaticalized markers carries volition, aspect, polarity, and defective person/number agreement (agreement that is real but does not distinguish every person/number combination). These appear bound to verbs in the **frame** (technically, the light verb complex) and behave as inflection rather than as independent words. A second grammaticalized pair — the **recognitional marker** (from GA *the*) and the **iterative marker** (from GA plural *-s*) — operates on deverbal nominals. Both are described in `verbal-system.md`.

### 3.2 Nouns

Noun morphology in the working draft is light. Number marking is consistent and largely transparent (deriving from GA *-s* and irregular plurals); irregular plurals tend to be preserved or have undergone independent sound changes that obscure the alternation. No derived plural forms have yet been entered in the dictionary to exemplify this. **[Open: example plural pairs pending dictionary work]**

Possession, definiteness, and case-like marking are still under design. Likely candidates for grammaticalization:

- A possessive marker from a fused GA *of*-construction.
- Locative/directional case-like elements from prepositions that have phonologically fused with their nominal heads (especially likely given the heavy elision processes).

These remain open pending further design work.

A note on definiteness specifically: the GA definite article *the* has not survived as a definite article. It has grammaticalized into the recognitional marker on deverbal nominals (see `verbal-system.md` §7). Definite reference, where needed, is conveyed through other means: the visibility particles handle a substantial portion of the work (see §3.7), with possessives and context filling in elsewhere. A general definite-article system has not re-emerged and is not expected to.

### 3.3 Adjectives and Descriptive Modification

Adjective forms inherit largely from GA. Comparative and superlative formation is open. Adjective ordering and stacking conventions are open.

### 3.4 Verbs

Verbs carry the greater part of the language's grammatical innovation. The full reference is `verbal-system.md` (sibling document, parallel to `phonology.md` and `orthography.md`); this section is a high-level summary.

#### 3.4.1 Tense has largely become aspect

The historic present, common in colloquial GA narration, has generalized. Combined with the loss of distinct past-tense morphology in many forms (through sound change collapsing distinctions), the system functions more as an aspectual one than a tense one.

The frame's aspect cells cover habitual, progressive, past, and perfect, with the perfect cell structurally absent on the go-ahead side (see `verbal-system.md` §2.2). Time reference is conveyed lexically (adverbs, time phrases) or contextually rather than by inflection.

#### 3.4.2 The volition system: go-ahead vs. get-oneself

The most distinctive grammatical feature. Every framed verb commits to the subject's relationship to the event, on a contrast between two paradigm sides:

- The **volitional go-ahead** (shorthand: *go-ahead*) — the subject deliberately undertook the event. Compact paradigm: three frame aspect cells, single concord shape. From GA *go ahead and-*.
- The **non-volitional get-oneself** (shorthand: *get-oneself*) — the subject's relationship to the event is qualified in some way other than straightforward agency. Richer paradigm: four frame aspect cells × two concord shapes (six productive cells, two structurally blocked), hosting four readings — **happenstance** (it simply befell the subject), **effortful self-benefit** (brought about on the subject's own behalf, with effort), **threshold** (on the approach to a tipping point), and **backdrop** (the ongoing scene against which something else happens). From GA *get oneself-*.

The asymmetry — go-ahead small, get-oneself structured — is principled: deliberateness is a single value, while non-straightforward agency fans out into several. The go-ahead frame is incompatible with stative verbs; the get-oneself frame restricts the self-benefit reading but admits the other three for statives.

The contrast cuts the action space differently from GA:

> *I went to bed* (go-ahead) vs. *I fell asleep* (get-oneself, happenstance)
> *I deliberately bought myself a cake* (get-oneself, self-benefit) vs. *I happened to be eating cake when she walked in* (get-oneself, backdrop)

GA can express all of these, but only by choosing different verbs or adding adverbial material. The conlang grammaticalizes the distinction directly.

For the cell × reading grid, the four readings, the two structurally blocked cells, the three stative-domain strategies (activity-coercion, stimulus-promotion, causative) that handle territory the morphology cannot host, and the open questions about the system's structure, see `verbal-system.md`.

#### 3.4.3 The frame and main-verb concord

The grammaticalized auxiliary unit is the **frame** (technically the light verb complex, LVC), derived from fused GA periphrases and carrying volition, frame aspect, and defective person/number agreement. The main verb takes a **concord affix** showing concordance with the frame; in the get-oneself paradigm, the concord shape (infinitive-shaped vs. progressive-shaped) selects the reading.

Worked example:

> *eu oheun relaxin* — `[Placeholder: main-verb surface form pending]`
>
> 1SG    go.ahead.LVC.VOL.HAB    relax-CONCORD
> "I deliberately relax (as a habit)"

For frame morphological status, agreement features, argument structure, concord-affix questions, and fuller assembled clauses, see `verbal-system.md` §4 and §12.

#### 3.4.4 Polarity

A **polarity** dimension (positive vs. negative) operates alongside volition, with negative values grammaticalized from GA *pass on-* (go-ahead negative — declining) and *not quite-* (get-oneself negative — falling short). Productive **nested negation** stacks the markers to derive obligation: "cannot fail to do" → "must do." How polarity distributes over the full cell × reading paradigm is under reconciliation; the discussion lives in `verbal-system.md` §10.

#### 3.4.5 The recognitional-iterative nominal construction

A second grammaticalized construction — independent of the go-ahead/get-oneself paradigm — operates on **deverbal nominals** (a verb's action treated as a noun, GA's gerund territory). The **recognitional marker** (REC, from GA *the*) marks shared-knowledge type reference; the **iterative marker** (ITER, from plural *-s*) adds a repeated-instances reading.

> *{went-ahead-with the-snooze-s}* — `[Placeholder: conlang surface forms pending]`
>
> go.ahead-AGR=LVC.VOL.PST    with    REC-snooze-ITER
> "(I) deliberately did the napping-thing (you know the kind, the recurring sort)"

This sits alongside the volition category as one of the language's two flagship grammatical innovations. For full detail, see `verbal-system.md` §7.

### 3.5 Pronouns

The pronominal system is described in `verbal-system.md` §5. Key commitments:

- Two paradigms: **weak (clitic)** pronouns (default subject expression) and **strong (tonic)** pronouns (emphatic, possessive, topic/frame functions).
- **Pronouns are aspect carriers.** Weak pronouns fuse with aspect, modal, and polarity markers. A noun subject cannot carry these fusions directly — it requires a resumptive weak pronoun via left dislocation.
- **Agreement asymmetry.** GO-AHEAD (the go-ahead frame) agrees for animacy only; GET-ONESELF (the get-oneself frame) agrees for full person and number.
- **Weak pronoun fusions:** bare (habitual), imperfect (+be), prospective/conditional (would), ability modal (could), and not-quite negative (habitual and perfective cells). The modal fusions are restricted to pronouns — no nominal-subject modal construction without a resumptive pronoun.
- **Defectiveness.** 2PL and 3PL are syncretic with their singular counterparts at the modal and negative cells.
- **Strong pronouns** derive from GA *on [POSS] end* and carry three readings (emphatic, possessive, topic/frame) on a single form.
- Interrogatives form by intonation; no do-inversion. Yes/no questions add the particle *ea* (from GA *at all*) at clause end. **[Provisional]**
- Pro-drop conditions and the WERE-based irrealis particle are **[Open]**.

Animacy distinctions are committed for the weak pronoun paradigm (animate vs. inanimate at 3SG, with inanimate restricted to 3SG.INANIM). Politeness distinctions are not yet committed.

### 3.6 Adpositions and Spatial Language

Many GA prepositions have phonologically fused with their hosts and are on a path toward case-like behavior. The full system remains open.

A specific case worth flagging: *with* in the frame's complement structure (see §3.4.5's example) appears to have grammaticalized from a preposition into a verbal-complementizer-like role. Whether this generalizes to other prepositions, and whether a productive case-like system emerges, is **[Open]**.

### 3.7 Demonstratives and topic particles

The conlang has a closed set of two **visibility particles**, grammaticalized from the imperatives of GA *see* and *know*: the **see-particle** and the **know-particle**. They mark a fronted topic constituent for a [±VIS] feature, where VIS encodes presence and perceptibility while NVIS covers absent, abstract, generic, and discourse-given referents.

This is the second of the language's flagged grammatical innovations on the nominal/discourse side, alongside the recognitional-iterative nominal (§3.4.5). The two systems are orthogonal: REC/ITER is verbal-system morphology operating on deverbal nominals, while the visibility particles are pure information-structure marking on any topic constituent. They can co-occur on the same noun phrase without interaction.

#### 3.7.1 Inventory and forms

The particles are **fossilized**: not verbs, not imperatives, not inflecting. They show a single morphological alternation — a fossilized portmanteau pattern reflecting historical incorporation of the GA article — but speakers do not synchronically decompose the long forms.

| Particle | Gloss | Bare form | Article-incorporating form | Clausal form |
|---|---|---|---|---|
| **See-particle** (present, perceptible) | VIS | *hii* /hi/ | *hiie* /hiɛ/ | *hiho* /hiho/ |
| **Know-particle** (absent, abstract, generic) | NVIS | *no* /no/ | *nou* /noː/ | *noho* /noho/ |

The bare form occurs before article-less nominals (proper nouns, pronouns, bare nouns where no article would have been present). The article-incorporating form occurs before what was historically an article-bearing nominal. The clausal form introduces a clausal topic.

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

- **Position:** strictly clause-initial. The particle precedes the topic constituent, which precedes the comment.
- **Scope:** marks a single topic constituent — a noun phrase or a clause (the latter via the clausal forms *noho*/*hiho*).
- **Stacking:** multiple topic-particle phrases in sequence are licensed, allowing chained topics with mixed visibility (*hiie* X, *no* Y, ...). Worked examples await further data.
- **Negation, questioning, embedding:** the particles do not combine with negation, do not occur in questions, and do not embed under matrix predicates. They are root-clause information-structure marking.
- **Topic discontinuity:** whether the topic constituent can be discontinuous (split between particle and comment by intervening material) is **[Open]**.

#### 3.7.4 Interaction with other systems

- **Recognitional-iterative nominal (§3.4.5):** orthogonal. A topic constituent can independently bear REC and/or ITER on a deverbal nominal head. The particles do not select for or block them.
- **Volition (§3.4.2):** orthogonal. Topic-particle marking is on the topic noun phrase or clause, not on the predicate; volition is on the predicate's frame. They co-occur freely.
- **Definiteness:** the visibility particles handle a substantial portion of what GA conveys with the definite article — referent-tracking and shared-reference signaling — but through a [±VIS] dimension rather than a [±DEFINITE] one. The conlang has no definite article and is not expected to develop one.

#### 3.7.5 Origin

The grammaticalization path *imperative-of-perception-verb → demonstrative / topic particle* is well-attested cross-linguistically (Latin *ecce*, French *voici/voilà*, similar uses in Mandarin and elsewhere). The visibility distinction is also typologically standard for demonstrative systems with deictic-perceptual marking.

The recruitment of GA *know* into the particle system, rather than into the verbal lexicon, has a side effect on the verb side: the canonical GA stative *know* is not expected to survive as a lexical verb. The lexical-stative gap left behind will be filled by other strategies — most likely the activity-coercion or stimulus-promotion routes from `verbal-system.md` §6, or possibly a *rhiiynii*-class bare stative entry. The decision is deferred (§3.7.7).

#### 3.7.6 Glossing

- **VIS** — see-particle (perceptible / present topic).
- **NVIS** — know-particle (non-perceptible / abstract / generic topic).

The bare and article-incorporating forms are not separately glossed at the morpheme level — the alternation is fossilized. Where the article-incorporating form occurs, it may optionally be noted as `VIS+art` or `NVIS+art` in pedagogical contexts to flag the historical structure. The clausal forms are glossed `VIS-CLAUSAL` and `NVIS-CLAUSAL`.

A separate `TOP` gloss is not used: these particles are inherently topic-marking, and stacking `TOP.VIS` would be redundant. If the conlang later develops a topic-marking construction without visibility, `TOP` may be added then.

#### 3.7.7 Open questions

- **Pragmatic know-particle extensions.** Discourse-given vs. discourse-new readings, expected to develop but not yet committed.
- **Stacking patterns.** Worked examples needed to determine whether mixed-visibility chained topics are pragmatically natural and what the ordering constraints are.
- **Topic discontinuity.** Whether material can intervene between the particle-marked topic and the comment.
- **The verb-side gap.** What strategy fills the *know*-as-stative gap on the verb side. Tied to the broader stative-domain recruitment plan in `verbal-system.md` §6 and §A.3.
- **Phonemic status of medial /h/.** See `orthography.md` §6 history and `phonology.md` §2.3. Bears on whether *noho* / *hiho* need disambiguating notation.
- **Clausal-form productivity.** Whether *noho* and *hiho* are the only fused-with-*how* clausal particles, or whether further fusions (with *what*, *that*, etc.) might exist or develop.

---

## 4. Syntax

Largely deferred. Working assumptions:

- Word order is broadly SVO, inherited from GA, but topic-prominent fronting may be more common than in GA.
- Question formation beyond yes/no (see `verbal-system.md` §5.5), relative clauses, and complement clauses are open.
- The interaction of volition marking with subordinate clauses is a question of particular interest — does an embedded verb inherit volition from the matrix, or carry its own? **[Open]**
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

A small handful of attested derivations to anchor the system. See `dictionary.md` for the full record and `phonology.md` §4.5 for the worked-derivation tables.

| GA etymon | Conlang | Gloss | Notes |
|---|---|---|---|
| *sodium* | *hoiom* | "salt" | /s/ → /h/; intervocalic /d/ elision; resulting hiatus |
| *countenance* | *hoʔnʔnts* | "face" | Heavy schwa elision; prosodic appendix with multiple syllabic-consonant nuclei |
| *Rochester* | *ritsstw* | (toponym) | /st/ → /ts/; vowel elision; appendix /w̩/ |
| *carrot* | *ŕeut* | "carrot" | M1 rhotic metathesis; /h/ as devoicing feature on tap |
| *today* | *ŕe* | "today" / "now!" | Light-monosyllabic foot; high-frequency irregular shifts |
| *pass out* | *beussou* | "to fall asleep" | Geminate /sː/ at stressed-syllable boundary; lexical /ʔ/-drop |
| *really need* | *rhiiynii* | "to need / want" | /ɪji/-smoothing → /iː/; bleached *really* prefix |

---

## 7. Open Questions and Next Commitments

Areas where the grammar is not yet committed:

- **Phonemic vs. allophonic status** of /ɪ~ɨ/, /ɑ~ɔ/, nasalization, breathy voice; **pitch contrastiveness** (placement is settled).
- **Number marking** and basic noun morphology. **Politeness register** and greeting forms. **Numerals.**
- **Adjective system**, ordering, and modification.
- **Locative/directional case-like marking**; **motion verb morphology.**
- **Imperatives** and sequential connectives.
- **Possession**, **relative-clause-like constructions**, **descriptive extension.**
- **Aspect system** in extended discourse.
- **Volition paradigm refinement** (reading-inventory unification, self-benefit billing, stative-strategy frequency); **polarity reconciliation** with the cell × reading structure; **concord affix inventory and surface forms**; **frame argument structure**; **nested negation glossing convention**. See `verbal-system.md` §9 and §10.
- **Surface forms of REC and ITER**, and of the concord endings — the highest-priority example gaps (`verbal-system.md` §4.2, §7.1, §12).
- **Written register**, formal vs. casual contrasts.

Each commitment, once made, is recorded in the affected document's §"Versioning Notes" entry with date and reasoning, and its consequences are propagated through the lexicon engine.

---

## 8. Methodological Note

This document is a living specification, refined as design proceeds and explicitly versioned. It serves three purposes simultaneously: a working reference for the designer, the canonical context to feed into LLM-assisted conlang reasoning, and the seed of an eventual full descriptive grammar.

The project's current document set:

- **`language_reference.md`** (this document) — top-level descriptive grammar. Carries the design philosophy, a phonology summary, the morphology-and-syntax-and-lexicon framework, and high-level summaries pointing at sibling documents.
- **`phonology.md`** — full phonological reference. Inventory, sound-change rules, derivational cascade, metrical analysis.
- **`orthography.md`** — full orthographic reference. Diacritic conventions, length and gemination conventions, pitch and nasalization placement.
- **`verbal-system.md`** — full reference for the verbal system. Go-ahead and get-oneself paradigms and frame forms (§2–§4); the pronominal system (§5); stative-domain strategies (§6); recognitional-iterative nominal (§7); verbs and the verbal system (§8); open questions (§9); polarity and negation (§10); mood (§11); assembled clauses (§12); verb-lexicon methodology (Appendix A).
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

### v3, June 2026 — conformance pass: house-style canon and terminology registry adopted

**Front matter added.** A new unnumbered "How to read this document set" section consolidates the reading apparatus (etymon convention, status tags, four-line example format, gloss-tag channel, registry pointer, mora paraphrase, analytical-note convention). Section numbering is unchanged.

**Terminology.** All prose normalized to `terminology-registry.md` (June 2026 batch): *volitional go-ahead* / *non-volitional get-oneself* (shorthands *go-ahead* / *get-oneself*) replace *volitive* / *non-volitive*; *frame* and *frame aspect* replace prose *LVC* and *LVC.TAM*; the four readings are named *happenstance*, *effortful self-benefit*, *threshold*, *backdrop* (replacing PH/AB/INC/PS); *iterative marker* (ITER) replaces nominal *HAB*; §3.4.5 retitled *recognitional-iterative*; the visibility particles gain the prose names *see-particle* and *know-particle* (gloss tags VIS/NVIS unchanged); *prosodic appendix* used where document appendices are in scope.

**Voice.** Project-history narration removed from body prose: the document opener no longer narrates the latest revision; the *sesquisyllabic* retirement parenthetical is dropped from §2.2 (record remains in `phonology.md`); §3.7's etymological and grammaticalization material is consolidated under marked *Origin* blocks (§3.7.1, §3.7.5). A surviving mini-game reference in §4 ("storyteller, mystery, and letter-writing games") is removed, completing the v2.3 cleanup.

**Deduplication.** §5.2 and §5.3 trimmed to summaries pointing at the new canonical home `verbal-system.md` §8.4 (selection/reanalysis/loss and the semantic shift patterns); §5.3 retains only the lexicon-design notes specific to this document (false friends, untranslatables) and the *rhiiy-* worked example.

**Examples and flags.** GA-calque examples flagged `[Placeholder: …]` throughout (§3.4.3, §3.4.5, §3.7.2). New [Open] flags: example plural pairs (§3.2); REC/ITER and concord surface forms promoted into §7 as the highest-priority example gaps. §3.4.3's worked example upgraded to use the attested pronoun and frame forms.

**§8 document set updated.** Added `terminology-registry.md` and `skills/reference-grammar-section-drafting-and-integration.md`; `verbal-system.md` entry updated to its v2 section layout; superseded-documents entry simplified to point at the registry.

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

**Terminology shift: involitive → non-volitive.** The v2 document used *involitive* (sourced from Sinhala) as the marked term opposite *volitive*. The May 2026 verbal-system-description session worked with *modulated* as a positively-named alternative. v2.1 adopts *non-volitive* — privatively named for readability, with the principled-asymmetry argument preserved in prose framing rather than encoded in the term. See `verbal-system.md` §14 for the full terminology history.

**Polarity preserved with reconciliation flag.** v2 §3.4.2 had a four-cell VOL/INVOL × POS/NEG grid as the central organizing structure. In v2.1, polarity is preserved as a separate grammatical dimension (§3.4.4) but flagged as needing reconciliation with the cell × sub-modality structure described in `verbal-system.md`. The polarity discussion proper lives in `verbal-system.md` §10.

**Recognitional-habitual moved.** The full discussion of REC and HAB, including the DEF → REC grammaticalization and its open questions, has moved to `verbal-system.md` §7. A summary remains in language reference §3.4.5.

**Document set list updated (§8).** Added `verbal-system.md`, `verb-paradigm-verdict.md`, and `translation-frequency-task.md` to the sibling-document list. Marked `verb-terminology.md` as superseded; `verb-recipe.md` confirmed as sibling working note.

**Open questions list updated (§7).** Item 8 (mystery/witness commitments) expanded to reflect the new structure: sub-modality unification, AB billing, stative-strategy frequency, polarity reconciliation, concord affix inventory, LVC argument structure, nested negation glossing.

### v2, May 2026

Verb-terminology integration (volitive/involitive committed; LVC, concord affixes, REC/HAB committed); pitch-revision integration; phonology summary harmonized with `phonology.md` v2 and `orthography.md` v2. See full v2 changelog in earlier versions.

### v1 (original)

Original document. Established the design philosophy (§1), the phonology summary (§2), the morphology sketch (§3) with volition system and nested negation, the lexicon framing (§5), and the sample-forms anchor (§6).
