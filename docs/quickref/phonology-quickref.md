# Phonology Quick Reference

*Extracted from `phonology.md` v4.6. Tables only — no prose. Rebuild via `skills/quickref-updater.md` after any §4 revision. §4.4 is now a named-rule **registry** organized by family; legacy IDs (E1–E5, M1, C-Coal, R-Assim, S1–S3) are valid aliases.*

## 4.3 The cascade (CVCVC)

Notation: **C₀ V₁ C₁ V₂ C₂**.

| Step | Rule | Condition | Output |
|---|---|---|---|
| 1a | soft-six hollowing (E1): elide C₁ | C₁ ∈ {ɾ, dʒ, n, j, g, v} | C₀ V₁ V₂ C₂ → step 2 |
| 1b | the wandering r (M1): relocate C₁ if /ɻ/ | C₁ = /ɻ/ AND C₀ ∈ {/h/, ∅} | rhotic → onset; /h/ → devoicing → /r̥/; hiatus → step 2 |
| 1c | wandering r blocked / no rule | C₁ = /ɻ/ but C₀ other; or C₁ in no set | unchanged → step 4 |
| 2 | smoothing | (a) one V is /ə/, or (b) Vs articulatorily close | C₀ V₁ː C₂ |
| 2 | hiatus retention | neither smoothing condition | hiatus kept; stress on final V |
| 3 | stranded schwa (Emma landing) | V₂ = /ə/ in open syllable | ə → a |
| 4 | schwa crush (E3): elide V₂ | V₂ ∈ elision set, locus not vacated | C₀ V₁ C₁ C₂ → step 5 |
| 5 | syllabic promotion | C₁/C₂ syllabic-eligible | C₀ V₁ C₁ C̩₂ (foot + appendix) |
| 6 | the coda purge (E2a–d) | C₂ subject to coda rules | varies (§4.4.11) |
| 7 | final-V: Emma landing / final-glide settling | V₂ ∈ {e,a,ə} / {i,o} | ə→a / reduce to /j̩, w̩/ |
| 8 | alveolar-wins (R-Assim) | word has both /ɻ/ and /ɾ/ | /ɻ/ → /ɾ/ throughout |

Dactyl (CVCVCVC) enters the same cascade; where elision fails, the three-vowel shape is retained and stress falls on V₃.

## 4.4 Sound-change registry

Status: **[S]** Settled · **[P]** Provisional · **[O]** Open. Stratum in parentheses.

### 4.4.1 The rough-breathing family
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| s-breathing | /s/ → /h/ in most positions | 1 | S |
| k-breathing | onset /k/ → /h/ | 1 | S |
| the cluster shield | debuccalization blocked when /s/ heads an onset cluster (/sp/, /sk/) | 1 | S |
| cute-and-quick fortition | /h/ → [k] before a glide (surface [kj, kw] = allophonic /hj, hw/) | 8 | P |

### 4.4.2 The soft six
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| soft-six tapping | /d, dʒ, n, j, g, v/ → /ɾ/ (tap) in onset | 1 | S-core |
| soft-six hollowing (E1) | /ɾ, dʒ, n, j, g, v/ delete intervocalically | 2 | S |

### 4.4.3 The whispered r / rhotic instability
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| kr-whispering | /kr/ → /ɾ̥/ | 1 | S |
| the wandering r (M1) | intervocalic /ɻ/ → onset; with /h/-onset → /ɾ̥/, empty onset → /ɻ/; else blocked | 2 | S-core/O-edges |
| today coalescence (C-Coal) | /h/ + /ɾ,ɻ/ adjacent in onset → /ɾ̥/ | 2 | S |
| tap–rhotic dissimilation | /ɻ/ elides when the preceding onset is a tap | 2 | P |
| linking r | stem-final vocalized rhotic resurfaces as ⟨rr⟩ (=/ɻ/) before a V-initial suffix (rhotic special case of the fossil resurrection, §4.4.14) | morphophon. | S |
| alveolar-wins (R-Assim) | word with both /ɾ/ and /ɻ/ → /ɻ/ assimilates to /ɾ/ | 8 | S |

### 4.4.4 Glide hardening
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| w-hardening | /w/ → /ɻ/ | 1 | S |
| the reluctant yod | /j/ → /ɻ/ in restricted contexts (conditioning uncommitted) | 1 | O |
| dark-l vocalization | /ɫ/ → /j/ adjacent a front vowel; → /ɻ/ (→/ɾ/) elsewhere | 1 | S-core (/j/ P) |

### 4.4.5 The labial funnel
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| bat-mat merger | /m/ → /b/ in onset (unconditional) | 1 | S-core |
| pass-out voicing | singleton onset /p/ → /b/ before /ɛ, ɛː/ (any position) & word-medially before any V | 1 | P |
| prep-breaking | word-initial /pr/ → /bɑˈɾ̥/ ⟨baŕ⟩ (epenthetic /ɑ/, /p/→/b/, rhotic → devoiced /ɾ̥/); /br/ = voiced sibling (rhotic stays /ɻ/, *bridge*→*baurrits*) | 1 | S-core (cross-cluster O) |

### 4.4.6 Ambisyllabic gemination
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| pass-out gemination | /s/ (and /st/) → /sː/ at a syllable boundary preceding stress | 1 | S |
| labial gemination | ambisyllabic /pp/ → /pː/ (formerly "apply gemination"; sole witness *epplii* reanalyzed away — now unattested) | 1 | P |

### 4.4.7 Other consonantal changes
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| fin-thin merger | /f/ → /θ/ | 1 | S |
| the Rochester flip | /st/ → /ts/ | 1 | S |
| cherish tapping | /tʃ/ → /ɾ̥/ in a stressed-syllable onset | 1 | P |
| ch-funnelling | /tʃ/ → /ts/ outside stressed onsets | 1 | P |
| stand-out leveling | coda /nd/ → /nː/ (regressive assim. then geminate) | 1 | S |
| the really glide | dark [ɫ] → /j/ between high front vowels (feeds /ɪji/→/iː/) | 1 | S |
| the -er tail | word-final /ɚ/ (*-er*) → syllabic /w̩/ in appendix | 6 | P |
| though-elision | /ð/ → ∅ in all positions | 1 | S |
| the dishes clip | recognitional *the* procliticizes; stranded /ð/ → /θ/ ⟨þ⟩ (or /i/ ⟨y⟩ prevocalic) | 1 | P |

### 4.4.8 Vocalic mergers
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| goose-foot-strut merger | /u, ʊ, ʌ/ → /ɨ/ (~/ɪ/); long /u/ → /ɨː/ | 1 | S |
| the price splinter | /ai/ → /eː/ ~ /i/ ~ /ɛ/ (conditioning undetermined) | 1 | O |
| mouth-north merger | /au/ → /o(ː)/ (NORTH half superseded by report gliding) | 1 | S |
| report gliding | /ɔr/ → /oe/ (coda de-rhotacization) | 1 | S |
| trap-square merger | /æ, er/ → /eː/ | 1 | S |
| the stand-out vowel | tensed /æ/ before a nasal → /ɛː/ | 1 | S-core |
| choice smoothing | /ɔɪ/ → /oe/ | 1 | S |

### 4.4.9 The three fates of schwa
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| schwa swallowing (E4) | schwa adjacent to a vowel is absorbed by smoothing | 3 | S |
| schwa crush (E3) | unstressed schwa elides where its locus is not vacated | 4 | S |
| schwa strengthening (E5) | final stranded /ə/ → /a/ (Emma landing); initial unstressed /ə/ → /ɛ/ (apply onset) | 6 | S |

### 4.4.10 Vowel resolution and residues
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| squeaky prothesis | prothetic /o/ before an /s/+stop onset | 1 | P |
| smoothing | hiatus vowels merge to a long vowel when (a) one is /ə/ or (b) close | 3 | S |
| syllabic promotion | consonant stranded by crush → syllabic nucleus (post-stress = appendix) | 4 | P |
| final-glide settling | final unstressed /i, o/ (and goose-/u/) → syllabic /j̩, w̩/ | 6 | S-core |

### 4.4.11 The coda purge
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| coda glottaling (E2a) | coda /t/ → /ʔ/ | 5 | S |
| need-clipping (E2b) | coda /d/ → ∅ (no compensatory lengthening) | 5 | S |
| total l-loss (E2c) | singleton coda /l/ → ∅ (multi-path) | 5 | O |
| coda k-loss | coda /k/ → ∅ (blocked by labial rescue) | 5 | S |
| labial rescue | coda /k/ + adjacent /w/ → onset /kʷ/ (ambisyllabic → /kʷː/) | 5 | S (morphophon. ext. S — §4.4.14) |
| the glottal anchor (E2d) | coda /ʔ/ doesn't elide; exception: out-drop in grammaticalized particles | 5 | S (junction O) |

### 4.4.12 Suprasegmental residues and prosody
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| nasal ghosting (S1) | /n/-elision transfers nasality to adjacent vowels (V₂ marked) | rider/2 | S |
| breath ghosting (S2) | breathy voice from elided /h/ or weakened obstruents | rider | P |
| pitch stranding (S3) | pitch lands on the GA-primary-stress syllable | 7 | S (contrastiveness O) |
| final landing | stress assigned to the final vocalic position (right-headed foot) | 7 | S |

### 4.4.13 Junction phonology — [Open stubs]
junction welding (/ʔk/ → /kʷː/ at seams) · **and-went gemination** (/nw/ → /mː/ ⟨mm⟩ at *and+went*; **P**, best-attested) · the coffee shield (welded /kː/ counterbleeds breathing) · the junction drop (coda /ʔ/ loss at junctions) · the linker question (*-e-* combining form) · compound prominence.

### 4.4.14 Inflectional morphophonology — the fossil resurrection
| Rule | Statement | Stratum | Status |
|---|---|---|---|
| the fossil resurrection | under inflection a suppressed GA coda resurfaces, re-syllabifies as onset, re-runs the stratum-1 onset lenitions (*click*→*kli* but PROG *klihıĩ*); inflected form keyed to GA coda | morphophon. | S |
| PROG exponent | progressive-shaped concord = suffix /‑ıĩ/ (< GA *-ing*) | morphophon. | S |
| PRET exponent | preterite/perfect = coronal /‑ɾi ~ ‑t/; strong-verb class keeps GA morphology | morphophon. | S |
| concord infix | in phrasal/object stems the increment infixes at the root–particle seam (PROG ‑n‑, PRET ‑t‑) | morphophon. | S |

Special cases registered elsewhere: **linking r** (§4.4.3, rhotic reflex), **labial-rescue extension** (§4.4.11, /k/→/kʷ/). Full coda-class paradigm: `verbal-system.md` §4.2.2.

### 4.4.15 Pending
**the sodium coloring** [O]: labial /m/ colors a preceding schwa to /o/, then /m/ elides (*sodium* → *hoiiǫ*); proposed for all *-ium*.

### 4.4.16 Retired
clack-to-tlack (/kl/ → /tl/) — removed v4 (no attestations).
