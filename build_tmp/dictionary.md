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

- `#### Definition` — numbered glosses.
- Examples appear inline within the definition they illustrate, separated from the definition text by an em dash. Conlang form in italics, followed by the English translation in double quotes. No separate `#### Examples` heading.
- `#### Morphology` — inflected/derived forms when committed.
- `#### Notes` — observations genuinely specific to this form: irregular surface properties, optional realizations, notable phonotactic patterns. Not for propagation tickets, pending rule discussions, or paradigm-candidate flags — those go in the session changelog or target document.

Any section may be omitted. When a committed field depends on an unresolved question elsewhere, mark `[Open: see phonology §X]`.

---

## 2. Collation Order

The conlang alphabet, in sort order:

> a, ą, b, ð, e, ę, æ, h, i, ii, k, l, m, ḿ, n, ń, o, ǫ, œ, p, r, rh, ŕ, s, ś, š, t, þ, w, w̃, y, ỹ

**Rules:**

1. Within a base letter's region, undiacriticked sequences sort first by Latin order on subsequent characters, then diacriticked forms follow.
   - Example a-region: `a` < `aa` < `au` < `aų` < `ą`
   - Example e-region: `e` < `ee` < `eu` < `eų` < `ę`
   - Example i-region: `i` < `ia` < `iu` < `ių` < `iyi` < `ĩ`
   - Example o-region: `o` < `oo` < `ou` < `oų` < `ǫ`

2. `ii` and `rh` are distinct phonemes, not digraph extensions of `i` and `r`, and have their own slots in the alphabet:
   - `i`-region (all `i`-initial sequences and `ĩ`) < `ii`-region (`ii`, `iia`, etc.)
   - `r` < `rh` < `ŕ` — the devoiced tap `ŕ` sorts last because devoiced `r` and devoiced `rh` collapse to a single phoneme, placed at the end of the rhotic series.

3. `æ` and `œ` are independent letters slotted into the bare-letter sequence (after the a-region and after the o-region respectively), not treated as diacritic forms.

4. Consonant diacritic forms (`ḿ`, `ń`, `ŕ`, `ś`, `š`, `w̃`, `ỹ`) follow their bare letter immediately, since consonants do not form length digraphs.

5. `ð` takes the slot where `d` would be (after `b`); `þ` takes its own slot (after `t`).

---

## 3. Orthographic Notes

A few conventions clarified during early entry-writing, supplementing `orthography.md`:

- The diphthong `/ei/` (phonemically `/ey/`, with `y` /j/ as the glide) is written `ei`. This is distinct from the length digraph `eu` /ɛː/ — `e` followed by `i` is the diphthong, `e` followed by `u` is length.

- **Geminate `ss`** represents /sː/ (voiceless long). This works in concert with the rule that `s` is /z/ intervocalically and finally but /s/ in onset (where it derives from GA /st/, GA /s/ having debuccalized to /h/). The doubled `ss` is therefore the standard spelling for a voiceless geminate; the formal/pedagogical variant `śś` is also licensed. Note: this convention is dictionary-internal pending propagation to `orthography.md`.

- **Dotless `ı`** appears when one element of the `ii` digraph takes a diacritic: the marked element retains its dot, and the unmarked partner is written as `ı` to reduce visual clutter. Example: in *béntsıìy*, the stress grave lands on the second `i` of the `iiy` digraph (written `ì`), and the first `i` becomes `ı`. Now propagated to `orthography.md` §3.7.

- **Circumflex in headwords**: when pitch and stress coincide on the same vowel, the dictionary headword uses the circumflex (formal-register form) rather than the bare acute. Example: *nobêt* (pitch and stress both on /ɛ/). Earlier entries with coinciding pitch and stress (*ŕeut*, *hoʔnʔnts*, etc.) predate this convention and have not been retrofitted. Now propagated to `orthography.md` §3.7.

---

## 4. Entries

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

### bárkennò

#### Etymology
*parking lot* — the full compound, lexicalized as a single noun.

**Part of speech:** n.  **IPA:** [Open]  **Foot:** [Open].

Phonological development: /p/ → /b/ onset [Open: before /ɑ/, the §4.4.1 refinement nominally blocks /p/→/b/; onset /p/→/b/ before /ɑ/ would extend the rule — new environment]; /ɑːɹk/ with pre-consonantal /ɹ/: /ɹ/→/ɾ/, /ɑ/ stays short (pre-consonantal, not coda) → /ɑɾ/ → `ar`; cluster-internal /k/ stays [Open: see *barnkw*]; /ɪ/ → ∅ or /ɛ/ [Open: unstressed /ɪ/ treatment]; /ŋl/ → /nː/ [Open: the §4.4.1 /nd/→/nː/ rule is regressive assimilation; /ŋl/→/nː/ would require a separate rule or a generalization — /ŋ/→/n/ by place assimilation to following lateral, then /nl/→/nː/ geminate]; *lot* /lɑt/: /l/ onset → [Open: onset /l/ treatment]; /ɑ/ → /o/ [Open: /ɑ/→/o/ not in §4.4.2]; /t/ → /ʔ/ (E2a) → appears to drop in the headword.

#### Definition

1. parking lot; car park.

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

Phonological development: /v/ → /b/ onset [Open: /v/→/b/ environment; see *béntsıìy*, *boeś*]; /aɪ/ → /ɑ/ + glide /j/ retained as a separate segment [Open: expected reflexes of /aɪ/ are /eː/ or short /i/ per §4.4.2; /ɑ/+/j/ outcome is unattested — new conditioning environment or new rule]; /ə/ → ∅ (absorbed, E4); /l/ → /ɾ/ [Open: /l/→/ɾ/ not in §4.4.1; onset /l/ has no stated merger to tap; flag for phonology session]; /ɪn/: /n/ elides intervocalically (E1), nasalization transfers to /ɪ/ (S1) → /ɛ̃/ (lowering of /ɪ/ in this position [Open: /ɪ/→/ɛ/ under nasalization? not stated in §4.4.2]) → `ę`.

#### Definition

1. violin.

---

### bąêų

#### Etymology
*banana* — the fruit; no semantic shift.

**Part of speech:** n.  **IPA:** /bɑ̃ˈɛ̃ː/  **Foot:** (L)(ˈH).

Phonological development: /bəˈnænə/ — both intervocalic /n/ elide (E1), each transferring nasalization to adjacent vowels (S1); initial /ə/ → /ɑ/ (E5 strengthening) + nasalized by left-flanking residue of first /n/ → /ɑ̃/ → `ą`; /æ/ (V₂) + nasalization from both flanking /n/ elisions → /ɛ̃/ via /æ/-before-nasal pathway (§4.4.2) with duration preserved; final /ə/ (V₃) absorbed into /ɛ̃/ as length suffix → /ɛ̃ː/ → `êų` (circumflex on ê: pitch + stress coincide; ogonek on ų: nasal long vowel).

#### Definition

1. banana.

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

### benıîæ

#### Etymology
*vanilla* — the flavor/plant; no semantic shift.

**Part of speech:** n.  **IPA:** /bɛˈniæ/  **Foot:** (L)(ˈH) [Open: whether final /æ/ is a separate light syllable or part of a diphthongal heavy nucleus with /i/].

Phonological development: /v/ → /b/ onset [Open: /v/→/b/ environment; see *béntsıìy*, *boeś*]; initial unstressed /ə/ → /ɛ/ (E5) → `e`; /n/ does not elide [Open: E1 targets intervocalic /n/; in *vanilla* the /n/ is onset of the stressed syllable between two vowels — possible blocking of E1 in stressed-onset position; needs rule statement]; stressed /ɪ/ + /j/ glide (from /ɫ/→/j/ between flanking high front vowels /ɪ/ and /ə/) → /iː/ → `ıî` (circumflex = pitch + stress coincide) [Open: left flank is /ɪ/, right flank /ə/ — §4.4.1 conditions /ɫ/→/j/ on *high front vowel* flanks; /ə/ is not high front]; final /ə/ strengthens to /æ/ [Open: /ə/→/æ/ in word-final position rather than expected /a/ from E5; new conditioning].

#### Definition

1. vanilla (the flavor and the plant).

---

### benskyi

#### Etymology
*minuscule* — the adjective; no semantic shift.

**Part of speech:** adj.  **IPA:** /bɛnˈski/  **Foot:** (H)(ˈL).

Phonological development: /m/ → /b/ (§4.4.1 /m,p/→/b/ in onset); /ɪ/ (V₁) → /ɛ/ [Open: /ɪ/→/ɛ/ rule; see *nobêt*]; /n/ does not elide [Open: same stressed-onset blocking question as *benıîæ*]; /ɪ/ (V₂) → ∅ (E3: unstressed vowel, cluster-feeding position); /sk/ cluster-internal → both segments stay [Open: onset /s/ debuccalizes to /h/ normally; cluster position may shield it — not stated in §4.4.1]; /j/ (from /kj/) → /j/ → `y`; /uːl/: /uː/ → /ɪ/ (§4.4.2 back-vowel fronting, short reflex), /l/ → ∅ (E2c coda-singleton elision) → /ɪ/ → `i`.

#### Definition

1. small; tiny; minuscule.

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

Cross-refs: *rıírǫ* (general "approximately; around"); *récquıìs* (also; likewise — different temporal reference direction).

---

### bessts

#### Etymology
*message* — the verb "to send a message to someone"; digital/text communication primary.

**Part of speech:** v.  **IPA:** /ˈbɛsːts/  **Foot:** (ˈH) heavy monosyllable.

Phonological development: /m/ → /b/ (§4.4.1); /æ/ → /ɛ/ (short reflex); /s/: gemination [Open: the /s/→/sː/ gemination rule applies at the syllable boundary preceding stress; in *message* the stressed syllable is the first (/ˈmæs/), so the /s/ is not preceding stress but within the stressed syllable — rule environment unclear for this case]; /ɪ/ → ∅ (E3); /dʒ/ → /ts/ [Open: /dʒ/ is in E1's intervocalic set; in word-final coda position with no following vowel, coda /dʒ/ treatment is unspecified — /dʒ/→/ts/ by partial devoicing is a plausible path but not a stated rule].

#### Definition

1. to send a message to (someone); to text; to DM.

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

Phonological development: /pʰ/ → /b/ [Open: environment to be finalized — see phonology §4.1]; /æ/ → /ɛː/; /s/ geminates to /sː/ at stressed-syllable boundary rather than debuccalizing; /aʊ/ → /oː/; coda /ʔ/ dropped (lexically conditioned in grammaticalized particles; careful-speech variant /ˌbɛːˈsːoːʔ/ exists).

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

### beykw

#### Etymology
*vehicle* — broadened from private car to any motor vehicle.

**Part of speech:** n.  **IPA:** /ˈbɛjkw̩/  **Foot:** (ˈH) with syllabic /w̩/ tail.

Phonological development: /v/ → /b/ onset [Open: /v/→/b/ environment; see *béntsıìy*]; /iː/ → /ɛ/ [Open: /iː/→/ɛ/ not in §4.4.2; expected reflex of GA /iː/ is /iː/ or possibly /i/; short /ɛ/ outcome would require a new rule]; /ɪ/ → /j/ (glide formation in hiatus with preceding /ɛ/) → `y` [Open: /ɪ/→/j/ conditioned by hiatus; not the same environment as the /ɫ/→/j/ rule in §4.4.1]; /k/ cluster-internal stays [Open: see *barnkw*]; /l/ → /w̩/ (syllabic glide, E2c + final position) → `w`.

#### Definition

1. car; automobile.
2. any motor vehicle, including buses and trucks.

---

### bęiink

#### Etymology
*panic* — the verb, with semantic extension to worry and apprehension.

**Part of speech:** v.  **IPA:** /bɛ̃ˈink/  **Foot:** (L)(ˈH) [Open: whether the /ɛ̃/ syllable is light or heavy].

Phonological development: /p/ → /b/ (§4.4.1); /æ/ + following /n/ → /ɛ̃/ (/æ/-before-nasal pathway §4.4.2, short reflex) [Open: §4.4.2 predicts /ɛː/ long; short /ɛ̃/ here suggests the length component is blocked when /n/ stays as onset rather than eliding]; /n/ stays as onset of second syllable (E1 blocked — /n/ is onset of unstressed syllable adjacent to a stressed vowel, same blocking environment as *benıîæ* and *benskyi*); /ɪ/ → /i/ (tense short) [Open: /ɪ/→/i/ tense promotion not in §4.4.2]; /k/ in coda stays [Open: coda /k/→∅ expected per §4.4.1; retention unexplained].

#### Definition

1. to be scared; to be frightened.
2. to worry; to feel anxious about.
3. to deem unfortunate; to dread (a situation or outcome).

---

### boeś

#### Etymology
*voice* — the noun; semantic range matches GA closely.

**Part of speech:** n.  **IPA:** /boes/  **Foot:** (ˈH) heavy monosyllable (diphthong nucleus).

Phonological development: /v/ → /b/ onset [Open: /v/→/b/ environment; same flag as *béntsıìy*; contrast *reųś*, *rékwıì* where /v/ → /r/ — possible conditioning by following vowel quality]; /ɔɪ/ → /oe/ (diphthong; same pathway as *bœ* ← *boy*) [Open: orthographic note — established grapheme for /oe/ is the ligature `œ`; `boeś` written without ligature may represent hiatus /bo.ɛs/ rather than the diphthong /boes/ — user confirmation needed]; final /s/ → /s/ (devoiced, written `ś`: GA /s/ was voiceless; non-onset default is /z/, so devoicing mark required to preserve voicelessness).

#### Definition

1. voice (the acoustic signal produced by the vocal tract).

Cross-refs: *bœ* (same /ɔɪ/→/oe/ derivation from *boy*).

---

### bœ

#### Etymology
*boy* — the noun; no semantic shift.

**Part of speech:** n.  **IPA:** /boe/  **Foot:** (ˈH) heavy monosyllable (diphthong nucleus).

Phonological development: /b/→/b/; /ɔɪ/→/oe/ (diphthong → `œ`) [Open: /ɔɪ/→/oe/ not explicitly stated in §4.4.2, which lists /ai/→/eː/~/i/ but not /ɔɪ/; this is a likely new rule or sub-case needed]; no coda consonant.

#### Definition

1. boy; male child or young man.

Cross-refs: *boeś* (same /ɔɪ/→/oe/ derivation from *voice*).

---

### e

#### Etymology
*egg* — the food item; no semantic shift.

**Part of speech:** n.  **IPA:** /ɛ/  **Foot:** (ˈL) light monosyllable.

Phonological development: /ɛ/ → /ɛ/ (unchanged); coda /g/ → ∅ [Open: §4.4.1 specifies coda /k/→∅; coda /g/ (voiced counterpart) is not listed — analogous loss assumed; or /g/ elides via E1 if treated as being between a vowel and silence, but that environment is non-standard]. Pitch and stress coincide on the only vowel; casual orthography = bare `e`; formal = `ê`.

#### Definition

1. egg (especially a bird or chicken egg as food).

---

### emmáwwè

#### Etymology
*in what way* — the interrogative phrase, lexicalized as a single adverb.

**Part of speech:** adv. (interrogative).  **IPA:** /ɛmːˈɑwːɛ/  **Foot:** [Open].

Phonological development: [Open — the reduction of a three-word phrase /ɪn.wʌt.weɪ/ to a single phonological word involves several steps not individually attested: initial /ɪn/ + adjacent /w/ of *what* → /m/ (possible labial assimilation of /n/ before /w/) → /mː/ (gemination of boundary /m/); /wʌt/: /ʌ/→/ɑ/ (§4.4.2 /u,ʊ,ʌ/→/ɨ/ pathway; short /ɑ/ reflex), /t/→/ʔ/→drops; /weɪ/: /w/→/wː/ (gemination at boundary?) → /wː/ → `ww`; /eɪ/→/ɛ/ → `è`. Most steps are unattested; this entry records the headword as given with the full derivation flagged for a dedicated session.]

#### Definition

1. how; in what way; by what means.

---

### epplii

#### Etymology
*to apply* — with ambisyllabic /p/ in GA (/əp.ˈpɫaɪ/) phonologized as a true geminate.

**Part of speech:** v.  **IPA:** /ˈɛpːli/  **Foot:** [Open].

Phonological development: initial unstressed /ə/ → /ɛ/ [Open: new rule needed — see phonology §4.2]; /p.p/ ambisyllabic → geminate /pː/; /aɪ/ → short /i/ [Open: third reflex for §4.2's conditioning-open question].

Cross-refs: *beussou* (parallel geminate from ambisyllabic stop); *rhiiy* (morpheme entry for the `rhiiy-` prefix); *rhiiysseunnou*, *rhiiynii* (parallel `rhiiy-` prefix in alternative form *rhiiyepplii*).

#### Definition

1. to put, place, or spread something on something else (paint, ointment, a label).
2. to put effort into a task; to try with real effort. Sense 2 admits the alternative form *rhiiyepplii* (with the `rhiiy-` intensifier prefix, still transparent here — unlike its fully-bleached form in *rhiiysseunnou* and *rhiiynii*).
3. to apply for (a job, position, program).

---

### éuskrıì

#### Etymology
*icecream* — the compound noun; no semantic shift.

**Part of speech:** n.  **IPA:** /ɛːˈskɾi/  **Foot:** (H)(ˈL).

Phonological development: *ice* /aɪs/: /aɪ/ → /ɛː/ (§4.4.2 /ai/→/eː/ pathway) → `éu`; pitch stays on this syllable (GA primary stress on *ice*). At the *ice-cream* juncture, the /s/ of *ice* meets the /kr/ onset of *cream* → resulting cluster /skɾ/ [Open: onset /k/ normally debuccalizes to /h/; in the cluster /sk/, the /k/ is shielded — or /kr/→/r̥/ (§4.4.1) collapses the cluster differently; exact path unclear]. *cream* /kriːm/: /r/ → /ɾ/ (tap); /iː/ → /i/ short (secondary stress, final vocalic position in conlang) → `ıì` (dotless `ı` = first element of `ii` with following diacritic; grave `ì` = stress); /m/ in coda → ∅ [Open: coda /m/ treatment not in §4.4].

#### Definition

1. ice cream.

---

### ęy

#### Etymology
*any* — NPI determiner/pronoun "any whatsoever," GA /eni/. Inherited as a strict negative-polarity item, narrowed to the concord reinforcer of the volitive-negative marker *skwkw*.

**Part of speech:** aux. (VOL.NEG concord reinforcer; doubly restricted NPI).  **IPA:** /ẽj̃/  **Foot:** [Open].

Phonological development: intervocalic /n/ elides, leaving nasalization on the flanking vowels (E1, S1); smooths to a single nasalized /ej/ diphthong [Open: smoothing conditioned by function-word status — a lexical word such as *penny* would remain disyllabic; conditioning rule not yet in §4]. Glide nasalization predictable from the nasalized vowel; left unmarked (headword *ęy*, not *ęỹ*).

Cross-refs: *skwkw* (sole licensor); *rhiiy* (parallel reinforcer, in the *nocquıî* paradigm).

#### Definition

1. *(aux., VOL.NEG concord reinforcer)* emphatic floor-of-the-scale particle, sitting with the action or object quantified over; licensed only by *skwkw* within the LVC. Reinforces categorical refusal: "any instance whatsoever." — *I'm skwkw passing out ęy.* "I'm refusing to fall asleep at all."

#### Notes

Doubly restricted: licensed only in negative contexts (NPI behavior) and, within those, only by verbal *skwkw*. Does not survive the adverbial/substitutional uses of *skwkw* (*on my way to the bar skwkw ęy gym* is unnatural). The concord is paradigm-internal, not a property of *skwkw* wherever it appears.

In nested negation, *ęy* sits locally with the lexical verb (post-*skwkw*), while the outer marker's reinforcer (*rhiiy*, for *nocquıî*) sits clause-finally — the two reinforcers occupy different structural positions and do not compete. — *nocquıî go ahead and skwkw ęy V rhiiy.*

[Open: *ęy* may have other NPI distributions (questions, conditionals, comparatives) not yet described.]

---

### hohô

#### Etymology
*how so* — a rhetorical question reduced to a fixed interrogative particle. The GA rhetorical "how so?" (requesting explanation or justification) has lexicalized as a general why-question word.

**Part of speech:** interrogative particle.  **IPA:** /hoˈho/  **Foot:** (L)(ˈL).

Phonological development: *how* /haʊ/: onset /h/→/h/; /aʊ/→/o/ (§4.4.2); *so* /soʊ/: onset /s/→/h/ (debuccalization); /oʊ/→/o/; circumflex on final `ô` = pitch + stress coincide (GA stress and conlang final stress both on the second syllable). The internal `h` (written between the two `o` vowels) marks the boundary; if read as a hiatus-delimiter it is silent; if phonologically active it marks breathy voice on the adjacent vowel (see `orthography.md` §4).

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

Phonological development: onset /k/→/h/ twice (§4.4.1, both syllables); /oʊ/→/o/ (§4.4.2) for both /koʊ/ syllables; medial /ə/ → /o/ [Open: E3 predicts /ə/→∅, which would give cluster /hn/; the surface /o/ between the second /h/ and /n/ requires /ə/→/o/ rather than elision — same open rule as *nobêt* but without the /n/-conditioning; possibly a more general /ə/→/o/ rule in unstressed open-syllable position before a nasal]; /n/ stays (onset of the secondary-stressed syllable, same stress-onset blocking environment as *benıîæ* etc.); /ʌ/→/ɪ/ (§4.4.2); /t/ stays [Open: E2a predicts /t/→/ʔ/].

#### Definition

1. coconut (the fruit, and coconut as a flavor).

---

### hœ hoś

#### Etymology
*soy sauce* — the condiment; no semantic shift.

**Part of speech:** n. (two-word headword).  **IPA:** /hoe ˈhos/  **Foot:** (ˈH)(ˈH) [two phonological words].

Phonological development: *soy* /sɔɪ/: onset /s/→/h/ (debuccalization); /ɔɪ/→/oe/ (diphthong; same pathway as *bœ* ← *boy*) → `hœ`; *sauce* /sɔːs/: onset /s/→/h/ (debuccalization); /ɔː/→/o/ (§4.4.2 /au,or/→/o/); coda /s/: GA source was voiceless /s/ → non-onset default is /z/, so devoiced mark required → `ś`; circumflex on `ô`... actually the headword is `hoś` (no circumflex): the formal-register circumflex is absent in the casual form; stress falls on the second phonological word (`hoś`).

#### Definition

1. soy sauce.

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

### nocquıî

#### Etymology
*not quite* — adverbial phrase "approximately; falling short of," colloquial GA /nɑʔ kwaɪʔ/ (from /nɑt kwaɪt/ with coda glottalization). Lexicalized as a single unit before grammaticalizing as the non-volitive-negative marker. The approximative-from-below semantics is inherited and underlies both the high-scope frustrative reading and the low-scope attenuative reading. Also productive as a derivational element forming "a small lack" compounds (see Morphology).

**Part of speech:** aux. (LVC.NONVOL.NEG); also adv. (temporal proximative, substitutional apologetic); also deriv. prefix.  **IPA:** /noˈkʷːi/  **Foot:** [Open].

Phonological development: /ɑ/ → /o/ (raising-and-rounding, word-initially and after /n/) [Open: new rule, not in §4]; /aɪ/ → /i/; /ʔk/ → geminate /kʷː/ (coda glottal of *not* assimilates to and geminates the following /k/, which labializes from the /w/ of *quite*) [Open: /ʔk/-gemination rule not in §4]; final coda /ʔ/ (from *quite*'s /t/) drops [Open: coda /ʔ/ drop condition at compound junctions]; the final /i/ from /aɪ/ carries stress and pitch (circumflex in headword). Spelling: `cqu` for /kʷː/ dictionary-internal pending propagation to `orthography.md`.

Cross-refs: *skwkw* (paradigmatic opposite on the polarity axis, volitive side); *rhiiy* (concord reinforcer in the LVC, and the general negator); *ęy* (parallel reinforcer in the *skwkw* paradigm).

#### Definition

1. *(aux., LVC.NONVOL.NEG)* the non-volitive-negative cell of the light verb complex; marks falling-short, typically with a frustrative reading (a trajectory toward V, often involuntary, that fails to reach V, with the not-reaching foregrounded and often regretful). — *I do nocquıî get myself tuning them out.* "I couldn't manage to tune them out and ended up watching anyway."
2. *(low-scope attenuative)* under a volitive LVC, modifies the lexical verb: "only partway; only a little." — *I go ahead and nocquıî tune them out.* "I deliberately tune them out only a little bit."
3. *(adv., temporal proximative)* before; not yet at. — *on my way to the gym when it's nocquıî Thursday* "…before Thursday."
4. *(adv., substitutional apologetic)* rather than; instead of — softened, with an unintentional or mildly apologetic flavor (contrast the deliberate substitutional *skwkw* sense 2). — *on my way to the bar nocquıî the gym* "…the bar, rather than the gym."

#### Morphology

**Derivational prefix *nocquii-***, forming compounds that denote "a small lack" — a quantitative or qualitative falling-short of the base noun. Productive. The combining form is *nocquii-*; the junction behaves per the phonology:

- Before an obstruent, the dropped coda /ʔ/ geminates the following consonant. When the geminating consonant is /k/, gemination **bleeds debuccalization** (a geminate /kː/ does not debuccalize to /h/ the way a singleton onset /k/ does), yielding /h/ ~ /kː/ alternations between free and bound forms.
- Before a vowel or rhotic, a linker *-e-* appears.

[Open: combining-form rules inferred from attested compounds; ratify. Open: stress/pitch placement in compounds undetermined.]

#### Notes

Pairs with the reinforcer *rhiiy* (sense 1): an optional emphatic concord particle sitting clause-finally, licensed only by *nocquıî* within the LVC and not surviving the adverbial uses (senses 3–4). — *I'm not quite getting myself to pass out rhiiy.*

The frustrative reading (sense 1) is compositional — falling-short semantics + the non-volitive frame + the action's natural endpoint — not separately encoded.

Has both high scope (sense 1) and low scope (sense 2), in contrast to *skwkw* (high-scope only). The split follows from the degree-of-approximation core, which can target a whole event or the realization-level within an event.

[Open: glossing convention for nested negation. Open: distribution across the four non-volitive sub-modalities (PH, AB, INC, PS) — whether even, or favoring some; and whether AB admits *nocquıî* at all. For `verbal-system.md` §9.]

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

---

### nóeıìe

#### Etymology
*no idea* — GA /noʊ aɪˈdiə/, colloquial response particle reduced to a single phonological word.

**Part of speech:** interj.  **IPA:** /noɛˈiɛ/  **Foot:** [Open].

Phonological development: /n/→/n/; /oʊ/→/o/; /aɪ/→/ɛ/ [Open: /aɪ/→/ɛ/ short reflex — distinct from established /eː/ and /i/ pathways; conditioning unresolved]; /d/→/ɾ/ (tap merger, §4.4.1) → intervocalic → E1 elides; /ɪ/→/i/ [Open: tense promotion]; /ə/→/ɛ/ [Open: E5 normally gives /a/; /ɛ/ here possibly front-vowel assimilation].

#### Definition

1. *(interj.)* no idea; I don't know; beats me.

---

### nœ

#### Etymology
*annoy* — GA /əˈnɔɪ/.

**Part of speech:** v.  **IPA:** /noe/  **Foot:** (ˈH) [Open: diphthong weight].

Phonological development: initial /ə/→∅ (E3); /n/→/n/; /ɔɪ/→/oe/ [Open: /ɔɪ/→/oe/ pathway not in §4.4.2 — parallel to *bœ*, *boeś*].

Cross-refs: *bœ* (parallel /ɔɪ/→/oe/).

#### Definition

1. to annoy; to irritate; to bother.

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

### ouś

#### Etymology
*August* — GA /ˈɔːɡəst/, proper noun.

**Part of speech:** proper n.  **IPA:** /ˈoːs/  **Foot:** (ˈH).

Phonological development: /ɔː/→/oː/ (back long vowel; written `ou`); /ɡ/→/ɾ/ (tap merger, §4.4.1) → intervocalic → E1 elides; /ə/→∅ (E3); coda /st/→/ts/ (§4.4.1) → /t/→/ʔ/ (E2a) → drops [Open: /ʔ/-drop condition here]; /s/ in coda position → non-onset → /z/ → devoiced → `ś`.

#### Definition

1. August (the month).

---

### piiquóæ

#### Etymology
*peek over at* — GA /piːk ˈoʊvər æt/, periphrastic phrase lexicalized as a single verb.

**Part of speech:** v.  **IPA:** /piˈkʷoæ/  **Foot:** (L)(ˈH) [Open].

Phonological development: /p/→/p/ (blocked before /i/, §4.4.1 /p/→/b/ rule); /iː/→/i/ [Open: /iː/ shortening]; coda /k/ of *peek* labializes absorbing onset /w/ of *over* → /kʷ/ [Open: /k/ labialization mechanism]; /oʊ/→/o/; /v/→∅ or /ɾ/ → elides [Open]; /ər/→∅ (E3+E1); /æ/→/æ/ (residual, final).

#### Definition

1. to peek over at; to glance toward; to sneak a look at.

---

### piquô

#### Etymology
*pick out* — GA /pɪk ˈaʊt/, phrasal verb. *Out* particle grammaticalized with /ʔ/-drop (cf. *rhiiysseunnou*).

**Part of speech:** v.  **IPA:** /pɪˈkʷoː/  **Foot:** (L)(ˈH).

Phonological development: /p/→/p/ (blocked before /ɪ/); /ɪ/→/ɪ/; coda /k/ labializes absorbing *out*'s /aʊ/ → /kʷ/ [Open: same mechanism as *piiquóæ*]; /aʊ/→/oː/; coda /t/→/ʔ/ (E2a) → drops (grammaticalized *out* /ʔ/-drop, §4.4.3 E2d). Circumflex on `ô` = pitch+stress coincide.

Cross-refs: *rhiiysseunnou* (parallel grammaticalized *out* /ʔ/-drop).

#### Definition

1. to pick out; to select; to choose.

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

### récquıìs

#### Etymology
*likewise* — GA /ˈlaɪkˌwaɪz/.

**Part of speech:** adv.  **IPA:** /ˈɾɛkʷːis/  **Foot:** (ˈH)(L).

Phonological development: /l/→/ɻ/ [Open: /ɫ/→/ɻ/ candidate rule — dark-l vocalization; see pending phonology session]; /aɪ/→/ɛ/ [Open: /aɪ/→/ɛ/ short reflex]; coda /k/ + *wise* onset /w/ → geminate /kʷː/ [Open: labialization and gemination mechanism]; /aɪ/ of *wise* → /ɪ/ [Open]; coda /z/→devoiced /s/.

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

### rékriiyæ

#### Etymology
*yakitty-yak* — GA /ˈjækɪtiˌjæk/, expressive reduplication for idle chatter.

**Part of speech:** v.  **IPA:** /ɾɛkˈɾiːæ/  **Foot:** (H)(ˈH).

Phonological development: first /j/→/ɻ/ (§4.4.1) → R-Assim → /ɾ/ (second /j/ also present); /æ/→/ɛ/ [Open: /æ/→/ɛ/ without preceding nasal — distinct from established nasal pathway]; /k/ retained in cluster; /ɪ/→∅ (E3); /t/→/ɾ/ (tap merger); second /j/→/ɻ/→R-Assim→/ɾ/; /iː/ from smoothing [Open: trigger path]; final /æ/→/æ/ retained.

#### Definition

1. to talk incessantly and idly; to chatter; to ramble; to go on and on.

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

### reųś

#### Etymology
*Venus* — GA /ˈviːnəs/, proper noun.

**Part of speech:** proper n.  **IPA:** /ˈɾɛ̃ːs/  **Foot:** (ˈH).

Phonological development: /v/→/ɾ/ [Open: /v/ before front vowel /iː/ → tap merger; see /v/ conditioning]; /iː/→/ɛː/ [Open: /iː/→/ɛː/ pathway not in §4.4.2]; /n/→∅ (E1) + S1 nasalizes adjacent vowel → /ɛ̃ː/ (written `eų`); /ə/→∅ (E4); coda /s/→/z/ (non-onset) → devoiced → `ś`.

#### Definition

1. Venus (the planet).

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

### ritsstw

#### Etymology
*Rochester* — toponym.

**Part of speech:** proper n.  **IPA:** /ˈritsstw̩/  **Foot:** (ˈH) with sesquisyllabic /w̩/ tail.

Phonological development: /tʃ/ → /ts/; /st/ → /ts/ (or retained as /ts/-cluster); E3 schwa elision; /ɻ/ → syllabic /w̩/ in final position.

Cross-refs: *toutw* (parallel sesquisyllabic /w̩/).

#### Definition

1. Rochester (the city).

#### Notes

Used in `phonology.md` §6.1 as a worked example of heavy onset-and-coda clustering with a final syllabic /w̩/. The double /ts/ at the cluster boundary (from /tʃ/ + /st/) is phonotactically legal; cited there as a test case for sequences like `tsst`.

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

### rhiiy

A polyfunctional morpheme from GA *really*, spanning intensifier prefix → bleached lexical prefix → non-volitive-negative reinforcer → general negator. The bound-prefix uses appear inside *rhiiynii*, *rhiiysseunnou*, and *rhiiyepplii* (under *epplii* sense 2); the free-word uses (reinforcer, general negator) are described here. Consolidated as a single lemma (same form /ɻiː/, same primary source).

**Part of speech:** aux. (general negation); also aux. (NONVOL.NEG concord reinforcer); also deriv./intensifier prefix `rhiiy-`.  **IPA:** /ɻiː/  **Foot:** [Open].

Phonological development: GA /ˈɹɪl.i/ → /ɻiː/: dark velarized /ɫ/, sandwiched between front vowels, becomes /j/ (§4.4.1) and then elides, leaving a lengthened /iː/; onset /ɹ/ → /ɻ/ (§4.4.1). (Same derivation as the `rhiiy-` prefix attested in *rhiiynii*, *rhiiysseunnou*, *rhiiyepplii* — this entry consolidates that morpheme.)

Cross-refs: *nocquıî* (host for the reinforcer reading, sense 2); *skwkw* (volitive-domain negator — complementary distribution by domain); *ęy* (parallel reinforcer, in the *skwkw* paradigm); *rhiiynii*, *rhiiysseunnou*, *epplii* (contain the bound-prefix uses, senses 3–4).

#### Definition

1. *(aux., general negation)* "no"; "not so." Volition-neutral propositional negation, used outside the LVC: phrasal denial, short answers, negation of non-verbal predicates. — *Rhiiy.* "No." / "Not so."
   - Etymology: *not really* (colloquial GA general negator), grammaticalized via a Jespersen-cycle pathway — the *not* erodes, leaving bare *really* to carry negative force on its own.
2. *(aux., NONVOL.NEG concord reinforcer)* clause-final emphatic concord with *nocquıî* in the LVC; emphasizes the predicate's full realization, the standard the action falls short of. — *I'm not quite getting myself to pass out rhiiy.*
   - Etymology: GA intensifier *really* "to a real degree."
3. *(intensifier prefix `rhiiy-`)* still-transparent intensifier on a verb stem. — attested in *rhiiyepplii* "to apply oneself with real effort" (under *epplii* sense 2).
   - Etymology: GA intensifier *really*.
4. *(bleached lexical prefix `rhiiy-`)* fully bleached, no longer felt as an intensifier; part of a lexicalized stem. — attested in *rhiiynii* "to need/want" and *rhiiysseunnou* "to be different/excellent."
   - Etymology: GA *really*, bleached.

#### Notes

Senses 1 and 2 are **the same morpheme, contextually disambiguated**, not homophones: inside the LVC with *nocquıî* upstream → reinforcer reading (sense 2); outside the LVC, or without *nocquıî* → negator reading (sense 1). The two play off a shared "realness" core — the reinforcer asserts the predicate's realness as the standard fallen short of; the negator denies the predicate's realness outright.

Senses 3–4 are the bound-prefix uses, which show grammaticalization stratification across the lexicon: transparent in *rhiiyepplii* (sense 3), fully bleached in *rhiiynii* and *rhiiysseunnou* (sense 4).

Does not enter the LVC as a polarity marker (only as the sense-2 reinforcer); verbal negation is handled by the dedicated volition-aware markers *skwkw* and *nocquıî*. Fills the standalone declarative-negation gap: *skwkw* standalone is prohibitive, *nocquıî* has no standalone use, so *rhiiy* is the language's assertional "no."

[Open: whether negator-*rhiiy* itself attracts a new reinforcer over time (a Jespersen spiral). Deferred — long-horizon.]

---

### rhilþ

#### Etymology
*wolf* — inherited directly; no semantic shift.

**Part of speech:** n.  **IPA:** /ˈɻɪlθ/  **Foot:** [Open: depends on whether coda consonants contribute weight].

Phonological development: /w/ → /ɻ/ (§4.4.1 /w, j/ → /ɻ/); /ʊ/ → /ɪ/ (§4.4.2 back-vowel fronting); /f/ → /θ/ (§4.4.1); coda /l/ preserved in cluster /lθ/ (E2c targets singleton /l/; cluster environment exempt).

#### Definition

1. wolf (the animal).

---

### rhiiynii

#### Etymology
*really need* — *really* bleached and lexicalized as the `rhiiy-` prefix; stem from *need*. The need/want polysemy collapses two GA concepts onto a single axis.

**Part of speech:** v.  **IPA:** /ɻiːni/  **Foot:** [Open].

Phonological development: /ɫ/ → /j/ between high front vowels; /ɪji/ → /iː/; coda /d/ → ∅ (E2, no compensatory lengthening).

Cross-refs: *rhiiy* (morpheme entry for the `rhiiy-` prefix); *rhiiysseunnou* (parallel `rhiiy-` prefix, fully bleached); *epplii* (intensifier variant *rhiiyepplii*, where `rhiiy-` is still transparent).

#### Definition

1. to need.
2. to want.

#### Notes

The prefix /ɻiː-/ (`rhiiy`) surfaces as long /iː/ from /ɪji/-smoothing; the stem /ni/ (`nii`) is short /i/ from coda /d/-deletion with no compensatory lengthening. The /iː/ vs. /i/ contrast within the same word is the orthographic working rule: `iiy` = long /iː/ (etymologically-justified glide source), `ii` = short tense /i/ [Open: to be confirmed when `orthography.md` §3.2 is revised to admit /iː/].

---

### rhiiysseunnou

#### Etymology
*really stand out* — *really* bleached and lexicalized as the `rhiiy-` prefix; *stand out* also lexicalized as a phrasal verb in GA. Treated as a single verb in the conlang.

**Part of speech:** v.  **IPA:** /ɻiːsːɛːnːoː/  **Foot:** [Open].

Phonological development: /æ/-tense (pre-nasal in GA, with preserved duration) → /ɛː/ via length reanalysis; /ɫ/ → /j/ between high front vowels; /ɪji/ → /iː/; /st/ → /sː/ at stressed-syllable boundary; /nd/ → /nː/ in coda [Open: new rule needed — see phonology §4]; /aʊ/ → /oː/; /t/ → /ʔ/ in coda; coda /ʔ/ dropped (lexically conditioned in grammaticalized *out*).

Cross-refs: *beussou* (parallel /st/ → /sː/, parallel coda /ʔ/-drop in *out*-particle); *rhiiy* (morpheme entry for the `rhiiy-` prefix); *rhiiynii*, *epplii* (parallel `rhiiy-` prefix).

#### Definition

1. to be different; to stand apart; to be distinctive.
2. to be excellent; to excel.

#### Notes

The `rhiiy-` prefix is fully bleached here and in *rhiiynii* — not felt as an intensifier, only as part of the lexicalized stem. Contrast *rhiiyepplii* (under *epplii* sense 2), where the same prefix is still transparent. This stratification (bleached vs. transparent) across the lexicon reflects grammaticalization at different stages.

The `eu` digraph unifies two diachronic sources: (1) the smoothed-schwa pathway for /ɛː/ in `orthography.md` §3.2, and (2) the /æ/-with-preserved-duration pathway attested here. Both surface as `eu`.

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

### ŕe

#### Etymology
*today* — from colloquial GA [tʰɾeɪ] (reduced from [tʰəˈdeɪ] via schwa elision and tap-realization). Sense 2 grammaticalizes the GA emphatic use ("done today" = "right now") as a distinct interjectional sense.

**Part of speech:** (1) adv., (2) interj.  **IPA:** /ˈr̥ɛ/  **Foot:** (ˈL) light monosyllable.

Phonological development: /h/ + tap coalescence → /r̥/ (M1 devoicing mechanism generalized to onset, without metathesis); two irregular shifts specific to this high-frequency colloquial form: /t/ → /h/ in onset cluster (not a regular rule); /eɪ/ → short /ɛ/ (clipping, not a regular rule).

Cross-refs: *ŕeut* (parallel /r̥/ onset, from M1 metathesis rather than coalescence).

#### Definition

1. *(adv.)* today. — *Ŕeus bémmo oų rĩbii·hii. Oų riis·hii o noê.* "It's a little more chillier today, in a pleasant kind of way."
2. *(interj.)* hurry!; right now!; immediately!

#### Notes

The two irregular shifts — /t/ → /h/ and /eɪ/ → short /ɛ/ — are one-offs licensed by this form's high frequency and rapid-speech origin, not regular rules. The convergence of irregularities in one form is the design point: high-frequency colloquial words bleed off the regular cascade, and *ŕe* is the canonical example.

---

### ŕeut

#### Etymology
*carrot*.

**Part of speech:** n.  **IPA:** /ˈr̥eːʔ/  **Foot:** (ˈH) heavy monosyllable.

Phonological development: onset /k/ → /h/; coda /t/ → /ʔ/; M1 (rhotic metathesis: intervocalic /ɻ/ → onset, /h/ reanalyzed as devoicing feature → /r̥/); smoothing of /æ + ə/ → /eː/.

Cross-refs: *ŕe* (parallel /r̥/ onset, from /h/ + tap coalescence rather than M1 metathesis).

#### Definition

1. carrot (the root vegetable).

#### Notes

The canonical illustration of M1: GA onset /k/ debuccalizes to /h/, which becomes the devoicing feature on the metathesizing rhotic. Used as a worked example in `phonology.md` §6.1.

---

### skwkw

#### Etymology
*skip* — GA /skɪp/, "decline; pass over." Lexicalized as the volitive-negative marker. The deliberate-declination semantics is inherited and sharpened to active counter-volition (going out of one's way to not-do, not merely the absence of volition).

**Part of speech:** aux. (LVC.VOL.NEG); also adv./substitutional; also interj. (prohibitive).  **IPA:** /skʷkʷ/ (first /kʷ/ syllabic).  **Foot:** [omitted].

Phonological development: irregular, peculiar to this high-frequency form. Coda /p/ delabializes — but only after labializing the /k/ (the labial feature transfers from /p/ to /k/ before /p/ is lost). The vowel /ɪ/, squeezed between two /kʷ/ sequences, elides entirely, leaving a vowelless /skʷkʷ/ with the first /kʷ/ as syllable nucleus. [Open: irregular; not a proposed regular rule.]

Cross-refs: *nocquıî* (paradigmatic opposite on the polarity axis, non-volitive side); *rhiiy* (general negator, complementary domain — outside the LVC); *ęy* (concord reinforcer, licensed only by this marker).

#### Definition

1. *(aux., LVC.VOL.NEG)* the volitive-negative cell of the light verb complex; marks deliberate refusal or active counter-volition. High-scope only. — *I'm skwkw passing out ęy.* "I'm deliberately refusing to fall asleep (not even a little)."
2. *(adv./substitutional)* in place of, instead of, declining the alternative; deliberate, with a mutual-exclusivity flavor. — *on my way to the bar skwkw the gym* "…the bar, deliberately not the gym."
3. *(interj., prohibitive)* "Don't!"; "Pass on it!" — standalone negative imperative. — *Skwkw!* "Don't!"

#### Notes

A showcase for vowelless syllabification: /skʷkʷ/ has no vocalic nucleus, the first /kʷ/ serving as the syllable's nucleus. Novel for the lexicon — other consonant-heavy forms (*hoʔnʔnts*, *ritsstw*, *toutw*) retain at least one full vowel. [Open: foot structure and the metrical status of a syllabic obstruent.]

Pairs with the reinforcer *ęy* (sense 1 only): optional emphatic floor-of-the-scale particle, licensed only by *skwkw* within the LVC, not surviving the adverbial/substitutional uses (sense 2). See *ęy*.

Does not stack with GO-AHEAD: *going ahead and skwkw V* collapses to the *skwkw* reading since both fill the single volition slot.

Layers with the non-volitive-positive marker (GET-ONESELF) productively but narrowly: *getting myself to skwkw V* = "finding myself in the position of having to deliberately refuse V." Felicitous only in forced-choice contexts.

[Open: glossing convention for nested negation — when *skwkw* appears under *nocquıî* or vice versa.]

---

### spyi

#### Etymology
*spew* — GA /spjuː/. Highly specific semantic narrowing to the surprise-spit context.

**Part of speech:** v.  **IPA:** /spjɪ/  **Foot:** (ˈH) [Open: cluster onset weight].

Phonological development: /s/ in cluster /sp/ retained (not debuccalized) [Open: §4.4.1 debuccalization of /s/ blocked in /sp/ cluster? Rule not in §4]; /p/→/p/; /j/ retained in cluster; /uː/→/ɨː/→/ɪ/ [Open: /uː/→/ɪ/ via /ɨ/ unrounding then shortening].

#### Definition

1. to spew liquid; specifically: to involuntarily spit out a drink due to surprise or laughter. Most naturally collocates with coffee.

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

**Part of speech:** v.  **IPA:** /ˈtoːtw̩/  **Foot:** (ˈH) with sesquisyllabic /w̩/ tail.

Phonological development: /oʊ/ → /oː/; intervocalic tap /ɾ/ elided (E1); coda /ɫ/ → ∅ [Open: not explicitly stated in phonology §4 — see §3.2]; smoothing of /oː + ə/ → /oː/; final unstressed /u/ → syllabic /w̩/ (phonology §5.2 step 7).

Cross-refs: *ritsstw* (parallel sesquisyllabic /w̩/).

#### Definition

1. to cost a certain amount (of money).
2. to be present in a certain number; to amount to; to add up to.

#### Notes

Initial /t/ is aspirated [tʰ] in stressed onset — allophonic, not marked orthographically. [Open: aspiration's phonemic status not committed in `phonology.md`.]

---

## 5. Changelog

A running record of additions and changes to the dictionary, with dates and any open questions surfaced.

### 2026-05-24

Batch addition: 36 new entries from `drafts/batch-dict-entry-0523.xlsx` (51 source rows; some consolidated or deferred). Entries span the b-, e-, h-, n-, o-, p-, r-, rh-, s-, and t-regions. All entries with unresolved phonological steps carry inline `[Open]` flags; none resolve any existing `[Open]` items without an explicit decision.

**Open questions surfaced (propagate to phonology session):**
- /v/ conditioning: /v/ → /b/ before back vowels vs. /v/ → /ɾ/ (tap merger) before front vowels — candidate rule, not yet committed.
- /ɫ/→/ɻ/ candidate rule: all /l/-initial GA words → /r/-initial headwords, suggesting dark-l vocalization path to /ɻ/ → R-Assim → /ɾ/.
- /ɪ/→/ɛ/ after onset: appears in *benskyi*, *béntsıìy*, *rékwıì* — rule not in §4.
- /ə/→/o/ after /n/: flagged in *noê* — rule not in §4.
- /aɪ/→/ɛ/ short reflex: third candidate pathway alongside established /eː/ and /i/ reflexes.
- /aɪ/→/i/ short reflex: fourth candidate; appears in *récquıìs*, *rıírǫ*, *rhiwıĩ*.
- /ɔɪ/→/oe/: parallel to established bœ/boeś pathway; now attested in *nœ* as well.
- /ɜːr/→/ɨː/ vocalization: needed for *rhiušp*; not in §4.4.2.
- Coda /t/ retention vs. E2a: *pot*, *rérèyt* show unexpected /t/ retention.
- /k/ labialization: coda /k/ absorbing adjacent /w/ → /kʷ/; needed for *piiquóæ*, *piquô*, *récquıìs*.
- /s/ in /sp/ cluster: debuccalization blocked? Needed for *spyi*.

**New entries (collation order):** *barnkw*, *bárkennò*, *bawiiquoh?*, *bayarę*, *bąêų*, *benıîæ*, *benskyi*, *beńt*, *béo·ò*, *bessts*, *béuksoè*, *beušiioskô*, *beusp*, *beųtw*, *bewii·iit*, *bewiipessô*, *beykw*, *bęiink*, *boeś*, *bœ*, *e*, *emmáwwè*, *éuskrıì*, *hohô*, *hóhonìt*, *hœ hoś*, *noê*, *nóeıìe*, *nœ*, *ohô*, *óhò*, *ouś*, *piiquóæ*, *piquô*, *pot*, *récquıìs*, *réıì*, *rékriiyæ*, *rékwıì*, *rérèyt*, *reųś*, *rıírǫ*, *rhéulyèś*, *rhiušp*, *rhiwıĩ*, *spyi*, *toś*.

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