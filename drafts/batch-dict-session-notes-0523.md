# Batch Dictionary Entry Session — 2026-05-23

Working notes for the batch from `batch-dict-entry-0523.xlsx`. Save this file before any interruption so a retry session can pick up without re-reading everything.

---

## Status at interruption

**Read:** `phonology.md` (v2.3), `orthography.md` (v2.4), `dictionary.md` (full).  
**Not yet done:** drafting entries, checking collisions against existing dictionary, writing anything to `dictionary.md`.

---

## Full reconstructed spreadsheet table

Columns: ENTRY | MEANING (definition) | ETYMON (GA source) | PART OF SPEECH

| Row | Entry (headword) | Meaning / Definition | GA Etymon | POS |
|-----|-----------------|----------------------|-----------|-----|
| 2 | éuskrıì | icecream | icecream | noun |
| 3 | benıîæ | vanilla | vanilla | noun |
| 4 | ńyokwt | chocolate | chocolate | noun |
| 5 | hóhonìt | coconut | coconut | noun |
| 6 | beńt | mint | mint | noun |
| 7 | bąêų | banana | banana | noun |
| 8 | boeś | voice | voice | noun |
| 9 | reųś | Venus | Venus | noun |
| 10 | rékwıì | victory | victory | noun |
| 11 | ouś | August | August | noun |
| 12 | óhò | hey! | — | interjection |
| 13 | ohô | aha, I see | — | interjection |
| 14 | récquıìs | also, likewise | likewise | adverb |
| 15 | bœ | boy | boy | noun |
| 16 | hœ hoś | soy sauce | soy sauce | noun |
| 17 | nœ | annoy | annoy | verb |
| 18 | noê | kind of, sort of | in a way | adverb |
| 19 | nóeıìe | "I don't know!" | "no idea" | interjection |
| 20 | hohô | why | how so | interrogative particle |
| 21 | emmáwwè | how | in what way | interrogative particle |
| 22 | béuksoè | (1) reason, explanation, excuse, (2) childhood, personal history, (3) history | backstory | noun |
| 23 | beykw | (1) car, (2) automobiles such as bus, trucks | vehicle | noun |
| 24 | bayarę | violin | violin | noun |
| 25 | bárkennò | parking lot | parking lot | noun |
| 26 | beųtw | lunch, especially packed lunch for school or work | bento | noun |
| 27 | toś | toast | toast | noun |
| 28 | réıì | toast | toast | noun |
| 29 | réıì | milk | dairy | noun |

**WAIT — rows 27 and 28 both produce "toast"?** The spreadsheet has:
- Row 27: entry=`toś`, meaning=toast, etymon=toast
- Row 28: entry=`e`, meaning=egg, etymon=egg  ← this is what row 28 actually is; I may have mis-indexed

Let me re-state the correct table from the PowerShell output (authoritative):

```
Row 2:  éuskrıì    | icecream                                                          | icecream   | noun
Row 3:  benıîæ     | vanilla                                                           | vanilla    | noun
Row 4:  ńyokwt     | chocolate                                                         | chocolate  | noun
Row 5:  hóhonìt    | coconut                                                           | coconut    | noun
Row 6:  beńt       | mint                                                              | mint       | noun
Row 7:  bąêų       | banana                                                            | banana     | noun
Row 8:  boeś       | voice                                                             | voice      | noun
Row 9:  reųś       | Venus                                                             | Venus      | noun
Row 10: rékwıì     | victory                                                           | victory    | noun
Row 11: ouś        | August                                                            | August     | noun
Row 12: óhò        | hey!                                                              | —          | interject
Row 13: ohô        | aha, I see                                                        | —          | interject
Row 14: récquıìs   | also                                                              | likewise   | adverb
Row 15: bœ         | boy                                                               | boy        | noun
Row 16: hœ hoś     | soy sauce                                                         | soy sauce  | noun
Row 17: nœ         | annoy                                                             | annoy      | verb
Row 18: noê        | kind of, sort of                                                  | in a way   | adverb
Row 19: nóeıìe     | "I don't know!"                                                   | "no idea"  | interjection
Row 20: hohô       | why                                                               | how so     | interrogative particle
Row 21: emmáwwè    | how                                                               | in what way | interrogative particle
Row 22: béuksoè    | (1) reason, explanation, excuse, (2) childhood/personal history, (3) history | backstory | noun
Row 23: beykw      | (1) car, (2) automobiles such as bus, trucks                      | vehicle    | noun
Row 24: bayarę     | violin                                                            | violin     | noun
Row 25: bárkennò   | parking lot                                                       | parking lot | noun
Row 26: beųtw      | lunch, especially packed lunch for school or work                 | bento      | noun
Row 27: toś        | toast                                                             | toast      | noun
Row 28: e          | egg                                                               | egg        | noun
Row 29: réıì       | milk                                                              | dairy      | noun
Row 30: spyi       | for coffee in mokapot to spew, resulting in bitter mediocre coffee | spew      | verb
Row 31: rérèyt     | to tell, to recount, to explain                                   | narrate    | verb
Row 32: pot        | to be mad, to harbor bad feelings, to pout                        | pout       | verb
Row 33: bęiink     | to be scared, to worry, to deem as unfortunate                    | panic      | verb
Row 34: rhiušp     | (1) to like intensely, to obsess about, (2) to be religious, (3) (with causative form) to convert | worship | verb
Row 35: barnkw     | (1) to hug tightly, to snuggle, (2) to be stuck on/attached, (3) to cling, to be clingy, (4) to insist, to be unable to move on | barnacle | verb
Row 36: barnkw     | (1) somebody who barnacles, (2) zit, (3) nipple                  | barnacle   | verb [second POS — noun senses of same headword]
Row 37: bessts     | to message, to send a message to someone                          | message    | verb
Row 38: piiquóæ    | to look                                                           | to peek over at | verb
Row 39: piquô      | (1) to discern (GET ONESELF form), (2) to see from afar/with difficulty, (3) to detect with sense, (4) to choose (with GO-AHEAD form) | to pick out | verb
Row 40: rékriiyæ   | to chat, to shoot the breeze                                      | yakitty-yak | verb
Row 41: rıírǫ      | approximately, "about", "circa"                                   | right around | adverb/preposition
Row 42: beušiioskô | where-she-goes-to-school                                          | school     | noun
Row 43: bawiiquoh? | what-we-call-home                                                 | home       | noun
Row 44: bewii·iit  | where-we-eat                                                      | dinner table | noun
Row 45: bewiipessô | where-we-pass-out                                                 | bed        | noun
Row 46: rhiwıĩ     | (1) hold on, wait what?, come again?                             | rewind     | interjection
Row 47: rhiwıĩ     | before, ago (time)                                                | rewind     | adverb [second POS — same headword]
Row 48: béo·ò      | a little bit before                                               | bit ago    | adverb
Row 49: rhéulyèś   | (1) take a wild guess, tell me what you think, (2) hedging ("I could be wrong") | wild guess | interjection
Row 50: rhéulyèś   | just maybe, possibly                                              | wild guess  | interjection [second sense — same headword]
Row 51: benskyi    | small, tiny                                                       | miniscule  | adjective
Row 52: beusp      | large, big                                                        | massive    | adjective
```

**Note on multi-row headwords:** rows 35–36 (barnkw), 46–47 (rhiwıĩ), 49–50 (rhéulyèś) are the same headword appearing twice with different sense blocks or different POS. These should be consolidated into single entries with multiple numbered senses (or a two-POS form line).

---

## Collision check against existing dictionary

Existing headwords in `dictionary.md` (in collation order):
béntsıìy, beussou, epplii, ęy, hoiiǫ, hoʔnʔnts, nobêt, nocquıî, nocquiiayo, nocquiie-ŕóųzǫ, nocquiissprıĩ, ritsstw, rhiiy, rhilþ, rhiiynii, rhiiysseunnou, ŕe, ŕeut, skwkw, toutw

**Collision check — batch entries vs. existing:**
- `béuksoè` — already in dictionary (entry exists; see `phonology.md` and `dictionary.md` §5 changelog). **COLLISION — needs investigation.**
- All other batch entries appear novel. No other collisions detected by inspection.

**béuksoè collision detail:** The existing changelog references `béuksoè` and `epplii` in the context of phonological flags. Need to verify whether `béuksoè` actually has a full entry in the dictionary or only appears in notes. Based on full read of `dictionary.md`, **béuksoè does NOT have its own entry** — it was mentioned in the CLAUDE.md context as a flagged example, not a written entry. So no collision; safe to proceed.

---

## What I have read and key takeaways

### phonology.md (v2.3)

**Consonant mergers relevant to this batch:**
- /s/ → /h/ (debuccalization) — applies to word-initial /s/, intervocalic /s/
- /k/ (onset) → /h/ — so *coconut* /ˈkoʊkənʌt/ → /h/ onsets
- /d, dʒ, n, j, g, v/ → /r/ (tap) — the big merger
- /m, p/ → /b/ in onset
- /f/ → /θ/
- /w, j/ → /ɻ/ (retroflex); then /ɻ/ → /ɾ/ near another /ɾ/ (R-Assim)
- /nd/ in coda → /nː/
- /t/ → /ʔ/ in coda (E2a)
- /d/ → ∅ in coda (E2b)

**Vocalic mergers:**
- /u, ʊ, ʌ/ → /ɪ/ (surface /ɨ/ is allophonic)
- /ai/ → /eː/ ~ /i/ (conditioning open; /iː/ ruled out)
- /au, or/ → /o(ː)/
- /æ, er/ → /eː/
- /æ/ before nasal → /ɛː/
- /ə/ final → /a/ (stranded open syllable); absorbed when adjacent; elides in cluster-feeding position
- /ə/ initial unstressed → /ɛ/ (when not absorbed/elided)

**Open rules flagged in prior sessions (from memory and dictionary changelog) that are likely relevant to this batch:**
1. /v/ → /b/ onset (specifically for onset /v/, not covered by the general /v/ → /r/ merger) — flagged in *béntsıìy*
2. /ə/ → /o/ after /n/ — flagged in *nobêt*
3. /ɪ/ → /ɛ/ after /b/ — flagged in *nobêt*
4. /ɫ/ → /j/ extended environment (palatal consonant as left flank, not just high front vowel) — flagged in *béntsıìy*

**New rules likely needed for this batch** (to be flagged as [Open] in entries, not committed to phonology.md):
- /m/ → /b/ in onset (separate from /p/ → /b/; or possibly /m, p/ → /b/ in onset is the existing settled rule — yes, this IS in §4.4.1: "/m, p/ → /b/ in onset") — so mint → beńt via /m/ → /b/ is covered
- /v/ → /r/ is the general rule; /v/ → /b/ in onset may be new (flagged open)

### orthography.md (v2.4)

**Key rules for reading/writing headwords:**
- Acute on vowel = pitch accent (always written)
- Grave on vowel = stress (usually unwritten; written in formal/pedagogical text)
- Circumflex = pitch + stress coincide (formal register; used in headwords per dictionary §3)
- Acute on consonant = devoicing (ń, ḿ, ŕ, ś)
- `rh` = /ɻ/; `r` = /ɾ/
- `ss`=geminate /sː/, `nn`=geminate /nː/, `pp`=geminate /pː/
- Long vowels: `au`=/ɑː/, `eu`=/ɛː/, `iu`=/ɨː/, `ou`=/oː/, `iiy`=/iː/
- Short vowels: `i`=/ɪ/, `ii`=gliding short /i/, `e`=/ɛ/, `a`=/ɑ/, `o`=/o/
- `œ` = the diphthong /oe/ (monosyllabic)
- `ı` (dotless i) appears when one element of `ii` takes a diacritic
- Ogonek for nasalization on open/mid vowels: `ą`=/ɑ̃/, `ę`=/ɛ̃/, `ǫ`=/õ/; on `u` of digraph: `aų`, `eų`, `ių`, `oų`
- Tilde for nasalization on close-front/approximants: `ĩ`, `ỹ`, `w̃`
- `s` in onset = /s/; `s` non-onset = /z/; `ś` non-onset = /s/ (devoiced); `ss` = /sː/ geminate

### dictionary.md (full read)

**Schema (per §1):**
```
### headword

#### Etymology
*GA etymon* — drift/register notes.

**Part of speech:** abbr.  **IPA:** /…/  **Foot:** (…).

Phonological development: semicolon-separated rules with brief labels. [Open: …] tags inline.

Cross-refs: *word* (description).

#### Definition

1. gloss.

#### Morphology
(optional)

#### Notes
(optional; form-specific only — no propagation tickets)
```

**Collation order** (from §2):
> a, ą, b, ð, e, ę, æ, h, i, ii, k, l, m, ḿ, n, ń, o, ǫ, œ, p, r, rh, ŕ, s, ś, š, t, þ, w, w̃, y, ỹ

`ii` and `rh` are distinct letters with their own slots. `r < rh < ŕ`. `æ` slots after a-region; `œ` after o-region.

**Key patterns from existing entries:**
- Foot notation: `(L)` = light syllable, `(H)` = heavy syllable, `(ˈH)` = stressed heavy, etc.
- `[Open]` used freely when a field depends on unsettled phonology
- `Phonological development` is a compact derivation record, not prose discussion
- Semantic drift notes go in the Etymology section
- The changelog (§5) records open questions surfaced during each session

---

## Preliminary phonological analysis of batch entries

Working through the entries with known rules — **flagging issues**.

### Icecream block (rows 2–7)

**éuskrıì** "icecream" ← *icecream* /ˈaɪsˌkriːm/
- /aɪ/ → /ɪ/ or /eː/ (conditioning open) — the `eu` in `éusk-` suggests /eː/? But the headword has `eu`... wait, `éuskrıì` = é-u-s-k-r-ı-ì. So `eu`=/ɛː/, `sk`=cluster, `r`=/ɾ/, `ıì`=... `ı` is dotless i (one element of `ii` taking a diacritic). So this is `ii` with grave on second `i` → `ıì`. That means the word ends in `iiy`? No — `ıì` without trailing `y` is just `ii` with grave on second element. So: `éu`=/ɛː/ (pitch on é), `sk`=cluster /sk/, `r`=/ɾ/, `ıì`= stressed gliding /i/ (`ii` with stress grave). Final stress on /i/.
- Derivation: *icecream* /ˈaɪsˌkriːm/: /aɪ/→/ɛː/ (→ `eu`); /s/→/h/ (debuccalization) — but wait, there's an `s` in `éusk`, which in onset would be /s/ not /h/. But /s/→/h/ in onset... Hmm. Actually the /s/ here is the start of `-cream` part: /ˈaɪs.ˌkriːm/. The /aɪ/ collapses, the /s/ in "ice" would be... between vowel-reduced position or onset? 
- Actually *icecream* is a compound: *ice* /aɪs/ + *cream* /kriːm/. The /aɪ/ → /ɛː/ (`eu`). The /s/ of *ice* is in coda of that syllable — not onset, so it would → /z/ (the non-onset /s/ = /z/ rule)? But `ss` would be geminate. Or the /s/ stays as /s/ because it's at the syllable boundary preceding stress (→ /sː/ rule from §4.4.1). Yes! The `/s/ → /sː/ at syllable boundary preceding stress` rule applies here: the /s/ of *ice* is at the boundary before the stressed *cream* syllable → /sː/ → `ss`. But the headword has single `s` in `éusk-`... So it's /sk/ not /sː/. Hmm.
- Let me re-read: `éuskrıì`. Breaking this down: `é`=pitch on /ɛː/, `u`=second element of long vowel, `sk`=cluster, `r`=tap, `ı`=dotless i (first element of `ii`), `ì`=stressed second element of `ii`. So the IPA would be approximately /ɛːˈskri/ or /ɛːˈskɾi/?
- Wait, but /s/ is in onset here since `sk` is an onset cluster. In onset, `s` is /s/ (not /z/). And /k/ in onset → /h/ normally... but /kj, kw/ stay surface [k]. Here `kr` not `kw`, so /k/ → /h/? That would give `sh` not `sk`... Unless /k/ before /ɾ/ → /r̥/ via the /kr/ → /r̥/ rule in §4.4.1. So /kr/ → /r̥/. That would collapse `skr` to `sr̥` → something like `sŕ`?
- This is getting complex. FLAG: éuskrıì derivation needs dedicated analysis. The headword as given should be trusted; derivation goes in the [Open] field.

**benıîæ** "vanilla" ← *vanilla* /vəˈnɪlə/
- /v/ → /b/ onset (the flagged-open /v/→/b/ rule)? Or /v/ → /r/ (general merger)? Headword starts with `b` so /v/→/b/.
- /v/→/b/ in onset: [Open — same flag as béntsıìy]
- /ə/ → absorbed or /ɛ/: initial unstressed /ə/ → /ɛ/ (E5, settled in v2). But headword is `ben-` not `*bɛn-`... hmm, `e` = /ɛ/, so `be` = /bɛ/. ✓
- /n/ → tap via general merger /n/→/r/? But headword has `n` not `r`. Hmm — /n/ can either elide (E1) or merge to /r/ or stay. In GA *vanilla* /vəˈnɪlə/, the /n/ is intervocalic between /ə/ and /ɪ/. E1 says intervocalic /n/ elides (leaving nasalization). But headword `benıîæ` has `n`... So either E1 didn't fire (maybe function of stress pattern?), or the /n/ was treated differently.
- Actually in *vanilla*, stress is on the second syllable /ˈnɪlə/. So /v/ is onset, /ə/ is pre-stress unstressed, /n/ is the start of the stressed syllable — it's not intervocalic in the same way (it's at the onset of the stressed syllable). So E1 (intervocalic consonant elision) wouldn't fire on /n/ here because /n/ is an *onset* consonant, not intervocalic.
- /ɪ/ → short lax /ɪ/ (written `i`). With pitch (from GA stress on this syllable): `í`. But headword has `ı` (dotless i from `ii` digraph). So maybe the vowel here is the gliding /i/ (`ii`) not short lax /ɪ/ (`i`)?
- /l/ → ? In GA /ˈnɪlə/, /l/ is between /ɪ/ and /ə/. The /ɫ/ → /j/ rule applies between high front vowels. Is /ɪ/ high front? Yes. Is /ə/ high front? No. So /ɫ/ → /j/ might not fire. But then coda /l/ → ∅ (E2c)? And /ə/ → absorbed or /a/ or /ɛ/...
- Final vowel: `æ`. In the orthography, `æ` represents residual /æ/ — "did not fully collapse into /eː/." So the final vowel of *vanilla* /ˈnɪlə/ → /æ/? The /ə/ final → /a/ (E5 strengthening) normally. Getting /æ/ from /ə/ would be unusual. FLAG for analysis.
- Overall: benıîæ ← *vanilla*. The `î` is `i` with circumflex (pitch+stress coincide on this `i` from the `ii` digraph). So pitch and stress both land on the gliding /i/. And `æ` is the final syllable /æ/.

This is getting quite involved. Let me just flag these for the session rather than fully analyzing here.

### Key flags to raise with the user

1. **Loanword block (rows 3–7, icecream flavors):** These are all straightforward borrowings of English food words. The phonology is real but the entries are basically loanword adaptations. Derivations may involve the same handful of rules repeated.

2. **Venus → reųś (row 9):** Expected onset /v/ → /b/ per the /v/→/b/ open rule, giving something like *bee-*. But headword starts with `r`. This is surprising. Either:
   - The /v/ → /r/ (general tap merger) applies here rather than /v/→/b/
   - OR the word is derived from a different form of "Venus" (e.g., genitive "Veneris" /ˈvɛnərɪs/?)
   - FLAG for user confirmation.

3. **victory → rékwıì (row 10):** Again `r-` onset from a word starting with /v/. Same issue as Venus. /v/→/r/ (general merger) rather than /v/→/b/?

4. **likewise → récquıìs (row 14):** GA /ˈlaɪkwaɪz/. `r-` onset from /l/... Dark /l/ → /j/ → then M1? Or /l/ → /r/ directly (not in the settled rules). FLAG.

5. **barnkw (rows 35–36):** Two POS for same headword — verb senses and noun senses. Should be one entry with multiple senses and perhaps two form lines or a POS note.

6. **rhiwıĩ (rows 46–47):** Two POS — interjection and adverb/temporal — same headword. One entry.

7. **rhéulyèś (rows 49–50):** Two senses under interjection (both rows say interjection). One entry with two numbered senses.

8. **Definitional meanings (rows 42–45):** beušiioskô, bawiiquoh?, bewii·iit, bewiipessô — these are *descriptive circumlocutions* ("where-she-goes-to-school", "what-we-call-home", etc.) that serve as the ETYMON, suggesting these are compound/periphrastic constructions, not borrowings. The headwords themselves are complex morphological forms. These likely need special treatment.

9. **piiquóæ vs. piquô (rows 38–39):** Two different headwords with related meanings ("to look" vs. "to pick out / discern"). These are likely a morphological pair — possibly `piiquóæ` is one verb form and `piquô` another (e.g., different aspectual or volition forms). They should be cross-referenced.

10. **réıì "milk" (row 29) and "toast" (row 27) collision check:** `toś` = toast (row 27), `réıì` = milk/dairy (row 29). No collision between them.

11. **spyi (row 30):** "for coffee in mokapot to spew, resulting in bitter mediocre coffee." Very specific meaning. From *spew*. The definition is more of a usage note than a gloss.

---

## Next steps for the session (to do when retrying)

1. **Phonological derivations** — work through each entry's sound changes systematically.
2. **Flag novel/suspicious derivations** — see flags above, especially Venus/victory (v→r), likewise (l→r), barnkw noun/verb split.
3. **Draft entries** in dictionary schema format.
4. **Sort into collation order** for insertion into dictionary.md.
5. **Write entries** and **update changelog**.

---

## Collation positions for batch entries (approximate)

Working through the collation order (a, ą, b, ð, e, ę, æ, h, i, ii, k, l, m, ḿ, n, ń, o, ǫ, œ, p, r, rh, ŕ, s, ś, š, t, þ, w, w̃, y, ỹ):

- **b-region:** bayarę, bárkennò, bąêų, benskyi, benıîæ, béo·ò, béuksoè, beųtw, beusp, beušiioskô, bewiipessô, bewii·iit, boeś, bœ, barnkw, bawiiquoh?, bęiink, bessts, beykw, beńt
- **e-region:** e, emmáwwè, éuskrıì
- **h-region:** hœ hoś, hóhonìt, hohô
- **n-region:** nœ, noê, nóeıìe
- **o-region:** ohô, óhò, ouś
- **œ-region:** (after o-region)
- **p-region:** piiquóæ, piquô, pot
- **r-region:** réıì, rékwıì, récquıìs, rékriiyæ, rérèyt, rıírǫ, reųś
- **rh-region:** rhiušp, rhiwıĩ, rhéulyèś
- **s-region:** spyi
- **t-region:** toś
- **œ-region entries:** bœ and nœ — wait, `œ` is in the alphabet after `o`. Headwords starting with `bœ` sort in the b-region (first letter `b`), not the œ-region. The œ slot is for headwords STARTING with `œ`. Same for compound/two-word entries like `hœ hoś` — starts with `h`, sorts in h-region.

---

*End of session notes. Created 2026-05-23.*
