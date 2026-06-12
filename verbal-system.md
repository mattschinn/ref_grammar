# The Verbal System

**Version:** v2.1 (June 2026)
**Status:** Sibling reference document, parallel to `phonology.md` and `orthography.md`. The language reference's §3.4 is a high-level summary that points here. Supersession history: §16.

**Abstract.** The verbal system grammaticalizes the subject's relationship to the event: every framed verb commits to either the volitional go-ahead frame (the subject deliberately undertook the event) or the non-volitional get-oneself frame (the subject's relationship to the event is qualified in some other way). The go-ahead side is deliberately compact; the get-oneself side is richer, hosting four readings — happenstance, effortful self-benefit, threshold, and backdrop — selected jointly by frame aspect, concord shape, and the verb's own event structure. The frames do not stand alone: they combine with a pronominal system in which pronouns are aspect carriers, while the language's only tense lives in a small class of matrix particles that scaffold whole clauses with modal meaning. A possession construction derives having, getting, choosing, and giving from frame-plus-nominal combination, with the recognitional-iterative nominal as its deverbal special case; three stative-domain strategies carry the meanings the morphology cannot host. This document is the canonical reference for all of these systems; the verb-lexicon-building methodology lives in its Appendix A.

This document describes the verbal system as it currently stands. Where a question is open, it is flagged; the document does not commit to interpretations the data has not yet supported.

Status tags — **[Settled]** committed; **[Provisional]** current best analysis, expected to hold; **[Open]** explicitly undecided — and the reading conventions for examples and glosses are explained in `language_reference.md`, "How to read this document set." Terminology follows `terminology-registry.md`.

---

## 1. Overview

The verbal system grammaticalizes the subject's relationship to the event. Every framed verb commits to one of two sides:

- The **volitional go-ahead** (shorthand: *go-ahead*) — the subject deliberately undertook the event. From GA *go ahead and-*.
- The **non-volitional get-oneself** (shorthand: *get-oneself*) — the subject's relationship to the event is qualified in some way other than straightforward agency. From GA *get oneself-*.

The contrast cuts the action space differently from GA. The attested verb *beussou* (< GA *pass out*) shows it at full power: in the go-ahead frame it means going to bed — a deliberate act — while in the get-oneself frame, on its happenstance reading, it means falling asleep — something that befell the subject. GA needs two different expressions for these; the conlang needs one verb and a choice of frame.

The two sides are asymmetric, and the asymmetry is principled rather than accidental. Deliberateness is a single semantic value, so the go-ahead side does one thing and has a compact paradigm: three frame aspect cells, one concord shape. Non-straightforward agency fans out into several distinct values, so the get-oneself side has a richer paradigm — four frame aspect cells crossed with two concord shapes, hosting four **readings**: **happenstance** (it simply befell the subject), **effortful self-benefit** (the subject brought it about on their own behalf, with effort), **threshold** (the subject is on the approach to a tipping point), and **backdrop** (the activity is the ongoing scene against which something else happens). A useful way to hold the whole system: the go-ahead is the unmarked default — "the subject just did it" — and the get-oneself paradigm carries everything else the language wants to say about how an event and its subject relate.

Three further resources extend the system beyond the paradigm proper. When the meaning to be expressed is a state rather than an event, speakers reach for one of three **stative-domain strategies** (§6). The frames combine directly with nominals in the **possession construction** (§12), which covers having, getting, choosing, and giving; its deverbal special case is the **recognitional-iterative nominal** (§7), marking shared-knowledge type reference and iteration. And above the clause sits a small class of **matrix particles** (§11) — the only tense-bearing elements in the language — which scaffold the clause with modal meaning: that it merely ended up so, that the speaker knows it, needs it, or that it appears so.

> *Analytical note.* The paradigm-side names, the reading names, and their full naming history (including the retired terms *volitive*, *involitive*, *modulated*, *non-volitive*, and the abbreviations PH/AB/INC/PS) are maintained in `terminology-registry.md`. Prose here uses the registry's canonical terms; interlinear glosses use its compact gloss tags.

---

## 2. The volitional go-ahead frame

The go-ahead frame presents the subject as deliberately undertaking the event. Its paradigm is compact:

- Three frame aspect cells: habitual, progressive, past.
- A single main-verb concord shape.
- No perfect cell (structurally absent — §2.2).

### 2.1 Origin: the source frame

The go-ahead frame grammaticalized from the GA *go ahead and-* construction: *I went ahead and V-ed* underlies the past cell, *I'm going ahead and V-ing* the progressive, *I go ahead and V* the habitual. The periphrasis has phonologically fused into the frame forms in §2.4; for the frame as a morphological object, see §4.

### 2.2 The perfect gap

The go-ahead paradigm has no perfect cell. This is a principled absence, not a gap waiting to be filled: the source construction has launching-frame semantics — it points at the moment of undertaking the action — and these clash with the perfect's result-relevance semantics, which orient the action toward its consequences. Any morphologically fused form would also be phonetically clunky. The combination is structurally blocked. **[Settled]**

### 2.3 Verb classes

The go-ahead frame is incompatible with stative verbs: *go ahead and rhiiynii* ("be in a state of needing") is ungrammatical across all three cells. States are reached through the restricted get-oneself paradigm (§3.6) or through the stative-domain strategies (§6). **[Settled]**

The frame is fully productive with activity, accomplishment, and achievement verbs. Achievements may carry a marked flavor depending on how plausibly the achievement can be construed as deliberate — *find* in the go-ahead frame asserts a deliberate finding, as in a search. This is verb-by-verb pragmatics, not a structural restriction.

### 2.4 GO-AHEAD paradigm forms

The GO-AHEAD frame agrees for animacy at the habitual cell only; all other cells are invariant across persons and numbers.

| Frame aspect | Animacy restriction | GA source | Conlang form |
|---|---|---|---|
| Habitual | Animate (all persons/numbers) | *go ahead and* | *oheun* |
| Habitual | Inanimate (3SG.INANIM only) | *goes ahead and* | *osoheun* |
| Imperfect/progressive | — | *(I'm) going ahead and* | *ounoheun* |
| Past | — | *went ahead and* | *beųheun* |

**[Open: animate habitual form — the table's *oheun* parallels *osoheun* exactly (the *goes* sibilant infixed), but a 2026-06-10 correction note reads *ouhen*; confirm one spelling before the next paradigm sweep]**

The habitual cell covers both habitual and timeless/general statements. The imperfect form *ounoheun* is the bare gerund shape of the frame; in this construction the pronoun carries the +be fusion (§5.2). The past cell is the preterite *went ahead and*, not a grammatical perfect (which is structurally absent — §2.2).

---

## 3. The non-volitional get-oneself frame

The get-oneself side carries the system's expressive richness. Its paradigm:

- Four frame aspect cells: habitual, progressive, past, perfect.
- Two main-verb concord shapes: infinitive-shaped and progressive-shaped.
- Two of the eight resulting cells are structurally blocked (§3.4), leaving six productive cells.
- Each productive cell hosts one of the four readings.

### 3.1 Origin: the source frame

The get-oneself frame grammaticalized from the GA *get oneself-* construction: *I got myself V-ing* and *I got myself to V* underlie the two past cells (with progressive-shaped and infinitive-shaped concord respectively); *I had myself V-ing* underlies the perfect; and so on. The fused source produces the GET-ONESELF frame forms in §3.7.

### 3.2 The cell × reading grid

| Frame aspect | + infinitive-shaped concord | + progressive-shaped concord |
|---|---|---|
| **HABITUAL** | self-benefit (marked) | happenstance (default) |
| **PROGRESSIVE** | threshold (default) | *(blocked: vacuous redundancy)* |
| **PAST** | self-benefit | happenstance |
| **PERFECT** | *(blocked: result-state requires stative target)* | backdrop |

### 3.3 The four readings

The four readings are working labels; whether they form a unified semantic class — and if so, what the unifying property is — is **[Open]** and translation data are expected to inform it (§9.1). Gloss tags in parentheses.

- **Happenstance** (HAP). The subject finds themselves doing the verb without agency or effort — the event simply befell them. The default reading of the get-oneself frame, hosted by HABITUAL + progressive-shaped and PAST + progressive-shaped concord.
- **Effortful self-benefit** (SELF.BEN). The subject brought the event about on their own behalf, with effort. The reflexive *myself* in the source phrase retains its dative-of-interest force, so the reading carries effortful and evaluative coloring: it took work, and it served the subject. Hosted by HABITUAL + infinitive-shaped concord (marked) and PAST + infinitive-shaped concord.
- **Threshold** (THRESH). The subject is in the process of becoming such that the verb will happen — on the approach to a tipping point. The progressive frame supplies the becoming; the infinitive-shaped concord keeps the verb prospective. Hosted by PROGRESSIVE + infinitive-shaped concord.
- **Backdrop** (BACK). The verb's ongoing activity is the discourse-relevant scene — the *I-was-V-ing-when-X* framing, with experiential or narrative coloring. Hosted by PERFECT + progressive-shaped concord.

### 3.4 The two blocked cells

**Perfect + infinitive-shaped concord (e.g., *had myself to V*) is blocked.** The perfect's result-state semantics requires a stative-shaped target; the *to-V* infinitive is too prospective to combine. A clean grammatical gap. **[Settled]**

**Progressive + progressive-shaped concord (e.g., *getting myself V-ing*) is blocked.** The get-oneself frame already supplies a durative envelope; progressive concord on the main verb adds nothing. The form is vacuously redundant rather than ungrammatical, but it is consistently rejected in well-formedness judgments. **[Settled]**

### 3.5 Soft preferences within productive cells

- HABITUAL defaults to progressive-shaped concord (happenstance); the infinitive-shaped variant is available but marked, carrying the self-benefit reading.
- PAST permits both shapes productively; the choice is semantically loaded (self-benefit on infinitive-shaped, happenstance on progressive-shaped), not stylistic.

### 3.6 Readings and verb class

The readings interact with lexical aspect. Stative verbs access happenstance, threshold, and backdrop within the get-oneself paradigm but are blocked from the self-benefit reading, since it requires an action the subject can undertake on their own behalf. The restriction follows directly from what the readings denote. **[Settled]**

How the self-benefit reading selects on counter-benefactive verbs (*catch a cold*, *fall*), whether the threshold reading extends to states or is restricted to action-hosts, and whether HABITUAL + infinitive-shaped concord consistently carries self-benefit or sometimes a weaker effortful flavor, are live questions documented in `verb-paradigm-verdict.md` §1.5. **[Open]**

### 3.7 GET-ONESELF paradigm forms

The GET-ONESELF frame agrees for full person and number across all cells. Three frame aspect cells are attested; the fourth (perfect, from GA *had myself V-ing*) is a candidate pending confirmation.

| Person | Habitual | Imperfect/progressive | Past |
|---|---|---|---|
| 1SG | *remase* | *remmase* | *rimase* |
| 2SG | *rešise* | *renyose* | *rišise* |
| 3SG.ANIM | *retmśe* | *retmmśe* | *ritmśe* |
| 3SG.INANIM | *reutse* | *retnntse* | *riutse* |
| 1PL | *reaśeus* | *retnaśeus* | *riaśeus* |
| 2PL | *rešiseus* | *renyoseus* | *rišiseus* |
| 3PL.ANIM | *retmśeus* | *retmmśeus* | *ritmśeus* |

GA sources: habitual from *get [oneself]-*, imperfect/progressive from *getting [oneself]-*, past from *got [oneself]-*. The morphology is discussed further in §5.2, alongside the pronominal paradigm with which GET-ONESELF combines. Inanimate 3SG (the *reutse* series) is restricted to inanimate subjects. Animate 3SG and 3PL share a GA source (*get/got themselves*) and are distinguished by the *-eus* plural suffix. **[Settled]**

---

## 4. The frame and main-verb concord

### 4.1 The frame

The grammaticalized unit that carries volition, frame aspect, and (defective) person/number agreement is the **frame** — the go-ahead frame and the get-oneself frame of §2–3. The frame metaphor captures its function: the same lexical event gets *placed in* an attitudinal context. In morphology-internal discussion the frame is called the **light verb complex (LVC)**, and composite gloss tags use `LVC` (e.g., `LVC.VOL.HAB`).

The frame is not a bleached helper. It carries the bulk of the grammatical work and is the heart of the predicate. It is also the locus of the polarity dimension (§10) and of stacking phenomena like nested negation.

Open questions about the frame's grammar:

- **Morphological status** — clitic, affix, separate word, compound element. The term is neutral on this; orthography and syntax decisions will force the question. **[Open]**
- **Agreement features** — what exactly is agreed with: subject, event, both? "Defective person/number agreement" — agreement that is real but does not distinguish every person/number combination — is the working description; the locus needs analysis. **[Open]**
- **Argument structure** — can the frame take nominal complements directly, or always mediated by a preposition? See §12 (The possession construction) for the *with*-mediation facts. **[Open]**

### 4.2 Concord

The main verb carries the lexical content and takes a **concord affix** — an ending showing concordance with the frame. Two shapes exist: **infinitive-shaped** and **progressive-shaped**. In the get-oneself paradigm the choice of shape selects the reading (§3.2); this is the most semantically loaded work concord does in the system.

The surface forms of the concord endings have not yet been tabulated; the progressive-shaped concord is exemplified by the *-in* of placeholder forms like *relaxin*, but a committed inventory is pending. **[Open: concord-affix surface inventory — what features does concord actually mark beyond the shape contrast (volition, frame aspect, person/number redundantly with the frame)?]**

> *Analytical note.* The term *concord affix* commits only to the agreement function — the most stable of the three effects originally observed (agreement with the frame, interaction with the verb's event structure, pragmatic-salience effects). If the latter two prove to do independent grammatical work, the term may be revisited; candidate replacements and the noncommittal fallback *stem extensions* are held in `terminology-registry.md`.

A third shape is attested: the **passive-shaped concord**, patterned on the GA passive participle.

> *Rimmase spli·oþw.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> 1SG.LVC.NVOL.PST split-CONCORD
> "I drifted off / I got split off (from the group)."

The passive shape fills a gap the other two cannot: it delivers a completed event under the get-oneself frame without the threshold coloring of the infinitive shape and without the imperfect aspect of the progressive shape. The same stem across all three shapes:

- *Rimmase spli·oþw* — passive-shaped: completed, happenstance. The natural rendering of "I drifted off."
- *Rimmase splitnoþw* — progressive-shaped: imperfect; wrong aspect for a completed departure.
- *Rimmaseto splitoþw* — infinitive-shaped: right aspect, but threshold-colored — the splitting off took effort.

> *Analytical note.* In the discovery example the passive shape is conflated with the separative satellite *oþw* (§12 Interactions; `terminology-registry.md`), because GA *split* has a zero-marked participle — all the visible material belongs to the satellite. Disambiguating the shape from the satellite needs a verb with overt participle morphology (a *got myself taken-* class form). **[Open: passive-shaped concord — confirm with an overt-participle stem]**

**Readings are compositional.** Translation data show that the reading a clause receives is not a property of a paradigm cell alone: it is the joint product of **frame aspect × concord shape × the stem's own event structure**, with the matrix particles (§11) available as a further scaffolding layer when the bare frame under-delivers. Three regularities recur:

1. The threshold reading tracks **prospectivity**, surfacing wherever the infinitive shape meets an effortful stem — including past cells (*Rimmaseto splitoþw* above).
2. Beginning-readings ("first noticing," onsets) are intrinsically **imperfect**: available only where the frame aspect supplies ongoing time, never from a perfective cell.
3. Stems whose GA source is lexically volitional resist the happenstance reading bare, and take the get-oneself frame only with scaffolding — a satellite supplying a befall-able event shape, or a matrix particle supplying the happenstance from above (*Enniip remmaseto split* "I ended up leaving").

This is direct evidence on the concord term's standing question: the stem's event structure does grammatical work alongside the shape contrast. The term remains **[Provisional]** on exactly this point. **[Open: concord-affix surface inventory — unchanged; the compositional findings sharpen what the inventory must capture]**

#### 4.2.1 Irregular concord

A small set of verbs preserves GA irregular (strong-verb) morphology in the concord slot where the regular derivation predicts the *-t(t)-* infix: *meirtt* (from GA *made it*) where regular *meiktt* plus the infix is expected. Same stem, unexpected exponent — inherited irregularity, not suppletion (`terminology-registry.md`). `[Lexicon: meiktt / concord meirtt not yet entered]` **[Open: irregular-concord inventory — collect members as the dictionary grows]**

#### 4.2.2 Concord under suffixation

Concord and incorporated material interact morphophonologically: the *-t(t)-* infix surfaces inside particle-incorporating stems (*pikborrô* ~ *piknib·orrô* across frames), and coda material can resurface intervocalically under vowel-initial concord (*bemmorret* ~ *bemmorreųt*). The alternations are attested but not yet standardized. **[Open: concord-suffixation morphophonology]** `[New rule needed: coda-rhotic resurfacing under vowel-initial suffixation]`

### 4.3 Worked example

> *e oheun relaxin* — `[Placeholder: main-verb surface form pending dictionary derivation]`
>
> 1SG    go.ahead.LVC.VOL.HAB    relax-CONCORD
> "I deliberately relax (as a habit)"

The frame *oheun* carries the volition and the frame aspect (habitual); the main verb carries the progressive-shaped concord. The pronoun and frame forms are attested (§2.4, §5.2); the main verb is a placeholder. For fuller assembled clauses, see §14 (A clause, assembled).

---

## 5. The Pronominal System

The conlang's pronominal system is not a list of stand-alone word-forms. Pronouns are **aspect carriers** — they fuse with aspect, modal, and polarity markers to form the grammatically complex units that clause structure depends on. A clause does not have a subject pronoun and a separate aspect marker; it has a pronominal-aspect complex that does both jobs in one phonological unit.

The practical consequence: the frame paradigms in §2 and §3 do not stand alone. They combine with pronouns, and the combination is what appears in speech. This section describes the combinatorial system.

### 5.1 Overview and asymmetry

GO-AHEAD and GET-ONESELF pattern differently with respect to what they agree with:

- **GO-AHEAD** (go-ahead frame) agrees for **animacy only**, and only at the habitual cell (§2.4). All other cells are invariant; the pronoun supplies person/number.
- **GET-ONESELF** (get-oneself frame) agrees for **full person and number** across all cells (§3.7). Both the pronominal and frame forms are person-anchored, doubly anchoring the predicate to its subject.

This asymmetry follows from the GA sources: *go ahead and-* did not encode person/number robustly, while *get oneself-* contains the reflexive, which is person-anchored by definition.

### 5.2 Weak (clitic) pronouns

Weak pronouns are the default subject expression. They are phonologically reduced and carry the grammatical fusions: aspect, prospective/conditional, ability modal, and negation. **A noun subject cannot carry these fusions directly**; it requires a resumptive weak pronoun (§5.4). The full paradigm CSV is at `paradigms/pronoun-weak.csv`.

**Bare (habitual):**

| Person | Animate | Inanimate |
|---|---|---|
| 1SG | *e* | — |
| 2SG | *rhi* | — |
| 3SG | *ey* | *e* |
| 1PL | *rhii* | — |
| 2PL | *rhiau* | — |
| 3PL | *eiau* | — |

1SG *e* is syncretic with inanimate 3SG *e* in the bare series — the same 1SG/3SG.INANIM syncretism the prospective and ability series already show (*ew*, *ekw*). The 1SG form is irregular for its GA source (weak pronouns are always unstressed). **[Settled]**

**Imperfect/progressive (+be fusion):**

| Person | Animate | Inanimate |
|---|---|---|
| 1SG | *em* | — |
| 2SG | *rhia* | — |
| 3SG | *eiia* | *eś* |
| 1PL | *rhiia* | — |
| 2PL | *rhiauæ* | — |
| 3PL | *eiiauæ* | — |

In the imperfect construction, the pronoun takes the +be fusion and the frame appears in its bare gerund shape (*ounoheun* for GO-AHEAD; the person-marked GET-ONESELF form for the get-oneself frame).

**Prospective/conditional (would):**

| Person | Animate | Inanimate |
|---|---|---|
| 1SG | *ew* | — |
| 2SG | *rhiw* | — |
| 3SG | *eyt* | *ew* |
| 1PL | *rhiit* | — |
| 2PL | *rhiw* | syncretic 2SG |
| 3PL | *eyt* | syncretic 3SG.ANIM |

**Ability modal (could):**

| Person | Animate | Inanimate |
|---|---|---|
| 1SG | *ekw* | — |
| 2SG | *rhikw* | — |
| 3SG | *eykw* | *ekw* |
| 1PL | *rhiikw* | — |
| 2PL | *rhikw* | syncretic 2SG |
| 3PL | *eykw* | syncretic 3SG.ANIM |

The modal fusions (would, could) are **restricted to pronouns** — they cannot be expressed analytically on the frame directly. Modal constructions therefore require a pronominal subject; there is no nominal-subject modal construction without a resumptive pronoun.

#### 5.2.1 Negation — the not-quite fusions

The negative fusions grammaticalize GA *don't/doesn't quite* (negative habitual) and *didn't quite* (negative perfective). The conlang forms fuse the pronoun, the *do/did* auxiliary, and the not-quite particle (*nocquıî*).

**Negative habitual:**

| Person | Animate | Inanimate |
|---|---|---|
| 1SG | *eonquii* | — |
| 2SG | *rhionquii* | — |
| 3SG | *eonquii* | *reusnquii* |
| 1PL | *rhiionquii* | — |
| 2PL | *rhionquii* | syncretic 2SG |
| 3PL | *eonquii* | syncretic 3SG.ANIM |

**Negative perfective:**

| Person | Animate | Inanimate |
|---|---|---|
| 1SG | *reunnquii* | — |
| 2SG | *riennquii* | — |
| 3SG | *reunnquii* | *reunnquii* |
| 1PL | *rhiiennquii* | — |
| 2PL | *riennquii* | syncretic 2SG |
| 3PL | *reunnquii* | syncretic 3SG.ANIM |

The *do/did* within the fusion carries aspect: *do* = habitual, *did* = perfective. 1SG, 3SG.ANIM, and 3PL share the same negative habitual form (*eonquii*) and the same negative perfective form (*reunnquii*). 3SG.INANIM has its own negative habitual (*reusnquii*) but merges with animate forms in the negative perfective. The negative fusions interact with the polarity dimension — see §10.

#### 5.2.2 Defectiveness and syncretism

The weak paradigm is **defective** at several modal cells: 2PL and 3PL are syncretic with their singular counterparts for the prospective/conditional, ability, and both negative fusions. Distinct forms are preserved only at the bare and imperfect cells.

> *Analytical note.* The modal syncretism is historically motivated: the modal fusions derive from high-frequency colloquial GA sources that leveled person/number agreement early, while the bare and imperfect forms, from more transparently person-anchored sources (*you're* vs. *I'm*), preserved the distinctions longer. **[Provisional]**

### 5.3 Strong (tonic) pronouns

Strong pronouns are the emphatic counterpart to the weak clitic paradigm. They derive from GA *on [POSS] end* and carry three functional readings. The full paradigm is at `paradigms/pronoun-strong.csv`.

| Person | GA source | Conlang form |
|---|---|---|
| 1SG | *on my end* | *bayen* |
| 2SG | *on your end* | *yoen* |
| 3SG.ANIM | *on their end* (sg) | *þeren* |
| 3SG.INANIM | *on its end* | *nitsen* |
| 1PL | *on our end* | *nauen* |
| 2PL | *on y'all's end* | *yoen* — syncretic 2SG |
| 3PL | *on their end* (pl) | *þeren* — syncretic 3SG.ANIM |

The GA source phrase had three pragmatic uses that survive as the strong pronoun's three readings:

1. **Emphatic** — contrastive or focus emphasis on the subject. *bayen* = it's *me*.
2. **Possessive** — free-standing possessive. *bayen* = mine.
3. **Topic/frame** — discourse topic-frame. *bayen* = as far as I'm concerned; on my part.

The three readings are not homonymy: context selects the reading. Strong pronouns do not carry aspect fusions; they set a discourse frame that the clause's weak pronoun and frame fill in. 2PL and 3PL are syncretic with their singular counterparts, the plural reading supplied by context or an overt plural NP. **[Provisional — GA source for 2PL is variable (*y'all's end* vs. *your all's end*); confirm]**

A fourth use is **antitopic tagging**: a strong pronoun tags a topic postposed after the clause (right dislocation — §5.4), and the same strong-pronoun phrases serve as boundary markers between layers in stacked matrix-particle constructions (§11). **[Provisional]**

### 5.4 Left dislocation and resumptive pronouns

Full NPs **cannot** directly take the aspect, modal, or negation fusions that weak pronouns carry. When a full NP is the discourse subject, the construction uses **left dislocation with a resumptive weak pronoun** — the NP sits outside the clause as a topic, and a weak pronoun inside the clause refers back to it and carries the fusion:

> *the coffee — e oheun drinkin* — `[Placeholder: NP and main-verb surface forms pending]`
>
> coffee.TOP    1SG    go.ahead.LVC.VOL.HAB    drink-CONCORD
> "the coffee — I go ahead and drink (it)"

The NP topic is the discourse locus for reference; the resumptive pronoun is the grammatical locus for the fusion. This is the core mechanism by which full nominals access the pronominal-aspect system.

A consequence for clause architecture: the pronominal paradigm is not peripheral marking — it is structural. Argument NPs are expressed through dislocation, not through NP-agreement on the verb. **[Settled]**

Whether the weak pronoun can be omitted when its referent is inferrable is **[Open]** — see §5.6.

**Right dislocation.** A topic can also be postposed after the clause, with definite coloring retained — but the two peripheries are asymmetrically marked. A left-dislocated topic carries a visibility particle; a right-dislocated topic strips it and is tagged instead with the strong-pronoun *on-X-end* phrase (§5.3). The visibility contrast is a left-periphery-only phenomenon. **[Provisional — wants worked conlang examples]** `[Placeholder: right-dislocation example pending — GA pattern: "they went ahead and split, Mark, on their end"]` The full information-structure description is the language reference's responsibility (`language_reference.md`, nominal and discourse sections).

### 5.5 Interrogative: intonation and *ea* **[Provisional]**

Interrogative constructions use the **same pronominal form as the indicative**, distinguished by intonation. **There is no do-inversion.**

Yes/no questions add the particle *ea* (from GA *at all*) at the end of the clause:

> *e oheun... ea?*
> 1SG go.ahead.LVC.VOL.HAB ... Q
> "Am I going ahead and...?"

*Ea* marks the proposition as presented for binary verification — *is it the case at all that X?* The "at all" source semantics are preserved: genuine yes/no verification, not rhetorical or presupposing framing.

*Ea* also marks **conditionals** — "if … at all" — placing a clause under hypothetical rather than interrogative verification. `[Placeholder: conditional example pending]` It applies to matrix-scaffolded clauses as to any other (§11). **[Provisional]**

Content questions (who, what, where, when, why) are formed differently and are not yet systematized. **[Open]**

### 5.6 Pro-drop **[Open]**

Whether the weak pronoun can be dropped when the subject is referentially recoverable from context is an explicit open question. The conditions for pro-drop — if available at all — require systematic judgment data. Relevant literature on GA-derived or contact-variety pro-drop has been flagged for consultation.

### 5.7 Irrealis **[Open]**

A WERE-based irrealis particle is hypothesized on the basis of GA *if I were, as if I were, I wish I were* sources. The form has fused past the point of transparent pronominal structure and is treated as an **analytical irrealis particle** — it operates above the pronominal layer rather than fusing with the weak pronoun paradigm. Its form, distribution, and aspect-interaction are not yet committed.

---

## 6. Stative-domain strategies

When the meaning to be expressed is a state — feelings, attitudes, internal conditions — the go-ahead frame is unavailable, and the get-oneself frame is available only in restricted form (§3.6). Speakers reach for one of three constructional strategies. They are described here as a unified set of resources, without yet committing to whether they are part of the same broader system as the morphological paradigm (§9.2).

All examples in this section are GA-calque placeholders; conlang surface forms await lexicon derivation. `[Placeholder: all §6 example sentences]`

### 6.1 Activity-coercion

A lexical strategy. The speaker selects an activity verb that correlates with the desired stative meaning, then frames the activity verb.

> *they are going ahead and smiling for the photo* — used where GA might say *they are happy*.

The strategy reconstructs the stative meaning from the activity's typical correlate. The result is biased toward externalized, observable predicates: the conlang ends up describing displayed happiness rather than internal happiness. **This is a productive feature of the language, not a limitation.**

Activity-coercion requires no new grammatical machinery; it is a lexicon-level choice the frames happen to facilitate.

### 6.2 Stimulus-promotion

A constructional strategy. The argument structure is rearranged so that the stimulus becomes the grammatical subject and the experiencer becomes the object; the go-ahead frame is then applied to the stimulus.

> *Emma, they going ahead and charming me* — used where GA might say *I like Emma* or *Emma is charming*.
> *it goes ahead and calls me, a nice warm bath* — non-human stimulus with personification flavor.

This is not a passive in the typological sense — there is no demoting morphology, no by-phrase, no detransitivization. It is subject/object reversal, with the experiencer reanalyzed as a topic-comment object. The strategy is most natural with attitudinal experiencer verbs (*charm*, *captivate*, *soothe*) where the stimulus can plausibly be construed as an actor, and extends naturally to non-human stimuli with affective or poetic flavor.

A pragmatic question the construction has to handle: whether the promoted stimulus is read as deliberately acting or merely as the cause. The reading is context-dependent and disambiguated by the lexical content of the verb (some verbs are natively two-faced, some lean one way).

### 6.3 Causative

A periphrastic strategy. The get-oneself paradigm's *get X to V* shape is reused with a third-party causer in the *get*-slot.

> *the math professor, they get me to pass out all the time* — the auto-causative *I get myself to pass out* with an external subject.
> *Emma, they get me to smile all the time* — used where GA might say *I like Emma*.

The causative externalizes the trigger as an agent acting on the experiencer, where stimulus-promotion (§6.2) externalizes the trigger as a quality of the stimulus. The two strategies are not synonymous even when targeting the same GA gloss; they package the relationship differently.

The causative requires an action-host main verb, since *get X to V* selects for an action. It is therefore parasitic on activity-coercion at the verb-choice level: the speaker still has to pick an externalizable activity correlate of the internal state. The two strategies are often deployed together.

### 6.4 Idiom-level frame blocking

At least one idiom blocks the volitional axis as a unit even though its parts do not. The negated-possession idiom *oo riuś* "out of juice" (≈ tired, depleted) accepts the get-oneself frame (*Rimmase oo riuś* "I got worn out"), the become-verb (*Beń oo riuś*), bare predication (*Au oo riuś a bauyen* "all out of juice, on my end"), and the imperfect (*Em oun oo riuś* "I'm running out of juice") — but not the go-ahead frame. Ordinary "on the X side" adjectival predication, by contrast, combines with both axes. Blocking at the idiom level rather than the verb level is a phenomenon class of its own. **[Open: collect further idiom-level blocks before generalizing]** `[Lexicon: riuś, oo not yet entered]`

### 6.5 Open structural questions about the strategies

- **Frequency.** How often each strategy surfaces in everyday discourse, and whether they collectively represent core grammar or peripheral resources. **[Open]**
- **Inheritance of readings by the causative.** Whether the causative inherits the get-oneself paradigm's reading distinctions (e.g., *Emma gets me falling* vs. *Emma gets me to fall*) or collapses the cells. **[Open]**
- **Stacking.** Whether the strategies can compose — e.g., stimulus-promotion of a causative — or are mutually exclusive. **[Open]**

---

## 7. The recognitional-iterative nominal construction

A grammaticalized construction operating on **deverbal nominals** — a verb's action treated as a noun, the territory GA covers with the gerund (*the running*, *the eating*). It is one of the conlang's flagship grammatical innovations and is analyzed as the **deverbal special case of the possession construction** (§12): the frames engage the nominal exactly as they engage any noun, and what is special here is the nominal's own morphology and one piece of supporting syntax.

### 7.1 The two morphemes

The construction stacks the **recognitional marker** (REC, *þ ~ y*, from GA *the*: shared-knowledge type reference) and optionally the **iterative marker** (ITER, *-ś*, from plural *-s*: repeated instances) on a deverbal nominal; attested together in *þ rishś* "the dishes (you know the chore)." Glossing pattern: REC-stem-ITER. The canonical morphological description — forms, stacking, and the morphology-scoped open questions — is `language_reference.md` §3.2.1; this document holds what the construction does with the frames.

### 7.2 The frame meets the recognitional nominal

> *Rimmase ię þ rishś, a bayen, een een.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> 1SG.LVC.NVOL.PST do.CONCORD REC dish-ITER on 1SG.end again again
> "I got (myself) doing the dishes, on my end, again and again."

The frame combinatorics — which frame, which frame aspect, what the combination means — are the possession construction's (§12), and the habitual reading is compositional: recognitional type + iteration + frame engagement. Two features distinguish the deverbal case from a plain noun in the same construction:

1. **The recognitional exponent.** The deverbal nominal takes *þ ~ y* where a plain noun takes the merged article *o*.
2. **Helper-verb support.** On the get-oneself side the deverbal nominal requires a helper verb (*ię* above, from GA *doing*); on the go-ahead side, the grammaticalized *with*. A plain noun combines bare on the get-oneself side. The helper-verb system is deliberately open — see §12.

> *Analytical note.* This construction was previously analyzed as free-standing, with the *with*-mediation treated as its own complement pattern. The possession data reanalyzed it as a special case: the same frame-plus-nominal machinery covers plain nouns ("got myself a drink") and deverbal nominals ("got myself doing the dishes"), with the residue listed above blocking full reduction. The reasoning record lives in `phase4-triage-2026-06.md` §2.1 and the registry entry.

### 7.3 Not a definite article

Glossing the *the*-morpheme as DEF would be etymologically accurate but functionally misleading: the morpheme does not pick out a definite referent. It presupposes addressee familiarity with the *type*, not uniqueness of reference. **[Settled]**

A consequence for the noun system: GA's definite article has not survived as a definite article. Definite reference, where needed, is conveyed through other means (the visibility particles, possessives, context); that system is the responsibility of the language reference's nominal sections (`language_reference.md` §3.2, §3.7), not this document.

> *Origin.* The grammaticalization path *definite article → recognitional marker* is well-attested cross-linguistically; the term *recognitional* is sourced from the determiner-typology literature (Himmelmann and others) for exactly this "you-know-the-one" function. GA *the* is in fact an **etymological doublet** in the conlang: its referential use weakened and merged with *a* into the article *o*, while its recognitional use fused onto the nominal and kept its segmental integrity as *þ ~ y* — divergent reduction paths from one etymon, on the pattern of Latin *ille* yielding both the Romance articles and the third-person pronouns. Like the volition contrast, the construction grammaticalized from a high-frequency GA function word and restructures semantic territory GA does not grammaticalize.

### 7.4 Open questions

The morphology-scoped questions (bare REC; ITER without REC; scope relative to other nominal morphology) live with the morphemes at `language_reference.md` §3.2.1. Construction-scoped questions are the possession construction's (§12.5).

---

## 8. Verbs and the verbal system

This section is the descriptive home for the lexicon-side facts that bear on which verbs participate richly in the verbal system. The procedural counterpart — the methodology for fleshing out the verb lexicon — lives in Appendix A and points back here.

### 8.1 Three relationships between verbs and the volition contrast

Verbs sit in one of three relationships to the volition system, a property of the verb's inherent semantics interacting with the go-ahead/get-oneself contrast.

**Polysemy-resolving.** GA already lexicalized two semantically related events under one form, and the conlang's frame choice disambiguates. *beussou* (< *pass out*): go to bed (go-ahead) vs. fall asleep (get-oneself, happenstance). This category is small and found, not constructed — the verbs are inherited from GA's polysemy. Likely candidates: *fall, catch, drop, lose, take, get*.

**Aspectual-shift.** The two frames do not name different events; the get-oneself reading shifts the aspectual profile of the same event. The go-ahead cell tends to be punctual, agentive, bounded; the get-oneself cell processual, stative-like, unbounded. *remember*: deliberate retrieval (go-ahead) vs. involuntary slide into a state of remembering (get-oneself, happenstance). Cognitive and perceptual verbs (*notice, realize, see, understand, learn, recognize*) are typical here.

**Attitudinal.** The frame choice does evaluative work: same action, different framing of how the subject came to be doing it. *chit-chat*: a deliberately maintained Sunday routine (go-ahead) vs. getting roped into one at the store (get-oneself, happenstance). Most of the verb stock lives here.

The proportions matter: polysemy-resolving is small and closed; attitudinal is the workhorse open category.

### 8.2 Stative verbs

Stative verbs (*know, want, have, be*) need a principled handling decision before entering the system — they do not sit in the go-ahead frame at all, and the get-oneself frame gives them only restricted access (happenstance, threshold, backdrop, but not self-benefit; §3.6).

The three stative-domain strategies (§6) handle most of the territory the morphological paradigm cannot host. Many stative meanings will end up expressed via the strategies rather than by direct stative entries; the bare lexical stative (the *rhiiynii* class, "need/want") is reserved for the irreducibly internal cases. How statives that resist all three strategies are handled — suppletion, simply not framing, or some other mechanism — is **[Open]**.

### 8.3 The deverbal nominal layer

The recognitional-iterative construction (§7) reaches into GA's gerund/nominalization territory and is therefore richer for some verbs than for others. A useful diagnostic: does the GA source have a salient deverbal nominal use? *The walk, our walks* — yes. *The eating* — partial. *The being* — essentially no. Verbs with strong deverbal use participate richly in the recognitional-iterative register; verbs without are action-bound and show their personality primarily through the frames. Verbs with **both** rich deverbal nominalization and clear frame contrasts are the highest-value targets for fleshing out.

### 8.4 How GA history shapes the verb lexicon

The conlang does not inherit GA verbs; it inherits **GA verb uses** — specific constructions that survived three diachronic processes.

**Selection.** A GA verb participates in dozens of constructions; only some survive. Selection is biased by frequency (high-frequency uses survive), colloquial grammaticalization (uses already drifting toward grammatical function in colloquial GA are favored), and fit with conlang grammar (uses that slot into the frames, the recognitional-iterative system, or the stative strategies are favored).

**Reanalysis.** Surviving uses are re-fit into the conlang's grammar: GA *take a walk* (light verb + deverbal noun) → recognitional-iterative nominal; GA's volition-bearing adverbials (*on purpose*, *accidentally*) → the grammaticalized frames; GA's shared-knowledge uses of *the* → the recognitional marker; colloquial GA *get oneself V-ing / to V* → the get-oneself paradigm with concord shape selecting the reading.

**Loss with replacement.** Where the conlang's phonology collapses two GA verbs: one may win and the other die; both may survive but specialize (one taking the go-ahead cell, the other the get-oneself); a periphrasis may fill the gap. **Homophonous merger from sound change is a productive lexical source** — two semantically adjacent stems collapsing into one form gives the conlang verbs whose polysemy is created by its own diachrony, with the frames or the reading grid doing the disambiguating work GA did segmentally.

Three semantic shift patterns recur across these processes: **narrowing** (a broad GA verb survives in one use: *countenance* → just "face"), **specialization driven by grammar** (when the system forces speakers to commit to a reading, the more frequent cell shifts the verb's perceived core meaning), and **accretion of grammatical material** (high-frequency verbs absorb bits of the frame sources into their stems, producing suppletion and verbs that "feel" inherently go-ahead or get-oneself).

---

## 9. Open questions about the system as a whole

Several questions about the system's structure are explicitly held open. They are not gaps to be filled by guessing; they are questions waiting on data.

### 9.1 Are the four readings a unified semantic class?

Happenstance, self-benefit, threshold, and backdrop share a frame (the get-oneself paradigm) and a selection mechanism (frame aspect × concord shape). Whether they share a *semantic dimension* is unclear.

Three of them can be ordered roughly along a scale of how the subject's agency is qualified — agency removed (happenstance), agency on a trajectory (threshold), agency turned inward and effortful (self-benefit). Backdrop is harder to place: it is about discourse status rather than agency per se, though one reading is that "agency backgrounded" is just discourse-framing seen from the agency side.

Two views are live:

- **Unified umbrella.** All four are forms of agency-modulation, with backdrop as the discourse-end of the dimension. This view supports a unifying term for the inventory.
- **Co-grammaticalized.** Three are agency-modulation; backdrop is a discourse-framing function that shares morphology with the others by co-grammaticalization, as is typologically common. This view treats the inventory as a structural set, not a semantic class.

Translation-task data are expected to bear on this — particularly whether backdrop surfaces in discourse contexts similar to the others or in distinctly narrative ones. **[Open]**

### 9.2 Are the stative-domain strategies part of the same broader system?

The strategies (§6) are functionally continuous with the morphological paradigm: they handle subject-event relationships the morphology cannot host. Whether they belong in the same chapter as the frames, or in a sibling chapter cross-referenced with it, depends on how integral they prove. If they surface constantly in everyday speech (plausible, given how much speech is about internal states), they are core grammar; if reached for occasionally, sibling treatment is appropriate. **[Open]**

### 9.3 Is the self-benefit reading on equal billing?

The self-benefit reading is distinctive — the only reading that adds evaluative coloring rather than reducing or qualifying agency — and may also be the rarest. Whether to treat it as a full reading on equal billing or as a marked emphatic with a more specialized term depends on its frequency and contexts of use. **[Open]**

### 9.4 Are there readings the current inventory is missing?

The four readings were identified through systematic exploration of the frame-aspect × concord-shape grid. Translation tasks may surface meanings the inventory cannot host gracefully — candidates noted include avertive (*almost V-ed*), evidential (*must have V-ed*), and try-but-fail. Whether any warrants a new reading, a new strategy, or simply lexical handling is **[Open]**.

### 9.5 Terminology status

The terminology in this document is tracked in `terminology-registry.md`, which records each term's status, shorthand, gloss tag, and full history of alternatives. Terms expected to be revisited when §9.1–9.4 settle: the class term *reading* (if §9.1 settles for the unified-umbrella view, a unifying name for the dimension may be warranted), *stative-domain strategies* (if §9.2 settles for integral-system inclusion), and the system's overall name (currently the generic *verbal system*). **[Open]**

---

## 10. Polarity and negation

**Status: [Provisional — the polarity dimension predates the §2–3 paradigm structure and awaits reconciliation with it; see the analytical note below.]**

The system has a **polarity** dimension (positive vs. negative) alongside volition. The two negative values grammaticalized from distinct GA source phrases, each pairing with one paradigm side:

| | Positive | Negative |
|---|---|---|
| **Go-ahead** | VOL.POS — deliberately doing | VOL.NEG — deliberately not doing; declining. From GA *pass on-*. |
| **Get-oneself** | NVOL.POS — happening to do | NVOL.NEG — failing to; falling short. From GA *not quite-*. |

The negative meanings are not symmetrical: the go-ahead negative is a refusal (the subject declined), while the get-oneself negative is a shortfall (the subject didn't quite get there). On the pronominal side, the not-quite negative surfaces as the fused pronoun forms of §5.2.1.

### 10.1 Nested negation

A productive stacking phenomenon: a get-oneself negative applied over an already-negative go-ahead form yields obligation.

> [NVOL.NEG] [VOL.NEG] (do) → "cannot fail to do" → "must do"

The compositional logic: VOL.NEG marks deliberate refusal; NVOL.NEG marks failure-to. "Failing to deliberately decline" is the inability to choose otherwise — obligation. This is one of the few productive stacking phenomena in the frame.

Open questions:

- Which of the four polarity-bearing markers can productively nest, and in what orders? **[Open]**
- Whether the resulting forms are fully compositional or have idiomatic readings. **[Open]**
- Whether some compositions are blocked or replaced by suppletive forms. **[Open]**
- **Glossing convention for nested constructions.** Candidates: stacked tags `LVC.NVOL.NEG=LVC.VOL.NEG`, or a dedicated obligation gloss `OBLIG` once the construction is treated as conventionalized. **[Open]**

### 10.2 The reconciliation problem

> *Analytical note.* The polarity framework above was developed before the §2–3 paradigm structure (three go-ahead cells; six productive get-oneself cells with readings) and has not yet been integrated with it. Specific tensions: (1) the four-cell grid uses a binary contrast — how does polarity distribute over the richer paradigms; does each productive cell have a negative counterpart, or is polarity more selective? (2) *pass on-* and *not quite-* are GA periphrases on the same model as the frame sources — are they frames in their own right, with their own aspect grids, or polarity markers within the existing frames? **[Open]** (3) How does each reading negate — does happenstance negate as "didn't happen to V," as "happened to not-V," or both? (4) How do the stative-domain strategies interact with negation? **[Open]** The polarity dimension is one of the conlang's distinctive features and is not being deprecated; it needs re-fitting to the more articulated paradigm structure.

---

## 11. The matrix particles

A small class of particles places a whole clause inside a modal frame — that something merely *ended up* so, that the speaker *knows* it, *needs* it, or that it *appears* so. These are the **matrix particles** (informally, *scaffold particles*): each descends from a GA matrix clause, and each colors everything that follows it.

> *Enniip ounoheun splitn.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> MP.ENDUP.PST LVC.VOL.IPFV split-CONCORD
> "It ended up that (they) went ahead and left."

Two facts make the class architecturally important. The matrix particles are the only place in the language where **tense** survives: the verbal system runs on aspect, carried by the weak pronouns (§5.2), while the matrix particles carry a past/non-past contrast inherited from their source clauses. And they are unmarked for **person** — *enniip* reports an outcome without saying whose.

### 11.1 Forms

| Member | Non-past | Past | GA source | Meaning |
|---|---|---|---|---|
| end-up particle | *enp* | *enniip* | *(it) end(ed) up …* | happenstance outcome |
| know-that particle | *no* | *nii* | *(I) know/knew (that) …* | knowledge, awareness |
| really-need particle | *rhi·iiniies* | *rhi·iiniir·ros* | *what I need(ed) is …* | desire; weak obligation |
| appears particle | *piies* | **[Open: past form unattested]** | *(it) appears (that) …* | appearance, seeming |

The really-need particle has a reduplicated intensive, *rhi·ii·rhii·niies*, from GA *what I **really** need is …*. `[Lexicon: all four members pending dictionary entries]`

### 11.2 Function

The tense contrast is **privative**: the non-past member is unmarked and combines freely with habitual and future time adverbs, while the past member asserts a realized state of affairs. `[Placeholder: adverb-combination examples pending — "always end up …", "tomorrow, probably end up …" attested as judgments only]`

The really-need particle codes want and, more weakly, must:

> *Rhi·iiniies ounahen splitn.*
> /—/ `[Placeholder: IPA pending phonology pass; frame form spelling pending the §2.4 paradigm question]`
> MP.NEED LVC.VOL.HAB split-CONCORD
> "What I need is to leave."

### 11.3 Distribution

- **Position.** The matrix particle precedes the clause it scaffolds; a topic precedes the matrix particle: **topic particle > matrix particle > clause**.
- **Aspect government.** Each particle lexically specifies whether the scaffolded clause keeps its own aspect. The end-up particle forces the imperfect — the clause surrenders its aspect (*Beųheun split* "went ahead and left," but *Enniip **ounoheun** splitn*, with the imperfect frame). The know-that particle imposes nothing: *No ei beųheun split* "I know that they went ahead and left." **[Open: government class per particle — survey pending]**
- **Person.** Unmarked throughout. Ambiguity is resolved, when needed, by a strong-pronoun *on-X-end* phrase (§5.3), with flexible placement.
- **Stacking.** Matrix particles stack over each other and under topics, but parseability demands strong-pronoun buffering between the layers; speakers avoid depth beyond two. **[Provisional]**
- **Questions.** The polarity-question particle *ea* applies to a scaffolded clause as to any other (§5.5). `[Placeholder: example pending]`
- **Negation.** Interaction with the negators of §10 undecided. **[Open]**

### 11.4 Interactions

- **With the visibility particles.** The know-that particle is homophonous with the know-particle but syntactically distinct: matrix *no* takes a noun phrase or a full clause and yields a complete sentence; the topic particle's clausal form *noho* instead raises a topic the listener expects elaborated. The two can co-occur (*No Báuyà, no Báuyà* — topic, then assertion).
- **With the frames.** The end-up particle supplies happenstance from above when the bare get-oneself frame under-delivers it (§4.2): *Enniip remmaseto split* "I ended up leaving."
- **With the evidential division of labor.** Under the appears particle, the choice of visibility particle distinguishes perceptible from non-perceptible evidence: *Hiie ossii, piies aų nibii hii* "Look at the outside — it looks nippy" versus *Nou ossii, piies aų nibii hii* "You know the outside — it seems nippy."
- **With mood.** The really-need particle carries the desiderative territory §13 anticipates; the appears and know-that particles carry evidential territory.

### 11.5 Origin

Each member fuses a GA matrix clause — finite verb included — into a particle; the membership criterion for the class is precisely that the etymon contains a finite verb, which is why the members can bear tense while etyma without one (*maybe*, *in my eyes*) yield plain adverbs instead. The path is well-attested cross-linguistically: Latin American Spanish *dizque* (from *dice que* "says that") is a matrix verb fused with its complementizer into a hearsay particle — the exact mirror of the know-that particle in the knowledge domain. The person syncretism follows from phonetic erosion at the pronominal slot: in *what I need is*, the GA pronouns */i, jɪ, ɛj, ɻi/* merge acoustically after /ɻ/ and before /iː/. The end-up particle's aspect government recalls the conjunct order of Algonquian languages such as Ojibwe, where subordinating elements select a dedicated dependent verb form.

### 11.6 Glossing

Composite tags: `MP.ENDUP`, `MP.KNOW`, `MP.NEED`, `MP.APPEAR`, with `.PST` on the past member (`MP.ENDUP.PST` = *enniip*).

### 11.7 Open questions

- *Piies* past form; membership confirmed if found. **[Open]**
- Government class per particle. **[Open]**
- Negation interaction. **[Open]**
- Stacking depth and ordering constraints. **[Open]**
- A predicted reportative member — a *they say / I heard* descendant. **[Open]**

---

## 12. The possession construction

The language has no everyday verb *have*. Possession, acquisition, choosing, and giving are carried by the frames combining directly with a nominal — the **possession construction**. What GA spreads across *have*, *get*, *pick*, and *give*, the conlang derives from frame choice and frame aspect over a bare noun.

> *Rimmaseu beikw.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> 1SG.LVC.NVOL.PST=ART vehicle
> "I have a vehicle." (lit. "got myself a vehicle")

The final lengthened vowel of *rimmaseu* is the fused etymological article. `[Placeholder: gloss segmentation of the article fusion pending]`

### 12.1 Forms and function

- **get-oneself + nominal, perfect frame aspect** → possession ("have"): *Rimmaseu beikw*.
- **get-oneself + nominal, imperfect frame aspect** → acquisition in progress ("getting"). `[Placeholder: example pending]`
- **go-ahead (+ *with*) + nominal** → deliberate selection ("picking and choosing"). `[Placeholder: plain-noun example pending; the deverbal case is attested at §7.2]`
- The frame choice carries the usual coloring: *Rimmaseu rhink* "got myself a drink" reads self-benefit; *Rimmaseu þlii* "got the flu" reads affliction — the same construction, with the nominal's semantics selecting the flavor.
- **Lexical alternatives** modulate intentionality: *rib* "give" for explicit volition in transfer; *ǫıĩ* "own" for neutral mere-having. `[Lexicon: rib, ǫıĩ not yet entered]`

### 12.2 The transfer extension

With a recipient in the *get*-slot, the construction causativizes into giving, volition-neutral by default:

> *Ritm o rhémstwè.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> get.3PL ART book
> "(I/they) gave them the book." (lit. "got them the book")

The extension resists a topic-marked definite object; explicit-volition *rib* with the go-ahead frame is used instead. **[Open: transfer-extension object restrictions]**

### 12.3 The deverbal special case and the helper-verb question

A deverbal nominal in the construction is the recognitional-iterative nominal of §7, distinguished by the recognitional exponent (*þ ~ y* for merged *o*) and by **helper-verb support** on the get-oneself side (*Rimmase ię þ rishś* — §7.2).

**The helper-verb question is deliberately open.** *Do* is the default helper, but GA's own collocations vary by lexical item (*do* the dishes, but *take out* the trash, *pull* the trigger, *push* the issue), and importing that variety wholesale would both drift toward relexification and nest light verbs inside the already-grammaticalized frames. The working disposition, **[Open]** in all four parts:

1. A **small licensed set** of helper-verb pairings, admitted only where the lexical item earns it.
2. **Default avoidance**: most such meanings are phrased another way — Latinate verbs in particular tend to supply frame-free lexical routes (*preb* "cook" rather than a do-the-cooking construction).
3. A **tentative additional helper** under consideration (candidate source GA *bop*), unconfirmed.
4. Some deverbal nominals may simply be **incompatible** with the get-oneself frame — a gap, not a workaround.

> *Analytical note.* A related lexical decision is recorded here because it bears on the helper's eventual citation shape: GA *do* is assigned an **irregular** sound-change path, yielding *o* rather than the regular reflex in ⟨ii⟩ — merging with the descendant of GA *go*, which already covers "become" and is expected to extend to motion and speech senses. The default helper, the become-verb, and the merged article would then share the surface form *o*; the collision load on *o* is flagged for review, and the attested concord form *ię* (from GA *doing*) must be reconciled with the merger. `[New rule needed: irregular reflex of GA *do* → o (designed exception)]` `[Lexicon: o (do/go merger) pending — senses: do-helper, become, go]`

### 12.4 Interactions

- **With the recognitional-iterative nominal** (§7): the deverbal special case, above.
- **With the frame's argument structure** (§4.1): the *with*-mediation facts live here; §4.1's open question is fed, not closed.
- **With the separative satellite** *oþw* (§4.2): unrelated mechanisms — the satellite shapes the verb's event structure; the helper supports a nominal.

### 12.5 Open questions

- Helper-verb ecology — the four-part disposition of §12.3. **[Open]**
- Transfer-extension object restrictions. **[Open]**
- The *bop* helper candidate. **[Open]**
- The imperfect-aspect acquisition reading — confirm with attested examples. **[Open]**

---

## 13. Mood

Beyond the go-ahead/get-oneself contrast (which arguably is mood), the system likely includes:

- **Imperative** — formation and inventory not yet committed. **[Open]**
- **Optative / desiderative** — the desiderative territory is carried by the really-need particle (§11); whether a separate *want to*-derived optative also exists is **[Open]**.
- **Evidential distinctions** — partly carried at the matrix layer (the appears and know-that particles, with the visibility particles dividing perceptible from non-perceptible evidence — §11.4); whether further evidential machinery exists is **[Open]**.

These are placeholders for sections that will be developed as design proceeds.

---

## 14. A clause, assembled

The pieces described above combine as: (optional dislocated NP topic) + weak pronoun (carrying any fusion) + frame + main verb with concord. This section assembles them. Frame and pronoun forms below are attested (§2.4, §3.7, §5.2); **all main-verb and NP surface forms are placeholders** pending dictionary derivation, and pitch diacritics are omitted because the pitch of the frame forms has not yet been recorded. `[Open: pitch marking on frame and pronoun forms]`

**Go-ahead, habitual:**

> *e oheun drinkin* — `[Placeholder: drinkin]`
> 1SG    go.ahead.LVC.VOL.HAB    drink-CONCORD
> "I go ahead and drink (it)" — habitual, deliberate

**Go-ahead, imperfect (pronoun carries the +be fusion; frame in bare gerund shape):**

> *em ounoheun drinkin* — `[Placeholder: drinkin]`
> 1SG.be    go.ahead.LVC.VOL.IPFV    drink-CONCORD
> "I'm going ahead and drinking (it)" — ongoing, deliberate

**Get-oneself, past, happenstance (progressive-shaped concord):**

> *e rimase beussourin* — `[Placeholder: concord shape on beussou unverified]`
> 1SG    get.oneself.LVC.NVOL.PST.1SG    fall.asleep-CONCORD
> "I got myself falling asleep" = "I fell asleep" — it befell me

**With a dislocated NP topic and resumptive pronoun (§5.4):**

> *the coffee — e oheun drinkin* — `[Placeholder: NP and main verb]`
> coffee.TOP    1SG    go.ahead.LVC.VOL.HAB    drink-CONCORD
> "the coffee — I go ahead and drink (it)"

Negated clauses replace the bare pronoun with a not-quite fusion (§5.2.1); the shape of the main verb under negation is **[Open]** pending the §10 reconciliation.

---

## 15. Cross-references

- `terminology-registry.md` — canonical terminology, gloss tags, and naming history.
- `verb-paradigm-verdict.md` — full cell-by-cell predictions, the three live questions on self-benefit selectivity / threshold-for-statives / habitual-plus-infinitive reading, and the analytical history behind this consolidation.
- `translation-frequency-task.md` — the translation-task instrument designed to gather the usage-weighted data §9 calls for.
- `language_reference.md` §3.4 — the high-level summary that points at this document.
- `phonology.md` — phonological details of the frame and verb-stem forms.
- Appendix A (below) — the verb-lexicon-building methodology.

---

## Appendix A: Verb-Lexicon-Building Methodology

A working procedure for fleshing out the conlang's verb lexicon in a way that showcases the grammar's divergence from GA, rather than producing one-to-one translations of GA verbs. Methodology, not descriptive grammar — kept as an appendix so the recipe sits adjacent to the verbal-system reference it draws on. Descriptive facts the recipe relies on live in §3, §6, §7, and §8; the appendix points there rather than restating them.

### A.1 Goal

Build a verb stock that:

- Foregrounds the **verbal system as a whole** — the frames, the four readings, the stative-domain strategies, and the recognitional-iterative nominal — as the language's distinctive expressive tools.
- Does **not** map cleanly onto GA verbs. The conlang's verb territory should be carved differently — sometimes finer, sometimes coarser, sometimes shifted laterally.
- Lets the conlang's grammar do real expressive work that GA does clunkily or not at all.
- Provides a small set of **showcase verbs** for pedagogical illustration, alongside a much larger set of **workhorse verbs** for everyday use.
- Loads the lexicon with verbs that light up the get-oneself paradigm across multiple readings, not just verbs that produce one shining cell and four muted ones.

### A.2 The two selection axes

Each candidate verb sits on two independent dimensions; both inform whether to recruit it and how to flesh it out.

#### A.2.1 Axis A — verb-volition category

Where the verb sits with respect to the go-ahead/get-oneself contrast at the *outer* level. The three categories — **polysemy-resolving**, **aspectual-shift**, **attitudinal** — are described in §8.1. Recipe-relevant additions:

- Polysemy-resolving is **closed and found, not constructed** — don't manufacture polysemy GA didn't supply. Expected size: 15–40 verbs. Role: showcase verbs for pedagogical materials.
- Aspectual-shift: secondary showcase — demonstrates the system doing meaningful work even where GA supplies no ready-made polysemy.
- Attitudinal: the everyday expressive tool — claiming credit, deflecting responsibility, signaling agency or its absence. Most of the verb stock.

#### A.2.2 Axis B — get-oneself paradigm coverage

How richly the verb populates the four readings. This is the *inner* level of selection and is independent of Axis A. Coverage is described as **rich**, **medium**, or **thin** based on how many of the four readings yield productive, non-coerced uses. What each reading wants from a verb:

##### A.2.2.1 Happenstance

Hosted by HABITUAL and PAST with progressive-shaped concord. Wants verbs where the event can plausibly happen to the subject without their agency. Broadest of the four — almost any verb hosts happenstance if the event can be construed as befalling the subject. Achievements (*fall, find, notice, realize, catch*) host it richly because the moment of the event is naturally non-agentive. Activities (*think, wander, hum, doodle*) host it richly when they can drift into existence without intention. Verbs that *only* make sense as deliberate (*sign a contract, vote, file taxes*) host it poorly.

##### A.2.2.2 Effortful self-benefit

Hosted by HABITUAL (marked) and PAST with infinitive-shaped concord. The most selective reading. Wants (a) action-host semantics so the subject can do the thing, (b) plausible benefit to the subject, and (c) effort or self-direction in the doing. *get up, get going, get clean, get organized, get fed, get to bed, get out of the rain* host it extremely well. Verbs that benefit others (*give, help, comfort*) host it poorly. Verbs that are bad for the subject (*catch a cold, get lost, fall*) host it only under coerced negative-evaluation readings — a live question (§9.3, `verb-paradigm-verdict.md` §1.5).

##### A.2.2.3 Threshold

Hosted by PROGRESSIVE + infinitive-shaped concord. Wants verbs with a natural onset — events with a "becoming-such-that" build-up phase. Threshold-event verbs (*fall asleep, doze off, walk out, leave, give up, break down, melt down, cave*) host it paradigmatically. Graded approaches to a state (*warm up, calm down, tire out, perk up, sober up*) also work. Punctual achievements without build-up (*find, notice, realize*) host it poorly.

##### A.2.2.4 Backdrop

Hosted by PERFECT + progressive-shaped concord. Wants verbs producing a durative event whose ongoing-ness is discourse-relevant. Activity verbs work well (*read, walk, cook, watch, listen, talk, write, drive*). Cognitive activities (*think, wonder, worry, dream, daydream*) are paradigmatic. Achievements host it poorly; telic accomplishments work only mid-event.

#### A.2.3 The two axes in combination

Each verb gets a two-coordinate label: an Axis A category and an Axis B coverage profile (rich / medium / thin, optionally with reading detail like *rich on happenstance and backdrop, thin on self-benefit and threshold*). The combined profile drives recruitment priority (§A.8). The two axes are orthogonal: Axis A is a typology of what the outer frame contrast does for a verb; Axis B is a typology of inner-paradigm richness. Any Axis A category can carry any Axis B profile.

### A.3 The stative domain

Statives (*be happy, like, want, need, hurt*) sit outside the frames proper (§3.6, §8.2). The three strategies of §6 are, from the recipe's standpoint, three different ways of recruiting a GA stative meaning into the lexicon.

#### A.3.1 Activity-coercion

Recruit an activity verb whose typical correlate of the GA stative meaning carries the load: GA *be happy* → conlang *smile, laugh, grin*; GA *be sad* → *frown, sigh*. When a GA stative meaning is on the recruitment list, look for the GA activity verbs that correlate with it and prioritize *those*. The stative itself may need no conlang entry at all.

#### A.3.2 Stimulus-promotion

Recruit a verb that frames the stimulus as the grammatical subject acting on the experiencer (§6.2). GA experiencer-object verbs (*charm, captivate, soothe, bore, annoy, fascinate*) are the natural targets: their conlang counterparts host the go-ahead frame productively because the stimulus can be construed as an actor.

#### A.3.3 Causative

Recruit the *get X to V* shape with a third-party causer (§6.3). The causative needs an action-host main verb, so it composes with activity-coercion: the speaker still picks an externalizable activity correlate of the internal state. The two strategies are deployed together for many GA stative meanings.

#### A.3.4 What this means for stative-domain recruitment

For each GA stative meaning the conlang needs to express:

1. Identify the activity verbs that correlate with it (for activity-coercion).
2. Identify the stimulus-frame verbs that can host it (for stimulus-promotion).
3. Decide whether the bare stative — the *rhiiynii*-class lexical stative, accessed through happenstance/threshold/backdrop — also needs an entry, or whether the strategies cover the territory.

For most GA statives the answer to (3) will be that the strategies cover it. A small number warrant bare entries for the irreducibly internal cases (*rhiiynii* "need/want" being the paradigm example).

### A.4 Semantic territories to prioritize

High Axis B coverage clusters in specific semantic regions of GA. These are the highest-yield recruitment targets for a richly colored verbal system.

#### A.4.1 Tier 1 — verbs that should light up across all four readings

The gold of the lexicon; recruit aggressively.

- **Self-care and bodily-state activities.** *fall asleep, wake up, doze, rest, settle in, settle down, calm down, perk up, sober up, get up, get going, ease into, lean back, sink down, sit up, get dressed, shower, eat, drink, settle.* Hits self-benefit (self-directed effortful action), happenstance (can happen without intention), threshold (natural onsets), backdrop (durative and experientially salient).
- **Cognitive activities.** *think, wonder, worry, dream, daydream, brood, ruminate, reflect, ponder, mull.* Hits backdrop paradigmatically (the I-was-thinking-about-it-when-X reading), happenstance richly (thoughts arrive uninvited), threshold for the ones with onset, self-benefit by coercion ("I got myself to think about it").
- **Threshold-transition verbs.** *walk out, drift off, slip away, give up, break down, cave, melt down, slip into, ease into, sink down, lean back.* Hits threshold paradigmatically, happenstance richly, backdrop for the durative ones, self-benefit for deliberate-self-positioning uses.

#### A.4.2 Tier 2 — verbs that light up three of the four richly

Strong targets; expect one reading to be thin.

- **Daily-life social-texture activities.** *chit-chat, wander, hang out, putter, tinker, fuss, dawdle, browse, mosey, lounge.* Strong on happenstance and backdrop. Self-benefit coerced but available. Threshold weak — no natural onsets.
- **State-onset cognitive/perceptual verbs.** *realize, notice, recognize, remember, learn, understand, see, hear, feel.* Strong on happenstance (the moment of noticing is non-agentive), threshold (becoming-aware), and backdrop (the durative state of remembering). Self-benefit weak unless the verb has a deliberate effortful use. These double as Axis A aspectual-shift verbs, layering inner and outer richness.

#### A.4.3 Tier 3 — strong happenstance/backdrop pairings, less elsewhere

Useful for filling out the lexicon, but not anchors of the paradigm.

- **Durative perceptual/experiential activities.** *watch, listen, read, watch over, look out, keep an eye on, follow along, observe.* Strong on happenstance and backdrop; threshold and self-benefit weak.
- **Mid-process accomplishments.** *cook, write, work on, sort through, get through, build, repair, clean up.* Backdrop strong mid-event; happenstance possible; self-benefit and threshold mostly weak or coerced.

#### A.4.4 What to deprioritize

Thin-paradigm verbs are still worth recruiting eventually, but not first if richness is the goal.

- **Pure-deliberate action verbs** (*sign, vote, build, pay, file, ratify, declare*). Belong in the go-ahead frame; mostly coerced or marked on the get-oneself side.
- **Other-directed verbs** (*give, help, teach, comfort, serve, deliver*). Self-benefit and threshold weak; happenstance and backdrop coerced.
- **Pure achievements without onset** (*win, lose, hit, arrive, die* — though *die* has cultural weight that may justify exception). Host only happenstance cleanly.
- **Punctual transitive achievements** (*catch, find, notice* — the polysemy-resolving class). Dramatic Axis A contrasts, but the get-oneself cells themselves are thin.

#### A.4.5 A design-strategy note

The Tier 1 convergence zone clusters heavily in the **self-state / cognitive / threshold-transition** territory. This is not accidental: it is exactly where a system grammaticalizing non-straightforward agency *should* be richest, because that is where straightforward agency is most often qualified.

A consequence: a lexicon loaded preferentially with these verbs gives the conlang a distinctive *texture* — speech will lean toward introspective, processual, transition-aware framings. Whether that fits the conlang's cultural and aesthetic profile is a deliberate design question; the current default assumption is yes, but the assumption is flagged rather than naturalized.

### A.5 How GA history drives the lexicon

The selection / reanalysis / loss-with-replacement processes and the three semantic shift patterns are described in §8.4. The recipe consequence: when working a candidate verb, list its GA construction inventory, predict which uses survive selection, and watch for the merger phenomena §8.4 describes — they are recruitment opportunities, not noise.

### A.6 The deverbal nominal layer

The recognitional-iterative construction and its per-verb diagnostic are described in §7 and §8.3. Recipe consequence: test *the V-ing* and *the V-ings* for every candidate. Verbs with both rich deverbal nominalization and rich frame contrasts and reading coverage are the highest-value targets — flesh these out first. This layer is orthogonal to both axes and adds a third dimension to the verb's expressive profile.

### A.7 The diagnostic questions

For any candidate verb, work through these five questions in order. Verbs that yield satisfying answers across all five are the ones to build out first; thin answers signal candidates to defer.

1. **Which GA constructions did it participate in, and which survived?** List the GA uses; mark which are high-frequency, colloquial, formal. Predict which survive selection (§8.4).
2. **Where does it sit on Axis A?** Polysemy-resolving, aspectual-shift, or attitudinal (§8.1)?
3. **Where does it sit on Axis B?** Test the four readings. Which cells are productive, coerced, blocked? Record a coverage profile (rich / medium / thin), optionally with reading detail.
4. **Does it have a salient deverbal nominal, and what is the recognitional-iterative reading?** Test *the V-ing* and *the V-ings*. Is the shared-knowledge reading natural? The iterative reading? Is the verb register-flexible or register-bound?
5. **Are there cognates or competitors in GA that the conlang's phonology has merged or distinguished?** Check for near-homophones the sound changes will collapse, semantic neighbors the conlang may force into specialization, and GA polysemy the conlang may split across multiple verbs.

Questions 2 and 3 give the two-axis profile; 1, 4, and 5 give the diachronic and morphological context.

### A.8 Two-axis building order

Recruitment priority combines the Axis A and Axis B profiles. A verb that is rich on Axis B and poly-resolving or aspectual-shift on Axis A is the highest-priority target — it lights up both the outer contrast and the inner reading grid.

#### A.8.1 Priority 1 — flagship verbs

High on both axes (poly-resolving or aspectual-shift; rich coverage). The showcase: the frame contrast does dramatic work *and* the paradigm fills out across all four readings. Examples: *fall asleep* (poly-resolving via GA *pass out*, Tier 1 self-care/threshold), *remember* (aspectual-shift, Tier 1 cognitive), *walk out* (poly-resolving or attitudinal, Tier 1 threshold-transition). First batch.

#### A.8.2 Priority 2 — workhorse verbs

High on Axis B, plain on Axis A (attitudinal; rich or medium-rich coverage). The everyday vocabulary that gives the get-oneself paradigm its expressive weight in normal speech: most cognitive activities, self-care verbs, daily-life social-texture activities. *think, wonder, chit-chat, wander, putter, doze*.

#### A.8.3 Priority 3 — secondary showcase

High on Axis A, plain on Axis B (poly-resolving or aspectual-shift; medium or thin coverage). Dramatic outer contrasts, thin inner paradigms. Useful pedagogically because the contrast is sharp and easy to teach. *catch, find, notice*.

#### A.8.4 Priority 4 — long-tail vocabulary

Plain on both axes. The bulk of the lexicon; recruit as needed for breadth.

#### A.8.5 Priority 5 — stative-domain recruitment

Run alongside Priorities 1–4: for each GA stative meaning the conlang needs, identify activity-coercion, stimulus-promotion, and causative recruitments per §A.3.4. Bare stative entries (*rhiiynii*-class) only for the irreducibly internal cases.

### A.9 Avoiding GA-mapped lexicon

Specific tactics for keeping the conlang's verb territory genuinely divergent:

- **Don't ask "what's the conlang word for X."** Ask "what's the conlang's whole vocabulary for the territory X covers in GA," and expect the answer to involve multiple verbs splitting GA's range differently, plus possibly a stative-domain strategy.
- **Look for GA polysemy to split.** *Run* covers physical running, machines operating, organizations being directed, water flowing, candidates campaigning. The conlang's *run*-cognate may take only one, with the others recruited to different verbs entirely.
- **Look for GA distinctions to merge.** Where GA distinguishes two verbs the phonology collapses, the merged form may be enriched by frame disambiguation, or one sense may take over.
- **Identify GA volitional twins.** Pairs like *fall/drop*, *forget/put-out-of-mind*, *sleep/go-to-bed*, *learn/find-out* — does the conlang preserve both, merge them, or recruit them to different paradigm sides of a single verb?
- **Watch for sound-change-driven mergers.** When working derivations, flag cases where two semantically related GA stems will produce identical conlang forms. These are dictionary entries with multiple GA etyma — record both, with notes on which senses came from which source.
- **Check the deverbal nominal slot.** A verb without a recognitional-iterative paradigm is missing one dimension of its expressive range. Either find a GA construction that supplies one, or note that the verb lives in the frame dimensions only.
- **Look for GA stative meanings the strategies can recruit.** Before adding a stative entry, ask which activity-coercion, stimulus-promotion, or causative recruitments cover the territory. Often the entry isn't needed.
- **Default to the Tier 1 convergence zone** (self-care, cognitive activity, threshold-transition) when uncertain where to recruit next — these pay back recruitment effort with the highest expressive dividend.

### A.10 Polarity — held aside

The get-oneself paradigm and reading inventory have been worked out for positive polarity. Negative polarity is held in §10 pending reconciliation. For diagnostic question 3 (Axis B coverage), apply only to the positive-polarity grid for now, recording negative-polarity behavior as observations rather than systematizing it. When the §10 reconciliation is done, §A.2.2 will be updated. This is a known incompleteness, not a hidden assumption.

### A.11 What to record per verb

Beyond the dictionary's standard schema, verb entries should include:

- **Two-axis profile.** Axis A category and Axis B coverage (rich/medium/thin, with reading detail if useful).
- **GA construction inventory** — which GA uses survived, died, were reanalyzed.
- **Get-oneself paradigm coverage** — for each of the six productive cells, is it productive, coerced, or blocked? Which reading does the productive cell host? Example sentences for productive cells.
- **Go-ahead paradigm coverage** — for the three cells, productive, marked, or blocked?
- **Recognitional-iterative paradigm** — whether *the V-ing* and *the V-ings* are licensed, and the readings.
- **Stative-domain recruitment** (if applicable) — which activity-coercion / stimulus-promotion / causative recruitments share territory with this verb.
- **Mergers and competitors** — other GA verbs whose territory this verb has absorbed or shares.
- **Register notes** — intimate/formal, frequent/rare, marked uses.

This is more apparatus than current dictionary entries carry, and most of it can be deferred to a Notes section. But the two-axis profile and the two paradigm-coverage records should be in the entry from the start: they justify the verb's place in the lexicon and define how it interacts with the rest of the grammar.

---

## 16. Versioning notes

### v2.2, June 2026 — §7 migration executed (Session L)

§7.1 and §7.4 reduced to pointers: REC/ITER morphological description and its open questions migrated to `language_reference.md` §3.2.1 (langref v3.2), completing the relocation the v2.1 note anticipated. §7 now holds the special-case statement, the worked example, and the Origin material (REC ≠ DEF; the *þ/o* etymological doublet), per the one-home rule.

### v2.1, June 2026 — translation-exercise integration (Session V)

**New sections.** §11 The matrix particles (class, four members, privative tense, aspect government, person syncretism, stacking, evidential division of labor; the language's split TAM stated: aspect on the weak pronouns, tense on the matrix particles). §12 The possession construction (have/get/choose from frame + nominal; the transfer extension; the deverbal special case; the helper-verb question left open by user decision — four-part disposition recorded with the relexification/nesting rationale; the designed *do* → *o* irregular merger flagged for phonology and lexicon). Former §11–§14 renumbered §13–§16; live cross-references updated in-document and in `language_reference.md`; historical versioning notes left as written.

**§4.2.** Passive-shaped concord added with the *spli·oþw* paradigm and the satellite-conflation caveat; compositional-readings statement (frame aspect × concord shape × stem event structure, plus matrix scaffolding); new §4.2.1 irregular concord (*meirtt*); new §4.2.2 concord under suffixation (stub).

**Paradigm corrections (user, 2026-06-10/11).** 1SG weak pronoun *e* (bare) and *em* (+be), replacing *eu*/*eum* — creating a 1SG/3SG.INANIM syncretism in the bare series parallel to the existing prospective and ability syncretisms; inanimate habitual go-ahead *osoheun*, replacing *ośeun*; progressive *ounoheun* confirmed canonical (*ounahen*, *ounohen* are errors). Animate habitual flagged **[Open]**: table *oheun* vs. a 2026-06-10 note reading *ouhen*; the *osoheun* parallel favors *oheun*. Examples swept in §4.3, §5.4, §5.5, §14.

**§5.** §5.3: antitopic tagging added as a fourth strong-pronoun use. §5.4: right-dislocation asymmetry added (visibility contrast is left-periphery-only) **[Provisional]**. §5.5: *ea* conditional use added.

**§6.** New §6.4 idiom-level frame blocking (*oo riuś*); former §6.4 renumbered §6.5.

**§7.** Surface forms closed (REC *þ ~ y*, ITER *-ś*; attested *þ rishś*), removing the v2 [Open] flag. Rewritten as the deverbal special case of the possession construction (demotion decision, 2026-06-11), with the prior free-standing analysis and reasoning quarantined; the *þ/o* etymological-doublet origin added to §7.3. §7.4 questions marked as migrating to the language reference's nominal sections.

**Abstract** restored and revised in the front matter: the v2 Abstract survived only as the copy in `language_reference.md` §3.4's stub (the source document had lost it — drift incident); the restored text merges the v2 claims with the new architecture, and the §3.4 stub was regenerated from it. Source decisions: 2026-06-10 translation exercise; `phase4-triage-2026-06.md`; registry Batch II (accepted 2026-06-11, with *need particle* renamed *really-need particle* by user decision).


### v2, June 2026 — conformance pass: terminology registry adopted; structure and voice revised

**Terminology.** All prose normalized to `terminology-registry.md` (June 2026 batch): *volitional go-ahead* / *non-volitional get-oneself* replace *volitive* / *non-volitive*; *frame* promoted to prose-primary over *light verb complex* (LVC retained for morphology-internal prose and gloss tags); *frame aspect* replaces *LVC.TAM*; the four readings renamed *happenstance* (HAP), *effortful self-benefit* (SELF.BEN), *threshold* (THRESH), *backdrop* (BACK), retiring the prose abbreviations PH/AB/INC/PS; *iterative marker* (ITER) replaces the nominal *habitual marker* (HAB), resolving the collision with the habitual frame aspect cell; §7 retitled *recognitional-iterative nominal construction*; concord shapes reworded *infinitive-/progressive-shaped* (synchronic) from *-derived* (diachronic); *gnomic/habitual* single-named *habitual*. §10 legacy *INVOL* tags normalized to *NVOL* (terminology only; the analytical reconciliation remains open).

**Structure.** §1 absorbs the asymmetry argument previously restated in §12; §12 repurposed as "A clause, assembled" (worked clause assembly from attested frame and pronoun forms, placeholders flagged). §8 gains §8.4 (GA history: selection/reanalysis/loss and shift patterns), now the canonical home for material previously duplicated across §8, A.5, and `language_reference.md` §5.2–5.3; A.5, A.6, and A.2.1 reduced to pointers plus procedural additions. §9.5 reduced to a status pointer at the registry. §10 restructured synchronic-first ("Polarity and negation"): the description leads, the reconciliation problem moves to an analytical note. Section numbering otherwise preserved to protect cross-references from out-of-tree documents.

**Voice and examples.** Project-history narration moved into analytical-note blocks or the registry (§1 reading note, §4.2 term hedge, §5.2.2 syncretism motivation, §7.3 origin, §10.2). Source-frame subsections retitled "Origin." GA-calque examples flagged `[Placeholder]` throughout (§4.3, §5.4, §6, §7.2, §12). New explicit [Open] flags: concord-affix surface inventory (§4.2), REC/ITER surface forms (§7.1), pitch marking on frame/pronoun forms (§12).

### v1.3, May 2026 — pronominal system added as §5; LVC paradigm tables added

**New §5: The Pronominal System.** Pronouns treated as aspect carriers rather than standalone word forms. §5.1 describes the animacy (GO-AHEAD) vs. person/number (GET-ONESELF) agreement asymmetry. §5.2 documents the weak (clitic) pronoun paradigm across bare, imperfect, prospective/conditional (would), ability (could), and n't.quite negative cells, with syncretism noted for 2PL and 3PL modal/negative forms. §5.3 documents the strong (tonic) pronoun paradigm from GA *on [POSS] end*, with three functional readings (emphatic, possessive, topic/frame). §5.4 establishes left dislocation with resumptive pronouns as the mechanism for full-NP subjects. §5.5 describes interrogative via intonation + *ea* (from GA *at all*) with no do-inversion [Provisional]. §5.6 (pro-drop) and §5.7 (WERE irrealis particle) are held [Open]. The modal fusions (would, could) are restricted to pronouns — no nominal-subject modal construction without a resumptive pronoun. **[Settled]**

**New §2.4 and §3.7: LVC paradigm tables.** GO-AHEAD paradigm given for animacy distinction at gnomic/habitual aspect (*oheun* animate, *ośeun* inanimate 3SG), invariant imperfect (*ounoheun*), and past (*beųheun*). GET-ONESELF paradigm given for full person/number grid across three aspects (gnomic/habitual, imperfect/progressive, past).

**Renumbering.** Former §5–§13 shifted to §6–§14 to accommodate new §5. All internal cross-references updated.

**Paradigm CSVs.** Full paradigm data held in `paradigms/pronoun-weak.csv`, `paradigms/pronoun-strong.csv`, `paradigms/lvc-paradigm.csv`.

**Open questions added.** §5.6 (pro-drop conditions), §5.7 (WERE irrealis form and distribution).

### v1.2, May 2026 — verb-lexicon-building methodology folded in as Appendix A

**Appendix A added.** The `verb-recipe.md` sibling working note (specifically its v2 draft, dated May 2026) is folded in as Appendix A: Verb-Lexicon-Building Methodology. The procedure was restructured into eleven sub-sections (A.1–A.11) covering goal, two-axis selection (Axis A verb-volition category × Axis B non-volitive paradigm coverage), stative-domain recruitment via the three strategies, semantic-territory tier list, GA-history-driven lexicon shaping, recognitional-habitual diagnostic, five diagnostic questions, two-axis building order (Priorities 1–5), tactics for avoiding GA-mapped lexicon, polarity-deferred note, and per-verb recording schema. The original draft is archived at `drafts/integrated/2026-05-05-verb-recipe-v2.md`.

**Terminology normalized during integration.** The draft used the older *modulated* term throughout (the May 2026 verbal-system-description session terminology). Replaced with *non-volitive* to match the §1–9 main body and v1's terminology decision. The legacy four-cell INVOL terminology in §10 is unchanged here; that section's terminology drift is a separate reconciliation task.

**Cross-doc propagation.** §7 lead and §8 lead updated to point at Appendix A rather than the retired sibling. §13 cross-references list updated. Parallel updates: `language_reference.md` v2.5 (§5.1, §8 doc set list, §3.7.5, §3.7.7); `CLAUDE.md` "Document hierarchy" out-of-tree list.

### v1.1, May 2026 — pedagogical-game references stripped

Three open-question entries previously motivated their open status by reference to the in-development game's mini-game build sequence:

- §7.4 "Scope of REC and HAB relative to other nominal morphology" dropped its "to be forced by the market and lost-and-found mini-games" tag.
- §11 "Imperative" dropped its "used in the kitchen and delivery mini-games" tag; rewritten to flag formation and inventory as open.
- §11 closing line rewritten from "developed when the relevant mini-games force commitment" to "developed as design proceeds."

The questions themselves are unchanged. Parallel cleanup applied across `language_reference.md` (v2.3), `orthography.md` (v2.2), `dictionary.md`, and `CLAUDE.md`.

### v1, May 2026 — initial consolidation

This document supersedes `verb-terminology.md` (now retired) and consolidates the verbal-system analysis from the May 2026 verbal-system-description session. It draws on the verb-terminology session (volitive, LVC, concord affixes, recognitional-habitual), the verbal-system-description session (the volitive-vs-non-volitive paradigm structure, four sub-modalities, stative-domain strategies, principled gaps), and the verb-recipe session (verb-volition typology, deverbal nominal layer).

**Relationship to predecessors.**
- `verb-terminology.md` (May 2026, retired) — content superseded by this document. The terminology committed there (volitive, LVC, concord affixes, REC/HAB) is preserved here; the *involitive* term is replaced by *non-volitive*.
- `verb-recipe.md` (May 2026, sibling working note) — methodology for verb lexicon-building. Descriptive-grammar claims it depended on are folded into §8 of this document; the recipe procedure itself remains a sibling reference.
- `verb-paradigm-verdict.md` (May 2026, sibling) — cell-by-cell analytical predictions and history. Stays as a separate document; this consolidation references it for analytical detail.

**Terminology shift: involitive → modulated → non-volitive.**
- *Involitive* was used in early verb-terminology work; rejected as privatively naming the side of the paradigm where the structured inventory of sub-modalities lives.
- *Modulated* was the working term in the May 2026 verbal-system-description session, chosen positively to capture that the side modulates rather than negates volition.
- *Non-volitive* is the term used in this document, chosen for readability. It accepts the privative form on the understanding that the principled-asymmetry argument (§8) is preserved in the prose framing rather than in the term itself.

**Polarity carry-forward.** The polarity dimension and nested-negation phenomenon (§10) are preserved as flagged-for-reconciliation. They predate the §2–3 paradigm structure and need re-fitting to it.
