# Phonology Reference

**Version:** v2.4 (May 2026)
**Predecessor:** v2.2 (pitch-residue reframing); v2.1 (diphthongal long vowel /iɛ/, audience-fit reframings); v2 (top-down reorganization and dictionary-batch closures); v1 (original).

This v2.2 revision reframes pitch in §3.4 as the **phonetic residue of GA-style prominence** after stress migrated to the final vocalic position, rather than as an independently assigned prosodic dimension. The placement rule is unchanged; the analytical framing is sharpened, and a structural account of why minimal pairs are scarce is added. §1.1, §2.3, §4.4.5 (S3), and §5 are updated to align. Specific changes are listed in §7 (Versioning Notes).

Status tags used throughout:

- **[Settled]** — committed; downstream design depends on it.
- **[Provisional]** — current best analysis; expected to hold but open to revision.
- **[Open]** — explicitly undecided; flagged for future commitment.

GA reconstructions appear in italics with an asterisk (*sodium*). Surface forms appear in slashes (/...) for phonemes or in plain italics for the working orthography.

---

## 1. The phonology in outline

### 1.1 Character of the system

The conlang's phonology has a recognizable shape that organizes most of what follows. Five interlocking choices define it.

**Small consonant inventory, reorganized.** GA's consonant set has been substantially reduced through targeted mergers — /d, dʒ, n, j, g, v/ collapsed into a tap, /m, p/ into /b/ in onset, /f/ into /θ/, /s/ debuccalized to /h/. The surviving inventory is smaller than GA's, but distributed in unfamiliar ways: most of the segments occur in GA, but their distribution and patterning are foreign.

**Vowel-cluster-friendly.** Intervocalic consonant elision has produced widespread vowel hiatus, long vowels from smoothing, and diphthongs from reanalysis. Where GA has a single intervocalic consonant, the conlang often has a long vowel or an open hiatus. *sodium* /ˈsoʊdiəm/ → *hoiom* /ˈhoiom/ is canonical.

**Cluster-permissive in onsets, restricted in codas.** Long onset clusters survive (*ritsstw* "Rochester"); coda phonotactics is tighter, with most coda consonants reduced to /ʔ/ or eliminated outright. The asymmetry is a familiar one cross-linguistically; the closest natural-language parallel is Ancient Greek (cluster-permissive onsets, /n, r, s/-only codas), though the conlang's coda restrictions are even tighter.

**Post-stress consonantal appendix.** A subset of words have substantial syllabic-consonant material *after* the stressed vowel — *Jennifer* /ˈrɛ̃ːθw̩/, *countenance* /ˈhoʔn̩ʔn̩ts/, *Rochester* /ˈritsstw̩/. This material is weight-bearing (the syllabic consonants are moraic) but stress-invisible (primary stress stays on the leftmost full vowel). Earlier drafts called this *sesquisyllabic*; that label is misapplied (see §3.5) and the structurally accurate term is *appendix*.

**Pitch-stress dissociation.** Stress falls on the final vocalic position; pitch sits on the syllable that carried primary stress in the GA etymon. These are usually different syllables, producing the characteristic shape of *Emma* /ɛma/ — pitch on the first vowel, stress on the second. The two are best analyzed not as independently assigned features but as a redistribution of GA prominence across the word: loudness and length transfer to the final vowel under the conlang's final-stress rule, while F0 stays behind on the etymological-stress syllable as residue. See §3.4.

The unifying thread is that suprasegmentals do as much expressive work as segments. Pitch, length, nasalization, and breathy voice are all phonemically active; the orthography reflects this with a load of diacritics that are not decorative. A reader treating the diacritics as ornamental will collapse pairs the language treats as fully distinct.

### 1.2 How this differs from GA

The conlang's prosodic and segmental shape inverts GA almost completely.

GA is stress-timed, with aggressive vowel reduction in unstressed positions, initial-leaning stress, default trochaic feet (DUM-bah), and stress as the primary locus of prominence. The conlang is closer to syllable-timed, with the GA reductions *frozen into the surface lexicon* rather than performed live. Stress is final, the default foot is iambic (bah-DUM), and pitch carries a melodic dimension that GA does not have. A GA listener hears the conlang's segmental material as recognizable but the rhythmic shape as foreign — which is exactly the design intent.

Three further inversions worth flagging up front:

- **Schwa is not a reduction vowel.** GA's pervasive schwa has either been absorbed into long vowels (smoothing), elided (creating consonant clusters and syllabic consonants), or strengthened to /a/ or /ɛ/ depending on position. Where GA distributes schwa across most unstressed syllables, the conlang has none.
- **The rhotic system is reorganized.** GA's single rhotic /ɹ/ has split into a tapped /ɾ/ and a retroflex /ɻ/, with /ɻ/ becoming /ɾ/ near another /ɾ/ (alveolar wins). Where GA uses /ɹ/ for /d, dʒ, n, j, g, v/-mergers, the conlang uses the tap.
- **Coda /ʔ/ is stable.** GA's variable /t/-glottalization has phonologized: /ʔ/ is the regular reflex of GA coda /t/, and it does not elide further (with one lexical exception, see §4.4).

### 1.3 Typological position and stability

> *Background section.* This subsection situates the conlang within natural-language typology and is intended for readers interested in the analytical justification or the design context. It is *not* required for using or learning the language; readers focused on inventory and rules can skip to §2.

The system is naturalistic but unusual. Each component sits in attested typological territory; the assembly is not exactly matched by any single natural language.

The closest precedents:

- **Tashlhiyt Berber** for the segment inventory in syllabic-consonant position. Tashlhiyt licenses almost any segment, including voiceless obstruents, as a syllabic nucleus (*tkkst stt*, *tftktstt*). The conlang's appendix nuclei /s, θ, ʔ/ sit in the same low-sonority range that has driven Tashlhiyt's analytical literature.
- **Nuxalk (Bella Coola)** for the upper bound on appendix length. Nuxalk's all-consonant words (*xłpʼχʷłtʰłpʰłːskʷʰt͡sʼ*) demonstrate that low-sonority syllabicity is attested at substantial length. The conlang's *countenance* /ˈhoʔn̩ʔn̩ts/ — four post-stress nuclei depending on parse — sits within this range.
- **English and Slavic languages** for the structural mechanism. English *rhythm* /ˈɹɪð.m̩/, *button* /ˈbʌʔ.n̩/, *little* /ˈlɪɾ.l̩/, plus Czech and Polish post-stress syllabic liquids, are the direct structural parallel: weight-bearing post-stress syllabic-sonorant material that does not compete for stress. The standard analysis is *appendix adjunction* (Selkirk, Itô-Mester), the same mechanism this document adopts in §3.5.
- **Ancient Greek** for the segmental-prosodic combination. Greek's /s/-debuccalization (*hex* < *seks*), pitch accent on a vowel-quantity-contrasting system, and cluster-permissive-onsets-with-strict-codas asymmetry are the closest segmental-and-prosodic parallel to the conlang's overall shape.

Other resonances that surface in the design but aren't structural matches: Hawaiian and Japanese for vowel-cluster tolerance; Latin → Modern Parisian French as a diachronic-feel model (dramatic reduction producing a barely-recognizable daughter); Vietnamese for the orthographic philosophy of load-bearing diacritics; Swedish for the prosodic-overlay sensibility (geminates and pitch coexisting on a stress system); Arapaho and Minnesota Ojibwe for the small-inventory + length + pitch combination.

The combination most distinctive to the conlang — Polynesian-style vowel hiatus and small consonant inventory **with** Salishan-style syllabic obstruents and clusters **with** Swedish-style pitch overlay **with** Vietnamese-style diacritic load — is hard to find a direct natural-language match for. Each piece has clear precedent; the assembly is unusual.

**On stability.** Languages with rich post-stress syllabic-consonant tails tend to evolve in one of two directions: further reduction (the appendix nuclei elide or merge into the preceding coda) or secondary-stress development (some appendix nucleus acquires its own foot). Old English's *-ende* participles reduced to modern *-ing*; Latin post-stress material became Spanish secondary stress. The conlang's current state is best read as a **synchronic snapshot of a language mid-restabilization** — captured at a moment after aggressive schwa elision has produced the appendix material, but before the typologically-expected next step has occurred. This framing aligns with the conlang's stated diachronic origin story (regular sound changes from GA producing the surface forms) and gives the document a coherent answer to "is this naturalistic?"

For a conlang fixed at a synchronic stage, this is not a problem. The diachronic story produces exactly the right origin for a system at this stage: regular sound changes from a recognizable source language, stopped before they have run further to completion.

---

## 2. Inventories

### 2.1 Consonants

**Stops:** /b, t, ʔ/. **[Settled]**

Note on /k/: surface [k] occurs only in /kj, kw/ clusters. The current working analysis is that **/k/ is not a phoneme**: surface [kj, kw] are allophonic realizations of underlying /hj, hw/, with [k] arising as fortition of /h/ before a glide. **[Provisional, under analysis]**

Coda /ʔ/ is the most stable coda segment in the language and serves as a reliable anchor in derivations. It does not elide under the regular rules; one lexical exception applies (see §4.4). **[Settled]**

**Fricatives:** /θ, h, ts, s/. **[Settled]**

- /h/ derives from GA /s/ via debuccalization in most positions, and from GA onset /k/ in parallel.
- /ts/ derives from the historical /st/ cluster.
- /s/ as a phoneme survives in contexts where the historical /st/ produced it (taking the synchronic place of /s/ in clusters), and in geminate /sː/ position (see below).

**Geminates:** /sː, nː, pː/ are attested as a sub-inventory.

Geminates arise from two diachronic feeds:

1. **Phonologization of GA ambisyllabic consonants** in stressed-second-syllable environments. *beussou* /ˌbɛːˈsːoː/ "to fall asleep" (< *pass out*) and *epplii* /ˈɛpːli/ "to apply" both phonologize the slight gemination GA already has at these boundaries.
2. **Cluster collapse.** *rhiiysseunnou* /ɻiːsːɛːnːoː/ "to be different" shows /nd/ in coda → /nː/ by regressive assimilation (/d/ → /n/, then geminate). The same form's /sː/ comes from GA /st/ at a stressed-syllable boundary.

The /s/ → /sː/ rule at syllable boundary preceding stress is in tension with the more general /s/ → /h/ debuccalization rule; the gemination wins in this specific environment. See §4.4 for the rule.

**Nasals:** /n, m/. **[Settled]**

**Liquids/Tap:** /r/ (tapped), /l/ (clusters only), /ɻ/ (assimilates to /r/ near another /r/). **[Settled]**

**Glides as syllabic consonants:** /w, j/ — occur as unstressed allophones of /o, i/ in syllabic-consonant position. **[Settled, per current note]**

**Syllabic consonants generally:** /n, m, s, θ, ʔ, w, j/ — and possibly /r/. These segments occur as syllabic nuclei in **appendix position** (post-stress, foot-external; see §3.5). They are moraic but stress-invisible. **[Provisional]**

**Voiceless sonorants:** /n̥, m̥, ɾ̥/ exist as distinct surface forms, arising from elided coda obstruents and from the M1 mechanism (see §4.4). The orthography marks devoicing with an acute accent on the consonant.

**Aspiration** is treated as fully allophonic (English-style: voiceless stops aspirate in stressed onsets) and is not represented orthographically. **[Settled]**

**Notable gaps relative to GA.** Sounds present in GA but absent here: /k, dʒ, tʃ, ʒ, g, ŋ, v, f, d, p, ʊ, ʌ, u/. Most have specific merger paths (see §4.4). /k/'s "absence" is the analytical move — surface [k] in /kj, kw/ is reanalyzed as allophonic /h/ + glide. **[Settled, with /k/ analysis Provisional]**

### 2.2 Vowels

**Short:** /i, ɪ, ɛ, o, ɑ/ **[Settled]**

The /i/ vs. /ɪ/ contrast deserves a note: /i/ is the short tense vowel inherited from GA "long-e" /ɪi/, with its gliding quality preserved synchronically. It is a single nucleus, not a sequence. The orthography spells this `ii` (see *Orthography Reference* §3.2 for the contrast with hiatus `iyi` and with long /iː/ `iiy`).

**Long:** Bimoraic nuclei in two surface types. **[Settled]**

- *Monophthongal long vowels.* /iː, ɛː, oː, aː, ɨː/. Both morae carry the same vowel quality; the IPA carries `ː`. These arise from intervocalic-consonant elision plus smoothing, and from reanalysis of historical diphthongs. **/iː/ is a phoneme** of the conlang, arising principally from /ɪji/-smoothing (the /ɫ/-glide-becoming pathway, e.g., *Emily* /ˈɛməli/ → /ɛˈmiː/, *rhiiynii* /ɻiːni/ "to need" < *really need*). It is spelled `iiy` orthographically.
- *Diphthongal long vowels.* /iɛ/ is the first attested case: a bimoraic nucleus whose two morae carry different vowel qualities (here /i/ and /ɛ/). The IPA does *not* carry `ː` — the second-quality vowel is what makes the digraph bimoraic. /iɛ/ arises from /i/-fronting of an absorbed schwa: a base vowel /i/ absorbs a following schwa as length, with the schwa raising to /ɛ/ under the influence of the preceding /i/ rather than smoothing into pure length. Attested in *hiie* /hiɛ/ "(see), VIS-REC" (cf. `language_reference.md` §3.7). Spelled `iie` orthographically. Additional diphthongal long-vowel digraphs (e.g., /io/ as `iio`) are predictable by analogy but currently unattested. **[Open: whether other /i/-initial diphthongal long vowels occur]**

**Diphthongs (monomoraic):** /ei, oe, ia/ **[Settled]**

The conlang has two diphthong classes, distinguished by mora count: monomoraic diphthongs above (with /j/ or vocalic glide as the consonantal second element) and bimoraic *diphthongal long vowels* under "Long" (with a vocalic second mora). The contrast `ei` /ei/ (monomoraic) vs. `iie` /iɛ/ (bimoraic) is the cleanest minimal pair for the distinction. See `orthography.md` §3.3–3.4.

**Suprasegmental contrasts on vowels:** see §2.3.

### 2.3 Suprasegmental contrasts on vowels

Vowels contrast in nasalization, breathy voice, and pitch in some environments. All three arose from elided coda consonants (nasals, /h/, weak obstruents) leaving residual features on adjacent vowels.

- **Nasalization** is phonemic. **[Settled]**
- **Breathy voice** is not phonemic — the `VhV` surface pattern is an allophonic realization, not a contrast in the inventory. **[Settled]** Medial /h/ in fused-function-word contexts (*noho*, *hiho*) has the same allophonic status; the proposed phonemic distinction (`VhV` consonantal vs. `VhU` breathy) is not adopted.
- **Pitch accent** is dissociated from stress in placement (see §3.4). Placement is settled: pitch sits on the syllable that carried primary stress in the GA etymon. The placement is **etymologically determined** (fully derivable from the etymon) but **not synchronically derivable** (a speaker without etymological access has to know it word by word, the same epistemic status English lexical stress has). Contrastiveness — whether minimal pairs distinguishable only by pitch placement actually exist — is **[Open]** pending audio-recorded verification.

---

## 3. Syllable and metrical structure

### 3.1 Syllable structure and phonotactics

The language permits both substantial vowel clusters (*hoiom* /ˈhoiom/ "salt" < *sodium*) and substantial consonant clusters (*hoʔnʔnts* /ˈhoʔn̩ʔn̩ts/ "face" < *countenance*; *ritsstw* /ˈritsstw̩/ "Rochester"). The two distributions arise from different processes: vowel clusters from intervocalic consonant elision (§4.4 E1), consonant clusters from systematic schwa elision (§4.4 E3).

**Onset phonotactics is permissive.** Long onset clusters survive, including sequences violating sonority sequencing in moderate ways. The /st/ → /ts/ shift produced /ts/-onsets that are phonotactically normal in the conlang but unusual cross-linguistically.

**Coda phonotactics is restrictive.** Most coda consonants have either elided outright (the /l, d/-paths in §4.4), reduced to /ʔ/ (the /t/-path), or assimilated and geminated (the /nd/ → /nː/ path). The surviving codas are sparse.

**Syllabic consonants** (/n, m, s, θ, ʔ, w, j/, possibly /r/) serve as syllable nuclei. They occur predominantly in appendix position (§3.5) but can also occur foot-internally where elision has stranded them.

A **mora (μ)** is the unit of syllable weight: a short vowel is 1μ, a long vowel is 2μ, a syllabic consonant is 1μ. A syllable is **light** (1μ) or **heavy** (2μ) depending on its moraic content. The conlang's stress and foot rules are weight-sensitive.

### 3.2 Foot construction

Feet are built **right-to-left** and are **trochaic** by default (left-headed): the leftmost syllable of a two-syllable foot bears prominence within the foot. The **rightmost foot** is the head foot of the prosodic word and bears primary stress.

Feet may be one or two syllables. **Degenerate (single-syllable) feet are licensed** at the right edge regardless of syllable weight. Light-monosyllabic words like *ŕe* /ˈr̥ɛ/ "today" are fully grammatical; an earlier draft's minimality clause restricting degenerate feet to heavy syllables is retired.

### 3.3 Stress placement

The descriptive rule: **stress falls on the final vocalic position of a word.** Because syllabic consonants count as nuclei, "final vocalic position" may be a syllabic consonant rather than a full vowel.

Three things follow from the right-headed foot construction in §3.2:

1. In a monosyllabic head foot, the head is that single syllable — which is the final vocalic position. Stress lands there.
2. In a disyllabic head foot, the head is the leftmost syllable of the foot by default (trochee) — but the rightmost syllable bears stress, by the right-headed prosodic-word rule. The two interact such that stress effectively lands on the rightmost full vowel.
3. **Quantitative metathesis** — what earlier drafts called the "rightward stress shift" in dactyl-shaped words — is not a separate rule. It falls out as a consequence of right-headed foot construction applied to a foot where no rule has reduced the rightmost syllable.

If an unstressed vowel followed the final vowel historically, one of three things happened: it smoothed into the stressed vowel (lengthening), elided (creating clusters), or received the stress instead (becoming the new final vocalic position).

### 3.4 Pitch placement

**Pitch falls on the syllable that carried primary stress in the GA etymon.** The placement claim is the basic descriptive fact and has been settled since the May 3 2026 session.

The analytical framing this v2.2 commits to: pitch is best understood as the **phonetic residue of GA-style prominence** after stress has migrated to the final vocalic position, rather than as an independently assigned prosodic dimension. Speakers do not target pitch as a separate articulatory dimension; they retain GA-style prominence on its inherited syllable (where prominence in English already bundles loudness, length, and F0) and superimpose the conlang's final-stress rule on top. Loudness and length transfer to the final vowel; F0 stays behind on the etymological-stress syllable. The audible "pitch on V₁, stress on V_final" pattern falls out of this redistribution, rather than being assigned by a separate rule.

Pitch and stress are usually on **different** syllables. Where GA stress was initial (most multisyllabic GA etyma), the conlang's stress has migrated to the final position while pitch has stayed where it was. *Emma* /ɛma/ has pitch on /ɛ/, stress on /a/. *Emily* /ɛmiː/ has pitch on /ɛ/, stress on /iː/.

When pitch and stress would land on the same syllable, the result is a single-prominence word. Monosyllables coincide trivially. Some longer forms also coincide where the GA etymon's stress was final or where derivational reductions have placed both prominences on the same vowel — *ŕeut* /r̥eːʔ/ "carrot" coincides because the GA *carrot*'s stress was on the first syllable, which is now the only syllable left.

#### Diachronic pathway

```
Stage 0 (GA):           σ₁ {loud + long + high F0}    σ₂ ...    σₙ {weak}
                        full English prominence on the lexically-stressed syllable

Stage 1 (transitional): σ₁ {long + high F0}            σ₂ ...    σₙ {emerging final prominence}
                        final-stress constraint begins applying; loudness migrates

Stage 2 (current):      σ₁ {high F0, slight length}    σ₂ ...    σₙ {loud + long, primary stress}
                        stress is now on σₙ; F0 residue on σ₁
```

The end state has two prominences competing on one word: an inherited one phonetically reduced to mostly F0, and a new one carrying loudness and length. This is the dissociation pattern.

The pathway has cross-linguistic parallels. The standard analysis of how Tokyo Japanese pitch accent emerged from earlier accent-with-stress is roughly this — stress simplifies to its F0 correlate while a separate prominence dimension takes over. The development of tone from accent in some Bantu lineages has a similar shape. The conlang is in well-attested typological territory.

#### Etymologically determined, synchronically opaque

The placement is **etymologically determined** — fully derivable from the GA etymon's stress location. From the historical-linguist's viewpoint, it is a regular reflex.

It is **not synchronically predictable** — from the speaker's viewpoint, with the GA source no longer accessible, pitch placement is lexical information attached to each word. A speaker cannot derive it from the conlang surface form. This is the same epistemic status English lexical stress has: a speaker has to know that *récord* and *recórd* differ word by word.

The two senses of "predictable" are different and were conflated in earlier framings. Calling pitch "predictable" in the sense that closes the question of whether it is lexical is sloppy; "predictable from the etymon" does not entail "predictable from the surface form." Pitch is **lexical**, in the same sense that lexical-stress systems are lexical. Whether it is also **contrastive** (carries minimal-pair distinctions) is a separate question, treated below and in §5.

#### Why minimal pairs are scarce

The minimal-pair scarcity is **not** evidence that pitch is weak. It is evidence that GA stress is loud — in the information-theoretic sense — and has already eaten most of the territory in which pitch could carry contrast.

GA stress is not just a prominence diacritic. It restructures everything around itself: stressed vowels are full, unstressed vowels reduce to schwa or elide, syllable weight and segment count depend on where prominence fell. By the time GA stress has done its work, two words sharing the same stress pattern have largely the same shape, and two words with different stress patterns have largely different shapes.

The conlang's cascade compounds this. Vowel mergers, consonant mergers, schwa elision, the appendix system — all operate on already-stress-conditioned material. The result is that residual segmental skeletons that could converge on a homophonous form while differing only in pitch almost never exist.

The territory left for pitch to carry contrast is mostly **GA stress-shift derivational pairs** — pairs like *récord* / *recórd*, *présent* / *presént*, *súbject* / *subjéct*, where both members share segments under different prominences. These are the cleanest candidates for true conlang minimal pairs distinguishable by pitch alone, because they are the cases where GA's segment-shaping power is held constant across the pair.

The reframed picture: pitch's potential workspace was mostly absorbed by the segmental consequences of the prominence pattern it descends from. Low functional load on pitch follows directly from this and is not, on its own, evidence about whether pitch is contrastive, allophonic, or vestigial.

#### Phonetic predictions

Under the residue analysis, V₁ should retain phonetic correlates of GA-style prominence beyond pure F0:

- **Slight length.** V₁ should be marginally longer than a comparable unstressed vowel, because length was part of the inherited prominence package and would not fully transfer to the final.
- **Slight fullness or amplitude.** V₁ should not reduce all the way to schwa-like quality even when stress has clearly moved off it.
- **F0 peak roughly aligned with the syllable nucleus**, not displaced to a syllable margin (which would suggest a contour-tone analysis).

A "true" pitch-accent system fully grammaticalized away from its stress origin would have F0 doing the work alone, with V₁ otherwise indistinguishable from any other unstressed vowel. The conlang should *not* look like that under the residue analysis. Acoustic recordings (pending; see §5) are the falsification test.

#### Orthography

Pitch is marked with **acute** on a vowel; stress is marked with **grave** (normally unwritten because predictable, marked in formal/pedagogical text); coincidence is marked with **circumflex** in formal register. The acute-on-consonant devoicing convention is unaffected — pitch and devoicing live on different segment types.

The orthographic conventions are not affected by the residue reframing. Pitch is still marked because it is still lexical, regardless of whether it is analyzed as a feature target or as residue.

#### Pedagogical note

For GA-speaking learners, the framing matters in practice. "Pitch accent" as a label triggers a mental block: learners begin consciously controlling F0 in unnatural ways and overshoot. The technique implicit in the residue analysis avoids this — say the word with English-style prominence on the etymological-stress syllable, then put extra weight on the final vowel. The pitch pattern emerges automatically without being thought of as pitch.

This is a teaching artifact, not a phonological claim, but it matches the analysis: if pitch is residue rather than target, the right way to teach it is as residue too.

### 3.5 Appendix structure

Some conlang words have substantial syllabic-consonant material following the stressed vowel:

| Form | Stressed nucleus | Post-stress material |
|---|---|---|
| *Jennifer* /ˈrɛ̃ːθw̩/ | /ɛ̃ː/ | /θ/ + syllabic /w̩/ |
| *Rochester* /ˈritsstw̩/ | /i/ | /tsst/ + syllabic /w̩/ |
| *countenance* /ˈhoʔn̩ʔn̩ts/ | /o/ | /ʔ/ + /n̩/ + /ʔ/ + /n̩/ + /ts/ |

This material is **weight-bearing** (the syllabic consonants are moraic) but **stress-invisible** (primary stress stays on the leftmost full vowel even when there are multiple post-stress nuclei). It can be **substantial** — *countenance* has up to four post-stress nuclei depending on whether /ts/ is parsed as a complex coda or a fourth nucleus.

The right structural analysis is **appendix adjunction**: the post-stress material is adjoined to the prosodic word at a level above the foot, rather than being foot-internal-but-invisible.

```
        ω (prosodic word)
       / \
      F   App (appendix)
      |    \
      σ    σ σ ... (syllabic-C nuclei)
     /|
    μμ
```

The foot F contains the stressed syllable. Everything to the right of F is appendix material adjoined to ω, foot-external by virtue of attaching at a higher level.

This analysis is standard for English word-final consonant clusters that violate sonority sequencing (*sixths* /sɪksθs/), German word-final extrametrical consonants, Japanese moraic nasal codas, and Polish/Czech post-stress syllabic sonorants. The mechanism handles the conlang's pattern cleanly:

- It naturally permits multiple nuclei in the appendix zone (no single-constituent restriction).
- It correctly predicts stress-invisibility (the appendix is outside the foot domain).
- It correctly predicts weight-bearing (the appendix nuclei are moraic syllables, just attached higher).

**On terminology.** Earlier drafts called this material *sesquisyllabic*. The label was misapplied. Sesquisyllabicity is a defined left-edge phenomenon in Mainland Southeast Asian (Mon-Khmer, adjacent Tibeto-Burman) languages: a reduced presyllable precedes a major stressed syllable, and the prosodic word is iambic in shape. The conlang's pattern inverts every defining property — the reduced material *follows* the stressed nucleus, the shape is trochaic-with-tail, the reduced nuclei can be lower-sonority than MSEA presyllables typically host, and the appendix can be longer than half a syllable. The borrowed term locates the asymmetry on the wrong side and imports typological expectations that don't apply. *Appendix* is the correct term; *sesquisyllabic* should not be used in new descriptions.

**Extrametricality** — a related concept that licenses single peripheral constituents to be invisible to foot construction — does some work for the simpler cases (*Jennifer* with one peripheral syllable) but doesn't scale to the multi-nucleus cases. The classical formulation permits one peripheral constituent to be invisible; *countenance*'s up-to-four post-stress nuclei break that. Iterative or persistent extrametricality has precedent (Cairene Arabic, some Berber varieties) but is non-standard. Appendix adjunction is the cleaner analysis.

> *Analytical sources.* The appendix-adjunction mechanism originates in the prosodic-phonology literature (Selkirk 1986, 1996; Itô & Mester 1992 and later). Cited here for completeness; not required reading for using the language.

---

## 4. Diachronic development

### 4.1 Overview

The conlang's surface forms derive from GA etyma by a designed cascade of regular sound changes. The high-level shape:

- **Aggressive schwa elision** in unstressed positions, producing consonant clusters and syllabic consonants where GA had vowel-bearing syllables.
- **Intervocalic consonant elision** for /d, dʒ, n, j, g, v/, producing widespread vowel hiatus and feeding the long-vowel inventory.
- **Debuccalization** of /s/ to /h/ in most positions, and of onset /k/ to /h/ in parallel.
- **Massive consonant mergers**, especially /d, dʒ, n, j, g, v/ → /r/ (tap), /m, p/ → /b/ in onset, /f/ → /θ/, /w, j/ → /ɻ/.
- **Coda reduction**: /t/ → /ʔ/, /d/ → ∅, /l/ along several paths (still under analysis), with coda /ʔ/ stable.
- **Vocalic mergers**: /u, ʊ, ʌ/ → /ɨ/, /ai/ → /iː/ ~ /eː/ ~ /i/ (conditioning open), /au, or/ → /o(ː)/, /æ, er/ → /eː/.
- **Suprasegmental residue**: nasalization on vowels adjacent to elided /n/, breathy voice from elided /h/ and weak obstruents, pitch retained on the GA-stress vowel even after stress migrates rightward.
- **Final-vowel stress assignment**, with the historical stress vowel keeping its pitch — producing the pitch-stress dissociation.

The cascade is best understood as a feeding pipeline rather than a flat list of rules. The ordering encodes a design preference for vocalic events over consonantal ones: vowel clusters and long vowels are typologically rarer than consonant clusters, and the conlang aims to foreground them.

### 4.2 The cascade in overview

Four processes apply in feeding order:

1. **Consonant elision** (intervocalic and coda). Creates vowel hiatus and feeds vowel resolution. M1 (rhotic metathesis) also fires here as an alternative way to vacate the intervocalic position.
2. **Vowel resolution.** Smoothing of hiatus into long vowels (when conditions are met), or retention of hiatus.
3. **Vowel elision.** Applies to inputs that survived process 1 unchanged. Creates consonant clusters, often with syllabic-consonant promotion.
4. **Stress and pitch placement.** Stress is assigned to the now-final vocalic position. Pitch lands on the syllable that historically carried GA primary stress.

The crucial ordering claim is that **process 1 bleeds process 3**: once an intervocalic consonant has elided, the vowels it separated are no longer in an environment for vowel-elision. A word is either a "vowel-event" word (long vowel or hiatus) or a "consonant-event" word (cluster, syllabic consonant), but not both at the same locus. **[Settled]**

### 4.3 The cascade in detail

Notation: for a CVCVC input, **C₀ V₁ C₁ V₂ C₂**. For a dactyl-shaped CVCVCVC input, **C₀ V₁ C₁ V₂ C₂ V₃ C₃**. Cs may be clusters; Vs include diphthongs.

#### Cascade for CVCVC

| Step | Rule | Condition | Output |
|---|---|---|---|
| 1a | E1: elide C₁ | C₁ ∈ {ɾ, dʒ, n, j, g, v} | C₀ V₁ V₂ C₂ → step 2 |
| 1b | M1: relocate C₁ if /ɻ/ | C₁ = /ɻ/ AND C₀ ∈ {/h/, ∅} | rhotic moves to onset; /h/ becomes devoicing feature → /r̥/. Hiatus created. → step 2 |
| 1c | M1 blocked / no rule fires | C₁ = /ɻ/ but C₀ is something else; OR C₁ not in any set | unchanged → step 4 |
| 2 | Smoothing | (a) one participant is /ə/, OR (b) participants are articulatorily close | C₀ V₁ː C₂ |
| 2 | Hiatus retention | neither smoothing condition met | hiatus preserved; stress placed on final V (see §3.3) |
| 3 | Stranded schwa | V₂ = /ə/ in resulting open syllable | strengthen ə→a |
| 4 | E3: elide V₂ | V₂ ∈ elision set, intervocalic position not vacated | C₀ V₁ C₁ C₂ → step 5 |
| 4 | E3: skip | otherwise | → step 6 |
| 5 | Syllabic-C promotion | C₁ or C₂ ∈ syllabic-eligible | C₀ V₁ C₁ C̩₂ (foot + appendix) |
| 6 | E2 family: coda treatment | C₂ subject to coda rules (E2a–E2d) | varies — see §4.4 |
| 7 | Final-V resolution | V₂ ∈ {e, a, ə} | strengthen ə→a |
| 7 | Final-V resolution | V₂ ∈ {i, o} | reduce to syllabic /j, w/ |
| 8 | R-Assim | word contains both /ɻ/ and /ɾ/ | /ɻ/ → /ɾ/ throughout |

**Note on step 2.** Smoothing is licensed by **either** of two conditions: (a) at least one of the vowels in hiatus is /ə/ (which is absorbed into its neighbor), or (b) the two vowels are articulatorily close. When neither is met — i.e., two or more full, articulatorily distant vowels are in hiatus — the hiatus is retained and stress falls on the final vowel. This is why /eio/ in *radio* stays as three syllables. **[Settled]**

#### Cascade for dactyl (CVCVCVC)

Dactyl-shaped words enter the same cascade and resolve to CVCVC or shorter shapes via E1, E3, or coda reduction. Where elision fully fails, the word retains its three-vowel shape and stress falls on V₃ — by right-headed foot construction, not by a separate metathesis rule (this was previously labeled D1; it is now understood as a consequence of §3.2's foot construction, not an independent rule).

#### Five generalizations the cascade encodes

1. **Vacate the intervocalic position** where licensed — by elision (E1) or by metathesis (M1). Either creates hiatus.
2. **Smooth** vowels in hiatus when (a) one is schwa, or (b) they are articulatorily close.
3. **Promote** stranded consonants to syllabic nuclei where sonority licenses; this produces appendix material when the result is post-stress.
4. **Strengthen** final stranded schwa.
5. **Place stress** on the rightmost full vocalic position; **place pitch** on the syllable that carried GA primary stress.

#### Bleeding and feeding relations

- **E1 always bleeds E3 at the same locus.** If C₁ has elided, V₂ is no longer in the right environment for vowel elision.
- **M1 conditionally bleeds E3.** When M1 fires, the intervocalic position is vacated and E3 is bled. When M1 is blocked, E3 is free to fire.
- **E1 and M1 (when firing) both feed Smoothing.**
- **Smoothing bleeds Strengthening.** A schwa that has smoothed into the preceding vowel is no longer available to be strengthened to /a/.
- **E3 feeds Syllabic-C promotion**, which feeds Appendix adjunction at the prosodic-word level.
- **All vowel-creating and vowel-removing rules feed Stress placement.**
- **Pitch placement is independent of the segmental cascade** — it lands on the historical-GA-stress vowel regardless of what the segmental rules have done elsewhere.
- **R-Assim fires last.**

### 4.4 Sound-change inventory

Diachronic changes that produce the synchronic inventory. Listed by domain. These are descriptive of the historical processes; some are productive synchronic rules, others are residue.

#### 4.4.1 Consonantal mergers and shifts

| GA source | Conlang reflex | Notes |
|---|---|---|
| /s/ | /h/ in most positions | Debuccalization. |
| /s/ | /sː/ at syllable boundary preceding stress | Phonologization of GA ambisyllabic /s/. Wins over debuccalization in this environment. **[New in v2; see *beussou*, *rhiiysseunnou*]** |
| /s/ (onset cluster) | /s/ | Debuccalization blocked when /s/ is the first element of an onset cluster (e.g., /sp/, /sk/). Cluster-protection: /s/ surfaces. **[New in v2.4; see *spyi*]** |
| /st/ | /ts/ | Takes the synchronic place of /s/ in clusters. |
| /k/ (onset) | /h/ | Joins /s/ in the debuccalization path. |
| /k/ (coda) | ∅ | Lost outright. |
| coda /k/ + adjacent /w/ | /kʷ/ (onset) | /k/ absorbs the labial feature of adjacent /w/; blocks coda /k/→∅; surfaces as onset /kʷ/. Ambisyllabic /kw/ → geminate /kʷː/. **[New in v2.4; see *piiquóæ*, *piquô*, *récquıìs*]** |
| /kr/ | /r̥/ | /k/ devoices the rhotic and merges in. |
| /kl/ | /tl/ | Stop place shifts; cluster preserved. |
| /kj, kw/ | [kj, kw] | Surface intact; analyzed as allophonic /hj, hw/. **[Provisional]** |
| /d, dʒ, n, j, g, v/ | /r/ (tap) | Massive merger into the tap. /n/-merger conditional on environment (can also elide with nasal coloring). |
| /m, p/ | /b/ (in onset) | Merger into voiced labial. |
| /p/ | /b/ before /ɛ/ and its long counterpart | More specifically: /p/ → /b/ in onset before /ɛ, ɛː/; blocked before /i, ɪ, ɑ, o/ and consonant clusters. **[New in v2; environment from *beussou*]** |
| /pp/ ambisyllabic | /pː/ | Phonologization of GA ambisyllabic /p/. **[New in v2; see *epplii*]** |
| /f/ | /θ/ | Merger into the dental fricative. |
| /w, j/ | /ɻ/ | Then /ɻ/ → /r/ near another /r/. |
| /nd/ in coda | /nː/ | Regressive assimilation: /d/ → /n/, then geminate. **[New in v2; see *rhiiysseunnou*]** |
| /ɫ/ between high front vowels | /j/ | Glide-becoming, feeds smoothing of /ɪji/ → /iː/. Attested in *Emily*, *rhiiynii*, *rhiiysseunnou*. |

#### 4.4.2 Vocalic mergers and reanalyses

| GA source | Conlang reflex |
|---|---|
| /u, ʊ, ʌ/ | /ɨ/ (possibly further to /ɪ/) |
| /ai/ | /eː/ ~ /i/ (conditioning **[Open]**; /iː/ outcome ruled out May 2026) |
| /au, or/ | /o(ː)/ |
| /æ, er/ | /eː/ |
| /æ/ before nasal | /ɛː/ (long, via GA-tense-/æ/-with-preserved-duration pathway) |
| /u/ (long pathway) | /ɨː/ |
| /ə/ (final) | /a/ when stranded in open syllable; absorbed when adjacent to vowel; elides when in cluster-feeding position |
| /ə/ (initial unstressed, surviving) | /ɛ/ when not absorbed or elided. **[New in v2; see *epplii*]** |
| /ɔɪ/ | /oe/ | Attested in *bœ*, *boeś*, *nœ*. **[New in v2.4]** |

The /ai/ reflex is the most analytically open question in the vocalic system: multiple surface outputs with conditioning still undetermined, including possible free variation and lexically-specific shifts. See §5 data-gathering bucket.

The /æ/-before-nasal pathway is distinct from the smoothed-schwa pathway for long /ɛː/, but both produce the same orthographic digraph `eu`. The orthography unifies the two diachronic feeds under one grapheme.

#### 4.4.3 Elision rules

Synchronically active processes deriving surface forms from etyma.

**E1. Intervocalic consonant elision.** /ɾ, dʒ, n, j, g, v/ delete between vowels. (/ɾ/ here is the alveolar tap — the GA intervocalic realization of /d/; the rule operates on the surface segment.) /n/ leaves behind nasalization on adjacent vowels. Fed by no rule; feeds vowel resolution. **[Settled]**

**E2 family. Coda treatment.** v1's generic E2 has been replaced with several focused rules. Each handles one segment or environment; they share the property of operating on word-final or syllable-final coda position.

- **E2a. Coda /t/ → /ʔ/.** Strictly coda-weakening rather than elision, but lives in this section structurally. Productive across the lexicon (*ŕeut* < *carrot*, *rhiiysseunnou* before /ʔ/-drop, etc.). **[Settled]**
- **E2b. Coda /d/ → ∅.** No compensatory lengthening on the preceding vowel. *rhiiynii* /ɻiːni/ "to need" < *need* shows the stem's /i/ remaining short after /d/ deletes, contrasting with the prefix's /iː/ (which arose by a different pathway, /ɪji/-smoothing). **[Settled in v2]**
- **E2c. Coda /l/ → ∅, multi-path.** /l/ has multiple elision paths along which singleton /l/ has been lost (per the §2.1 inventory note that /l/ "occurs only in clusters"). At least one path is attested: *toutw* /ˈtoːtw̩/ < *to total to* shows coda /l/ loss in a non-cluster environment. The full set of paths and conditions is **[Open]** and deferred to a later session.
- **E2d. Coda /ʔ/ stable.** Coda /ʔ/ does not elide under the regular cascade. **Lexical exception:** in grammaticalized particles (notably the *out* of phrasal-verb-derived stems), /ʔ/ is dropped. *beussou* /ˌbɛːˈsːoː/ "to fall asleep" < *pass out* and *rhiiysseunnou* /ɻiːsːɛːnːoː/ "to be different" < *really stand out* both drop the /ʔ/ from *out*; an optional careful-speech variant preserves it. **[Settled in v2; v1's "never elides" claim softened]**

**E3. Schwa elision in unstressed position.** Applies when not blocked by E1 or M1 having already created hiatus at that locus. Feeds cluster formation and syllabic-consonant promotion.

**E4. Schwa absorption.** Adjacent to another vowel, schwa is consumed by smoothing rather than elided.

**E5. Schwa strengthening.** Final stranded /ə/ in an open syllable strengthens to /a/. Initial unstressed /ə/ that survives to the final stage strengthens to /ɛ/ (parallel pathway, **[New in v2]**).

#### 4.4.4 Rhotic rules

**M1. Rhotic metathesis (retroflex only).** Intervocalic /ɻ/ relocates to onset position. The rule is motivated by GA r-coloring: /ɻ/'s articulation already extends across adjacent vowels, making it phonologically "loose" and relocatable in a way other consonants are not.

- **Trigger:** /ɻ/ in intervocalic position.
- **Required onset environment:** the word has either an onset /h/ or no onset at all.
- **When the onset is /h/:** the rhotic lands in onset, the /h/ ceases to function as an independent segment and is reanalyzed as a devoicing feature on the rhotic. Output: /r̥/.
- **When the onset is empty:** the rhotic lands in onset as plain /ɻ/.
- **When blocked** (any other onset): /ɻ/ stays in place and surfaces as /ɻ/. It does not elide and does not convert to /ɾ/.
- Coda /ɻ/ is not in M1's domain — it participates in the historical /er/ → /eː/, /or/ → /oː/ mergers (§4.4.2) instead.

Conditioning environment in detail (e.g., what counts as "intervocalic" across cluster boundaries) is **[Open]**. **[Settled in core, Open in edges]**

**C-Coal. Onset coalescence of /h/ + tap.** Sister rule to M1, sharing the /h/-as-devoicing-feature mechanism. When /h/ and /ɾ/ (or /ɻ/) come together in onset position by direct adjacency rather than by metathesis, the same coalescence applies: /h/ ceases to be an independent segment and reanalyzes as devoicing on the rhotic, producing /r̥/. Attested in *ŕe* /r̥ɛ/ "today" (< colloquial *today* with rapid-speech reduction producing /h/ + tap onset). **[New in v2; sister to M1]**

**R-Assim. Alveolar-wins rhotic assimilation.** Fires after M1 and C-Coal. If a word contains both an alveolar /ɾ/ and a retroflex /ɻ/, the retroflex assimilates to alveolar. This establishes the alveolar tap as the unmarked rhotic in the conlang. **[Settled]**

#### 4.4.5 Suprasegmental rules

**S1. Nasalization transfer.** When /n/ elides, nasality transfers to the adjacent vowels. The transfer typically lands on V₁ (left of the elided /n/) and/or V₂ (right of it); in the orthographic system, V₂ carries the nasalization mark by default (see *Orthography Reference* §3.5 for the V₁-pitch / V₂-nasalization placement rule). **[Settled]**

**S2. Breathy voice.** From elided coda /h/ or weakened obstruents. **[Provisional]**

**S3. Pitch placement.** Pitch lands on the syllable that carried primary stress in the GA etymon, regardless of where conlang stress has migrated to. Best analyzed as the F0 residue of GA-style prominence after the loudness-and-length components have transferred to the final vocalic position under the conlang's final-stress rule, rather than as an independently assigned dimension (see §3.4). Placement is **[Settled]**; whether the placement is *contrastive* (i.e., whether minimal pairs distinguishable only by pitch placement actually exist) is **[Open]** — see §5 for the structural account of why such pairs are scarce.

### 4.5 Worked derivations

Each row shows: GA etymon, conlang IPA, the rules that applied, the foot/appendix structure, and notes. Pitch and stress placement follow §3.3–3.4.

| GA etymon | GA IPA | Rules applied | Conlang IPA | Pitch | Stress | Structure |
|---|---|---|---|---|---|---|
| *Jennifer* | /ˈdʒɛnəfɻ/ | E1 (n→∅, nasalize); /ɻ/→syllabic /w/; smoothing | /ˈrɛ̃ːθw̩/ | /ɛ̃ː/ | /ɛ̃ː/ (coincide) | (ˈH) heavy foot + appendix |
| *Emma* | /ˈɛmə/ | E5 schwa strengthening | /ɛma/ | /ɛ/ | /a/ | (L)(L) two light feet, dissociated prominences |
| *Emily* | /ˈɛməli/ | E1 (l via /ɫ/→/j/→smooth); /ɪji/→/iː/ | /ɛmiː/ | /ɛ/ | /iː/ | (L)(ˈH) — pitch on left, stress on right |
| *Betty* | /ˈbɛɾi/ | E1 (tap d→∅); hiatus | /bɛi/ | /ɛ/ | /i/ | (L)(L) dissociated |
| *sodium* | /ˈsoʊdiəm/ | /s/→/h/; E1 (d→∅); hiatus stays | /ˈhoiom/ | /o/ | open question on final | hiatus retained |
| *countenance* | /ˈkaʊntənəns/ | /k/→/h/; massive E3; syllabic /n/, /ʔ/; /st/→/ts/ | /ˈhoʔn̩ʔn̩ts/ | /o/ | /o/ (coincide) | (ˈH) heavy foot + long appendix |
| *Rochester* | /ˈrɑtʃɛstɻ/ | /tʃ/→/ts/; E3; /ɻ/→syllabic /w/ | /ˈritsstw̩/ | /i/ | /i/ (coincide) | (ˈH) heavy foot + appendix |
| *carrot* | /ˈkæɻət/ → /ˈkæɻəʔ/ | /k/→/h/; /t/→/ʔ/ (E2a); M1 (/ɻ/→onset, /h/ as devoicing); smoothing /æ+ə/; /æ/→/eː/ | /r̥eːʔ/ | /eː/ | /eː/ (coincide) | (ˈH) heavy monosyllable |
| *radio* | /ˈɻeɪdiˌo/ | E1 (d→∅); no smoothing (no /ə/, distant Vs); stress to final | /reio/ | /e/ | /o/ | three syllables, hiatus retained |
| *baron* | /ˈbæɻən/ | M1 blocked (/b/ onset); /æ/→/eː/; E3 elides schwa; /n/ syllabic | /ˈbeɻn̩/ **[Provisional]** | /eː/ | /eː/ (coincide) | (ˈH) heavy foot + n-appendix |
| *barn* | /bæɻn/ | coda /ɻ/ → vowel coloring (/er/→/eː/ pathway); /n/ stays | /beːn/ | /eː/ | /eː/ (coincide) | (ˈH) heavy monosyllable |

#### Dictionary entries exercising the v2 rules

| Headword | GA etymon | Rules applied | Conlang IPA | Notes |
|---|---|---|---|---|
| *beussou* | *pass out* | /pʰ/→/b/ before /ɛ/; /æ/→/ɛː/; /s/→/sː/ at syllable boundary preceding stress; /aʊ/→/oː/; lexical /ʔ/-drop in *out* | /ˌbɛːˈsːoː/ | Geminate /sː/, /p/→/b/ environment, lexical /ʔ/-drop |
| *rhiiysseunnou* | *really stand out* | /ɫ/→/j/ between high front vowels; /ɪji/→/iː/; /æ/-before-nasal→/ɛː/ via tense-/æ/-with-duration pathway; /st/→/sː/; /nd/→/nː/ regressive assimilation; lexical /ʔ/-drop in *out* | /ɻiːsːɛːnːoː/ | Three geminates (/sː/, /nː/), /iː/ phoneme, /æ/-before-nasal pathway |
| *rhiiynii* | *really need* | /ɫ/→/j/; /ɪji/→/iː/; coda /d/→∅ (E2b, no comp lengthening) | /ɻiːni/ | Long /iː/ in prefix (etymological glide source) vs. short /i/ in stem (no comp lengthening from /d/-deletion) |
| *epplii* | *to apply* | Initial unstressed /ə/→/ɛ/ (E5); ambisyllabic /pp/→/pː/; /aɪ/→short /i/ (third reflex of /ai/) | /ˈɛpːli/ | New initial-schwa-strengthening rule, geminate /pː/, third /ai/ reflex |
| *toutw* | *to total to* | E1 on intervocalic /ɾ/ (from GA /t/); coda /l/→∅ outside cluster (E2c, multi-path flagged open); /aʊ/→/oː/; smoothing; final unstressed /u/→syllabic /w̩/ | /ˈtoːtw̩/ | Coda /l/ elision attested; final /w̩/ in appendix position |
| *ŕe* | *today* (colloquial *t'day* /tʰɾeɪ/) | C-Coal: /h/ + tap → /r̥/ in onset; irregular /t/→/h/ (lexically conditioned); irregular /eɪ/→/ɛ/ (lexically conditioned, frequency-driven) | /ˈr̥ɛ/ | New C-Coal sister rule to M1; light-monosyllabic foot (no minimality violation) |
| *ŕeut* | *carrot* | /k/→/h/; /t/→/ʔ/ (E2a); M1; smoothing; /æ/→/eː/ | /ˈr̥eːʔ/ | Canonical M1 derivation; pitch+stress coincide on /eː/ |

#### Issues surfaced by the table

- ***sodium*** → ***hoiiǫ* /ˈhoiõ/.** **[Closed v2.3]** The rule is committed: labial /m/ colors the preceding schwa to /o/ (rather than the expected /ɛ/ from regular strengthening), then /m/ elides leaving nasalization on the vowel → /-iõ/. Proposed as productive for all *-ium* endings (*podium*, *Colosseum*, *Liam*). Formalization as a §4 rule is pending a dedicated session.
- ***Annabeth*** — output depends on a phonemic question about the source (whether GA V₂ was /ɛ/ or /ə/). The conlang's choice forces a phonological commitment about the input. **[Open]**
- **Multi-stress GA etymons** — when a GA word had primary + secondary stress, does the conlang preserve both as pitch peaks, or only the primary? **[Open, carried forward from May 3 session]**

### 4.6 Probes and unresolved derivations

Words chosen to stress-test rule interactions where the description is silent or where two analysts could reasonably reach different outputs. Each probe specifies what it tests and what outputs are possible. These are forcing-functions for committing to ambiguous rules; they live alongside the worked derivations because they're the same kind of content at different stages of resolution.

#### Probes for E3 vs. M1 competition

**Probe: *pilot* /ˈpaɪlət/.**
- C₁ = /l/, not in E1 elision set, not a rhotic. Intervocalic position not vacated.
- V₂ = /ə/, eligible for E3.
- C₂ = /t/, eligible for E2a (→/ʔ/).
- Predicted: E3 fires, /l/ becomes syllabic, giving /ˈbail̩(ʔ)/ (with /p/→/b/).
- **Test:** does /l/ promote to syllabic, even though /l/ is described as "clusters only"? Or does the system block this? **[Decision needed]**

**Probe: *salad* /ˈsæləd/.**
- /s/→/h/ in onset.
- C₁ = /l/, not eligible for E1 or M1.
- V₂ = /ə/, eligible for E3.
- C₂ = /d/, eligible for E2b (→∅).
- Predicted: /ˈhæl̩/ with syllabic /l/, possibly /ˈheːl̩/ if smoothing intervenes.
- **Test:** confirm /d/-deletion path; confirm /l/-syllabification. **[Decision needed]**

#### Probes for cascade in dactyls

**Probe: *Penelope* /pəˈnɛləpi/.**
- Multiple loci for elision: /n/ (E1), /l/ (not E1), schwas (E3 or E4).
- Stress originally on V₂; what happens after rules apply?
- Predicted (one path): E1 elides /n/ → /pəˈɛ̃ləpi/ → smoothing → /ˈbɛ̃ːləpi/. Then E3 may elide the next schwa → /ˈbɛ̃ːlpi/.
- **Test:** does the cascade run left-to-right, or does it apply globally and re-evaluate? **[Decision needed]**

**Probe: *Daniela* /ˌdæniˈɛlə/ or /ˌdænˈjɛlə/.**
- Already iambic (stress on penult); right-headed foot construction should be vacuous on stress placement.
- E1 applies to /n/ (→ nasalization); /l/ not in the E1 set.
- Predicted: a form like /rẽˈirɛrə/-shape depending on /d/, /n/, /l/ treatments.
- **Test:** working stress assignment with multiple eliding loci. **[Decision needed]**

#### Probes for smoothing edge cases

**Probe: a CVCVC where smoothing yields a long vowel of a quality the inventory doesn't support.**

- Long-vowel inventory: /iː, ɛː, oː, aː, ɨː/.
- Test word: *ladder* /ˈlæɾɻ/. After E1 on /ɾ/ (and possibly M1 on /ɻ/), what's the resulting long vowel quality? /æ/→/eː/, but the second segment is rhotic, not vowel.
- **Test:** when smoothing would produce a quality outside the long-vowel inventory, does it fail and retain hiatus, or coerce to the nearest inventory member? **[Open]**

**Probe: *idea* /aɪˈdiə/.**
- After E1 on /d/: /aiˈiə/ → smoothing of /iə/ → /aiˈiː/? Or does /ai/ → /iː/ apply first, giving /iˈiː/ → /iː/?
- **Test:** does /ai/ → /iː/ apply *before* or *after* E1 creates new hiatus? Rule ordering question. **[Open]**

#### Probes for nasalization persistence

**Probe: *ginger* /ˈdʒɪndʒɻ/.**
- Both /n/ and /dʒ/ are in the E1 set; /ɻ/ becomes syllabic.
- Predicted: /ˈrɪ̃rw̩/ or /ˈrɪ̃w̩/ depending on /ndʒ/ resolution.
- **Test:** does nasalization survive into a closed syllable? Or only in open syllables? **[Open]**

#### Probes for syllabic /j, w/ in non-final position

**Probe: *tomorrow* /təˈmɑɻo/.**
- /m/-onset blocks M1; /ɻ/ stays. /ɑ/→/o/, schwa absorbed.
- Predicted: /toˈboɻo/ or /təˈboɻo/, with possible final /o/ → syllabic /w/.
- **Test:** the syllabic-glide rule's domain — final only, or anywhere? **[Open]**

#### Probes for monosyllables

**Probe: *cat* /kæt/, *song* /sɔŋ/, *tree* /tɻiː/.**
- *cat*: /k/→/h/, /æ/→/eː/, /t/→/ʔ/ → /heːʔ/. Clean derivation.
- *song*: /sɔŋ/ → /hoŋ/, but /ŋ/ isn't in the inventory — possibly /n/ with vowel nasalization, giving /hõ/.
- *tree*: cluster /tɻ/ in onset is unusual — does /ɻ/ undergo M1? Or is the cluster preserved?
- **Test:** monosyllabic outputs and cluster behavior in onset position. **[Open]**

---

## 5. Open questions

### Carried forward from v1 and the May 3 pitch session

### Data-gathering bucket — conditioning unclear, possible free variation (opened v2.4)

The following shifts are attested in dictionary entries but lack sufficient data to commit an environment. They may have conditioned reflexes, free variation, or lexically-specific (irregular) outcomes. Collect more attestations before proposing rules. Do not treat these as settled.

- **/ai/ reflex** — at least four surface outcomes attested: /eː/, /i/, /ɛ/ (short), /i/ (short, possibly the same as the second but distinct from the first). Conditioning factors guessed at: stress position, preceding/following consonant, syllable count, lexical frequency. May include free variation. **[Open — data gathering]**
- **/v/ conditioning** — proposed split: /v/ → /ɾ/ (tap merger) before front vowels; /v/ → /b/ (labial onset) before back vowels. Multiple attestations in each direction, but boundary cases unresolved. May also include free variation. **[Open — data gathering]**
- **/ɫ/ dark-l vocalization** — all /l/-initial GA words so far produce /r/-initial headwords; candidate path: /ɫ/→/ɻ/→R-Assim→/ɾ/. Relationship to the existing /ɫ/→/j/ rule (between high front vowels) unclear — possibly one rule with environment-dependent outputs. **[Open — data gathering]**
- **/ɪ/→/ɛ/ lowering** — originally flagged as conditioned by following /b/; now attested without /b/ in context. May be a general unstressed-/ɪ/→/ɛ/ rule, or conditioned on syllable position. **[Open — data gathering]**
- **/ə/→/o/ or /ɪ/→/o/ rounding after /n/** — two attestations in nasal-initial words; mechanism unclear (nasalization coloring? labial spreading?). **[Open — data gathering]**

### Carried forward from v1 and the May 3 pitch session

- Conditioning of /ai/ → /eː/ vs. /i/. (/iː/ outcome ruled out May 2026; two-way conditioning still open. Expanded to full data-gathering bucket above.)
- Is /r/ syllabic?
- Treatment of /h/ in onset clusters from /s/- and /k/-debuccalization edge cases.
- M1 edge cases — what counts as "intervocalic" across cluster boundaries; behavior in trisyllabic words with multiple potential M1 sites.
- Whether the **/k/-as-allophonic-/h/-before-glides** analysis holds.
- Smoothing failures when the resulting long vowel would be outside the inventory.
- Interaction of /ai/ with new hiatus from E1.
- Persistence of nasalization across resyllabification.
- Domain of syllabic /j, w/ — final only, or anywhere?
- Treatment of monosyllables — coda /ŋ/, onset clusters with /ɻ/.

### Newly opened in v2.1

- **Other /iX/ diphthongal long vowels.** Whether bimoraic diphthongal nuclei beyond /iɛ/ occur (e.g., /io/ spelled `iio`). Predictable by analogy from the /iɛ/ pattern but no attestations yet. See §2.2.

### Newly opened in v2

- **E2c — coda /l/ elision paths.** /l/ has multiple elision paths along which singleton /l/ has been lost; the full set is undescribed and deferred to a later session.
- **Appendix licensing conditions.** Working hypothesis: a syllable is parsed as appendix when its nucleus is a syllabic consonant of low sonority and it follows the stressed full vowel. Edge cases need testing.
- **Appendix and minimum-word effects.** Does the conlang have a minimum-word constraint? If so, does appendix material count toward satisfying it? Bears on the licensing of light-monosyllabic forms like *ŕe*.
- **Diachronic trajectory of the appendix.** The current state is best read as a snapshot mid-restabilization; does this matter for any synchronic decision, or is it purely a framing claim?
- **/ts/ in *countenance*.** Is the final /ts/ a complex coda on the second /n̩/ syllable, or is it a fourth nucleus in its own right? Affects appendix-syllable count and whether /ts/ is licensed as a syllabic affricate.
- **Internal structure of the appendix.** Are the nuclei in *hoʔn̩ʔn̩ts* a flat sequence of σ adjoined to ω, or is there sub-grouping (e.g., a degenerate foot containing /ʔn̩ʔn̩/)?
- **Appendix–pitch interaction.** If pitch is contrastive (still open), does the appendix participate in the pitch contour, or is it pitch-flat?
- **Confirmation of pitch-accent contrast.** Whether minimal pairs distinguishable only by pitch placement actually exist (audio-recorded verification deferred). Under the v2.2 residue analysis (§3.4), low minimal-pair density is **structurally expected** — GA stress's segment-shaping power has absorbed most of the territory pitch could carry contrast in — and is not, on its own, evidence about contrastiveness, allophony, or vestigiality. Note on search strategy: GA stress-shift derivational pairs (*récord*/*recórd*, *présent*/*presént*, *súbject*/*subjéct*) are not clean candidates — in GA, unstressed vowels reduce to schwa, so it is vowel quality doing as much heavy lifting as stress. The conlang reflex pairs would differ in more than pitch alone. A different search strategy (targeting pairs where the GA etymons share segment quality across the stress-site) is needed.
- **Multi-stress GA etymons.** When a GA word had primary + secondary stress, does the conlang preserve both as pitch peaks, or only the primary?

### Closed by v2.3

- **/ɪ~ɨ/.** One phoneme: /ɪ/. Surface /ɨ/ is an allophone. Closed May 2026.
- **/ɑ~ɔ/.** One phoneme: /ɑ/. Closed May 2026.
- **Nasalization.** Phonemic. Closed May 2026.
- **Breathy voice.** Not phonemic — allophonic `VhV`. Medial /h/ in fused particles (*noho*, *hiho*) has the same allophonic status; proposed `VhV`/`VhU` distinction not adopted. Closed May 2026.
- **/ai/ → /iː/ outcome.** Ruled out. The two-way /eː/ ~ /i/ conditioning question stays open. Closed May 2026.
- ***sodium* derivation.** Committed as *hoiiǫ* /ˈhoiõ/ via labial-coloring-of-schwa + /m/-elision-with-nasalization. Proposed productive for all *-ium* endings; rule formalization in §4 pending. Closed as an open derivation; opened as a pending rule ticket. Closed May 2026.

### Closed by v2

- **Geminates as a category.** /sː, nː, pː/ admitted as a sub-inventory; doubled-consonant orthographic convention generalized. Closed via dictionary batch.
- **/iː/ as a phoneme.** Admitted to the long-vowel inventory; spelled `iiy`. Closed via dictionary batch.
- **/s/ → /sː/ at syllable boundary preceding stress.** Rule added to §4.4.1. Closed.
- **/p/ → /b/ environment.** Specified: before /ɛ/ and its long counterpart, blocked elsewhere. Closed.
- **Coda /ʔ/ exceptions.** v1's "never elides" softened to admit lexical exceptions in grammaticalized particles. Closed.
- **/nd/ → /nː/.** Settled as regressive assimilation. Closed.
- **Initial unstressed /ə/ → /ɛ/.** Rule added to E5 (parallel to final-schwa-strengthening). Closed.
- **Coda /d/ → ∅, no compensatory lengthening.** Confirmed; rule added as E2b. Closed.
- **/æ/-before-nasal → /ɛː/.** Distinct pathway from smoothed-schwa, both feeding `eu`. Closed.
- **/h/+tap coalescence.** Settled as separate sister rule (C-Coal) to M1, sharing the devoicing mechanism. Closed.
- **Aspiration.** Confirmed as fully allophonic, not orthographically represented. Closed.
- **Degenerate-foot minimality.** v1's clause restricting degenerate feet to heavy syllables retired. Light-monosyllabic feet are licensed. Closed via *ŕe* attestation.
- **Quantitative metathesis (D1).** Confirmed as a consequence of right-headed foot construction, not a separate rule. Closed via May 3 session.
- **Pitch placement.** Settled as lexically determined by GA etymon; orthographically marked with acute on the relevant vowel. Closed via May 3 session.
- **Sesquisyllabic terminology.** Retired. *Appendix* is the correct term. Closed.

---

## 6. Glossary

Technical vocabulary used throughout. Inline short definitions appear in earlier sections at first use; this glossary is the consolidated reference.

**Appendix.** Material adjoined to the prosodic word at a level above the foot. Weight-bearing (moraic) but stress-invisible (foot-external). The structural mechanism for the conlang's post-stress syllabic-consonant tails (§3.5).

**Appendix nucleus.** A syllabic consonant heading a syllable that is part of the appendix rather than the head foot.

**Bleeding and feeding.** Standard ordering relations between rules. Rule A **feeds** Rule B if A creates the input environment for B. Rule A **bleeds** Rule B if A removes (consumes) inputs that B would otherwise have applied to. The cascade in §4.2–4.3 is built on a feeding-then-bleeding sequence.

**Compensatory lengthening.** The lengthening of a vowel to "compensate" for the loss of a neighbouring segment. In the conlang, compensatory lengthening occurs when intervocalic /d/ elides and V₁+V₂ smooth into V₁ː. Notably it does *not* occur in coda /d/ deletion (E2b), where the preceding vowel stays short.

**Concord affixes.** *(Morphological term, used in `language_reference.md`; included here for cross-reference completeness.)* Affixes on the main verb stem that show concordance with the light verb complex. Defined in `verbal-system.md` §4.

**Foot.** A grouping of one or two syllables carrying a single primary prominence. The conlang builds **trochaic feet right-to-left**, with the **rightmost foot** receiving primary stress (right-headed prosodic word, left-headed foot — common cross-linguistically). The final foot is the last two syllables (or the last syllable, if only one survives elision).

**Head (of a foot).** The prominent syllable within a foot. The default head is the leftmost (trochaic).

**Mora (μ).** The unit of syllable weight. A short vowel = 1μ. A long vowel = 2μ. A syllabic consonant = 1μ. Coda consonants are non-moraic by default; syllabic consonants (which are moraic) can occupy coda position.

**Prominence.** Generic term for stress-like salience. Includes primary stress, secondary stress, and pitch-accent prominence.

**Quantitative metathesis.** A traditional term for the rightward shift of stress (or vowel length) across positions in a word. In the conlang, what looks like quantitative metathesis in dactyl-shaped words is now understood as a *consequence* of right-headed foot construction (§3.2), not a separate rule.

**Recursive prosodic structure.** Prosodic constituents (foot, prosodic word) that contain or are adjoined to other constituents of the same level. The mechanism by which appendix material attaches to the prosodic word.

**Resyllabification.** The redrawing of syllable boundaries after a segment is added or lost. After vowel elision, the orphaned consonant either joins the preceding syllable as a coda or becomes a syllabic nucleus of its own.

**Sesquisyllable.** A defined left-edge phenomenon in Mainland Southeast Asian languages: a reduced presyllable precedes a major stressed syllable, with the prosodic word iambic in shape. **The conlang's post-stress consonantal tails are NOT sesquisyllabic** (despite earlier drafts using the term). The structural details — direction (post-stress vs. pre-stress), shape (trochaic-with-tail vs. iambic), nucleus inventory, length — all diverge. Use *appendix* (above) for the conlang's pattern.

**Sonority.** A scalar property of segments, roughly: vowels > glides > liquids > nasals > fricatives > stops. The **Sonority Sequencing Principle** (SSP) says syllable nuclei should be drawn from the most sonorous available segments. The conlang stretches this — it allows /s, θ, ʔ/ as syllabic, which are unusually low on the scale.

**Spondee.** A traditional foot name for a two-syllable foot where both syllables bear stress (DUM-DUM). Earlier drafts of this document used *spondee* and *stress clash* to describe certain conlang outputs. Both are retired: what was previously analyzed as clash is now understood as pitch-stress dissociation (pitch on one syllable, stress on another), not as two stresses on adjacent syllables.

**Stress clash.** Two adjacent syllables both bearing primary or near-primary stress. Retired from the conlang's analysis (see *Spondee*).

**Syllable weight.** A function of moraic content. **Light** = 1μ (short V, open syllable). **Heavy** = 2μ (long V, or short V plus syllabic consonant in same syllable).

**Trochee, iamb, dactyl.** Traditional foot names for stress patterns: trochee = DUM-bah, iamb = bah-DUM, dactyl = DUM-bah-bah. The conlang's default foot is trochaic (left-headed); the prosodic word is right-headed (rightmost foot is the head foot).

---

## 7. Versioning notes

### v2.4, May 2026 — three rules committed; data-gathering bucket opened

**Three rules added to §4.4 from dictionary batch work.**
- **§4.4.1:** /ɔɪ/→/oe/ added to the vocalic mergers table. Attested in *bœ*, *boeś*, *nœ*.
- **§4.4.1:** /s/ cluster-protection added: debuccalization blocked when /s/ heads an onset cluster (e.g., /sp/, /sk/). See *spyi*.
- **§4.4.1:** /k/ labialization added: coda /k/ + adjacent /w/ → onset /kʷ/; blocks coda /k/→∅; geminate /kʷː/ when ambisyllabic. See *piiquóæ*, *piquô*, *récquıìs*.

**Data-gathering bucket opened (§5).** Five conditioning-unclear shift patterns collected from 36-entry dictionary batch: /ai/ reflex (now confirmed multi-way), /v/ conditioning, /ɫ/ dark-l vocalization, /ɪ/→/ɛ/, /ə/→/o/ after /n/. All marked [Open — data gathering]. May include free variation or lexically-specific outcomes; do not commit until more attestations and a dedicated analysis session.

**§4.4.2 /ai/ prose updated** to point to §5 data-gathering bucket rather than claiming three defined outputs.

### v2.3, May 2026 — phoneme inventory closures; /ai/ narrowed; *sodium* committed

**Phoneme inventory closures (§2.2, §2.3, §5).**
- /ɪ~ɨ/ consolidated to a single phoneme /ɪ/; surface /ɨ/ is allophonic.
- /ɑ~ɔ/ consolidated to a single phoneme /ɑ/.
- Nasalization: phonemic. [Settled].
- Breathy voice: not phonemic — allophonic `VhV`. Medial /h/ in fused particles (*noho*, *hiho*) carries the same allophonic status; proposed `VhV`/`VhU` phonemic distinction not adopted.

**§4.4.2 /ai/ reflex narrowed.** /iː/ is ruled out as an outcome of /ai/. The two-way /eː/ ~ /i/ conditioning remains open.

***sodium* derivation committed (§6.1).** Headword revised to *hoiiǫ* /ˈhoiõ/. The committed rule: labial /m/ colors the preceding schwa → /o/ (rather than expected /ɛ/), then /m/ elides leaving nasalization on the vowel → /-iõ/. Proposed productive for all *-ium* endings; formalization as a §4 rule is deferred to a dedicated phonology session.

**§5 open-questions list updated.** Closed items moved to "Closed by v2.3." Pitch-accent minimal-pairs note updated: GA stress-shift pairs (*récord*/*recórd*, etc.) are not clean candidates because unstressed vowels reduce to schwa in GA, making vowel quality and stress co-vary. A search strategy targeting pairs where segment quality is held constant across the stress-site is needed.

### v2.2, May 2026 — pitch as residue of GA prominence

**§3.4 reframed.** The pitch placement rule (pitch on the syllable that carried GA primary stress) is unchanged. The analytical framing is sharpened: pitch is now treated as the **phonetic residue of GA-style prominence** after stress has migrated to the final vocalic position, rather than as an independently assigned prosodic dimension. Speakers do not target pitch as a separate articulatory dimension; loudness and length transfer to the final under final-stress, F0 stays behind. The "two prominences" pattern falls out of redistribution.

§3.4 now contains: a brief statement of the placement claim; the residue analysis; a diachronic-pathway diagram (Stage 0 GA → Stage 1 transitional → Stage 2 current); cross-linguistic parallels (Tokyo Japanese pitch-accent emergence; tone-from-accent in Bantu); the **etymologically determined / not synchronically predictable** distinction (sharpened from earlier "lexically determined and not predictable from the surface form" framing, which conflated two senses of "predictable"); a structural account of why minimal pairs are scarce (GA stress's segment-shaping power has absorbed most of pitch's potential contrastive workspace); the **GA stress-shift derivational pair** corner (*récord*/*recórd* etc.) as the candidate workspace for genuine pitch-only minimal pairs; **phonetic predictions** under the residue analysis (V₁ should retain slight length and amplitude beyond pure F0; F0 peak nucleus-aligned); and a **pedagogical note** as a teaching artifact.

**§1.1 pitch-stress dissociation bullet** updated to mention the redistribution-of-prominence framing and point at §3.4. Wording around "independent prosodic features" softened.

**§2.3 pitch-accent suprasegmental bullet** updated to make the etymological / synchronic distinction explicit, with the English lexical-stress comparison.

**§4.4.5 S3** updated to characterize pitch as F0 residue of GA-style prominence after loudness and length transfer to the final, rather than as an independent placement rule. Placement claim and **[Settled]** status unchanged.

**§5 contrastiveness question reframed.** The contrastiveness open question now flags low minimal-pair density as **structurally expected** under the residue analysis (GA segment-shaping absorbs the workspace), not as evidence of weakness. GA stress-shift derivational pairs are flagged as the candidate corner where genuine pitch-only minimal pairs could survive. A targeted survey is added to pending work.

**Orthographic conventions unchanged.** Pitch is still marked, because pitch is still lexical, regardless of whether it is analyzed as a feature target or as residue.

**Source.** Integrated from `drafts/integrated/2026-05-06-pitch-accent-diachrony.md` (working note, May 2026).

### v2.1, May 2026 — diphthongal long vowel; audience-fit reframings; cross-doc fixes

**§2.2 — diphthongal long vowel /iɛ/ admitted.** The long-vowel category is generalized into two surface types: *monophthongal long vowels* /iː, ɛː, oː, aː, ɨː/ (existing, with `ː` in IPA) and *diphthongal long vowels* /iɛ/ (new, no `ː` because the second mora supplies a distinct vowel quality rather than length). Forced by the topic-particle paradigm in `language_reference.md` §3.7 (the article-incorporating form of the visibility particle *hii* /hi/ is *hiie* /hiɛ/) and by the parallel admission in `orthography.md` v2.1 (§3.3). The §2.2 "Diphthongs (monomoraic)" header is added to clarify the contrast with bimoraic diphthongal long vowels; the `ei` vs. `iie` minimal pair is the cleanest illustration.

**§5 — two new open questions.**
- *Genuine medial /h/ vs. breathy voice.* Whether the topic particles *noho* / *hiho* attest a phonemic /h/ distinct from breathy voice. Parallel question raised in `orthography.md` §6 with a candidate orthographic disambiguation; phonology owns the phonemic-status side.
- *Other /iX/ diphthongal long vowels.* Whether bimoraic diphthongal nuclei beyond /iɛ/ occur (e.g., /io/ as `iio`).

**§6 — glossary cross-reference repointed.** The *Concord affixes* entry pointed to retired `verb-terminology.md` §1.3; repointed to `verbal-system.md` §4.

**§1.3 reframed as background.** A note at the head of §1.3 marks the typological-position discussion as analytical context, not required for using the language. Content unchanged. Targeted at the linguistically-aware-learner audience — the typological references (Tashlhiyt, Nuxalk, Salishan, etc.) are valuable but presuppose more typology than the audience needs to use the language.

**§3.5 analytical citations relegated to a closing remark.** The inline parenthetical "(Selkirk 1986, 1996; Itô & Mester 1992 and later)" is removed from the body and consolidated into a closing "Analytical sources" remark at the end of §3.5. Same intent as the §1.3 reframe.

### v2, May 2026 — post-dictionary-batch and post-stress-appendix revision

**Structural reorganization.** Top-level structure changed from v1's 10-section apparatus-first layout to a 7-section top-down layout: outline → inventories → syllable/metrical structure → diachronic development → open questions → glossary → versioning. The glossary moved to the end; metrical content consolidated into §3 instead of being split between §1.2, §2, and §8; cascade and worked derivations consolidated into §4 instead of being split between §4, §5, §6, and §7.

**Inventory additions.**
- /iː/ admitted as a phoneme (§2.2). Previously denied by `orthography.md` §3.2 and under-acknowledged by phonology.md §3.1.
- Geminate sub-inventory (/sː, nː, pː/) admitted (§2.1).
- Aspiration confirmed as allophonic, not orthographically represented (§2.1).

**New rules added to §4.4.**
- /s/ → /sː/ at syllable boundary preceding stress.
- /p/ → /b/ before /ɛ, ɛː/, blocked elsewhere.
- /pp/ ambisyllabic → /pː/.
- /nd/ in coda → /nː/ by regressive assimilation.
- /æ/-before-nasal → /ɛː/ via tense-/æ/-with-preserved-duration pathway.
- Initial unstressed /ə/ → /ɛ/ (added to E5).
- E2 family replacing v1's generic E2: E2a /t/→/ʔ/, E2b /d/→∅ no comp lengthening, E2c /l/-paths flagged open, E2d /ʔ/ stable with lexical exceptions.
- C-Coal: sister rule to M1 for /h/+tap coalescence in onset.

**Rules softened or retired.**
- Coda /ʔ/'s "never elides" softened to admit lexical exceptions in grammaticalized particles.
- /ai/ → /iː/ ~ /eː/ extended to three-way: /iː/ ~ /eː/ ~ /i/ (conditioning open).
- v1's degenerate-foot minimality clause (§8.1) retired. Light-monosyllabic feet are licensed.

**Appendix analysis.** The §3.5 analysis is new in v2: post-stress syllabic-consonant material is now treated as appendix (adjoined to the prosodic word above the foot level), not as sesquisyllabic. The term *sesquisyllabic* is retired from the conlang's description and flagged in the glossary as borrowed-but-misapplied.

**Worked derivations updated.** Existing rows for *Jennifer*, *Rochester*, *countenance* updated to use appendix terminology. New rows added for the dictionary entries *beussou*, *rhiiysseunnou*, *rhiiynii*, *epplii*, *toutw*, *ŕe*.

**Open questions reset.** §5 reorganized into "carried forward," "newly opened in v2," and "closed by v2." Closures total 14 items; new opens total 9.

**Predecessor: May 3 2026 pitch-accent revision.** v2 builds on the May 3 revision that introduced pitch-stress dissociation (pitch on the historical-GA-stress vowel, stress on the final vocalic position), the V₁-pitch / V₂-nasalization orthographic convention, the right-headed foot construction analysis (which collapsed v1's D1 quantitative metathesis rule), and the corrected *Emily* and *Emma* derivations. All May 3 closures and additions are preserved in v2.

### v1 (pre-May 3 2026)

Original document. Established the four-process pipeline framing (§1.1), the rule inventory (E1–E5, M1, R-Assim, S1–S3), the cascade tables, and the worked derivations table. Closed by v2 in places where dictionary work or the May 3 session forced commitment.
