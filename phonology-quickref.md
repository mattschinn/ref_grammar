# Phonology Quick Reference

*Extracted from `phonology.md` v2.4. Tables only — no prose. Rebuild via `skills/quickref-updater.md` after any §4 revision.*

---

## Cascade: CVCVC

| Step | Rule | Condition | Output |
|---|---|---|---|
| 1a | E1: elide C₁ | C₁ ∈ {ɾ, dʒ, n, j, g, v} | C₀ V₁ V₂ C₂ → step 2 |
| 1b | M1: relocate C₁ | C₁ = /ɻ/ AND C₀ ∈ {/h/, ∅} | rhotic → onset; /h/ → devoicing → /r̥/; hiatus created → step 2 |
| 1c | M1 blocked / no rule | C₁ = /ɻ/ with other onset; or C₁ not in any set | unchanged → step 4 |
| 2 | Smoothing | one participant is /ə/, OR vowels articulatorily close | C₀ V₁ː C₂ |
| 2 | Hiatus retention | neither smoothing condition met | hiatus preserved; stress on final V |
| 3 | Stranded schwa | V₂ = /ə/ in resulting open syllable | ə → a |
| 4 | E3: elide V₂ | V₂ ∈ elision set; intervocalic position not vacated | C₀ V₁ C₁ C₂ → step 5 |
| 4 | E3: skip | otherwise | → step 6 |
| 5 | Syllabic-C promotion | C₁ or C₂ ∈ syllabic-eligible | C₀ V₁ C₁ C̩₂ (foot + appendix) |
| 6 | E2 family: coda treatment | C₂ subject to coda rules | see E2a–E2d below |
| 7 | Final-V resolution | V₂ ∈ {e, a, ə} | ə → a |
| 7 | Final-V resolution | V₂ ∈ {i, o} | → syllabic /j, w/ |
| 8 | R-Assim | word has both /ɻ/ and /ɾ/ | /ɻ/ → /ɾ/ throughout |

---

## §4.4.1 Consonantal Mergers and Shifts

| GA source | Conlang reflex | Notes |
|---|---|---|
| /s/ | /h/ in most positions | Debuccalization. |
| /s/ | /sː/ at syllable boundary preceding stress | Beats debuccalization in this environment. **[New in v2]** |
| /s/ (onset cluster) | /s/ | Debuccalization blocked in cluster position. **[New in v2.4]** |
| /st/ | /ts/ | |
| /k/ (onset) | /h/ | Joins /s/ in debuccalization. |
| /k/ (coda) | ∅ | Lost outright. |
| coda /k/ + /w/ | /kʷ/ (onset) | Labialization; blocks coda /k/→∅. Geminate /kʷː/ if ambisyllabic. **[New in v2.4]** |
| /kr/ | /r̥/ | /k/ devoices the rhotic and merges in. |
| /kl/ | /tl/ | Stop place shifts; cluster preserved. |
| /kj, kw/ | [kj, kw] | Surface intact; analyzed as allophonic /hj, hw/. **[Provisional]** |
| /d, dʒ, n, j, g, v/ | /r/ (tap) | Massive merger. /n/-merger conditional (can also elide with nasal coloring). |
| /m, p/ | /b/ (in onset) | Merger into voiced labial. |
| /p/ | /b/ before /ɛ, ɛː/ in onset | Blocked before /i, ɪ, ɑ, o/ and consonant clusters. **[New in v2]** |
| /pp/ ambisyllabic | /pː/ | Phonologization of GA ambisyllabic /p/. **[New in v2]** |
| /f/ | /θ/ | |
| /w, j/ | /ɻ/ | Then /ɻ/ → /ɾ/ near another /ɾ/ (R-Assim). |
| /nd/ in coda | /nː/ | Regressive assimilation. **[New in v2]** |
| /ɫ/ between high front vowels | /j/ | Feeds /ɪji/ → /iː/ smoothing. |

---

## §4.4.2 Vocalic Mergers

| GA source | Conlang reflex |
|---|---|
| /u, ʊ, ʌ/ | /ɨ/ (possibly further to /ɪ/) |
| /ai/ | multiple outputs; conditioning **[Open — data-gathering bucket, see §5]** |
| /au, or/ | /o(ː)/ |
| /æ, er/ | /eː/ |
| /æ/ before nasal | /ɛː/ (long; tense-/æ/-with-preserved-duration pathway) |
| /ɔɪ/ | /oe/ **[New in v2.4; see *bœ*, *boeś*, *nœ*]** |
| /u/ (long pathway) | /ɨː/ |
| /ə/ (final) | /a/ when stranded in open syllable; absorbed when adjacent to vowel; elides in cluster-feeding position |
| /ə/ (initial unstressed, surviving) | /ɛ/ **[New in v2]** |

---

## §4.4.3 Elision Rules

| Rule | Trigger | Output | Notes |
|---|---|---|---|
| E1 | /ɾ, dʒ, n, j, g, v/ intervocalic | segment elided; /n/ leaves nasalization on adjacent vowels | Feeds vowel resolution. **[Settled]** |
| E2a | coda /t/ | /ʔ/ | Productive across lexicon. **[Settled]** |
| E2b | coda /d/ | ∅ | No compensatory lengthening. **[Settled in v2]** |
| E2c | coda /l/ (singleton) | ∅ (multi-path) | Full set of paths **[Open]**. Cluster /l/ exempt. |
| E2d | coda /ʔ/ | stable — no elision | Exception: lexical /ʔ/-drop in grammaticalized particles (e.g., *out*). **[Settled in v2]** |
| E3 | schwa in unstressed position | ∅ | Blocked by prior E1 or M1 at same locus. Feeds cluster formation. |
| E4 | schwa adjacent to another vowel | absorbed by smoothing | |
| E5 | final stranded /ə/ in open syllable | /a/ | Initial unstressed surviving /ə/ → /ɛ/ (parallel pathway). **[Partly new in v2]** |

---

## §4.4.4 Rhotic Rules

| Rule | Trigger | Output | Notes |
|---|---|---|---|
| M1 | intervocalic /ɻ/; onset = /h/ | /ɻ/ → onset; /h/ → devoicing feature → /r̥/ | Core **[Settled]**; edges (what counts as intervocalic) **[Open]** |
| M1 | intervocalic /ɻ/; onset = ∅ | /ɻ/ → plain onset | |
| M1 blocked | any other onset | /ɻ/ stays; does not elide, does not → /ɾ/ | |
| C-Coal | /h/ + /ɾ/ or /ɻ/ directly adjacent in onset | /h/ → devoicing feature → /r̥/ | Sister rule to M1. **[New in v2]** |
| R-Assim | word contains both /ɻ/ and /ɾ/ | /ɻ/ → /ɾ/ throughout | Fires after M1 and C-Coal. **[Settled]** |

---

## §4.4.5 Suprasegmental Rules

| Rule | Trigger | Output | Status |
|---|---|---|---|
| S1 | /n/ elides (E1) | nasality transfers to adjacent vowels (V₂ by default) | **[Settled]** |
| S2 | coda /h/ or weakened obstruents elide | breathy voice on adjacent vowel | **[Provisional]** |
| S3 | always | pitch lands on syllable of GA primary stress; stress lands on final vocalic position | Placement **[Settled]**; contrastiveness **[Open]** |
