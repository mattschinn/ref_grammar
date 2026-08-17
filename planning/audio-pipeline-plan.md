# Audio Pipeline — Planning Document

**Status:** [Active] — pilot 01 recorded, split and measured end-to-end (122/125 tokens);
first acoustic result in hand; publication branch built through polish (25/25 ready to encode)
**Opened:** 2026-08-11
**Last updated:** 2026-08-16

> **Reading this cold?** Jump to §2 (Current state) and §8 (Milestones). §1 and §3 are
> the original design reasoning, retained because parts of it were tested and one
> central assumption was falsified — the supersession trail is the useful part.
>
> **Companion documents.** `planning/audio-pipeline-map.html` is the pipeline diagram
> (published at <https://claude.ai/code/artifact/f40d5faf-bcb2-43af-b038-0585072341da>) —
> read it first if you want the shape before the detail.
> `planning/audio-pipeline-learnings.md` is the retrospective: why the pipeline looks like
> this, which approaches were tried and abandoned, and the judgement that should survive
> into the eventual skill (M10).

---

## 1. Objectives

- **Primary — throughput.** Asset creation is the bottleneck on rich example content. The
  goal is a workflow where a single recording session yields many per-item audio files
  with near-zero manual editing.
- **Secondary — phonetic analysis.** The same corpus should serve as acoustic data for
  testing open phonological claims, chiefly pitch accent contrastiveness and the V₁
  length-and-amplitude prediction (`phonology.md` §3.4).
- **Method.** A series of deterministic Python/CLI tools that an LLM *wields*, rather than
  an LLM that processes audio directly.

### Posture: the grammar is descriptive (author ruling, 2026-08-12)

Recorded production **is** admissible evidence for changing the canon docs. This reverses
the more cautious line the plan carried through the pilot, and it is the author's call.

- The reference docs describe the language as produced, not as prescribed. Where a recording
  and an entry disagree, **neither automatically wins** — but the author's expectation is
  that production is right more often than the written entry, because entries are derived by
  hand from GA premises that are easy to get wrong and production applies them by ear.
- **Every discrepancy gets flagged, not silently reconciled** — in either direction.
  Production can be wrong too (a misreading, a citation-form artefact, one speaker on one
  night), and a flag is what lets the author adjudicate.
- **This does not repeal the standing caveat below** (§7). One GA speaker who designed the
  language cannot *confirm* the residue analysis. The asymmetry is the point: production
  showing a documented contrast **absent** is informative, and it works by sending the
  analysis back to a premise — usually a claim about GA — that is decidable without the
  recording. The *noê* merger is the worked example.
- **Consequence for M10.** The eventual skill should not just cut audio; it should
  **quality-check dictionary entries against production** and report disagreements. That is
  now a first-class output, not a by-product.

### Division of labour

- **Mat provides:** a word list (or a selection rule over `dictionary.md`), and one long
  audio file recorded to a fixed protocol.
- **Deterministic tools do:** splitting, trimming, filtering, loudness normalisation,
  encoding, and measurement. Everything acoustic is code.
- **Claude does:** manifest generation, tool orchestration, and reconciliation over
  structured metrics output — never listening.
- **Explicit non-capability:** Claude cannot hear audio. See §4 for how identity is
  established without it.

---

## 2. Current state (2026-08-12)

### Files

| Path | What |
|---|---|
| `planning/audio-pilot-01.md` | Pilot 01 manifest + teleprompter (25-item V₁-contrast set, 5 blocks) |
| `audio/masters/session-01.wav` | Pilot 01 master, 10m52s. **Archive untouched.** |
| `audio/masters/session-01.txt` | Session header — **mostly unfilled, needs completing from memory** |
| `audio/work/session-01-anchors.csv` | Stage-1 output: item identity → approximate time |
| `audio/work/session-01-segments.csv` | Stage-2 output: exact word boundaries, 122/125 usable |
| `audio/work/session-01-tokens.csv` | Stage-3 output: per-token acoustic table |
| `audio/work/items/` | 122 per-item WAVs, padded and unprocessed |
| `audio/work/contours.json`, `contours.html` | Contour data + published readout |
| `tools/audiolib.py` | Shared primitives: envelope, blob/utterance clustering, endpointing, F0 |
| `tools/audio-metrics.py` | Session characterisation + reconciliation report |
| `tools/audio-slate-align.py` | Stage 1: digit-slate anchoring via Whisper |
| `tools/audio-split.py` | Stage 2: utterance clustering + anchor-driven word boundaries |
| `tools/audio-contour.py` | Stage 3: per-token measurement, contours, paired contrasts |
| `tools/audio-readout.py` | Builds `contours.html` from `contours.json`; the published readout's source |
| `tools/audio-select.py` | Stage 4: one publishable take per item — technical gate, then medoid |
| `tools/audio-polish.py` | Stage 5: publication conditioning (HPF → trim → loudness). **Never measure its output** |
| `audio/work/session-01-picks.csv` | Stage-4 output: the chosen take per headword, 25/25 |
| `audio/work/session-01-polish.csv` | Stage-5 per-file report (gain applied, method, ceiling hits) |
| `audio/work/polished/` | 25 polished WAVs, publication branch only |

### Pilot 01 measured results

Run `python tools/audio-metrics.py audio/masters/session-01.wav` to reproduce.

**Capture path is good.** Noise floor −60 dBFS, no mains hum (50/60/100/120 Hz bands
empty), SNR ~29 dB. The ZealSound in that room at midnight is fine. This question is
closed — do not re-litigate the mic.

**Three defects, all fixable in the next session:**

- Recorded 44.1 kHz / 16-bit, though the session header claims 48 k / 32-float.
  Acoustically survivable; 32-bit float would have made the clipping recoverable.
- 9,795 clipped samples across ~17 utterances. Amplitude data destroyed for those.
- 25 dB peak-level spread across the corpus — the opposite of the uniformity the whole
  design is meant to buy.

**One design assumption falsified — see §3.**

---

## 3. What the pilot falsified

### Silence-based segmentation does not work on this material

The original protocol asked for a ~0.5 s pause between slate and word and a ~1 s pause
between items, so that a splitter could tell the two apart. Measured:

```
gaps at even positions : 0.88 s
gaps at odd  positions : 0.90 s
separation             : 0.02 s
```

The hierarchy collapsed. Within-item and between-item pauses are indistinguishable.
A parameter sweep confirms this is not a tuning problem — segment counts run **68 to 353**
across a reasonable grid with **no plateau**. Any setting that lands near the true count
does so by coincidence.

**Two causes, and the second was not anticipated:**

1. Maintaining a two-level pause discipline across 125 utterances is not humanly
   realistic. The author's verdict: *"when saying 25 words 5 times it's really hard."*
   Treat this as a hard constraint on all future protocol design, not a discipline problem.
2. **Rickett Yack fights silence-based segmentation.** The language is full of
   word-internal silence — /ʔ/, geminates, /h/, /θ/, /sː/. Internal closures in
   `hóhonìt`, `ossıî`, `ŕeut`, `béntsıìy` are as long as the gaps between utterances.
   Any future silence-threshold approach hits this same wall.

> **Superseded:** the original §"Session protocol" bullet *"Say the item number in
> English, pause, then the item"* and the accompanying processing-chain step
> *"Silence-based segmentation into per-item files, with slate detection"* both assumed a
> recoverable pause hierarchy. Retained here for the trail; replaced by §4.

---

## 4. Architecture: identity and boundaries are separate problems

This is the central design correction, and it is what makes the pipeline work.

| Stage | Question | Method | Precision |
|---|---|---|---|
| **1 · identity** | which item is where | Whisper digit anchors + known reading order | ~0.3 s |
| **2 · boundaries** | exact onset/offset | local energy search *inside* a pinned interval | ~10 ms |

**Whisper is an anchor finder, not a transcriber.** Only English digit tokens are trusted;
everything it emits about the conlang is discarded. It does hallucinate — pilot 01 produced
`Thank you very much for joining us today` over a quiet stretch and a 26-way `Three.`
repetition loop. That does not matter, for four compounding reasons:

1. English digits are the one thing in the recording Whisper has an acoustic model for.
2. **The reading order is known in advance.** A missed slate bracketed by two correct
   anchors is still unambiguous — its position in the sequence fixes its identity. Recall
   of 91% yielded 100% recoverability on pilot 01.
3. Detections are aligned to the expected sequence by monotonic LCS, so hallucinations
   and loops drop out instead of propagating. This is the index-drift failure the original
   slating design was meant to prevent, now actually prevented.
4. Failure is local, not catastrophic. Timing structure fails globally — one missed
   boundary shifts every later label. A missed anchor costs nothing beyond itself.

**Hard constraint:** slates must stay **English digits**, permanently. Slating in
Rickett Yack collapses the whole scheme — there would be nothing to anchor on.

**Never let stage-1 times reach measurement.** Whisper's word timestamps come from
cross-attention, good to perhaps ±0.3 s. Fine for "item 17 is in this interval," useless
for "V₁ was 12 ms longer." Stage 2 re-derives boundaries locally, where the search is
constrained (one digit + one word per interval) and no parameter has to generalise across
ten minutes.

### Stage-1 results on pilot 01

```
raw digit detections           : 187
aligned to expected sequence   : 114 / 125  (91% recall)
items recoverable (bracketed)  : 125 / 125  (100%)
```

Session-01 needs neither re-recording nor hand-labelling.

### Stage-2 results on pilot 01

```
utterances clustered            : 316   (stable: 303-327 across the whole parameter grid)
usable word segments            : 122 / 125  (98%)
unresolved, flagged for a listen :   3
```

Two findings worth carrying forward:

- **Utterance clustering is stable where item segmentation was not.** Clustering asks only
  "where is a run of speech", not "where does an item begin", and the count barely moves
  across the grid — a real plateau, unlike the 68→353 sweep in §3. The item boundaries come
  from the anchors, not from silence, which is the whole point of the two-stage split.
- **The anchor lands *inside* its digit**, not before the word. Measured on pilot 01, a
  Whisper anchor sits within its slate utterance or up to ~0.5 s after it, while the word
  follows 1.3-1.8 s later. So the rule is: the slate is the last utterance starting at or
  before the anchor, and the word is the next one. Whisper's timestamp error is far too
  large to use any other way.

A row whose anchor does not resolve is **demoted, not dropped** — a bad anchor is a
stage-1 misdetection, and the reading order still fixes the item's identity, so it is
recovered by the same interpolation that handles the 11 slates Whisper never heard.

---

## 5. Revised session protocol

Supersedes the original protocol. Changes are driven by §3.

- **Manifest first.** Generate the annotation file and teleprompter before recording
  (`planning/audio-pilot-01.md` is the template; it is generated, not hand-written).
- **Room tone.** Five seconds of silence at the head. On pilot 01 the first 2.5 s were
  contaminated — hold still and say nothing, and start the clock after the mouse click.
- **Slate every item with its English digit.** Non-negotiable; this is the whole anchoring
  mechanism.
- **Pause discipline is no longer load-bearing.** Read at a comfortable pace. All that is
  needed is enough gap between digit and word (~0.3 s, produced naturally) for a local
  two-blob search to separate them. Do not try to hold a metronomic rhythm.
- **Retakes.** Say **"scratch"**, then re-slate and re-read. Whisper detected `Scratch.`
  cleanly in pilot 01, so this survives as a machine-readable marker. Last take wins.
- **Retake, don't repair.** A retake costs seconds; a manual edit costs minutes.
- **Block structure.** Read the full list once per block, order rotated per block, rather
  than repeating each word N times in a row — consecutive repetition causes
  given-information reduction that biases exactly the duration and amplitude measures
  under test.
- **Levels:** drop input gain ~10 dB from the pilot 01 setting (median peak was −20.8 dBFS
  with occasional items hitting 0). Record **32-bit float** so overshoots stay recoverable.
- **Freeze and log the setup.** Mic distance, gain position, room, host, format — into the
  session header *before* recording. "Never change the setup mid-corpus" is meaningless
  without a record of what the setup was.

---

## 6. Processing chain

- Format normalisation → mono WAV; **masters archived untouched, permanently**
- **Stage 1** — digit-slate anchoring (`audio-slate-align.py`) → anchor CSV
- **Stage 2** — local boundary search inside each anchor interval → per-item WAVs + segment CSV
- High-pass at ~60 Hz — no higher, or it clips the bottom of the F0 range
- Profile-based noise reduction from session room tone, used **conservatively** (spectral
  gating eats fricative energy and adds musical noise)
- EBU R128 loudness normalisation **per file, not per segment**, so within-utterance
  amplitude relationships survive
- Silence trimming with ~150 ms padding retained, so word-initial aspiration and /h/ are
  not amputated
- **Endpoints cut relative to each token's own peak, not to the session floor.** With a
  25 dB spread across the corpus, a session-relative threshold makes loud tokens measure
  longer than quiet ones for reasons that have nothing to do with phonology — and duration
  is one of the two measures under test. The within-item correlation between a token's peak
  level and its measured duration is the bias itself, and the defaults in
  `audiolib.refine_bounds` were calibrated to minimise it: **−0.31 → −0.05**. The endpoint
  walk must bridge dips of ~0.15 s or it halts at the first internal /h/, /ʔ/ or geminate
  closure and returns one syllable of a disyllable.
- Dual encode: **MP3 96–128 kbps mono** for the site, WAV master archived. *(Revised
  2026-08-16 from "Opus ~56 kbps". Three reasons: `site/src/lib/explore.ts` and
  `lessons.ts` already resolve `.mp3`; Safari only gained native Opus-in-ogg in 17.5;
  and at this corpus size the byte saving does not pay for the compatibility tail.
  The floor of 96 kbps is not negotiable downward — lossy codecs discard
  perceptually-masked high-frequency low-energy content first, which here means /h/,
  /θ/, /sː/ aspiration and the /ʔ/ and geminate-release transients.)*

### The corpus forks at stage 5

**Analysis reads stage-2 per-item WAVs. Publication reads stage-5 polished WAVs. The
two must never cross.** Loudness normalisation deliberately destroys cross-item
amplitude relationships — that is the whole point of it — and the V₁
length-and-amplitude prediction (`phonology.md` §3.4) is tested on amplitude. Measuring
polished audio would answer that question with an artefact of `audio-polish.py`. The
same applies to any future voice-conversion stage, more so.

Toolchain: numpy + scipy (present in the anaconda env), torch + transformers for stage 1.
ffmpeg/SoX not currently installed. praat-parselmouth would be convenient for F0 but is
not installed either — an autocorrelation/YIN tracker in numpy is sufficient and avoids
the dependency.

---

## 7. Analysis plan

### Metrics output (the LLM's actual input)

Per-token structured table: peak, RMS, integrated LUFS, estimated noise floor, SNR,
clipping sample count, duration, F0 track summary, intensity track, source anchor.

### Reconciliation

- Token count vs. manifest; missing `item_id`s; anchor-spacing anomalies (a gap far larger
  than the running median means a retake, break, or commentary sits in the interval)
- Durations implausible for the predicted foot and mora structure
- Tokens below SNR threshold or showing clipping → flagged for retake
- Coverage audit against `dictionary.md`: which headwords still lack audio

### The phonetic tests, and what is actually measurable

The binding constraint: testing "V₁ is longer than a comparable unstressed vowel" needs
vowel-level boundaries, and no forced aligner exists for Rickett Yack. The pilot-01 frame
design routes around this in two ways.

**a. Contour comparison — needs no alignment.** `óhò` /ˈoho/ and `ohô` /oˈho/ are
segmentally identical. Take the F0 track over the whole word, time-normalise to 0–100%,
average the 5 reps, overlay. If pitch placement is real, `óhò` peaks in the first half and
`ohô` in the second. The word is the unit. Same procedure for `nóè` vs `noê` — which
directly tests the claim in `dictionary.md` that they are a pitch minimal pair. If the
contours do not separate, that claim is unsupported.

**b. The /h/-medial items self-segment.** `óhò`, `ohô`, `hohô`, `hóhonìt` have voiceless
/h/ between vowels, so a voicing detector splits V₁ from V₂ with no aligner.
`hóhonìt` /ˈhohoˌnɪt/ gives pitched-V₁, plain-V₂, stressed-V₃ at **identical vowel
quality**. The V₁ length-and-amplitude prediction is directly testable on Frame A. (The
items were chosen for the quality match; the segmentability is a bonus.)

**c. Frame C is blocked without an aligner.** `rérèyt` /ɾɛˈɾɛjt/ is voiced throughout —
no acoustic seam. Whole-word contours only, until MFA or equivalent exists.

**Statistical honesty.** With n=5 per cell, this detects large effects — a pitch peak
moving between syllables is unmissable. It will *not* resolve "V₁ is 8% longer." Report
effect sizes and within-item variance; refuse conclusions the reps cannot carry.

### First results (pilot 01, 2026-08-12)

Published readout: <https://claude.ai/code/artifact/a23235c7-efac-433e-b460-69e51e2cb8ef>

Pairs are compared **within block** — each block contributes one token per item, which is
what the blocked reading order was for. With five blocks, all five agreeing is the weakest
result that means anything (sign test p = 0.06); 4/5 and below is noise.

Figures below are the **re-run of 2026-08-12 evening**, after the F0 search floor was
corrected from 70 Hz to 55 Hz (see "The F0 floor was railing" below). The duration result
is unchanged; the centroid figures moved by 0.4–1.8 pp.

| Contrast | Measure | Effect | Blocks agreeing |
|---|---|---|---|
| *óhò* → *ohô* | F0 centroid | +10.2 pp, d = +1.11 | 4/5 |
| *hóhonìt* → *hohô* | F0 centroid | +7.7 pp, d = +0.65 | 3/5 |
| *nóè* → *noê* | F0 centroid | +4.3 pp, d = +0.30 | 3/5 |
| *nóè* → *noê* | **duration** | **−280 ms** | **5/5** |

- **Pitch placement moves in the predicted direction in all three pairs**, but only the
  /oho/ pair does so with a large effect, and none is consistent across all five blocks.
  Suggestive; not established.
- **The one consistent effect in the set is duration, on the pair that is documented as a
  *pitch* contrast.** `dictionary.md` declares *nóè* / *noê* a minimal pair carried "by
  spelling and pitch, not the broad IPA." Their centroids differ by 4.3 pp with sd 23.4 —
  noise. Their durations differ by 280 ms, or 57% of the shorter token, in every block.
- **The standing caveat.** The corpus is produced by a GA speaker who designed the
  language, so a positive result is not evidence for the residue analysis; see the boxed
  note below. What follows is a case where that cut the *other* way and was informative.

#### The *nóè* / *noê* pair: production disagrees with the entry, and the entry is the
#### side that gives

Author's reading, 2026-08-12, after seeing the duration result: both words descend from GA
phrases accented on their **second** element — *in a WAY* and *no, WAY!* — so *no* is
unstressed in both. The entry's "residual high pitch on *no*" was derived from a **NO way!**
realization, which is possible but much rarer than *no WAY!*. The recording follows the
genuine GA pattern rather than the entry's prescription.

Three checks against the pilot audio, all consistent with that reading:

1. **No V₁ pitch peak exists in *nóè*.** Its mean normalised contour is flat (80 → 82 Hz
   across the word; early-third minus late-third = **−1.8 Hz**, i.e. very slightly rising).
   *noê* is equally flat (+1.5 Hz). For comparison the Frame A items show real declination
   from a real accent: *óhò* falls **16.3 Hz**, *hóhonìt* 10.9, *ohô* 9.1.
2. **Both members start ~16 Hz lower than the Frame A items** (80–84 Hz vs 96–99 Hz), at
   the bottom of the speaker's range. Neither word carries an early accent to decline from.
   (Frame A vs Frame B is not a controlled comparison — different carriers — but the
   *within*-Frame-B pair is matched, and neither member has a V₁ peak.)
3. **The +4.3 pp centroid "shift" is two flat contours differing by noise.** The centroid
   statistic degrades toward 50% on a flat contour by construction; 43.9% vs 48.2% with
   sd 23.4 is exactly that.

**The pause hypothesis was tested and does not hold.** If the length difference were the
comma in *no, WAY!*, it would appear as internal silence. It does not: the longest internal
sub-threshold run is 44 ms in *both* words (identical means), and removing *all* internal
low-energy time leaves 252 ms of the 280 ms difference standing. A wide-window check is
independently decisive — the endpointer bridges dips only to 150 ms, so a 200–300 ms pause
would have halted the walk and left a second sounding chunk outside the token boundary. In
all five blocks *nóè* is a single unbroken sounding run. The extra 250 ms is **sounding
material**, not a gap.

- **Still confounded, and still not a dictionary edit.** *nóè* is an emphatic interjection
  and *noê* a hedging adverb, so 250 ms of extra sounding material may be citation-form
  emphatic lengthening rather than phonology. Separating them needs the pair in frames that
  hold pragmatics constant — not in pilot 01. **Do not amend `dictionary.md`** on the
  duration.
- **RULED 2026-08-12 — the entries are merged.** The GA premise (**NO** way!) is wrong; the
  two words are homophones and now form one polysemous entry, `dictionary.md` §*noê*, with
  both etymologies. Propagated to `orthography.md` v3.11 (§3.7's worked example moves to
  *óhò* / *ohô*, which this recording supports) and `phonology.md` v4.9 (§5.4 candidate pair
  withdrawn). The duration finding stayed out, as above.

#### The F0 floor was railing

`F0_MIN` was 70 Hz against a speaker median of **84.5 Hz** — about four semitones of
headroom, which creak at the end of an isolated citation word falls straight through. The
tracker did not fail loudly; it reported the octave above. 27 of 120 tokens had `f0_min`
sitting exactly on the rail, and *noê* block 2 read 103.7 Hz where the true value is 82.0.
Floor lowered to 55 Hz in `audiolib.py`: railing goes to 0/120, median voiced fraction is
unmoved (0.40 → 0.41, so the change is not admitting noise), and `f0_track` now takes
explicit `f0_min` / `f0_max` arguments.

**Voiced fraction is the diagnostic** — median 0.47 across the corpus, and 19 of 120 tokens
below 0.30. Any per-token F0 summary computed over a handful of voiced frames is weak
evidence, which is a further reason the duration result (no pitch tracking required) is the
solid one in this set.

#### Variable pitch on the new final stress [Open — the session-02 question]

Author's hypothesis, 2026-08-12: where stress relocated off the GA position onto the final
vowel, the new stress reliably carries **length and loudness**, but its **pitch varies** —
sometimes staying low, retaining the pitch of the originally unstressed GA syllable, and
sometimes going high (which he hears as resembling the Swedish disyllabic accent). No
meaning difference; possibly conditioned by emphasis or focus. He judges the variation
genuine and wants it **described as variation**, not normalised away.

The pilot is consistent with it and cannot do better than that:

| Group | Items | F0 late−early | Rising | Range |
|---|---|---|---|---|
| First-syllable pitch | *óhò*, *hóhonìt* | −2.58 st | **0/10** | −6.2 … −0.1 |
| Final stress | *ohô*, *hohô*, *noê* (both senses) | −0.52 st | **8/20** | −5.8 … +3.2 |

Fisher p = 0.03; Mann–Whitney p = 0.02; variance ratio 1.8. The words with an early accent
decline categorically; the final-stressed words scatter across nine semitones. There is a
1.5 st gap in the middle of the final-stressed distribution (12 values ≤ −0.65, 8 values
≥ +0.87) which *looks* bimodal, **but n = 20 cannot distinguish two modes from one wide
distribution** and nothing should be built on that gap.

**What the pilot cannot test, by construction.** A citation wordlist has no focus
manipulation, so the conditioning environment is untested — and the emphasis proxies
available are useless here: correlating the F0 rise against each token's duration and peak
level within an item gives mean r = +0.12 and −0.07, with per-item values swinging from
−0.96 to +0.92 at n = 5. Loudness is separately unusable in this session (Frame E clipped).

**Relative loudness does move the right way**, weakly: peak intensity in the second half
minus the first is −4.6 dB for first-syllable-pitch words and −1.5 dB for final-stressed
ones. Both negative — intensity declines across a citation form regardless — so only the
3.1 dB *difference* is meaningful, and it is one number. **The length half of the claim is
untested:** whole-token duration is measured, but per-syllable duration needs phone
boundaries the pipeline does not produce (see MFA, §9).

**Typological footing.** The hypothesis is not exotic; it is close to the textbook
stress/accent split. Beckman (1986) separates *stress accent* (prominence cued by duration
and spectral properties) from *non-stress accent* (cued by pitch alone), and in the
Beckman & Pierrehumbert model of English the lexicon marks *where* a pitch accent would go
while whether one is realized at all depends on phrasal structure and focus — an unfocused
English word keeps its stress and loses its pitch accent entirely. Hyman's word-prosodic
typology makes the same point from the other end: obligatoriness and culminativity define
stress, and F0 is *not* criterial, so systems where prominence is real but pitch is
optional are expected rather than anomalous. Fry's cue-weighting results and the
cross-language literature that followed establish that duration, intensity and F0 are
separable cues whose weights differ by language.

Two consequences worth stating plainly. **First, if the variation is focus-conditioned it
is post-lexical, not lexical** — it belongs in the description of phrasal prosody, not in
headword diacritics, and the circumflex's "coincidence" reading then covers only the
high-pitch realization (`orthography.md` §3.7, flagged). **Second, the Swedish comparison
is a perceptual analogy, not an analysis:** Scandinavian accent 1/2 is *lexically
contrastive* and this explicitly is not, so the resemblance is in the contour shape only.
The diachronic literature on Scandinavian accentogenesis is nonetheless the right
neighbourhood for how a stress shift *becomes* a tonal contrast later, if it ever does.

**Session 02 must manipulate focus.** Everything else in the design follows from that; see
§5 and M8.

**The standing caveat.** The corpus is produced by a GA speaker who designed the language.
It can show whether Mat's production matches the spec's predictions; it cannot confirm the
residue analysis. A negative result is informative (he cannot produce what the spec
describes); a positive one is not evidence for the analysis. **Do not let reconciliation
output be written into `phonology.md` as confirmation.**

---

## 8. Milestones

- [x] **M0** — Draft pilot manifest + teleprompter (`planning/audio-pilot-01.md`)
- [x] **M1** — Record pilot 01 (`audio/masters/session-01.wav`)
- [x] **M2** — Session metrics tool (`tools/audio-metrics.py`)
- [x] **M3** — Stage 1: digit-slate anchoring (`tools/audio-slate-align.py`), 100% recoverable
- [ ] **M4** — Complete `audio/masters/session-01.txt` — **needs Mat**: mouth-to-mic
      distance, gain position, ZealSound variant, mic position, room. The measured facts
      are already corrected in the file; only the physical setup is missing.
- [x] **M5** — Stage 2: `tools/audio-split.py` — 122/125 (98%). Retakes trimmed to the last
      take, unanchored items interpolated, bad anchors demoted and recovered.
      3 unresolved and flagged: block 1 *toś*, block 2 *béntsıìy*, block 5 *rhiitsô*.
- [x] **M6** — `tools/audio-contour.py --tokens` — per-token table (duration, peak, RMS, SNR,
      clipping, F0 median/min/max, peak position, centroid, voiced fraction)
- [x] **M7** — Frame A/B contour analysis, paired by block. See §7 "First results".
- [ ] **M8** — **Record session 02.** No longer a question of whether; the design is now
      determined by three things the pilot cannot do:
      1. **Focus manipulation** — the variable-final-pitch hypothesis (§7) is the main
         question and a citation wordlist cannot test it. Each target word needs to appear
         both **focused** and **unfocused** in a carrier frame, several times each. This is
         the primary design driver.
      2. **Amplitude headroom** — Frame E clipped in every block of pilot 01. Drop input
         gain ~10 dB and record 32-bit float so overshoots stay recoverable.
      3. **Pragmatics held constant** — to separate the *noê* senses' 280 ms, the two need
         frames that do not make one an emphatic interjection and the other a hedge.
      Keep everything that worked: English digit slates, blocked rotation, five reps.
      Per-syllable duration still needs phone boundaries (MFA, §9) — worth resolving before
      recording, since it decides whether the length half of the hypothesis is testable at all.
- [x] **M9a** — Stage 4 take selection (`tools/audio-select.py`). 25/25 items resolved,
      0 forced past the technical gate, 2 flagged thin (*rhiitsô* 2 usable, *pot* 1).
      **Selection is by medoid, not by quality score** — ranking on SNR or peak would
      systematically publish the loudest, most emphatic reading of every word, which is
      the same citation-form emphasis that confounds the *noê* duration result (§7).
      The gate is disqualifying-only; the medoid decides among survivors.
- [x] **M9b** — Stage 5 polish (`tools/audio-polish.py`). 60 Hz zero-phase high-pass →
      trim with 150 ms padding → loudness normalisation. All 25 land at **−24.0 LUFS
      with 0.00 dB spread**, peaks −6.9…−1.4 dBFS, none ceiling-limited.
      Two calibration findings:
      - **Target is −24 LUFS, derived not chosen.** Citation words have a 17.1–22.6 dB
        peak-to-loudness ratio; at the initial −20 LUFS, 12 of 25 files hit the peak
        ceiling and landed short of target, defeating the uniformity the stage exists
        for. −24 is the first whole dB at which all 25 reach target.
      - **BS.1770 gating is meaningless at this token length.** A 0.4 s block with 75%
        overlap yields ~2 blocks on a 0.6 s word. Below `--gate-min-blocks` the tool
        falls back to ungated K-weighted RMS over the trimmed token and reports the
        fallback per file rather than applying it silently. All 25 used the fallback.
      - Noise reduction is implemented but **off by default** (§9 open question; median
        SNR 45 dB, and spectral gating eats fricative energy).
- [ ] **M9c** — Site integration: MP3 encode + per-word audio on `/explore/`.
      ffmpeg 9.0 installed 2026-08-16 (winget `Gyan.FFmpeg`, not conda — mixing
      conda-forge into the `defaults` base env risks collateral downgrades to the
      torch/numpy stack). Encode path verified end-to-end on a pilot token.
      **Open detail:** `explore.ts` expects `public/audio/words/<slug>.mp3`, and
      github-slugger leaves the headword's diacritics intact, so the slug is literally
      `óhò`. That means Unicode filenames and percent-encoded URLs. The author's
      proposal is to reuse the diacritic typer's postfix trigger codes
      (`site/src/scripts/diacritics.js`: `1` acute, `2` nasal, `3` ligature, `4` grave,
      `5` háček, `9` thorn/eth, `c` circumflex, `d` diaeresis) as a reversible
      ASCII-safe filename encoding — *óhò* → `o1ho4`. Unresolved: the typer's rule set
      has no code for dotless `ı` (*ossıî*, *rékwıì*), which is needed before this can
      be adopted. Decide before encoding, since the mapping must match on both sides.
- [ ] **M10** — Fold a skill doc (`audio-pipeline`) once the workflow stabilises. The
      procedure comes from this file; the judgement comes from
      `planning/audio-pipeline-learnings.md` §5, which sketches the skill's steps.

---

## 9. Open questions

**Answered by pilot 01:**

- ~~Spoken-digit vs keystroke slating: which survives contact with actual reading~~ →
  Spoken digits survive, but only because they are anchors rather than boundary markers
  (§4). Keystroke slating is unnecessary.
- ~~Which ZealSound variant / host~~ → laptop host, WASAPI, measured clean. Log the variant
  in the session header (M4).

**Still open:**

- Noise reduction aggressiveness — the fricative-preservation threshold needs empirical
  tuning. Untested; the SNR is good enough that NR may be skippable entirely.
- Whether connected-speech recordings belong in the same corpus or need a separate protocol.
- Whether to re-record pilot 01 for clean amplitude data (17 clipped utterances) or accept
  the loss and move on (M8).
- ~~**The *nóè* entry's GA premise.**~~ **Ruled and executed 2026-08-12** — entries merged
  (`dictionary.md` §*noê*), propagated to `orthography.md` v3.11 and `phonology.md` v4.9.
- **Is the variable final pitch two modes or one wide distribution, and what conditions it?**
  The open question session 02 exists to answer. See §7 and M8. Until it is settled, the
  circumflex's "pitch–stress coincidence" reading in `orthography.md` §3.7 is flagged as
  possibly describing only one of two realizations.
- **Is the length half of the stress claim even testable here?** Whole-token duration is
  measured; per-syllable duration is not, and the hypothesis is about the final *syllable*.
  Blocked on MFA (below) or on hand-segmenting a subset.
- **MFA viability** — phone-level boundaries would unblock Frame C. Mapping RY phones to
  nearest English equivalents *for alignment only* may work, since alignment is far more
  constrained than recognition; geminates, `iu`, and the nasal vowels are the likely failure
  points. **This is an experiment, not a plan.**

---

## 10. Handoff notes

- **Interpreter:** `C:\Users\schin\anaconda3\python.exe`. System `python`/`python3` are
  broken Windows Store stubs.
- **Deps present:** numpy, scipy, torch 2.10 (CPU), transformers 5.3, onnxruntime.
  **Absent:** ffmpeg, SoX, librosa, soundfile, parselmouth, whisper/faster-whisper.
- Stage 1 uses `openai/whisper-base.en` via `transformers`, cached in
  `~/.cache/huggingface`. A full 10-minute session takes ~12 min on CPU — **run it in the
  background.**
- Reproduce the whole chain (stage 1 is the only slow step):
  ```
  python tools/audio-metrics.py      audio/masters/session-01.wav
  python tools/audio-slate-align.py  audio/masters/session-01.wav \
      --out audio/work/session-01-anchors.csv                        # ~12 min, background
  python tools/audio-split.py        audio/masters/session-01.wav \
      --anchors audio/work/session-01-anchors.csv \
      --out audio/work/session-01-segments.csv --write-wav audio/work/items
  python tools/audio-contour.py      audio/masters/session-01.wav \
      --segments audio/work/session-01-segments.csv \
      --tokens audio/work/session-01-tokens.csv --out audio/work/contours.json \
      --items 1,2,3,4,5,6
  ```
- `audio-split.py --dump 5-60` prints the utterance sequence with anchors interleaved. It is
  the first thing to run when a segment looks wrong; the structure is legible by eye.
- Stages 2 and 3 share `tools/audiolib.py` deliberately. Two tools each finding their own
  word boundaries is how the first pass produced two incompatible views of one recording.
- `audio/masters/` is append-only. `audio/work/` is regenerable scratch.
