# Poetics Reference

**Version:** v1 (May 2026)
**Depends on:** `phonology.md` v2 (inventories §2, metrical structure §3, pitch-stress dissociation §3.4)

This document collects the phonological features of the conlang that bear on verse design, and sketches three poetic formats those features suit. It is a forward-looking exploration: none of the forms below is committed, and the verse conventions proposed here are working proposals, not settled rules. Where a form depends on an unresolved phonological question, that dependency is flagged.

Status tags follow `phonology.md`:

- **[Settled]** — committed in `phonology.md`; safe to build verse conventions on.
- **[Provisional]** — current best analysis; expected to hold.
- **[Open]** — explicitly undecided; a verse convention resting on it inherits the openness.

GA reconstructions appear in italics with an asterisk (*sodium*). Surface forms appear in slashes (/.../) or in plain italics for the working orthography.

---

## 1. Phonological features relevant to poetry

Five features of the system carry verse-design weight. Each is cross-referenced to its home in `phonology.md`.

### 1.1 A real moraic system [Settled]

Syllable weight is a function of moraic content (`phonology.md` §3.1): a short vowel is 1μ, a long vowel is 2μ, a syllabic consonant is 1μ, and coda consonants are non-moraic by default. Light (1μ) and heavy (2μ) syllables are therefore genuinely distinct, and the stress/foot rules are weight-sensitive.

This is the single most important fact for verse. A working light/heavy contrast is exactly what quantitative meter (Greek, Sanskrit, Arabic) is built on. The conlang can count quantity cleanly in a way that, e.g., Modern English cannot.

### 1.2 Pitch-stress dissociation [pitch placement Settled; contrastiveness Open]

Stress and pitch are independent prosodic dimensions with separate placement rules (`phonology.md` §3.3–3.4):

- **Stress** falls on the final vocalic position of the word (syllabic consonants count; appendix material does not).
- **Pitch** falls on the syllable that carried primary stress in the GA etymon.

Because most multisyllabic GA etyma had initial stress, these two prominences usually land on **different** syllables — *Emma* /ɛma/ carries pitch on /ɛ/ and stress on /a/; *Emily* /ɛmiː/ carries pitch on /ɛ/ and stress on /iː/. Where the GA etymon's stress was final, or where reduction has left a single surviving vowel, the two **coincide** — *r̥eːʔ* "carrot", *hoʔnʔnts* "face".

No major natural-language poetic tradition uses an independent pitch tier as a *structural counterpoint* to a stress-based meter (Classical Chinese tonal verse keeps tone and meter on the same syllables; Greek pitch accent runs free of metrical quantity but is not deployed as a deliberate second tier). The dissociation is therefore a genuine, unexploited verse resource — see §4.

### 1.3 An alliteration-rich onset inventory [Settled]

The targeted mergers of `phonology.md` §1.1 collapse many distinct GA onsets into a few high-frequency conlang onsets:

- GA /s/ debuccalizes to /h/, and surface [k] is allophonic /h/ before a glide — so /h/ is an unusually common word onset.
- GA /d, dʒ, n, j, g, v/ all merge into the tap /ɾ/.
- GA /m, p/ merge into /b/ in onset; GA /f/ merges into /θ/.

The result is a small onset inventory with several very high-frequency members (/h/, /ɾ/, /b/, /θ/). Alliterative verse, which needs a steady supply of matching onsets, is correspondingly easy to feed — easier than in English, where the onset inventory is large and thinly spread.

The complication is *where* alliteration should attach (see §3.2): conlang stress is final, so the onset of a polysyllabic word is typically an unstressed onset, whereas Germanic alliteration attaches to stressed-syllable onsets.

### 1.4 The appendix [Settled; metrical treatment Open]

A subset of words carry substantial syllabic-consonant material after the stressed vowel — *Jennifer* /ˈrɛ̃ːθw̩/, *Rochester* /ˈritsstw̩/, *countenance* /ˈhoʔn̩ʔn̩ts/ (up to four post-stress nuclei depending on parse). This material is **weight-bearing** (moraic) but **stress-invisible** (foot-external; `phonology.md` §3.5).

For verse this is a fork in the road, not a settled resource. Any quantitative or syllable-counting form must take a stand on whether appendix moras count. The three live options:

1. **Count fully** — appendix moras are metrical like any other. *hoʔnʔnts* is then a heavy, multi-mora word.
2. **Ignore entirely** — appendix is metrically zero; only the head foot counts. *hoʔnʔnts* contributes ~1μ to the meter.
3. **Separate ornamental tier** — the meter runs on the head foot; appendix material adds texture without disturbing the count.

Option 3 has the least natural-language precedent and the most expressive potential (a sound/weight tension the classical traditions lack). This document tentatively adopts **option 3** in §2, but the choice is **[Open]**.

### 1.5 Vowel-cluster tolerance and length [Settled]

Intervocalic elision has produced widespread hiatus (*hoiom* /ˈhoiom/ "salt", *reio* /reio/ "radio") and a long-vowel series (/iː, ɛː, oː, aː, ɨː/) plus diphthongs (/ei, oe, ia/). Long vowels and diphthongs are reliably heavy; hiatus sequences supply runs of light nuclei.

This gives a verse-maker a usable mix of weights to compose lines from — long vowels and diphthongs for heavy positions, hiatus and short vowels for light ones — without having to lean on the appendix.

---

## 2. Quantitative meter

**Model:** Sanskrit *anuṣṭubh*/*śloka*, Greek and Arabic quantitative verse.
**Fit:** Strong. Rests directly on the moraic system (§1.1).

### 2.1 Principle

The line is measured by **mora count and light/heavy patterning**, not by syllable count or stress. A foot is a fixed quantitative shape (e.g. light-heavy, heavy-light-light), and the line is a sequence of such feet, typically with the cadence (line-end) more strictly regulated than the opening.

### 2.2 Mora assignment

Following `phonology.md` §3.1, and adopting the **ornamental-appendix** treatment (§1.4, option 3):

| Element | Moras |
|---|---|
| Short vowel (open syllable) | 1μ |
| Long vowel / diphthong | 2μ |
| Foot-internal syllabic consonant | 1μ |
| Coda consonant (non-syllabic) | 0μ |
| Appendix nucleus | off-meter (ornamental) |

### 2.3 Worked example

Using dictionary forms (*Betty* /bɛi/, *Emma* /ɛma/, *really need* /ɻiːni/, *salt* /hoiom/, *face* /hoʔn̩ʔn̩ts/):

> *bɛi ɛma ɻiːni ‖ hoiom on hoʔnʔnts*
> "Betty Emma needs ‖ salt on her face"

Mora scan, ornamental-appendix treatment:

- Pāda 1: *bɛi* (1μ diphthong — or 2μ if /ei/ is parsed heavy) · *ɛma* (1μ+1μ) · *ɻiːni* (2μ+1μ)
- Pāda 2: *hoiom* (1μ+1μ, coda /m/ = 0μ) · *on* (1μ) · *hoʔnʔnts* (head /ho/ = 1μ; appendix /ʔn̩ʔn̩ts/ off-meter)

The line does not yet fill a fixed template — the example demonstrates that the quantitative tier can be *counted cleanly*, which is the precondition for building one. The distinctive aesthetic effect of option 3 is visible in *hoʔnʔnts*: a phonetically hefty word contributes a single metrical mora, its consonantal tail sounding as ornament against the count.

### 2.4 Open questions

- **Appendix treatment** [Open] — §1.4. Adopting option 1 or 2 instead would re-scan every appendix-bearing word and change the texture substantially.
- **Diphthong weight** [Open] — are /ei, oe, ia/ uniformly 2μ, or can some count light in the cadence (as in Greek *correptio*)? Depends partly on `phonology.md`'s still-open diphthong analysis.
- **Cadence template** — no fixed line-end shape is proposed yet; this is the natural next design step.

---

## 3. Alliterative verse

**Model:** Old English / Old Norse alliterative long line.
**Fit:** Strong on supply (§1.3); requires one convention decision on attachment.

### 3.1 Principle

The line has **four stressed (lifted) positions** divided by a medial caesura into two half-lines. Alliteration of the onsets of lifted positions binds the line: in the Germanic model, positions 1–2–3 alliterate and position 4 is free. Unstressed material between lifts is metrically free.

### 3.2 The attachment problem and proposed convention

Germanic alliteration attaches to **stressed-syllable onsets**. Conlang stress is final (`phonology.md` §3.3), so in a polysyllabic word the word-initial onset is usually *unstressed*. Two ways to resolve this:

- **(a) Head-foot onset** — alliteration attaches to the onset that begins the **head foot** (the foot bearing primary stress). *hoʔnʔnts* alliterates on /h/ because its head foot begins /ho-/, even though stress falls later within the appendix-bearing word.
- **(b) Word-initial onset** — alliteration attaches to the word-initial onset regardless of stress, decoupling alliteration from prominence entirely.

**Proposed convention: (a) head-foot onset** [Provisional]. It keeps alliteration tied to prominence, as in the source tradition, and for monosyllables (*ŕe* /ˈr̥ɛ/, *r̥eːʔ*) the two options coincide trivially.

### 3.3 Worked example

> *hoiom on hoʔnʔnts ‖ ŕe r̥eːʔ*
> /ˈhoiom on ˈhoʔn̩ʔn̩ts ‖ ˈr̥ɛ ˈr̥eːʔ/
> "salt on the face — today, a carrot"

Four lifts: *hóiom*, *hóʔnʔnts*, *ŕé*, *r̥éːʔ*.

- Positions 1–2 alliterate on /h/ (head-foot onsets).
- Positions 3–4 alliterate on /r̥/ (devoiced tap).

This is **richer** than the Germanic template, which binds only three of four lifts: the high frequency of /h/ onsets (debuccalized /s/, allophonic /k/) and the /r̥/ devoicing pattern make double-alliteration across the caesura easy to achieve. A house rule could *require* only 3 of 4 (Germanic-strict) or reward all 4 (conlang-rich) as an ornamental option.

### 3.4 Open questions

- **Attachment** [Provisional] — §3.2; convention (a) adopted provisionally.
- **Lift assignment in appendix-heavy words** — does a word like *hoʔnʔnts* occupy one lift or can its appendix host a secondary lift? Tied to the §1.4 appendix question.
- **Devoiced-rhotic alliteration** — do /r/ and /r̥/ alliterate with each other, or are they distinct alliterative classes? (`phonology.md`'s rhotic system, §1.2, makes this a real choice.)

---

## 4. Pitch-counterpoint verse (novel form)

**Model:** none — built from the conlang's pitch-stress dissociation (§1.2).
**Fit:** Native to the system; no natural-language precedent.

### 4.1 Principle

The line carries **two prosodic contours at once**:

- a **metrical tier** running on **stress** (the final-vocalic-position prominence of each word), and
- a **counterpoint tier** running on **pitch** (the GA-etymon prominence).

Because pitch and stress usually fall on different syllables, the two contours are **offset** within most words and **aligned** only where pitch and stress coincide (final-stress etyma, single-vowel reductions). The craft of the form is the placement of those alignments: a coincident word is a moment of **unison** in a line otherwise running on two independent melodic/rhythmic lines.

### 4.2 Proposed constraints [Provisional]

A line of *N* metrical positions (stresses) specifies:

- the **stress count** *N* (the metrical tier — e.g. four lifts, as in §3), and
- a **dissociation pattern**: which positions must be filled by dissociated words (pitch ≠ stress) and which by coincident words (pitch = stress).

The dissociation pattern is the form's signature, the way a rhyme scheme is for European verse. Example schemes:

- *D D D C* — three dissociated words building two-tier tension, resolving to unison at the cadence.
- *C D D C* — framed: unison at both edges, divergence in the middle.

### 4.3 Worked example

> *ɛma ɻiːni bɛi ‖ ɛmiː hoʔnʔnts*

| Word | Pitch on | Stress on | Status |
|---|---|---|---|
| *ɛma* | /ɛ/ | /a/ | dissociated |
| *ɻiːni* | /ɻiː/ (GA *really*) | /ni/ | dissociated |
| *bɛi* | /bɛ/ | /i/ | dissociated |
| *ɛmiː* | /ɛ/ | /iː/ | dissociated |
| *hoʔnʔnts* | /ho/ | /ho/ | **coincident (unison)** |

Read aloud, the stress contour and pitch contour are offset by one nucleus through the first four words, then snap into alignment on *hoʔnʔnts* at the line's end — a *D D D D C* cadence. The two tiers thread through each other and resolve to unison, an effect available *only* because of the dissociation.

### 4.4 Open questions

- **Pitch contrastiveness** [Open] — `phonology.md` §3.4 leaves open whether pitch placement is *contrastive* (minimal pairs by pitch alone). If pitch turns out non-contrastive, the counterpoint tier still exists phonetically but carries less structural weight; the form survives but its stakes change.
- **Coincidence inventory** — how many high-frequency words actually have coincident pitch/stress? The form needs a usable supply of unison words for cadences. A count against `dictionary.md` would settle this.
- **Notation** — a two-stave notation (one line for stress, one for pitch) may be the natural way to write this form down; worth designing if the form is pursued.
- **Interaction with §2 and §3** — the counterpoint tier is in principle orthogonal to the metrical tier and could overlay either a quantitative meter (§2) or an alliterative meter (§3). Whether all three tiers at once is composable or merely possible is untested.

---

## 5. Summary table

| Form | Counts / binds on | Phonological basis | Precedent | Fit | Key open question |
|---|---|---|---|---|---|
| Quantitative (§2) | Moras, light/heavy | Moraic system §1.1 | Sanskrit, Greek, Arabic | Strong | Appendix treatment §1.4 |
| Alliterative (§3) | Head-foot onsets | Onset frequency §1.3 | Old English/Norse | Strong | Attachment §3.2 |
| Pitch-counterpoint (§4) | Stress tier + pitch tier | Dissociation §1.2 | None | Native | Pitch contrastiveness §1.2 |

---

## 6. Versioning notes

### v1, May 2026 — initial draft

- Collected the five poetry-relevant phonological features (§1) from `phonology.md` v2.
- Sketched three forms: quantitative (§2), alliterative (§3), pitch-counterpoint (§4).
- Adopted provisional conventions: ornamental-appendix mora treatment (§2.2), head-foot-onset alliteration attachment (§3.2).
- Semantic parallelism deliberately excluded: it is a syntactic/semantic device independent of the morphophonology, so it carries into any language and tells us nothing specific about this one.
- All verse conventions here are proposals, not commitments; none feeds back into `phonology.md`.
