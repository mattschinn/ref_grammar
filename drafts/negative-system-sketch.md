# Negative System — Working Sketch

A first-pass description of the conlang's negative morphology, developed in a sketch session before being incorporated into `verbal-system.md` §9. This document is provisional and intended for eventual integration; terminology and analysis here are not yet canon.

The sketch covers three negators (SKIP, NOT.QUITE, REALLY), their reinforcers (ANY, REALLY), the composition rules that govern how they interact with the volitive/non-volitive LVC and with each other, the diachronic story behind each, and a section on what entries each marker needs in the dictionary.

---

## 1. The Three Negators

The conlang has three distinct negative elements, distributed across two domains.

| Marker | Source | Domain | Function | Standalone? |
|---|---|---|---|---|
| **SKIP** | GA *pass on* | Volitive LVC | VOL.NEG — deliberate refusal | Yes — prohibitive ("Skip!" = "Don't!") |
| **NOT.QUITE** | GA *not quite* | Non-volitive LVC | NONVOL.NEG — falling short | No |
| **REALLY** | GA *not really* (Jespersen) | General phrasal | Generic negation, volition-neutral | Yes — declarative ("Really" = "No") |

The division of labor is principled: **volition-aware negation lives inside the LVC; volition-neutral negation lives outside it.** The LVC has dedicated negative slots (SKIP for the volitive side, NOT.QUITE for the non-volitive); REALLY handles everything else — nouns, adjectives, copular predicates, short answers, and any phrasal context where volition isn't a category of the predicate being negated.

This division is closed: REALLY does not appear inside the LVC. The temptation to admit a weakened-volitional construction (something like "passively not doing" intermediate between SKIP's active counter-volition and a non-volitive frame) was considered and rejected. The system already covers that semantic territory through layered composition (see §3.2 below), and admitting a third volitional-negative would erode the force of the volitive/non-volitive binary by giving SKIP a weaker comparand.

---

## 2. The Markers in Detail

### 2.1 SKIP (VOL.NEG)

**Core meaning:** deliberate passing-over, active refusal. SKIP is not merely "deliberately not V-ing" — it's "going out of one's way to not-V," with implicit counter-volition: I have considered V-ing and have actively declined it, possibly in favor of the opposite action.

**Slot:** the volitive-negative cell of the LVC. SKIP is paradigmatically opposed to GO-AHEAD (VOL.POS); the two cannot stack productively. *I'm going ahead and skipping V* is grammatical but the GO-AHEAD adds nothing semantically (mild rhetorical emphasis at most); SKIP wins because it's the marked, polarity-bearing element.

**Scope:** always high. SKIP is inherently an LVC-level operator; it has no low-scope (lexical-verb-modifying) use. Constructions like *go ahead and SKIP V* do not yield a "deliberately do the opposite of V" reading distinct from SKIP-as-VOL.NEG; the only reading available is the high-scope refusal one. This contrasts with NOT.QUITE (see §2.2).

**Reinforcer:** **ANY**, an emphatic floor-of-the-scale concord item. ANY licenses only under SKIP-in-the-LVC; it does not survive the non-verbal uses of SKIP (*I'm on my way to the bar SKIP ANY gym* is unnatural). ANY is therefore a strict NPI doubly restricted — to negative contexts in general and to verbal-SKIP specifically. Its emphatic contribution is "any instance whatsoever," which reinforces SKIP's categorical-refusal semantics: a refusal that admits no exceptions or partial instances.

**Standalone use:** *Skip!* survives as a prohibitive imperative ("Don't!"). This is the only LVC-internal negator that has standalone life; it fits the active-counter-volitional semantics (you can command someone to refuse, but you can't easily command them to fall short).

**Phrase-level uses (no reinforcer):** SKIP also survives in substitutional contexts: *I'm on my way to the bar SKIP the gym* ("the bar, instead of the gym") with a deliberate, mutually-exclusive flavor. This is the same passing-over semantics applied to nominal alternatives rather than predications.

### 2.2 NOT.QUITE (NONVOL.NEG)

**Core meaning:** falling short, approximation-from-below. NOT.QUITE describes a trajectory toward V that does not reach V, with the trajectory's incompleteness foregrounded. In the non-volitive LVC, this typically yields a **frustrative reading**: the subject was on a course toward V (often involuntarily), didn't reach V, and the experience of not-reaching is what's foregrounded, often with regret or disappointment.

**Slot:** the non-volitive-negative cell of the LVC, paradigmatically opposed to GET-ONESELF (NONVOL.POS).

**Scope:** has both high and low uses, in contrast to SKIP.
- **High scope (LVC-level):** the canonical NONVOL.NEG reading — *I don't NOT.QUITE get myself V-ing* (frustrative).
- **Low scope (lexical-verb-level):** an attenuative on the action itself — *I go ahead and NOT.QUITE V-ing* = "I deliberately V only partway." Here NOT.QUITE is a degree operator on the lexical verb's realization, not a polarity marker on the predication.

The high/low scope split is principled: NOT.QUITE's core meaning is degree-of-approximation, which can apply to either a whole event (did it almost happen?) or to the realization-level within an event (was it carried partway through?). SKIP doesn't have this flexibility because "deliberate refusal" doesn't have a degree-modifier reading.

**Reinforcer:** **REALLY**, an emphatic concord item appearing clause-finally. REALLY licenses only under NOT.QUITE-in-the-LVC; it does not survive non-verbal uses. Its emphatic contribution is "to a real/full degree," which reinforces the falling-short semantics by underscoring what was fallen-short-of: the predicate's full realization. *I'm not quite getting myself to pass out REALLY* = "I'm falling short of really/fully passing out."

REALLY's contribution to the frustrative flavor is emphatic, not constitutive. The frustrative reading comes compositionally from NOT.QUITE + non-volitive frame + the action's natural endpoint (with telicity sharpening the effect — see §6, Open Questions). REALLY underscores the failure-to-reach but does not produce it.

**Standalone use:** blocked. This fits the semantics — one cannot felicitously command or assert incompleteness in isolation.

**Phrase-level uses (no reinforcer):** NOT.QUITE survives in two adverbial contexts:
- **Temporal approximative:** *NOT.QUITE Thursday* = "before Thursday, not quite there yet."
- **Substitutional apologetic:** *I'm on my way to the bar NOT.QUITE the gym* = "the bar, rather than the gym," with a softened, slightly regretful or unintentional flavor — contrast with SKIP's more deliberate substitutional.

### 2.3 REALLY (general negation)

**Core meaning:** generic propositional negation, volition-neutral. The conlang's "no."

**Source:** Jespersen-cycle grammaticalization of GA *not really*. The conlang inherits *not really* as a colloquial general negator; phonological erosion drops the *not*, leaving *really* to carry the negative force on its own. This parallels French *personne* (originally "a person," now negative on its own through loss of the obligatory *ne*).

**Slot:** outside the LVC. REALLY does not compete with SKIP or NOT.QUITE for verbal-negation duty; it covers everything else — adjectives, nouns, copular predicates, short answers, phrasal denials.

**Standalone use:** *Really* = "No." This is the form that fills the standalone-declarative-negation gap left by SKIP-as-prohibitive (a command, not an assertion) and NOT.QUITE-as-no-standalone.

**Relationship with NOT.QUITE's reinforcer-REALLY:** the negator-REALLY and the reinforcer-REALLY are **the same morpheme, contextually disambiguated.** The two readings play off each other rather than being treated as homophones:

- Inside the LVC with NOT.QUITE upstream → reinforcer reading ("to a real degree").
- Outside the LVC, or without NOT.QUITE → negator reading ("no, not so").

This unification is supported by the shared semantic core (both uses pivot on "realness"): the reinforcer asserts the predicate's realness as the standard the action falls short of; the negator denies the predicate's realness outright. Speakers parse on the environmental cue: LVC + NOT.QUITE selects the reinforcer reading; everything else selects the negator reading.

---

## 3. Composition

### 3.1 Same-slot competitors collapse

When two markers compete for the same LVC slot — i.e., GO-AHEAD with SKIP, or GET-ONESELF with NOT.QUITE *as straight co-markers* — the marked (polarity-bearing) element wins and the other adds nothing compositional. The construction is grammatical but the unmarked element is rhetorical reinforcement only, not contributing a second feature value.

```
I'm going ahead and skipping ANY passing out.
≈ I'm skipping ANY passing out.        (GO-AHEAD adds emphasis only)
```

This generalizes: a single slot can host one feature value at a time.

### 3.2 Different-slot markers layer

When markers from *different* slots co-occur, they compose productively, with the outer marker embedding the inner one as its complement.

**GET-ONESELF + SKIP** = "find oneself in the position of having to deliberately refuse":

```
I go ahead and sip coffee everyday but
I'm getting myself to skip sipping it today. Too much on the busy side.
```

Structure: `[ GET-ONESELF [ SKIP [ sip ] ] ]`. The refusal (SKIP) is deliberate; the arriving-at-the-refusal (GET-ONESELF) is not. The construction is **productive but pragmatically narrow**: it requires a forced-choice context where the subject's circumstances impose a refusal they wouldn't otherwise make. Without that frame, the construction is grammatical but inert.

**GO-AHEAD + NOT.QUITE** = "deliberately fall short of":

```
I go ahead and NOT.QUITE tune them out.
"I intentionally watch the trailers only a little bit."
```

This is the low-scope NOT.QUITE under high GO-AHEAD — the attenuative use of NOT.QUITE described in §2.2.

**General principle:** layered combinations are fully productive grammatically; their use is constrained by pragmatics rather than by morphology. The system supports these compositions whenever the discourse situation supplies the right frame.

### 3.3 Nested negation: stacking inside the LVC

The system supports stacked negation — NOT.QUITE over SKIP or vice versa — with reinforcers occupying different structural positions:

```
NOT.QUITE go ahead and SKIP ANY V REALLY
"I don't quite go out of my way to refuse to V."
```

The linear order encodes scope:
- **ANY** sits with the action/object it quantifies over (post-SKIP, local to the lexical verb).
- **REALLY** sits clause-finally, concording with the outer LVC's NOT.QUITE.

This positional asymmetry follows from the reinforcers' semantic types: REALLY modifies the degree-realization of the whole predicate and so attaches at the predicate's edge; ANY quantifies over the action/object and so attaches with what it quantifies. They don't compete because they're doing different syntactic-semantic work.

The reading of nested negation tends toward modal-attitudinal nuance — lukewarm compliance, partial counter-volition, mild obligation — rather than pure logical doubled-negation. The older description of nested negation in `verb-terminology.md` framed this as "cannot fail to" → "must," which is one specific reading but not the only one; the full range needs more data.

**Glossing convention for nested negation remains open** — `verb-terminology.md` §2.5 flagged this and the question is unresolved. Candidates: stacked LVC tags (`LVC.NONVOL.NEG=LVC.VOL.NEG`) vs. a dedicated obligation gloss (`OBLIG`) once the construction's productivity is better characterized. Defer until more nested-negation data is collected.

---

## 4. Diachronic Story

Each negator has a two-channel grammaticalization history:

**High channel** → into the LVC, where the marker became a polarity slot-filler and recruited a dedicated reinforcer.

**Low channel** → into adverbial / prepositional / standalone uses, which preserved the core meaning but lost the reinforcer apparatus.

| Marker | High channel | Low channel |
|---|---|---|
| SKIP | VOL.NEG slot, recruits ANY | Substitutional ("X SKIP Y"), prohibitive ("Skip!") |
| NOT.QUITE | NONVOL.NEG slot, recruits REALLY | Temporal proximative, substitutional apologetic |
| REALLY | (does not enter LVC) | General negator, standalone "no" |

The reinforcer apparatus is what marks the high-channel uses as the *grammaticalized verbal-system* negatives, distinct from the surviving adverbial cousins. This is a useful diagnostic: if a negator-marked phrase admits its reinforcer, it's the verbal-system use; if it doesn't, it's the phrase-level survival.

REALLY's diachronic profile is different because it didn't grammaticalize *into* the LVC — it grammaticalized as a general-clause negator via Jespersen erosion of *not really*. Its source phrase already lived outside the verbal-system, so the high/low channel distinction doesn't apply to it. The reinforcer-use and negator-use of REALLY are two synchronic readings of one morpheme, not two grammaticalization channels.

---

## 5. Dictionary Implications

Each negative marker needs its own dictionary entry. The entries should follow `dictionary.md`'s standard schema, but the Definition and Notes sections will carry more grammatical weight than for typical lexical entries because these are grammaticalized morphemes with paradigmatic distribution.

### 5.1 SKIP — entry contents

- **GA etymology:** *pass on* (phrasal verb, "decline, decline an offer of"). The particle *on* is preserved in the grammaticalized form, and the whole phrase has been lexicalized as a single morpheme before entering the LVC paradigm.
- **Part of speech:** grammatical marker (VOL.NEG of LVC); also adverbial/substitutional; also prohibitive interjection.
- **IPA / Foot / Sound changes:** to be derived. Pre-conlang GA *pass on* /ˌpæs ˈɑn/ → conlang form. Likely sound changes include the /æ/ → /ɛː/ raising-before-nasal pattern (cf. *rhiiysseunnou*), and the /s/ → /sː/ or /h/ pattern depending on stress boundary. Worth a careful derivation when the entry is written, because SKIP is high-frequency and its surface form will anchor speakers' intuitions about the negative system.
- **Cross-refs:** NOT.QUITE (paradigmatic opposite on the polarity axis); GO-AHEAD (paradigmatic opposite on the polarity axis within the volitive side); ANY (obligatory-optional reinforcer); REALLY (general negator that occupies a different domain).
- **Definition:**
  1. *(LVC.VOL.NEG)* the volitive-negative cell of the light verb complex. Marks deliberate refusal or active counter-volition. *(High-scope only; not a lexical-verb modifier.)*
  2. *(adv./substitutional)* in place of, instead of, declining the alternative. *On my way to the bar SKIP the gym.*
  3. *(interj., imperative)* "Don't!" — prohibitive standalone.
- **Notes:** record the ANY-concord behavior; record that the *.ON* particle is part of the inherited form (not a separate morpheme in the conlang); record the GET-ONESELF + SKIP layered composition with its pragmatic narrowness; flag the no-low-scope finding.

### 5.2 NOT.QUITE — entry contents

- **GA etymology:** *not quite* (adverbial phrase, "approximately, falling short of"). Like *pass on*, lexicalized as a single morpheme before grammaticalization.
- **Part of speech:** grammatical marker (NONVOL.NEG of LVC); also adverbial (temporal proximative, substitutional apologetic); also low-scope attenuative under volitive frames.
- **IPA / Foot / Sound changes:** to be derived. Pre-conlang GA *not quite* /nɑt kwaɪt/ → conlang form. The /t/ → /ʔ/ pattern, /aɪ/ outcomes (the open question from `phonology.md` §4.2 — /iː/ vs. /eː/ vs. /i/), and stress-driven elision will all bear on the output. The morpheme may end up with internal complexity if both *not* and *quite* contribute surviving material; alternatively one may bleach phonologically.
- **Cross-refs:** SKIP (paradigmatic opposite on the polarity axis); GET-ONESELF (paradigmatic opposite within the non-volitive side); REALLY (obligatory-optional reinforcer; also the general negator, same morpheme).
- **Definition:**
  1. *(LVC.NONVOL.NEG)* the non-volitive-negative cell of the light verb complex. Marks falling-short, typically with frustrative flavor (trajectory toward V did not reach V, often with regret).
  2. *(low-scope attenuative)* under a volitive LVC, modifies the lexical verb to mean "only partway, only a little bit." *I go ahead and NOT.QUITE V.*
  3. *(adv., temporal proximative)* before, not yet at. *NOT.QUITE Thursday* = "before Thursday."
  4. *(adv., substitutional apologetic)* rather than, instead of, with softened or unintentional flavor. *On my way to the bar NOT.QUITE the gym.*
- **Notes:** record the REALLY-concord behavior (clause-final position); record the frustrative reading as compositional rather than encoded (NOT.QUITE + non-volitive frame + telic endpoint); record the high/low scope distinction and contrast with SKIP's high-scope-only profile; flag the telicity-frustrative interaction as a deferred test.

### 5.3 REALLY — entry contents

- **GA etymology:** colloquial GA *not really* (general negator, "no, not so"), Jespersen-cycle eroded to bare *really*. Compare French *personne*.
- **Part of speech:** general phrasal negator; also concord reinforcer for NOT.QUITE inside the LVC; also a free intensifier in non-negative contexts (likely a third reading inherited from the *really* meaning "to a real degree," which is the etymological source of the reinforcer use).
- **IPA / Foot / Sound changes:** to be derived. Pre-conlang GA *really* /ˈɹɪli/ → conlang form. Watch for the /ɪ/ outcomes (the carried-forward question from `phonology.md` §5) and the medial /l/ — the appendix-and-syllabic-/l/ behavior may produce an interesting derivation.
- **Cross-refs:** NOT.QUITE (host for the reinforcer reading); SKIP (volitive-domain negator; complementary distribution by domain); ANY (parallel reinforcer in the SKIP-paradigm).
- **Definition:**
  1. *(general negation)* "no," "not so." Used outside the LVC for phrasal denial, short answers, and predicate negation in non-verbal contexts.
  2. *(NONVOL.NEG concord reinforcer)* clause-final emphatic concord with NOT.QUITE in the LVC. Underscores the falling-short by emphasizing the predicate's full realization. *I'm not quite getting myself to pass out REALLY.*
  3. *(intensifier, possibly)* "to a real degree" — the inherited GA intensifier use, if it survives independent of the reinforcer reading.
- **Notes:** record the same-morpheme analysis (negator and reinforcer disambiguated by environment); record that REALLY does not appear inside the LVC as a polarity marker (only as a reinforcer); record the diachronic story (Jespersen erosion of *not really*); flag the question of whether the bare-intensifier reading survives or has been absorbed into the negator and reinforcer readings.

### 5.4 ANY — entry contents

- **GA etymology:** *any* (NPI determiner / pronoun, "any whatsoever"). Inherited as a strict NPI restricted to the SKIP-paradigm.
- **Part of speech:** concord particle / NPI, distributionally restricted.
- **Cross-refs:** SKIP (sole licensor); REALLY (parallel reinforcer in the NOT.QUITE paradigm).
- **Definition:**
  1. *(VOL.NEG concord reinforcer)* emphatic floor-of-the-scale particle, sitting with the action or object quantified over, licensed only by SKIP in the LVC. *I'm skipping ANY passing out.*
- **Notes:** record the double restriction (negative contexts in general + verbal-SKIP specifically); record that ANY does not survive non-verbal SKIP uses; flag that ANY may have other NPI distributions in the broader grammar (e.g., questions, conditionals) that are not yet described.

---

## 6. Open Questions

Carried forward for the eventual `verbal-system.md` §9 write-up and the dictionary entries above.

1. **Frustrative-from-telicity.** Predicted: the frustrative reading of NOT.QUITE is sharper with telic predicates (clear endpoint to fall short of) than with atelic ones. Worth testing with a handful of contrastive verb pairs.

2. **Glossing convention for nested negation.** From `verb-terminology.md` §2.5, still open. Candidates: stacked LVC tags vs. dedicated `OBLIG` gloss. Defer until more nested-negation data is collected and the reading range is better characterized (it's broader than just "must").

3. **ANY's broader NPI distribution.** The sketch establishes ANY as restricted to verbal-SKIP, but the language may have other NPI-licensing contexts (questions, conditionals, comparatives) where ANY appears. Out of scope for this sketch; needs its own analysis.

4. **REALLY's bare-intensifier reading.** The Jespersen story posits *not really* → *really*-as-negator, but the inherited GA *really*-as-intensifier reading should also be checked for survival. Does the conlang have a bare *really* meaning "to a real degree" outside the NOT.QUITE-reinforcer context? Bears on whether the dictionary entry needs two readings or three.

5. **Reconciliation with the cell × sub-modality structure.** The sketch above treats polarity as a single binary on each LVC cell, but `verbal-system.md`'s four-sub-modality structure on the non-volitive side (PH, AB, INC, PS) may interact non-trivially with NOT.QUITE-marking. Does NOT.QUITE distribute evenly across all four sub-modalities, or do some sub-modalities favor it? Does AB (auto-benefactive) admit NOT.QUITE at all, given its agentive-leaning semantics? These are the questions §9 will need to address head-on.

6. **Jespersen spiral.** Deferred long-horizon: does negator-REALLY pick up its own reinforcer over time, restarting the cycle?

---

## 7. Status and Integration Path

This sketch is **provisional** and was developed in a single conversational session. The terminology adopted here (SKIP / NOT.QUITE / REALLY / ANY as marker names; high/low scope; reinforcer; concord) is working terminology and may shift when the sketch is folded into `verbal-system.md` §9.

**Integration plan when ready:**
- Move the substantive content of §§1–4 into `verbal-system.md` §9, harmonizing terminology with the rest of that document.
- Use §5 to populate dictionary entries for SKIP, NOT.QUITE, REALLY, and ANY when the lexicographic work reaches them. The sound-change derivations are flagged for careful treatment because these are high-frequency morphemes.
- Carry §6 forward as the polarity-reconciliation open-questions list, merging with the corresponding items already in `language_reference.md` §7 and `verb-terminology.md` §2.5.
- Retire this file once §9 and the dictionary entries are in place.

---

## Changelog

- **May 19, 2026.** Sketch created in a focused session on the negative system. Established the three-negator picture (SKIP, NOT.QUITE, REALLY), the reinforcer system (ANY, REALLY-as-reinforcer), the composition rules (same-slot collapse, different-slot layering, nested stacking), and the diachronic story (high/low channels for SKIP and NOT.QUITE; Jespersen for REALLY). Identified key decisions: REALLY stays outside the LVC (rejected weakened-volitional construction); REALLY-negator and REALLY-reinforcer are one morpheme contextually disambiguated; SKIP is high-scope only while NOT.QUITE is high-and-low. Deferred items: telicity-frustrative test, nested negation glossing convention, ANY's broader NPI distribution, REALLY's bare-intensifier survival, sub-modality interactions, Jespersen spiral.
