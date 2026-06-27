# Phonology Reference

**Version:** v4.8 (June 2026)
**Predecessor:** v3 and earlier — see §7 (Versioning Notes).

**Abstract.** The phonology derives from General American English through a designed cascade of regular sound changes, frozen at a synchronic stage. Its character: a small, reorganized consonant inventory; widespread vowel clusters and long vowels from intervocalic elision; permissive onsets against restricted codas; post-stress syllabic-consonant material housed in a prosodic appendix; and pitch dissociated from stress, analyzed as the residue of GA prominence after stress migrated to the word-final position. Suprasegmentals — pitch, length, nasalization, breathy voice — do as much expressive work as segments. This document is the canonical reference for the inventories, the syllable and metrical structure, the rule cascade with worked derivations, and the phonological open-questions backlog.

`language_reference.md` §2 carries this document's orientation abstract.

Status tags — **[Settled]** committed; **[Provisional]** current best analysis, expected to hold; **[Open]** explicitly undecided — and the reading conventions (asterisked GA etyma, slashes for phonemes, italics for working orthography) are explained in `language_reference.md`, "How to read this document set." Terminology follows `terminology-registry.md`.

---

## 1. The phonology in outline

### 1.1 Character of the system

The conlang's phonology has a recognizable shape that organizes most of what follows. Five interlocking choices define it.

**Small consonant inventory, reorganized.** GA's consonant set has been substantially reduced through targeted mergers — the soft six /d, dʒ, n, j, g, v/ collapsed into a tap, /m/ (and conditionally /p/) into /b/ in onset, /f/ into /θ/, /s/ debuccalized to /h/. The surviving inventory is smaller than GA's, but distributed in unfamiliar ways: most of the segments occur in GA, but their distribution and patterning are foreign.

**Vowel-cluster-friendly.** Intervocalic consonant elision has produced widespread vowel hiatus, long vowels from smoothing, and diphthongs from reanalysis. Where GA has a single intervocalic consonant, the conlang often has a long vowel or an open hiatus. *sodium* /ˈsoʊdiəm/ → *hoiiǫ* /ˈhoiõ/ is canonical.

**Cluster-permissive in onsets, restricted in codas.** Long onset clusters survive (*ritsstw* "Rochester"); coda phonotactics is tighter, with most coda consonants reduced to /ʔ/ or eliminated outright. The asymmetry is a familiar one cross-linguistically; the closest natural-language parallel is Ancient Greek (cluster-permissive onsets, /n, r, s/-only codas), though the conlang's coda restrictions are even tighter.

**Post-stress consonantal appendix.** A subset of words have substantial syllabic-consonant material *after* the stressed vowel — *Jennifer* /ˈrɛ̃ːθw̩/, *countenance* /ˈhoʔn̩ʔn̩ts/, *Rochester* /ˈritsstw̩/. This material is weight-bearing (the syllabic consonants are moraic) but stress-invisible (primary stress stays on the leftmost full vowel). The structural term is *prosodic appendix*; see §3.5.

**Pitch-stress dissociation.** Stress falls on the final vocalic position; pitch sits on the syllable that carried primary stress in the GA etymon. These are usually different syllables, producing the characteristic shape of *Emma* /ɛma/ — pitch on the first vowel, stress on the second. The two are best analyzed as a redistribution of GA prominence across the word rather than as independently assigned features; see §3.4.

The unifying thread is that suprasegmentals do as much expressive work as segments. Pitch, length, nasalization, and breathy voice are all phonologically active; the orthography reflects this with a load of diacritics that are not decorative. A reader treating the diacritics as ornamental will collapse pairs the language treats as fully distinct.

### 1.2 How this differs from GA

The conlang's prosodic and segmental shape inverts GA almost completely.

GA is stress-timed, with aggressive vowel reduction in unstressed positions, initial-leaning stress, default trochaic feet (DUM-bah), and stress as the primary locus of prominence. The conlang is closer to syllable-timed, with the GA reductions *frozen into the surface lexicon* rather than performed live. Stress is final, the default foot is iambic (bah-DUM), and pitch carries a melodic dimension that GA does not have. A GA listener hears the conlang's segmental material as recognizable but the rhythmic shape as foreign — which is exactly the design intent.

Three further inversions worth flagging up front:

- **Schwa is not a reduction vowel.** GA's pervasive schwa has either been absorbed into long vowels (smoothing), elided (creating consonant clusters and syllabic consonants), or strengthened to /a/ or /ɛ/ depending on position. Where GA distributes schwa across most unstressed syllables, the conlang has none. This grounds the low-back vowel asymmetry behind the orthographic `au` = /ɑ/ (short) decision: GA's lower back /ɑ/ is relatively long, but its short counterpart (schwa) has lost phonemic status, so the smoothed-`a`+ə source surfaces as plain short /ɑ/ rather than a long /ɑː/ — a naturalistic gap (`orthography.md` v3.7). **[Provisional — under analysis.]**
- **The rhotic system is reorganized.** GA's single rhotic /ɹ/ has split into a tapped /ɾ/ and a retroflex /ɻ/, with /ɻ/ becoming /ɾ/ near another /ɾ/ (alveolar wins). Where GA uses /ɹ/ for /d, dʒ, n, j, g, v/-mergers, the conlang uses the tap. Notationally, GA "r" is broad transcription for what is already /ɻ/, so a derivation step written "/r/ → /ɻ/" marks **retention**, not a change; the genuinely innovative rhotic is the **tap /ɾ/**, phonemicized from GA's positional /d/-flap allophone (and the soft-six mergers). Dictionary Sound-changes lines are renotated accordingly.
- **Coda /ʔ/ is stable.** GA's variable /t/-glottalization has phonologized: /ʔ/ is the regular reflex of GA coda /t/, and it does not elide further (lexical exceptions in grammaticalized particles: the out-drop, §4.4.11).

### 1.3 Typological position and stability

The system is naturalistic but typologically unusual: each component sits in attested territory, but the assembly is not matched by any single natural language, and the current state is best read as a synchronic snapshot of a language mid-restabilization (captured after aggressive schwa elision produced the appendix material, but before the typologically-expected next reduction or secondary-stress step). For a conlang fixed at a synchronic stage this is not a problem — it is exactly the right origin for a system at this stage.

> *Design context.* The natural-language precedents (Tashlhiyt Berber, Nuxalk, English/Slavic, Ancient Greek, and the looser resonances), the distinctive-combination argument, and the full stability/naturalism discussion are collected in `language_reference.md` Appendix A.3. They are analytical justification, not required for using or learning the language; readers focused on inventory and rules can skip to §2.

---

## 2. Inventories

### 2.1 Consonants

**Stops:** /b, t, ʔ/. **[Settled]**

Note on /k/: surface [k] occurs only in /kj, kw/ clusters. The current working analysis is that **/k/ is not a phoneme**: surface [kj, kw] are allophonic realizations of underlying /hj, hw/, with [k] arising as fortition of /h/ before a glide. **[Provisional, under analysis]**

Coda /ʔ/ is the most stable coda segment in the language and serves as a reliable anchor in derivations. It does not elide under the regular rules; lexical exceptions apply in grammaticalized particles (the out-drop; see §4.4.11). **[Settled]**

**Fricatives:** /θ, h, ts, s/. **[Settled]**

- /h/ derives from GA /s/ via debuccalization — the consonant loses its mouth posture and surfaces as a bare /h/ — in most positions, and from GA onset /k/ in parallel.
- /ts/ derives from the historical /st/ cluster.
- /s/ as a phoneme survives in contexts where the historical /st/ produced it (taking the synchronic place of /s/ in clusters), and in geminate /sː/ position (see below).

**Geminates:** /sː, nː, pː/ are attested as a sub-inventory; the labialized geminate /kʷː/ is attested at compound junctions (see §5.5).

Geminates arise from two diachronic feeds:

1. **Phonologization of GA ambisyllabic consonants** in stressed-second-syllable environments. *beussou* /ˌbɛːˈsːoː/ "to fall asleep" (< *pass out*) phonologizes the slight gemination GA already has at these boundaries. (The labial parallel /pp/ → /pː/ is predicted but currently unattested — see labial gemination, §4.4.6.)
2. **Cluster collapse.** *rhiiysseunnou* /ɻiːsːɛːnːoː/ "to be different" shows /nd/ in coda → /nː/ by regressive assimilation (/d/ → /n/, then geminate). The same form's /sː/ comes from GA /st/ at a stressed-syllable boundary.

The /s/ → /sː/ rule at syllable boundary preceding stress is in tension with the more general /s/ → /h/ debuccalization rule; the gemination wins in this specific environment (**pass-out gemination**; see §4.4.6).

**Nasals:** /n, m/. **[Settled]**

**Liquids/Tap:** /r/ (tapped), /l/ (clusters only), /ɻ/ (assimilates to /r/ near another /r/). **[Settled]**

**Glides as syllabic consonants:** /w, j/ — occur as unstressed allophones of /o, i/ in syllabic-consonant position. **[Settled, per current note]**

**Syllabic consonants generally:** /n, m, s, θ, ʔ, w, j/ — and possibly /r/. These segments occur as syllabic nuclei in **appendix position** (post-stress, foot-external; see §3.5). They are moraic but stress-invisible. **[Provisional]**

**Voiceless sonorants:** /n̥, m̥, ɾ̥/ exist as distinct surface forms, arising from elided coda obstruents and from the whispered-r mechanism (the wandering r and kin; see §4.4.3). The orthography marks devoicing with an acute accent on the consonant.

**Aspiration** is treated as fully allophonic (English-style: voiceless stops aspirate in stressed onsets) and is not represented orthographically. **[Settled]**

**Notable gaps relative to GA.** Sounds present in GA but absent here: /k, dʒ, tʃ, ʒ, g, ŋ, v, f, d, p, ʊ, ʌ, u/. Most have specific merger paths (see §4.4). /k/'s "absence" is the analytical move — surface [k] in /kj, kw/ is reanalyzed as allophonic /h/ + glide. **[Settled, with /k/ analysis Provisional]**

### 2.2 Vowels

**Short:** /i, ɪ, ɛ, o, ɑ/ **[Settled]**

Surface [ɨ] is an allophone of /ɪ/, and surface [ɔ] an allophone of /ɑ/; neither is an independent phoneme.

The /i/ vs. /ɪ/ contrast deserves a note: /i/ is the short tense vowel inherited from GA "long-e" /ɪi/, with its gliding quality preserved synchronically. It is a single nucleus, not a sequence. The orthography spells this `ii` (see *Orthography Reference* §3.2 for the contrast with hiatus `iyi` and with long /iː/ `iiy`).

**Long:** Bimoraic nuclei in two surface types. **[Settled]**

- *Monophthongal long vowels.* /iː, ɛː, oː, aː, ɨː/. Both morae carry the same vowel quality; the IPA carries `ː`. These arise from intervocalic-consonant elision plus smoothing, and from reanalysis of historical diphthongs. **/iː/ is a phoneme** of the conlang, arising principally from /ɪji/-smoothing (the /ɫ/-glide-becoming pathway, e.g., *Emily* /ˈɛməli/ → /ɛˈmiː/, *rhiiynii* /ɻiːni/ "to need" < *really need*). It is spelled `iiy` orthographically.
- *Diphthongal long vowels.* /iɛ/ is the first attested case: a bimoraic nucleus whose two morae carry different vowel qualities (here /i/ and /ɛ/). The IPA does *not* carry `ː` — the second-quality vowel is what makes the digraph bimoraic. /iɛ/ arises from /i/-fronting of an absorbed schwa: a base vowel /i/ absorbs a following schwa as length, with the schwa raising to /ɛ/ under the influence of the preceding /i/ rather than smoothing into pure length. Attested in *hiie* /hiɛ/, the article-incorporating form of the see-particle (cf. `language_reference.md` §3.7). Spelled `iie` orthographically. Additional diphthongal long-vowel digraphs (e.g., /io/ as `iio`) are predictable by analogy but currently unattested. **[Open: whether other /i/-initial diphthongal long vowels occur]**

**Diphthongs (monomoraic):** /ei, oe, ia/ **[Settled]**

The conlang has two diphthong classes, distinguished by mora count: monomoraic diphthongs above (with /j/ or vocalic glide as the consonantal second element) and bimoraic *diphthongal long vowels* under "Long" (with a vocalic second mora). The contrast `ei` /ei/ (monomoraic) vs. `iie` /iɛ/ (bimoraic) is the cleanest minimal pair for the distinction. See `orthography.md` §3.3–3.4.

**Suprasegmental contrasts on vowels:** see §2.3.

### 2.3 Suprasegmental contrasts on vowels

Vowels contrast in nasalization, breathy voice, and pitch in some environments. All three arose from elided coda consonants (nasals, /h/, weak obstruents) leaving residual features on adjacent vowels.

- **Nasalization** is phonemic. **[Settled]**
- **Breathy voice** is not phonemic — the `VhV` surface pattern is an allophonic realization, not a contrast in the inventory. **[Settled]** Medial /h/ in fused-function-word contexts (*noho*, *hiho*) has the same allophonic status; the proposed phonemic distinction (`VhV` consonantal vs. `VhU` breathy) is not adopted.
- **Pitch accent** is dissociated from stress in placement. Placement is settled — pitch sits on the syllable that carried primary stress in the GA etymon — and is lexical from the speaker's standpoint; contrastiveness is **[Open]**. The full analysis, including the etymologically-determined / not-synchronically-derivable distinction, is in §3.4.

---

## 3. Syllable and metrical structure

### 3.1 Syllable structure and phonotactics

The language permits both substantial vowel clusters (*hoiiǫ* /ˈhoiõ/ "salt" < *sodium*) and substantial consonant clusters (*hoʔnʔnts* /ˈhoʔn̩ʔn̩ts/ "face" < *countenance*; *ritsstw* /ˈritsstw̩/ "Rochester"). The two distributions arise from different processes: vowel clusters from intervocalic consonant elision (soft-six hollowing, §4.4.2), consonant clusters from systematic schwa elision (schwa crush, §4.4.9).

**Onset phonotactics is permissive.** Long onset clusters survive, including sequences violating sonority sequencing in moderate ways. The /st/ → /ts/ shift produced /ts/-onsets that are phonotactically normal in the conlang but unusual cross-linguistically.

**Coda phonotactics is restrictive.** Most coda consonants have either elided outright (total l-loss and need-clipping, §4.4.11), reduced to /ʔ/ (the /t/-path), or assimilated and geminated (the /nd/ → /nː/ path). The surviving codas are sparse.

**Syllabic consonants** (/n, m, s, θ, ʔ, w, j/, possibly /r/) serve as syllable nuclei. They occur predominantly in appendix position (§3.5) but can also occur foot-internally where elision has stranded them.

A **mora (μ)** is the unit of syllable weight: a short vowel is 1μ, a long vowel is 2μ, a syllabic consonant is 1μ. A syllable is **light** (1μ) or **heavy** (2μ) depending on its moraic content. The conlang's stress and foot rules are weight-sensitive.

**The ideophone class is exempt.** The expressive class — ideophones (`ideophones.md`) — is not bound by the phonotactic and metrical constraints above. Ideophones may contain rare or non-phonemes and clusters the core lexicon disallows, and may bear stress on a nucleus the regular rules would never accent — the geminate syllabic /m/ of *rhitmmtm*, where the *t*'s surface as glottal stops. The exemption and its inventory of licenses are described in `ideophones.md` §5; the note here keeps the core phonotactics from being read as exceptionless. **[Settled — the class is exempt; the inventory of licenses Provisional]**

### 3.2 Foot construction

Feet are built **right-to-left** and are **trochaic** by default (left-headed): the leftmost syllable of a two-syllable foot bears prominence within the foot. The **rightmost foot** is the head foot of the prosodic word and bears primary stress.

Feet may be one or two syllables. **Degenerate (single-syllable) feet are licensed** at the right edge regardless of syllable weight. Light-monosyllabic words like *ŕe* /ˈr̥ɛ/ "today" are fully grammatical.

### 3.3 Stress placement

The descriptive rule: **stress falls on the final vocalic position of a word.** Because syllabic consonants count as nuclei, "final vocalic position" may be a syllabic consonant rather than a full vowel.

Three things follow from the right-headed foot construction in §3.2:

1. In a monosyllabic head foot, the head is that single syllable — which is the final vocalic position. Stress lands there.
2. In a disyllabic head foot, the head is the leftmost syllable of the foot by default (trochee) — but the rightmost syllable bears stress, by the right-headed prosodic-word rule. The two interact such that stress effectively lands on the rightmost full vowel.
3. **Quantitative metathesis** — the apparent rightward stress shift in dactyl-shaped words — is not a separate rule. It falls out as a consequence of right-headed foot construction applied to a foot where no rule has reduced the rightmost syllable.

If an unstressed vowel followed the final vowel historically, one of three things happened: it smoothed into the stressed vowel (lengthening), elided (creating clusters), or received the stress instead (becoming the new final vocalic position).

**Stress in adjectival predication.** In the *aų* X *hii* predication pattern (`language_reference.md` §3.3), the closing element *hii* carries the phrase-final prominence, exempting the adjective itself from final-position stress. This is a phrase-level fact, not a lexical exception: the adjective's word-level stress is unchanged; the predicative element simply outranks it in the phrase. **[Provisional]** The analysis of *hii* itself (plausibly < GA *side*, riding the price splinter's /aɪ/ → /i(ː)/ reflex) is **[Open]** at `language_reference.md` §3.3.

### 3.4 Pitch placement

**Pitch falls on the syllable that carried primary stress in the GA etymon.** The placement claim is the basic descriptive fact. **[Settled]**

The analytical framing: pitch is best understood as the **phonetic residue of GA-style prominence** after stress has migrated to the final vocalic position, rather than as an independently assigned prosodic dimension. Speakers do not target pitch as a separate articulatory dimension; they retain GA-style prominence on its inherited syllable (where prominence in English already bundles loudness, length, and F0) and superimpose the conlang's final-stress rule on top. Loudness and length transfer to the final vowel; F0 stays behind on the etymological-stress syllable. The audible "pitch on V₁, stress on V_final" pattern falls out of this redistribution, rather than being assigned by a separate rule.

Pitch and stress are usually on **different** syllables. Where GA stress was initial (most multisyllabic GA etyma), the conlang's stress has migrated to the final position while pitch has stayed where it was. *Emma* /ɛma/ has pitch on /ɛ/, stress on /a/. *Emily* /ɛmiː/ has pitch on /ɛ/, stress on /iː/.

When pitch and stress would land on the same syllable, the result is a single-prominence word. Monosyllables coincide trivially. Some longer forms also coincide where the GA etymon's stress was final or where derivational reductions have placed both prominences on the same vowel — *ŕeut* /r̥eːʔ/ "carrot" coincides because the GA *carrot*'s stress was on the first syllable, which is now the only syllable left.

#### Origin: the diachronic pathway

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

The two senses of "predictable" are different and must not be conflated. "Predictable from the etymon" does not entail "predictable from the surface form." Pitch is **lexical**, in the same sense that lexical-stress systems are lexical. Whether it is also **contrastive** (carries minimal-pair distinctions) is a separate question, treated below and in §5.

#### Why minimal pairs are scarce

The minimal-pair scarcity is **not** evidence that pitch is weak. It is evidence that GA stress is loud — in the information-theoretic sense — and has already eaten most of the territory in which pitch could carry contrast.

GA stress is not just a prominence diacritic. It restructures everything around itself: stressed vowels are full, unstressed vowels reduce to schwa or elide, syllable weight and segment count depend on where prominence fell. By the time GA stress has done its work, two words sharing the same stress pattern have largely the same shape, and two words with different stress patterns have largely different shapes.

The conlang's cascade compounds this. Vowel mergers, consonant mergers, schwa elision, the appendix system — all operate on already-stress-conditioned material. The result is that residual segmental skeletons that could converge on a homophonous form while differing only in pitch almost never exist.

> *Analytical note.* GA stress-shift derivational pairs (*récord*/*recórd*, *présent*/*presént*, *súbject*/*subjéct*) were initially flagged as the candidate workspace for genuine pitch-only minimal pairs, since both members share segments under different prominences. On closer inspection they are not clean candidates: in GA, unstressed vowels reduce to schwa, so vowel quality co-varies with stress and the conlang reflex pairs would differ in more than pitch alone. The open search strategy targets pairs where the GA etyma share segment quality across the stress site; see §5.4.

The reframed picture: pitch's potential workspace was mostly absorbed by the segmental consequences of the prominence pattern it descends from. Low functional load on pitch follows directly from this and is not, on its own, evidence about whether pitch is contrastive, allophonic, or vestigial.

#### Phonetic predictions

Under the residue analysis, V₁ should retain phonetic correlates of GA-style prominence beyond pure F0:

- **Slight length.** V₁ should be marginally longer than a comparable unstressed vowel, because length was part of the inherited prominence package and would not fully transfer to the final.
- **Slight fullness or amplitude.** V₁ should not reduce all the way to schwa-like quality even when stress has clearly moved off it.
- **F0 peak roughly aligned with the syllable nucleus**, not displaced to a syllable margin (which would suggest a contour-tone analysis).

A "true" pitch-accent system fully grammaticalized away from its stress origin would have F0 doing the work alone, with V₁ otherwise indistinguishable from any other unstressed vowel. The conlang should *not* look like that under the residue analysis. Acoustic recordings (pending; see §5.4) are the falsification test.

#### Orthography

Pitch is marked with **acute** on a vowel; stress is marked with **grave** (normally unwritten because predictable, marked in formal/pedagogical text); coincidence is marked with **circumflex** in formal register. The acute-on-consonant devoicing convention is unaffected — pitch and devoicing live on different segment types.

Pitch is marked in all registers because it is lexical, regardless of whether it is analyzed as a feature target or as residue.

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

**Extrametricality** — a related concept that licenses single peripheral constituents to be invisible to foot construction — does some work for the simpler cases (*Jennifer* with one peripheral syllable) but doesn't scale to the multi-nucleus cases. The classical formulation permits one peripheral constituent to be invisible; *countenance*'s up-to-four post-stress nuclei break that. Iterative or persistent extrametricality has precedent (Cairene Arabic, some Berber varieties) but is non-standard. Appendix adjunction is the cleaner analysis.

> *Analytical note.* The earlier label *sesquisyllabic* is retired: sesquisyllabicity names a left-edge presyllable phenomenon in Mainland Southeast Asian languages, and the conlang's pattern inverts every defining property (post-stress rather than pre-stress, trochaic-with-tail rather than iambic, lower-sonority and longer tails). The full retirement record is in the §6 glossary entry *Sesquisyllable* and in `terminology-registry.md`. Analytical sources for appendix adjunction: the prosodic-phonology literature (Selkirk 1986, 1996; Itô & Mester 1992 and later) — cited for completeness, not required reading for using the language.

---

## 4. Diachronic development

### 4.1 Overview

The conlang's surface forms derive from GA etyma by a designed cascade of regular sound changes. The high-level shape:

- **Aggressive schwa elision** in unstressed positions, producing consonant clusters and syllabic consonants where GA had vowel-bearing syllables.
- **Intervocalic consonant elision** for /d, dʒ, n, j, g, v/, producing widespread vowel hiatus and feeding the long-vowel inventory.
- **Debuccalization** of /s/ to /h/ in most positions, and of onset /k/ to /h/ in parallel.
- **Massive consonant mergers**, especially the soft six /d, dʒ, n, j, g, v/ → /r/ (tap), /m/ → /b/ in onset (with /p/ joining only conditionally), /f/ → /θ/, /w/ → /ɻ/ (with /j/ joining only in restricted contexts).
- **Coda reduction**: /t/ → /ʔ/, /d/ → ∅, /l/ along several paths (still under analysis), with coda /ʔ/ stable.
- **Vocalic mergers**: /u, ʊ, ʌ/ → /ɨ/, /ai/ → multiple reflexes (conditioning open, see §5.1), /au/ → /o(ː)/, /ɔr/ → /oe/ (report gliding — supersedes the earlier /or/ → /oː/ statement), /æ, er/ → /eː/.
- **Suprasegmental residue**: nasalization on vowels adjacent to elided /n/, breathy voice from elided /h/ and weak obstruents, pitch retained on the GA-stress vowel even after stress migrates rightward.
- **Final-vowel stress assignment**, with the historical stress vowel keeping its pitch — producing the pitch-stress dissociation.

The cascade is best understood as a feeding pipeline rather than a flat list of rules. The ordering encodes a design preference for vocalic events over consonantal ones: vowel clusters and long vowels are typologically rarer than consonant clusters, and the conlang aims to foreground them.

From v4, every sound change carries a descriptive name (the fin-thin merger, the wandering r, schwa crush, …). The division of labor: **§4.2 owns ordering** (the master stratal table), **§4.4 is the registry** — the canonical, family-organized inventory of named rules with uniform fields — and the legacy rule IDs (E1, M1, S3, …) remain valid aliases throughout this document set.

### 4.2 The cascade in overview

#### Stage 0: the GA surface snapshot

The cascade operates on a **Stage 0 input**: the GA etymon rendered in a fairly *narrow surface* transcription, not broad phonemic form. Several changes phonologize GA allophony, so the allophones must already be present in the input:

- **flapping** — intervocalic /t, d/ → [ɾ], which is the segment soft-six hollowing actually operates on;
- **variable glottaling** — phonologized by coda glottaling;
- **ambisyllabic gemination** — phonologized by pass-out gemination (the labial parallel predicted, §4.4.6);
- **/æ/-tensing** — feeding the stand-out vowel;
- **dark [ɫ]** — feeding the really glide;
- **r-colored vowels** — feeding the /er, or/ rows of the trap-square and mouth-north mergers.

Stage 0 is input normalization, not a conlang rule; an error here propagates cleanly through every later stratum. When deriving new forms, render and check the GA surface transcription before applying any rule.

#### The four processes

Four processes apply in feeding order:

1. **Consonant elision** (intervocalic and coda). Creates vowel hiatus and feeds vowel resolution. The wandering r (M1) also fires here as an alternative way to vacate the intervocalic position.
2. **Vowel resolution.** Smoothing of hiatus into long vowels (when conditions are met), or retention of hiatus.
3. **Vowel elision.** Applies to inputs that survived process 1 unchanged. Creates consonant clusters, often with syllabic-consonant promotion.
4. **Stress and pitch placement.** Stress is assigned to the now-final vocalic position (final landing). Pitch lands on the syllable that historically carried GA primary stress (pitch stranding).

The crucial ordering claim is that **process 1 bleeds process 3** — equivalently, Stratum 2 bleeds Stratum 4 at the same locus: once an intervocalic consonant has elided, the vowels it separated are no longer in an environment for vowel-elision. A word is either a "vowel-event" word (long vowel or hiatus) or a "consonant-event" word (cluster, syllabic consonant), but not both at the same locus. **[Settled]**

#### Master ordering table

| Stratum | Label | What happens | Principal rules | Ordering status |
|---|---|---|---|---|
| 0 | GA surface snapshot | Etymon rendered in narrow GA surface transcription | (input normalization — not conlang rules) | — |
| 1 | Segment mappings | Context-free(ish) consonantal and vocalic mergers | rough-breathing family; soft-six tapping; the labial funnel; fin-thin merger; glide hardening; the Rochester flip; stand-out leveling; the really glide; pass-out and apply gemination; vocalic mergers (goose-foot-strut, the price splinter, mouth-north, trap-square + the stand-out vowel, choice smoothing) | Consonantal mappings precede Stratum 2 (the worked derivations apply them first). Vocalic mergers behave **persistently** — they can apply to derived environments (e.g. *carrot*'s smoothed /æ+ə/ → /eː/) — and their precise ordering against Strata 2–3 is **[Open]** (the *idea* and *ladder* probes, §4.6). |
| 2 | Vacating the middle | The intervocalic position is emptied by elision or metathesis | soft-six hollowing (E1); the wandering r (M1); today coalescence (C-Coal). Riders: nasal ghosting (S1), breath ghosting (S2) | Committed: hollowing bleeds schwa crush at the same locus; the wandering r conditionally bleeds schwa crush; both feed smoothing. |
| 3 | Vowel resolution | Hiatus resolves or is retained | smoothing; schwa swallowing (E4); hiatus retention | Committed: smoothing bleeds the Emma landing. |
| 4 | Crush and promotion | Surviving unstressed schwa elides; stranded consonants promote | schwa crush (E3); syllabic promotion → appendix formation (§3.5) | Committed: crush feeds promotion, which feeds appendix adjunction. Left-to-right vs. global application in dactyls is **[Open]** (the *Penelope* probe, §4.6). |
| 5 | The coda purge | Coda consonants weaken, delete, or anchor | coda glottaling (E2a); need-clipping (E2b); total l-loss (E2c); coda k-loss + labial rescue; the glottal anchor + the out-drop (E2d) | Follows Stratum 4 in the CVCVC cascade (§4.3). |
| 6 | Residual vowel resolution | Leftover weak vowels and tails resolve | the Emma landing, the apply onset (E5); final-glide settling; the -er tail | — |
| 7 | Prosody | Feet built; prominences assigned | foot construction (§3.2); final landing (stress, §3.3); pitch stranding (S3, §3.4) | Pitch stranding is independent of the segmental cascade. |
| 8 | Late rules | Word-level cleanup and surface allophony | alveolar-wins (R-Assim); cute-and-quick fortition | Alveolar-wins fires last among segmental rules; fortition is surface allophony. |

### 4.3 The cascade in detail

Notation: for a CVCVC input, **C₀ V₁ C₁ V₂ C₂**. For a dactyl-shaped CVCVCVC input, **C₀ V₁ C₁ V₂ C₂ V₃ C₃**. Cs may be clusters; Vs include diphthongs.

#### Cascade for CVCVC

| Step | Rule | Condition | Output |
|---|---|---|---|
| 1a | soft-six hollowing (E1): elide C₁ | C₁ ∈ {ɾ, dʒ, n, j, g, v} | C₀ V₁ V₂ C₂ → step 2 |
| 1b | the wandering r (M1): relocate C₁ if /ɻ/ | C₁ = /ɻ/ AND C₀ ∈ {/h/, ∅} | rhotic moves to onset; /h/ becomes devoicing feature → /r̥/. Hiatus created. → step 2 |
| 1c | the wandering r blocked / no rule fires | C₁ = /ɻ/ but C₀ is something else; OR C₁ not in any set | unchanged → step 4 |
| 2 | smoothing | (a) one participant is /ə/, OR (b) participants are articulatorily close | C₀ V₁ː C₂ |
| 2 | hiatus retention | neither smoothing condition met | hiatus preserved; stress placed on final V (see §3.3) |
| 3 | stranded schwa (the Emma landing) | V₂ = /ə/ in resulting open syllable | strengthen ə→a |
| 4 | schwa crush (E3): elide V₂ | V₂ ∈ elision set, intervocalic position not vacated | C₀ V₁ C₁ C₂ → step 5 |
| 4 | schwa crush: skip | otherwise | → step 6 |
| 5 | syllabic promotion | C₁ or C₂ ∈ syllabic-eligible | C₀ V₁ C₁ C̩₂ (foot + appendix) |
| 6 | the coda purge (E2a–d): coda treatment | C₂ subject to coda rules | varies — see §4.4.11 |
| 7 | final-V resolution (the Emma landing) | V₂ ∈ {e, a, ə} | strengthen ə→a |
| 7 | final-V resolution (final-glide settling) | V₂ ∈ {i, o} | reduce to syllabic /j̩, w̩/ |
| 8 | alveolar-wins (R-Assim) | word contains both /ɻ/ and /ɾ/ | /ɻ/ → /ɾ/ throughout |

**Note on step 2.** Smoothing is licensed by **either** of two conditions: (a) at least one of the vowels in hiatus is /ə/ (which is absorbed into its neighbor), or (b) the two vowels are articulatorily close. When neither is met — i.e., two or more full, articulatorily distant vowels are in hiatus — the hiatus is retained and stress falls on the final vowel. This is why /eio/ in *radio* stays as three syllables. **[Settled]**

#### Cascade for dactyl (CVCVCVC)

Dactyl-shaped words enter the same cascade and resolve to CVCVC or shorter shapes via hollowing, schwa crush, or coda reduction. Where elision fully fails, the word retains its three-vowel shape and stress falls on V₃ — by right-headed foot construction, not by a separate metathesis rule (see §3.3).

#### Five generalizations the cascade encodes

1. **Vacate the intervocalic position** where licensed — by elision (soft-six hollowing) or by metathesis (the wandering r). Either creates hiatus.
2. **Smooth** vowels in hiatus when (a) one is schwa, or (b) they are articulatorily close.
3. **Promote** stranded consonants to syllabic nuclei where sonority licenses; this produces appendix material when the result is post-stress.
4. **Strengthen** final stranded schwa (the Emma landing).
5. **Place stress** on the rightmost full vocalic position (final landing); **place pitch** on the syllable that carried GA primary stress (pitch stranding).

#### Ordering commitments

- **Soft-six hollowing always bleeds schwa crush at the same locus.** If C₁ has elided, V₂ is no longer in the right environment for vowel elision.
- **The wandering r conditionally bleeds schwa crush.** When it fires, the intervocalic position is vacated and crush is bled. When it is blocked, crush is free to fire.
- **Hollowing and the wandering r (when firing) both feed smoothing.**
- **Smoothing bleeds the Emma landing.** A schwa that has smoothed into the preceding vowel is no longer available to be strengthened to /a/.
- **Schwa crush feeds syllabic promotion**, which feeds appendix adjunction at the prosodic-word level.
- **Pass-out gemination outranks s-breathing and the Rochester flip** in the pre-stress syllable-boundary environment.
- **Labial rescue blocks coda k-loss.**
- **All vowel-creating and vowel-removing rules feed final landing** (stress placement).
- **Pitch stranding is independent of the segmental cascade** — it lands on the historical-GA-stress vowel regardless of what the segmental rules have done elsewhere.
- **Alveolar-wins fires last.**

#### Open orderings

- **Vocalic mergers vs. Stratum 2.** Does the price splinter apply before or after soft-six hollowing creates new hiatus? (The *idea* probe, §4.6.) **[Open]**
- **Smoothing quality coercion.** When smoothing would produce a long vowel outside the inventory, does it fail (retaining hiatus) or coerce to the nearest member? (The *ladder* probe, §4.6.) **[Open]**
- **Directionality in dactyls.** Does the cascade run left-to-right, or apply globally and re-evaluate? (The *Penelope* probe, §4.6.) **[Open]**
- **The coffee shield.** Junction welding counterbleeds debuccalization at compound junctions; attested but not yet a registered ordering within the cascade (§4.4.13, §5.5). **[Open]**

### 4.4 Sound-change registry

The canonical inventory of sound changes, organized by **family** — a named group of changes sharing a mechanism, a drift, or a segment set. Each rule carries a descriptive name in the tradition of English historical phonology (exemplar names like the fin-thin merger; mechanism names like smoothing); the names are the primary reference keys, and the legacy IDs (E1–E5, M1, C-Coal, R-Assim, S1–S3) remain valid aliases. Family membership is organizational; ordering lives in each entry's stratum field and in the §4.2 master table. These changes are descriptive of the historical processes; some are productive synchronic rules, others are residue — but for deriving new forms from GA etyma, the whole cascade applies.

**Reading a registry entry.** Each rule opens with a headword line — **name** · family · legacy alias (if any) · stratum · status — followed by labeled fields: **Statement** (the formal change), **Environment** (conditions and blocks), **Ordering** (feeds/bleeds/outranks, where committed), **Attestations**, and **Notes** (exceptions, surfaced flags). Empty fields are omitted.

#### 4.4.1 The rough-breathing family

*Family note.* GA obstruents that lose their mouth posture and surface as bare /h/ — named for the Greek *spiritus asper* ("rough breathing"), whose *s* > *h* history this family replays.

**s-breathing** · rough breathing · Stratum 1 · **[Settled]**
- **Statement:** /s/ → /h/ in most positions.
- **Environment:** blocked by the cluster shield; outranked by pass-out gemination at a syllable boundary preceding stress.
- **Attestations:** *hoiiǫ* (< *sodium*); passim.

**k-breathing** · rough breathing · Stratum 1 · **[Settled]**
- **Statement:** onset /k/ → /h/.
- **Environment:** surface [k] before glides is reanalyzed as fortified /h/ (cute-and-quick fortition, below); coda /k/ is handled by coda k-loss and labial rescue (§4.4.11).
- **Attestations:** *hoʔnʔnts* (< *countenance*), *ŕeut* (< *carrot*).

**the cluster shield** · rough breathing · Stratum 1 · **[Settled]**
- **Statement:** debuccalization is blocked when /s/ is the first element of an onset cluster (e.g., /sp/, /sk/); /s/ surfaces.
- **Attestations:** *spyi*.

**cute-and-quick fortition** · rough breathing · Stratum 8 (surface allophony) · **[Provisional]**
- **Statement:** /h/ fortifies to [k] before a glide; surface [kj, kw] are analyzed as allophonic /hj, hw/ — the exemplar environments are the onsets of *cute* and *quick*.
- **Notes:** this is the analytical move by which /k/ is excluded from the phoneme inventory (§2.1). Whether the analysis holds is listed in §5.2.

#### 4.4.2 The soft six

*Family note.* /d, dʒ, n, j, g, v/ — six segments that lenite as a class: they merge into the tap in onset and delete intervocalically. /d/ usually enters the cascade as its GA surface flap [ɾ] (Stage 0). Membership caveats: /n/ is the conditional member (it can elide with nasal ghosting instead of tapping); /v/'s membership is conditioned (the proposed front-vowel/back-vowel split with /b/, §5.1); and /j/ is claimed by both this family and glide hardening (§4.4.4) — the division of labor is flagged in §5.1 (surfaced in v4).

**soft-six tapping** · the soft six · Stratum 1 · **[Settled in core]**
- **Statement:** /d, dʒ, n, j, g, v/ → /r/ (tap) in onset.
- **Environment:** /n/ conditional on environment (can also elide with nasal coloring); /v/ per the §5.1 conditioning question; /j/ per the §5.1 allocation question.
- **Attestations:** /ˈrɛ̃ːθw̩/ (< *Jennifer*, /dʒ/); passim.

**soft-six hollowing** · the soft six · legacy **E1** · Stratum 2 · **[Settled]**
- **Statement:** /ɾ, dʒ, n, j, g, v/ delete between vowels. (/ɾ/ here is the alveolar tap — the GA intervocalic realization of /t, d/; the rule operates on the Stage 0 surface segment.)
- **Ordering:** bleeds schwa crush at the same locus; feeds smoothing and vowel resolution. Fed by no rule.
- **Rider:** /n/-hollowing triggers nasal ghosting (S1, §4.4.12).
- **Attestations:** *hoiiǫ* (< *sodium*), /bɛi/ (< *Betty*), *toutw* (< *to total to*).

#### 4.4.3 The whispered r

*Family note.* Three roads to the devoiced rhotic /r̥/, all sharing one mechanism: an obstruent collapses into a voicelessness feature on the rhotic. More broadly, this section houses the **rhotic-instability drift**: rhotics in this language migrate (the wandering r), coalesce (today coalescence), assimilate (alveolar-wins), dissimilate (tap–rhotic dissimilation), and resurface across morpheme boundaries (linking r) — the retroflex's loose, vowel-spanning articulation makes it the most mobile segment in the system. Alveolar-wins, the rhotic system's closing rule, is housed here for convenience.

**kr-whispering** · the whispered r · Stratum 1 · **[Settled]**
- **Statement:** /kr/ → /r̥/ — the /k/ devoices the rhotic and merges in.

**the wandering r** · the whispered r · legacy **M1** · Stratum 2 · **[Settled in core, Open in edges]**
- **Statement:** intervocalic /ɻ/ relocates to onset position. Motivated by GA r-coloring: the retroflex's articulation already extends across adjacent vowels, making it phonologically "loose" and relocatable in a way other consonants are not.
- **Environment:** requires an onset /h/ or an empty onset. When the onset is /h/: the rhotic lands in onset, the /h/ ceases to function as an independent segment and is reanalyzed as a devoicing feature on the rhotic → /r̥/. When the onset is empty: the rhotic lands in onset as plain /ɻ/. When blocked (any other onset): /ɻ/ stays in place and surfaces as /ɻ/ — it does not elide and does not convert to /ɾ/. Coda /ɻ/ is outside this rule's domain — it participates in the historical /er/ → /eː/ merger (trap-square) and /ɔr/ → /oe/ (report gliding) instead.
- **Ordering:** conditionally bleeds schwa crush; feeds smoothing when it fires.
- **Attestations:** *ŕeut* (< *carrot*) canonical; blocked in /ˈbeɻn̩/ (< *baron*).
- **Notes:** what counts as "intervocalic" across cluster boundaries, and behavior in words with multiple potential sites, are **[Open]** (§5.2).

**today coalescence** · the whispered r · legacy **C-Coal** · Stratum 2 · **[Settled]**
- **Statement:** /h/ + /ɾ/ (or /ɻ/) adjacent in onset → /r̥/ — the same /h/-as-devoicing mechanism as the wandering r, arrived at by direct contact rather than migration.
- **Attestations:** *ŕe* (< colloquial *today* with rapid-speech reduction producing /h/ + tap onset).

**tap–rhotic dissimilation** · rhotic instability · Stratum 2 · **[Provisional]**
- **Statement:** /ɻ/ elides when the onset of the preceding syllable is a tap (plain or devoiced).
- **Environment:** distinct from the wandering r: there the rhotic *becomes* the (devoiced) tap by migration; here a rhotic *following* an established tap onset deletes. No migration occurs.
- **Attestations:** *ŕeush* (< *cherish*: /tʃ/ → /ɾ̥/ by cherish tapping, then medial /r/ elides).
- **Notes:** single attestation; environment stated narrowly. Collect *parish/perish/nourish*-class etyma.

**linking r** · rhotic instability · morphophonological · **[Settled]**
- **Statement:** a stem-final GA rhotic that was vocalized or absorbed into the appendix word-finally resurfaces, intervocalically, as ⟨rr⟩ before a vowel-initial suffix.
- **Attestations:** *bemmw* (< *remember*) ~ suffixed *bemmorret*, *bemmorreųt*; and across the ‑er class under PROG — *bekw* → *bekrrıĩ*, *rhinnw* → *rhinzrrıĩ* (B12, June 2026).
- **Notes:** the standard term from English phonology, used in its standard sense. This is the **rhotic special case of the fossil resurrection** (§4.4.14): morphology-sensitive, firing at suffixation, full statement shared with `verbal-system.md` §4.2.2. The surface value of ⟨rr⟩ is /ɻ/ (intervocalic) per `orthography.md` §2.6, which lists linking r explicitly; alveolar-wins (above) maps it to /ɾ/ where a tap co-occurs in the word.

**alveolar-wins** · rhotic closer · legacy **R-Assim** · Stratum 8 · **[Settled]**
- **Statement:** if a word contains both an alveolar /ɾ/ and a retroflex /ɻ/, the retroflex assimilates to alveolar.
- **Ordering:** fires after the wandering r and today coalescence; last among segmental rules.
- **Notes:** establishes the alveolar tap as the unmarked rhotic of the conlang. (Mechanically not a whispered-r member; housed in this section as the rhotic system's closing rule.)

#### 4.4.4 Glide hardening

*Family note.* A drift toward the GA glides merging with the glide-like retroflex rhotic — complete for /w/, partial and context-dependent for /j/. The candidate /ɫ/ → /ɻ/ vocalization path (§5.1) would make dark-l a third, still more reluctant member of the same drift.

**w-hardening** · glide hardening · Stratum 1 · **[Settled]**
- **Statement:** /w/ → /ɻ/ (*wet* → *ret*-type onsets).
- **Ordering:** feeds alveolar-wins.

**the reluctant yod** · glide hardening · Stratum 1 · **[Open — data gathering]**
- **Statement:** /j/ → /ɻ/ in restricted contexts only; the conditioning is not yet committed.
- **Notes:** *yet*'s /j/ does not shift — the standing counterexample that gives the rule its name. /j/ is also a soft-six member (tapping in onset, hollowing intervocalically); how the lexicon divides /j/ between the two paths is flagged in §5.1 (surfaced in v4).

**dark-l vocalization** · glide hardening · Stratum 1 · **[Settled in core; /j/ branch Provisional]**
- **Statement:** GA dark /ɫ/ vocalizes, with two conditioned outputs — → /j/ adjacent to a front vowel; → /ɻ/ elsewhere (and thence to /ɾ/ by alveolar-wins). The rhotic branch makes dark-l the third, most reluctant member of the glide-hardening drift.
- **Environment:** the /j/ output is conditioned by adjacency to a front vowel (the *really* glide); the rhotic output is the elsewhere case.
- **Ordering:** the rhotic branch feeds alveolar-wins (§4.4.3).
- **Attestations:** /l/-initial GA words consistently yield /r/-initial headwords (the /ɾ/ branch); the *really* glide /iː/ of *rhiiynii* (< *really need*) is the /j/ branch in a high-front-vowel environment.
- **Notes:** the consistently /r/-initial output across the lexicon settles the rhotic branch; the front-vowel conditioning of the /j/ branch is committed here (user decision, June 2026) but wants direct attestation of a /j/-surfacing form. Closes the §5.1 dark-l data-gathering item.

#### 4.4.5 The labial funnel

*Family note.* GA labials funnel toward /b/ in onset — unconditionally for /m/, conditionally and irregularly for /p/. Earlier versions stated a single unconditional /m, p/ → /b/ merger alongside the conditioned /p/ rule without reconciling them; v4 splits the two and supersedes the unconditional /p/ claim.

**bat-mat merger** · the labial funnel · Stratum 1 · **[Settled in core]**
- **Statement:** /m/ → /b/ in onset, unconditional — *bat* and *mat* merge.
- **Notes:** the environment is stated as "onset," but *Emma* /ɛma/ retains its medial /m/ — suggesting the merger targets true onsets and exempts GA-ambisyllabic consonants. The environment needs pinning; flagged in §5.1 (surfaced in v4).

**pass-out voicing** · the labial funnel · Stratum 1 · **[Provisional]**
- **Statement:** singleton onset /p/ → /b/ (a) before /ɛ, ɛː/ in any position, and (b) in **word-medial** onsets before any vowel. Word-initial /p/ before other vowels resists; blocked in consonant clusters and geminates.
- **Attestations:** *beussou* (< *pass out*; environment a, word-initial before /ɛː/), *rhiboet* (< *report*; environment b, medial before /o/). Resisting word-initial forms: *pot*, *pikkp*, *piquô*, *piiquóä*.
- **Notes:** restated twice in v4.1 — first widened to all vowels on the *rhiboet* attestation, then corrected the same day when the dictionary's word-initial /p/ forms surfaced as counterexamples to the widening. The two-environment statement fits all known data. /p/ remains **not** a general member of the labial funnel; the inventory's singleton-/p/ gap (§2.1) now holds only word-medially. Residual question in §5.1.

**prep-breaking** · the labial funnel · Stratum 1 · **[Settled in core; cross-cluster generalization Open]**
- **Statement:** a word-initial GA /pr/ onset cluster resolves to **/bɑˈɾ̥/** ⟨baŕ⟩: the cluster breaks with an **epenthetic /ɑ/** (creating a new first syllable), the /p/ **voices to /b/**, and the rhotic surfaces as a **devoiced tap /ɾ̥/** ⟨ŕ⟩ — the voicelessness fossilized from GA's voiceless-cluster realization [pɹ̥]. Stress stays on the original (now second) syllable.
- **Attestations:** *baŕep* (< *prep*), *baŕaumss* (< *promise*), *baŕâuss* (< *process*) (B12, June 2026).
- **Notes:** resolves the two ad-hoc flags formerly carried in the *promise*/*process* entries (`[New rule needed: stop–rhotic epenthesis]`, `[Open: cluster epenthesis + /r/-devoicing]`) and **supersedes their divergent derivations** — *process* had used /ɻ/ ⟨rr⟩ with epenthetic /ɑ/, *promise* a devoiced /ɾ̥/ with epenthetic /ɛ/; the rule standardizes both on /ɑ/ + /ɾ̥/. The epenthetic vowel is the language's **default low-back /ɑ/** (consistent with the de-phonemicized schwa's low-back merger — the low-back asymmetry, overview §). Contrast **kr-whispering** (§4.4.3), where /kr/ instead **loses** the stop (/kr/ → /ɾ̥/): the labial cluster keeps its stop (as /b/), the velar does not. This also closes the word-initial /p/→/b/ that pass-out voicing leaves open for clusters.
- **The voiced sibling — /br/.** The cluster-breaking epenthesis is **not** /pr/-specific: GA /br/ breaks the same way (*bridge* → *baurrits* /bɑˈɻɪts/), but because the stop is already voiced the rhotic stays **voiced /ɻ/** ⟨rr⟩ rather than devoicing. So the analysis factors cleanly: the **/ɑ/-epenthesis is general** to a word-initial labial-stop + rhotic onset; the **rhotic-devoicing (→ /ɾ̥/ ⟨ŕ⟩) is conditioned** by the voicelessness of the /pr/ source. *(Named prep-breaking for its showcase /pr/ set; covers the /br/ case as the voiced reflex.)*
- **Ordering:** epenthesis feeds the voicing and the rhotic devoicing.
- **Open:** further generalization — /tr, gr/ untested; /dr/ shows a *different* (palatalizing) reflex (*wond'ring* → *rhinzrrıĩ*, `verbal-system.md` §4.2.2).

#### 4.4.6 Ambisyllabic gemination

*Family note.* GA's slight gemination of ambisyllabic consonants at stressed-syllable boundaries phonologizes into true geminates. Stage 0 must mark ambisyllabicity for these to fire. Cross-reference: stand-out leveling (§4.4.7) produces geminate /nː/ by a different mechanism (assimilation) and is registered separately.

**pass-out gemination** · ambisyllabic gemination · Stratum 1 · **[Settled]**
- **Statement:** /s/ (and /st/) → /sː/ at a syllable boundary preceding stress.
- **Ordering:** outranks s-breathing and the Rochester flip in this environment.
- **Attestations:** *beussou* (< *pass out*, /s/), *rhiiysseunnou* (< *really stand out*, /st/).

**labial gemination** · ambisyllabic gemination · Stratum 1 · **[Provisional — currently unattested]**
- **Statement:** ambisyllabic /pp/ → /pː/ — the labial parallel to pass-out gemination.
- **Attestations:** none at present. Its former sole attestation, *epplii* (< *to apply*), was **reanalyzed 2026-06-23** as having a plain /pl/ onset cluster (GA *apply* /əˈplaɪ/, single onset /p/) — no ambisyllabic geminate — and respelled *eplii*. The rule is retained as the predicted labial member of the ambisyllabic-gemination family (and underwrites the systematic `pp` = /pː/ grapheme, `orthography.md` §2.4), pending a genuine attestation. *(Was named "apply gemination" through v4.4.)*

#### 4.4.7 Other consonantal changes

**fin-thin merger** · singleton · Stratum 1 · **[Settled]**
- **Statement:** /f/ → /θ/ — merger into the dental fricative; *fin* and *thin* merge.
- **Attestations:** /ˈrɛ̃ːθw̩/ (< *Jennifer*).

**the Rochester flip** · singleton · Stratum 1 · **[Settled]**
- **Statement:** /st/ → /ts/, the new affricate taking the synchronic place of /s/ in clusters.
- **Environment:** outranked by pass-out gemination at a pre-stress syllable boundary (where /st/ → /sː/ instead).
- **Attestations:** *ritsstw* (< *Rochester*), *hoʔnʔnts* (< *countenance*).
- **Notes:** GA /tʃ/'s parallel route into /ts/ is now a full entry — see **ch-funnelling**, immediately below, which forks with **cherish tapping** on stress.

**cherish tapping** · the affricate fork · Stratum 1 · **[Provisional]**
- **Statement:** /tʃ/ → /ɾ̥/ (the voiceless tap) in the onset of a stressed syllable.
- **Environment:** forks with ch-funnelling on stress, not vowel quality: *Rochester*'s unstressed /tʃ/ precedes a front vowel yet funnels to /ts/, falsifying front-vowel conditioning; the stress condition survives all four attestations.
- **Attestations:** *ŕequoþw* (< *check off*), *ŕeush* (< *cherish*).
- **Notes:** makes /tʃ/ the voiceless mirror of soft-six /dʒ/-tapping; the output joins the existing /ɾ̥/ from the whispered-r roads. Feeds tap–rhotic dissimilation (§4.4.3) in *ŕeush*.

**ch-funnelling** · the affricate fork · Stratum 1 · **[Provisional]**
- **Statement:** /tʃ/ → /ts/ outside stressed-syllable onsets — the funnel into the native affricate.
- **Attestations:** *ritsstw* (< *Rochester*), *hitsn* (< *kitchen*).
- **Notes:** promoted in v4.1 from the v4 sub-statement under the Rochester flip, on the *hitsn* attestation. *Family note (the affricate fork):* the two entries jointly exhaust GA /tʃ/ — stressed onsets tap, everything else funnels.

**stand-out leveling** · singleton · Stratum 1 · **[Settled]**
- **Statement:** coda /nd/ → /nː/ — regressive assimilation (/d/ → /n/), then geminate.
- **Attestations:** *rhiiysseunnou* (< *really stand out*).

**the really glide** · singleton · Stratum 1 · **[Settled]**
- **Statement:** dark [ɫ] → /j/ between high front vowels (ell-yodding); feeds smoothing of /ɪji/ → /iː/.
- **Attestations:** *rhiiynii*, *rhiiysseunnou* (the *rhiiy-* prefix < *really*); /ɛmiː/ (< *Emily*).
- **Notes:** the relationship to the candidate general /ɫ/-vocalization path (§5.1) is unresolved — possibly one rule with environment-dependent outputs.

**the -er tail** · singleton · Stratum 6 · **[Provisional — formalized in v4 from derivation practice]**
- **Statement:** word-final GA /ɚ/ (orthographic *-er*) → syllabic /w̩/ in appendix position.
- **Attestations:** /ˈrɛ̃ːθw̩/ (< *Jennifer*), *ritsstw* (< *Rochester*).
- **Notes:** consistently used in the worked derivations but never stated as a rule before v4. The choice of /w̩/ (rather than a syllabic rhotic) interacts with the open "is /r/ syllabic?" question (§5.3).

**though-elision** · singleton · Stratum 1 · **[Settled]** *(user decision, 2026-06-12)*
- **Statement:** /ð/ → ∅ in all positions.
- **Attestations:** *o* (< *though*, in all contexts including standalone); *notto* /noʔo/ (< *note though*: coda glottaling supplies /ʔ/, /ð/ elides — the surface form is fully regular); the merged article *o* (GA *the* /ðə/ loses /ð/, falls together with *a* as schwa, which strengthens to /o/ — see the §5.1 rounding item).
- **Ordering:** feeds the *a/the* article merger; counterfed by the dishes clip (below), whose early fusion removes the recognitional *the* from this rule's reach.
- **Notes:** with fin-thin pulling /f/ *into* /θ/ and this rule deleting /ð/ outright, the dental fricatives develop asymmetrically — the voiceless one gains members while its voiced partner vanishes from the system.

**the dishes clip** · singleton · Stratum 1 · **[Provisional]**
- **Statement:** the recognitional *the* (`verbal-system.md` §7; `language_reference.md` §3.2.1) procliticizes onto its nominal, loses its schwa, and the stranded /ð/ devoices against a following obstruent → /θ/ ⟨þ⟩. Before an etymological vowel, the GA prevocalic allomorph /ði/ surfaces as /i/ ⟨y⟩ instead — the fricative drops, the vowel survives.
- **Ordering:** fires before (and so escapes) though-elision: early fusion protects the segment, the same protective logic as the coffee shield (§5.5). Derived /θ/ is not re-fed to fin-thin (which is a /f/ → /θ/ merger; no conflict arises).
- **Attestations:** *þ rishś* "the dishes."
- **Notes:** the recognitional half of the *the*-doublet; the referential half goes through though-elision to merged *o* (`verbal-system.md` §7.3 Origin).

#### 4.4.8 Vocalic mergers

**goose-foot-strut merger** · vocalic · Stratum 1 · **[Settled]**
- **Statement:** /u, ʊ, ʌ/ → /ɨ/ (possibly further to /ɪ/; surface [ɨ] is allophonic to /ɪ/, §2.2).
- **Subcase — goose fronting (long):** the long pathway /u/ → /ɨː/.

**the price splinter** · vocalic · Stratum 1 · **[Open — data gathering]**
- **Statement:** /ai/ → /eː/ ~ /i/ ~ /ɛ/ at minimum; conditioning undetermined, possibly including free variation and lexically-specific outcomes.
- **Attestations:** *eplii* (short-/i/ reflex).
- **Notes:** the most analytically open question in the vocalic system; see §5.1. Its ordering against soft-six hollowing (which creates new hiatus) is also open (the *idea* probe, §4.6).

**mouth-north merger** · vocalic · Stratum 1 · **[Settled — NORTH half superseded v4.1]**
- **Statement:** /au/ → /o(ː)/.
- **Attestations:** *beussou*, *toutw*, *hoʔnʔnts* (all MOUTH-set).
- **Notes:** the v4 statement included /or/ → /oː/; that half is superseded by **report gliding** (below) by user decision (2026-06-12) — uniform /ɔr/ → /oe/, no split. All v4 attestations of this entry are MOUTH-set, so no derived form changes. The entry name retains "north" as history.

**report gliding** · vocalic · Stratum 1 · **[Settled]** *(user decision, 2026-06-12)*
- **Statement:** /ɔr/ → /oe/ — coda de-rhotacization yields the front-gliding diphthong, in all environments.
- **Ordering:** supersedes and overrides the former /or/ → /oː/ statement of the mouth-north merger; an audit of any entries derived under the old statement is flagged in §5.2.
- **Attestations:** *rhiboet* (< *report*).
- **Notes:** identifies a regular source for the /oe/ diphthong (§2.2), previously inventory-listed without a feeding rule. Bears on the ⟨œ⟩/⟨oë⟩ grapheme decision (orthography session).

**trap-square merger** · vocalic · Stratum 1 · **[Settled]**
- **Statement:** /æ, er/ → /eː/.
- **Environment:** persistent — applies to derived /æ/-nuclei, e.g. *carrot*'s smoothed /æ+ə/ → /eː/.
- **Attestations:** *ŕeut* (< *carrot*), /beːn/ (< *barn*).

**the stand-out vowel** · vocalic, split from trap-square · Stratum 1 · **[Settled in core]**
- **Statement:** tensed /æ/ before a nasal → /ɛː/ (long), via the GA-tense-/æ/-with-preserved-duration pathway. Stage 0 must mark æ-tensing.
- **Attestations:** *rhiiysseunnou* (< *stand*).
- **Notes:** *beussou* (< *pass*) shows /æ/ → /ɛː/ before /sː/, outside the stated nasal environment — the operative environment may be the broader GA tensing set (voiceless fricatives as well as nasals). Flagged in §5.1 (surfaced in v4). Both diachronic feeds of long /ɛː/ (this rule and smoothed schwa) share the orthographic digraph `eu`; the orthography unifies the two under one grapheme.

**choice smoothing** · vocalic · Stratum 1 · **[Settled]**
- **Statement:** /ɔɪ/ → /oe/.
- **Attestations:** *boë*, *boëś*, *noë*. *(Respelled per orthography v3.1: `œ` → `oë`.)*

#### 4.4.9 The three fates of schwa

*Family note.* GA's pervasive schwa never survives as schwa — it is swallowed, crushed, or strengthened (§1.2). The three fates are distinct rules with distinct ordering positions.

**schwa swallowing** · schwa fate · legacy **E4** · Stratum 3 · **[Settled]**
- **Statement:** schwa adjacent to another vowel is absorbed into it by smoothing rather than elided.

**schwa crush** · schwa fate · legacy **E3** · Stratum 4 · **[Settled]**
- **Statement:** unstressed schwa elides when its locus has not been vacated by a Stratum 2 rule; feeds cluster formation and syllabic promotion.
- **Ordering:** bled by soft-six hollowing and (conditionally) the wandering r at the same locus.
- **Attestations:** *hoʔnʔnts* (< *countenance*, massive crush), /ˈbeɻn̩/ (< *baron*).

**schwa strengthening** · schwa fate · legacy **E5** · Stratum 6 · **[Settled]** — two named subcases:
- **the Emma landing:** final stranded /ə/ in an open syllable → /a/. Attestation: /ɛma/ (< *Emma*).
- **the apply onset:** initial unstressed /ə/ that survives to the final stage → /ɛ/. Attestation: *eplii* (< *to apply*).
- **Ordering:** bled by smoothing — a swallowed schwa cannot strengthen.

#### 4.4.10 Vowel resolution and residues
**squeaky prothesis** · vowel resolution · Stratum 1 · **[Provisional]**
- **Statement:** a prothetic /o/ appears before an /s/+stop onset.
- **Environment:** attested before triconsonantal /skw-/ (*osquihii*) and biconsonantal /sp-/ (*ospii*, *ospokwþ*); but the /spj-/ of *spyi* does **not** trigger it, and glideless extreme forms tolerate clusterhood outright (*skwkw*). The conditioning is therefore not cleanly segmental — possibly lexical or frequency-sensitive.
- **Attestations:** *osquihii* (< *squeaky*), *ospii* (< *speak*), *ospokwþ* (< *speak* + *with*).
- **Notes:** the prothetic vowel's quality (/o/, not /ɛ/ or /ə/) may connect to the §5.1 rounding item. The *ospii*-triggers / *spyi*-doesn't split is the open conditioning question.


**smoothing** · vowel resolution · Stratum 3 · **[Settled]**
- **Statement:** vowels in hiatus merge into a long vowel when (a) one participant is /ə/, or (b) the participants are articulatorily close.
- **Environment:** when neither condition holds, hiatus is retained and final landing places stress on the final vowel (/reio/ < *radio*).
- **Ordering:** fed by soft-six hollowing and the wandering r; bleeds the Emma landing.
- **Notes:** behavior when the output quality lies outside the long-vowel inventory is **[Open]** (the *ladder* probe, §4.6).

**syllabic promotion** · vowel resolution · Stratum 4 · **[Provisional in membership]**
- **Statement:** a consonant stranded by schwa crush promotes to a syllabic nucleus where its segment type licenses it (/n, m, s, θ, ʔ, w, j/, possibly /r/); post-stress promotions adjoin as appendix material (§3.5).
- **Ordering:** fed by schwa crush; feeds appendix adjunction.
- **Notes:** whether /l/ promotes is the live question in the *pilot* and *salad* probes (§4.6).

**final-glide settling** · vowel resolution · Stratum 6 · **[Settled in core]**
- **Statement:** final unstressed /i, o/ (and goose-merged /u/) reduce to syllabic /j̩, w̩/.
- **Attestations:** *toutw* (< *to total to*, final /u/ → /w̩/).
- **Notes:** whether the rule's domain is final-only or general is **[Open]** (§5.3; the *tomorrow* probe, §4.6).

#### 4.4.11 The coda purge

*Family note.* The legacy E2 family plus the dorsal coda rows. The conlang's restrictive coda phonotactics (§3.1) is the cumulative result of this family: codas weaken to /ʔ/, delete outright, assimilate, or — for the glottal stop — anchor.

**coda glottaling** · the coda purge · legacy **E2a** · Stratum 5 · **[Settled]**
- **Statement:** coda /t/ → /ʔ/ — strictly coda-weakening rather than elision; phonologizes GA variable glottaling.
- **Attestations:** *ŕeut* (< *carrot*); productive across the lexicon.
- **Notes:** unexpected /t/ retention in *pot* and *rérèyt* is **[Open — dictionary backlog]** (§5.2).

**need-clipping** · the coda purge · legacy **E2b** · Stratum 5 · **[Settled]**
- **Statement:** coda /d/ → ∅ with **no compensatory lengthening** on the preceding vowel.
- **Attestations:** *rhiiynii* (< *really need*) — the stem's /i/ remains short after /d/ deletes, contrasting with the prefix's /iː/ (a really-glide product).

**total l-loss** · the coda purge · legacy **E2c** · Stratum 5 · **[Open — multi-path]**
- **Statement:** singleton coda /l/ → ∅ along several paths (per the §2.1 note that /l/ occurs only in clusters); at least one path attested.
- **Attestations:** *toutw* (< *to total to*) — coda /l/ loss in a non-cluster environment.
- **Notes:** the full set of paths and conditions is deferred to a dedicated session (§5.2).

**coda k-loss** · the coda purge · Stratum 5 · **[Settled]**
- **Statement:** coda /k/ → ∅.
- **Environment:** blocked by labial rescue (below).
- **Notes:** the voiced counterpart, coda /g/ → ∅, is attested (*e* < *egg*) but not committed — **[Open — dictionary backlog]** (§5.2).

**labial rescue** · the coda purge · Stratum 5 · **[Settled; morphophonological extension Settled]**
- **Statement:** coda /k/ + adjacent /w/ → onset /kʷ/ — the /k/ absorbs the labial feature of the /w/ and escapes coda k-loss; ambisyllabic /kw/ → geminate /kʷː/.
- **Attestations:** *piiquóä*, *piquô*, *récquıìś*.
- **Morphophonological extension [Settled]:** the rescue also fires at suffixation — a stem-final /k/ that would be lost word-finally is preserved as /kʷ/ (⟨kw⟩) before a /w/-initial suffix. This is the **velar special case of the fossil resurrection** (§4.4.14), beside linking r (§4.4.3): the same suffix re-exposure, here channelled through labial rescue rather than the onset lenitions. Attestation: *ospokwþ* (< *speak* + *-wþ* < *with*), the /k/ of *speak* rescued by the suffix's /w/. (Where the suffix is not /w/-initial the same /k/ instead breathes to /h/ — *ospiihıĩ* — under the general rule.)

**the glottal anchor** · the coda purge · legacy **E2d** · Stratum 5 · **[Settled, junction behavior Open]**
- **Statement:** coda /ʔ/ does not elide under the regular cascade — the most stable coda segment in the language and a reliable anchor in derivations (§2.1).
- **Exception — the out-drop:** in grammaticalized particles, notably the *out* of phrasal-verb-derived stems, /ʔ/ is dropped; an optional careful-speech variant preserves it. Attestations: *beussou* (< *pass out*), *rhiiysseunnou* (< *really stand out*).
- **Notes:** the related drop at compound junctions (the junction drop, §4.4.13) is under analysis (§5.5).

#### 4.4.12 Suprasegmental residues and prosody

**nasal ghosting** · suprasegmental · legacy **S1** · rider on Stratum 2 · **[Settled]**
- **Statement:** when /n/ elides (soft-six hollowing), nasality transfers to the adjacent vowels. The transfer typically lands on V₁ (left of the elided /n/) and/or V₂ (right of it); in the orthographic system, V₂ carries the nasalization mark by default (see *Orthography Reference* §3.6 for the V₁-pitch / V₂-nasalization placement rule).

**breath ghosting** · suprasegmental · legacy **S2** · rider · **[Provisional]**
- **Statement:** breathy voice from elided coda /h/ or weakened obstruents.

**pitch stranding** · suprasegmental · legacy **S3** · Stratum 7 · **[Settled placement, Open contrastiveness]**
- **Statement:** pitch lands on the syllable that carried primary stress in the GA etymon, regardless of where conlang stress has migrated — the F0 residue of GA-style prominence. The full analysis is in §3.4.
- **Ordering:** independent of the segmental cascade.

**final landing** · prosody · Stratum 7 · **[Settled]**
- **Statement:** stress is assigned to the final vocalic position, via right-headed foot construction. Registered here for completeness; the prosodic machinery lives in §3.2–3.3.

#### 4.4.13 Junction phonology [Open — stubs]

*Family note.* Phenomena at compound and derivational junctions, surfaced by the *nocquii-* family; collected as named stubs because they likely share an analysis (§5.5). None has a committed statement yet.

- **junction welding** — gemination at compound seams: the coda glottal assimilates to and geminates the following consonant (/ʔk/ → /kʷː/ at the *not*+*quite* junction, with the labialization supplied by *quite*'s /w/).
- **and-went gemination** — at the *and*+*went* seam of the go-ahead perfect, the /n/ coda of *and* and the /w/ onset of *went* fuse to a geminate labial nasal /mː/ (⟨mm⟩), the /w/ supplying the labiality; a nasal-onset counterpart to junction welding. Attestation: *beunheumm* (< *…and went*). The best-attested of these junction phenomena. **[Provisional]**
- **the coffee shield** — junction welding counterbleeds debuccalization: a welded geminate /kː/ does not breathe to /h/ the way a singleton onset /k/ does, yielding /h/ ~ /kː/ alternations between free and bound forms of one base. Named for the showcase alternation in the *coffee* base attested across the *nocquii-* compound family; the key generalization to ratify when the junction rules are formalized.
- **the junction drop** — coda /ʔ/ loss at compound junctions, distinct from the out-drop. Attestations: *nocquıî*, *toś*.
- **the linker question** — the *-e-* combining form specified before vowel- or rhotic-initial bases vs. its absence in *nocquiiayo*.
- **compound prominence** — stress and pitch placement in derived compounds, undetermined.

#### 4.4.14 Inflectional morphophonology — the fossil resurrection

*Family note.* These processes are **morphophonological**: they fire at inflection (concord suffixation and infixation), not in the historical cascade, and their full statements are shared with `verbal-system.md` §4.2.2 (the coda-class concord paradigm). One mechanism unifies them — inflection re-exposes an etymological coda the cascade had suppressed word-finally, and the re-exposed segment re-runs the relevant stratum-1 lenitions. The rhotic and velar special cases were registered earlier (linking r §4.4.3; the labial-rescue extension §4.4.11); the **B12 elicitation** (June 2026; `drafts/translation_exercise_2/`) confirms the general pattern across every coda class and is the warrant for stating it as a single rule.

**the fossil resurrection** · inflectional morphophonology · morphophonological · **[Settled]**
- **Statement:** under inflection, a GA-etymological coda that the cascade deleted or altered word-finally **resurfaces**; because the concord increment is syllable-initial, the resurfaced coda is re-syllabified as an **onset** and **re-enters the stratum-1 onset lenitions** (§4.4.1–§4.4.2). The inflected form is therefore predicted by the GA source coda, not by the bare conlang citation form — making the paradigm a synchronic window for internal reconstruction.
- **Reflexes:** (i) resurrected /k/ → /h/ by k-breathing — *click* → *kli*, but PROG *klihıĩ*; *speak* → *ospii*, PROG *ospiihıĩ*. (ii) resurrected /s/ → /h/ by s-breathing — *notice* → *nouś*, PROG *nouhıĩ* (singleton only; geminate /sː/ resists: *þokssıĩ*). (iii) deleted/glottalled coronal /t d/ returns as a tap intervocalically — *recruit* → *rhikriutt*, PRET *rhikriuri*. (iv) voiced stop /b/ (< GA /v p/) nasalizes to geminate /mː/ — *drive* → *rhiib*, PROG *rhiimm*. (v) vocalized liquids return — rhotic as ⟨rr⟩ (= linking r) and lateral as ⟨l⟩ (the ‑le class: *barnacle* → *barnkw*, PROG *barnklm*).
- **Special cases (registered separately):** **linking r** (§4.4.3, the rhotic reflex); the **labial-rescue extension** (§4.4.11, the /k/→/kʷ/ reflex before a /w/-suffix).
- **Attestations:** the full coda-class battery is tabulated in `verbal-system.md` §4.2.2. Canonical: *klihıĩ*, *nouhıĩ*, *rhikriuri*, *rhiimm*, *barnklm*.
- **Notes:** open edges (the Db nasalization beyond labials; the singleton-vs-geminate sibilant-PROG split) are listed at `verbal-system.md` §4.2.2 and remain **[Open]**.

**the concord exponents** — the increments the fossil resurrection hosts. Their morphological distribution (shape-selects-reading, infinitive/passive shapes) lives in `verbal-system.md` §4.2; their segmental forms are:
- **PROG /‑ıĩ/** — the progressive-shaped concord suffix ⟨ıĩ⟩, from GA *‑ing* /‑ɪŋ/ → colloquial *‑in'* → nasal vowel /ɪ̃/.
- **PRET /‑ɾi ~ ‑t/** — the preterite/perfect ("‑ed-family") coronal: a tap /‑ɾi/ ⟨‑ri⟩ on vowel- and dental-final stems, plain /‑t/ after sibilants and voiceless obstruents. A lexically-listed strong-verb class retains GA morphology instead (`verbal-system.md` §4.2.1).
- **Infix placement** — in fused verb-plus-particle and verb-plus-object stems both exponents are **infixed at the root–particle seam** (PROG ‑n‑, PRET ‑t‑): *beussou* → *beussnou* / *beustou*. Placement is morphological; the segmental shapes are as above.

#### 4.4.15 Pending formalizations

**the sodium coloring** · pending · **[Open — formalization pending]**
- **Statement (committed at entry level):** labial /m/ colors a preceding schwa to /o/ (rather than the expected /ɛ/), then /m/ elides with nasal ghosting: *sodium* → *hoiiǫ* /ˈhoiõ/. Proposed productive for all *-ium* endings (*podium*, *Colosseum*, *Liam*). See §5.6.

#### 4.4.16 Retired changes

- **clack-to-tlack** (/kl/ → /tl/) — a draft shift with no dictionary attestations; removed from the inventory in v4 (see §7).

### 4.5 Worked derivations

Each row shows: GA etymon, conlang IPA, the rules that applied, the foot/appendix structure, and notes. Pitch and stress placement follow §3.3–3.4.

| GA etymon | GA IPA | Rules applied | Conlang IPA | Pitch | Stress | Structure |
|---|---|---|---|---|---|---|
| *Jennifer* | /ˈdʒɛnəfɻ/ | soft-six hollowing (/n/→∅, nasal ghosting); fin-thin; the -er tail (/ɻ/→/w̩/); smoothing | /ˈrɛ̃ːθw̩/ | /ɛ̃ː/ | /ɛ̃ː/ (coincide) | (ˈH) heavy foot + appendix |
| *Emma* | /ˈɛmə/ | the Emma landing (schwa strengthening) | /ɛma/ | /ɛ/ | /a/ | (L)(L) two light feet, dissociated prominences |
| *Emily* | /ˈɛməli/ | the really glide (/ɫ/→/j/); smoothing /ɪji/→/iː/ | /ɛmiː/ | /ɛ/ | /iː/ | (L)(ˈH) — pitch on left, stress on right |
| *Betty* | /ˈbɛɾi/ | soft-six hollowing (flapped /d/→∅); hiatus retained | /bɛi/ | /ɛ/ | /i/ | (L)(L) dissociated |
| *sodium* | /ˈsoʊdiəm/ | s-breathing; soft-six hollowing (/d/→∅); the sodium coloring (/m/ colors schwa →/o/, then elides with nasal ghosting) | /ˈhoiõ/ | /o/ | /õ/ | hiatus retained; see the sodium coloring, §5.6 |
| *countenance* | /ˈkaʊntənəns/ | k-breathing; massive schwa crush; syllabic promotion (/n̩/, /ʔ/); the Rochester flip | /ˈhoʔn̩ʔn̩ts/ | /o/ | /o/ (coincide) | (ˈH) heavy foot + long appendix |
| *Rochester* | /ˈrɑtʃɛstɻ/ | ch-funnelling (/tʃ/→/ts/); schwa crush; the -er tail (/ɻ/→/w̩/) | /ˈritsstw̩/ | /i/ | /i/ (coincide) | (ˈH) heavy foot + appendix |
| *carrot* | /ˈkæɻət/ → /ˈkæɻəʔ/ | k-breathing; coda glottaling; the wandering r (/ɻ/→onset, /h/→devoicing); smoothing /æ+ə/; trap-square (/æ/→/eː/) | /r̥eːʔ/ | /eː/ | /eː/ (coincide) | (ˈH) heavy monosyllable |
| *radio* | /ˈɻeɪdiˌo/ | soft-six hollowing (flapped /d/→∅); no smoothing (no /ə/, distant Vs); final landing | /reio/ | /e/ | /o/ | three syllables, hiatus retained |
| *baron* | /ˈbæɻən/ | the wandering r blocked (/b/ onset); trap-square; schwa crush; syllabic promotion (/n̩/) | /ˈbeɻn̩/ **[Provisional]** | /eː/ | /eː/ (coincide) | (ˈH) heavy foot + n-appendix |
| *barn* | /bæɻn/ | coda /ɻ/ coloring (trap-square /er/→/eː/ pathway); /n/ retained | /beːn/ | /eː/ | /eː/ (coincide) | (ˈH) heavy monosyllable |

#### Dictionary entries exercising the geminate and prefix rules

| Headword | GA etymon | Rules applied | Conlang IPA | Notes |
|---|---|---|---|---|
| *beussou* | *pass out* | pass-out voicing (/pʰ/→/b/ before /ɛ/); tensed /æ/→/ɛː/ (see the stand-out vowel environment flag, §5.1); pass-out gemination; mouth-north (/aʊ/→/oː/); the out-drop | /ˌbɛːˈsːoː/ | Geminate /sː/, the voicing environment, lexical /ʔ/-drop |
| *rhiiysseunnou* | *really stand out* | the really glide (/ɫ/→/j/); smoothing /ɪji/→/iː/; the stand-out vowel (/æ/-before-nasal→/ɛː/); pass-out gemination (/st/→/sː/); stand-out leveling (/nd/→/nː/); the out-drop | /ɻiːsːɛːnːoː/ | Three geminates (/sː/, /nː/), /iː/ phoneme, the stand-out vowel pathway |
| *rhiiynii* | *really need* | the really glide; smoothing /ɪji/→/iː/; need-clipping (coda /d/→∅, no comp. lengthening) | /ɻiːni/ | Long /iː/ in prefix (etymological glide source) vs. short /i/ in stem (no comp. lengthening from /d/-deletion) |
| *eplii* | *to apply* | the apply onset (initial /ə/→/ɛ/); the price splinter (short-/i/ reflex of /aɪ/) | /ˈɛpli/ | Initial-schwa strengthening, plain /pl/ onset (no geminate — reanalyzed 2026-06-23), short-/i/ price reflex |
| *toutw* | *to total to* | soft-six hollowing (flapped /t/→∅); total l-loss (coda /l/→∅, multi-path flagged open); mouth-north (/aʊ/→/oː/); smoothing; final-glide settling (/u/→/w̩/) | /ˈtoːtw̩/ | Coda /l/ elision attested; final /w̩/ in appendix position |
| *ŕe* | *today* (colloquial *t'day* /tʰɾeɪ/) | today coalescence (/h/ + tap → /r̥/ in onset); irregular /t/→/h/ (lexically conditioned); irregular /eɪ/→/ɛ/ (lexically conditioned, frequency-driven) | /ˈr̥ɛ/ | Today-coalescence attestation; light-monosyllabic foot |
| *ŕeut* | *carrot* | k-breathing; coda glottaling; the wandering r; smoothing; trap-square (/æ/→/eː/) | /ˈr̥eːʔ/ | Canonical wandering-r derivation; pitch+stress coincide on /eː/ |

#### Issues surfaced by the table

- ***Annabeth*** — output depends on a phonemic question about the source (whether GA V₂ was /ɛ/ or /ə/). The conlang's choice forces a phonological commitment about the input. **[Open]**
- **Multi-stress GA etyma** — when a GA word had primary + secondary stress, does the conlang preserve both as pitch peaks, or only the primary? **[Open]**

### 4.6 Probes and unresolved derivations

Words chosen to stress-test rule interactions where the description is silent or where two analysts could reasonably reach different outputs. Each probe specifies what it tests and what outputs are possible. These are forcing-functions for committing to ambiguous rules; they live alongside the worked derivations because they're the same kind of content at different stages of resolution.

#### Probes for schwa crush vs. the wandering r (E3 vs. M1)

**Probe: *pilot* /ˈpaɪlət/.**
- C₁ = /l/, not in the soft-six set, not a rhotic. Intervocalic position not vacated.
- V₂ = /ə/, eligible for schwa crush.
- C₂ = /t/, eligible for coda glottaling (→/ʔ/).
- Predicted: schwa crush fires, /l/ becomes syllabic, giving /ˈ(p/b)ail̩(ʔ)/ — the onset depends on the /p/-distribution flag (§5.1; pass-out voicing as stated does not voice /p/ here), and the nucleus on the price splinter.
- **Test:** does /l/ promote to syllabic, even though /l/ is described as "clusters only"? Or does the system block this? **[Decision needed]**

**Probe: *salad* /ˈsæləd/.**
- s-breathing in onset.
- C₁ = /l/, not eligible for hollowing or the wandering r.
- V₂ = /ə/, eligible for schwa crush.
- C₂ = /d/, eligible for need-clipping (→∅).
- Predicted: /ˈhæl̩/ with syllabic /l/, possibly /ˈheːl̩/ if smoothing or trap-square intervenes.
- **Test:** confirm the /d/-deletion path; confirm /l/-syllabification. **[Decision needed]**

#### Probes for cascade in dactyls

**Probe: *Penelope* /pəˈnɛləpi/.**
- Multiple loci for elision: /n/ (soft-six hollowing), /l/ (not in the set), schwas (crush or swallowing).
- Stress originally on V₂; what happens after rules apply?
- Predicted (one path): hollowing elides /n/ → /pəˈɛ̃ləpi/ → smoothing → /ˈbɛ̃ːləpi/. Then schwa crush may elide the next schwa → /ˈbɛ̃ːlpi/.
- **Test:** does the cascade run left-to-right, or does it apply globally and re-evaluate? **[Decision needed]**

**Probe: *Daniela* /ˌdæniˈɛlə/ or /ˌdænˈjɛlə/.**
- Already iambic (stress on penult); right-headed foot construction should be vacuous on stress placement.
- Soft-six hollowing applies to /n/ (→ nasal ghosting); /l/ not in the set.
- Predicted: a form like /rẽˈirɛrə/-shape depending on /d/, /n/, /l/ treatments.
- **Test:** working stress assignment with multiple eliding loci. **[Decision needed]**

#### Probes for smoothing edge cases

**Probe: a CVCVC where smoothing yields a long vowel of a quality the inventory doesn't support.**

- Long-vowel inventory: /iː, ɛː, oː, aː, ɨː/.
- Test word: *ladder* /ˈlæɾɻ/. After soft-six hollowing on /ɾ/ (and possibly the wandering r on /ɻ/), what's the resulting long vowel quality? /æ/→/eː/ by trap-square, but the second segment is rhotic, not vowel.
- **Test:** when smoothing would produce a quality outside the long-vowel inventory, does it fail and retain hiatus, or coerce to the nearest inventory member? **[Open]**

**Probe: *idea* /aɪˈdiə/.**
- After soft-six hollowing on /d/: /aiˈiə/ → smoothing of /iə/ → /aiˈiː/? Or does the price splinter apply first, giving a different input to smoothing?
- **Test:** does the price splinter apply *before* or *after* hollowing creates new hiatus? Rule ordering question. **[Open]**

#### Probes for nasalization persistence

**Probe: *ginger* /ˈdʒɪndʒɻ/.**
- Both /n/ and /dʒ/ are in the soft-six set; /ɻ/ becomes syllabic (the -er tail).
- Predicted: /ˈrɪ̃rw̩/ or /ˈrɪ̃w̩/ depending on /ndʒ/ resolution.
- **Test:** does nasal ghosting survive into a closed syllable? Or only in open syllables? **[Open]**

#### Probes for syllabic /j, w/ in non-final position

**Probe: *tomorrow* /təˈmɑɻo/.**
- /m/-onset blocks the wandering r; /ɻ/ stays. Mouth-north-adjacent /ɑ/→/o/, schwa absorbed.
- Predicted: /toˈboɻo/ or /təˈboɻo/, with possible final /o/ → syllabic /w̩/ (final-glide settling).
- **Test:** the syllabic-glide rule's domain — final only, or anywhere? **[Open]** Also bears on the bat-mat environment flag (§5.1): stressed-onset /m/ voices to /b/ here where *Emma*'s ambisyllabic /m/ does not.

#### Probes for monosyllables

**Probe: *cat* /kæt/, *song* /sɔŋ/, *tree* /tɻiː/.**
- *cat*: k-breathing, trap-square, coda glottaling → /heːʔ/. Clean derivation.
- *song*: s-breathing gives /hɔŋ/ → /hoŋ/, but /ŋ/ isn't in the inventory — possibly /n/ with nasal ghosting, giving /hõ/.
- *tree*: cluster /tɻ/ in onset is unusual — does /ɻ/ undergo the wandering r? Or is the cluster preserved?
- **Test:** monosyllabic outputs and cluster behavior in onset position. **[Open]**

---

## 5. Open questions

Organized by topic. Items are tagged with the dictionary entries that attest them where applicable; closure records live in the §7 versioning entries for the versions that closed them.

### 5.1 Data-gathering bucket — conditioning unclear, possible free variation

The following shifts are attested in dictionary entries but lack sufficient data to commit an environment. They may have conditioned reflexes, free variation, or lexically-specific (irregular) outcomes. Collect more attestations before proposing rules. Do not treat these as settled.

- **The price splinter (/ai/ reflex)** — at least four surface outcomes attested: /eː/, /i/, /ɛ/ (short), /i/ (short, possibly the same as the second but distinct from the first). Conditioning factors guessed at: stress position, preceding/following consonant, syllable count, lexical frequency. May include free variation. Candidate new attestation: predicative *hii* if the < *side* analysis holds (`language_reference.md` §3.3). **[Open — data gathering]**
- **/v/ conditioning (soft-six membership)** — proposed split: /v/ → /ɾ/ (tap merger) before front vowels; /v/ → /b/ (labial onset) before back vowels. Multiple attestations in each direction, but boundary cases unresolved. May also include free variation. **[Open — data gathering]**
- **/ɪ/→/ɛ/ lowering** — originally flagged as conditioned by following /b/; now attested without /b/ in context (*benskyi*, *béntsıìy*, *rékwıì*). May be a general unstressed-/ɪ/→/ɛ/ rule, or conditioned on syllable position. **[Open — data gathering]**
- **Rounding to /o/ in nasal-adjacent and word-initial environments** — attested as /ə/→/o/ or /ɪ/→/o/ after /n/ (*nobêt*, *noê*) and as /ɑ/→/o/ word-initially and after /n/ (*nocquıî* < *not*). New attestation (v4.1): the merged article *o* — *a/the* fall together as schwa after though-elision and strengthen to /o/ in this function-word environment. The squeaky-prothesis vowel quality (/o/) may belong here too. Mechanism unclear (nasalization coloring? labial spreading? function-word strengthening?); the attestations may reflect one rule or several. **[Open — data gathering]**
- **/j/ allocation** — /j/ is claimed by both the soft six (tapping in onset, hollowing intervocalically) and glide hardening (the reluctant yod, /j/→/ɻ/); which contexts route to which path is undetermined, and *yet*'s /j/ shifts by neither. **[Open — data gathering, surfaced v4]**
- **Tensed-/æ/ environment** — the stand-out vowel is stated for pre-nasal tensed /æ/ → /ɛː/, but *beussou* (< *pass*) shows the same /ɛː/ before /sː/; the operative environment may be the broader GA tensing set (voiceless fricatives as well as nasals). **[Open — data gathering, surfaced v4]**
- **/p/ distribution residue** — pass-out voicing restated in v4.1 (two environments: /ɛ(ː)/ anywhere; word-medial onsets generally). Remaining question: whether the word-initial resistance is categorical or frequency-sensitive. *(The former word-final-/p/-voicing sub-question is **withdrawn**: its only evidence, *preb* /ˈprɛb/ < *prep*, was reanalyzed as *baŕep* — ending in /p/, no final voicing — under prep-breaking, v4.6.)* **[Open — data gathering, restated v4.1; word-final clause retired v4.6]**
- **Bat-mat environment** — *Emma* /ɛma/ retains its medial /m/, suggesting the bat-mat merger targets true onsets and exempts GA-ambisyllabic consonants; the operative environment ("onset") needs pinning. The *tomorrow* probe (§4.6) bears on this. **[Open — data gathering, surfaced v4]**
- **Progressive (-ing) and -ed coda morphophonology** — **[Resolved v4.4]**, now formalized as the fossil resurrection family (§4.4.14); the coda-varied survey called for here was run (B12, June 2026). The unifying analysis: the increment re-syllabifies the GA-etymological coda as an onset and re-runs the stratum-1 lenitions; PROG = /‑ıĩ/, PRET = coronal /‑ɾi ~ ‑t/. Residual open edges (Db beyond labials; singleton-vs-geminate sibilant-PROG conditioning) are tracked at `verbal-system.md` §4.2.2.

### 5.2 Segmental questions

Carried forward and newly surfaced from dictionary work:

- **Treatment of /h/ in onset clusters** from s- and k-breathing edge cases.
- **Wandering-r edge cases (M1)** — what counts as "intervocalic" across cluster boundaries; behavior in trisyllabic words with multiple potential wandering-r sites.
- **Whether cute-and-quick fortition (the /k/-as-allophonic-/h/-before-glides analysis) holds.**
- **Smoothing failures** when the resulting long vowel would be outside the inventory (§4.6 probe).
- **Interaction of the price splinter with new hiatus from soft-six hollowing** (§4.6 probe).
- **Persistence of nasalization across resyllabification** (§4.6 probe).
- **Total l-loss (E2c) — coda /l/ elision paths.** Multiple paths along which singleton /l/ has been lost; the full set is undescribed and deferred to a dedicated session.
- **/ɜːr/ → /ɨː/ vocalization** — needed for *rhiušp*; not yet among the vocalic mergers (§4.4.8). **[Open — dictionary backlog]**
- **Coda /t/ retention vs. coda glottaling (E2a)** — *pot* and *rérèyt* show unexpected /t/ retention where coda glottaling predicts /ʔ/. **[Open — dictionary backlog]**
- **Coda /g/ → ∅** — §4.4.11 specifies coda k-loss; the voiced counterpart is not listed. Attested in *e* (< GA *egg*); analogous loss assumed, rule not committed. **[Open — dictionary backlog]**
- **/oʊ/ → /o/ short reduction** — attested in *toś* (< *toast*), the know-particle *no* (< *know*), *o* (< *though*, via though-elision), and *o* (< *go*, via soft-six /g/-loss). Possibly high-frequency reduction; whether it extends beyond function words needs data. **Lexical irregularity recorded here:** GA *do* → *o* by designed analogical absorption into *go* — the regular path would give a ⟨ii⟩ reflex via /uː/-fronting; rationale and consequences at `verbal-system.md` §13.3 and the pending dictionary entry for *o*. **[Open — dictionary backlog]**
- **/ɔr/ audit (report gliding)** — entries derived under the superseded /or/ → /oː/ half of the mouth-north merger need a re-derivation sweep; none of that entry's v4 attestations are NORTH-set, so the sweep is expected small. `cascade.py` is pinned to phonology v4 and needs a v4.1 sync (report gliding, though-elision, the affricate fork, pass-out widening, squeaky prothesis, the dishes clip). **[Open — tooling/audit, surfaced v4.1]**
- **Function-word smoothing condition** — *ęy* (< GA *any*) smooths to a monosyllable where a lexical word like *penny* would remain disyllabic; the frequency-sensitive condition is not yet a rule. **[Open — dictionary backlog]**

### 5.3 Prosodic and metrical questions

- **Is /r/ syllabic?**
- **Domain of syllabic /j, w/** — final only, or anywhere? (§4.6 probe.)
- **Treatment of monosyllables** — coda /ŋ/, onset clusters with /ɻ/ (§4.6 probe).
- **Appendix licensing conditions.** Working hypothesis: a syllable is parsed as appendix when its nucleus is a syllabic consonant of low sonority and it follows the stressed full vowel. Edge cases need testing.
- **Appendix and minimum-word effects.** Does the conlang have a minimum-word constraint? If so, does appendix material count toward satisfying it? Bears on the licensing of light-monosyllabic forms like *ŕe*.
- **Diachronic trajectory of the appendix.** The current state is best read as a snapshot mid-restabilization; does this matter for any synchronic decision, or is it purely a framing claim?
- **/ts/ in *countenance*.** Is the final /ts/ a complex coda on the second /n̩/ syllable, or is it a fourth nucleus in its own right? Affects appendix-syllable count and whether /ts/ is licensed as a syllabic affricate.
- **Internal structure of the appendix.** Are the nuclei in *hoʔn̩ʔn̩ts* a flat sequence of σ adjoined to ω, or is there sub-grouping (e.g., a degenerate foot containing /ʔn̩ʔn̩/)?
- **Do coda consonants contribute weight?** Surfaced by the *rhilþ* foot question (coda cluster /lθ/). Bears on light/heavy classification beyond the §3.1 mora rules. **[Open — dictionary backlog]**
- **Foot structure of vowelless words.** *skwkw* (< GA *skip*) is built entirely on syllabic obstruents; its foot structure is uncommitted. **[Open — dictionary backlog]**
- **Whether other /i/-initial diphthongal long vowels occur** (e.g., /io/ as `iio`). Predictable by analogy from /iɛ/ but unattested. See §2.2.

### 5.4 Pitch

- **Appendix–pitch interaction.** If pitch is contrastive (still open), does the appendix participate in the pitch contour, or is it pitch-flat?
- **Pitch contrastiveness.** Whether minimal pairs distinguishable only by pitch placement actually exist (audio-recorded verification deferred). Under the residue analysis (§3.4), low minimal-pair density is **structurally expected** — GA stress's segment-shaping power has absorbed most of the territory pitch could carry contrast in — and is not, on its own, evidence about contrastiveness, allophony, or vestigiality. Search strategy: GA stress-shift derivational pairs are not clean candidates (vowel quality co-varies with stress in GA); target pairs where the GA etyma share segment quality across the stress site. Acoustic data collection is the other prong: the §3.4 phonetic predictions (V₁ retains slight length and amplitude; F0 peak nucleus-aligned) are falsifiable with recordings.
- **Multi-stress GA etyma.** When a GA word had primary + secondary stress, does the conlang preserve both as pitch peaks, or only the primary?
- **Candidate minimal pair (*noê* / *nóè*).** *noê* "in a way" (pitch and stress coincident on the final, written *ê*) and *nóè* "no way" (pitch on the first syllable, written *ó*; stress on the final, written *è*) differ in the placement of pitch relative to stress. Flagged as a candidate pitch-accent minimal pair (user, June 2026); whether the two are segmentally close enough to count as a *true* minimal pair for the contrastiveness question above wants checking. **[Open]**

### 5.5 Compound-junction phonology

The *nocquii-* derivational family (see `dictionary.md`, *nocquıî* and its compounds) has surfaced a cluster of junction phenomena that the cascade does not yet cover. They are collected here as one bundle because they likely share an analysis:

- **Junction welding (junction gemination).** At the *not*+*quite* junction, the coda glottal assimilates to and geminates the following consonant: /ʔk/ → /kʷː/ (with the labialization supplied by the /w/ of *quite*). Registered as a named stub in §4.4.13; a committed statement is still pending. **[Open — dictionary backlog]**
- **The coffee shield (gemination counterbleeds debuccalization).** Per the *nocquıî* Morphology section: when the geminating consonant is /k/, the resulting geminate /kː/ does not debuccalize to /h/ the way a singleton onset /k/ does, yielding /h/ ~ /kː/ alternations between free and bound forms of the same base. The ordering relationship protects base consonants in compounds and is the key generalization to ratify when the junction rules are formalized. **[Open — dictionary backlog]**
- **The junction drop (coda /ʔ/ drop at compound junctions).** Related to but distinct from the out-drop (the E2d lexical exception); attested in *nocquıî* (final /ʔ/ from *quite*'s /t/) and in *toś*. Condition not yet stated. **[Open — dictionary backlog]**
- **The linker question (combining-form linker).** The *nocquıî* Morphology section specifies a linker *-e-* before vowel- or rhotic-initial bases, but the attested compound *nocquiiayo* lacks it. The combining-form rule needs reconciling and ratifying. **[Open — dictionary backlog]**
- **Compound prominence (stress and pitch in compounds).** Placement of both prominences in derived compounds is undetermined. **[Open — dictionary backlog]**

### 5.6 Pending rule formalizations

Rules committed at the entry level but not yet formalized in §4.4; each needs a dedicated-session write-up:

- **The sodium coloring (the *-ium* rule).** Labial /m/ colors a preceding schwa to /o/ (rather than the expected /ɛ/), then /m/ elides leaving nasalization: *sodium* → *hoiiǫ* /ˈhoiõ/. Proposed productive for all *-ium* endings (*podium*, *Colosseum*, *Liam*). **[Open — formalization pending]**
- **The *upon-us* reduction (*pons*).** The existential particle *pons* (< *upon us*; `language_reference.md` §4) shows grammatical-word reduction: /p/ retained, /ɑ/→/ɔ/→/o/, /n/ retained with schwa drop, /s/→/z/ adjacent to /n/. A function-word quirk; whether any sub-step is productive is unclear. **[Open — formalization pending]**
- **The *I-guess* merger (*reś*).** GA *I guess* and *I guessed* erode to one form, *reś* — a function-word reduction that neutralizes the tense contrast, which is the phonological basis for the tenseless guess particle (`verbal-system.md` §11.5). **[Open — formalization pending]**
- **The *which-is-when* convergence (*rhishisben*).** The clause linker *rhishisben* (`language_reference.md` §3.8) reflects a convergence of GA *which is when* and *which has been* into one form — a compound-junction reduction (cf. §5.5). **[Open — formalization pending]**
- **The *the-blank* cluster (*niblę*).** *niblę* (< *the blank*, in the read-the-room idiom) shows an irregular cluster: /-nð-/ ("in the") → /nː/ giving an initial /n/, /æ/ raised before the nasal, and a short quantity from formulaic unstress. Lexically specific. **[Open — formalization pending]**
- **Glottal-*t* under agglutination.** In the agglutinated perfect (*þiltm·ę·aų·et*; `verbal-system.md` §13.2), the perfective/*-ed* *t* surfaces as a glottal stop — coda glottaling (§4.4.11) reaching into suffixal morphology. Interacts with the concord/agglutination morphology; joint write-up pending. **[Open — formalization pending]**

---

## 6. Glossary

Technical vocabulary used throughout. Inline short definitions appear in earlier sections at first use; this glossary is the consolidated reference. Naming history (retired terms, alternatives considered) is held in `terminology-registry.md`.

**Appendix (prosodic appendix).** Material adjoined to the prosodic word at a level above the foot. Weight-bearing (moraic) but stress-invisible (foot-external). The structural mechanism for the conlang's post-stress syllabic-consonant tails (§3.5). Use the disambiguated form *prosodic appendix* where document appendices are in scope.

**Appendix nucleus.** A syllabic consonant heading a syllable that is part of the appendix rather than the head foot.

**Bleeding and feeding.** Standard ordering relations between rules. Rule A **feeds** Rule B if A creates the input environment for B. Rule A **bleeds** Rule B if A removes (consumes) inputs that B would otherwise have applied to. The cascade in §4.2–4.3 is built on a feeding-then-bleeding sequence.

**Compensatory lengthening.** The lengthening of a vowel to "compensate" for the loss of a neighbouring segment. In the conlang, compensatory lengthening occurs when intervocalic /d/ elides and V₁+V₂ smooth into V₁ː. Notably it does *not* occur in coda /d/ deletion (need-clipping, E2b), where the preceding vowel stays short.

**Concord affix.** *(Morphological term; included here for cross-reference completeness.)* The affix on the main verb showing concordance with the frame (light verb complex). Defined in `verbal-system.md` §4.

**Family (rule family).** A named group of sound changes sharing a mechanism, a drift, or a segment set (the rough-breathing family, the soft six, the three fates of schwa, …). Family membership is organizational; ordering is carried per-rule by the stratum field and the §4.2 master table.

**Foot.** A grouping of one or two syllables carrying a single primary prominence. The conlang builds **trochaic feet right-to-left**, with the **rightmost foot** receiving primary stress (right-headed prosodic word, left-headed foot — common cross-linguistically). The final foot is the last two syllables (or the last syllable, if only one survives elision).

**Head (of a foot).** The prominent syllable within a foot. The default head is the leftmost (trochaic).

**Mora (μ).** The unit of syllable weight. A short vowel = 1μ. A long vowel = 2μ. A syllabic consonant = 1μ. Coda consonants are non-moraic by default; syllabic consonants (which are moraic) can occupy coda position.

**Prominence.** Generic term for stress-like salience. Includes primary stress, secondary stress, and pitch-accent prominence.

**Quantitative metathesis.** A traditional term for the rightward shift of stress (or vowel length) across positions in a word. In the conlang, what looks like quantitative metathesis in dactyl-shaped words is a *consequence* of right-headed foot construction (§3.2), not a separate rule.

**Recursive prosodic structure.** Prosodic constituents (foot, prosodic word) that contain or are adjoined to other constituents of the same level. The mechanism by which appendix material attaches to the prosodic word.

**Resyllabification.** The redrawing of syllable boundaries after a segment is added or lost. After vowel elision, the orphaned consonant either joins the preceding syllable as a coda or becomes a syllabic nucleus of its own.

**Sesquisyllable.** A defined left-edge phenomenon in Mainland Southeast Asian languages: a reduced presyllable precedes a major stressed syllable, with the prosodic word iambic in shape. **The conlang's post-stress consonantal tails are NOT sesquisyllabic** (despite earlier drafts using the term). The structural details — direction (post-stress vs. pre-stress), shape (trochaic-with-tail vs. iambic), nucleus inventory, length — all diverge. Use *appendix* (above) for the conlang's pattern.

**Soft six, the.** The segment set /d, dʒ, n, j, g, v/, which lenites as a class — merging to the tap in onset (soft-six tapping) and deleting intervocalically (soft-six hollowing). See §4.4.2 for membership caveats (/n/ conditional, /v/ conditioned, /j/ contested with glide hardening).

**Sonority.** A scalar property of segments, roughly: vowels > glides > liquids > nasals > fricatives > stops. The **Sonority Sequencing Principle** (SSP) says syllable nuclei should be drawn from the most sonorous available segments. The conlang stretches this — it allows /s, θ, ʔ/ as syllabic, which are unusually low on the scale.

**Spondee.** A traditional foot name for a two-syllable foot where both syllables bear stress (DUM-DUM). Earlier drafts of this document used *spondee* and *stress clash* to describe certain conlang outputs. Both are retired: what was previously analyzed as clash is now understood as pitch-stress dissociation (pitch on one syllable, stress on another), not as two stresses on adjacent syllables.

**Stratum.** An ordered stage of the diachronic cascade (Stage 0 plus Strata 1–8; see the master table in §4.2). Each registry entry in §4.4 carries its stratum; orderings not committed are explicitly marked [Open].

**Stress clash.** Two adjacent syllables both bearing primary or near-primary stress. Retired from the conlang's analysis (see *Spondee*).

**Syllable weight.** A function of moraic content. **Light** = 1μ (short V, open syllable). **Heavy** = 2μ (long V, or short V plus syllabic consonant in same syllable).

**Trochee, iamb, dactyl.** Traditional foot names for stress patterns: trochee = DUM-bah, iamb = bah-DUM, dactyl = DUM-bah-bah. The conlang's default foot is trochaic (left-headed); the prosodic word is right-headed (rightmost foot is the head foot).

---

## 7. Versioning notes

### v4.8, June 2026 — writing-style pass (front matter)

Line-editing pass applying the writing-style prose canon. Removed the redundant sentence "The full phonological reference for the conlang: inventories, syllable and metrical structure, the diachronic cascade, and the open questions" after the Abstract (V4 restatement of the Abstract's closing sentence); the orientation-abstract pointer that followed it is kept. No inventory, rule, derivation, or status-tag content changed; §1–§6 reviewed and found conformant (the §4 registry and §4.5–§4.6 tables are structured reference data, not running prose).

### v4.7, June 2026 — §1.3 design context relocated to language_reference Appendix A.3

§1.3 "Typological position and stability" reduced to a short synchronic statement plus a *Design context* pointer: the natural-language precedents (Tashlhiyt Berber, Nuxalk, English/Slavic, Ancient Greek, the looser resonances), the distinctive-combination argument, and the stability/naturalism discussion moved to `language_reference.md` Appendix A.3 as part of the project-wide consolidation of conlanging-process material into that document's design appendix (`language_reference.md` v3.8). The §1.3 heading is retained; no other section renumbered. The §3.5 *appendix-adjunction* cross-reference that lived in the moved text now reads "`phonology.md` §3.5" in its new home. No segmental or rule content changed.

### v4.6, June 2026 — prep-breaking (GA /pr/ onset resolution)

New §4.4.5 rule **prep-breaking** [Settled in core]: word-initial GA /pr/ → /bɑˈɾ̥/ ⟨baŕ⟩ (cluster-breaking epenthetic /ɑ/, /p/→/b/, rhotic → devoiced tap /ɾ̥/). Surfaced by the B12 dictionary corrections (companion `dictionary.md` 2026-06-23): the three /pr/-initial verbs were standardizing divergently — *process* *baurrâuss* (/ɻ/ ⟨rr⟩ + /ɑ/) and *promise* *beŕaumss* (/ɾ̥/ + /ɛ/) — and are now reconciled on a single onset reflex (*baŕep*, *baŕaumss*, *baŕâuss*). The rule subsumes the entries' former `[New rule needed]`/`[Open]` epenthesis flags. The /ɑ/-epenthesis is shown to be **general** to labial-stop + rhotic onsets: GA /br/ breaks the same way (*bridge* → *baurrits*, already in the lexicon), keeping a **voiced** /ɻ/ — so the devoicing (→ /ɾ̥/) is the /pr/-conditioned part; *baurrits* now cites the rule as the voiced sibling. Further generalization (/tr, gr/; /dr/'s divergent palatalizing reflex) left **[Open]**. *(The deferred sixth B12 correction, *preb* → *baŕep*, is hereby resolved.)*

### v4.5, June 2026 — *apply* gemination reanalyzed away; rule renamed

The B12 dictionary corrections (companion `dictionary.md` changelog 2026-06-23) reanalyzed *epplii* "to apply" as **eplii** /ˈɛpli/ with a plain /pl/ onset cluster — GA *apply* /əˈplaɪ/ has a single onset /p/, not an ambisyllabic /pp/, so the geminate was spurious. Consequences: **§4.4.6 "apply gemination" renamed → "labial gemination"** and demoted **[Settled] → [Provisional — currently unattested]** (it was *epplii*'s sole witness); it is retained as the predicted labial parallel to pass-out gemination and continues to underwrite the systematic `pp` = /pː/ grapheme (`orthography.md` §2.4, also unattested now). The *eplii* spelling/IPA updated in §2.1, §4.3, the price splinter (§4.4.8), the apply onset (§4.4.9 — this rule keeps its name, *apply* still attests the initial /ə/→/ɛ/), and the §4.5 worked-derivation row (geminate step removed). Companion: `orthography.md` v3.9.

### v4.4, June 2026 — inflectional morphophonology family (the fossil resurrection; B12)

New registry family **§4.4.14 "Inflectional morphophonology — the fossil resurrection"**, settling the concord morphophonology the B12 elicitation resolved (`drafts/translation_exercise_2/verb-coda-morpho-phon-study.xlsx`; companion `verbal-system.md` v2.9 §4.2.2). The general rule **the fossil resurrection** [Settled]: under inflection a suppressed GA coda resurfaces, re-syllabifies as an onset, and re-runs the stratum-1 onset lenitions (so *click* → *kli* but PROG *klihıĩ*, the /k/ breathing). The two pre-existing morphophonological entries are reclassified as its special cases and **promoted to [Settled]**: **linking r** (§4.4.3, rhotic reflex; its /ɾ/-vs-/ɻ/ open note closed — ⟨rr⟩ = /ɻ/ per `orthography.md` §2.6) and the **labial-rescue extension** (§4.4.11, the /k/→/kʷ/ reflex). The **concord exponents** are registered: PROG suffix /‑ıĩ/, PRET coronal /‑ɾi ~ ‑t/, and the ‑n‑/‑t‑ infix at the root–particle seam. Renumbering: old §4.4.14 (Pending formalizations) → §4.4.15, old §4.4.15 (Retired) → §4.4.16; no inbound name-cites to those two. The §5.1 "progressive/-ed coda morphophonology" data-gathering item (logged v4.2) is hereby **resolved** for the attested classes; residual open edges (Db beyond labials, sibilant-PROG conditioning) move to `verbal-system.md` §4.2.2.

### v4.3, June 2026 — rhotic renotation; low-back asymmetry note

Two clarifications from the SAYING-round P/O pass (companion: `orthography.md` v3.7, `dictionary.md` changelog 2026-06-22). (1) **Rhotic renotation** (overview §, dictionary SC lines): GA "r" is broad notation for /ɻ/, so "/r/ → /ɻ/" in a derivation means **retention**, not change; the innovation is the **tap /ɾ/** phonemicizing (GA /d/-flap allophone + the soft-six mergers). The four dictionary SC lines that read "/r/→/ɻ/" are renotated to "/ɻ/ retained." (2) **Low-back asymmetry** [Provisional]: ties to `orthography.md` v3.7's `au` = /ɑ/ (short) — GA's relatively long lower back /ɑ/ with a de-phonemicized short counterpart (schwa) yields a naturalistic gap; consistent with the standing "schwa is not a reduction vowel" analysis (overview §).

### v4.2, June 2026 — translation-exercise round 2: glide-hardening, prothesis, junction rules (P/O session, SAYING round)

§4.4.4 gains **dark-l vocalization** (committed: /ɫ/ → /j/ adjacent to a front vowel, → /ɾ/ elsewhere; user decision), closing the §5.1 dark-l data-gathering item — the rhotic branch [Settled in core], the /j/ branch [Provisional]. §4.4.10 **squeaky prothesis** broadened to /s/+stop onsets generally (new attestations *ospii*, *ospokwþ* < *speak*; the *ospii*/*spyi* split left as the open conditioning question). §4.4.11 **labial rescue** gains a [Provisional] morphophonological extension — coda /k/ rescued to /kʷ/ before a /w/-initial suffix (*ospokwþ*), parallel to linking r. §4.4.13 gains the **and-went gemination** junction stub (/n/+/w/ → /mː/ at the *and*+*went* seam, *beunheumm*) [Provisional]. §3.1 records the **ideophone phonotactic exemption** (the expressive class is exempt from the core phonotactic/metrical constraints; `ideophones.md` §5). §5.6 logs five entry-level irregularities pending formalization (*pons*, *reś*, *rhishisben*, *niblę*, and glottal-*t* under agglutination); §5.1 adds the progressive/-ed coda morphophonology as a data-gathering item; §5.4 logs the *noê/nóè* candidate pitch pair. Sources: `phase4-triage-saying-2026-06.md` §5. Companion orthography edits in `orthography.md` v3.4.

### v4.1, June 2026 — translation-exercise rules; the /ɔr/ override

**New rules committed.** **though-elision** (/ð/ → ∅ everywhere; [Settled], user decision) with three consequences stated: *though* → *o* in all contexts, *notto* /noʔo/ resolved as fully regular (coda glottaling + elision — the former "intervocalic glottal stop" flag dissolves), and the *a/the* article merger derived (elision → shared schwa → /o/, logged under the §5.1 rounding item). **the dishes clip** (recognitional *the* procliticizes, clips, devoices to *þ*; prevocalic allomorph *y*; escapes though-elision by early fusion — the protective ordering parallels the coffee shield) — the phonological half of the *the*-doublet. **report gliding** (/ɔr/ → /oe/ in all environments; [Settled], user decision): an explicit **override**, not a split — the NORTH half of the mouth-north merger is superseded; mouth-north restricted to /au/; audit + `cascade.py` v4.1 sync flagged in §5.2. **the affricate fork**: cherish tapping (/tʃ/ → /ɾ̥/ in stressed onsets; *ŕequoþw*, *ŕeush*) paired with **ch-funnelling** promoted to a full entry (*ritsstw*, now also *hitsn*); conditioning is stress, not vowel quality — *Rochester* falsifies the front-vowel hypothesis. **squeaky prothesis** (/o/ before /skw-/; *osquihii*). **tap–rhotic dissimilation** (*ŕeush*) and **linking r** (*bemmw* ~ *bemmorret*) housed under §4.4.3, whose family note now states the rhotic-instability drift explicitly.

**Amendments.** pass-out voicing restated (and same-day corrected against the lexicon's word-initial /p/ forms): /p/ → /b/ before /ɛ(ː)/ anywhere and in word-medial onsets generally (*rhiboet*); word-initial /p/ before other vowels resists (*pot*, *pikkp*). §3.3 gains the phrase-level adjectival-predication stress statement (*hii* outranks the adjective; *hii* < *side* analysis [Open] at langref §3.3, logged as a price-splinter candidate in §5.1).

**Naming policy recorded.** Names are reserved for regular, far-reaching changes or for families/patterns (the affricate fork; the rhotic-instability drift). Morphophonological statements use standard terminology (*linking r*), and lexical irregularities are recorded plainly where they live — the designed *do* → *o* absorption into *go* sits in the §5.2 short-reduction item with its rationale pointer, not as a named rule.

**Handed to the orthography session:** the ⟨tt⟩ = /ʔ/ spelling in *notto*; ⟨æ⟩ → ⟨ä⟩ and ⟨œ⟩ → ⟨oë⟩ with the fold-diaeresis-under-pitch-marks convention (user decision); ⟨rh/rr/r·r⟩; report gliding's bearing on the /oe/ grapheme and the *boeś* question. *(Addendum: the orthography session ran as v3.1 the same day; this document's attestation spellings were swept — *boë*, *boëś*, *noë*, *piiquóä*.)*

### v4, June 2026 — sound-change registry: named rules, families, master ordering table

**§4.4 restructured into a named registry.** Every sound change now carries a descriptive name in the tradition of English historical phonology (exemplar names: the fin-thin merger; mechanism names: schwa crush), organized into **families** with a uniform entry format (statement / environment / ordering / attestations / notes, each entry tagged with its stratum and status). The names are the primary reference keys; **legacy IDs (E1–E5, M1, C-Coal, R-Assim, S1–S3) remain valid aliases**, so existing dictionary derivation records stay resolvable. Naming records to port to `terminology-registry.md` are listed in the session changelog.

**Rename table (legacy → registry name).**

| Legacy | Registry name |
|---|---|
| E1 | soft-six hollowing |
| E2a | coda glottaling |
| E2b | need-clipping |
| E2c | total l-loss |
| E2d | the glottal anchor (exception: the out-drop) |
| E3 | schwa crush |
| E4 | schwa swallowing |
| E5 | schwa strengthening (subcases: the Emma landing, the apply onset) |
| M1 | the wandering r |
| C-Coal | today coalescence |
| R-Assim | alveolar-wins |
| S1 | nasal ghosting |
| S2 | breath ghosting |
| S3 | pitch stranding |

**Newly named (previously unnamed table rows):** s-breathing, k-breathing, the cluster shield, cute-and-quick fortition, soft-six tapping, kr-whispering, w-hardening, the reluctant yod, bat-mat merger, pass-out voicing, fin-thin merger, the Rochester flip, stand-out leveling, the really glide, pass-out gemination, apply gemination, coda k-loss, labial rescue, goose-foot-strut merger (with goose fronting), the price splinter, mouth-north merger, trap-square merger, the stand-out vowel, choice smoothing, final-glide settling, final landing, the sodium coloring. *Smoothing* and *syllabic promotion* keep their existing mechanism names.

**Splits (two earlier merged statements separated by conditionality).**
- /m, p/ → /b/ split into the **bat-mat merger** (/m/, unconditional in onset, [Settled in core]) and **pass-out voicing** (/p/ → /b/ before /ɛ(ː)/ only, [Provisional — conditional and irregular]). The earlier unconditional /p/ claim is superseded; /p/ is not a general member of the labial funnel.
- /w, j/ → /ɻ/ split into **w-hardening** (/w/, [Settled]) and **the reluctant yod** (/j/ in restricted contexts only; *yet* unshifted; [Open — data gathering]). Grouped as the **glide hardening** family with a drift framing: glides merging toward the glide-like rhotic, complete for /w/, partial for /j/, with the candidate /ɫ/-vocalization path (§5.1) a possible third member.

**Retired: clack-to-tlack** (/kl/ → /tl/) — a draft shift with no dictionary attestations; removed from the inventory. Does not make the cut.

**Newly registered from derivation practice.** **The -er tail** (word-final /ɚ/ → syllabic /w̩/; used in the *Jennifer* and *Rochester* derivations) and **ch-funnelling** (/tʃ/ → /ts/; used in the *Rochester* derivation, registered as a sub-statement of the Rochester flip) had been applied in §4.5 without ever being stated as rules. Both now carry [Provisional] entries.

**Master ordering table added (§4.2).** A **Stage 0 GA surface snapshot** is now an explicit input step — the etymon in narrow surface transcription with flapping, glottaling, ambisyllabicity, /æ/-tensing, dark [ɫ], and r-coloring marked, since several rules phonologize GA allophony. Strata 1–8 follow (segment mappings; vacating the middle; vowel resolution; crush and promotion; the coda purge; residual vowel resolution; prosody; late rules). §4.3 now separates **ordering commitments** from **open orderings** explicitly; the vocalic-mergers-vs-Stratum-2 ordering, smoothing quality coercion, and dactyl directionality remain [Open] (the *idea*, *ladder*, and *Penelope* probes).

**Flags surfaced by the restructuring (added to §5.1):** /j/ allocation between the soft six and glide hardening; the tensed-/æ/ environment (*beussou* shows /ɛː/ outside the nasal condition); /p/'s distribution outside the voicing environment (clusters-and-geminates-only candidate); the bat-mat environment (*Emma*'s surviving ambisyllabic /m/).

**Junction phonology stubs (§4.4.13).** The §5.5 bundle registered as named stubs pending analysis: junction welding, the coffee shield, the junction drop, the linker question, compound prominence.

**Cross-references updated** throughout §§1–6 to the new names, with legacy aliases retained in parentheses at first mention. The §4.5 worked-derivation tables now cite rules by name; the probe set (§4.6) updated likewise, and the *pilot* probe's onset prediction corrected to reflect the pass-out-voicing split (the old form assumed unconditional /p/→/b/). Section numbering within §4.4 changed (the registry runs §4.4.1–4.4.15); inbound references from §§1–3 and §5 repointed.

### v3, June 2026 — conformance pass: voice, deduplication, dictionary backlog consolidated

**Abstract added (second pass on this draft).** Per the stub-abstract model adopted June 2026 (skill v1.1, §1.5): an architecture-level Abstract opens the document; `language_reference.md` §2 now carries a generated copy instead of a hand-maintained summary.

**Voice.** The document opener no longer narrates the latest revision (revision narration lives here in §7 only). Inline `[New in vX]` version tags removed from the §4.4 rule tables, replaced by plain attestation pointers ("Attested: *headword*"). The §3.5 *sesquisyllabic* retirement paragraph compressed into an analytical note pointing at the §6 glossary entry and `terminology-registry.md` (now the canonical home for naming history); §1.1's retirement narration dropped. §3.4's "this v2.2 commits to" phrasing removed; the stress-shift-pairs caveat (formerly split between §3.4 body and the §5 contrastiveness question) consolidated into a §3.4 analytical note. The §3.4 diachronic-pathway subsection retitled "Origin." Reading conventions and status-tag definitions now point at `language_reference.md` front matter.

**Deduplication.** Pitch material now has one home (§3.4): §1.1's bullet trimmed to the redistribution claim plus pointer; §2.3's bullet trimmed to placement-plus-status plus pointer; §4.4.5 S3 trimmed to the placement rule plus pointer. §3.2's degenerate-foot sentence drops the earlier-draft narration. §5's "Closed by v2 / v2.3" subsections removed — closure records are already enumerated in the §7 entries for those versions.

***sodium* updated throughout.** The committed *hoiiǫ* /ˈhoiõ/ derivation (closed v2.3) replaces the stale *hoiom* /ˈhoiom/ forms in §1.1, §3.1, and the §4.5 worked-derivations table; the *-ium* rule ticket moves to §5.6 (pending formalizations). §4.4.2's /ai/ row repointed at the §5.1 data-gathering bucket instead of carrying inline closure narration.

**§5 reorganized topically** (data-gathering bucket; segmental; prosodic/metrical; pitch; compound-junction; pending formalizations) instead of by the version that opened each question. **Dictionary backlog consolidated:** newly listed items not previously in this document, all sourced from `dictionary.md` entry flags and changelog — /ɜːr/→/ɨː/ (*rhiušp*); coda /t/ retention (*pot*, *rérèyt*); coda /g/→∅ (*e*); /oʊ/→/o/ short reduction (*toś*, *no*); function-word smoothing condition (*ęy*); coda-weight question (*rhilþ*); vowelless-word foot structure (*skwkw*); and the §5.5 compound-junction bundle from the *nocquii-* family (junction gemination /ʔk/→/kʷː/, gemination-bleeds-debuccalization and the /h/ ~ /kː/ alternation, junction /ʔ/-drop, the *-e-* linker reconciliation, compound stress/pitch). The §5.1 rounding-to-/o/ bucket entry broadened to cover the /ɑ/→/o/ attestations (*nocquıî*). No question is resolved by this pass; consolidation only.

**Terminology.** Conformed to `terminology-registry.md`: *prosodic appendix* disambiguation adopted; the §6 *Concord affix* entry updated to the frame/light-verb-complex pairing; the see-particle reference in §2.2 named per the registry. Section numbering unchanged throughout.

### v2.4, May 2026 — three rules committed; data-gathering bucket opened

**Three rules added to §4.4 from dictionary batch work.**
- **§4.4.1:** /ɔɪ/→/oe/ added to the vocalic mergers table. Attested in *bœ*, *boeś*, *nœ*.
- **§4.4.1:** /s/ cluster-protection added: debuccalization blocked when /s/ heads an onset cluster (e.g., /sp/, /sk/). See *spyi*.
- **§4.4.1:** /k/ labialization added: coda /k/ + adjacent /w/ → onset /kʷ/; blocks coda /k/→∅; geminate /kʷː/ when ambisyllabic. See *piiquóä*, *piquô*, *récquıìs*.

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
