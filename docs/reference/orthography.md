# Orthography

**Version:** v3.12 (August 2026)
**Predecessor:** v2.4 and earlier — see §7 (Versioning Notes).

**Abstract.** The writing system is Latin script with load-bearing diacritics in the manner of Vietnamese: the marks are not decorative, and ignoring them collapses minimal pairs. Diacritics and digraphs encode vowel length, nasalization, consonant devoicing, gemination, pitch, stress, and pitch-stress coincidence. Several conventions deliberately invert what a GA-literate reader expects, including position-dependent letter values and doubled vowels marking hiatus rather than length. This document is the canonical reference for the grapheme inventory, the diacritic placement rules, and the open spelling questions.

Status tags ( **[Settled]** / **[Provisional]** / **[Open]** ) and the reading conventions for forms and IPA are explained in `language_reference.md`, "How to read this document set." Terminology follows `terminology-registry.md`.

---

## 1. Design Principles

The orthography encodes:

- Vowel **length**, via `Vu` digraphs whose `u` traces the historical smoothed schwa. The `iiy` digraph is a special case for /iː/ (see §3.2).

  *On the IPA convention for long vowels:* where the length digraph supplies a *distinct vowel quality* in its second graph (as in `iie` /iɛ/, see §3.3), the IPA does not carry an additional length mark — the second-quality vowel is what makes the digraph bimoraic. Where the digraph's second graph reflects historical schwa or glide that has been absorbed into pure length (`Vu`, `iiy`), the IPA carries `ː`. The orthographic length pattern, not a uniform IPA convention, is what identifies a digraph as bimoraic.

- Vowel **nasalization**, with the diacritic placement reflecting the segment that historically carried the nasal feature.
- Consonant **devoicing**, via acute accent on sonorants and on `s`.
- Consonant **gemination**, via doubled letters (`ss`, `nn`, `pp`).
- **Pitch accent**, via acute on a vowel.
- **Stress**, via grave on a vowel — normally unwritten because predictable, marked in formal/pedagogical text.
- **Pitch–stress coincidence**, via circumflex (formal register).
- **Breathy voice**, via `VhV`. The feature is allophonic, not phonemic. **[Settled]** The `VhV` notation is stable; the proposed `VhU` variant for disambiguating medial /h/ from breathy voice is not adopted.

Three structural choices invert what a GA-literate reader would expect, and are worth flagging up front:

1. **`s` represents /z/ in non-onset position; in onset, `s` represents /s/.** This is consistent with the conlang's history: GA /s/ debuccalized to /h/, and onset /s/ in the conlang derives only from GA /st/ (which gave conlang /ts/ in some environments and /s/ in others). The voiceless reading in onset is therefore predictable, and `ś` (the explicit-devoiced spelling) is reserved for non-onset position where the contrast with /z/ is real. See §2.2.
2. **Digraphs do real phonemic work.** `rh` is the only way to write /ɻ/, distinct from bare `r` /ɾ/. `Vu` digraphs (and `iiy`) are the only way to write long vowels — single-letter doubling does *not* mark vowel length. (Single-letter doubling on consonants *does* mark gemination — see §2.4.)
3. **Doubled vowels mark hiatus, not length.** `aa` is /a.a/, `oo` is /o.o/, `ee` is /e.e/. The one apparent exception is `ii`, which represents the gliding short /i/ inherited from the GA "long-e" /ɪi/ quality — historically a sequence, synchronically a single syllable. See §3.3.

---

## 2. Consonants

### 2.1 Single-letter and digraph consonants

| Grapheme | IPA | Notes |
|---|---|---|
| `s` | /s/ in onset, /z/ elsewhere | See §2.2. |
| `ś` | /s/ | Used in non-onset position to mark devoicing of underlying /z/. Not used in onset (where `s` is already /s/). |
| `š` | /ʃ/ | Caron. |
| `r` | /ɾ/ | Alveolar tap — by far the more common rhotic. |
| `rh` | /ɻ/ | Retroflex approximant, **onset position**. Digraph. Non-onset /ɻ/ is written `rr` — see §2.6. |
| `sh` | /ʃ/ | Digraph (the hacek `š` is retired — user ruling, 2026-06-12). With `rh` and `th`, `h` is the system's digraph-former. |
| `þ` | /θ/ | Thorn. |
| `ð` | /ð/ | Eth. |
| `y` | /j/ | Palatal approximant. Not a vowel. |
| `w` | /w/ | Labio-velar approximant. Occurs almost exclusively in consonant clusters; most GA /w/ either merged with `rh` /ɻ/ or elided. |

Other consonants (`b`, `t`, `k`, `l`, `h`, `n`, `m`, etc.) take their expected IPA values. Recall from `phonology.md` that `k` and `l` occur only in clusters, and `h` is the regular reflex of GA /s/ in most positions. Aspiration on voiceless stops is allophonic (English-style: aspirate in stressed onsets) and is not represented orthographically.

### 2.2 The `s` / `ś` / `ss` system

The interaction of the `s` graphemes is one of the orthography's more subtle points. Four rules govern it:

**Onset `s` is /s/.** Onset `s` derives only from the GA /st/ → /s/ pathway (GA /s/ having debuccalized to /h/ in onset elsewhere). There is no underlying /z/ in onset, so onset `s` is unambiguously /s/. The `ś` grapheme is therefore not used in onset position; the explicit-devoicing mark adds no information.

**Non-onset `s` is /z/.** Intervocalic and final `s` represents /z/ by default. To mark a voiceless /s/ in these positions, write `ś`. There is **no general word-final devoicing**: a word-final `s` is /z/ like any other non-onset `s`, and a form whose final sibilant is a true /s/ is spelled `ś` (e.g. *rhemmêś* /ɻɛˈmːɛs/, *rhéulyèś* /ɻɛːlˈjɛs/), never bare `s`.

**Adjacent to a voiceless obstruent, `s` is /s/.** When a non-onset `s` is immediately adjacent to a voiceless obstruent — `p`, `t`, `k`, including the `ts` affricate — it surfaces as /s/, not /z/, and is written bare `s` (not `ś`): the voiceless value is predictable from the cluster, so the explicit-devoicing mark adds no information, exactly as in onset. Examples: *beusp* /bɛːsp/, *benskyi* /bɛnˈski/, *bessts* /ˈbɛsːts/, *ritsstw* /ˈritsstw̩/. This generalizes the onset rule's logic — `ś` is reserved for the genuinely contrastive non-onset position, which excludes voiceless clusters. (This clause supersedes the earlier word-initial-only formulation; it was confirmed by `spell2ipa.py` validation against the dictionary's cluster forms.)

**Doubled `ss` is /sː/ (geminate).** This applies regardless of position. The geminate is voiceless throughout. *beussou* /ˌbɛːˈsːoː/ "to fall asleep" and *rhiiysseunnou* /ɻiːsːɛːnːoː/ "to be different" both show the geminate at the syllable boundary preceding stress. A formal-register variant `śś` is licensed but not standard; in casual writing, `ss` is canonical for the geminate.

### 2.3 The devoicing diacritic

An **acute accent on a consonant** marks devoicing. This applies productively to the sonorants and to `s` in non-onset position:

| Grapheme | IPA |
|---|---|
| `ń` | /n̥/ |
| `ḿ` | /m̥/ |
| `ŕ` | /ɾ̥/ |
| `ś` | /s/ (i.e., devoiced /z/, in non-onset position) |

Voiceless sonorants generally surface as reflexes of elided coda obstruents, or from the M1 / C-Coal mechanism in onset (see `phonology.md` §4.4.4). Acute is the consistent way to write that devoicing wherever it occurs.

### 2.4 Gemination: doubled consonants

**Doubled consonants represent geminates** — single phonemes with double duration, sharing onset and coda position across a syllable boundary. Three are attested in the lexicon:

| Grapheme | IPA |
|---|---|
| `ss` | /sː/ |
| `nn` | /nː/ |
| `pp` | /pː/ |

Geminates arise from two diachronic feeds (see `phonology.md` §2.1): phonologization of GA ambisyllabic consonants in stressed-second-syllable environments (*beussou*), and cluster collapse such as /nd/ → /nː/ by regressive assimilation (*rhiiysseunnou*). `pp` /pː/ is currently **unattested** — its former witness *epplii* was reanalyzed as *eplii* (plain /pl/ onset) on 2026-06-23 — and stands as the predicted labial completion of the doubling convention (`phonology.md` §4.4.6, labial gemination).

The convention generalizes: any future-attested geminate /Cː/ is spelled `CC`. This is independent of the `Vu` length convention for vowels, which uses an explicit second letter rather than doubling.

Two letter-pairs are **carved out** of the geminate convention: `rr` spells non-onset /ɻ/ (§2.6), not a geminate tap — should /ɾː/ ever be attested, it will need another spelling (§6); and `tt` spells the glottal stop (§2.7), not /tː/.

**Labialized geminate /kʷː/.** A special case: the labialized geminate /kʷː/ (attested in *nocquıî* < *not quite*) has two candidate spellings. **`cqu`** treats the combination as `c` (first /k/) + `qu` (/k/ + labial /w/); **`kkw`** treats it as doubled `kk` (geminate) + `w` (labial). Both are valid; neither is yet canonical. **[Open: standardize one spelling — see §6.]**

### 2.5 Approximants and syllabicity

Per `phonology.md` §3.5, complex consonant clusters — including syllabic ones — can occur in prosodic-appendix position after the stressed final vowel of a word. This means `y` /j/ and `w` /w/ can appear in syllabic position post-vocalically.

Phonetically, a syllabic /j/ in such a position can be near-indistinguishable from an unstressed /i/, and a syllabic /w/ from an unstressed /o/. *Phonemically* they remain consonants: their distribution is governed by consonantal phonotactics (occurring in cluster positions, after the stressed nucleus), not by the vowel-distribution rules. The parallel is to Proto-Indo-European, whose approximants likewise had vowel-like syllabic realizations that complemented a minimal vowel inventory while remaining phonemically consonantal.

### 2.6 Positional spelling of the rhotics

The rhotic letters divide by phoneme and position. **[Settled — user proposal 2026-06-10, ratified 2026-06-12]**

| Grapheme | IPA | Position |
|---|---|---|
| `r` | /ɾ/ | the alveolar tap, all positions |
| `ŕ` | /ɾ̥/ | the devoiced tap (§2.3) |
| `rh` | /ɻ/ | onset |
| `rr` | /ɻ/ | everywhere else (coda, intervocalic) |

The linking *r* of suffixed forms (`phonology.md` §4.4.3) is non-onset by definition and writes `rr`: *bemmorret*. Where a tap abuts a syllabic tap and the letter sequence would mislead, the interpunct disambiguates per §3.5: `r·r` (*rhi·iiniir·ros*). `rr` is not a geminate spelling (§2.4).

### 2.7 The glottal stop

Two spellings by position:

- **The glottal stop is never written with the IPA character.** `ʔ` is transcription notation only — not a letter of the alphabet (user ruling, 2026-06-12). The v3 sample table's *ŕéuʔ* spellings were notation leaking into the orthographic column, corrected below.
- **`tt` is /ʔ/ in all non-initial positions** — intervocalic (*notto* /noʔo/ < *note though*: coda glottaling plus though-elision) and word-final (*meiktt* /mɛiʔ/-class concord forms). **[Settled — user decisions 2026-06-12]** The doubled letter typically preserves an etymological *t* while the pronunciation is the glottal.

`tt` is therefore carved out of the geminate convention (§2.4). Geminate /tː/ and /t/+/ʔ/ clusters are not expected to occur; should a rare case arise, the interpunct disambiguates per §3.5 — `t·t` for the geminate, `tt·t` or `t·tt` for clusters. The ambiguity is tolerated as practically negligible. Pre-consonantal /ʔ/ (the *hoʔnʔnts* type, where the transcription character still stands in for an undecided spelling) is **[Open]** (§6).

**`th` = /tʰ/.** Aspiration is generally unwritten, with one registered exception: the digraph `th` spells /tʰ/ (*thių*), motivated by the graphic three-way contrast `t` (plain) / `tt` (glottal) / `th` (aspirated). Whether `th` should generalize to *all* aspirated /t/ — making aspiration systematically written — is a larger change, **[Open]** in §6 (user leaning toward it, deferred). **[Provisional]**

**Expressive-class spellings.** In the ideophone class (`ideophones.md` §7), a single *t* may spell a glottal stop (*rhitmmtm*) — the regular `tt` = /ʔ/ convention is a core-lexicon rule the expressive class is exempt from (`phonology.md` §3.1). The onomatopoeia-object marker is written *-ðs* (the existing graphemes `ð` /ð/ + `s`; < GA *this*). **[Provisional]**

---

## 3. Vowels

### 3.1 Short vowels

| Grapheme | IPA | Notes |
|---|---|---|
| `i` | /ɪ/ | Short lax. |
| `ii` | /i/ | Short tense, with the gliding /ɪi/ quality inherited from GA "long e." Single syllable, written as a sequence. See §3.3. |
| `e` | /ɛ/ | |
| `a` | /ɑ/ | |
| `o` | /o/ | |
| `ä` | /æ/ | Residual /æ/ — did not fully collapse into /eː/. Diaeresis spelling (v3.1; formerly the ligature `æ`). |

Note that bare `u` does **not** occur as a grapheme: it appears only as the second element of a length digraph (§3.2). And `y`, despite the visual resemblance to an `i`-ish letter, is the consonant /j/ (§2.1), not a vowel.

**The fold hierarchy.** No letter carries two diacritics; when marks compete, the lower-ranked one **folds** (is dropped) and remains recoverable from the lexical spelling. The precedence: **ogonek > pitch/quantity mark > diaeresis**. So a pitch mark displaces a diaeresis (`ä` + acute → `á`), and an ogonek displaces a pitch mark (*bényǫ*: the final *ǫ* carries stress and an implied grave — the grave folds under the nasal hook). **[Settled — user decisions 2026-06-12]**

### 3.2 Long vowels: `Vu` digraphs and `iiy`

Long vowels are written with explicit-second-letter digraphs, never by doubling. There are two graphemic patterns: `Vu` for the long vowels whose source is smoothed-schwa (or related vocalic reanalysis), and `iiy` for /iː/. Of the `Vu` digraphs, **`au` is the exception**: it surfaces **short** /ɑ/, not long (it keeps the digraph spelling for its smoothed-`a`+ə source; see the table and Versioning Notes v3.7).

#### The `Vu` digraphs

| Grapheme | IPA | Source |
|---|---|---|
| `au` | /ɑ/ | smoothed `a` + ə (surfaces **short**, unlike the other `Vu` digraphs — see Versioning Notes v3.7) |
| `eu` | /ɛː/ | smoothed `e` + ə (and: /æ/-before-nasal via tense-/æ/-with-preserved-duration; see below) |
| `iu` | /ɨː/ (phonemically /ɪː/) | GA /u/ unrounded and fronted; historical laxness reanalyzed *as length itself*, leaving the long vowel where the back vowel had been |
| `ou` | /oː/ | smoothed `o` + ə (and: /au, or/ → /oː/) |

The `u` traces the historical smoothed schwa from intervocalic consonant elision (see `phonology.md` §4.1).

The `iu` case is the most theoretically interesting: there is no phonemic /ɨ/ in the conlang. The lax-back-vowel quality of GA /u/ was reinterpreted as length on the lax-front /ɪ/ axis, so what surfaces phonetically as /ɨː/ patterns phonemically as /ɪː/ — i.e., the long counterpart of /ɪ/ rather than its own phoneme.

The `eu` digraph has **two diachronic feeds** that both surface as /ɛː/:

1. Smoothed schwa: GA /ɛ/ + adjacent /ə/ smooths into long /ɛː/.
2. /æ/-before-nasal: GA pre-nasal /æ/ raises in quality toward /ɛ/ but preserves the tense-lax distinction via greater duration. The conlang reanalyzes that durational difference as length, yielding long /ɛː/ where lax /ɛ/ would have been short. *rhiiysseunnou* /ɻiːsːɛːnːoː/ (< *really stand out*) shows this pathway.

The orthographic digraph is unified across both feeds — the spelling `eu` doesn't distinguish them, and the surface /ɛː/ is the same.

The `ou` digraph also has two feeds: smoothed schwa and the /au, or/ → /oː/ merger. Same unification principle.

#### The `iiy` digraph for /iː/

**/iː/ is a phoneme** of the conlang, spelled `iiy`. It arises principally from /ɪji/-smoothing — the pathway in which /ɫ/ between high front vowels glides to /j/, and the resulting /ɪji/ sequence smooths into /iː/. *Emily* /ɛˈmiː/ (< /ˈɛməli/) and *rhiiynii* /ɻiːni/ "to need" (< *really need*, with the bleached *really*-prefix carrying the long /iː/) both show this pathway.

The `iiy` shape captures the etymology orthographically: `ii` is the gliding short tense /i/ (from GA "long-e" quality, see §3.3), and the trailing `y` reflects the historical glide that produced the length. Phonemically, `iiy` is a unitary /iː/, not a sequence — but the spelling preserves the visible trace of how the long vowel was formed.

A working rule of thumb: **`iiy` for /iː/ where there is an etymologically-justified glide source.** Where /iː/ might arise by other pathways without a glide source, the spelling convention is **[Open]** — possibilities include `iiy` extended by analogy, or bare `ii` for glide-source-less /iː/. This will be locked when more derivations attest the alternatives. To date, all attested /iː/ in the lexicon come from the /ɪji/-smoothing pathway and are spelled `iiy`.

### 3.3 Doubled vowels: hiatus, plus the special case of `ii`

Doubled vowels mark **hiatus** (two syllables) rather than length:

| Grapheme | IPA |
|---|---|
| `aa` | /a.a/ |
| `ee` | /e.e/ |
| `oo` | /o.o/ |

The apparent exception is `ii`, which is *not* a hiatus form. It represents the short tense /i/ with its gliding /ɪi/ quality — historically a vowel-glide sequence, synchronically a single syllable. The shape `ii` captures the gliding quality visually while the form behaves as a single nucleus.

**Genuine /i.i/ hiatus** is therefore written `iyi`, with `y` /j/ inserted to give the syllable boundary a real consonantal segment to live on. The `y` is not a vowel here — it is the regular palatal approximant doing what it normally does between vowels.

**/i.a/ hiatus** is written `iia`: the first syllable is the gliding /i/ (`ii`), and `a` follows directly. A further pattern, **`iie` /iɛ/**, attests a third row in the analysis: `ii` plus `e` marks neither hiatus nor a short diphthong, but a *bimoraic long diphthong* — a length pattern parallel to `Vu` and `iiy`, in which the second graph (`e`) supplies a distinct vowel quality rather than smoothing into pure length. The full contrast:

| Grapheme | IPA | Type | Morae |
|---|---|---|---|
| `ia` | /ia/ | diphthong, monosyllabic | 1 |
| `iia` | /i.a/ | hiatus, disyllabic | 2 (separate syllables) |
| `iie` | /iɛ/ | long diphthong, monosyllabic | 2 (single nucleus) |
| `ea` | /e.a/ | hiatus, disyllabic | 2 (separate syllables) |

The `iie` pattern is the first attestation of a **diphthongal long vowel** — a single bimoraic nucleus whose two morae carry different vowel qualities. Diachronically it parallels the `Vu` digraphs: a base vowel (here /i/) absorbs a following schwa as length, except that fronting under the influence of the preceding /i/ raises the schwa to /ɛ/ rather than smoothing it into pure length. The orthography records the etymology in the second graph.

This generalizes the long-vowel system: long vowels in the conlang are **bimoraic nuclei**, of which there are two surface types — *monophthongal long vowels* (`Vu`, `iiy`, with a length mark in IPA) and *diphthongal long vowels* (`iie`, where the second graph's vowel quality marks the second mora and no IPA length mark is used).

The contrast with the existing `ei` /ei/ diphthong (§3.4) is preserved and classifiable: `ei` is a **monomoraic** diphthong (with /j/ as a consonantal glide), while `iie` is a **bimoraic** diphthong (with /ɛ/ as a vocalic second mora). The conlang has two diphthong classes distinguished by mora count.

By analogy, additional diphthongal long-vowel digraphs are predictable but currently unattested — `iio` /io/ would be the parallel form for an /i/-initial bimoraic nucleus with /o/-quality second mora. Whether such forms occur is **[Open]**, but the convention generalizes if they do.

The form `ea` reflects a sound rule rather than just an orthographic convention: historical /ɪ.a/ does not occur, having lowered to /e.a/. The orthography records the surface form. A consequence: the spelling `ia` is unambiguously the diphthong, never a hiatus form.

### 3.4 The diphthongs: `ei` and `oë`

The diphthong /ei/ is written `ei`. Phonemically /ey/ (with `y` /j/ as the glide), it is a single syllable.

This grapheme is distinct from the length digraph `eu` /ɛː/ (§3.2): `e` followed by `i` is the diphthong, `e` followed by `u` is length. The contrast is real and the spelling distinguishes them cleanly.

The diphthong /oe/ is written **`oë`** — the diaeresis on the second element marks the pair as a single nucleus. **[Settled — user decision 2026-06-12; formerly the ligature `œ`, now retired.]** This resolves the long-standing *boeś* question: plain `oe` is unambiguously **hiatus** /o.ɛ/ on the mixed-pair pattern of `ea` (§3.3), `oë` is unambiguously the diphthong, and the ligature drops out of the system. The headword *boeś* respells *boëś* (diphthong), pending the dictionary sweep (§6).

Two regular feeds supply /oe/: **choice smoothing** (GA /ɔɪ/) and **report gliding** (GA /ɔr/; `phonology.md` §4.4.8). Classification: /oe/ patterns as the second **diphthongal long vowel** alongside `iie` /iɛ/ (§3.3) — a bimoraic nucleus with two vowel qualities, which both of its sources (a GA diphthong; a vowel-plus-coda-rhotic sequence) supply naturally. **[Provisional — mora class to be confirmed against stress and meter]**

Under the fold hierarchy (§3.1), a pitch or quantity mark anywhere on the digraph **supplants the diaeresis** — the marked digraph cannot be read as hiatus, so the diaeresis's work is done (the same logic as dotless `ı` in marked `ii`): *rhibôet*, with the circumflex on the diphthong's head mora. A mark on the second mora is written on plain `e`.

### 3.5 The interpunct as optional disambiguator

In pedagogical or formal-register text, an interpunct may be inserted to disambiguate. Its three uses: **[Provisional — unified policy, v3.1]**

- **Vowel hiatus:** `a·a` for /a.a/, `o·o` for /o.o/, `ii·a` for /i.a/.
- **Morpheme and compound junctions:** *not·ho* (< *note how*), *piknib·orrô* (stem and incorporated suffix), and the junction compounds of the *nocquıî* family.
- **Consonant-letter sequences** that would otherwise misread: `r·r` for a tap adjoining a syllabic tap (*rhi·iiniir·ros*; §2.6).

The interpunct is a register marker rather than a phonological one. Casual writing omits it; learning materials, dictionaries, and formal documents include it where ambiguity might otherwise arise.

### 3.6 Nasalization

Nasalization is marked, but the diacritic differs by segment — historical accident of which marks were in use when which forms were first transcribed.

**Tilde** is used on the close-front segments and on the approximants:

| Grapheme | IPA | Notes |
|---|---|---|
| `ĩ` | /ĩ/ | Nasalized short tense /i/. |
| `ỹ` | /j̃/ | Nasalized palatal approximant. Phonotactically capable of syllabic realization (see §2.5); occurrences are expected to be rare. |
| `w̃` | /w̃/ | Nasalized labio-velar approximant. Even rarer than `ỹ`. |

A note on the absence of `į`: the lax /ɪ/ does not nasalize, so no ogonek-on-`i` form occurs.

**Ogonek** is used on the open and mid vowels:

| Grapheme | IPA |
|---|---|
| `ą` | /ɑ̃/ |
| `ę` | /ɛ̃/ |
| `ǫ` | /õ/ |

For long vowels (`Vu` digraphs), the ogonek lands on the `u`, which is etymologically apt — the `u` is the smoothed schwa, and historical nasalization rode on schwa-adjacent elided consonants:

| Grapheme | IPA |
|---|---|
| `aų` | /ɑ̃ː/ |
| `eų` | /ɛ̃ː/ |
| `ių` | /ɨ̃ː/ (phonemically /ɪ̃ː/) |
| `oų` | /õː/ |

**A near-minimal pair** shows nasalization carrying lexical contrast on its own: *riųś* "news" (nasalized *ių* /ɨ̃ː/) versus *riuś* "juice" (oral *iu*) — distinguished by the ogonek alone.

#### Placement principle: V₁ pitch / V₂ nasalization

Nasalization in the conlang nearly always arises from a historical **V₁nV₂** sequence: /n/ elides and the nasal feature transfers to the surrounding vowels (see `phonology.md` §4.4.5 S1). In the typical case, V₁ is also the historical-GA-stress syllable (the one carrying pitch under §3.7), and V₂ is the post-elision residue — they're already different vowels. The orthographic convention exploits this:

- **Pitch acute on V₁** (the historical-stress vowel).
- **Nasalization on V₂** (the rightward partner of the original /VnV/ pair).

For long vowels written `Vu`, V₂ *is* the `u`, so the existing ogonek-on-`u` convention falls out as a natural consequence. No diacritic stacking is required in the typical case.

#### The clash case

A genuine clash arises only when a **short vowel** carries both pitch and nasalization, with no V₂ to host the nasal mark. This is rare and may not actually arise in attested forms. The fallback:

- Pitch acute is always written.
- Nasalization is either left **implicit** (recoverable from etymology and context) or marked etymologically with `Vn` — writing the historical /n/ as if it had not elided, letting the consonant serve as orthographic carrier for the nasal feature.

So a hypothetical clash form gets either `é` (implicit nasalization) or `én` (explicit etymological-spelling nasalization), never `ę́`. The choice between the two is a register question, parallel to the interpunct.

Stacked diacritics are not the working policy. They might still arise as Unicode renderings of certain combinations, but they are not part of the everyday orthography.

#### Predictable nasalization left unmarked

When glide nasalization is fully predictable from an adjacent nasalized vowel (e.g., a nasalized vowel immediately preceding or following /j/ or /w/), the glide's nasalization is left orthographically unmarked. The diacritically simpler form (bare `y` or `w`) is canonical; the nasalized form (`ỹ`, `w̃`) is licensed in hyperprecise transcription but is not standard. Example: *ęy* /ẽj̃/ is written `ęy`, not `ęỹ` — the nasalization of /j̃/ is recoverable from the nasalized `ę`.

### 3.7 Pitch and stress

Pitch and stress occupy different syllables in most words (see `phonology.md` §3.3–3.4 for the placement rules and the residue analysis) and are marked separately in the orthography. **Three diacritics on vowels** handle them:

- **Acute (`´`) on a vowel** — pitch accent. Always written, in casual and formal register alike, because pitch placement is etymologically determined but not synchronically derivable from the surface form — it is lexical information, like English lexical stress (`phonology.md` §3.4).
- **Grave (`` ` ``) on a vowel** — stress. Normally unwritten because stress is predictable (always final). Marked only in formal or pedagogical text.
- **Circumflex (`^`) on a vowel** — pitch + stress coincidence. Combines acute and grave when they would land on the same syllable. Formal register only.

The acute-on-*consonant* devoicing convention (§2.3) is unaffected — pitch and devoicing live on different segment types and don't collide.

#### The `ii`-digraph diacritic rule

When a stress or pitch diacritic lands on one element of the `ii` digraph, the *other* element is written without its dot as **`ı`** (dotless i). This reduces visual clutter and makes clear which element bears the mark. The convention applies to any diacritic on `ii`: grave for stress, acute for pitch, or circumflex for coincidence.

Examples: in *béntsıìy*, the stress grave lands on the second `i` of `iiy` → written `ì`; the first `i` becomes `ı`. In a form where pitch lands on the first `i`, the acute makes it `í` and the second `i` becomes `ı`.

#### Placement on digraphs and syllabic consonants

- **`Vu` length digraph:** grave (stress) lands on the `u`, parallel to ogonek-on-`u` for long nasals. Acute (pitch) lands on the `V` if pitch is on this syllable.
- **`iiy` for /iː/:** grave lands on the second `i` of `ii` (making the first `i` dotless `ı` per the rule above). The trailing `y` is never marked — it is a semivowel recording the lengthened realization, not a vowel. Acute on the first `i` if pitch is on this syllable.
- **Syllabic consonants in stressed position:** grave borne by the consonant in pedagogical text (e.g., `ẁ` for stressed syllabic /w̩/).

#### Worked examples

| GA etymon | Conlang IPA | Casual orthography | Formal orthography | Pitch | Stress |
|---|---|---|---|---|---|
| *Emma* | /ɛma/ | `éma` | `émà` | /ɛ/ | /a/ |
| *Emily* | /ɛmiː/ | `émiiy` | `émıiìy` | /ɛ/ | /iː/ |
| *Betty* | /bɛi/ | `béi` | `béì` | /ɛ/ | /i/ |
| *Jennifer* | /rɛ̃ːθw̩/ | `réųþw` | `réųþẁ` | /ɛ̃ː/ | syllabic /w̩/ |
| *carrot* | /r̥eːʔ/ | `ŕéutt` | `ŕêutt` | /eː/ | /eː/ (coincide) |
| *barn* | /beːn/ | `béun` | `bêun` | /eː/ | /eː/ (coincide) |

Monosyllables have pitch and stress on the only available vowel — circumflex in formal register, plain acute in casual.

Multisyllables typically dissociate, with pitch on the historical-GA-stress syllable and stress on the new final position. The worked instance is *óhò* "hey" (< *OH hey*) against *ohô* "aha" (< *oh I see*): *óhò* carries pitch on the first vowel (acute *ó*, the historical GA stress) and stress on the final (grave *ò*), while in *ohô* the two coincide on the final (*ô*). This pair is **acoustically attested**: across the repetitions that survive content verification, the F0 centroid moves later by 6.0 percentage points from *óhò* to *ohô* — the predicted direction, in 4 of 4 usable blocks. The mean normalised contours carry it more plainly than the summary statistic does: *ohô* rises from 84 Hz to a late peak of 115 Hz and falls back to 80, while *óhò* stays within 84–98 Hz with no comparable excursion. The supporting pair *hóhonìt* / *hohô* moves the same way (+10.0 pp, Cohen's *d* +1.15). (Figures corrected 2026-08-17; the 16.3 / 9.1 Hz decline values previously cited here were measured on a corrupted extraction and are withdrawn — see `planning/audio-pipeline-plan.md` §7. The attestation survives the correction; only the numbers change.)

**Which GA element carried the accent is the load-bearing fact,** and it is the one an etymology line most easily gets wrong. The *noê* entry formerly stood as a *noê* / *nóè* pair on the strength of a **NO** way! reading of its source; the ordinary realization is *no WAY!*, leaving nothing on the first syllable for the conlang to inherit, and the recorded production shows no first-syllable pitch peak. The two headwords were merged (`dictionary.md` §*noê*, August 2026). Where an etymon's GA accent placement is uncertain, say so in the entry rather than inferring it from the conlang spelling — the spelling is the thing being derived.

[Open: whether pitch on the *final* (stressed) vowel is stable. Recorded final-stressed words vary between a low final, retaining the pitch of the originally unstressed GA syllable, and a high final; the words with first-syllable pitch do not vary this way. If the variation is real, the circumflex's "coincidence" reading describes only the high-pitch realization and the low one is unmarked. See `phonology.md` §5.4.]

---

## 4. Quick Reference Table

| Diacritic / device | On consonants | On vowels |
|---|---|---|
| Acute (`´`) | Devoicing: `ń ḿ ŕ ś` | Pitch: any vowel |
| Grave (`` ` ``) | — | Stress: any vowel (formal/pedagogical only; predictable so usually unwritten) |
| Circumflex (`^`) | — | Pitch + stress coincidence (formal only) |
| Caron (`ˇ`) | `š` /ʃ/ | — |
| Tilde (`˜`) | `ỹ w̃` (nasalized approximants, rare) | Nasalization on close-front: `ĩ` |
| Ogonek (`˛`) | — | Nasalization on open/mid: `ą ę ǫ`; on `u` of length digraphs for long nasals: `aų eų ių oų` |
| Doubling | Gemination: `ss` `nn` `pp` | Hiatus: `aa ee oo` (and special: `ii` for gliding /i/) |
| `Vu` digraph | — | Length: `eu iu ou` (`au` = short /ɑ/ — historical `Vu` digraph that did not lengthen) |
| `iiy` digraph | — | Length: /iː/ from /ɪji/-smoothing |
| `ei` digraph | — | Diphthong /ei/ |
| `h` between vowels | — | Breathy voice: `VhV` |
| Interpunct (`·`) | — | Optional disambiguator: hiatus, junctions, consonant sequences (formal register) |
| Digraph | `rh` /ɻ/ | — |
| Special letters | `þ ð` | `ä` (plus the digraph `oë`, §3.4) |

---

## 5. Pedagogical Implication

Because diacritics and digraphs are load-bearing, learning materials must drill minimal pairs distinguished only by these marks. A learner who treats diacritics as ornamental will collapse pairs the language treats as fully distinct.

The richest minimal-pair territories are:

- `s` vs. `ś` (/z/ vs. /s/) in non-onset position
- `s` (single) vs. `ss` (geminate) — singleton vs. geminate
- `r` vs. `rh` (/ɾ/ vs. /ɻ/)
- `i` vs. `ĩ`, `a` vs. `ą`, etc. (oral vs. nasal)
- `a` / `au`: both now surface /ɑ/ (the historical length contrast is **retracted** — `au` is short, v3.7); the long /ɑː/ counterpart is deferred to a future `aa` [Open]
- `ia` vs. `iia` vs. `ea` (diphthong vs. /i/-initial hiatus vs. lowered /ɪ/-initial hiatus)
- `ei` vs. `eu` (diphthong /ei/ vs. length /ɛː/)
- `ii` vs. `iiy` (short tense /i/ vs. long /iː/)
- Pitch-placement contrasts on otherwise homographic forms (acute on V₁ vs. acute on V₂, etc.)

---

## 6. Open Questions

- **Spelling convention for /iː/ outside the etymological-glide environment.** Working rule is `iiy` where there's a glide source; the convention for /iː/ from other pathways (if any are attested) is undecided. Bare `ii` for non-glide-source /iː/, or extension of `iiy` by analogy?
- **Standardization of /kʷː/ spelling.** Both `cqu` and `kkw` are valid (see §2.4). Which becomes canonical is open.
- **Whether the interpunct will eventually become obligatory** in any context, or remain a register feature.
- **Treatment of `ä` in environments where it borders on /eː/** — whether the orthography preserves the etymological `ä` or follows the surface form.
- **Pre-consonantal /ʔ/ spelling** — `tt` covers intervocalic and final position; the *hoʔnʔnts* type (glottal before a consonant) has no spelling yet, and that headword awaits one.
- **A spelling for /ɾː/** if ever attested (`rr` is carved out of §2.4).
- **Generalizing `th` /tʰ/** to all aspirated /t/ (overwriting plain `t` where aspirated) — would make aspiration systematically written; user leaning yes, deferred as a large change (§2.7).
- **Mora class of `oë`** — confirm the diphthongal-long-vowel classification (§3.4) against stress placement and meter.
- **Whether genuine clash cases** (short vowel carrying both pitch and nasalization, with no V₂ to host the nasal mark) actually occur in the lexicon. If so, whether the implicit (`é`) or `Vn` (`én`) route should become the default.

---

## 7. Versioning Notes

### v3.12, August 2026 — §3.7's acoustic figures corrected

The numbers cited in §3.7 for the *óhò* / *ohô* attestation were measured on the wrong audio. The pipeline's segmentation stage assigned every utterance one position early, exporting the spoken English digit slates in place of the words, so the "16.3 Hz against 9.1 Hz" declines describe the numerals *one* and *two*. Fixed at source (`tools/audio-split.py`), with a content gate added (`tools/audio-verify.py`) that rejects any token transcribing as its own item number; see `planning/audio-pipeline-plan.md` §7.

**The attestation survives; only the figures change.** Re-measured on corrected, content-verified audio, the F0 centroid moves later by 6.0 pp from *óhò* to *ohô* in 4 of 4 usable blocks, and the mean contours separate more clearly than before — *ohô* rises to a late peak of 115 Hz where *óhò* has no comparable excursion. The supporting pair *hóhonìt* / *hohô* agrees (+10.0 pp, *d* +1.15). §3.7 now cites these.

The **[Open]** on the circumflex opened in v3.11 is **downgraded to an untested hypothesis**. It rested on a contrast between first-syllable-pitch and final-stressed words that does not survive correction: the reported categorical split (0 of 10 against 8 of 20 rising) becomes 2 of 9 against 4 of 17, with Mann–Whitney *p* = 0.196 and Fisher *p* = 1.000. Final-stressed words do scatter more widely (sd 3.5 st against 1.8 st), but Levene's test gives *p* = 0.484, so even that is unestablished. The circumflex's "coincidence" reading is not currently in question on acoustic grounds — nothing acoustic bears on it yet.

### v3.11, August 2026 — §3.7 worked example replaced; *noê*/*nóè* merged

*(Superseded in part by v3.12: the 16.3 / 9.1 Hz figures below are withdrawn. The merger and the worked-example replacement stand.)*

The §3.7 illustration of pitch/stress dissociation moved from *nóè* / *noê* to *óhò* / *ohô*. The old example was not one: *nóè* had been assigned first-syllable pitch from a **NO** way! reading of its GA source, where the ordinary realization is *no WAY!*, leaving *no* unstressed and the acute without a source. The two headwords are merged into a single polysemous entry (`dictionary.md` §*noê*, changelog 2026-08-12). The replacement pair is the acoustically attested one — pilot 01 measured *óhò* falling 16.3 Hz from an early peak against *ohô*'s 9.1 Hz from a later one, the predicted direction at d ≈ 1.1.

Two additions in the same section. A **practice note**: which GA element carried the accent is the load-bearing fact in these derivations and the one most easily got wrong; where it is uncertain the entry should say so rather than back-infer it from the conlang spelling. And an **[Open]** on the circumflex: recorded final-stressed words vary between a low and a high final pitch while first-syllable-pitch words do not, so "coincidence" may describe only one of two realizations (`phonology.md` §5.4).

The three-diacritic system itself is unchanged, and the dissociation analysis is unaffected — one lexical item was misassigned, not the rule.

### v3.10, June 2026 — writing-style pass (front matter)

Line-editing pass applying the writing-style prose canon. Removed the redundant standalone line "A dedicated reference for the conlang's writing system" after the Abstract (V4 restatement — the Abstract's closing sentence already states the document's scope). No grapheme, rule, or status-tag content changed; §1–§6 reviewed and found conformant.

### v3.9, June 2026 — `pp` geminate now unattested (*epplii* → *eplii*)

The B12 dictionary corrections (companion `dictionary.md` changelog 2026-06-23; `phonology.md` v4.5) reanalyzed *epplii* "to apply" as **eplii** /ˈɛpli/ — a plain /pl/ onset, no geminate. §2.4 prose updated: `pp` /pː/ loses its only attestation and is now flagged as the **predicted** labial completion of the doubling convention (still spelled `pp` per the "any future `Cː` doubles" generalization). The grapheme row is retained; the historical motivation note in this section (the v3.4-era "Geminate-doubling generalization" entry, which cites *epplii*) is left verbatim as a record of why the convention was first formulated.

### v3.8, June 2026 — dictionary respell sweep closed

The §6 "Dictionary respell sweep (pending)" open question is **removed** — verified complete (2026-06-22). The `œ`→`oë` and `æ`→`ä` conventions are fully applied in the `dictionary.md` body (headwords swept incrementally / at v3.1: *boë, noë, boëś, hoë hoś*; zero `œ` remains) and in `phonology.md` attestations (its v4.1); the lone stray *rékriiyæ*→*rékriiyä* (a supersession-trail reference) was fixed. `cascade.py` is not in the repo, so that clause is moot. The generated quickref files still show pre-sweep forms (*bœ, nœ, boeś*) and will refresh on the next quickref rebuild. (The separate *boëś* diphthong-vs-hiatus question stays [Open] — see the *boëś* entry / §3.4.)

### v3.7, June 2026 — `au` = /ɑ/ (short)

`au` is reassigned from long /ɑː/ to **short /ɑ/** (author ruling, surfaced in dictionary batch D4-C: *baurrits* /bɑˈɻɪts/, etc.). It is the one `Vu` digraph that does not lengthen — kept as a digraph for its smoothed-`a`+ə source. Applied here: the vowel table (§3.1), the diacritic summary (§4), and the §5 minimal-pair drill no longer treat `au` as length. The `a`/`au` overlap is **not** a defect to fix: both surface /ɑ/ (a historical-source distinction only). It reflects an intentional, naturalistic **asymmetry** in the low-back vowel system — GA's lower back vowel /ɑ/ is already relatively long, while its short counterpart, schwa /ə/, is **losing phonemic status** in the dialect (author analysis, [Provisional]; `phonology.md`). A robust /ɑ/ with a fading short counterpart and a not-yet-needed long /ɑː/ is the kind of gap natural vowel systems show. The long /ɑː/ slot (future `aa`) stays **deferred** — add only when a form needs it (author decision). Companion: lexicon-wide IPA sweep of `au` entries in `dictionary.md` (changelog 2026-06-22) and the `spell2ipa.py` table update.

### v3.6, June 2026 — interpunct "ideophone-beat" use retired

§3.5's fourth bullet — the interpunct separating the "beats" of a reduplicated ideophone (added v3.4 with *rhémmen·bèm*) — is removed. Per author ruling the interpunct has no beat- or rhythm-defining function; it only disambiguates syllable division, and a reduplicated ideophone such as *rhemmemmêm* (the renamed *rhémmen·bèm*, now spelling its beats with gemination) carries no such ambiguity, so it takes no interpunct. The interpunct's other three uses (hiatus, morpheme/compound junctions, consonant-letter sequences) are unaffected. Companion edit: `ideophones.md` v1.1 §7.

### v3.5, June 2026 — `s`/`ś` voiceless-adjacency clause; word-final devoicing ruled out

§2.2 gains a fourth governing rule: a non-onset `s` immediately adjacent to a voiceless obstruent (`p t k`, including `ts`) is /s/ and stays bare `s`, generalizing the onset rule's predictability logic. This supersedes the earlier word-initial-only formulation and was confirmed by `spell2ipa.py` validation against the dictionary's cluster forms (*beusp*, *benskyi*, *bessts*, *ritsstw*). The same edit closes the open word-final-`s` question in the **opposite** direction from a devoicing rule: there is **no** general word-final devoicing — a word-final `s` is /z/, and a true final /s/ is spelled `ś`. Source: `ipa-reconciliation-note.md` Decision 1; consequent dictionary correction tracked in `dictionary.md`'s 2026-06-22 changelog.

### v3.4, June 2026 — translation-exercise round 2: ideophone and expressive-class spellings (P/O session)

§3.5 interpunct gains the **ideophone-beat** use (*rhémmen·bèm*). §2.7 records the **expressive-class spellings**: a single *t* may spell a glottal stop in ideophones (the core `tt` = /ʔ/ convention is one the class is exempt from, `phonology.md` §3.1), and the onomatopoeia-object marker *-ðs* (existing `ð` + `s`; < *this*). §3.6 logs the *riųś* "news" / *riuś* "juice" near-minimal pair (nasalization by ogonek alone); §3.7 logs the *noê* / *nóè* pitch-accent pair as a worked example of pitch/stress dissociation. Companion phonology edits in `phonology.md` v4.2. Source: `phase4-triage-saying-2026-06.md` §5.

### v3.3, June 2026 — `sh`; `ʔ` ruled out of the alphabet; marked-digraph convention

`sh` /ʃ/ adopted; `š` retired (user ruling) — `h` confirmed as the digraph-former (`rh`, `th`, `sh`). `ʔ` ruled transcription-only, never orthographic (user ruling): §2.7 rewritten, the v3 sample table's *ŕéuʔ* corrected to *ŕéutt*, the final-/ʔ/ canonical question closed in `tt`'s favor, and the pre-consonantal case (*hoʔnʔnts*) opened in its place. Marked-digraph convention stated for `oë`: a diacritic on the digraph supplants the diaeresis (*rhibôet*), paralleling dotless `ı`. Circumflex-pass scope from the dictionary session: monosyllables exempt (user); single-full-vowel words exempted by extension [Provisional].

### v3.2, June 2026 — fold hierarchy; `th`; `iu` registered

The diaeresis fold generalized to a **fold hierarchy** (ogonek > pitch > diaeresis; *bényǫ* exemplar — user decision). `th` /tʰ/ registered as the one written-aspiration exception (three-way `t/tt/th` contrast; generalization question opened in §6). `iu` /ɪː/ noted explicitly in the Vu length series (long-GOOSE reflex). Source: dictionary batches A/B review, 2026-06-12.

### v3.1, June 2026 — grapheme revision and the translation-exercise conventions

**`æ` → `ä` and `œ` → `oë`** by user decision (2026-06-12): the ligatures are retired in favor of diaeresis spellings, with the **diaeresis fold** committed alongside (a pitch or quantity mark displaces the diaeresis; the base letter carries the mark; the diaeresis is recoverable). The `oë` convention **closes the *boeś* open question**: `oë` = diphthong, plain `oe` = hiatus /o.ɛ/ on the `ea` pattern, ligature retired; *boeś* respells *boëś* at the dictionary sweep. `oë` provisionally classified as the second diphthongal long vowel (with `iie`), supported by its two feeds (choice smoothing; report gliding, new in phonology v4.1). **Rhotic spelling settled** (user proposal 2026-06-10): `rh` /ɻ/ onset, `rr` /ɻ/ elsewhere (linking-*r* forms write `rr`), `r·r` by interpunct where disambiguation is needed; `rr` carved out of the §2.4 geminate convention. **Glottal-stop spelling** split by position: final `ʔ` glyph (unchanged), intervocalic-from-/t/ `tt` (*notto* /noʔo/; user decision), `tt` carved out of §2.4; the concord-final `tt` value and the generalization question opened in §6. **Interpunct policy unified** across its three attested uses (hiatus, junctions, consonant sequences). New §2.6, §2.7; §3.1, §3.4 (retitled), §3.5, §4 updated. Open questions: one closed (*boeś*), four added, one reworded (`ä`). *(Same-day addendum: word-final `tt` settled as /ʔ/ by user decision — concord forms are glottal-final; rare geminates/clusters disambiguated by interpunct; the concord-`tt` and `tt`-generalization items close, replaced by the narrower final-/ʔ/-canonical-spelling question.)*

### v3, June 2026 — conformance pass: voice, cross-document alignment, dictionary backlog

**Abstract added (second pass on this draft).** Per the stub-abstract model adopted June 2026 (skill v1.1, §1.5): an architecture-level Abstract opens the document; its copy lives in `language_reference.md` §2.

**Voice.** The document opener no longer narrates the latest revision (revision narration lives here in §7 only). Status-tag definitions and reading conventions now point at `language_reference.md` front matter. §3.3's "new pattern" phrasing for `iie` normalized to plain description (the pattern is established, not news).

**Cross-document alignment (§3.7).** The lead sentence "Pitch and stress are independent prosodic features" replaced: under the residue analysis (`phonology.md` §3.4, settled in its v2.2), pitch and stress are a redistribution of GA prominence, not independent features — the orthographic fact is that they are *marked separately*. The acute bullet's "lexically determined and not predictable from the surface form" wording updated to the sharpened "etymologically determined but not synchronically derivable" formulation, with a pointer to `phonology.md` §3.4. Marking conventions unchanged. §2.5 adopts the *prosodic appendix* disambiguation per `terminology-registry.md`.

**§6 dictionary backlog.** New open question added from dictionary work: ligature `œ` vs. letter-sequence `oe` in headwords (*boeś* — diphthong, hiatus, or error). The §2.4 /kʷː/ note gains an explicit [Open] tag pointing at §6. No question is resolved by this pass.

### v2.4, May 2026 — inventory closures propagated; dotless ı and iiy stress placement settled; predictable nasalization rule added; /kʷː/ spelling noted

**Breathy voice closed as allophonic (§1).** The design-principles entry for breathy voice now records the settled status: allophonic, not phonemic. The `VhU` disambiguation variant is not adopted.

**Short vowel `a` (§3.1).** Simplified from `/ɑ/ ~ /ɔ/` (range, under analysis) to `/ɑ/`. The /ɑ~ɔ/ variation is allophonic. Parallel to the /ɪ~ɨ/ closure in `phonology.md` v2.3.

**Labialized geminate /kʷː/ (§2.4).** Two candidate spellings noted: `cqu` and `kkw`. Both valid; neither canonical yet. Open question added to §6.

**Predictable nasalization left unmarked (§3.6).** When glide nasalization is fully predictable from an adjacent nasalized vowel, the glide is written bare. Canonical example: *ęy* `ęy` (not `ęỹ`).

**`ii`-digraph diacritic rule and `iiy` stress placement settled (§3.7).** When a diacritic lands on one element of the `ii` digraph, the other element is written as dotless `ı`. For `iiy` /iː/: the stress grave lands on the second `i` of `ii` (not on `y`), because `y` is a semivowel recording the lengthened realization, not a vowel. The formal orthography for *Emily* is `émıiìy` (not `émiiỳ`). This resolves the conflict with the earlier dictionary-internal convention.

**§6 open questions.** Medial /h/ vs. breathy-voice question removed (closed in `phonology.md` v2.3). /kʷː/ spelling question added.

### v2.3, May 2026 — retirement-paragraph trim

**§3.7 closing paragraph removed.** The paragraph beginning "The earlier framing of pitch in terms of 'ba-DUM vs. DUM-DUM feet' is retired..." is dropped. It was the only retirement-marker in body text rather than a glossary entry, and its content is canonically held in `phonology.md` §6 glossary entries for *Spondee* and *Stress clash*. The phenomenon is described correctly in current text (§3.7 main body, `phonology.md` §3.4) as pitch-stress dissociation.

### v2.2, May 2026 — pedagogical-game references stripped

**§5 lead paragraph reworded.** The lead paragraph's references to "the earliest mini-games — the phonology game and the ice cream shop" are removed; the paragraph now motivates the diacritic-as-load-bearing claim on its own terms (drilling minimal pairs in learning materials generally). Parallel to the broader cleanup in `language_reference.md` v2.3.

### v2.1, May 2026 — diphthongal long vowels admitted

**Diphthongal long vowels (§3.3).** The `iie` digraph is admitted as a bimoraic long diphthong /iɛ/, parallel to `Vu` and `iiy` as a length-encoding digraph but with a vocalic second mora rather than a smoothed-schwa or glide-source second graph. This generalizes the long-vowel system: long vowels are bimoraic nuclei of two surface types (monophthongal and diphthongal). Forced by the topic-particle paradigm in `language_reference.md` §3.7 (the article-bearing form of the visibility particle *hii* /hi/ "see" is *hiie* /hiɛ/). The IPA convention is clarified in §1: the colon is dropped for diphthongal long vowels because the second graph's vowel quality supplies the length-marking work.

**New open question on phonemic medial /h/ (§6).** The fossilized topic particles `noho` /noho/ and `hiho` /hiho/ (see `language_reference.md` §3.7) attest genuine medial /h/ between vowels. Whether this is phonemically distinct from breathy voice (currently the sole reading of `VhV`) is undecided; a candidate disambiguation (`VhV` for consonantal /h/, `VhU` for breathy voice) is sketched without commitment. Contextual disambiguation suffices for now.

### v2, May 2026 — pitch-revision integration and dictionary-batch closures

**Pitch-stress system (May 3 integration).** The acute/grave/circumflex three-diacritic system on vowels (§3.7) is integrated into the orthography document. v1 had used "ba-DUM vs. DUM-DUM" foot framing and proposed stacked diacritics for pitch+nasalization clash; both are retired. The current system reflects the May 3 pitch-stress dissociation analysis: pitch lands on the historical-GA-stress vowel, stress on the final vocalic position; the orthography marks them with separate diacritics (acute, grave) plus circumflex for coincidence.

**V₁/V₂ placement principle.** §3.6 (Nasalization) now includes the V₁-pitch / V₂-nasalization placement rule. Stacked-diacritic policy retired; clash-case fallback specified (`é` implicit or `én` explicit-etymological).

**`s` / `ś` / `ss` system (§2.2).** The `s` grapheme is now position-dependent: /s/ in onset (where there is no underlying /z/), /z/ elsewhere. `ś` is reserved for non-onset position where the contrast with /z/ is real. `ss` is the geminate /sː/ (with formal variant `śś`). v1's framing of `s` as uniformly /z/ has been refined.

**Geminate-doubling generalization (§2.4).** New section establishing that doubled consonants represent geminates: `ss` /sː/, `nn` /nː/, `pp` /pː/, with the convention generalizing to any future-attested /Cː/. v1 had no such rule; the dictionary entries *beussou*, *rhiiysseunnou*, and *epplii* forced its formulation.

**/iː/ as a phoneme; `iiy` as its spelling (§3.2).** v1 stated explicitly that "/iː/ does not occur in the conlang." This claim is retired. /iː/ is a phoneme, arising from /ɪji/-smoothing (the /ɫ/-glide-becoming pathway), and is spelled `iiy`. The spelling captures the etymological glide source. *Emily*, *rhiiynii*, and *rhiiysseunnou* all attest. The convention for /iː/ from non-glide-source pathways (if any) remains open.

**`eu` and `ou` digraphs unified across two feeds (§3.2).** The `eu` digraph now covers both the smoothed-schwa pathway (v1's only feed) and the /æ/-before-nasal pathway (via tense-/æ/-with-preserved-duration, attested in *rhiiysseunnou*). Similarly `ou` covers smoothed-schwa and the /au, or/ → /oː/ merger. The orthography unifies these without distinguishing the diachronic source.

**`ei` diphthong clarified (§3.4).** New section explicit about the contrast between `ei` (diphthong /ei/, single syllable) and `eu` (length /ɛː/). The clarification originated as a dictionary-internal note and is now propagated to the main orthography.

### v1 (pre-May 3 2026)

Original document. Established the load-bearing-diacritics philosophy, the consonant inventory and devoicing convention, the `Vu` length system, the doubled-vowel-as-hiatus rule with `ii` as exception, the tilde/ogonek nasalization split, breathy voice as `VhV`. Closed by v2 in places where the pitch revision and dictionary work forced commitment.
