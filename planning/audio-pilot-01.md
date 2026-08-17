# Audio Pilot 01 — Manifest & Teleprompter

**Status:** [Provisional] — pilot session sheet, generated 2026-08-11
**Plan:** `planning/audio-pipeline-plan.md`
**Design:** V1-contrast set, 25 items x 5 repetitions = 125 utterances

---

## 1. Session header — fill this in BEFORE recording

Copy these values into a `session-01.txt` next to the WAV master. They are the
frozen-setup record; per the plan's decision principle, they must not change
mid-corpus.

```
session_id:       01
date:
mic:              ZealSound (variant:            USB / 3.5mm )
host:             laptop
mouth_to_mic_cm:
mic_position:     (stand / desk / boom; describe)
room:             (describe furnishings, hard surfaces)
audacity_rate:    48000
audacity_format:  32-bit float
audacity_channels: mono
input_gain:       (slider position / dial mark)
windows_enhancements_disabled:  yes / no
time_of_day:
notes:
```

**Windows check (do this first).** Sound settings -> your ZealSound -> Properties ->
disable every "Audio Enhancements" / AGC / noise-suppression option. Windows applies
automatic gain silently, and it destroys exactly the amplitude relationships the
V1 prediction depends on. This is the laptop-side equivalent of the phone-DSP risk in
`audio-pipeline-plan.md` "Hardware decisions".

**Audacity check.** 48 kHz, mono, 32-bit float. Nothing in the effects chain. Watch the
meter: peaks around -12 to -6 dBFS. If anything touches 0, stop and lower the gain --
clipping is unrecoverable and the metrics pass will flag it anyway.

---

## 2. Recording protocol

1. **Room tone.** Press record. Say nothing for **5 seconds**. Do not move. This is
   the noise profile for the whole session.
2. **Session slate.** Say: *"Session one. Twenty-five items. Five blocks."*
3. **For each block:** say *"Block one"* (two, three...), pause ~1 second, then read
   the block.
4. **For each item:** say the **English number**, pause ~0.5 s, say the **word**,
   pause ~1 s before the next item.
   > *"Seven."* ... *rérèyt* ... (pause) ... *"Twelve."* ... *béuksoè* ...
5. **Retake:** say **"scratch"**, then re-slate and re-read that item. The splitter
   drops the segment before the scratch; last take for an id wins. Retake, don't repair.
6. **Do not stop the recording between blocks.** One continuous file.
7. At the end, say *"End of session one"*, then hold silent for 3 seconds before stopping.

**Why five separate blocks and not five-in-a-row per word.** Consecutive repetitions of
the same word undergo given-information reduction -- each token comes out shorter and
flatter than the last. That would bias duration and amplitude systematically, which are
the two measures this list exists to test. Blocking spreads the drift across all items
instead of loading it onto each item's tail.

**Why the order changes each block.** Item position within a block correlates with
fatigue and with list-final lowering. Rotating the order decorrelates position from
item identity. The slate number travels with the word, so `item_id` is stable across
blocks regardless of order.

**Read them flat.** Do not perform the contrasts. Items 1/2/3 and 5/6 are near-identical
by design and are deliberately kept apart in every block; if you catch yourself
exaggerating a difference because you know the pair is coming, that is the measurement
contaminating itself.

---

## 3. Manifest

`pitch` / `stress` give the predicted prominence positions, counting vocalic positions
left to right. `frame` is the contrast group (see section 4).

| id | headword | IPA | gloss | pos | pitch | stress | frame |
|---:|---|---|---|---|---|---|---|
| 1 | *óhò* | /ˈoho/ | oh hey; hey | interj. | V1 | V2 | A |
| 2 | *ohô* | /oˈho/ | oh I see | interj. | V2 | V2 | A |
| 3 | *hohô* | /hoˈho/ | how so | part. | V2 | V2 | A |
| 4 | *hóhonìt* | /ˈhohoˌnɪt/ | coconut | n. | V1 | V3 | A |
| 5 | *nóè* | /noˈɛ/ | no way | interj. | V1 | V2 | B |
| 6 | *noê* | /noˈɛ/ | in a way | adv. | V2 | V2 | B |
| 7 | *rérèyt* | /ɾɛˈɾɛjt/ | narrate | v. | V1 | V2 | C |
| 8 | *rékwıì* | /ɾɛˈkʷi/ | victory | n. | V1 | V2 | C |
| 9 | *récquıìś* | /ˈɾɛkʷːis/ | likewise | adv. | V1 | V2 | C |
| 10 | *réıì* | /ɾɛˈi/ | dairy | n. | V1 | V2 | C |
| 11 | *béntsıìy* | /bɛntsˈiː/ | eventually | adv. | V1 | V2 | C |
| 12 | *béuksoè* | /ˈbɛːk.soɛ/ | backstory | n. | V1 | V2 | C |
| 13 | *béo·ò* | /bɛˈoo/ | a bit ago | adv. | V1 | V3 | C |
| 14 | *twıítò* | /ˈtwiːto/ | bird | n. | V1 | V2 | C |
| 15 | *emmáwwè* | /ɛmːˈɑwːɛ/ | in what way | adv. | V2 | V3 | D |
| 16 | *benıîä* | /bɛˈniæ/ | vanilla | n. | V2 | V2 | D |
| 17 | *ossıî* | /oˈsːiː/ | outside | n. | V2 | V2 | D |
| 18 | *piquô* | /pɪˈkʷoː/ | pick out | v. | V2 | V2 | D |
| 19 | *nobêt* | /noˈbɛʔ/ | in a bit | adv. | V2 | V2 | D |
| 20 | *rhiitsô* | /ɻiːˈtso/ | reach out | v. | V2 | V2 | D |
| 21 | *ŕe* | /ˈɾ̥ɛ/ | today | adv. | V1 | V1 | E |
| 22 | *toś* | /ˈtos/ | toast | n. | V1 | V1 | E |
| 23 | *e* | /ɛ/ | egg | n. | V1 | V1 | E |
| 24 | *ŕeut* | /ˈɾ̥eːʔ/ | carrot | n. | V1 | V1 | E |
| 25 | *pot* | /pot/ | pout | v. | V1 | V1 | E |

### CSV (for `audio-split.py` when it exists)

```csv
item_id,headword,ipa,gloss,pos,predicted_pitch,predicted_stress,frame
1,óhò,"/ˈoho/",oh hey; hey,interj.,V1,V2,A
2,ohô,"/oˈho/",oh I see,interj.,V2,V2,A
3,hohô,"/hoˈho/",how so,part.,V2,V2,A
4,hóhonìt,"/ˈhohoˌnɪt/",coconut,n.,V1,V3,A
5,nóè,"/noˈɛ/",no way,interj.,V1,V2,B
6,noê,"/noˈɛ/",in a way,adv.,V2,V2,B
7,rérèyt,"/ɾɛˈɾɛjt/",narrate,v.,V1,V2,C
8,rékwıì,"/ɾɛˈkʷi/",victory,n.,V1,V2,C
9,récquıìś,"/ˈɾɛkʷːis/",likewise,adv.,V1,V2,C
10,réıì,"/ɾɛˈi/",dairy,n.,V1,V2,C
11,béntsıìy,"/bɛntsˈiː/",eventually,adv.,V1,V2,C
12,béuksoè,"/ˈbɛːk.soɛ/",backstory,n.,V1,V2,C
13,béo·ò,"/bɛˈoo/",a bit ago,adv.,V1,V3,C
14,twıítò,"/ˈtwiːto/",bird,n.,V1,V2,C
15,emmáwwè,"/ɛmːˈɑwːɛ/",in what way,adv.,V2,V3,D
16,benıîä,"/bɛˈniæ/",vanilla,n.,V2,V2,D
17,ossıî,"/oˈsːiː/",outside,n.,V2,V2,D
18,piquô,"/pɪˈkʷoː/",pick out,v.,V2,V2,D
19,nobêt,"/noˈbɛʔ/",in a bit,adv.,V2,V2,D
20,rhiitsô,"/ɻiːˈtso/",reach out,v.,V2,V2,D
21,ŕe,"/ˈɾ̥ɛ/",today,adv.,V1,V1,E
22,toś,"/ˈtos/",toast,n.,V1,V1,E
23,e,"/ɛ/",egg,n.,V1,V1,E
24,ŕeut,"/ˈɾ̥eːʔ/",carrot,n.,V1,V1,E
25,pot,"/pot/",pout,v.,V1,V1,E
```

---

## 4. What each frame is for

**Frame A — the /oho/ quartet (items 1-4).** *óhò* and *ohô* are a true minimal pair on
prominence placement alone: same segments /oho/, pitch on V1 vs. pitch-stress coincident
on V2. *hohô* adds an onset control. *hóhonìt* gives a three-level word (pitched V1,
plain V2, stressed V3) where V1 and V2 are the **same vowel quality**, so a duration
difference between them cannot be blamed on intrinsic vowel length. This is the
cleanest test in the set of `phonology.md` 3.4's residue prediction.

**Frame B — the declared minimal pair (items 5-6).** *nóè* "no way" vs. *noê* "in a way".
`dictionary.md` states outright that these are a pitch-accent minimal pair and that the
contrast "is carried by spelling and pitch, not the broad IPA." That is a falsifiable
claim about your own production. If these two do not separate acoustically, the language
has no attested pitch minimal pair.

**Frame C — pitch on V1, stress on V_final (items 7-14).** The main body of the residue
prediction: V1 should be marginally longer and fuller than a comparable unstressed vowel,
with the F0 peak aligned to the nucleus rather than a syllable margin. *rérèyt* /ɾɛˈɾɛjt/
and *béo·ò* /bɛˈoo/ hold vowel quality constant across the two positions.

**Frame D — pitch not on V1 (items 15-20).** The controls Frame C is measured against.
Items 16-20 have a plain unstressed V1 with prominence on V2; *emmáwwè* puts pitch on V2
and stress on V3, testing that placement tracks the etymon rather than the word edge.

**Frame E — monosyllables (items 21-25).** Pitch and stress coincide trivially. These are
the single-prominence baseline: what one vowel looks like carrying the whole package.
*e* /ɛ/ is the floor case (light monosyllable), *ŕeut* /ˈɾ̥eːʔ/ the heavy one.

---

## 5. What this pilot can and cannot settle

**Can:** whether your production separates the Frame A and Frame B pairs at all; whether
V1 in Frame C is measurably longer/louder than the matched V1 in Frame D; whether F0
peaks align to nuclei; whether the phrase-final fall on an isolated citation form swamps
the V1 peak (which is what decides whether a carrier frame is needed for pass 2); and
what the room and capture chain actually sound like, in numbers.

**Cannot:** confirm the residue analysis. You are a GA speaker producing a language you
designed, so this measures whether your production matches your stated predictions, not
whether the language independently behaves that way. A negative result is still
informative -- it means you cannot produce what the spec describes -- but a positive one
is not evidence for the analysis. Do not let the reconciliation output get written up as
confirmation in `phonology.md`.

---

## 6. Teleprompter

Read straight down. Number first, pause, word, pause. Blocks run continuously --
do not stop the recorder between them.

- Room tone. Press record. Say nothing for 5 seconds. Do not move. This is the noise profile for the whole session.
- Session slate. Say: "Session one. Twenty-five items. Five blocks."

### Block 1

> Say: **"Block one"** — pause — then begin.

**1.**  **óhò**  <sub>/ˈoho/ · oh hey; hey</sub>

**7.**  **rérèyt**  <sub>/ɾɛˈɾɛjt/ · narrate</sub>

**5.**  **nóè**  <sub>/noˈɛ/ · no way</sub>

**16.**  **benıîä**  <sub>/bɛˈniæ/ · vanilla</sub>

**4.**  **hóhonìt**  <sub>/ˈhohoˌnɪt/ · coconut</sub>

**22.**  **toś**  <sub>/ˈtos/ · toast</sub>

**2.**  **ohô**  <sub>/oˈho/ · oh I see</sub>

**8.**  **rékwıì**  <sub>/ɾɛˈkʷi/ · victory</sub>

**11.**  **béntsıìy**  <sub>/bɛntsˈiː/ · eventually</sub>

**17.**  **ossıî**  <sub>/oˈsːiː/ · outside</sub>

**6.**  **noê**  <sub>/noˈɛ/ · in a way</sub>

**21.**  **ŕe**  <sub>/ˈɾ̥ɛ/ · today</sub>

**9.**  **récquıìś**  <sub>/ˈɾɛkʷːis/ · likewise</sub>

**3.**  **hohô**  <sub>/hoˈho/ · how so</sub>

**18.**  **piquô**  <sub>/pɪˈkʷoː/ · pick out</sub>

**13.**  **béo·ò**  <sub>/bɛˈoo/ · a bit ago</sub>

**23.**  **e**  <sub>/ɛ/ · egg</sub>

**15.**  **emmáwwè**  <sub>/ɛmːˈɑwːɛ/ · in what way</sub>

**14.**  **twıítò**  <sub>/ˈtwiːto/ · bird</sub>

**19.**  **nobêt**  <sub>/noˈbɛʔ/ · in a bit</sub>

**10.**  **réıì**  <sub>/ɾɛˈi/ · dairy</sub>

**24.**  **ŕeut**  <sub>/ˈɾ̥eːʔ/ · carrot</sub>

**12.**  **béuksoè**  <sub>/ˈbɛːk.soɛ/ · backstory</sub>

**20.**  **rhiitsô**  <sub>/ɻiːˈtso/ · reach out</sub>

**25.**  **pot**  <sub>/pot/ · pout</sub>

---

### Block 2

> Say: **"Block two"** — pause — then begin.

**16.**  **benıîä**  <sub>/bɛˈniæ/ · vanilla</sub>

**2.**  **ohô**  <sub>/oˈho/ · oh I see</sub>

**17.**  **ossıî**  <sub>/oˈsːiː/ · outside</sub>

**9.**  **récquıìś**  <sub>/ˈɾɛkʷːis/ · likewise</sub>

**13.**  **béo·ò**  <sub>/bɛˈoo/ · a bit ago</sub>

**14.**  **twıítò**  <sub>/ˈtwiːto/ · bird</sub>

**24.**  **ŕeut**  <sub>/ˈɾ̥eːʔ/ · carrot</sub>

**25.**  **pot**  <sub>/pot/ · pout</sub>

**5.**  **nóè**  <sub>/noˈɛ/ · no way</sub>

**22.**  **toś**  <sub>/ˈtos/ · toast</sub>

**11.**  **béntsıìy**  <sub>/bɛntsˈiː/ · eventually</sub>

**21.**  **ŕe**  <sub>/ˈɾ̥ɛ/ · today</sub>

**18.**  **piquô**  <sub>/pɪˈkʷoː/ · pick out</sub>

**15.**  **emmáwwè**  <sub>/ɛmːˈɑwːɛ/ · in what way</sub>

**10.**  **réıì**  <sub>/ɾɛˈi/ · dairy</sub>

**20.**  **rhiitsô**  <sub>/ɻiːˈtso/ · reach out</sub>

**7.**  **rérèyt**  <sub>/ɾɛˈɾɛjt/ · narrate</sub>

**4.**  **hóhonìt**  <sub>/ˈhohoˌnɪt/ · coconut</sub>

**8.**  **rékwıì**  <sub>/ɾɛˈkʷi/ · victory</sub>

**6.**  **noê**  <sub>/noˈɛ/ · in a way</sub>

**3.**  **hohô**  <sub>/hoˈho/ · how so</sub>

**23.**  **e**  <sub>/ɛ/ · egg</sub>

**19.**  **nobêt**  <sub>/noˈbɛʔ/ · in a bit</sub>

**12.**  **béuksoè**  <sub>/ˈbɛːk.soɛ/ · backstory</sub>

**1.**  **óhò**  <sub>/ˈoho/ · oh hey; hey</sub>

---

### Block 3

> Say: **"Block three"** — pause — then begin.

**3.**  **hohô**  <sub>/hoˈho/ · how so</sub>

**10.**  **réıì**  <sub>/ɾɛˈi/ · dairy</sub>

**5.**  **nóè**  <sub>/noˈɛ/ · no way</sub>

**17.**  **ossıî**  <sub>/oˈsːiː/ · outside</sub>

**23.**  **e**  <sub>/ɛ/ · egg</sub>

**20.**  **rhiitsô**  <sub>/ɻiːˈtso/ · reach out</sub>

**22.**  **toś**  <sub>/ˈtos/ · toast</sub>

**9.**  **récquıìś**  <sub>/ˈɾɛkʷːis/ · likewise</sub>

**19.**  **nobêt**  <sub>/noˈbɛʔ/ · in a bit</sub>

**7.**  **rérèyt**  <sub>/ɾɛˈɾɛjt/ · narrate</sub>

**11.**  **béntsıìy**  <sub>/bɛntsˈiː/ · eventually</sub>

**13.**  **béo·ò**  <sub>/bɛˈoo/ · a bit ago</sub>

**12.**  **béuksoè**  <sub>/ˈbɛːk.soɛ/ · backstory</sub>

**4.**  **hóhonìt**  <sub>/ˈhohoˌnɪt/ · coconut</sub>

**21.**  **ŕe**  <sub>/ˈɾ̥ɛ/ · today</sub>

**14.**  **twıítò**  <sub>/ˈtwiːto/ · bird</sub>

**1.**  **óhò**  <sub>/ˈoho/ · oh hey; hey</sub>

**8.**  **rékwıì**  <sub>/ɾɛˈkʷi/ · victory</sub>

**18.**  **piquô**  <sub>/pɪˈkʷoː/ · pick out</sub>

**24.**  **ŕeut**  <sub>/ˈɾ̥eːʔ/ · carrot</sub>

**16.**  **benıîä**  <sub>/bɛˈniæ/ · vanilla</sub>

**6.**  **noê**  <sub>/noˈɛ/ · in a way</sub>

**15.**  **emmáwwè**  <sub>/ɛmːˈɑwːɛ/ · in what way</sub>

**25.**  **pot**  <sub>/pot/ · pout</sub>

**2.**  **ohô**  <sub>/oˈho/ · oh I see</sub>

---

### Block 4

> Say: **"Block four"** — pause — then begin.

**7.**  **rérèyt**  <sub>/ɾɛˈɾɛjt/ · narrate</sub>

**9.**  **récquıìś**  <sub>/ˈɾɛkʷːis/ · likewise</sub>

**20.**  **rhiitsô**  <sub>/ɻiːˈtso/ · reach out</sub>

**17.**  **ossıî**  <sub>/oˈsːiː/ · outside</sub>

**10.**  **réıì**  <sub>/ɾɛˈi/ · dairy</sub>

**2.**  **ohô**  <sub>/oˈho/ · oh I see</sub>

**15.**  **emmáwwè**  <sub>/ɛmːˈɑwːɛ/ · in what way</sub>

**16.**  **benıîä**  <sub>/bɛˈniæ/ · vanilla</sub>

**18.**  **piquô**  <sub>/pɪˈkʷoː/ · pick out</sub>

**1.**  **óhò**  <sub>/ˈoho/ · oh hey; hey</sub>

**21.**  **ŕe**  <sub>/ˈɾ̥ɛ/ · today</sub>

**12.**  **béuksoè**  <sub>/ˈbɛːk.soɛ/ · backstory</sub>

**11.**  **béntsıìy**  <sub>/bɛntsˈiː/ · eventually</sub>

**19.**  **nobêt**  <sub>/noˈbɛʔ/ · in a bit</sub>

**22.**  **toś**  <sub>/ˈtos/ · toast</sub>

**23.**  **e**  <sub>/ɛ/ · egg</sub>

**5.**  **nóè**  <sub>/noˈɛ/ · no way</sub>

**3.**  **hohô**  <sub>/hoˈho/ · how so</sub>

**25.**  **pot**  <sub>/pot/ · pout</sub>

**6.**  **noê**  <sub>/noˈɛ/ · in a way</sub>

**24.**  **ŕeut**  <sub>/ˈɾ̥eːʔ/ · carrot</sub>

**8.**  **rékwıì**  <sub>/ɾɛˈkʷi/ · victory</sub>

**14.**  **twıítò**  <sub>/ˈtwiːto/ · bird</sub>

**4.**  **hóhonìt**  <sub>/ˈhohoˌnɪt/ · coconut</sub>

**13.**  **béo·ò**  <sub>/bɛˈoo/ · a bit ago</sub>

---

### Block 5

> Say: **"Block five"** — pause — then begin.

**5.**  **nóè**  <sub>/noˈɛ/ · no way</sub>

**23.**  **e**  <sub>/ɛ/ · egg</sub>

**22.**  **toś**  <sub>/ˈtos/ · toast</sub>

**19.**  **nobêt**  <sub>/noˈbɛʔ/ · in a bit</sub>

**11.**  **béntsıìy**  <sub>/bɛntsˈiː/ · eventually</sub>

**12.**  **béuksoè**  <sub>/ˈbɛːk.soɛ/ · backstory</sub>

**21.**  **ŕe**  <sub>/ˈɾ̥ɛ/ · today</sub>

**1.**  **óhò**  <sub>/ˈoho/ · oh hey; hey</sub>

**18.**  **piquô**  <sub>/pɪˈkʷoː/ · pick out</sub>

**16.**  **benıîä**  <sub>/bɛˈniæ/ · vanilla</sub>

**15.**  **emmáwwè**  <sub>/ɛmːˈɑwːɛ/ · in what way</sub>

**2.**  **ohô**  <sub>/oˈho/ · oh I see</sub>

**10.**  **réıì**  <sub>/ɾɛˈi/ · dairy</sub>

**17.**  **ossıî**  <sub>/oˈsːiː/ · outside</sub>

**20.**  **rhiitsô**  <sub>/ɻiːˈtso/ · reach out</sub>

**9.**  **récquıìś**  <sub>/ˈɾɛkʷːis/ · likewise</sub>

**7.**  **rérèyt**  <sub>/ɾɛˈɾɛjt/ · narrate</sub>

**13.**  **béo·ò**  <sub>/bɛˈoo/ · a bit ago</sub>

**4.**  **hóhonìt**  <sub>/ˈhohoˌnɪt/ · coconut</sub>

**14.**  **twıítò**  <sub>/ˈtwiːto/ · bird</sub>

**8.**  **rékwıì**  <sub>/ɾɛˈkʷi/ · victory</sub>

**24.**  **ŕeut**  <sub>/ˈɾ̥eːʔ/ · carrot</sub>

**6.**  **noê**  <sub>/noˈɛ/ · in a way</sub>

**25.**  **pot**  <sub>/pot/ · pout</sub>

**3.**  **hohô**  <sub>/hoˈho/ · how so</sub>

---

> Say: **"End of session one."** Hold silent for 3 seconds. Stop the recorder.

---

## 7. After the session

1. **Archive the master untouched.** Export the raw WAV to `audio/masters/session-01.wav`
   and never edit it in place. Everything downstream regenerates from it.
2. Save the session header text file alongside it.
3. Note anything that went wrong while it is fresh -- coughs, a phone buzz, a retake you
   are unsure the splitter will catch, a word you fumbled repeatedly. Free-text is fine;
   it becomes the tuning input for `audio-split.py`.
4. Open questions this pilot is meant to answer are listed in section 5 and in
   `planning/audio-pipeline-plan.md` "Open questions". Answer what you can from the
   session itself (did spoken-digit slating survive contact with actual reading?) before
   any tooling exists.
