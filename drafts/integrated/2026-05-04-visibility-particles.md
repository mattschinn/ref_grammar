# Visibility-Marked Topic Particles — Draft

This draft contains revisions and additions for two files. Each section is labeled with its destination. Copy into the target files as appropriate.

---

# Part 1 — For `orthography.md`

## 1.1 Addition to §1 (Design Principles)

Add a clarifying bullet to the list of what the orthography encodes, placed alongside the existing "Vowel **length**" entry:

> A note on IPA convention for long vowels: where the length digraph supplies a *distinct vowel quality* in its second graph (as in `iie` /iɛ/, see §3.3), the IPA does not carry an additional length mark — the second-quality vowel is what makes the digraph bimoraic. Where the digraph's second graph reflects historical schwa or glide that has been absorbed into pure length (`Vu`, `iiy`), the IPA carries `ː`. The orthographic length pattern, not a uniform IPA convention, is what identifies a digraph as bimoraic.

## 1.2 Revision to §3.3 (Doubled vowels: hiatus, plus the special case of `ii`)

The current §3.3 establishes that `ii` plus another vowel marks hiatus (`iia` /i.a/, contrasted with diphthongal `ia` /ia/). A new pattern is now attested that requires a third row in the analysis: `ii` plus `e` marks neither hiatus nor a short diphthong, but a **bimoraic long diphthong** /iɛ/ — a length pattern parallel to `Vu` and `iiy`, in which the second graph (`e`) supplies a distinct vowel quality rather than smoothing into pure length.

Replace the existing contrast table with the expanded version:

| Grapheme | IPA | Type | Morae |
|---|---|---|---|
| `ia` | /ia/ | diphthong, monosyllabic | 1 |
| `iia` | /i.a/ | hiatus, disyllabic | 2 (separate syllables) |
| `iie` | /iɛ/ | long diphthong, monosyllabic | 2 (single nucleus) |
| `ea` | /e.a/ | hiatus, disyllabic | 2 (separate syllables) |

The `iie` pattern is the first attestation of a **diphthongal long vowel** — a single bimoraic nucleus whose two morae carry different vowel qualities. Diachronically it parallels the `Vu` digraphs: a base vowel (here /i/) absorbs a following schwa as length, except that fronting under the influence of the preceding /i/ raises the schwa to /ɛ/ rather than smoothing it into pure length. The orthography records the etymology in the second graph.

This forces a small generalization of the long-vowel system: long vowels in the conlang are **bimoraic nuclei**, of which there are now two surface types — *monophthongal long vowels* (`Vu`, `iiy`, with a length mark in IPA) and *diphthongal long vowels* (`iie`, where the second graph's vowel quality marks the second mora and no IPA length mark is used).

The contrast with the existing `ei` /ei/ diphthong (§3.4) is preserved and now classifiable: `ei` is a **monomoraic** diphthong (with /j/ as a consonantal glide), while `iie` is a **bimoraic** diphthong (with /ɛ/ as a vocalic second mora). The conlang has two diphthong classes distinguished by mora count.

By analogy, additional diphthongal long-vowel digraphs are predictable but currently unattested — `iio` /io/ would be the parallel form for an /i/-initial bimoraic nucleus with /o/-quality second mora. Whether such forms occur is **[Open]**, but the convention generalizes if they do.

## 1.3 Open-question note for §6 (Open Questions)

Add a new bullet to §6:

> **Genuine medial /h/ vs. breathy voice.** The `VhV` notation (§1, §4) currently encodes breathy voice across the board. The fossilized topic particles `noho` /noho/ and `hiho` /hiho/ (see `language_reference.md` §3.7) show genuine medial /h/ between vowels in fused-function-word contexts. Whether breathy voice and medial /h/ should be analyzed as allophones of one phoneme or as a phonemic contrast is undecided. If the latter, a working candidate orthographic disambiguation is `VhV` for the consonantal /h/ (where the second V is a full vowel) and `VhU` for breathy voice (with `u` acting as a length-marker in the manner of the `Vu` digraphs), but no commitment is made here. Currently the `VhV` reading in fused-function-word particles is contextually disambiguated.

## 1.4 Versioning note for §7

Add to §7's running list of v2 closures:

> **Diphthongal long vowels (§3.3).** The `iie` digraph is admitted as a bimoraic long diphthong /iɛ/, parallel to `Vu` and `iiy` as a length-encoding digraph but with a vocalic second mora rather than a smoothed-schwa or glide-source second graph. This generalizes the long-vowel system: long vowels are bimoraic nuclei of two surface types (monophthongal and diphthongal). Forced by the topic-particle paradigm in `language_reference.md` §3.7 (the article-bearing form of the visibility particle *hii* /hi/ "see" is *hiie* /hiɛ/). The IPA convention is clarified in §1: the colon is dropped for diphthongal long vowels because the second graph's vowel quality supplies the length-marking work.

---

# Part 2 — For `language_reference.md`

## 2.1 Revision to §3.2 (Nouns)

The existing paragraph on definiteness reads:

> A note on definiteness specifically: the GA definite article *the* has not survived as a definite article in the conlang. It has grammaticalized into the recognitional marker on deverbal nominals (see `verbal-system.md` §6). Definite reference, where needed, is conveyed through other means (demonstratives, possessives, context); the system here is **[Open]**.

Replace the closing sentence with:

> Definite reference, where needed, is conveyed through other means: a closed set of visibility-marked topic particles handles a substantial portion of the work (see §3.7), with possessives and context filling in elsewhere. A general definite-article system has not re-emerged and is not expected to.

## 2.2 New §3.7 — Demonstratives and topic particles

Insert as a new subsection of §3, after §3.6 (Adpositions and Spatial Language). The numbering of subsequent material in §3 (if any) shifts accordingly.

> ### 3.7 Demonstratives and topic particles
>
> The conlang has a closed set of two **visibility-marked topic particles**, grammaticalized from the imperatives of GA *see* and *know*. They mark a fronted topic constituent for a [±VIS] feature, where VIS encodes presence and perceptibility while NVIS covers absent, abstract, generic, and discourse-given referents.
>
> This is the second of the language's flagged grammatical innovations on the nominal/discourse side, alongside the recognitional-habitual nominal construction (§3.4.5). The two systems are orthogonal: REC/HAB is verbal-system morphology operating on deverbal nominals, while the visibility particles are pure information-structure marking on any topic constituent. They can co-occur on the same noun phrase without interaction.
>
> #### 3.7.1 Inventory and forms
>
> The particles are **fossilized**: not verbs, not imperatives, not inflecting. They show a single morphological alternation — a fossilized portmanteau pattern reflecting historical incorporation of the GA definite/indefinite article — but speakers do not synchronically decompose the long forms.
>
> | Function | Bare form | Article-incorporating form | Clausal form |
> |---|---|---|---|
> | **VIS** (present, perceptible) | *hii* /hi/ | *hiie* /hiɛ/ | *hiho* /hiho/ |
> | **NVIS** (absent, abstract, generic) | *no* /no/ | *nou* /noː/ | *noho* /noho/ |
>
> The bare form occurs before article-less nominals (proper nouns, pronouns, bare nouns where no article would have been present). The article-incorporating form occurs before what was historically an article-bearing nominal — the GA article *the/a* reduced to schwa in pre-conlang colloquial speech and cliticized onto the preceding particle, where it was absorbed as length (and, for *hii*, as a quality-shifted second mora). The article itself did not survive as an independent morpheme; this alternation is the only grammatical residue of its loss.
>
> The clausal form arose from fusion of the particle with GA *how* (introducing a clausal complement: *know how Christmas is coming up*, *see how the americano is steaming*). The fused form is treated as a single unit and is unrelated to the article-incorporation pattern.
>
> Etymological notes:
> - *no* /no/ from GA *know* /noʊ/ shows shortening below the regular /oʊ/ → /oː/ reflex, attributable to high-frequency function-word reduction. Parallel to the reduction of GA *the* itself.
> - *hii* /hi/ from GA *see* /siː/ shows regular /s/ → /h/ debuccalization (`phonology.md` §4.1) and the GA-/iː/-as-gliding-/i/ pattern (cf. orthography §3.3).
> - *hiie* /hiɛ/ shows /i/-fronting of the absorbed schwa to /ɛ/. The orthographic shape is the first attestation of a diphthongal long vowel; see orthography §3.3.
> - *noho* /noho/ and *hiho* /hiho/ preserve the /h/ of GA *how* in what is now a medial intervocalic position. The /h/ survives because at the time of fusion it was still a strong onset-/h/ of a stressed syllable. Whether the medial /h/ is phonemically distinct from breathy voice in the conlang is **[Open]**; see orthography §6.
>
> #### 3.7.2 Function
>
> The particles mark a fronted topic for visibility-deictic information.
>
> **VIS (*hii*, *hiie*)** — the topic referent is present and perceptible to the discourse participants, typically visually but extending to other modalities. Functions as a proximal demonstrative pointing-to-the-immediate, with topic-marking as its discourse role.
>
> **NVIS (*no*, *nou*)** — the topic referent is absent, abstract, generic, or discourse-given. Functions as a distal/abstract demonstrative or "as-for" topicalizer.
>
> The contrast can do real disambiguating work on the same noun phrase, distinguishing physical referent from abstract type:
>
> > *hiie nou·rítuiitsã*
> >
> > VIS-REC violin
> > *"see the violin"* — the physical instrument in the room, perceptible
>
> > *nou nou·rítuiitsã*
> >
> > NVIS-REC violin
> > *"know the violin"* — the violin-as-skill or violin-as-instrument-type, abstract
>
> (Surface forms of *violin* are placeholder; the actual conlang form awaits dictionary work. The example illustrates the particle contrast.)
>
> Worked examples from each form:
>
> > *hiie* αmericano today, it would be immaculate
> > VIS-REC americano today, ...
> > "(see) the americano today, it would be immaculate" — the americano is on the counter, visible.
>
> > *no* Alice, she is also learning the violin
> > NVIS Alice, ...
> > "(know) Alice, she is also learning the violin" — Alice as topic, not present.
>
> > *noho* Christmas is coming up, ...
> > NVIS-CLAUSAL Christmas is coming up, ...
> > "(know how) Christmas is coming up, ..." — clausal topic, abstract / discourse-introduced proposition.
>
> Pragmatic extensions of NVIS toward "discourse-given" / "as-we've-been-discussing" readings are expected to develop, parallel to the trajectory of Japanese *wa* and similar topic particles, but are not yet committed.
>
> #### 3.7.3 Syntax and scope
>
> - **Position:** strictly clause-initial. The particle precedes the topic constituent, which precedes the comment.
> - **Scope:** marks a single topic constituent — a noun phrase or a clause (the latter via the *noho/hiho* clausal forms).
> - **Stacking:** multiple topic-particle phrases in sequence are licensed, allowing chained topics with mixed visibility (*hiie* X, *no* Y, ...). Worked examples await further data.
> - **Negation, questioning, embedding:** the particles do not combine with negation, do not occur in questions, and do not embed under matrix predicates. They are root-clause information-structure marking.
> - **Topic discontinuity:** whether the topic constituent can be discontinuous (split between particle and comment by intervening material) is **[Open]**.
>
> #### 3.7.4 Interaction with other systems
>
> - **REC / HAB (§3.4.5):** orthogonal. A topic constituent can independently bear REC and/or HAB on a deverbal nominal head. The particles do not select for or block REC/HAB.
> - **Volition (§3.4.2):** orthogonal. Topic-particle marking is on the topic noun phrase or clause, not on the predicate; volition is on the predicate's LVC. They co-occur freely.
> - **Definiteness:** the visibility particles handle a substantial portion of what GA conveys with the definite article — referent-tracking and shared-reference signaling — but do so through a [±VIS] dimension rather than a [±DEFINITE] one. The conlang has no definite article and is not expected to develop one.
>
> #### 3.7.5 Diachronic note
>
> The grammaticalization path *imperative-of-perception-verb → demonstrative / topic particle* is well-attested cross-linguistically (Latin *ecce*, French *voici/voilà*, similar uses in Mandarin and elsewhere). The visibility distinction VIS / NVIS is also typologically standard for demonstrative systems with deictic-perceptual marking.
>
> The conlang's recruitment of GA *know* into the particle system, rather than into the verbal lexicon, has a side effect on the verb side: the canonical GA stative *know* is not expected to survive as a lexical verb. The lexical-stative gap left behind will be filled by other strategies — most likely the activity-coercion or stimulus-promotion routes from `verb-recipe-v2.md` §3, or possibly a *rhiiynii*-class bare stative entry. The decision is deferred.
>
> #### 3.7.6 Glossing
>
> Glossing abbreviations:
>
> - **VIS** — visibility-marked topic, perceptible / present.
> - **NVIS** — visibility-marked topic, non-perceptible / abstract / generic.
>
> The bare and article-incorporating forms are not separately glossed at the morpheme level — the alternation is fossilized. Where the article-incorporating form occurs, it may optionally be noted as `VIS+art` or `NVIS+art` in pedagogical contexts to flag the historical structure. The clausal forms (*noho*, *hiho*) may be glossed `NVIS-CLAUSAL` and `VIS-CLAUSAL` respectively.
>
> A separate `TOP` gloss is not used: these particles are inherently topic-marking, and stacking `TOP.VIS` would be redundant. If the conlang later develops a topic-marking construction without visibility, `TOP` may be added then.
>
> #### 3.7.7 Open questions
>
> - **Pragmatic NVIS extensions.** Discourse-given vs. discourse-new readings, expected to develop but not yet committed.
> - **Stacking patterns.** Worked examples needed to determine whether mixed-visibility chained topics are pragmatically natural and what the ordering constraints are.
> - **Topic discontinuity.** Whether material can intervene between the particle-marked topic and the comment.
> - **The verb-side gap.** What strategy fills the *know*-as-stative gap on the verb side. Tied to the broader stative-domain recruitment plan in `verb-recipe-v2.md` §3.
> - **Phonemic status of medial /h/.** See orthography §6. Bears on whether *noho* / *hiho* need disambiguating notation.
> - **Clausal-form productivity.** Whether *noho* and *hiho* are the only fused-with-*how* clausal particles, or whether further fusions (with *what*, *that*, etc.) might exist or develop.
