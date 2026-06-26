# Dictionary

A working lexicon for the conlang. Entries are sorted in conlang collation order (see §2). Each entry uses a template-style schema: fields may be omitted when not yet committed. Fields marked `[Open]` depend on phonological or grammatical questions still under analysis in `phonology.md` or `language_reference.md`.

This file is a living specification. As sound rules settle and grammar commits, entries should be revisited and updated.

---

## 1. Schema

Each entry is a level-3 heading (`### headword`). Below the heading:

- **`#### Etymology`** — A section opener. The proto-form in italics with asterisk, a dash, then a gloss. Semantic drift, register notes, and source-construction context are folded in as prose. Example: `*pass out* — colloquial "fall asleep" primary; "lose consciousness" secondary (salience inverted from GA).`
- **Form line:** Labeled fields on one line: `**Part of speech:** abbreviation  **IPA:** /…/  **Foot:** (…).` Example: `**Part of speech:** v.  **IPA:** /ˌbɛːˈsːoː/  **Foot:** (ˌH)(ˈH).`

Then, if committed, a **Phonological development** line: a compact semicolon-separated list of applied rules with brief labels. This is a derivation record, not a discussion.

Then **Cross-refs** if any: a single parenthetical or line linking related entries.

Then prose sections as needed:

- `#### Definition` — numbered glosses. Senses are grouped by part of speech where they differ (**Verb senses** / **Noun senses**), and verb senses may carry frame or cell tags — `(go-ahead)`, `(get-oneself)`, `(volitive perfect)` — where the meaning is frame-conditioned.
- Examples appear inline within the definition they illustrate, separated from the definition text by an em dash. Conlang form in italics, followed by the English translation in double quotes. No separate `#### Examples` heading.
- `#### Morphology` — inflected/derived forms when committed.
- `#### Notes` — observations genuinely specific to this form: irregular surface properties, optional realizations, notable phonotactic patterns. Not for propagation tickets, pending rule discussions, or paradigm-candidate flags — those go in the session changelog or target document.

Any section may be omitted. When a committed field depends on an unresolved question elsewhere, mark `[Open: see phonology §X]`.

---

## 2. Collation Order

The conlang alphabet, in sort order:

> a, ą, b, ð, e, ę, ä, h, i, ii, k, l, m, ḿ, n, ń, o, ǫ, p, r, rh, ŕ, s, ś, t, þ, w, w̃, y, ỹ

**Rules:**

1. Within a base letter's region, undiacriticked sequences sort first by Latin order on subsequent characters, then diacriticked forms follow.
   - Example a-region: `a` < `aa` < `au` < `aų` < `ą`
   - Example e-region: `e` < `ee` < `eu` < `eų` < `ę`
   - Example i-region: `i` < `ia` < `iu` < `ių` < `iyi` < `ĩ`
   - Example o-region: `o` < `oo` < `ou` < `oų` < `ǫ`

2. `ii` and `rh` are distinct phonemes, not digraph extensions of `i` and `r`, and have their own slots in the alphabet:
   - `i`-region (all `i`-initial sequences and `ĩ`) < `ii`-region (`ii`, `iia`, etc.)
   - `r` < `rh` < `ŕ` — the devoiced tap `ŕ` sorts last because devoiced `r` and devoiced `rh` collapse to a single phoneme, placed at the end of the rhotic series.

3. `ä` (formerly the ligature `ä`; orthography v3.1) is an independent letter slotted after the a-region. The former ligature `oë` is retired: the diphthong is now the digraph `oë` (orthography §3.4), which sorts within the o-region by rule 1, the diaeresis counting as a following diacritic.

4. Consonant diacritic forms (`ḿ`, `ń`, `ŕ`, `ś`, `w̃`, `ỹ`) follow their bare letter immediately, since consonants do not form length digraphs. (`š` retired, v3.3: /ʃ/ is written `sh`.)

5. `ð` takes the slot where `d` would be (after `b`); `þ` takes its own slot (after `t`).

---

## 3. Orthographic Notes

A few conventions clarified during early entry-writing, supplementing `orthography.md`:

- The diphthong `/ei/` (phonemically `/ey/`, with `y` /j/ as the glide) is written `ei`. This is distinct from the length digraph `eu` /ɛː/ — `e` followed by `i` is the diphthong, `e` followed by `u` is length.

- **Geminate `ss`** represents /sː/ (voiceless long). This works in concert with the rule that `s` is /z/ intervocalically and finally but /s/ in onset (where it derives from GA /st/, GA /s/ having debuccalized to /h/). The doubled `ss` is therefore the standard spelling for a voiceless geminate; the formal/pedagogical variant `śś` is also licensed. Now propagated to `orthography.md` §2.2 and §2.4.

- **/ʃ/ is written `sh`** (the hacek `š` is retired) — joining the `h`-digraph series `rh`, `th`, `sh`. Propagated to `orthography.md` §2.1 (v3.3).

- **Dotless `ı`** appears when one element of the `ii` digraph takes a diacritic: the marked element retains its dot, and the unmarked partner is written as `ı` to reduce visual clutter. Example: in *béntsıìy*, the stress grave lands on the second `i` of the `iiy` digraph (written `ì`), and the first `i` becomes `ı`. Now propagated to `orthography.md` §3.7.

- **Circumflex in headwords**: when pitch and stress coincide on the same vowel, the dictionary headword uses the circumflex (formal-register form) rather than the bare acute. Example: *nobêt* (pitch and stress both on /ɛ/). Earlier entries with coinciding pitch and stress (*ŕeut*, *hoʔnʔnts*, etc.) predate this convention and have not been retrofitted. Now propagated to `orthography.md` §3.7.

---

## 4. Entries

### baıĩ

#### Etymology
*money* — GA /ˈmʌni/.

**Part of speech:** n.  **IPA:** /bɑˈĩ/  **Foot:** [Open].

Phonological development: /m/ → /b/ [Open: word-initial /m/→/b/]; /ʌ/ → /ɑ/ `a`; intervocalic /n/ → ∅, leaving anticipatory nasalization on the following vowel; /i/ → nasalized /ĩ/ `ıĩ`.

#### Definition

1. money.

---

### barnkw

#### Etymology
*barnacle* — extended semantically from the marine crustacean's adhesive behavior to any form of persistent clinging or attachment, physical or emotional.

**Part of speech:** v.; also n.  **IPA:** /ˈbɑɾnkw̩/  **Foot:** (ˈH) with syllabic /w̩/ appendix.

Phonological development: /b/ onset unchanged; /ɑːɹ/ with pre-consonantal /ɹ/ → /ɑɾ/ (tap; no vowel lengthening — the /eː/ lengthening pathway applies to coda /ɹ/, not pre-consonantal) [Open: pre-consonantal /ɹ/→/ɾ/ rule not stated explicitly in §4.4]; /n/ unchanged (onset of unstressed syllable, not subject to E1); /ɪ/ → ∅ (E3: unstressed vowel elision); cluster-internal /k/ stays [Open: cluster-internal /k/ shielded from onset debuccalization? §4.4.1 lists onset /k/→/h/ without cluster conditioning]; /əl/: /ə/ → ∅ (E3), /l/ → /w̩/ (syllabic glide in post-stress appendix position).

#### Definition

**Verb senses:**

1. to hug tightly; to snuggle into.
2. to be stuck on; to be physically attached or adhered.
3. to cling; to be emotionally clingy or possessive.
4. to insist; to be unable to let go or move on.

**Noun senses:**

1. someone who barnacles; a clingy person.
2. a pimple; a zit.
3. nipple.

---

### baŕaumss

#### Etymology
*promise* — to promise, to give one's word.

**Part of speech:** v.  **IPA:** /bɑˈɾ̥ɑmsː/  **Foot:** (L)(ˈH) [Open].

Phonological development: word-initial /pr/ → /bɑˈɾ̥/ (prep-breaking, §4.4.5): the cluster breaks with an epenthetic /ɑ/ `a`, /p/→/b/, and /r/ → devoiced tap /ɾ̥/ `ŕ`; root /ɑ/ written `au`; /m/ retained; unstressed final /əs/ → geminate /sː/ `ss` (the reduced vowel coalesces into the sibilant, not a syllable-boundary gemination) [Open]. *(Revised from *beŕaumss* — epenthetic /ɛ/ — by B12, 2026-06-23, to follow prep-breaking.)*

#### Definition

1. to promise; to give one's word.

---

### baŕâuss

#### Etymology
*process* — the cognitive sense; the bureaucratic GA sense did not survive.

**Part of speech:** v.  **IPA:** /bɑˈɾ̥ɑsː/  **Foot:** (L)(ˈH) [Open].

Phonological development: word-initial /pr/ → /bɑˈɾ̥/ (prep-breaking, §4.4.5): epenthetic /ɑ/ `a`, /p/→/b/, /r/ → /ɾ̥/ `ŕ` (superseding the earlier *baurrâuss* derivation, which used /ɻ/ `rr` + epenthetic /ɑ/); root /ɑ/ written `âu`; final /ɛs/+/s/ → geminate /sː/ `ss` (E3 elision feeding the geminate). [Open: the B12 study writes this headword *baŕâustts* (coda ⟨stts⟩); that coda revision is not derivable from the current rules — only the onset has been standardized to prep-breaking here. Confirm the intended coda.]

#### Definition
1. to process; to work through over time. 2. *(get-oneself, imperfect)* to be coming to terms with — threshold-flavored.

---

### baŕep

#### Etymology
*prep* — everyday "to cook"; the frame-free Latinate route the helper-verb policy prefers (`verbal-system.md` §13.3).

**Part of speech:** v.  **IPA:** /bɑˈɾ̥ɛp/  **Foot:** (L)(ˈH) [Open].

Phonological development: word-initial /pr/ → /bɑˈɾ̥/ (prep-breaking, §4.4.5): epenthetic /ɑ/ `a`, /p/→/b/, /r/ → /ɾ̥/ `ŕ`; root /ɛ/ retained; final /p/ retained — no word-final voicing needed (the earlier *preb* /ˈprɛb/ analysis posited an unexplained final /p/→/b/; that flag is now moot, since the word simply ends in /p/).

#### Definition
1. to cook; to prepare (food). 2. to prep; to ready.

---

### bárkennò

#### Etymology
*parking lot* — the full compound, lexicalized as a single noun.

**Part of speech:** n.  **IPA:** [Open]  **Foot:** [Open].

Phonological development: /p/ → /b/ onset [Open: before /ɑ/, the §4.4.1 refinement nominally blocks /p/→/b/; onset /p/→/b/ before /ɑ/ would extend the rule — new environment]; /ɑːɹk/ with pre-consonantal /ɹ/: /ɹ/→/ɾ/, /ɑ/ stays short (pre-consonantal, not coda) → /ɑɾ/ → `ar`; cluster-internal /k/ stays [Open: see *barnkw*]; /ɪ/ → ∅ or /ɛ/ [Open: unstressed /ɪ/ treatment]; /ŋl/ → /nː/ [Open: the §4.4.1 /nd/→/nː/ rule is regressive assimilation; /ŋl/→/nː/ would require a separate rule or a generalization — /ŋ/→/n/ by place assimilation to following lateral, then /nl/→/nː/ geminate]; *lot* /lɑt/: /l/ onset → [Open: onset /l/ treatment]; /ɑ/ → /o/ [Open: /ɑ/→/o/ not in §4.4.2]; /t/ → /ʔ/ (E2a) → appears to drop in the headword.

#### Definition

1. parking lot; car park.

---

### baunnw

#### Etymology
*ponder* — slow, comfortable turning-over of a thought.

**Part of speech:** v.  **IPA:** /ˈbɑnːw̩/  **Foot:** (ˈH) with syllabic /w̩/ appendix.

Phonological development: /p/→/b/ [Open: word-initial before /ɑ/ — outside both pass-out environments; see changelog]; /nd/→/nː/ (stand-out leveling); /ər/→/w̩/ (appendix).

#### Definition
1. to ponder; to mull over. 2. to sit with (a feeling, a decision) without urgency — *(get-oneself, imperfect)* unbidden rumination.

---

### baurrits

#### Etymology
*bridge* — GA /brɪdʒ/.

**Part of speech:** n.  **IPA:** /bɑˈɻɪts/  **Foot:** [Open].

Phonological development: /b/ retained; epenthetic /ɑ/ `au` breaks the cluster (not lengthened) — the **voiced sibling of prep-breaking** (§4.4.5): the same /ɑ/-epenthesis as /pr/, but the rhotic stays voiced /ɻ/ (no devoicing, since the stop is voiced); GA /ɻ/ retained (the *r* of *bridge* — broad GA "r" = /ɻ/), spelled `rr`, the **non-initial spelling of `rh`** [pending `orthography.md` propagation — see changelog]; /ɪ/ retained; /dʒ/ → /ts/ [Open: affricate /dʒ/→/ts/]. Attested in the *reś* example *Nou baurrits…* "(you) know the bridge…".

#### Definition

1. bridge.

---

### baurzıĩ

#### Etymology
*barge in* — "enter" (the abruptness bleached in the neutral sense); the interjection keeps the inviting force.

**Part of speech:** (1) v., (2) interj.  **IPA:** /bɑɾˈzĩ/  **Foot:** (H)(ˈL) [Open].

Phonological development: /b/ retained; /ɑːr/ → /ɑɾ/ (rhotic kept as tap, `aur`); /dʒ/ → /z/ [Open: affricate /dʒ/→/z/ — not in §4.4]; *in* /ɪn/ → nasalized /ĩ/ `ıĩ` (§3.6). Stress falls on the *in* particle, as is typical for prepositional-verb sources.

#### Definition

1. to enter; to come/go in.
2. (interj.) come on in!; come in!

---

### bauwouwou

#### Etymology
Onomatopoeic — imitates the sound of General American speech; reduplicative.

**Part of speech:** ideophone (IDEO).  **IPA:** /bɑwoːˈwoː/  **Foot:** [Open] (ultimate-syllable stress; reduplication).  **[IPA Provisional — pending phonology pass, `ideophones.md` §2.]**

Phonological development: reduplicative onomatopoeia, not a regular derivation [Provisional]. Phonotactically exempt (`ideophones.md` §5).

#### Multimodality
χ wrist rotation, "and so on" (shared with *rekriiâ*).

#### Definition

1. (ideophone) speaking in General American; the manner of GA speech. Canonical class home: `ideophones.md`.

---

### bawiiquoh?

#### Etymology
*what-we-call-home* — a descriptive circumlocution as etymon, suggesting this is a grammaticalized compound rather than a phonological borrowing of a GA simple word. The `?` in the headword may represent a phonemicized question or evidential particle built into the compound form.

**Part of speech:** n.  **IPA:** [Open — compound form]  **Foot:** [Open].

Phonological development: [Open — morphological compound; phonology of component parts pending analysis in a dedicated session].

#### Definition

1. home; one's domestic residence; what we call home.

#### Notes

The etymon "what-we-call-home" and the `?` character in the headword both suggest this is not a simple phonological derivation but a lexicalized periphrastic compound, likely involving morphological elements not yet analyzed. Cross-reference *beušiioskô*, *bewii·iit*, *bewiipessô* (parallel descriptive-circumlocution compounds).

---

### bayarę

#### Etymology
*violin* — borrowed via phonological adaptation.

**Part of speech:** n.  **IPA:** /bɑˈjɑɾɛ̃/  **Foot:** (L)(ˈL) [Open: final syllable may be heavy if /ɛ̃/ is long].

Phonological development: /v/ → /b/ onset [Open: /v/→/b/ environment; see *béntsıìy*, *boëś*]; /aɪ/ → /ɑ/ + glide /j/ retained as a separate segment [Open: expected reflexes of /aɪ/ are /eː/ or short /i/ per §4.4.2; /ɑ/+/j/ outcome is unattested — new conditioning environment or new rule]; /ə/ → ∅ (absorbed, E4); /l/ → /ɾ/ [Open: /l/→/ɾ/ not in §4.4.1; onset /l/ has no stated merger to tap; flag for phonology session]; /ɪn/: /n/ elides intervocalically (E1), nasalization transfers to /ɪ/ (S1) → /ɛ̃/ (lowering of /ɪ/ in this position [Open: /ɪ/→/ɛ/ under nasalization? not stated in §4.4.2]) → `ę`.

#### Definition

1. violin.

---

### bäeĩyi

#### Etymology
*manager* — GA /ˈmænɪdʒər/.

**Part of speech:** n.  **IPA:** /bæˈɛ̃ĩj̃ː/  **Foot:** [Open].

Phonological development [Open, heavy reduction]: /m/ → /b/ [Open]; /æ/ retained `ä`; the medial /nɪdʒ/ reduces, leaving a nasalized nucleus /ɛ̃ĩ/ `eĩ` [Open]; the final `yi` realizes phonemic /j̃ː/ (phonetically ≈ [jɪ]). (`ä` = /æ/.)

#### Definition

1. manager.

---

### bąêų

#### Etymology
*banana* — the fruit; no semantic shift.

**Part of speech:** n.  **IPA:** /bɑ̃ˈɛ̃ː/  **Foot:** (L)(ˈH).

Phonological development: /bəˈnænə/ — both intervocalic /n/ elide (E1), each transferring nasalization to adjacent vowels (S1); initial /ə/ → /ɑ/ (E5 strengthening) + nasalized by left-flanking residue of first /n/ → /ɑ̃/ → `ą`; /æ/ (V₂) + nasalization from both flanking /n/ elisions → /ɛ̃/ via /æ/-before-nasal pathway (§4.4.2) with duration preserved; final /ə/ (V₃) absorbed into /ɛ̃/ as length suffix → /ɛ̃ː/ → `êų` (circumflex on ê: pitch + stress coincide; ogonek on ų: nasal long vowel).

#### Definition

1. banana.

---

### bekw

#### Etymology
*bicker* — to argue, to squabble.

**Part of speech:** v.  **IPA:** /ˈbɛkw̩/  **Foot:** (ˈL)(L) [Open].

Phonological development: /b/ retained; /ɪ/ → /ɛ/ [Open: /ɪ/→/ɛ/ candidate rule — pending phonology session]; /k/ retained; GA *-er* /ər/ → syllabic /w̩/ appendix, written `w` — the etymological /r/ surfaces only in the progressive. Progressive-shaped *bekrrıĩ* [Open: pending §3.22 morphophonology / B12 — the linking-*r* return].

#### Definition

1. to argue; to bicker; to squabble.

---

### belkm

#### Etymology
*welcome* — GA /ˈwɛlkəm/. The "you're welcome" response; the reduplicated *belkmlkm* is a welcoming greeting.

**Part of speech:** n./interj.  **IPA:** /ˈbɛlkm̩/ (reduplicated *belkmlkm* /ˈbɛlkm̩lkm̩/)  **Foot:** [Open].

Phonological development: /w/ → /b/ [Open: word-initial /w/→/b/]; /ɛl/ retained; /kəm/ → /km̩/ (schwa syncope, syllabic /m̩/).

#### Definition

1. (interj.) you're welcome.
2. (reduplicated *belkmlkm*) a welcoming greeting; "welcome!"

---

### bemmw

#### Etymology
*remember* — the recall event; the frames distribute GA's *remember/recall/reminisce* space (see *rhemmêś*).

**Part of speech:** v.  **IPA:** /ˈbɛmːw̩/  **Foot:** (ˈH) with syllabic /w̩/ appendix.

Phonological development: unstressed /rɪ-/ → ∅ [Open: aphesis — §5 backlog]; /m/→/b/ (bat-mat); /mb/→/mː/ [New rule needed: homorganic nasal-stop leveling — stand-out parallel]; /ər/→/w̩/.

Cross-refs: *rhemmêś*; *nott* (deliberate fixing-in-memory).

#### Definition
1. to remember; to recall. 2. *(get-oneself, perfect)* to suddenly remember; *(imperfect)* to have it coming back.

#### Morphology
Linking *r* before vowel-initial suffixes: *bemmorret*, *bemmorreųt* (`phonology.md` §4.4.3).

---

### béntsıìy

#### Etymology
*eventually* — from colloquial GA /vɛnt͡ʃ.li/; the GA reluctant-deferral connotation is not inherited.

**Part of speech:** adv.  **IPA:** /bɛntsˈiː/  **Foot:** (L)(ˈH).

Phonological development: /v/ → /b/ in onset [Open: §4.4.1 gives general /v/ → /r/ via the tap merger; onset /v/ → /b/ is a new environment not yet in §4.4]; /t͡ʃ/ spreads palatalization to adjacent /ɫ/ → /j/; /t͡ʃ/ then depalatalizes to /ts/ (§4.4.1); /ji/ → /iː/ smoothing [Open: §4.4.1 conditions /ɫ/ → /j/ on both flanks being high front vowels; left flank here is palatal consonant /t͡ʃ/ — extended environment or separate rule]; /n/ not intervocalic in /nt/ cluster, so E1 does not fire and /ɛ/ is not nasalized.

Cross-refs: *nobêt* (deictic counterpart).

#### Definition

1. *(adv.)* later; at a subsequent time.

#### Notes

Anaphoric — anchors to the contextually available reference time, not necessarily speech time. Compatible with both prospective and retrospective/narrative use. Contrast *nobêt*: deictic, proximal, prospective-only.

---

### benıîä

#### Etymology
*vanilla* — the flavor/plant; no semantic shift.

**Part of speech:** n.  **IPA:** /bɛˈniæ/  **Foot:** (L)(ˈH) [Open: whether final /æ/ is a separate light syllable or part of a diphthongal heavy nucleus with /i/].

Phonological development: /v/ → /b/ onset [Open: /v/→/b/ environment; see *béntsıìy*, *boëś*]; initial unstressed /ə/ → /ɛ/ (E5) → `e`; /n/ does not elide [Open: E1 targets intervocalic /n/; in *vanilla* the /n/ is onset of the stressed syllable between two vowels — possible blocking of E1 in stressed-onset position; needs rule statement]; stressed /ɪ/ + /j/ glide (from /ɫ/→/j/ between flanking high front vowels /ɪ/ and /ə/) → /iː/ → `ıî` (circumflex = pitch + stress coincide) [Open: left flank is /ɪ/, right flank /ə/ — §4.4.1 conditions /ɫ/→/j/ on *high front vowel* flanks; /ə/ is not high front]; final /ə/ strengthens to /æ/ [Open: /ə/→/æ/ in word-final position rather than expected /a/ from E5; new conditioning].

#### Definition

1. vanilla (the flavor and the plant).

---

### benkwtt

#### Etymology
*banquet* — generalized from feast to any meal.

**Part of speech:** n.  **IPA:** /ˈbɛnkwʔ/  **Foot:** (ˈH) with appendix [Open].

Phonological development: the GA input already supplies short raised [ɛ] for pre-/ŋk/ *a* (speaker judgment; conditioning hunch: the syllable-final /k/ — *bank* vs. *bang* length; input-dialect note, not a conlang rule); /ŋk/ → /nk/ (no /ŋ/ phoneme — [ŋ] is the /n/ allophone before /k/; see changelog); /ət/: E3, /t/→/ʔ/ `tt` (§2.7).

#### Definition
1. a meal. 2. a feast; a spread (emphatic).

---

### benskyi

#### Etymology
*minuscule* — the adjective; no semantic shift.

**Part of speech:** adj.  **IPA:** /bɛnˈski/  **Foot:** (H)(ˈL).

Phonological development: /m/ → /b/ (§4.4.1 /m,p/→/b/ in onset); /ɪ/ (V₁) → /ɛ/ [Open: /ɪ/→/ɛ/ rule; see *nobêt*]; /n/ does not elide [Open: same stressed-onset blocking question as *benıîä*]; /ɪ/ (V₂) → ∅ (E3: unstressed vowel, cluster-feeding position); /sk/ cluster-internal → both segments stay [Open: onset /s/ debuccalizes to /h/ normally; cluster position may shield it — not stated in §4.4.1]; /j/ (from /kj/) → /j/ → `y`; /uːl/: /uː/ → /ɪ/ (§4.4.2 back-vowel fronting, short reflex), /l/ → ∅ (E2c coda-singleton elision) → /ɪ/ → `i`.

#### Definition

1. small; tiny; minuscule.

---

### bényǫ

#### Etymology
*opinion* — the noun, retained; not verbalized (B12 elicitation, 2026-06-23: *opinion* does not become a verb).

**Part of speech:** n.  **IPA:** /bɛˈnjõ/ [Open: medial cluster]  **Foot:** [Open].

Phonological development: initial /ə/ → ∅ [Open: aphesis]; /p/→/b/ (pass-out, medial at the etymon stage); /ɪ/→/ɛ/ [Open: lowering]; /jən/→/jõ/ (§3.6). Pitch: high on *é* (etymon stress); the final *ǫ* carries stress and an implied grave — the pitch mark folds under the ogonek (orthography §3.1 fold hierarchy).

#### Definition
1. an opinion; a view.

---

### beńt

#### Etymology
*mint* — the herb, flavor, and candy type; no semantic shift.

**Part of speech:** n.  **IPA:** /bɛn̥t/  **Foot:** (ˈH) heavy monosyllable.

Phonological development: /m/ → /b/ (§4.4.1); /ɪ/ → /ɛ/ [Open: /ɪ/→/ɛ/ rule]; coda /nt/ cluster: /t/ devoices /n/ → /n̥/ → `ń`; /t/ remains word-final [Open: E2a predicts coda /t/→/ʔ/; retention of surface /t/ here is unexpected — possible blocking in coda-cluster position, or the devoiced /n̥/ feeds a different coda treatment].

#### Definition

1. mint (the herb).
2. mint flavor; anything mint-flavored.

---

### béo·ò

#### Etymology
*bit ago* — the temporal phrase "a little bit before (now)"; narrowed to the short interval just preceding speech time.

**Part of speech:** adv.  **IPA:** /bɛˈoo/  **Foot:** (L)(ˈL)(L) [Open: foot structure of the /oo/ hiatus sequence].

Phonological development: *bit* /bɪt/: /b/→/b/; /ɪ/→/ɛ/ [Open: /ɪ/→/ɛ/ rule]; /t/→/ʔ/ (E2a) → lexical drop [Open: /ʔ/-drop here is not in a grammaticalized particle; if the /ʔ/ is simply silent, or if it merges with the following vowel onset, needs rule statement]; initial /ə/ of *ago* → /o/ [Open: /ə/→/o/ not fully stated in §4.4.2; see *nobêt* for a parallel]; /ɡ/ elides (E1: intervocalic tap-merger consonant) → hiatus; /oʊ/ → /o/; resulting /o.o/ hiatus retained → `o·ò` (interpunct marks hiatus; grave on final `ò` = stress in formal register). Pitch on /bɛ/ (GA primary stress on *bit*); stress on final /o/.

#### Definition

1. *(adv.)* a little bit before (this moment); just a short time ago.

Cross-refs: *rıírǫ* (general "approximately; around"); *récquıìś* (also; likewise — different temporal reference direction).

---

### bessts

#### Etymology
*message* — the verb "to send a message to someone"; digital/text communication primary.

**Part of speech:** v.  **IPA:** /ˈbɛsːts/  **Foot:** (ˈH) heavy monosyllable.

Phonological development: /m/ → /b/ (§4.4.1); /æ/ → /ɛ/ (short reflex); /s/: gemination [Open: the /s/→/sː/ gemination rule applies at the syllable boundary preceding stress; in *message* the stressed syllable is the first (/ˈmæs/), so the /s/ is not preceding stress but within the stressed syllable — rule environment unclear for this case]; /ɪ/ → ∅ (E3); /dʒ/ → /ts/ [Open: /dʒ/ is in E1's intervocalic set; in word-final coda position with no following vowel, coda /dʒ/ treatment is unspecified — /dʒ/→/ts/ by partial devoicing is a plausible path but not a stated rule].

#### Definition

1. to send a message to (someone); to text; to DM.

---

### bet bät

#### Etymology
*pitter-patter* — onomatopoeic; the two beats with an expressive /ɛ/~/æ/ vowel alternation.

**Part of speech:** ideophone (IDEO), onomatopoeia.  **IPA:** /ˈbɛt ˈbæt/  **Foot:** [Open].  **[IPA Provisional.]**

Phonological development: *pitter-patter* compressed to two beats *bet bät*; expressive vowel alternation [Provisional]. (`ä` = /æ/.) Phonotactically exempt (`ideophones.md` §5).

#### Definition

1. (onomatopoeia) the sound of pattering — light rapid footfalls or rain; "pitter-patter." Enters a clause as an onomatopoeia-object via *-ðs* (`ideophones.md` §4). Canonical class home: `ideophones.md`.

---

### béuksoè

#### Etymology
*backstory* — from the colloquial GA compound *back* + *story*; all three senses are extensions of "the narrative behind something."

**Part of speech:** n.  **IPA:** /ˈbɛːk.soɛ/  **Foot:** (ˈH)(L) [Open].

Phonological development: *back* /bæk/: /b/→/b/; /æ/→/ɛː/ (§4.4.2 /æ/→/eː/ pathway) → `éu`; coda /k/ → [Open: coda /k/→∅ per §4.4.1, but headword retains /k/ — possible cluster-shielding if /k/ is reanalyzed as onset of second syllable, but then onset /k/→/h/; /k/ surface retention unexplained]; *story* /ˈstɔːɹi/: /st/→ stays? [Open: /st/→/ts/ applies in onset; here /s/ is onset of the second component → /s/ onset stays as /s/]; /ɔːɹ/ coda → /o/ (§4.4.2 /or/→/oː/ pathway, shortened); final /i/ → [Open: /i/ in final position → syllabic /j/ or stays? headword shows bare `è` = stressed /ɛ/].

#### Definition

1. reason; explanation; excuse.
2. childhood; personal history; the backstory of a person's development.
3. history (general); the narrative record of how something came to be.

---

### beušiioskô

#### Etymology
*where-she-goes-to-school* — a descriptive circumlocution as etymon; a grammaticalized compound form designating the institution.

**Part of speech:** n.  **IPA:** [Open — compound form]  **Foot:** [Open].

Phonological development: [Open — morphological compound; phonology of component parts pending analysis in a dedicated session. See *bawiiquoh?*, *bewii·iit*, *bewiipessô* for parallel constructions.]

#### Definition

1. school; educational institution.

#### Notes

Like *bawiiquoh?* and the *bewii-* compounds, the etymon is a periphrastic description rather than a GA simple word. The `beušiioskô` form likely encodes morphological elements (locative, subject agreement, or directional) — full analysis deferred to a dedicated morphology session.

---

### beusp

#### Etymology
*massive* — the adjective; narrowed to physical size (not intensity or scale).

**Part of speech:** adj.  **IPA:** /bɛːsp/  **Foot:** (ˈH) heavy monosyllable.

Phonological development: /m/ → /b/ (§4.4.1); /æ/ → /ɛː/ (§4.4.2 /æ/→/eː/) → `eu`; /s/: non-onset /s/ before further consonants [Open: coda /s/ treatment — expected /z/ by non-onset default, but surface /s/ here; devoicing by adjacent voiceless context?]; /ɪ/ → ∅ (E3: unstressed, cluster-feeding); /v/ → /b/? → /p/ [Open: coda /v/ treatment not in §4.4.1; /v/ → /b/ in onset is the flagged-open rule; coda /v/ might devoice to /f/→/θ/ via /f/→/θ/ rule, or → /p/ by labial stop]; the resulting coda cluster `sp` is the final form.

#### Definition

1. large; big; massive.

Cross-refs: *benskyi* (antonym: small, tiny).

---

### beussou

#### Etymology
*pass out* — colloquial "fall asleep from fatigue" primary; "lose consciousness" secondary (salience inverted from GA).

**Part of speech:** v.  **IPA:** /ˌbɛːˈsːoː/  **Foot:** (ˌH)(ˈH).

Phonological development: /pʰ/ → /b/ before /ɛ, ɛː/ (committed; `phonology.md` §4.4.1); /æ/ → /ɛː/; /s/ geminates to /sː/ at stressed-syllable boundary rather than debuccalizing; /aʊ/ → /oː/; coda /ʔ/ dropped (lexically conditioned in grammaticalized particles; careful-speech variant /ˌbɛːˈsːoːʔ/ exists). Progressive-shaped form *beussno* [Open: pending §3.22 morphophonology / B12].

#### Definition

1. to fall asleep from fatigue; to sleep heavily.
2. to lose consciousness; to faint.

---

### beųtw

#### Etymology
*bento* — the Japanese-origin word for a portioned lunch box, now used generally for any packed meal brought to work or school.

**Part of speech:** n.  **IPA:** /bɛ̃ːtw̩/  **Foot:** (ˈH) with syllabic /w̩/ tail.

Phonological development: /b/→/b/; /ɛn/: /n/ elides (E1: treated as intervocalic between the stressed /ɛ/ and following coda cluster) [Open: E1 canonically targets intervocalic consonants between full vowels; here /n/ is in coda before /t/ — whether E1 fires in this environment is unresolved]; nasalization on /ɛ/ (S1) → /ɛ̃/; length of /ɛ̃ː/ [Open: source of length unclear — possible compensatory lengthening after /n/-elision (not a stated rule), or analogical extension of `eu`-digraph for long vowels]; /t/ stays [Open: E2a predicts /t/→/ʔ/; cluster-position blocking?]; /oʊ/ → /oː/ → syllabic /w̩/ in appendix position (§4.3 step 7).

#### Definition

1. lunch; any portioned meal packed for consumption away from home, especially for school or work.

---

### bewii·iit

#### Etymology
*where-we-eat* — descriptive circumlocution; grammaticalized compound.

**Part of speech:** n.  **IPA:** [Open — compound form]  **Foot:** [Open].

Phonological development: [Open — morphological compound; pending analysis. See *bawiiquoh?*, *beušiioskô*, *bewiipessô* for parallel constructions.]

#### Definition

1. dining table; the place where meals are eaten together.

---

### bewiipessô

#### Etymology
*where-we-pass-out* — descriptive circumlocution based on *beussou* (to fall asleep from fatigue); grammaticalized compound.

**Part of speech:** n.  **IPA:** [Open — compound form]  **Foot:** [Open].

Phonological development: [Open — morphological compound; the `bewii-` element likely encodes a locative or directional morpheme; `-pessô` contains *beussou*-stem material. Pending dedicated morphology session.]

Cross-refs: *beussou* (to fall asleep; stem of the `-pessô` component); *bewii·iit*, *bawiiquoh?*, *beušiioskô* (parallel compounds).

#### Definition

1. bed.

---

### beikw

#### Etymology
*vehicle* — broadened from private car to any motor vehicle.

**Part of speech:** n.  **IPA:** /ˈbɛjkw̩/  *(headword respelled from* beykw *for §3.4 `ei` conformance, v3.1)*  **Foot:** (ˈH) with syllabic /w̩/ tail.

Phonological development: /v/ → /b/ onset [Open: /v/→/b/ environment; see *béntsıìy*]; /iː/ → /ɛ/ [Open: /iː/→/ɛ/ not in §4.4.2; expected reflex of GA /iː/ is /iː/ or possibly /i/; short /ɛ/ outcome would require a new rule]; /ɪ/ → /j/ (glide formation in hiatus with preceding /ɛ/) → `y` [Open: /ɪ/→/j/ conditioned by hiatus; not the same environment as the /ɫ/→/j/ rule in §4.4.1]; /k/ cluster-internal stays [Open: see *barnkw*]; /l/ → /w̩/ (syllabic glide, E2c + final position) → `w`.

#### Definition

1. car; automobile.
2. any motor vehicle, including buses and trucks.

---

### beiskiiy

#### Etymology
*basically* — discourse adverbial.

**Part of speech:** adv.  **IPA:** /beiˈskiː/  **Foot:** [Open].

Phonological development [Open]: /b/ retained; /eɪ/→/ei/ `ei`; medial /ɪ/ syncope → /sk/; /li/→/iː/ `iiy`.

#### Definition

1. (adv.) basically; in essence.

---

### bęiink

#### Etymology
*panic* — the verb, with semantic extension to worry and apprehension.

**Part of speech:** v.  **IPA:** /bɛ̃ˈink/  **Foot:** (L)(ˈH) [Open: whether the /ɛ̃/ syllable is light or heavy].

Phonological development: /p/ → /b/ (§4.4.1); /æ/ + following /n/ → /ɛ̃/ (/æ/-before-nasal pathway §4.4.2, short reflex) [Open: §4.4.2 predicts /ɛː/ long; short /ɛ̃/ here suggests the length component is blocked when /n/ stays as onset rather than eliding]; /n/ stays as onset of second syllable (E1 blocked — /n/ is onset of unstressed syllable adjacent to a stressed vowel, same blocking environment as *benıîä* and *benskyi*); /ɪ/ → /i/ (tense short) [Open: /ɪ/→/i/ tense promotion not in §4.4.2]; /k/ in coda stays [Open: coda /k/→∅ expected per §4.4.1; retention unexplained].

#### Definition

1. to be scared; to be frightened.
2. to worry; to feel anxious about.
3. to deem unfortunate; to dread (a situation or outcome).

---

### boëś

#### Etymology
*voice* — the noun; semantic range matches GA closely.

**Part of speech:** n.  **IPA:** /boes/  **Foot:** (ˈH) heavy monosyllable (diphthong nucleus).

Phonological development: /v/ → /b/ onset [Open: /v/→/b/ environment; same flag as *béntsıìy*; contrast *reųś*, *rékwıì* where /v/ → /r/ — possible conditioning by following vowel quality]; /ɔɪ/ → /oe/ (diphthong; same pathway as *boë* ← *boy*) [Open: orthographic note — established grapheme for /oe/ is the ligature `oë`; `boeś` written without ligature may represent hiatus /bo.ɛs/ rather than the diphthong /boes/ — user confirmation needed]; final /s/ → /s/ (devoiced, written `ś`: GA /s/ was voiceless; non-onset default is /z/, so devoicing mark required to preserve voicelessness).

#### Definition

1. voice (the acoustic signal produced by the vocal tract).

Cross-refs: *boë* (same /ɔɪ/→/oe/ derivation from *boy*).

---

### boë

#### Etymology
*boy* — the noun; no semantic shift.

**Part of speech:** n.  **IPA:** /boe/  **Foot:** (ˈH) heavy monosyllable (diphthong nucleus).

Phonological development: /b/→/b/; /ɔɪ/→/oe/ (diphthong → `oë`) [Open: /ɔɪ/→/oe/ not explicitly stated in §4.4.2, which lists /ai/→/eː/~/i/ but not /ɔɪ/; this is a likely new rule or sub-case needed]; no coda consonant.

#### Definition

1. boy; male child or young man.

Cross-refs: *boëś* (same /ɔɪ/→/oe/ derivation from *voice*).

---

### bǫëiio

#### Etymology
*morning joe* — colloquial for coffee (esp. morning coffee).

**Part of speech:** n.  **IPA:** [Open: ≈ /bõˈɛiio/; compound vowel sequence unsettled]  **Foot:** [Open].

Phonological development [Open, compound]: *morning* → *bǫ* /bõ/ (/m/ → /b/; heavy reduction with nasalization) [Open]; *joe* → *ëiio* [Open: diphthong/hiatus shape].

#### Definition

1. coffee, esp. morning coffee.

---

### -ðs

#### Etymology
*this* — the onomatopoeia-object marker (clitic): introduces a sound-word as the thing perceived (`ideophones.md` §4).

**Part of speech:** clitic (onomatopoeia-object marker).  **IPA:** /-ðs/  **Foot:** —.

Phonological development: *this* /ðɪs/ → /-ðs/ (vowel syncope; /ð/ + /s/).

#### Definition

1. (marker) introduces an onomatopoeia/ideophone as a perceived object: *…riprprp -ðs* "…the drip-drip-drip." (`ideophones.md` §4.)

---

### e

#### Etymology
*egg* — the food item; no semantic shift.

**Part of speech:** n.  **IPA:** /ɛ/  **Foot:** (ˈL) light monosyllable.

Phonological development: /ɛ/ → /ɛ/ (unchanged); coda /g/ → ∅ [Open: §4.4.1 specifies coda /k/→∅; coda /g/ (voiced counterpart) is not listed — analogous loss assumed; or /g/ elides via E1 if treated as being between a vowel and silence, but that environment is non-standard]. Pitch and stress coincide on the only vowel; casual orthography = bare `e`; formal = `ê`.

#### Definition

1. egg (especially a bird or chicken egg as food).

---

### eiem

#### Etymology
*A.M.* — the initialism (morning).

**Part of speech:** n.  **IPA:** /ˈeiɛm/  **Foot:** [Open].

Phonological development: spelled-out initialism — letter-names *A* /eɪ/ + *M* /ɛm/ → /ˈeiɛm/, stress on the first letter-name (parallel to *piiem*).

#### Definition

1. A.M.; the morning.

---

### emmáwwè

#### Etymology
*in what way* — the interrogative phrase, lexicalized as a single adverb.

**Part of speech:** adv. (interrogative).  **IPA:** /ɛmːˈɑwːɛ/  **Foot:** [Open].

Phonological development: [Open — the reduction of a three-word phrase /ɪn.wʌt.weɪ/ to a single phonological word involves several steps not individually attested: initial /ɪn/ + adjacent /w/ of *what* → /m/ (possible labial assimilation of /n/ before /w/) → /mː/ (gemination of boundary /m/); /wʌt/: /ʌ/→/ɑ/ (§4.4.2 /u,ʊ,ʌ/→/ɨ/ pathway; short /ɑ/ reflex), /t/→/ʔ/→drops; /weɪ/: /w/→/wː/ (gemination at boundary?) → /wː/ → `ww`; /eɪ/→/ɛ/ → `è`. Most steps are unattested; this entry records the headword as given with the full derivation flagged for a dedicated session.]

#### Definition

1. how; in what way; by what means.

---

### eńhii

#### Etymology
Adverb "inside; internally." [Etymon [Open].]

**Part of speech:** adv.  **IPA:** /ɛˈn̥hi/  **Foot:** [Open].

Phonological development [Open: etymon/derivation pending]; `ń` = devoiced /n̥/; `h` = breathy.

#### Definition

1. (adv.) inside; internally.

---

### eplii

#### Etymology
*to apply* — GA /əˈplaɪ/, a plain /pl/ onset cluster (no gemination — reanalyzed 2026-06-23, B12 corrections; the earlier *epplii* analysis posited a spurious ambisyllabic /pp/).

**Part of speech:** v.  **IPA:** /ˈɛpli/  **Foot:** [Open].

Phonological development: initial unstressed /ə/ → /ɛ/ (the apply onset, E5; committed, `phonology.md` §4.4.9); /pl/ onset cluster retained (no geminate); /aɪ/ → short /i/ (the price splinter) [Open: conditioning — see `phonology.md` §5.1 data-gathering bucket].

Cross-refs: *rhiiy* (morpheme entry for the `rhiiy-` prefix); *rhiiysseunnou*, *rhiiynii* (parallel `rhiiy-` prefix in alternative form *rhiiyeplii*).

#### Definition

1. to put, place, or spread something on something else (paint, ointment, a label).
2. to put effort into a task; to try with real effort. Sense 2 admits the alternative form *rhiiyeplii* (with the `rhiiy-` intensifier prefix, still transparent here — unlike its fully-bleached form in *rhiiysseunnou* and *rhiiynii*).
3. to apply for (a job, position, program).

---

### éuskrıì

#### Etymology
*icecream* — the compound noun; no semantic shift.

**Part of speech:** n.  **IPA:** /ɛːˈskɾi/  **Foot:** (H)(ˈL).

Phonological development: *ice* /aɪs/: /aɪ/ → /ɛː/ (§4.4.2 /ai/→/eː/ pathway) → `éu`; pitch stays on this syllable (GA primary stress on *ice*). At the *ice-cream* juncture, the /s/ of *ice* meets the /kr/ onset of *cream* → resulting cluster /skɾ/ [Open: onset /k/ normally debuccalizes to /h/; in the cluster /sk/, the /k/ is shielded — or /kr/→/ɾ̥/ (§4.4.1) collapses the cluster differently; exact path unclear]. *cream* /kriːm/: /r/ → /ɾ/ (tap); /iː/ → /i/ short (secondary stress, final vocalic position in conlang) → `ıì` (dotless `ı` = first element of `ii` with following diacritic; grave `ì` = stress); /m/ in coda → ∅ [Open: coda /m/ treatment not in §4.4].

#### Definition

1. ice cream.

---

### ęy

#### Etymology
*any* — NPI determiner/pronoun "any whatsoever," GA /eni/. Inherited as a strict negative-polarity item, narrowed to the concord reinforcer of the go-ahead negative marker *skwkw*.

**Part of speech:** aux. (VOL.NEG concord reinforcer; doubly restricted NPI).  **IPA:** /ɛ̃j̃/  **Foot:** [Open].

Phonological development: intervocalic /n/ elides, leaving nasalization on the flanking vowels (E1, S1); smooths to a single nasalized /ej/ diphthong [Open: smoothing conditioned by function-word status — a lexical word such as *penny* would remain disyllabic; conditioning rule not yet in §4]. Glide nasalization predictable from the nasalized vowel; left unmarked (headword *ęy*, not *ęỹ*).

Cross-refs: *skwkw* (sole licensor); *rhiiy* (parallel reinforcer, in the *nocquıî* paradigm).

#### Definition

1. *(aux., VOL.NEG concord reinforcer)* emphatic floor-of-the-scale particle, sitting with the action or object quantified over; licensed only by *skwkw* within the LVC. Reinforces categorical refusal: "any instance whatsoever." — *I'm skwkw passing out ęy.* "I'm refusing to fall asleep at all."

#### Notes

Doubly restricted: licensed only in negative contexts (NPI behavior) and, within those, only by verbal *skwkw*. Does not survive the adverbial/substitutional uses of *skwkw* (*on my way to the bar skwkw ęy gym* is unnatural). The concord is paradigm-internal, not a property of *skwkw* wherever it appears.

In nested negation, *ęy* sits locally with the lexical verb (post-*skwkw*), while the outer marker's reinforcer (*rhiiy*, for *nocquıî*) sits clause-finally — the two reinforcers occupy different structural positions and do not compete. — *nocquıî go ahead and skwkw ęy V rhiiy.*

[Open: *ęy* may have other NPI distributions (questions, conditionals, comparatives) not yet described.]

---

### hitsn

#### Etymology
*kitchen*.

**Part of speech:** n.  **IPA:** /ˈhitsn̩/  **Foot:** (ˈL) with syllabic /n̩/ appendix [Open].

Phonological development: /k/→/h/ (k-breathing); /ɪ/→/i/ [Open: tensing]; /tʃ/→/ts/ (ch-funnelling); /ən/→/n̩/ (E3 + syllabic promotion).

#### Definition
1. kitchen.

---

### hohô

#### Etymology
*how so* — a rhetorical question reduced to a fixed interrogative particle. The GA rhetorical "how so?" (requesting explanation or justification) has lexicalized as a general why-question word.

**Part of speech:** interrogative particle.  **IPA:** /hoˈho/  **Foot:** (L)(ˈL).

Phonological development: *how* /haʊ/: onset /h/→/h/; /aʊ/→/o/ (§4.4.2); *so* /soʊ/: onset /s/→/h/ (debuccalization); /oʊ/→/o/; circumflex on final `ô` = pitch + stress coincide (GA stress and conlang final stress both on the second syllable). The internal `h` (written between the two `o` vowels) marks the boundary; if read as a hiatus-delimiter it is silent; if phonologically active it marks breathy voice on the adjacent vowel (see `orthography.md` §1).

#### Definition

1. why; how so; for what reason.

---

### hoiiǫ

#### Etymology
*sodium* — narrowed from the chemical element to the everyday substance.

**Part of speech:** n.  **IPA:** /ˈhoiõ/  **Foot:** [Open].

Phonological development: /s/ → /h/ (debuccalization); intervocalic /d/ elided (E1); /oʊ/ → /o/; final /-iəm/: labial /m/ colors the schwa, deviating from the expected /ɛ/ outcome → /o/ rather than /iɛm/ or /iɛ̃b/; /m/ then elides, leaving nasalization on the vowel → /-iõ/ (written *iiǫ*). [Open: labial-coloring-of-schwa + /m/-elision-with-nasalization proposed as a productive rule for all *-ium* endings — attested or predictable in *podium*, *Colosseum*, *Liam*; to be formalized in `phonology.md` in a dedicated session.]

#### Definition

1. salt (the seasoning; the mineral).

---

### hoʔnʔnts

#### Etymology
*countenance* — narrowed to the concrete body-part term; facial expression, demeanor, and composure senses not inherited.

**Part of speech:** n.  **IPA:** /ˈhoʔn̩ʔn̩ts/  **Foot:** (ˈH) with multiple syllabic-C nuclei.

Phonological development: onset /k/ → /h/; /aʊ/ → /o/; E3 schwa elision in unstressed positions; /n/ → syllabic /n̩/; /st/ → /ts/; coda /ʔ/ preserved.

#### Definition

1. face (the part of the body).

#### Notes

A showcase for syllabic-consonant phonology: three nuclei follow the stressed vowel, two of them /n̩/ and one a complex coda /ts/. Stress remains on the initial /o/ — the syllabic consonants are moraic but not full vocalic positions for stress placement.

---

### hóhonìt

#### Etymology
*coconut* — the fruit; no semantic shift.

**Part of speech:** n.  **IPA:** /ˈhohoˌnɪt/  **Foot:** (ˈH)(L)(L) [Open: foot structure of three-syllable output].

Phonological development: onset /k/→/h/ twice (§4.4.1, both syllables); /oʊ/→/o/ (§4.4.2) for both /koʊ/ syllables; medial /ə/ → /o/ [Open: E3 predicts /ə/→∅, which would give cluster /hn/; the surface /o/ between the second /h/ and /n/ requires /ə/→/o/ rather than elision — same open rule as *nobêt* but without the /n/-conditioning; possibly a more general /ə/→/o/ rule in unstressed open-syllable position before a nasal]; /n/ stays (onset of the secondary-stressed syllable, same stress-onset blocking environment as *benıîä* etc.); /ʌ/→/ɪ/ (§4.4.2); /t/ stays [Open: E2a predicts /t/→/ʔ/].

#### Definition

1. coconut (the fruit, and coconut as a flavor).

---

### hoë hoś

#### Etymology
*soy sauce* — the condiment; no semantic shift.

**Part of speech:** n. (two-word headword).  **IPA:** /hoe ˈhos/  **Foot:** (ˈH)(ˈH) [two phonological words].

Phonological development: *soy* /sɔɪ/: onset /s/→/h/ (debuccalization); /ɔɪ/→/oe/ (diphthong; same pathway as *boë* ← *boy*) → `hoë`; *sauce* /sɔːs/: onset /s/→/h/ (debuccalization); /ɔː/→/o/ (§4.4.2 /au,or/→/o/); coda /s/: GA source was voiceless /s/ → non-onset default is /z/, so devoiced mark required → `ś`; circumflex on `ô`... actually the headword is `hoś` (no circumflex): the formal-register circumflex is absent in the casual form; stress falls on the second phonological word (`hoś`).

#### Definition

1. soy sauce.

---

### kli

#### Etymology
*click* — the impersonal idiom *it clicked*.

**Part of speech:** v. (impersonal)  **IPA:** /ˈkli/  **Foot:** (ˈL) — light monosyllable, licensed (`phonology.md` §8.1).

Phonological development: /kl/ onset shielded; coda /k/ → ∅ (coda k-loss).

#### Definition
1. (impersonal) to click; to suddenly make sense — *it clicked (for me)*.

#### Morphology
Perfect *klikt* (< *clicked*): the etymological /k/ resurfaces before the suffix — a latent-coda alternation parallel to linking *r* (see changelog).

---

### kyii

#### Etymology
*cue* — clause linker.

**Part of speech:** conj.  **IPA:** /ˈkji/  **Foot:** [Open].

Phonological development: *cue* /kjuː/ → /kji/ (`ky` /kj/; /uː/→/i/ `ii`).

#### Definition

1. (conj.) clause linker — introduces/links a following clause. (`language_reference.md` §3.8.)

---

### meiktt

#### Etymology
*make it* — the fused phrase; senses split on subject animacy.

**Part of speech:** v.  **IPA:** /ˈmeikʔ/  **Foot:** (ˈH) with /kʔ/ appendix.

Phonological development: /eɪ/→`ei`; /k/ cluster-internal; *it*: E3, /t/→/ʔ/ `tt` (§2.7).

#### Definition
1. (animate) to arrive; to make it. 2. (inanimate) to become ready; to come together.

#### Morphology
Irregular concord *meirtt* /ˈmeiɾʔ/ — the preserved GA past *made it*, /d/→/ɾ/ by ordinary soft-six tapping: inherited irregularity (`verbal-system.md` §4.2.1), regular from its own etymon.

---

### meirei

#### Etymology
*m'aidez* (French "help me," source of *mayday*) — interjection "come (here)."

**Part of speech:** interj.  **IPA:** /meiˈɾei/  **Foot:** [Open].

Phonological development [Open]: from Fr. *m'aidez* /mɛˈde/; /m/ retained; vowels → `ei` /ei/; /d/→/ɾ/ (tap) `r`.

#### Definition

1. (interj.) come!; come here!

---

### ḿiiy

#### Etymology
*smile*.

**Part of speech:** n.; v.  **IPA:** /ˈm̥iː/  **Foot:** (ˈH).

Phonological development: /sm/→/m̥/ (s-breathing collapsing into nasal devoicing, §2.3); /aɪ/→/iː/ (price splinter, long reflex; offglide → `iiy`); coda /l/ → ∅.

#### Definition
**Noun:** 1. a smile. **Verb:** 1. to smile — stimulus-promotion hosts the involuntary reading (`verbal-system.md` §6).

---

### nobêt

#### Etymology
*(i)n a bit* — from colloquial GA /nəbɪt/ (initial /ɪ/ of "in" already elided in GA liaison).

**Part of speech:** adv.  **IPA:** /noˈbɛʔ/  **Foot:** (L)(ˈL) [Open: depends on whether coda /ʔ/ contributes weight].

Phonological development: /ɪ/ of "in" elided at GA stage (colloquial liaison; not a conlang rule); /ə/ of "a" → /o/ in nasal environment [Open: /ə/ → /o/ rounding after /n/ not in §4.4.2; new rule needed]; /ɪ/ of "bit" → /ɛ/ after /b/ [Open: this lowering not in §4.4.2; new rule needed]; /t/ → /ʔ/ (E2a).

Cross-refs: *béntsıìy* (anaphoric counterpart).

#### Definition

1. *(adv.)* soon; in a short while.

#### Notes

Deictic — anchored to speech time (t₀); prospective, denoting a short interval following the moment of utterance. Carries a commitment implicature in promissory contexts. Use in third-person narrative is restricted to informal deictic-shift contexts, parallel to GA "in a bit". Contrast *béntsıìy*: anaphoric, duration-neutral, narrative-compatible.

---

### noblę

#### Etymology
*the blank* — used in the read-the-room idiom (with *þilnn*). Irregular sound changes.

**Part of speech:** n.  **IPA:** /noˈblɛ̃/  **Foot:** [Open].

Phonological development [Open, irregular]: *the* → /no/ [Open]; *blank* /blæŋk/ → /blɛ̃/ `blę` (/bl/ retained; /æ/ → nasalized /ɛ̃/ from the following /ŋk/; coda /ŋk/ → ∅ leaving nasalization).

#### Definition

1. the unspoken situation; the implicit context — the "blank" one reads. Chiefly in the read-the-room idiom with *þilnn* (sense 3; cross-ref).

---

### nocquıî

#### Etymology
*not quite* — adverbial phrase "approximately; falling short of," colloquial GA /nɑʔ kwaɪʔ/ (from /nɑt kwaɪt/ with coda glottalization). Lexicalized as a single unit before grammaticalizing as the get-oneself negative marker. The approximative-from-below semantics is inherited and underlies both the high-scope frustrative reading and the low-scope attenuative reading. Also productive as a derivational element forming "a small lack" compounds (see Morphology).

**Part of speech:** aux. (LVC.NVOL.NEG); also adv. (temporal proximative, substitutional apologetic); also deriv. prefix.  **IPA:** /noˈkʷːi/  **Foot:** [Open].

Phonological development: /ɑ/ → /o/ (raising-and-rounding, word-initially and after /n/) [Open: new rule, not in §4]; /aɪ/ → /i/; /ʔk/ → geminate /kʷː/ (coda glottal of *not* assimilates to and geminates the following /k/, which labializes from the /w/ of *quite*) [Open: /ʔk/-gemination rule not in §4]; final coda /ʔ/ (from *quite*'s /t/) drops [Open: coda /ʔ/ drop condition at compound junctions]; the final /i/ from /aɪ/ carries stress and pitch (circumflex in headword). Spelling: `cqu` for /kʷː/ — now recorded in `orthography.md` §2.4; standardization (`cqu` vs. `kkw`) remains [Open] there (§6).

Cross-refs: *skwkw* (paradigmatic opposite on the polarity axis, go-ahead side); *rhiiy* (concord reinforcer in the LVC, and the general negator); *ęy* (parallel reinforcer in the *skwkw* paradigm).

#### Definition

1. *(aux., LVC.NVOL.NEG)* the get-oneself negative cell of the frame (light verb complex); marks falling-short, typically with a frustrative reading (a trajectory toward V, often involuntary, that fails to reach V, with the not-reaching foregrounded and often regretful). — *I do nocquıî get myself tuning them out.* "I couldn't manage to tune them out and ended up watching anyway."
2. *(low-scope attenuative)* under a go-ahead frame, modifies the lexical verb: "only partway; only a little." — *I go ahead and nocquıî tune them out.* "I deliberately tune them out only a little bit."
3. *(adv., temporal proximative)* before; not yet at. — *on my way to the gym when it's nocquıî Thursday* "…before Thursday."
4. *(adv., substitutional apologetic)* rather than; instead of — softened, with an unintentional or mildly apologetic flavor (contrast the deliberate substitutional *skwkw* sense 2). — *on my way to the bar nocquıî the gym* "…the bar, rather than the gym."

#### Morphology

**Derivational prefix *nocquii-***, forming compounds that denote "a small lack" — a quantitative or qualitative falling-short of the base noun. Productive. The combining form is *nocquii-*; the junction behaves per the phonology:

- Before an obstruent, the dropped coda /ʔ/ geminates the following consonant. When the geminating consonant is /k/, gemination **bleeds debuccalization** (a geminate /kː/ does not debuccalize to /h/ the way a singleton onset /k/ does), yielding /h/ ~ /kː/ alternations between free and bound forms.
- Before a vowel or rhotic, a linker *-e-* appears.

[Open: combining-form rules inferred from attested compounds; ratify. Open: stress/pitch placement in compounds undetermined.]

#### Notes

Pairs with the reinforcer *rhiiy* (sense 1): an optional emphatic concord particle sitting clause-finally, licensed only by *nocquıî* within the LVC and not surviving the adverbial uses (senses 3–4). — *I'm not quite getting myself to pass out rhiiy.*

The frustrative reading (sense 1) is compositional — falling-short semantics + the get-oneself frame + the action's natural endpoint — not separately encoded.

Has both high scope (sense 1) and low scope (sense 2), in contrast to *skwkw* (high-scope only). The split follows from the degree-of-approximation core, which can target a whole event or the realization-level within an event.

[Open: glossing convention for nested negation. Open: distribution across the four readings (happenstance, effortful self-benefit, threshold, backdrop) — whether even, or favoring some; and whether the effortful self-benefit reading admits *nocquıî* at all. For `verbal-system.md` §9.]

---

### nocquiiayo

#### Etymology
*nocquii-* "a small lack" + *ayo* "joe; coffee" (base not yet an entry; GA slang *joe* → derivation [Open]). Decaffeinated coffee — coffee falling short of full coffee.

**Part of speech:** n.  **IPA:** [Open].  **Foot:** [Open].

Phonological development: *nocquii-* + vowel-initial base. [Open: the *nocquıî* Morphology section specifies a linker *-e-* before vowel- or rhotic-initial bases, predicting *nocquiieayo*; headword *nocquiiayo* has no linker — reconcile combining-form rule.]

Cross-refs: *nocquıî* (deriving prefix); *ayo* "joe; coffee" (base, not yet an entry); *nocquiie-ŕóųzǫ*, *nocquiissprıĩ* (parallel *nocquii-* compounds).

#### Definition

1. *(n.)* decaffeinated coffee; decaf.

---

### nocquiie-ŕóųzǫ

#### Etymology
*nocquii-* "a small lack" + *ŕóųzǫ* "chromosome" (base not yet an entry; GA source and derivation [Open]). Named for the chromosomal difference characteristic of the condition.

**Part of speech:** n.  **IPA:** [Open].  **Foot:** [Open].

Phonological development: *nocquii-* + rhotic-initial base takes the linker *-e-* (see *nocquıî* Morphology). Base derivation [Open].

Cross-refs: *nocquıî* (deriving prefix); *nocquiiayo*, *nocquiissprıĩ* (parallel *nocquii-* compounds).

#### Definition

1. *(n.)* Down syndrome.

---

### nocquiissprıĩ

#### Etymology
*nocquii-* "a small lack" + *sprıĩ* "spring" (base not yet an entry; GA *spring* → derivation [Open]; nasalized vowel from /ŋ/). The period after February that is nominally spring but still feels like winter.

**Part of speech:** n.  **IPA:** [Open].  **Foot:** [Open].

Phonological development: at the *nocquii-* + *spr-* junction, the dropped coda /ʔ/ geminates the following /s/ → /sː/ (spelled *ss*); final nasalization from *spring*'s /ŋ/ transferred to vowel. Base derivation [Open].

Cross-refs: *nocquıî* (deriving prefix); *nocquiiayo*, *nocquiie-ŕóųzǫ* (parallel *nocquii-* compounds).

#### Definition

1. *(n.)* the cold, gray period after February when it is nominally spring but the weather is still wintry; roughly March.

---

### noê

#### Etymology
*in a way* — GA /ɪn ə ˈweɪ/, pragmatic hedge phrase grammaticalized as a clause-final modal adverb.

**Part of speech:** adv.  **IPA:** /noˈɛ/  **Foot:** (L)(ˈL).

Phonological development: /ɪ/→/o/ [Open: /ɪ/→/o/ after initial /n/ — rule not in §4; flagged in pending phonology session]; coda /n/→∅ (E1) + S1 nasalizes — nasalization lost or absorbed [Open]; /ə/→∅ (E4); /w/→/ɻ/ (§4.4.1); intervocalic /ɻ/ + no prior /h/ → M1 plain onset → R-Assim → /ɾ/ → E1 elides; /eɪ/→/ɛ/ [Open: /eɪ/→/ɛ/ shortening path].

#### Definition

1. *(adv.)* in a way; sort of; somewhat. Clause-final position.

Cross-refs: *nóè* "no way" (pitch-accent minimal pair — residual high pitch on "no" vs. on "way"; the contrast is carried by spelling and pitch, not the broad IPA).

---

### nóè

#### Etymology
*no way* — GA /noʊ ˈweɪ/; emphatic refusal/disbelief. Pitch-accent minimal pair with *noê* "in a way": *nóè* keeps a residual high pitch on "no" (GA primary stress) while primary stress sits on "way"; *noê* has both on "way." The contrast is carried by spelling and pitch, not the broad IPA.

**Part of speech:** interj./adv.  **IPA:** /noˈɛ/  **Foot:** (L)(ˈL).

Phonological development: /noʊ/→/no/; /w/→/ɻ/→M1→/ɾ/→E1 elides; /eɪ/→/ɛ/ [Open] (parallel to *noê*).

#### Definition

1. (interj.) no way!; absolutely not. 2. (adv.) by no means.

Cross-refs: *noê* "in a way" (pitch-accent minimal pair).

---

### nóeıìe

#### Etymology
*no idea* — GA /noʊ aɪˈdiə/, colloquial response particle reduced to a single phonological word.

**Part of speech:** interj.  **IPA:** /noɛˈiɛ/  **Foot:** [Open].

Phonological development: /n/→/n/; /oʊ/→/o/; /aɪ/→/ɛ/ [Open: /aɪ/→/ɛ/ short reflex — distinct from established /eː/ and /i/ pathways; conditioning unresolved]; /d/→/ɾ/ (tap merger, §4.4.1) → intervocalic → E1 elides; /ɪ/→/i/ [Open: tense promotion]; /ə/→/ɛ/ [Open: E5 normally gives /a/; /ɛ/ here possibly front-vowel assimilation].

#### Definition

1. *(interj.)* no idea; I don't know; beats me.

---

### noë

#### Etymology
*annoy* — GA /əˈnɔɪ/.

**Part of speech:** v.  **IPA:** /noe/  **Foot:** (ˈH) [Open: diphthong weight].

Phonological development: initial /ə/→∅ (E3); /n/→/n/; /ɔɪ/→/oe/ (choice smoothing, `phonology.md` §4.4.8).

Cross-refs: *boë* (parallel /ɔɪ/→/oe/).

#### Definition

1. to annoy; to irritate; to bother.

---

### noës

#### Etymology
*noise*.

**Part of speech:** n.  **IPA:** /ˈnoez/  **Foot:** (ˈH) [Open: tied to the `oë` mora question].

Phonological development: /ɔɪ/→/oe/ (choice smoothing); final /z/ — non-onset `s` = /z/.

Cross-refs: *noë* "to annoy" — near-homophone pair (/noe/ ~ /noez/).

#### Definition
1. noise; an (unidentified or unwanted) sound.

---

### nokw

#### Etymology
*not quite* — the reduced negator; a clipped form of *nocquii* (< *not quite*). See *nocquıî*.

**Part of speech:** aux./adv.  **IPA:** /noˈkw̩/  **Foot:** [Open].

Phonological development [Open]: reduction of *nocquii* /nokʷːi/ → /nokw̩/ (final vowel → syllabic /w̩/; degemination).

#### Definition

1. (aux./adv.) not quite; not really — reduced negator. Cf. *nocquıî*.

---

### nott

#### Etymology
*note* — convergent pair with *nouś* (< *notice*): two etyma converged in form and territory while remaining distinct lexemes (`terminology-registry.md`).

**Part of speech:** v.  **IPA:** /ˈnoʔ/  **Foot:** (ˈL) [Open].

Phonological development: /oʊ/→/o/ (short reduction — content-verb attestation for §5.2); /t/→/ʔ/ (coda glottaling) `tt` (§2.7).

Cross-refs: *nouś*; distinct from topic *no/nou* and matrix *no*; connective offspring *notto*, *not·ho* (`language_reference.md` §3.8).

#### Definition
1. to note; to attend to deliberately. 2. *(volitive perfect)* to commit to memory; to memorize — *beųheun nouret*. 3. to mind; to keep in mind.

#### Morphology
Concord *nounet* (progressive-shaped); *nouret* (past-derived, < *noted*, the *meirtt* pattern); *nou·et* (stem + definite-object *-et*).

---

### nouś

#### Etymology
*notice* — the other half of the convergent pair (see *nott*).

**Part of speech:** v.  **IPA:** /ˈnoːs/  **Foot:** (ˈH).

Phonological development: /oʊ/→/oː/ (regular long reflex — the pair diverges precisely here: *nott* took the short reduction); medial /t/ → ∅ [Open: flap elision]; /ɪs/→`ś`.

Cross-refs: *nott*; *ouś* (August) is unrelated. Connective offspring *nousso* ×2 (`language_reference.md` §3.8).

#### Definition
1. to notice; to perceive (any modality; visual by default). 2. *(get-oneself)* to happen to perceive; *(imperfect)* first-noticing.

---

### nóuśshè

#### Etymology
*in a nutshell* — grammaticalized as a summary matrix particle (MP.SUMM).

**Part of speech:** aux. (matrix particle, MP.SUMM).  **IPA:** /noːsˈʃɛ/  **Foot:** [Open].  **[IPA Open.]**

Phonological development [Open]: *in a nutshell* heavily reduced; `óu` /oː/ (pitch unmarked in IPA); `ś` /s/; `sh` /ʃ/; `è` /ɛ/ (stress).

#### Definition

1. (matrix particle) in a nutshell; to summarize. Tenseless. Cf. *reś* (`verbal-system.md` §11).

---

### o (interj.)

#### Etymology
*oh* — the quote-opener: introduces a following direct quotation. One of three homophonous *o* lemmas (article *o (art.)*, quotative verb *o (quot.)*, this quote-opener), disambiguated by the parenthetical tag.

**Part of speech:** interj./part.  **IPA:** /ˈo/  **Foot:** (ˈL) [Open].

Phonological development: *oh* /oʊ/ → /o/.

#### Definition

1. (quote-opener) oh — marks the onset of a direct quotation. Cf. *o (quot.)*, quotation particle *quo*, *ohei*.

---

### o (quot.)

#### Etymology
*go* — the quotative "say" use of GA *go* ("and I go, 'no way'"), narrowed to a dedicated speech-report verb. Intransitive; obligatorily takes an ideophone complement.

**Part of speech:** v. (quotative).  **IPA:** /ˈo/  **Foot:** (ˈL) light monosyllable [Open].

Phonological development: onset /ɡ/ → ∅ [Open: word-initial /ɡ/-drop — not in §4.4; cf. soft-six tapping, which targets *intervocalic* /ɡ/]; /oʊ/ → /o/ (monophthongization). Suppletive perfect *rhentt* < *went* /wɛnt/: /w/ → /ɻ/ (§4.4.1); /ɛ/ retained; coda /nt/ → /n/ + glottal /ʔ/, spelled *tt* (`orthography.md` §2.7) → /ˈɻɛnʔ/.

Cross-refs: the three homophonous *o* lemmas are disambiguated by a parenthetical tag — article *o (art.)* [pending entry], this quotative verb *o (quot.)*, and quote-opener *o (interj.)* (< *oh*); quotation particle *quo* (`verbal-system.md` Quotation §).

#### Definition

1. (quotative) to say; to go (introducing reported speech or an ideophone). Perfect *rhentt*.

---

### ohei

#### Etymology
*oh hey* — direct-question marker.

**Part of speech:** part.  **IPA:** /oˈhei/  **Foot:** [Open].

Phonological development: *oh* /o/ + *hey* /hei/ `ei`.

#### Definition

1. (part.) direct-question marker; opens a direct question.

---

### ohô

#### Etymology
*oh I see* — GA /oʊ aɪ siː/, colloquial acknowledgment phrase. Grammaticalized as a realization interjection.

**Part of speech:** interj.  **IPA:** /oˈho/  **Foot:** (L)(ˈL).

Phonological development: /oʊ/→/o/; /aɪ/→∅ [Open: absorbed]; /s/→/h/ (§4.4.1 debuccalization); /iː/→/o/ [Open: /iː/→/o/ pathway not in §4.4.2]. Circumflex on `ô` = pitch+stress coincide.

#### Definition

1. *(interj.)* oh I see; aha; I understand now. — recognition, realization.

---

### óhò

#### Etymology
*oh hey* / *hey* — GA /heɪ/ or /oʊ ˈheɪ/, attention-getting interjection.

**Part of speech:** interj.  **IPA:** /ˈoho/  **Foot:** (ˈL)(L).

Phonological development: [Open: full derivation unclear — /h/ retention in onset; /oʊ/→/o/; /eɪ/→/o/ [Open: /eɪ/→/o/ not in §4.4.2]].

#### Definition

1. *(interj.)* hey!; hi!; (attention-getter, greeting).

---

### ospii

#### Etymology
*speak* — with prothetic /o/. In the combining form with *-wþ* (< *with*), the etymological /k/ is rescued: *ospokwþ* "speak with."

**Part of speech:** v.  **IPA:** /oˈspi/  **Foot:** (ˈL)(L) [Open].

Phonological development: prothetic /o/ before the /sp/ cluster [Open: epenthetic-/o/ prothesis]; /sp/ retained (s cluster-protection, §4.4.1); /i/ retained; coda /k/ → ∅ (coda purge, Stratum 5) — it returns under inflection (the fossil resurrection, §4.4.14). Combining form *ospokwþ*: coda /k/ + /w/ of *with* → /kʷ/ (labial rescue, §4.4.11 morphophonological extension [Settled] — the velar special case of the fossil resurrection); /θ/ `þ` from *with*; nucleus /i/ → /o/ [Open: vowel alternation in the combining form]. (Progressive *ospiihıĩ*: with no /w/-suffix the same /k/ instead breathes to /h/, §4.4.14.)

#### Definition

1. to speak; to talk.
2. (combining form *ospokwþ*) to speak with; to converse with.

---

### osquihii

#### Etymology
*squeaky(-clean)* — the cleanliness sense, clipped of *clean*.

**Part of speech:** adj.  **IPA:** /oskwiˈhiː/  **Foot:** [Open].

Phonological development: prothetic /o/ (squeaky prothesis); /skw/ intact; medial /k/→/h/ (k-breathing — the `-hii` is etymological, not the predicative element); final /i/→/iː/ under stress.

#### Definition
1. clean; spotless. — *aų osquihii hii* "on the spotless side" (the second *hii* is the predicative element, `language_reference.md` §3.3).

---

### ossıî

#### Etymology
*outside* — the outdoors; the exterior.

**Part of speech:** n.  **IPA:** /oˈsːiː/  **Foot:** (L)(ˈH) [Open].

Phonological development: /aʊ/→/o/ (mouth merger); /ts/ → /sː/ at the seam [New rule needed: /ts/-cluster coalescence to /sː/]; /aɪ/→/iː/ (price splinter); coda /d/ → ∅.

#### Definition
1. the outside; the outdoors. 2. the exterior (of a thing).

---

### ouðeu

#### Etymology
*over there* — distal locative deictic "there."

**Part of speech:** adv.  **IPA:** /oːˈðɛː/  **Foot:** [Open].

Phonological development: *over* → `ou` /oː/ (/v/→∅; /ər/ smoothed); *there* → `ðeu` /ðɛː/ (/ð/ retained; /ɛr/→/ɛː/ `eu`).

#### Definition

1. (adv.) there; over there (distal). Cf. *rheiiem* "here."

---

### ouś

#### Etymology
*August* — GA /ˈɔːɡəst/, proper noun.

**Part of speech:** proper n.  **IPA:** /ˈoːs/  **Foot:** (ˈH).

Phonological development: /ɔː/→/oː/ (back long vowel; written `ou`); /ɡ/→/ɾ/ (tap merger, §4.4.1) → intervocalic → E1 elides; /ə/→∅ (E3); coda /st/→/ts/ (§4.4.1) → /t/→/ʔ/ (E2a) → drops [Open: /ʔ/-drop condition here]; /s/ in coda position → non-onset → /z/ → devoiced → `ś`.

#### Definition

1. August (the month).

---

### ǫ

#### Etymology
*own* — survives for neutral mere-having beside the possession construction.

**Part of speech:** v.  **IPA:** /ˈõ/  **Foot:** (ˈL) [Open].

Phonological development: /oʊn/ → coda /n/ collapses into nasalization (§3.6) → /õ/.

#### Definition
1. to own; to have (neutral, non-constructional) — division of labor with `verbal-system.md` §13.1.

#### Morphology
Imperfect *ǫıĩ* /õĩː/ "owning": the GA *-ing* surfaces as nasalized /ĩː/ (`ıĩ` = `ii` + tilde, dotless-`ı` convention) — the first attested *-ing* reflex; see changelog.

---

### pauyiis

#### Etymology
*apologize* — to apologize, to say sorry. Cf. the interjection *pauyiiś* "apologies" (< *apologies*).

**Part of speech:** v.  **IPA:** /pɑˈjiz/  **Foot:** (H)(ˈL) [Open].

Phonological development: heavy reduction of /əˈpɑːlədʒaɪz/. Initial /ə/ → /ɑ/ `au` (or lost) [Open]; /p/ retained; intervocalic /l/ → /j/ (dark-l vocalization adjacent to a vowel, §4.4.4); medial /ədʒ/ syncopated [Open: medial-syllable loss]; /aɪ/ → /i/ (short /aɪ/ reflex, §4.4.2 candidate); final /z/ (non-onset `s` = /z/, `orthography.md` §2.2). Preterite/perfect *pauyiist* [Open: pending §3.22 morphophonology / B12].

#### Definition

1. to apologize; to say sorry.

---

### pauyiiś

#### Etymology
*apologies* — the interjection "(my) apologies." Cf. the verb *pauyiis* "to apologize."

**Part of speech:** interj.  **IPA:** /pɑˈjis/  **Foot:** [Open].

Phonological development: as *pauyiis* (< *apologize*), with final `ś` /s/ for the interjection *apologies*.

#### Definition

1. (interj.) apologies!; my apologies. Cf. *pauyiis* (v.).

---

### piiem

#### Etymology
*P.M.* — the initialism (afternoon/evening).

**Part of speech:** n.  **IPA:** /ˈpiɛm/  **Foot:** [Open].

Phonological development: spelled-out initialism — letter-names *P* /piː/ + *M* /ɛm/ → /ˈpiɛm/, stress on the first letter-name. Cf. *nopiiem* "(in the) evening" (< *on the P.M.*) (propagated 2026-06-22, `verbal-system.md` §12 / `ideophones.md`).

#### Definition

1. P.M.; the afternoon/evening.

---

### piiquóä

#### Etymology
*peek over at* — GA /piːk ˈoʊvər æt/, periphrastic phrase lexicalized as a single verb.

**Part of speech:** v.  **IPA:** /piˈkʷoæ/  **Foot:** (L)(ˈH) [Open].

Phonological development: /p/→/p/ (blocked before /i/, §4.4.1 /p/→/b/ rule); /iː/→/i/ [Open: /iː/ shortening]; coda /k/ of *peek* labializes absorbing onset /w/ of *over* → /kʷ/ [Open: /k/ labialization mechanism]; /oʊ/→/o/; /v/→∅ or /ɾ/ → elides [Open]; /ər/→∅ (E3+E1); /æ/→/æ/ (residual, final).

#### Definition

1. to peek over at; to glance toward; to sneak a look at.

---

### pikkp

#### Etymology
*pick up* — fused phrase; inherits GA *pick up*'s polysemy.

**Part of speech:** v.  **IPA:** /ˈpikːp/  **Foot:** (ˈH) with /p/ appendix [Open].

Phonological development: word-initial /p/ resists voicing; /ɪ/→/i/ [Open: tensing]; *up*: /ʌ/→/ɨ/→∅ in appendix [Open: appendix /ɨ/-deletion — the *skwkw* parallel]; /k…p/ → /kːp/ [Open: fusion-boundary geminate].

#### Definition
1. to pick up; to grab and lift. 2. to pick up (information); to learn in passing. 3. to pick up; to tidy.

#### Morphology
Compound-incorporating forms *pikborrô*, *piknib·orrô* (with *-orrô*; `verbal-system.md` §4.2.2). Concord [Open: surface form].

---

### piquô

#### Etymology
*pick out* — GA /pɪk ˈaʊt/, phrasal verb. *Out* particle grammaticalized with /ʔ/-drop (cf. *rhiiysseunnou*).

**Part of speech:** v.  **IPA:** /pɪˈkʷoː/  **Foot:** (L)(ˈH).

Phonological development: /p/→/p/ (blocked before /ɪ/); /ɪ/→/ɪ/; coda /k/ labializes absorbing *out*'s /aʊ/ → /kʷ/ [Open: same mechanism as *piiquóä*]; /aʊ/→/oː/; coda /t/→/ʔ/ (E2a) → drops (grammaticalized *out* /ʔ/-drop, §4.4.3 E2d). Circumflex on `ô` = pitch+stress coincide.

Cross-refs: *rhiiysseunnou* (parallel grammaticalized *out* /ʔ/-drop).

#### Definition

1. to pick out; to select; to choose.

---

### ponś

#### Etymology
*upon us* — grammaticalized as an existential/presentational particle.

**Part of speech:** part.  **IPA:** /ˈpons/  **Foot:** [Open].

Phonological development: *upon us* /əˌpɑn ˈʌs/ → /pons/ (initial /ə/ lost; /ʌs/ → coda /s/; final /s/ voiceless, written `ś`).

#### Definition

1. (existential/presentational particle) there is/are; presents a new referent. (`language_reference.md` §4.)

---

### pot

#### Etymology
*pout* — GA /paʊt/.

**Part of speech:** v.  **IPA:** /pot/  **Foot:** (ˈH).

Phonological development: /p/→/p/; /aʊ/→/o/ (§4.4.2 /au, or/→/o/); coda /t/ retained [Open: E2a predicts /t/→/ʔ/; retention here unexplained — possibly analogy or high-frequency blocking].

#### Definition

1. to pout.
2. to sulk; to brood petulantly.

---

### quo

#### Etymology
*quote* — the quotation particle. Merges with *reś* → *resquo* (layering a personal/quoted source onto indirect evidence; `verbal-system.md` §12).

**Part of speech:** part.  **IPA:** /ˈkʷo/  **Foot:** [Open].

Phonological development: *quote* /kwoʊt/ → /kʷo/ (`qu` /kʷ/; /oʊ/→/o/; coda /t/→∅).

#### Definition

1. (quotation particle) marks a quotation/quoted source. Merger form *resquo* (*reś* + *quo*). Cf. *o (interj.)*, *o (quot.)*.

---

### récquıìś

#### Etymology
*likewise* — GA /ˈlaɪkˌwaɪz/.

**Part of speech:** adv.  **IPA:** /ˈɾɛkʷːis/  **Foot:** (ˈH)(L).

Phonological development: /l/→/ɻ/ [Open: /ɫ/→/ɻ/ candidate rule — dark-l vocalization; see pending phonology session]; /aɪ/→/ɛ/ [Open: /aɪ/→/ɛ/ short reflex]; coda /k/ + *wise* onset /w/ → geminate /kʷː/ [Open: labialization and gemination mechanism]; /aɪ/ of *wise* → /ɪ/ [Open]; coda /z/→/s/ — **lexical** devoicing idiosyncratic to this item, *not* the general word-final rule (which retains /z/; `orthography.md` §2.2), hence spelled `ś`.

#### Definition

1. likewise; similarly; in the same way.

---

### réıì

#### Etymology
*dairy* — GA /ˈdeɪri/.

**Part of speech:** n.  **IPA:** /ɾɛˈi/  **Foot:** (L)(ˈL).

Phonological development: /d/→/ɾ/ (tap merger, §4.4.1); /eɪ/→/ɛ/ [Open: /eɪ/→/ɛ/ shortening — distinct from established /eɪ/→/eː/]; medial /ɹ/→/ɻ/ → M1 (no /h/ onset) → plain /ɻ/ onset → R-Assim → /ɾ/ → E1 (intervocalic) elides; /i/→/i/ retained.

#### Definition

1. dairy; dairy products collectively.
2. milk.

---

### rekriiâ

#### Etymology
*yakitty-yak* — GA /ˈjækɪtiˌjæk/, expressive reduplication for idle/dialect chatter; the GA exonym *Rickety Yak* is this word. Supersedes the earlier headword *rékriiyä* in form (§2.6 of `phase4-triage-saying-2026-06.md`).

**Part of speech:** ideophone (IDEO); verbalizes with concord — *rekriiâkm* "chatting" (v.).  **IPA:** /ɾɛkɾiˈɑ́/ (verbalized *rekriiâkm* /ɾɛkɾiˈɑ́km/)  **Foot:** [Open] (ultimate-syllable stress — an ideophone-class licence, `ideophones.md`).

Phonological development: first /j/ → /ɻ/ (§4.4.1) → R-Assim → /ɾ/, written `r`; /æ/ → /ɛ/ [Open: /æ/→/ɛ/ without preceding nasal — distinct from the established nasal pathway] `e`; /k/ retained in cluster; /ɪ/ → ∅ (E3); /t/ → /ɾ/ (tap merger), written `r`; /i/ → `ii`; the second-foot /jæk/ reduces to a final /ɑ/ `â` — second /j/ → ∅, /æ/ → /ɑ/, coda /k/ → ∅ (coda purge) — the word carrying ideophone ultimate stress + pitch (circumflex `â`).

#### Multimodality
Conventionally co-produced with a **wrist-rotation gesture** glossable as "and so on" (shared with *bauwouwou*). See `ideophones.md` §6.

#### Definition

1. (ideophone) speaking in dialect; idle/rambling speech; "and so on." Obligatory ideophone after the quotative verb *o* (*… o, rekriiâ*).
2. (verbalized *rekriiâkm*) to chatter; to talk incessantly and idly; to ramble; to go on and on.

---

### rékwıì

#### Etymology
*victory* — GA /ˈvɪktəri/.

**Part of speech:** n.  **IPA:** /ɾɛˈkʷi/  **Foot:** (L)(ˈL) [Open: /kʷ/ onset weight].

Phonological development: /v/→/ɾ/ [Open: /v/ before front vowel /ɪ/ → tap merger rather than /b/; see /v/ conditioning open question]; /ɪ/→/ɛ/ [Open: /ɪ/→/ɛ/ after onset — rule not in §4]; /kt/ cluster → /kʷ/ [Open: /k/+/t/ → labialized /kʷ/ mechanism]; /ə/→∅ (E3); final /i/ retained.

#### Definition

1. victory; win; success.

---

### rérèyt

#### Etymology
*narrate* — GA /nəˈɹeɪt/.

**Part of speech:** v.  **IPA:** /ɾɛˈɾɛjt/  **Foot:** (L)(ˈH).

Phonological development: /n/→/ɾ/ (tap merger, §4.4.1); /ə/→/ɛ/ (initial unstressed /ə/→/ɛ/, §4.4.2); /ɹ/→/ɻ/→R-Assim→/ɾ/ (since /ɾ/ from /n/ present); /eɪ/→/ɛj/ [Open: /eɪ/→/ɛj/ near-preservation, not full /ɛː/ shift]; coda /t/ retained [Open: E2a predicts /t/→/ʔ/].

#### Definition

1. to narrate; to tell (a story); to recount.

---

### renw

#### Etymology
*dinner* — the day's main meal.

**Part of speech:** n.  **IPA:** /ˈɾɛnw̩/  **Foot:** (ˈL) with syllabic /w̩/ appendix [Open].

Phonological development: /d/→/ɾ/ (soft six); /ɪ/→/ɛ/ [Open: lowering, with *bényǫ*]; /ər/→/w̩/.

#### Definition
1. dinner; the main meal.

---

### reś

#### Etymology
*I guess* — grammaticalized as the general indirect-evidential matrix particle (MP.GUESS); **supersedes *piies***. Tense-invariant (GA *I guess* / *I guessed* converge).

**Part of speech:** aux. (matrix particle, MP.GUESS).  **IPA:** /ˈɾɛs/  **Foot:** (ˈL) [Open].

Phonological development: *I guess* /aɪ ɡɛs/ → /ɾɛs/ (/aɪ/ reduced/lost; /ɡ/→/ɾ/ tap onset; /ɛ/ retained; final /s/ `ś`).

#### Definition

1. (matrix particle) indirect-evidential: covers hearsay and inference; "I guess; apparently; supposedly." Tenseless. Personal/quoted source layered via *quo* → *resquo*. Supersedes *piies* (`verbal-system.md` §11).

---

### reut

#### Etymology
*get it* — caused motion "bring, take, fetch." The extended form *reuto* incorporates the *it* object; a further extension *reutto* "get it to" (geminate /tː/ from *it* + *to*) also lives under this lemma, **not** as a separate headword (B12 elicitation, 2026-06-23).

**Part of speech:** v.  **IPA:** /ˈɾɛːt/ (extended *reuto* /ɾɛːˈto/)  **Foot:** (ˈH) / (H)(ˈL) [Open].

Phonological development: /ɡ/ → /ɾ/ (soft-six tapping → onset; written `r`); /ɛ/ → /ɛː/ `eu` [Open: lengthening]; coda /t/ retained (no glottalization here — cf. the unexpected /t/-retention in *pot*, *rérèyt*) [Open]; in *reuto*, the *it* object surfaces as a final /o/ [Open: object incorporation].

#### Definition

1. to bring; to take; to fetch (caused motion). Extended form *reuto* "get it / bring it."

---

### reųś

#### Etymology
*Venus* — GA /ˈviːnəs/, proper noun.

**Part of speech:** proper n.  **IPA:** /ˈɾɛ̃ːs/  **Foot:** (ˈH).

Phonological development: /v/→/ɾ/ [Open: /v/ before front vowel /iː/ → tap merger; see /v/ conditioning]; /iː/→/ɛː/ [Open: /iː/→/ɛː/ pathway not in §4.4.2]; /n/→∅ (E1) + S1 nasalizes adjacent vowel → /ɛ̃ː/ (written `eų`); /ə/→∅ (E4); coda /s/→/z/ (non-onset) → devoiced → `ś`.

#### Definition

1. Venus (the planet).

---

### ręim

#### Etymology
*name* + *game* — a homophonous merger (`verb-recipe-v2.md` §5.3): both onsets are soft-six members (/n/, /g/), so one rule applied twice collapses the pair.

**Part of speech:** n.  **IPA:** /ˈɾẽim/  **Foot:** (ˈH) [Open].

Phonological development: /n/, /g/ → /ɾ/ (soft-six tapping — the merger mechanism); /eɪ/ → /ẽi/ `ęi` by anticipatory nasalization from the **retained** coda /m/ [Open: §3.6 covers nasalization with coda loss; retained-coda case needs a statement].

#### Definition
1. a name — disambiguated in use by *obii* "go by." 2. a game.

---

### rib

#### Etymology
*give* — survives for explicitly volitional transfer beside the possession construction's give-extension.

**Part of speech:** v.  **IPA:** /ˈɾɪb/  **Foot:** (ˈL) [Open].

Phonological development: /g/→/ɾ/ (soft six); /v/→/b/ (labial funnel) — fully regular.

#### Definition
1. to give (deliberately; volition foregrounded) — preferred over the transfer extension with topic-marked definite objects (`verbal-system.md` §13.2).

#### Morphology
Past stem *reib* /ˈɾeib/ < *gave* — the strong verb survives, regular from its own past etymon (the *meirtt* pattern).

---

### rıírǫ

#### Etymology
*right around* — GA /ɹaɪt əˈɹaʊnd/, directional approximative phrase.

**Part of speech:** adv./prep.  **IPA:** /ɾiˈɾõ/  **Foot:** (L)(ˈH) [Open: nasal vowel weight].

Phonological development: /ɹ/→/ɻ/→R-Assim→/ɾ/ (two rhotics present); /aɪ/→/i/ [Open: /aɪ/→/i/ short reflex — third candidate alongside /eː/ and /ɛ/; conditioning unresolved]; coda /t/→/ʔ/ (E2a) → drops in this grammaticalized phrase [Open: /ʔ/-drop condition]; /ə/→∅ (E4); second /ɹ/→/ɻ/→/ɾ/ (R-Assim); /aʊ/→/o/ (§4.4.2); /n/→∅ (E1) + S1 nasalizes → /õ/ (written `ǫ`); /d/→∅ (E2b).

#### Definition

1. *(adv.)* right around; approximately; somewhere around.
2. *(prep.)* around; in the vicinity of.

---

### rhitmmtm

#### Etymology
*nuh-uh* — the GA dismissive interjection. Irregular/expressive path.

**Part of speech:** ideophone (IDEO).  **IPA:** /ɻɪʔˈm̩ːʔm̩/  **Foot:** [Open] (stress on the geminate syllabic *m̩ː*).  **[IPA Provisional.]**

Phonological development: the *t*'s surface as glottal stops /ʔ/, and stress falls on a geminate syllabic /m̩ː/ — both phonotactic-class licences (`ideophones.md` §5; `phonology.md` exemption flag). Expressive, not a regular derivation [Provisional].

#### Definition

1. (ideophone) refusal; negation; disagreement; "nuh-uh." (No conventional gesture.) Canonical class home: `ideophones.md`.

---

### rhitsstw

#### Etymology
*Rochester* — toponym.

**Part of speech:** proper n.  **IPA:** /ˈɹɪtsstw̩/  **Foot:** (ˈH) with appendix /w̩/ tail.

Phonological development: /tʃ/ → /ts/; E3 schwa elision; /ɻ/ → syllabic /w̩/ in final position.


#### Definition

1. Rochester (the city).

---

### riprprp

#### Etymology
*drip drip drip* — onomatopoeic reduplication.

**Part of speech:** ideophone (IDEO), onomatopoeia.  **IPA:** /ˈɾɪpɾpɾp/  **Foot:** [Open].  **[IPA Provisional.]**

Phonological development: *drip* → /ɾɪp/ reduplicated to /pɾpɾp/ — clusters the core lexicon does not permit (phonotactic licence, `ideophones.md` §5) [Provisional].

#### Definition

1. (onomatopoeia) the sound of dripping; "drip-drip-drip." Enters a clause as an onomatopoeia-object via *-ðs* (`ideophones.md` §4). Canonical class home: `ideophones.md`.

---

### riuś

#### Etymology
*juice* — literal, plus the energy idiom.

**Part of speech:** n.  **IPA:** /ˈɾɪːs/  **Foot:** (ˈH) [Open].

Phonological development: /dʒ/→/ɾ/ (soft six); /uː/→/ɪː/ `iu` (the long-GOOSE reflex; Vu digraph) [New rule needed: long /uː/→/ɪː/ beside the short goose-foot-strut /ɨ/ merger — length-conditioned split]; final `ś`.

Cross-refs: *riųś* "news" (nasalized minimal pair).

#### Definition
1. juice. 2. energy; vitality — chiefly *oo riuś* "out of juice" (`verbal-system.md` §6.4).

---

### riųś

#### Etymology
*news* — GA /nuːz/. Nasalized counterpart of *riuś* "juice"; the two form a minimal pair distinguished only by nasalization (`orthography.md` §3.6). The spelling *rıĩs* is a **misspelling**, not a variant.

**Part of speech:** n.  **IPA:** /ˈɾɪ̃ːs/  **Foot:** (ˈH) [Open].

Phonological development: onset /n/ → /ɾ/ (soft-six tapping → onset — the tap being the dialect's phonemicized rhotic), leaving anticipatory nasalization on the vowel; /uː/ → /ɪː/ `iu`, nasalized → /ɪ̃ː/ `ių`; final /z/ → /s/ (devoiced), written `ś`.

Cross-refs: *riuś* "juice" (oral minimal pair).

#### Definition

1. news.

---

### rheiiem

#### Etymology
*where I am* — proximal locative deictic "here."

**Part of speech:** adv.  **IPA:** /ɻeiɪˈɛm/  **Foot:** [Open].

Phonological development [Open]: *where* → `rhei` (/w/→/ɻ/ `rh`; /ɛr/→/ei/); *I am* → `iem` /ɪɛm/.

#### Definition

1. (adv.) here; where I am (proximal). Cf. *ouðeu* "there."

---

### rheĩ

#### Etymology
*rain* — GA /reɪn/.

**Part of speech:** n.  **IPA:** /ˈɻɛĩ/  **Foot:** [Open].

Phonological development: GA rhotic /ɻ/ retained (broad GA "r" = /ɻ/ — no change; written `rh`); /eɪ/ → /ɛĩ/ `eĩ` (nasalized in anticipation of the coda /n/); coda /n/ → ∅ leaving nasalization. Progressive-shaped *rheinn* /ˈɻeinː/ "(it's) raining" **[Open: pending §3.22 / B12]**.

#### Definition

1. rain.

---

### rhemmemmêm

#### Etymology
*boom boom boom* — onomatopoeic; a fully reduplicated three-beat form.

**Part of speech:** ideophone (IDEO).  **IPA:** /ɻɛmːɛmːˈɛm/  **Foot:** [Open] (ultimate-syllable stress — ideophone-class licence).  **[IPA Provisional — pending phonology pass, `ideophones.md` §2.]**

Phonological development: expressive/onomatopoeic, not a regular derivation; three reduplicated /ɛm/ beats with geminate /mː/ at the beat junctions [Provisional]. Phonotactically exempt (`ideophones.md` §5). Supersedes the earlier spellings *rhémmen·bèm* ~ *rhémm·bèm* (and the brief intermediate *rhémmemmèm*); the beats are marked by gemination, not an interpunct — the interpunct has no beat-defining function, only syllable-division disambiguation (`orthography.md` §3.5). Hub synced 2026-06-22 (`ideophones.md` v1.1).

#### Multimodality
χ back-of-hand rhythmic clap — beats out the bullet-pointed delivery.

#### Definition

1. (ideophone) a bullet-pointed, confident, confrontational manner of argument; "boom, boom, boom." Canonical class home: `ideophones.md`.

---

### rhemmêś

#### Etymology
*reminisce* — nostalgic dwelling, distinct from *bemmw*'s recall event.

**Part of speech:** v.  **IPA:** /ɻɛˈmːɛs/ [Open: geminate straddle]  **Foot:** [Open].

Phonological development: GA rhotic /ɻ/ retained `rh`; medial /m/ geminated (ambisyllabic phonologization); /nɪs/→/ɛs/ [Open: medial /n/ loss]; final `ś`.

Cross-refs: *bemmw*.

#### Definition
1. to reminisce; to dwell in (a memory) with pleasure.

---

### rhéulyèś

#### Etymology
*wild guess* — GA /waɪld ɡɛs/, idiomatic: a total shot in the dark.

**Part of speech:** interj.  **IPA:** /ɻɛːlˈjɛs/  **Foot:** [Open].

Phonological development: /w/→/ɻ/ (§4.4.1); /aɪ/→/ɛː/ (§4.4.2 /ai/→/eː/; written `eu`); /l/ in coda of *wild* retained in cluster /ld/ [Open: E2c targets singleton /l/ only; cluster /l/ exempt — cf. *rhilþ*]; /d/→∅ (E2b); /ɡ/→/ɾ/ (tap merger) → intervocalic → E1 elides; /ɛ/→/ɛ/ (stressed); /s/ falls to coda after /ɡ/-elision → non-onset /s/→/z/→devoiced → `ś`.

#### Definition

1. *(interj.)* wild guess; shot in the dark; I'm just guessing.
2. *(interj., stronger)* absolutely no idea; I'm making this up entirely.

---

### rhibôet

#### Etymology
*report* — the written or delivered account.

**Part of speech:** n.  **IPA:** /ɻiˈboet/  **Foot:** (L)(ˈH) [Open].

Phonological development: GA rhotic /ɻ/ retained `rh`; /p/→/b/ (pass-out voicing, word-medial — the v4.1 restatement's anchor); /ɔr/→/oe/ (report gliding — the rule's namesake) `oë`; coda /t/ retained [Open: coda-/t/ conditioning — see changelog].

#### Definition
1. a report; a written account.

---

### rhiib

#### Etymology
*drive* — to drive (a vehicle).

**Part of speech:** v.  **IPA:** /ˈɻib/  **Foot:** (ˈH) heavy monosyllable [Open].

Phonological development: /dr/ → /ɻ/ `rh` [Open: /dr/→/ɻ/ cluster reduction]; /aɪ/ → /i/ `ii` (short /aɪ/ reflex, §4.4.2 candidate); word-final /v/ → /b/ [Open: /v/→/b/ at coda — the /v/-conditioning candidate, pending phonology session]. Progressive-shaped *rhiimm* (the /v/ returning as /mː/) [Open: pending §3.22 morphophonology / B12].

#### Definition

1. to drive (a vehicle).

---

### rhiiy

A polyfunctional morpheme from GA *really*, spanning intensifier prefix → bleached lexical prefix → get-oneself negative reinforcer → general negator. The bound-prefix uses appear inside *rhiiynii*, *rhiiysseunnou*, and *rhiiyeplii* (under *eplii* sense 2); the free-word uses (reinforcer, general negator) are described here. Consolidated as a single lemma (same form /ɻiː/, same primary source).

**Part of speech:** aux. (general negation); also aux. (NVOL.NEG concord reinforcer); also deriv./intensifier prefix `rhiiy-`.  **IPA:** /ɻiː/  **Foot:** [Open].

Phonological development: GA /ˈɹɪl.i/ → /ɻiː/: dark velarized /ɫ/, sandwiched between front vowels, becomes /j/ (§4.4.1) and then elides, leaving a lengthened /iː/; onset /ɹ/ → /ɻ/ (§4.4.1). (Same derivation as the `rhiiy-` prefix attested in *rhiiynii*, *rhiiysseunnou*, *rhiiyeplii* — this entry consolidates that morpheme.)

Cross-refs: *nocquıî* (host for the reinforcer reading, sense 2); *skwkw* (go-ahead-domain negator — complementary distribution by domain); *ęy* (parallel reinforcer, in the *skwkw* paradigm); *rhiiynii*, *rhiiysseunnou*, *eplii* (contain the bound-prefix uses, senses 3–4).

#### Definition

1. *(aux., general negation)* "no"; "not so." Volition-neutral propositional negation, used outside the LVC: phrasal denial, short answers, negation of non-verbal predicates. — *Rhiiy.* "No." / "Not so."
   - Etymology: *not really* (colloquial GA general negator), grammaticalized via a Jespersen-cycle pathway — the *not* erodes, leaving bare *really* to carry negative force on its own.
2. *(aux., NVOL.NEG concord reinforcer)* clause-final emphatic concord with *nocquıî* in the LVC; emphasizes the predicate's full realization, the standard the action falls short of. — *I'm not quite getting myself to pass out rhiiy.*
   - Etymology: GA intensifier *really* "to a real degree."
3. *(intensifier prefix `rhiiy-`)* still-transparent intensifier on a verb stem. — attested in *rhiiyeplii* "to apply oneself with real effort" (under *eplii* sense 2).
   - Etymology: GA intensifier *really*.
4. *(bleached lexical prefix `rhiiy-`)* fully bleached, no longer felt as an intensifier; part of a lexicalized stem. — attested in *rhiiynii* "to need/want" and *rhiiysseunnou* "to be different/excellent."
   - Etymology: GA *really*, bleached.

#### Notes

Senses 1 and 2 are **the same morpheme, contextually disambiguated**, not homophones: inside the LVC with *nocquıî* upstream → reinforcer reading (sense 2); outside the LVC, or without *nocquıî* → negator reading (sense 1). The two play off a shared "realness" core — the reinforcer asserts the predicate's realness as the standard fallen short of; the negator denies the predicate's realness outright.

Senses 3–4 are the bound-prefix uses, which show grammaticalization stratification across the lexicon: transparent in *rhiiyeplii* (sense 3), fully bleached in *rhiiynii* and *rhiiysseunnou* (sense 4).

Does not enter the LVC as a polarity marker (only as the sense-2 reinforcer); verbal negation is handled by the dedicated volition-aware markers *skwkw* and *nocquıî*. Fills the standalone declarative-negation gap: *skwkw* standalone is prohibitive, *nocquıî* has no standalone use, so *rhiiy* is the language's assertional "no."

[Open: whether negator-*rhiiy* itself attracts a new reinforcer over time (a Jespersen spiral). Deferred — long-horizon.]

---

### rhilqui

#### Etymology
*real quick* — softener/mitigator.

**Part of speech:** part. (softener).  **IPA:** /ɻɪlˈkʷɪ/  **Foot:** [Open].

Phonological development: *real* → `rhil` (/ɻ/ `rh`; /iəl/→/ɪl/); *quick* → `qui` /kʷɪ/ (`qu` /kʷ/; coda /k/→∅).

#### Definition

1. (softener) real quick; just briefly — mitigates an imposition.

---

### rhilþ

#### Etymology
*wolf* — inherited directly; no semantic shift.

**Part of speech:** n.  **IPA:** /ˈɻɪlθ/  **Foot:** [Open: depends on whether coda consonants contribute weight].

Phonological development: /w/ → /ɻ/ (§4.4.1 /w, j/ → /ɻ/); /ʊ/ → /ɪ/ (§4.4.2 back-vowel fronting); /f/ → /θ/ (§4.4.1); coda /l/ preserved in cluster /lθ/ (E2c targets singleton /l/; cluster environment exempt).

#### Definition

1. wolf (the animal).

---

### rhiitsô

#### Etymology
*reach out* — initiating contact, medium-neutral.

**Part of speech:** v.  **IPA:** /ɻiːˈtso/  **Foot:** (H)(ˈL) [Open].

Phonological development: /riː/→`rhii`; /tʃ/→/ts/ (ch-funnelling — evaluated against the derived stress) [Open: fork ordering vs. stress shift — see changelog]; /aʊ/→/o/; final /t/ → ∅ (out-drop).

Cross-refs: *rhıĩ* (channel pair; division of labor [Open]).

#### Definition
1. to reach out; to initiate contact.

#### Morphology
Concord *rhiitsto* (the circumflex belongs to the citation form's final vowel; the concord form's stress shifts [Open]).

---

### rhiiynii

#### Etymology
*really need* — *really* bleached and lexicalized as the `rhiiy-` prefix; stem from *need*. The need/want polysemy collapses two GA concepts onto a single axis.

**Part of speech:** v.  **IPA:** /ɻiːni/  **Foot:** [Open].

Phonological development: /ɫ/ → /j/ between high front vowels; /ɪji/ → /iː/; coda /d/ → ∅ (E2, no compensatory lengthening).

Cross-refs: *rhiiy* (morpheme entry for the `rhiiy-` prefix); *rhiiysseunnou* (parallel `rhiiy-` prefix, fully bleached); *eplii* (intensifier variant *rhiiyeplii*, where `rhiiy-` is still transparent).

#### Definition

1. to need.
2. to want.

#### Notes

The prefix /ɻiː-/ (`rhiiy`) surfaces as long /iː/ from /ɪji/-smoothing; the stem /ni/ (`nii`) is short /i/ from coda /d/-deletion with no compensatory lengthening. The /iː/ vs. /i/ contrast within the same word is the orthographic working rule: `iiy` = long /iː/ (etymologically-justified glide source), `ii` = short tense /i/ [Open: to be confirmed when `orthography.md` §3.2 is revised to admit /iː/].

---

### rhiiyshêush

#### Etymology
*really cherish* — really-glide intensive of *ŕeush*.

**Part of speech:** v.  **IPA:** /ɻiːˈʃɛːʃ/ [Open]  **Foot:** [Open].

Phonological development: *really* → /ɻiː/ (really glide); intensive-internal onset surfaces as /ʃ/, not the tap [Open: neither fork branch fits the unstressed internal position]; spelling `sh` (/ʃ/ = `sh`, orthography §2.1, v3.3).

#### Definition
1. to cherish intensely; to treasure.

---

### rhiiysseunnou

#### Etymology
*really stand out* — *really* bleached and lexicalized as the `rhiiy-` prefix; *stand out* also lexicalized as a phrasal verb in GA. Treated as a single verb in the conlang.

**Part of speech:** v.  **IPA:** /ɻiːsːɛːnːoː/  **Foot:** [Open].

Phonological development: /æ/-tense (pre-nasal in GA, with preserved duration) → /ɛː/ via length reanalysis; /ɫ/ → /j/ between high front vowels; /ɪji/ → /iː/; /st/ → /sː/ at stressed-syllable boundary; /nd/ → /nː/ in coda (regressive assimilation; committed, `phonology.md` §4.4.1); /aʊ/ → /oː/; /t/ → /ʔ/ in coda; coda /ʔ/ dropped (lexically conditioned in grammaticalized *out*).

Cross-refs: *beussou* (parallel /st/ → /sː/, parallel coda /ʔ/-drop in *out*-particle); *rhiiy* (morpheme entry for the `rhiiy-` prefix); *rhiiynii*, *eplii* (parallel `rhiiy-` prefix).

#### Definition

1. to be different; to stand apart; to be distinctive.
2. to be excellent; to excel.

#### Notes

The `rhiiy-` prefix is fully bleached here and in *rhiiynii* — not felt as an intensifier, only as part of the lexicalized stem. Contrast *rhiiyeplii* (under *eplii* sense 2), where the same prefix is still transparent. This stratification (bleached vs. transparent) across the lexicon reflects grammaticalization at different stages.

The `eu` digraph unifies two diachronic sources: (1) the smoothed-schwa pathway for /ɛː/ in `orthography.md` §3.2, and (2) the /æ/-with-preserved-duration pathway attested here. Both surface as `eu`.

---

### rhikriutt

#### Etymology
*recruit* — "to be hiring; to recruit." Predominantly used in the progressive ("they're recruiting").

**Part of speech:** v.  **IPA:** /ɻɪˈkɾɪːʔ/  **Foot:** (L)(ˈH) [Open].

Phonological development: GA rhotic /ɻ/ retained `rh`; /ɪ/ retained; /kr/ retained as /kɾ/; /uː/ → /ɪː/ `iu`; coda /t/ → /ʔ/ (coda glottaling, §4.4.11), written `tt` — anchored, not elided (B12 elicitation, 2026-06-23). Under inflection the etymological /t/ re-exposes (the fossil resurrection, §4.4.14): progressive *rhikriuıĩ* (the /t/ taps and elides before /‑ıĩ/), preterite *rhikriuri* (the /t/ surfaces as the intervocalic tap of /‑ɾi/).

#### Definition

1. to recruit; to be hiring.

---

### rhiksse

#### Etymology
*you could say* — discourse adverbial/hedge.

**Part of speech:** adv.  **IPA:** /ɻɪkˈsːɛ/  **Foot:** [Open].

Phonological development [Open]: heavy reduction of *you could say*; `ss` /sː/ geminate; final /ɛ/.

#### Definition

1. (adv.) you could say; so to speak; in a manner of speaking.

---

### rhink

#### Etymology
*drink* — the noun; the verb territory belongs to the possession construction (*rimmaseu rhink*).

**Part of speech:** n.  **IPA:** /ˈɻɪnk/  **Foot:** (ˈH) [Open].

Phonological development: /dɻ/→/ɻ/ [Open: /d/-loss in the cluster — rhotic-instability datum]; /ŋk/ → /nk/ (no /ŋ/ phoneme; [ŋ] allophonic before /k/).

#### Definition
1. a drink; a beverage — the self-benefit showcase in `verbal-system.md` §13.1.

---

### rhinnw

#### Etymology
*wonder* — a **frame-split** verb: in the get-oneself frame it reads "ask, inquire"; in the go-ahead frame, "doubt, question" (`verbal-system.md` §4.2 frames).

**Part of speech:** v.  **IPA:** /ˈɻɪnːw̩/  **Foot:** (ˈL)(L) [Open] (stress on the initial syllable).

Phonological development: /w/ → /ɻ/ `rh` (§4.4.1); /ʌ/ → /ɪ/ [Open: /ʌ/→/ɪ/ — not in §4.4]; /nd/ → geminate /nː/ [Open: /nd/→/nː/]; GA *-er* /ər/ → syllabic /w̩/ (the GA *-er* → syllabic-*w* appendix, written `w`).

#### Definition

1. (get-oneself frame) to ask, to inquire; to wonder (aloud).
2. (go-ahead frame) to doubt; to question; to have one's doubts.

---

### rhishisben

#### Etymology
*which is when / which has been* — a clause linker from the convergence of two GA relative phrases.

**Part of speech:** conj.  **IPA:** /ɻɪʃɪzˈbɛn/  **Foot:** [Open].  **[IPA Prov.]**

Phonological development [Open]: convergence/merger of *which is when* and *which has been*; `sh` /ʃ/; non-onset `s` /z/; `b` /b/; `en` /ɛn/.

#### Definition

1. (conj.) clause linker — "which is when; whereupon; which has been." (`language_reference.md` §3.8.)

---

### rhiþoupii

#### Etymology
*without a peep* — adverb "without a peep; silently."

**Part of speech:** adv.  **IPA:** /ɻɪθoːˈpi/  **Foot:** [Open].

Phonological development [Open]: *without* → `rhiþou` (/w/→/ɻ/ `rh`; /ð/→/θ/ `þ`; /aʊt/→`ou` /oː/); *a peep* → `pii` /pi/.

#### Definition

1. (adv.) without a peep; silently; without a word.

---

### rhiušp

#### Etymology
*worship* — GA /ˈwɜːrʃɪp/.

**Part of speech:** v.  **IPA:** /ɻɨːʃp/  **Foot:** (ˈH) [Open].

Phonological development: /w/→/ɻ/ (§4.4.1); /ɜːr/ (rhotacized mid vowel) → /ɨː/ [Open: /ɜːr/→/ɨː/ unrounding pathway not in §4.4.2]; R-Assim not triggered [Open: rhotacized vowel vocalized rather than producing a separate /ɾ/]; /ʃ/→/ʃ/ retained [Open: confirm /ʃ/ exempt from debuccalization]; /ɪ/→∅ (E3); coda /p/ retained [Open: /p/ not in E2 elision set].

#### Definition

1. to worship; to revere; to idolize.

---

### rhiwıĩ

#### Etymology
*rewind* — GA /ˌriːˈwaɪnd/. Two POS consolidated: interjection and adverb/temporal.

**Part of speech:** interj.; also adv./temporal.  **IPA:** /ɻɪˈwĩ/  **Foot:** (L)(ˈH) [Open: nasal vowel weight].

Phonological development: /ɹ/→/ɻ/ (§4.4.1); /iː/→/ɪ/ [Open: /iː/→/ɪ/ shortening/laxing]; /w/→/w/ retained as plain onset; /aɪ/→/i/ [Open: /aɪ/→/i/ short reflex]; /n/→∅ (E1) + S1 nasalizes → /ĩ/ (written `ıĩ` per ii-diacritic rule — tilde on second element makes first dotless `ı`); /d/→∅ (E2b).

#### Definition

1. *(interj.)* rewind; go back; let's start that over; wait, let me back up.
2. *(adv./temporal)* going back to; rewinding to; returning to (an earlier point in narrative or time).

---

### rhıĩ

#### Etymology
*ring* — the call sense (telephone idiom) and the finger ring.

**Part of speech:** v.; n.  **IPA:** /ˈɻĩː/  **Foot:** (ˈH) [Open].

Phonological development: GA rhotic /ɻ/ retained `rh`; word-final /ɪŋ/ → /ĩː/ — coda /ŋ/ nasalizes the vowel and elides (`ıĩ` = `ii` + tilde, dotless-`ı` convention; the word-final half of the /ŋ/ resolution — see changelog).

Cross-refs: *rhiitsô*.

#### Definition
**Verb:** 1. to call; to ring (someone) up. **Noun:** 1. a ring (jewelry; for the finger).

---

### ŕe

#### Etymology
*today* — from colloquial GA [tʰɾeɪ] (reduced from [tʰəˈdeɪ] via schwa elision and tap-realization). Sense 2 grammaticalizes the GA emphatic use ("done today" = "right now") as a distinct interjectional sense.

**Part of speech:** (1) adv., (2) interj.  **IPA:** /ˈɾ̥ɛ/  **Foot:** (ˈL) light monosyllable.

Phonological development: /h/ + tap coalescence → /ɾ̥/ (M1 devoicing mechanism generalized to onset, without metathesis); two irregular shifts specific to this high-frequency colloquial form: /t/ → /h/ in onset cluster (not a regular rule); /eɪ/ → short /ɛ/ (clipping, not a regular rule).

Cross-refs: *ŕeut* (parallel /ɾ̥/ onset, from M1 metathesis rather than coalescence).

#### Definition

1. *(adv.)* today. — *Ŕeus bémmo oų rĩbii·hii. Oų riis·hii o noê.* "It's a little more chillier today, in a pleasant kind of way."
2. *(interj.)* hurry!; right now!; immediately!

#### Notes

The two irregular shifts — /t/ → /h/ and /eɪ/ → short /ɛ/ — are one-offs licensed by this form's high frequency and rapid-speech origin, not regular rules. The convergence of irregularities in one form is the design point: high-frequency colloquial words bleed off the regular cascade, and *ŕe* is the canonical example.

---

### ŕequôþw

#### Etymology
*check off* — completing, finishing.

**Part of speech:** v.  **IPA:** /ɾ̥ɛˈkwoθw̩/ [Open]  **Foot:** [Open].

Phonological development: /tʃ/→/ɾ̥/ (cherish tapping, at the GA stress stage) [Open: fork ordering — see changelog]; /k/ → `qu` before the rounded vowel [Open: `qu` distribution]; *off* → /oθw̩/ — fin-thin + labial rescue (the satellite *oþw*'s derivation, free-standing).

#### Definition
1. to finish; to complete; to check off.

---

### ŕeush

#### Etymology
*cherish*.

**Part of speech:** v.  **IPA:** /ˈɾ̥ɛːʃ/  **Foot:** (ˈH) [Open].

Phonological development: /tʃ/→/ɾ̥/ (cherish tapping — the namesake); medial /r/ → ∅ (tap–rhotic dissimilation); /ɛ…ɪ/ → /ɛː/ `eu`; final /ʃ/ `sh` (orthography §2.1, v3.3).

#### Definition
1. to cherish; to hold dear. 2. activity-coercion host for emotion predicates — *rimmase ŕeushiię·au* "got myself cherishing it all" (`verbal-system.md` §6).

#### Morphology
Intensive *rhiiyshêush*.

---

### ŕeut

#### Etymology
*carrot*.

**Part of speech:** n.  **IPA:** /ˈɾ̥eːʔ/  **Foot:** (ˈH) heavy monosyllable.

Phonological development: onset /k/ → /h/; coda /t/ → /ʔ/; M1 (rhotic metathesis: intervocalic /ɻ/ → onset, /h/ reanalyzed as devoicing feature → /ɾ̥/); smoothing of /æ + ə/ → /eː/.

Cross-refs: *ŕe* (parallel /ɾ̥/ onset, from /h/ + tap coalescence rather than M1 metathesis).

#### Definition

1. carrot (the root vegetable).

#### Notes

The canonical illustration of M1: GA onset /k/ debuccalizes to /h/, which becomes the devoicing feature on the metathesizing rhotic. Used as a worked example in `phonology.md` §4.5.

---

### skwkw

#### Etymology
*skip* — GA /skɪp/, "decline; pass over." Lexicalized as the go-ahead negative marker. The deliberate-declination semantics is inherited and sharpened to active counter-volition (going out of one's way to not-do, not merely the absence of volition).

**Part of speech:** aux. (LVC.VOL.NEG); also adv./substitutional; also interj. (prohibitive).  **IPA:** /skʷkʷ/ (first /kʷ/ syllabic).  **Foot:** [omitted].

Phonological development: irregular, peculiar to this high-frequency form. Coda /p/ delabializes — but only after labializing the /k/ (the labial feature transfers from /p/ to /k/ before /p/ is lost). The vowel /ɪ/, squeezed between two /kʷ/ sequences, elides entirely, leaving a vowelless /skʷkʷ/ with the first /kʷ/ as syllable nucleus. [Open: irregular; not a proposed regular rule.]

Cross-refs: *nocquıî* (paradigmatic opposite on the polarity axis, get-oneself side); *rhiiy* (general negator, complementary domain — outside the LVC); *ęy* (concord reinforcer, licensed only by this marker).

#### Definition

1. *(aux., LVC.VOL.NEG)* the go-ahead negative cell of the frame (light verb complex); marks deliberate refusal or active counter-volition. High-scope only. — *I'm skwkw passing out ęy.* "I'm deliberately refusing to fall asleep (not even a little)."
2. *(adv./substitutional)* in place of, instead of, declining the alternative; deliberate, with a mutual-exclusivity flavor. — *on my way to the bar skwkw the gym* "…the bar, deliberately not the gym."
3. *(interj., prohibitive)* "Don't!"; "Pass on it!" — standalone negative imperative. — *Skwkw!* "Don't!"

#### Notes

A showcase for vowelless syllabification: /skʷkʷ/ has no vocalic nucleus, the first /kʷ/ serving as the syllable's nucleus. Novel for the lexicon — other consonant-heavy forms (*hoʔnʔnts*, *ritsstw*, *toutw*) retain at least one full vowel. [Open: foot structure and the metrical status of a syllabic obstruent.]

Pairs with the reinforcer *ęy* (sense 1 only): optional emphatic floor-of-the-scale particle, licensed only by *skwkw* within the LVC, not surviving the adverbial/substitutional uses (sense 2). See *ęy*.

Does not stack with GO-AHEAD: *going ahead and skwkw V* collapses to the *skwkw* reading since both fill the single volition slot.

Layers with the positive get-oneself frame (GET-ONESELF) productively but narrowly: *getting myself to skwkw V* = "finding myself in the position of having to deliberately refuse V." Felicitous only in forced-choice contexts.

[Open: glossing convention for nested negation — when *skwkw* appears under *nocquıî* or vice versa.]

---

### split

#### Etymology
*split* — colloquial "to leave"; transitive "to share."

**Part of speech:** v.  **IPA:** /ˈsplɪt/  **Foot:** (ˈL) [Open].

Phonological development: /spl/ shielded; coda /t/ retained [Open: coda-/t/ conditioning — see changelog].

#### Definition
1. (intransitive) to leave; to depart (volitional in the bare stem). 2. (transitive) to split; to share (something, with someone).

#### Morphology
*spli·oþw* (passive-shaped + satellite: "drifted off"), *splitnoþw* (progressive-shaped + satellite), *splitoþw* (infinitive-shaped + satellite), *splitn* (concord). Bare *split* resists the happenstance reading; the satellite *oþw* or matrix *enniip* supplies it (`verbal-system.md` §11–§12).

---

### spyi

#### Etymology
*spew* — GA /spjuː/. Highly specific semantic narrowing to the surprise-spit context.

**Part of speech:** v.  **IPA:** /spjɪ/  **Foot:** (ˈH) [Open: cluster onset weight].

Phonological development: /s/ in cluster /sp/ retained (not debuccalized) [Open: §4.4.1 debuccalization of /s/ blocked in /sp/ cluster? Rule not in §4]; /p/→/p/; /j/ retained in cluster; /uː/→/ɨː/→/ɪ/ [Open: /uː/→/ɪ/ via /ɨ/ unrounding then shortening].

#### Definition

1. to spew liquid; specifically: to involuntarily spit out a drink due to surprise or laughter. Most naturally collocates with coffee.

---

### thių

#### Etymology
*tune* — melody; a song. Source taken as yod-ful /tjuːn/ [assumption noted].

**Part of speech:** n.  **IPA:** /tʰɪ̃ː/  **Foot:** (ˈH) [Open].

Phonological development: onset /tʰ/ written `th` (orthography §2.1 note, v3.2 — graphic contrast with `t`, `tt`); /(j)uː/→/ɪː/ `iu`; coda /n/ → nasalization `ų`.

#### Definition
1. a tune; a melody; a song.

---

### toś

#### Etymology
*toast* — GA /toʊst/.

**Part of speech:** n.  **IPA:** /ˈtos/  **Foot:** (ˈH).

Phonological development: /t/→/t/; /oʊ/→/o/ [Open: /oʊ/→/o/ short reduction rather than /oː/ — possibly high-frequency]; coda /st/→/ts/ (§4.4.1) → /t/→/ʔ/ (E2a) → drops [Open: /ʔ/-drop condition]; /s/ in coda (non-onset) → /z/→devoiced → `ś`.

#### Definition

1. toast (food; sliced bread browned by heat).

---

### toutw

#### Etymology
*to total to* — the GA tallying phrase ("the bill totals to forty dollars") lexicalized as a single verb.

**Part of speech:** v.  **IPA:** /ˈtoːtw̩/  **Foot:** (ˈH) with appendix /w̩/ tail.

Phonological development: /oʊ/ → /oː/; intervocalic tap /ɾ/ elided (E1); coda /ɫ/ → ∅ (E2c; rule stated in `phonology.md` §4.4.3, full path conditions [Open] there); smoothing of /oː + ə/ → /oː/; final unstressed /u/ → syllabic /w̩/ (phonology §4.3 step 7).

Cross-refs: *ritsstw* (parallel appendix /w̩/).

#### Definition

1. to cost a certain amount (of money).
2. to be present in a certain number; to amount to; to add up to.

#### Notes

Initial /t/ is aspirated [tʰ] in stressed onset — allophonic, not marked orthographically. [Open: aspiration's phonemic status not committed in `phonology.md`.]

---

### twıítò

#### Etymology
**Non-GA source** — from *Tweeto*, a deity invented by the author's niece; adopted for "bird" on the onomatopoetic connection. Second deliberate non-GA lexeme (with *rhémstwè*).

**Part of speech:** n.  **IPA:** /ˈtwiːto/ [Open: pitch realization, í…ò as spelled]  **Foot:** [Open].

Phonological development: not derived (nonce source); /tw/ onset and the dotless-`ı` spelling (`ii` + acute on the second element) are inventory-regular.

#### Definition
1. a bird (generic).

---

### þiiaii

#### Etymology
*finally* — interjection "finally!; at last."

**Part of speech:** interj.  **IPA:** /θi.aˈi/  **Foot:** [Open].  **[IPA Prov.]**

Phonological development [Open]: heavy reduction of *finally* /ˈfaɪnəli/; /f/→/θ/ `þ`; vowel sequence `iiaii`.

#### Definition

1. (interj.) finally!; at last!

---

### þilnn

#### Etymology
*fill in* — "tell, inform" (fill someone in). Also "replace / substitute" (fill in for) and an intransitive "read the room" sense (with *niblę*).

**Part of speech:** v.  **IPA:** /θɪlˈnː/  **Foot:** [Open] (stress on the syllabic geminate *nn*).

Phonological development: /f/ → /θ/ `þ` [Open: /f/→/θ/ not in §4.4]; /ɪl/ retained (coda dark *l* in cluster context — cf. the cluster exemption, §4.4.4); *in* /ɪn/ → stressed syllabic geminate /nː/ [Open: syllabic-nasal gemination + stress assignment].

#### Morphology
Direct object infixed; indirect object suffixed. [Open: infix/suffix templates — needs author spec.]

#### Definition

1. to tell, to inform (someone of something).
2. to replace, to substitute (for someone).
3. (intrans., with *niblę*) to read the room; to grasp an unspoken situation.

---

### þliu

#### Etymology
*flu*.

**Part of speech:** n.  **IPA:** /ˈθlɪː/  **Foot:** (ˈH).

Phonological development: /f/→/θ/ (fin-thin; companion *rhilþ*); /l/ in cluster (where /l/ lives); /uː/→/ɪː/ `iu` (long-GOOSE reflex — the regular path the *do* → *o* irregularity excepts; `phonology.md` §5.2).

#### Definition
1. the flu; a flu-like illness — affliction reading in *rimmaseu þliu* (`verbal-system.md` §13.1).

---

### þokss

#### Etymology
*focus* — concentrated attention; supplies the think-cluster's most agentive member.

**Part of speech:** v.  **IPA:** /ˈθoksː/ [Open: final cluster]  **Foot:** (ˈH) [Open].

Phonological development: /f/→/θ/ (fin-thin); /oʊ/→/o/ (short reduction — with *nott*, content-verb data for §5.2); /kəs/: E3 → /ksː/ [Open: final `ss` value].

Cross-refs: *þott* (its suppletive deverbal).

#### Definition
1. to focus; to concentrate on.

---

### þott

#### Etymology
*thought* — with the vowel **analogically leveled** toward *þokss*: the think-verb gap left *thought*'s reflex without a base, and it was adopted as the **suppletive deverbal of *þokss*** (orphaned-derivative adoption). The leveling is the unification evidence — speakers do not level vowels across words they treat as unrelated. First attested suppletion in the language (`terminology-registry.md`). Archaic/lectal variant *þautt* (pre-leveling) retained as speaker variation.

**Part of speech:** n.  **IPA:** /ˈθoʔ/  **Foot:** (ˈL) with /ʔ/ appendix [Open].

Phonological development: native /θ/ `þ`; vowel by analogy to *þokss* (not sound change); /t/→/ʔ/ `tt` (§2.7). The sound-change path alone gives *þautt* (/ɔː/→/ɑ/, glottaling).

Cross-refs: *þokss*.

#### Definition
1. a thought; an idea. — REC-eligible as *þokss*'s recognitional nominal: *þ þottś* "the thinkings (you know the kind)" [predicted, unattested].

---

### þri·ei·iiǫ

#### Etymology
*for a eon* — adverb "for a long time" (idiomatic *for an eon*).

**Part of speech:** adv.  **IPA:** /θɾi.ei.ˈiõ/  **Foot:** [Open].  **[IPA Prov.]**

Phonological development [Open]: *for* → `þr` (/f/→/θ/ `þ`; /ɔr/→/ɾ/ `r`); *a eon* → `ei·iiǫ` (hiatus). The interpuncts mark syllable division (formal register).

#### Definition

1. (adv.) for a long time; for ages.

---

### -wiis

#### Etymology
*-wise* — the aboutness suffix "concerning; with respect to."

**Part of speech:** suffix.  **IPA:** /-wiz/  **Foot:** —.

Phonological development: *-wise* /waɪz/ → /-wiz/ (/aɪ/→/i/ `ii`; final /z/, non-onset `s`).

#### Definition

1. (suffix) -wise; concerning; with respect to; about. (`language_reference.md` §3.8 aboutness.)

---


## 5. Changelog

A running record of additions and changes to the dictionary, with dates and any open questions surfaced.

### 2026-06-23

- **Sessions D — Batch D4-D (particles, markers, adverbs, affixes) — COMPLETE.** Added 23 entries:
  matrix particles *reś* (< *I guess*; MP.GUESS; supersedes *piies*), *nóuśshè* (< *in a nutshell*;
  MP.SUMM); quotation *quo* (< *quote*; + merger *resquo*), *o (interj.)* (quote-opener < *oh*), *ohei*
  (< *oh hey*; direct-Q marker); existential *ponś* (< *upon us*); clause linkers *rhishisben* (< *which
  is when/has been*), *kyii* (< *cue*); aboutness suffix *-wiis* (< *-wise*); onomatopoeia-object marker
  *-ðs* (< *this*); discourse adverbials *rhiksse* (< *you could say*), *beiskiiy* (< *basically*), *nóè*
  (< *no way*); deictics *rheiiem* (< *where I am*; "here"), *ouðeu* (< *over there*; "there"), *meirei*
  (< *m'aidez*; "come"); softener *rhilqui* (< *real quick*); adverbs *eńhii* ("inside"), *rhiþoupii*
  (< *without a peep*), *þri·ei·iiǫ* (< *for a eon*; "for a long time"); interjections *þiiaii*
  (< *finally*), *pauyiiś* (< *apologies*; cf. v. *pauyiis*); negation *nokw* (reduced *nocquii*). *noê*
  "in a way" already existed — only a back-cross-ref to its pitch-pair *nóè* was added.
- **Three-*o* homophone convention established (user decision):** homophonous headwords are disambiguated
  by a **parenthetical tag**. The quotative verb was re-tagged *o* → ***o (quot.)***; the quote-opener
  enters as ***o (interj.)***; the article ***o (art.)*** is pending its own entry.
- **Conventions for this batch:** tone is **not** marked in the broad IPA (user) — so the pitch-accent
  minimal pair *noê* / *nóè* both transcribe /noˈɛ/, the contrast carried by spelling + prose; *pons*
  spelled ***ponś*** (final /s/); *rheiiem* /ɻeiɪˈɛm/. Several particle IPAs/etyma are [Open]/[Prov]
  (phonotactically marginal or heavily reduced): *nóuśshè, rhishisben, þiiaii, þri·ei·iiǫ, eńhii, -wiis*.
- **Sessions D is now COMPLETE** (D4-A verbs, D4-B ideophones, D4-C nouns, D4-D particles + the two
  corrections). Next: a **quickref rebuild** to refresh `dictionary-index.md` / `phonology-quickref.md` /
  `orthography-quickref.md` against all the new/renamed entries.
- **B12 morphophonology corrections (set 1 of 2).** The concord-morphophonology elicitation
  (`drafts/translation_exercise_2/verb-coda-morpho-phon-study.xlsx`; now `verbal-system.md` §4.2.2,
  `phonology.md` §4.4.14) surfaced six entry-level fixes. Applied this session:
    - ***bényǫ*** changed to **noun-only** ("an opinion; a view") — *opinion* does not verbalize; the
      former "to think / to opine" verb sense removed.
    - ***reut*** note added: the form *reutto* "get it to" (< *get it to*, geminate /tː/) lives under this
      lemma, not as a separate headword.
    - ***ospii*** phon-development cross-refs repointed to the new fossil-resurrection family — labial
      rescue now §4.4.11 **[Settled]** (was "§4.4.1 … [Provisional]"); progressive *ospiihıĩ* noted (the
      /k/ breathing to /h/ where no /w/-suffix rescues it).
- **B12 morphophonology corrections (set 2 of 2) — coordinated phonology/orthography pass (user
  decision).** Two of the three deferred items were taken on with their cross-document consequences:
    - ***epplii* → *eplii* (no labial gemination):** GA *apply* /əˈplaɪ/ has a plain /pl/ onset, not an
      ambisyllabic /pp/ — the geminate was spurious. Headword, IPA (/ˈɛpli/), etymology, and phon-development
      updated; all live `rhiiyepplii`/`epplii` cross-refs respelled (*rhiiyeplii*; in the *rhiiy*, *rhiiynii*,
      *rhiiysseunnou* entries). Cross-doc: `phonology.md` v4.5 renamed §4.4.6 "apply gemination" →
      "labial gemination" and demoted it to [Provisional — unattested] (its only witness was *epplii*);
      `orthography.md` v3.9 flags `pp` = /pː/ as predicted-but-unattested. (Dated changelog entries below that
      cite *epplii* are left verbatim as historical record.)
    - ***rhikriu* → *rhikriutt* (glottal coda, user decision):** coda /t/ → /ʔ/ (coda glottaling, §4.4.11),
      written ⟨tt⟩; IPA /ɻɪˈkɾɪːʔ/. Under inflection the /t/ re-exposes (the fossil resurrection): progressive
      *rhikriuıĩ*, preterite *rhikriuri*. Synced in `verbal-system.md` §4.2.2 and `phonology.md` §4.4.14.
    - ***preb* → *baŕep*:** **resolved** (user confirmed the analysis) — see the prep-breaking item below.
- **prep-breaking rule + the three /pr/ verbs (user decision).** The B12 study revised all GA /pr/-initial
  verbs to a single onset reflex; the underlying rule is now formalized as **prep-breaking** (`phonology.md`
  §4.4.5, v4.6): word-initial /pr/ → /bɑˈɾ̥/ ⟨baŕ⟩ (cluster-breaking epenthetic /ɑ/, /p/→/b/, rhotic → devoiced
  tap /ɾ̥/). Entries reconciled onto it:
    - ***preb* → *baŕep*** /bɑˈɾ̥ɛp/ (resolves the old word-final /p/→/b/ flag — the word now simply ends in /p/).
    - ***beŕaumss* → *baŕaumss*** /bɑˈɾ̥ɑmsː/ (*promise*) — epenthetic /ɛ/ → /ɑ/, onset standardized.
    - ***baurrâuss* → *baŕâuss*** /bɑˈɾ̥ɑsː/ (*process*) — /ɻ/ ⟨rr⟩ → devoiced /ɾ̥/ ⟨ŕ⟩, epenthesis standardized.
      **[Open:** the study writes the headword *baŕâustts* (coda ⟨stts⟩); that coda revision is not derivable
      from current rules, so **only the onset was standardized** — confirm the intended coda.**]**
  - The /ɑ/-epenthesis is shown **general** to labial-stop + rhotic onsets: existing *baurrits* (< *bridge*,
    /br/) is the **voiced sibling** (rhotic stays /ɻ/) and now cites the rule. The two former ad-hoc flags
    (`[New rule needed: stop–rhotic epenthesis]`, `[Open: cluster epenthesis + /r/-devoicing]`) are retired.
    Companion: `phonology.md` v4.6; the §5.1 word-final-/p/-voicing sub-question withdrawn (its only evidence
    was *preb*).

### 2026-06-22

- IPA reconciliation pass (per `ipa-reconciliation-note.md`, surfaced by `spell2ipa.py`
  validation): corrected the devoiced rhotic from /r̥/ to /ɾ̥/ in *ŕe* and *ŕeut* (IPA
  fields, etymology prose, and cross-refs), and the nasal vowel from /ẽ/ to /ɛ̃/ in *ęy*
  (IPA field; nasalized glide /j̃/ kept). Both align the dictionary with `orthography.md`
  (`ŕ` → /ɾ̥/, §2.3; `ę` → /ɛ̃/, §3.6). The *éuskrıì* hypothetical /kr/→/ɾ̥/ note was also
  updated for symbol consistency, though the pathway it describes remains [Open].
- Left verbatim (house-style: dated changelog entries preserved): the /r̥/ mentions in the
  2026-04-30 *ŕe* entry, and the /ẽj̃/ mention in the 2026-05-20 *ęy* entry.
- Resolved (owner ruling): word-final `s` does **not** devoice — a final `s` is /z/ like any
  other non-onset `s`. Committed to `orthography.md` §2.2 (v3.5). Consequently **renamed
  *récquıìs* → *récquıìś***: its final /s/ (< GA *likewise* /z/) is retained but reanalyzed as a
  **lexical, idiosyncratic** devoicing rather than a regular rule, so the form now carries the
  devoicing diacritic `ś`. IPA /ˈɾɛkʷːis/ unchanged; Phonological-development line reworded; the
  live cross-ref in the *also/approximately* adverb entry and the labial-rescue attestation list
  in `phonology.md` §4.4.1 updated to *récquıìś*. Historical changelog/versioning mentions of
  *récquıìs* (here and in `phonology.md` v2.4) left verbatim. NB the `dictionary-index.md`
  quickref still shows *récquıìs* — it regenerates on the next quickref rebuild.
- Deferred / not yet applied: *ręim* /ˈɾẽim/ (`ęi` → /ẽi/) postdates the reconciliation note and
  carries the same /ẽ/-vs-/ɛ̃/ inconsistency, but via the `ęi` digraph; flagged for the owner to
  confirm whether Decision 3 extends to the `ęi` diphthong nucleus before editing.
- **Sessions D — Batch D4-A (verbs, SAYING core).** Added 11 new verb entries: *o* (quotative
  < *go*; suppletive perfect *rhentt*), *þilnn* (< *fill in*), *ospii* (< *speak*; combining form
  *ospokwþ*), *baurzıĩ* (< *barge in*), *bekw* (< *bicker*), *beŕaumss* (< *promise*), *pauyiis*
  (< *apologize*), *reut*/*reuto* (< *get it*), *rhiib* (< *drive*), *rhikriu* (< *recruit*),
  *rhinnw* (< *wonder*; frame-split). Appended a progressive-shaped note (*beussno*) to the
  existing *beussou*, kept as the lemma. IPA seeded with `spell2ipa`, then hand-corrected (stress:
  *baurzıĩ* on the *in* particle; *bekw*/*rhinnw* initial; the converter's final-stress default
  corrected throughout).
- **Open phonology flags (surfaced, not acted on — for a future phonology session):** word-initial
  /ɡ/-drop (*o*); /f/→/θ/ (*þilnn*); epenthetic-/o/ prothesis (*ospii*); /dʒ/→/z/ (*baurzıĩ*);
  /ɪ/→/ɛ/ (*bekw*); word-initial /p/→/b/, /pr/-cluster epenthesis, and unstressed /əs/→/sː/
  (*beŕaumss*); /ʌ/→/ɪ/ and /nd/→/nː/ (*rhinnw*); /dr/→/ɻ/ and coda /v/→/b/ (*rhiib*); coda
  /t/-retention (*reut*).
- **§3.22 progressive/-ed forms deferred [Open: pending B12]:** *bekrrıĩ*, *rhiimm*, *rhikriutm*,
  *beussno*, *pauyiist*.
- **Homophone flag:** quotative *o* is one of three homophonous *o* lemmas (article; quotative;
  quote-opener < *oh*); a disambiguation convention is still pending, to be settled when Batch
  D4-D adds the other two.
- **Correction — *rékriiyä* → *rekriiâ* (§2.6 override).** Renamed the headword in place and updated
  the form: final /æ/ → /ɑ/ `â`, the second-foot /jæk/ reduced (second /j/ → ∅, coda /k/ → ∅), and
  ultimate-syllable stress + pitch adopted (an ideophone-class licence). The entry **gains the
  ideophone sense** (dialect/"Rickety Yak" speech, wrist-rotation gesture) and is now the dictionary's
  first **ideophone (IDEO)**-class entry; the former chatter-verb sense is retained as the verbalized
  form *rekriiâkm*. IPA /ɾɛkˈɾiːæ/ → /ɾɛkɾiˈɑ́/. The reference docs (`ideophones.md`,
  `verbal-system.md` §4.2.3, terminology registry) already use *rekriiâ*; this brings the dictionary
  into line, and pre-handles the *rekriiâ* member of Batch D4-B.
- **No-op — *piies* retirement.** *piies* was never a `dictionary.md` headword (it is a matrix-particle
  member); its retirement/supersession by *reś* was completed in Sessions T/V/L (registry,
  `verbal-system.md` §11, `language_reference.md` §3.7) with trails. No dictionary action required;
  *reś* itself enters in Batch D4-D.
- **Sessions D — Batch D4-B (ideophones).** Added 5 ideophone (IDEO)-class entries: *rhemmemmêm*
  (< *boom boom boom*; bullet-pointed/confrontational; χ back-of-hand clap), *rhitmmtm* (< *nuh-uh*;
  refusal; *t* → /ʔ/, stress on geminate syllabic *m̩ː* — phonotactic licence), *bauwouwou*
  (onomatopoeic; speaking GA; χ wrist rotation), *riprprp* (< *drip drip drip*; onomatopoeia, via
  *-ðs*), *bet bät* (< *pitter-patter*; onomatopoeia, via *-ðs*). With *rekriiâ* (above), Batch D4-B
  is complete. All point to `ideophones.md` as the canonical class home; **IPA is [Provisional]**
  throughout, consistent with the hub deferring it to a phonology pass.
- **Hub sync + form finalized — *rhémmen·bèm* ~ *rhémm·bèm* → *rhemmemmêm* (done 2026-06-22).** The
  boom-boom-boom ideophone's form was finalized as ***rhemmemmêm*** (ultimate stress, /ɻɛmːɛmːˈɛm/;
  beats marked by gemination) and propagated to `ideophones.md` (v1.1 — §1, §2, §3, §5, §6, §8),
  `verbal-system.md` §12.1, and `terminology-registry.md`. **Interpunct loop closed:** per author
  ruling the interpunct has *no* beat/rhythm function — only syllable-division disambiguation — so the
  spurious "ideophone-beat" use was **retired** from `orthography.md` §3.5 (→ v3.6) and `ideophones.md`
  §7. The earlier stress/IPA discrepancy is resolved (stress now on the final beat, matching the
  circumflex *ê*). The ideophone **phonotactic-exemption rule** (`phonology.md`) remains its own
  already-flagged session item.
- **Sessions D — Batch D4-C (nouns).** Added 10 noun entries: *baıĩ* (< *money*), *baurrits* (< *bridge*),
  *bäeĩyi* (< *manager*), *belkm* (+ reduplicated *belkmlkm*; < *welcome*), *bǫëiio* (< *morning joe*;
  coffee; IPA [Open]), *eiem* (< *A.M.*), *noblę* (< *the blank*), *piiem* (< *P.M.*), *riųś* (< *news*;
  nasalized minimal pair with *riuś* "juice" — back-cross-ref added to *riuś*), *rheĩ* (< *rain*;
  progressive-shaped *rheinn* [Open: pending B12]). *riuś* "juice" already existed and was not re-added.
- **P/O reverberations flagged (applied to these new entries, but NOT yet swept across the lexicon — for a
  dedicated phonology/orthography session):**
  - **`au` = /ɑ/** (short), not /ɑː/ — orthography. Sweeps every `au` IPA, incl. D4-A *baurzıĩ*, *beŕaumss*
    and existing *baunnw*, *baurrâuss*, etc.; the `spell2ipa` table (`au`→/ɑː/) needs updating. (`aa` = /ɑː/
    deliberately **deferred** — may not occur; add only when a form needs it.)
  - **non-initial `rr` = /ɻ/** (the non-initial spelling of `rh`), not a geminate tap — orthography. Sweeps
    *baurrâuss*, *baurrits*; the converter (which geminates `rr`) needs the rule.
  - **Rhotic renotation** — phonology §4.4.1: GA "r" is broad notation for /ɻ/ (no change in the approximant);
    the innovation is the **tap /ɾ/** phonemicizing (a GA allophone of /d/). Renotate the "/r/→/ɻ/" SC steps.
  - **`nopiem` → `nopiiem`** downstream of *piiem* (`verbal-system.md` §12 / `ideophones.md`).
- **P/O session executed (2026-06-22).** Items 1–4 of the reverberations above, done. **`au` = /ɑ/:**
  committed to `orthography.md` v3.7 (the one non-lengthening `Vu` digraph; the `a`/`au` overlap framed as
  a naturalistic low-back asymmetry — schwa de-phonemicized) and `phonology.md` v4.3; swept 6 dictionary
  IPAs (*baunnw*, *baurrâuss*, *baurzıĩ*, *bauwouwou*, *beŕaumss*, *pauyiis*) + their `au` SC-mentions (and
  the hypothetical *þautt*); `spell2ipa.py` table updated (`au`→/ɑ/). **`rr` = /ɻ/:** the dictionary was
  already correct (*baurrâuss* /bɑˈɻɑsː/, *baurrits* /bɑˈɻɪts/); added the rule to `spell2ipa.py`
  (`rr`→/ɻ/). **Rhotic renotation:** the 4 SC lines reading "/r/→/ɻ/" (*rhemmêś*, *rhibôet*, *rhikriu*, and
  the *-ing* entry) renotated to "GA rhotic /ɻ/ retained"; `phonology.md` v4.3 overview clarified.
  **`nopiem` → `nopiiem`:** done in `verbal-system.md` §12 + `ideophones.md`; *piiem*'s cross-ref updated.
  Still open: the pre-existing May P/O backlog (dotless-`ı`, `iiy` stress-grave, circumflex headwords; the
  §5 phonology bucket) and the ideophone phonotactic-exemption rule.
- **Orthography respell-sweep verified (2026-06-22).** The `œ`→`oë` / `æ`→`ä` convention sweep is
  complete in the dictionary body (headwords swept incrementally / at orthography v3.1: *boë, noë,
  boëś, hoë hoś*); the lone remaining orthographic stray — *rékriiyæ* → *rékriiyä*, in the *rekriiâ*
  supersession trail — is fixed. All other `æ` are IPA /æ/ or GA reconstructions (untouched); `œ` no
  longer occurs. `cascade.py` is not in the repo. The `dictionary-index.md` / `phonology-quickref.md` /
  `orthography-quickref.md` quickrefs still show pre-sweep forms (*bœ, nœ, boeś*) and refresh on the
  next quickref rebuild. The separate *boëś* diphthong-vs-hiatus question stays [Open]. (`orthography.md`
  §6 "respell sweep (pending)" closed → v3.8.)

### 2026-06-12

- **Batches A + B (translation-exercise lexicon), 36 entries**, written after a two-draft review cycle with user corrections applied: *bényǫ* (pitch-explicit; ogonek-fold), *kli* (< *klik*; coda k-loss regular, perfect *klikt*), *baurrâuss* (< *berrauss*; epenthetic /ɑ/), *nott* (< *not*; glottal coda), *ǫ* (citation form; *ǫıĩ* reanalyzed as imperfect), *rhıĩ* (+ ring-noun sense), *split* (+ transitive share sense), *þautt* (< *þau*; glottal coda; suppletive-deverbal proposal), *þliu* (< *þlii*), *riuś* /ˈɾɪːs/, *thių* /tʰɪ̃ː/, *benkwtt* (GA-input pre-/ŋk/ conditioning recorded). Collisions: *béuksoè*, *beykw* pre-existing; *beykw* respelled **beikw** (approved). Grapheme sweep executed (*ä*, *oë*; *boëś*; collation §2 updated); stale /ɔɪ/ flags repaired to choice-smoothing citations. Schema §1: frame-tagged senses convention adopted.
- **[New rule needed]** for the next phonology session: **/ŋ/ resolution** — no /ŋ/ phoneme: word-final /Vŋ/ → nasalized vowel + elision (*rhıĩ*; and the *-ing* reflex /ĩː/ in *ǫıĩ* — the first attested *-ing* outcome, the §5 scaling answer); pre-/k/ /ŋ/ → /n/ with [ŋ] allophony (*benkwtt*, *rhink*). **Long-GOOSE split** — /uː/ → /ɪː/ `iu` (*riuś*, *þliu*, *thių*) beside short goose-foot-strut /ɨ/; the *do*-counterfactual in §5.2 should read *riu*, not ⟨ii⟩. **/ts/ → /sː/ coalescence** (*ossıî*). **Stop–rhotic epenthesis = /ɑ/** (*baurrâuss*; propagate to future derivations). **Latent-coda resurfacing** as a class: *kli* ~ *klikt* joins linking *r* (*bemmw* ~ *bemmorret*). **Homorganic nasal-stop leveling** /mb/→/mː/ (*bemmw*).
- **Open phonological questions (data logged):** coda-/t/ conditioning — glottaling (*nott*, *þautt*, *meiktt*, *benkwtt*) vs. retention (*split*, *rhibôet*, *rérèyt*); pass-out word-initial voicers now three (*beussou*, *baunnw*, *baurrâuss*) against resisters (*pot*, *pikkp*, *piquô*); aphesis (*bemmw*, *bényǫ*); /ɪ/-lowering (*bényǫ*, *renw*); medial /t/ loss (*nouś*); medial /n/ loss (*rhemmêś*); appendix /ɨ/-deletion (*pikkp*); affricate-fork ordering relative to the stress shift (*ŕequôþw* pre-shift vs. *rhiitsô* post-shift); word-final /p/ voicing (*preb*); retained-coda nasal spreading (*ręim*).
- **Open orthographic questions:** `sh` vs. `š` (*ŕeush*, *rhiiyshêush*); headword pitch-marking/circumflex pass for this batch (convention application unconfirmed — entries carry user-attested marking only); collation re-sort pass pending tooling; canonical final-/ʔ/ spelling (`tt` vs. `ʔ` glyph).
- **Registry:** first **suppletion** candidate annotated — *þokss/þautt* deverbal pairing (user proposal; activation and the *þott* leveling variant pending decision).
- **Policy:** two non-GA lexemes admitted (*rhémstwè*, *twıítò*) — nonce-source policy line flagged for the recipe's next revision.
- **Same-day verdicts applied:** *þott* adopted over *þautt* (suppletion **activated** — first attested case, *þokss/þott*; registry updated; *þautt* retained as archaic variant). `sh` over `š` (collation §2 and entry flags updated; `š` retired). Circumflex pass run on the batch — monosyllables and single-full-vowel words exempted [scope decision, confirm]: *rhibôet*, *ossıî* (user-specified); *baurrâuss*, *rhiitsô*, *ŕequôþw*, *rhiiyshêush*, *rhemmêś* (extension, for review). `ʔ` ruled IPA-only: orthography sample forms corrected to `tt`; **[Open: pre-consonantal /ʔ/ spelling — *hoʔnʔnts* headword pending]**; **[Open: pre-convention headword retrofit — *ŕeut* (final glottal → *ŕéutt*?), with the existing unretrofitted-pitch set]**. Remaining non-coincident polysyllables' acute pitch-marking (*osquihii* → *osquíhii*?) **[Open — follow-up pass]**.

### 2026-06-10

Terminology and pointer cleanup; no entries added or removed. Historical changelog entries below are left verbatim as records.

- **Registry sweep (June 2026 batch):** entry bodies for *ęy*, *nocquıî*, *rhiiy*, and *skwkw* normalized from *volitive / non-volitive* to *go-ahead / get-oneself*; *nocquıî*'s reading-distribution open question restated with the four reading names (happenstance, effortful self-benefit, threshold, backdrop — formerly PH/AB/INC/PS); *ritsstw* and *toutw* Foot lines and cross-refs updated from *sesquisyllabic* to *appendix*.
- **Gloss tags:** NONVOL → NVOL in POS lines and sense labels (LVC.NVOL.NEG, NVOL.NEG), matching `terminology-registry.md` and verbal-system v2 (user decision, 2026-06-10).
- **Stale [Open] flags closed against committed rules** (user decision, 2026-06-10): *beussou* /p/→/b/ environment (phonology §4.4.1), *epplii* initial-schwa strengthening (E5, §4.4.3), *rhiiysseunnou* /nd/→/nː/ (§4.4.1). *toutw*'s coda-/l/ flag repointed at E2c (§4.4.3, paths still [Open]); *epplii*'s /aɪ/ flag repointed at the §5.1 data-gathering bucket.
- **Pointer repairs to current sibling numbering:** phonology §6.1 → §4.5 (*ritsstw*, *ŕeut*); phonology §5.2 → §4.3 (*toutw*); orthography §4 → §1 (*hohô*). §3's `ss` note and *nocquıî*'s `cqu` note updated from "pending propagation" to propagated (`orthography.md` §2.2/§2.4, with `cqu`-vs-`kkw` standardization [Open] in its §6).

### 2026-05-24

Batch addition: 36 new entries from `drafts/batch-dict-entry-0523.xlsx` (51 source rows; some consolidated or deferred). Entries span the b-, e-, h-, n-, o-, p-, r-, rh-, s-, and t-regions. All entries with unresolved phonological steps carry inline `[Open]` flags; none resolve any existing `[Open]` items without an explicit decision.

**Open questions surfaced (propagate to phonology session):**
- /v/ conditioning: /v/ → /b/ before back vowels vs. /v/ → /ɾ/ (tap merger) before front vowels — candidate rule, not yet committed.
- /ɫ/→/ɻ/ candidate rule: all /l/-initial GA words → /r/-initial headwords, suggesting dark-l vocalization path to /ɻ/ → R-Assim → /ɾ/.
- /ɪ/→/ɛ/ after onset: appears in *benskyi*, *béntsıìy*, *rékwıì* — rule not in §4.
- /ə/→/o/ after /n/: flagged in *noê* — rule not in §4.
- /aɪ/→/ɛ/ short reflex: third candidate pathway alongside established /eː/ and /i/ reflexes.
- /aɪ/→/i/ short reflex: fourth candidate; appears in *récquıìs*, *rıírǫ*, *rhiwıĩ*.
- /ɔɪ/→/oe/: parallel to established boë/boeś pathway; now attested in *noë* as well.
- /ɜːr/→/ɨː/ vocalization: needed for *rhiušp*; not in §4.4.2.
- Coda /t/ retention vs. E2a: *pot*, *rérèyt* show unexpected /t/ retention.
- /k/ labialization: coda /k/ absorbing adjacent /w/ → /kʷ/; needed for *piiquóä*, *piquô*, *récquıìs*.
- /s/ in /sp/ cluster: debuccalization blocked? Needed for *spyi*.

**New entries (collation order):** *barnkw*, *bárkennò*, *bawiiquoh?*, *bayarę*, *bąêų*, *benıîä*, *benskyi*, *beńt*, *béo·ò*, *bessts*, *béuksoè*, *beušiioskô*, *beusp*, *beųtw*, *bewii·iit*, *bewiipessô*, *beykw*, *bęiink*, *boëś*, *boë*, *e*, *emmáwwè*, *éuskrıì*, *hohô*, *hóhonìt*, *hoë hoś*, *noê*, *nóeıìe*, *noë*, *ohô*, *óhò*, *ouś*, *piiquóä*, *piquô*, *pot*, *récquıìs*, *réıì*, *rékriiyä*, *rékwıì*, *rérèyt*, *reųś*, *rıírǫ*, *rhéulyèś*, *rhiušp*, *rhiwıĩ*, *spyi*, *toś*.

**Deferred/compound entries (IPA [Open]):** *bawiiquoh?*, *bárkennò*, *beušiioskô*, *bewii·iit*, *bewiipessô*, *nocquiie-ŕóųzǫ* (already present).

### 2026-05-20

Added four negative-system morpheme entries: *ęy*, *nocquıî*, *rhiiy*, *skwkw*. Back-cross-refs to *rhiiy* added to *epplii*, *rhiiynii*, *rhiiysseunnou*.

- **ęy** (ę-region, first ę-entry): VOL.NEG concord reinforcer from GA *any* /eni/. POS: `aux.` Orthographic decision: glide nasalization in /ẽj̃/ left unmarked — headword *ęy*, not *ęỹ* — on the grounds that nasalization is predictable from the flanking nasalized vowel. [Open: function-word smoothing condition — a lexical word such as *penny* would remain disyllabic; rule not yet in §4.]
- **nocquıî** (n-region, after *nobêt*): LVC.NONVOL.NEG from GA *not quite* /nɑʔ kwaɪʔ/. POS: `aux.`; also adv. and deriv. prefix. Includes Morphology section for the *nocquii-* prefix. Spelling: `cqu` for /kʷː/ dictionary-internal pending `orthography.md` propagation. [Open phonological questions: (1) /ɑ/→/o/ raising-and-rounding — new rule needed. (2) /ʔk/→/kʷː/ junction gemination — new rule needed. (3) coda /ʔ/ drop condition at compound junctions — new rule needed.]
- **rhiiy** (rh-region, first rh-entry — before *rhilþ*): polyfunctional morpheme from GA *really* and *not really*, consolidated as a single lemma. Per-sense etymology adopted as a schema extension for polyfunctional grammaticalized morphemes with divergent source phrases. POS: `aux.` (general negation and NONVOL.NEG reinforcer); also deriv. prefix. 4 senses.
- **skwkw** (s-region, first s-entry — between *ŕeut* and *toutw*): LVC.VOL.NEG from GA *skip* /skɪp/. POS: `aux.`; also adv./substitutional and interj. Derivation flagged as irregular. [Open: foot structure of vowelless syllabic obstruent.]
- **POS tag decision:** `aux.` adopted uniformly for all four negative-system markers. Draft source used `gram.`; not adopted.
- **Headword revision:** *hoiom* → *hoiiǫ* (/ˈhoiom/ → /ˈhoiõ/). Phonological development clarified: labial /m/ colors the preceding schwa to /o/ (rather than the expected /ɛ/ from regular strengthening), then /m/ elides leaving nasalization on the vowel. The prior [Open] on the final syllable (§6.2) is resolved for this entry. [Open: labial-coloring-of-schwa + /m/-elision-with-nasalization proposed as a productive rule for all *-ium* endings (*podium*, *Colosseum*, *Liam*); to be formalized in `phonology.md` in a dedicated session.]
- **Three *nocquii-* compounds** added as stubs (all base words pending): *nocquiiayo* (decaf; base *ayo* "joe/coffee"), *nocquiie-ŕóųzǫ* (Down syndrome; base *ŕóųzǫ* "chromosome"), *nocquiissprıĩ* (the cold false-spring weeks; base *sprıĩ* "spring"). Collation order: nocquiiayo (a) < nocquiie-ŕóųzǫ (e) < nocquiissprıĩ (s). [Open: the *nocquiiayo* headword lacks the linker *-e-* that the *nocquıî* Morphology section predicts before vowel-initial bases — combining-form rule needs reconciling.]

### 2026-05-19

- Added entry *rhilþ* ("wolf"). Straightforward derivation from GA *wolf* /wʊɫf/; all three sound changes settled (onset /w/ → /ɻ/, /ʊ/ → /ɪ/ by convention, /f/ → /θ/). Coda /l/ preserved in cluster /lθ/ (E2c exempts cluster environments). Foot left [Open] pending resolution of whether coda consonants contribute weight.
- Added entries *béntsıìy* ("later") and *nobêt* ("soon; in a short while"), cross-referenced as anaphoric/deictic counterparts.
  - **Open phonological questions (*béntsıìy*):** (1) /v/ → /b/ in onset — §4.4.1 gives general /v/ → /r/; new environment-specific rule proposed. (2) /ɫ/ → /j/ with palatal consonant as left flank — §4.4.1 conditions the rule on both flanks being high front vowels; this extends or replaces that environment.
  - **Open phonological questions (*nobêt*):** (1) /ə/ → /o/ rounding after /n/ — no current rule in §4.4.2. (2) /ɪ/ → /ɛ/ after /b/ — no current rule in §4.4.2.
  - **New orthographic conventions (see §3):** (1) Dotless `ı` when one element of the `ii` digraph takes a diacritic — dictionary-internal, pending `orthography.md` propagation. (2) Stress grave on the vowel element of `iiy` (the second `i`) rather than on trailing `y`, conflicting with `orthography.md` §3.7 — pending reconciliation. (3) Circumflex used in headwords when pitch and stress coincide (formal-register form), as in *nobêt*.

### 2026-05-17

- **Schema reformatting.** All existing entries (beussou, epplii, hoiom, hoʔnʔnts, ritsstw, rhiiynii, rhiiysseunnou, ŕe, ŕeut, toutw) converted to the new prosaic format per §1: etymology line with drift folded in, single form line (POS/IPA/foot), compact Sound changes line. Explicit field headers (`**GA etymology:**`, `**Part of speech:**`, etc.) and standalone `[Drift note: ...]` brackets removed. Notes sections stripped of propagation tickets and paradigm-candidate flags; only form-specific observations retained.
- **Schema revision (second pass).** All 10 entries reformatted with: (1) `#### Etymology` as a labeled section opener; (2) explicit `**Part of speech:**`, `**IPA:**`, `**Foot:**` labels on the form line; (3) `Sound changes` renamed to `Phonological development` throughout. Preamble files updated to route all monospace font to Brill (`\let\ttfamily\rmfamily`), eliminating DejaVu Sans Mono from compiled output.

### 2026-04-30

- Added entry *ŕe* ("today"; interj. "hurry!"). High-frequency colloquial form with two irregular shifts (onset /t/ → /h/, /eɪ/ → short /ɛ/), neither proposed as a rule.
  - **Open phonology nuance:** the /h/ + tap → /r̥/ coalescence in onset (without M1 metathesis) is plausibly a generalization of the M1 mechanism in `phonology.md` §4.3 — worth clarifying when phonology is next revised.
  - **Open phonology revision:** `phonology.md` §8.1 stipulates that degenerate (single-syllable) feet are licensed only if the syllable is heavy; *ŕe*'s light-monosyllabic foot /ˈr̥ɛ/ is a counterexample. The minimality clause appears to be an overgeneralization on limited data and should be relaxed when phonology is next revised.
- Added entry *beussou* ("to sleep; to pass out").
- **Schema revision:** renamed "GA etymon" to "GA etymology" in §1, expanding the field to accommodate drift notes and source-construction context. Existing entries (*hoiom*, *hoʔnʔnts*, *ŕeut*, *ritsstw*) updated to use the new bullet label.
- **Orthographic addition:** added §3 note on `ss` /sː/ as standard geminate spelling, with `śś` as formal variant. Convention is dictionary-internal pending propagation to `orthography.md`.
- **Open phonological question:** new rule needed in `phonology.md` §4.1 for /s/ → /sː/ at syllable boundary preceding stress (vs. default /s/ → /h/).
- **Open phonological question:** environment for /p/ → /b/ in onset to be finalized — current proposal is "before /ɛ/ (and long counterpart), blocked before /i, ɪ, ɑ, o/ and clusters."
- **Open phonological question:** §4.1's "coda /ʔ/ never elides" needs softening to permit lexical exceptions in grammaticalized particles (e.g., GA *out* in phrasal-verb lexicalizations).
- **Open orthographic question:** with `s` predictably voiceless in onset (since onset `s` derives only from GA /st/, GA /s/ having debuccalized to /h/), the `ś` grapheme may be redundant in onset position. Worth verifying against `orthography.md` whether `ś` is doing real work outside non-onset environments.
- **Cross-system note:** *beussou* flagged as candidate verb for volition-paradigm illustration (`language_reference.md` §3.4.2).

### 2026-05-03

Batch addition of four verbs: *epplii*, *rhiiynii*, *rhiiysseunnou*, *toutw*. Plus collation fix for *ritsstw*.

**Entries added:**

- Added entry *epplii* ("to spread on; to apply oneself; to apply for"). Three senses inherited from GA *apply*'s polysemy. Sense 2 admits an alternative form *rhiiyepplii* with an `rhiiy-` intensifier prefix.
- Added entry *rhiiynii* ("to need; to want"). Lexicalizes GA *really need* with a fully-bleached `rhiiy-` prefix from *really*. The need/want polysemy is a productive cultural/grammatical marker.
- Added entry *rhiiysseunnou* ("to be different; to be excellent"). Lexicalizes GA *really stand out* with the same fully-bleached `rhiiy-` prefix.
- Added entry *toutw* ("to cost; to amount to"). Lexicalizes GA *to total to* as a single verb.

**Collation fix:**

- Moved *ritsstw* to its correct position per the alphabet (`r < rh < ŕ`). It had been incorrectly placed at the end of the entries section (after the ŕ-region); it now sits between the h-region (after *hoʔnʔnts*) and the rh-region (before *rhiiynii*). No content changes to the entry itself.

**Open phonological questions surfaced:**

- **/iː/ as a phoneme.** `orthography.md` §3.2 states /iː/ does not occur in the conlang, but *rhiiysseunnou*, *rhiiynii*, and the existing *Emily* derivation in `phonology.md` §6.1 all attest /iː/ from /ɪji/-smoothing. §3.2 needs revision to admit /iː/ as a phoneme. The orthographic spelling `iiy` is the working convention for long /iː/, with bare `ii` reserved for short tense /i/ — this contrast is on display within *rhiiynii* itself (prefix `rhiiy` /ɻiː-/ vs. stem `nii` /ni/).
- **/nd/ → /nː/ in coda.** Attested in *rhiiysseunnou*. New rule needed in `phonology.md` §4: nasal+stop coda cluster simplifies to geminate nasal, by regressive assimilation or compensatory lengthening.
- **Coda /l/ → ∅ outside clusters.** Attested in *toutw*. `phonology.md` §3.2 implies this diachronic loss (since /l/ "occurs only in clusters") but §4 does not state it explicitly. Should be added or subsumed under E2.
- **Initial unstressed /ə/ → /ɛ/.** Attested in *epplii*. New rule needed in `phonology.md` §4.2: initial schwa (when not absorbed or elided) strengthens to /ɛ/, paralleling the final-schwa-strengthening pathway already in §4.2.
- **/aɪ/ → short /i/.** Attested in *epplii*. `phonology.md` §4.2 lists /ai/ → /iː/ ~ /eː/ as conditioning-open; *epplii* adds short /i/ as a third reflex. Conditioning still open — possibly stressed-position-before-geminate, possibly lexically conditioned for high-frequency verbs.
- **Aspiration's phonemic status.** Surfaced by *toutw*'s /ˈtoːtw̩/. Treated as allophonic and orthographically silent (English-style: voiceless stops aspirate in stressed onsets), but not yet committed in `phonology.md`.

**Reused phonological flags from prior changelog entries** (no new commitment needed, but worth noting which entries newly attest each rule):

- `/st/ → /sː/ at stressed-syllable boundary` — first flagged with *beussou*; now also attested in *rhiiysseunnou*.
- `Coda /ʔ/ drop in lexicalized *out*` — first flagged with *beussou*; now also attested in *rhiiysseunnou*.
- `/ɫ/ → /j/ between high front vowels` — implicit in the *Emily* derivation in `phonology.md` §6.1; now explicitly attested in *rhiiynii* and *rhiiysseunnou* as a regular rule.

**Open orthographic questions surfaced:**

- **Geminate-doubling generalization.** Dictionary §3 currently licenses `ss` for /sː/ only. This batch generalizes the principle: `nn` for /nː/ (in *rhiiysseunnou*), `pp` for /pː/ (in *epplii*). The unified rule — "doubled consonants represent geminates" — should be propagated to `orthography.md` §2.
- **`eu` digraph unification across two diachronic sources.** `orthography.md` §3.2 lists `eu` as the smoothed-schwa pathway for long /ɛː/ only. *rhiiysseunnou* attests a second pathway: /æ/-with-preserved-duration before nasals, where GA's tense-lax distinction is reanalyzed as length. The orthography unifies both sources under `eu`. Worth recording in `orthography.md` as a single graphemic rule with two etymological feeds.
- **Spelling convention for /iː/ vs. short tense /i/.** Working rule (from this batch): long /iː/ is `iiy` where there's an etymologically-justified glide source, and bare `ii` is short tense /i/. The contrast is on display in *rhiiynii*. To be confirmed when `orthography.md` §3.2 is revised.

**Cross-system notes:**

- *rhiiysseunnou*, *rhiiynii*, and *epplii* (sense 2) all flagged as volition-paradigm candidates (`language_reference.md` §3.4.2), joining *beussou*. The growing set of volition-relevant verbs is starting to anchor the eventual paradigm illustration.
- The `rhiiy-` prefix from bleached *really* shows productive stratification across the lexicon: fully bleached/lexicalized in *rhiiysseunnou* and *rhiiynii*, still functionally an intensifier in *rhiiyepplii*. This is a good candidate for a future grammatical note in `language_reference.md` on incomplete grammaticalization as a productive design feature.