# Orthography

**Version:** v2.4 (May 2026)
**Predecessor:** v2.3 (retirement-paragraph trim); v2.2 (pedagogical-game references stripped); v2.1 (diphthongal long vowels admitted); v2 (pitch-revision integration and dictionary-batch closures); v1 (original).

This v2.3 revision trims a redundant retirement paragraph from §3.7 — the "ba-DUM vs. DUM-DUM feet" framing was already retired across the body of the document, with the canonical retirement record kept in `phonology.md` §6 glossary entries (*Spondee*, *Stress clash*). Specific changes are listed in §7 (Versioning Notes).

A dedicated reference for the conlang's writing system. The orthography uses Latin script with load-bearing diacritics in the manner of Vietnamese — diacritics are not decorative, and ignoring them collapses minimal pairs.

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
| `rh` | /ɻ/ | Retroflex approximant. Digraph. |
| `þ` | /θ/ | Thorn. |
| `ð` | /ð/ | Eth. |
| `y` | /j/ | Palatal approximant. Not a vowel. |
| `w` | /w/ | Labio-velar approximant. Occurs almost exclusively in consonant clusters; most GA /w/ either merged with `rh` /ɻ/ or elided. |

Other consonants (`b`, `t`, `k`, `l`, `h`, `n`, `m`, etc.) take their expected IPA values. Recall from `phonology.md` that `k` and `l` occur only in clusters, and `h` is the regular reflex of GA /s/ in most positions. Aspiration on voiceless stops is allophonic (English-style: aspirate in stressed onsets) and is not represented orthographically.

### 2.2 The `s` / `ś` / `ss` system

The interaction of the `s` graphemes is one of the orthography's more subtle points. Three rules govern it:

**Onset `s` is /s/.** Onset `s` derives only from the GA /st/ → /s/ pathway (GA /s/ having debuccalized to /h/ in onset elsewhere). There is no underlying /z/ in onset, so onset `s` is unambiguously /s/. The `ś` grapheme is therefore not used in onset position; the explicit-devoicing mark adds no information.

**Non-onset `s` is /z/.** Intervocalic and final `s` represents /z/ by default. To mark a voiceless /s/ in these positions, write `ś`.

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

Geminates arise from two diachronic feeds (see `phonology.md` §2.1): phonologization of GA ambisyllabic consonants in stressed-second-syllable environments (*beussou*, *epplii*), and cluster collapse such as /nd/ → /nː/ by regressive assimilation (*rhiiysseunnou*).

The convention generalizes: any future-attested geminate /Cː/ is spelled `CC`. This is independent of the `Vu` length convention for vowels, which uses an explicit second letter rather than doubling.

**Labialized geminate /kʷː/.** A special case: the labialized geminate /kʷː/ (attested in *nocquıî* < *not quite*) has two candidate spellings. **`cqu`** treats the combination as `c` (first /k/) + `qu` (/k/ + labial /w/); **`kkw`** treats it as doubled `kk` (geminate) + `w` (labial). Both are valid; neither is yet canonical. [Open: standardize one spelling.]

### 2.5 Approximants and syllabicity

Per `phonology.md` §3.5, complex consonant clusters — including syllabic ones — can occur in appendix position after the stressed final vowel of a word. This means `y` /j/ and `w` /w/ can appear in syllabic position post-vocalically.

Phonetically, a syllabic /j/ in such a position can be near-indistinguishable from an unstressed /i/, and a syllabic /w/ from an unstressed /o/. *Phonemically* they remain consonants: their distribution is governed by consonantal phonotactics (occurring in cluster positions, after the stressed nucleus), not by the vowel-distribution rules. The parallel is to Proto-Indo-European, whose approximants likewise had vowel-like syllabic realizations that complemented a minimal vowel inventory while remaining phonemically consonantal.

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
| `æ` | /æ/ | Residual /æ/ — did not fully collapse into /eː/. |
| `œ` | /oe/ | The diphthong /oe/, monosyllabic. |

Note that bare `u` does **not** occur as a grapheme: it appears only as the second element of a length digraph (§3.2). And `y`, despite the visual resemblance to an `i`-ish letter, is the consonant /j/ (§2.1), not a vowel.

### 3.2 Long vowels: `Vu` digraphs and `iiy`

Long vowels are written with explicit-second-letter digraphs, never by doubling. There are two graphemic patterns: `Vu` for the four long vowels whose source is smoothed-schwa (or related vocalic reanalysis), and `iiy` for /iː/.

#### The `Vu` digraphs

| Grapheme | IPA | Source |
|---|---|---|
| `au` | /ɑː/ | smoothed `a` + ə |
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

**/i.a/ hiatus** is written `iia`: the first syllable is the gliding /i/ (`ii`), and `a` follows directly. A new pattern, **`iie` /iɛ/**, attests a third row in the analysis: `ii` plus `e` marks neither hiatus nor a short diphthong, but a *bimoraic long diphthong* — a length pattern parallel to `Vu` and `iiy`, in which the second graph (`e`) supplies a distinct vowel quality rather than smoothing into pure length. The full contrast:

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

The form `ea` reflects a sound rule rather than just an orthographic convention: historical /ɪ.a/ does not occur, having lowered to /e.a/. The orthography records the surface form. A consequence: the spelling `ia` is unambiguously the diphthong, never a hiatus form.

### 3.4 The `ei` diphthong

The diphthong /ei/ is written `ei`. Phonemically /ey/ (with `y` /j/ as the glide), it is a single syllable.

This grapheme is distinct from the length digraph `eu` /ɛː/ (§3.2): `e` followed by `i` is the diphthong, `e` followed by `u` is length. The contrast is real and the spelling distinguishes them cleanly.

### 3.5 The interpunct as optional disambiguator

In pedagogical or formal-register text, an interpunct may be inserted to make hiatus explicit:

- `a·a` for /a.a/
- `o·o` for /o.o/
- `ii·a` for /i.a/

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

Pitch and stress are independent prosodic features (see `phonology.md` §3.3–3.4) and are marked separately on the orthography. **Three diacritics on vowels** handle them:

- **Acute (`´`) on a vowel** — pitch accent. Always written, in casual and formal register alike, because pitch is lexically determined and not predictable from the surface form.
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
| *carrot* | /r̥eːʔ/ | `ŕéuʔ` | `ŕêuʔ` | /eː/ | /eː/ (coincide) |
| *barn* | /beːn/ | `béun` | `bêun` | /eː/ | /eː/ (coincide) |

Monosyllables have pitch and stress on the only available vowel — circumflex in formal register, plain acute in casual.

Multisyllables typically dissociate, with pitch on the historical-GA-stress syllable and stress on the new final position.

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
| `Vu` digraph | — | Length: `au eu iu ou` |
| `iiy` digraph | — | Length: /iː/ from /ɪji/-smoothing |
| `ei` digraph | — | Diphthong /ei/ |
| `h` between vowels | — | Breathy voice: `VhV` |
| Interpunct (`·`) | — | Optional hiatus disambiguator (formal register) |
| Digraph | `rh` /ɻ/ | — |
| Special letters | `þ ð` | `æ œ` |

---

## 5. Pedagogical Implication

Because diacritics and digraphs are load-bearing, learning materials must drill minimal pairs distinguished only by these marks. A learner who treats diacritics as ornamental will collapse pairs the language treats as fully distinct.

The richest minimal-pair territories are:

- `s` vs. `ś` (/z/ vs. /s/) in non-onset position
- `s` (single) vs. `ss` (geminate) — singleton vs. geminate
- `r` vs. `rh` (/ɾ/ vs. /ɻ/)
- `i` vs. `ĩ`, `a` vs. `ą`, etc. (oral vs. nasal)
- `a` vs. `au` (short vs. long), and the cross-cutting `aa` (hiatus) vs. `au` (length) contrast
- `ia` vs. `iia` vs. `ea` (diphthong vs. /i/-initial hiatus vs. lowered /ɪ/-initial hiatus)
- `ei` vs. `eu` (diphthong /ei/ vs. length /ɛː/)
- `ii` vs. `iiy` (short tense /i/ vs. long /iː/)
- Pitch-placement contrasts on otherwise homographic forms (acute on V₁ vs. acute on V₂, etc.)

---

## 6. Open Questions

- **Spelling convention for /iː/ outside the etymological-glide environment.** Working rule is `iiy` where there's a glide source; the convention for /iː/ from other pathways (if any are attested) is undecided. Bare `ii` for non-glide-source /iː/, or extension of `iiy` by analogy?
- **Standardization of /kʷː/ spelling.** Both `cqu` and `kkw` are valid (see §2.4). Which becomes canonical is open.
- **Whether the interpunct will eventually become obligatory** in any context, or remain a register feature.
- **Treatment of `æ` in environments where it borders on /eː/** — whether the orthography preserves the etymological `æ` or follows the surface form.
- **Whether genuine clash cases** (short vowel carrying both pitch and nasalization, with no V₂ to host the nasal mark) actually occur in the lexicon. If so, whether the implicit (`é`) or `Vn` (`én`) route should become the default.

---

## 7. Versioning Notes

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
