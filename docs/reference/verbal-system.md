# The Verbal System

**Version:** v2.10 (June 2026)
**Status:** Sibling reference document, parallel to `phonology.md` and `orthography.md`. The language reference's §3.4 is a high-level summary that points here. Supersession history: §17.

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

Three further resources extend the system beyond the paradigm proper. When the meaning to be expressed is a state rather than an event, speakers reach for one of three **stative-domain strategies** (§6). The frames combine directly with nominals in the **possession construction** (§13), which covers having, getting, choosing, and giving; its deverbal special case is the **recognitional-iterative nominal** (§7), marking shared-knowledge type reference and iteration. And above the clause sits a small class of **matrix particles** (§11) — the home of the language's only surviving tense — which scaffold the clause with modal and evidential meaning: that it merely ended up so, that the speaker knows it, needs it, gathers it to be so, or, in sum, that *in short* it is so.

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

The self-benefit reading's dative-of-interest force can **flip malefactive** in a zero-sum reading, where another party's benefit registers as the subject's detriment. With *baurzıĩ* "barge in," the get-oneself frame gives the intrusion a mildly undesirable color — *…rhishisben ei retmseto baurzıĩ* "…when she barged in (on me)" — against the neutral go-ahead alternative *…rhishisben ei ouheun baurzıĩ*. A single attestation; whether the flip is productive is **[Provisional]**. `[Lexicon: baurzıĩ pending]`

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
- **Argument structure** — can the frame take nominal complements directly, or always mediated by a preposition? See §13 (The possession construction) for the *with*-mediation facts. **[Open]**

**Frame semantics with inanimate subjects [Provisional].** Casting an inanimate subject as an active framed verb is never neutral. The go-ahead frame reads inconvenience or fate ("it's going ahead and raining anyway"); the get-oneself frame reads unexpectedness ("it got itself to rain"). The unmarked option is impersonal — the language defaults inanimate predications to the existential particle *pons* "there is" (*pons rheĩ* "there is rain"; `language_reference.md`), reserving active framing for discourse effect. `[Placeholder: active-framing conlang forms pending elicitation]` Generalization beyond weather awaits data.

### 4.2 Concord

The main verb carries the lexical content and takes a **concord affix** — an ending showing concordance with the frame. Two shapes exist: **infinitive-shaped** and **progressive-shaped**. In the get-oneself paradigm the choice of shape selects the reading (§3.2); this is the most semantically loaded work concord does in the system.

The surface forms of the two principal endings are now tabulated by coda class in §4.2.2 (the B12 elicitation): the progressive-shaped concord is the suffix **/‑ıĩ/** (the committed form of the *-in* exemplified by *relaxin*), and the preterite/perfect family is a coronal **/‑ɾi ~ ‑t/** with a strong-verb class (§4.2.1). What remains open is the higher-order question of what concord marks *beyond* shape. **[Open: concord-affix surface inventory — what features does concord mark beyond the shape contrast (volition, frame aspect, person/number redundantly with the frame)? The surface shapes are settled (§4.2.2); the feature content is not.]**

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

> *Analytical note.* In the discovery example the passive shape is conflated with the separative satellite *oþw* (§13 Interactions; `terminology-registry.md`), because GA *split* has a zero-marked participle — all the visible material belongs to the satellite. Disambiguating the shape from the satellite needs a verb with overt participle morphology (a *got myself taken-* class form). **[Open: passive-shaped concord — confirm with an overt-participle stem]**

**Readings are compositional.** Translation data show that the reading a clause receives is not a property of a paradigm cell alone: it is the joint product of **frame aspect × concord shape × the stem's own event structure**, with the matrix particles (§11) available as a further scaffolding layer when the bare frame under-delivers. Three regularities recur:

1. The threshold reading tracks **prospectivity**, surfacing wherever the infinitive shape meets an effortful stem — including past cells (*Rimmaseto splitoþw* above).
2. Beginning-readings ("first noticing," onsets) are intrinsically **imperfect**: available only where the frame aspect supplies ongoing time, never from a perfective cell.
3. Stems whose GA source is lexically volitional resist the happenstance reading bare, and take the get-oneself frame only with scaffolding — a satellite supplying a befall-able event shape, or a matrix particle supplying the happenstance from above (*Enniip remmaseto split* "I ended up leaving").

The shape contrast shows on a fresh stem in the quotative *o* (§12): *Rimmaśeto o* "I finally said it" — infinitive-shaped, the effortful threshold reading, with the "finally" carried by the shape rather than a separate word — beside *Rimmaśe oę* "I was saying it (when…)" — progressive-shaped, speech caught mid-act (backdrop).

This is direct evidence on the concord term's standing question: the stem's event structure does grammatical work alongside the shape contrast. The term remains **[Provisional]** on exactly this point. **[Open: concord-affix surface inventory — unchanged; the compositional findings sharpen what the inventory must capture]**

#### 4.2.1 Irregular concord

A structurally significant class of verbs preserves GA irregular (strong-verb) morphology in the **preterite/perfect** slot where the regular derivation predicts the coronal increment: *meirtt* (from GA *made it*) where regular *meiktt* plus the infix is expected. Same stem, unexpected exponent — inherited irregularity, not suppletion (`terminology-registry.md`). The B12 elicitation (§4.2.2) shows this is not a handful but a structural class: *o* → *bentt* (went), *ospii* → *ospo* (spoke), *rhiib* → *rhob* (drove), *rib* → *reib* (gave), *split* → *split*, *meiktt* → *meirt* (made it). The regular coronal **/‑ɾi ~ ‑t/** is the productive default; strong forms are lexically listed and carried over wholesale from GA. (PROG, by contrast, is regular even on strong verbs — *rhob* but *rhiimm*.) `[Lexicon: meiktt / concord meirtt not yet entered]` **[Open: irregular-concord inventory — extend the strong-verb list as the dictionary grows]**

#### 4.2.2 Concord morphophonology — the coda-class paradigm **[Settled]**

The June 2026 **B12 elicitation** (battery: every verb lemma in `dictionary.md` plus the SAYING-round verbs) settles how the two principal concord increments dock onto the main verb. The single most important result: **the inflected surface form is predicted by the verb's GA source coda, not by its bare conlang citation form.** Two lemmas that fell together in the citation form split again under concord, and the split tracks the GA original. This supersedes the predictions of the B12 coda survey (held in `drafts/`), whose "a nasal increment docks onto the coda" model is here revised.

**The two increments.**
- **Progressive-shaped (PROG):** a vocalic suffix **/‑ıĩ/** ⟨ıĩ⟩ — GA *‑ing* /‑ɪŋ/ → colloquial *‑in'* → nasal vowel /ɪ̃/. (This is the surface form of the *‑in* placeholder of §4.2; the inventory the §4.2 flag asked for.)
- **Preterite / perfect / passive (PRET, the "‑ed family"):** a **coronal** — weak *‑ed* surfaces as a tap **/‑ɾi/** ⟨‑ri⟩ on vowel- and dental-final stems, and as plain **/‑t/** after sibilants and voiceless obstruents. A large class instead retains GA **strong-verb** morphology (§4.2.1).

**The mechanism — fossil resurrection, then re-lenition.** Because both increments are syllable-initial, they **re-syllabify the verb's etymological coda as an onset.** Codas the cascade deleted or weakened word-finally — *recruit* /t/ → *rhikriutt*, *click* /k/ → *kli*, *drive* /v/ → *rhiib* /b/ — reappear before the increment; and, now standing in onset position, they **re-enter the stratum-1 onset lenitions** (`phonology.md` §4.4.1–§4.4.2). The resurrected /k/ of *click* therefore does not surface as [k] but breathes to /h/ (k-breathing): *kli* → **klihıĩ** /kliˈhɪ̃/. Inflection is a synchronic window onto the GA coda, run a second time through the cascade — which is exactly why citation form under-determines the inflected form. This rule is formalized at `phonology.md` §4.4.14 (the fossil resurrection); the PROG /‑ıĩ/ and PRET /‑ɾi ~ ‑t/ exponents are registered there too.

**The coda-class paradigm.** PROG and PRET reflexes by conlang coda shape (representative members; the full battery is in the B12 study):

| Coda class | Lemma (GA source) | PROG | PRET | Behavior |
|---|---|---|---|---|
| Ṽ nasal-vowel | *rheĩ* (rain), *ǫ* (own) | *rheĩy*, *ǫıĩ* | *rheinn*, *ǫnn* | glide PROG; PRET surfaces the latent nasal as coda *‑nn* |
| V true-vowel | *eplii* (apply), *noë* (annoy) | *eplıĩy*, *noıĩ* | *eplii*, *noë* | bare /‑ıĩ/; PRET merges with citation (open coda, *‑d* elides) |
| V masks GA /k/ | *kli* (click), *ospii* (speak) | *klihıĩ*, *ospiihıĩ* | *klkt*, *ospo* (str.) | /k/ resurfaces → **breathes to /h/** before PROG |
| V masks GA /t/ | *rhikriutt* (recruit), *pot* (pout) | *rhikriuıĩ*, *poıĩ* | *rhikriuri*, *pori* | glottal/deleted /t/; PROG bare suffix, PRET tap **/‑ri/** |
| Db voiced stop | *rhiib* (drive), *rib* (give) | *rhiimm*, *rimm* | *rhob*, *reib* (str.) | /b/ → geminate nasal **/mː/** under PROG, suffix absorbed |
| Tp voiceless stop | *split* (split), *bęink* (panic) | *spliyıĩ*, *bęinkıĩ* | *split* (str.), *bęinkt* | stop kept; PROG suffix, PRET *‑t* (the ⟨y⟩ of *spliyıĩ* is an orthographic syllable-divider only) |
| Glt glottal | *nott* (note) | *noıĩ* | *nouri* | glottal = eroded /t/; PROG bare, PRET tap **/‑ri/** |
| S sibilant /s sː/ | *nouś* (notice), *pauyiis* (apologize) | *nouhıĩ*, *pauyiisıĩ* | *nouśt*, *pauyiist* | singleton /s/ **breathes to /h/** before PROG; geminate/cluster /sː/ resists (*þokssıĩ*); PRET *‑t* |
| Sh /ʃ/ | *ŕeush* (cherish) | *ŕeushıĩ* | *ŕeusht* | /ʃ/ kept; PROG suffix, PRET *‑t* |
| W /w̩/ (‑er) | *bekw* (bicker), *rhinnw* (wonder) | *bekrrıĩ*, *rhinzrrıĩ* | *bekw*, *rhinnw* | **linking-r returns** before PROG (→ /‑rːı̃/); PRET covert in citation, rhotic resurfaces intervocalically under further suffix (*bemmorret*) |
| W /w̩/ (‑le) | *barnkw* (barnacle) | *barnklm* | *barnklt* | **lateral returns** — not rhotacism (resolves the survey's open ‑le question) |

**Infixation — phrasal and object-incorporating stems.** Where the stem is a fused GA verb-plus-particle or verb-plus-object, the increment is **infixed at the root–particle seam**, not suffixed: PROG infixes the nasal **‑n‑**, PRET infixes the coronal **‑t‑**.

| Stem (GA) | PROG (‑n‑ infix) | PRET (‑t‑ infix) |
|---|---|---|
| *piquô* (pick out) | *piknô* | — |
| *beussou* (pass out) | *beussnou* | *beustou* |
| *baurzıĩ* (barge in) | *baurznıĩ* | *baurztıĩ* |
| *pikkp* (pick up) | *piknip* | *pikttp* |
| *toutw* (total to) | *tolntw* | *toultw* |
| *ŕequôþw* (check off) | *ŕeknôþw* | *ŕektôþw* |
| *þilnn* (fill in) | *þilnenn* | *þilðnn* (coronal voices to ð in the voiced environment) |
| *meiktt* (make **it**) | *meiknet* | *meirt* (str.) |
| *reut(to)* (get it / to) | *retnet(to)* | *riet(to)* (str.) |

The object pronoun *it* hosts the infix exactly as an incorporated particle does — confirming the §4.2.1 *piknib·orrô* alternation as a fully productive rule, not a one-off. The same intervocalic coda-resurfacing seen in the suffixing classes (*bemmorret* < *bemmw*) operates here too.

**Open edges** (everything tabulated above is **[Settled]**; these remain **[Open]**):
- **Db beyond labials** — /d g/ → /nː ŋː/ under PROG is predicted by symmetry but only labials (*rhiimm*, *rimm*) are attested.
- **‑le subclass** — *barnacle* is the sole ‑le datapoint; confirm lateral-return on a second ‑le verb.
- ***baŕep*** (< *prep*) — the lemma is now settled (prep-breaking, `phonology.md` §4.4.5); it ends in /p/ (a voiceless-stop-shaped stem), not the Db it was tentatively filed under. Residual: its PROG was logged *baŕetm* (a /‑tm/ appendix form) where a /p/-final stem might instead predict the /‑ıĩ/ suffix — minor, left **[Open]**.
- ***rhıĩ* (ring) PRET** — the B12 elicitation cell is corrupted (mis-paste); re-elicit.
- **Sibilant PROG conditioning** — singleton /s/ breathes (*nouhıĩ*) but geminate/cluster /sː/ does not (*þokssıĩ*); pin the boundary.

#### 4.2.3 Ideophones as predicates

An ideophone (§12; `ideophones.md`) is not confined to following the quotative verb — it can serve as the main predicate itself, taking a frame and concord exactly as a verb stem does. The dialect-speech ideophone *rekriiâ* verbalizes with concord *-km*:

> *Rhii riauset rekriiâkm nopiiem.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> 1PL get.oneself.IPFV chat.IDEO-CONCORD evening
> "We were chatting in the evening."

This is the productive bridge between the expressive layer and the verbal system; the class itself is described in `ideophones.md`. `[Lexicon: rekriiâ (ideophone), nopiiem "(in the) evening" (< *on the P.M.*) pending — dictionary batch D4]`

### 4.3 Worked example

> *e oheun relaxin* — `[Placeholder: main-verb surface form pending dictionary derivation]`
>
> 1SG    go.ahead.LVC.VOL.HAB    relax-CONCORD
> "I deliberately relax (as a habit)"

The frame *oheun* carries the volition and the frame aspect (habitual); the main verb carries the progressive-shaped concord. The pronoun and frame forms are attested (§2.4, §5.2); the main verb is a placeholder. For fuller assembled clauses, see §15 (A clause, assembled).

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
| 3SG | *ey* | *et* |
| 1PL | *rhii* | — |
| 2PL | *rhia* | — |
| 3PL | *eia* | — |

The 1SG form is irregular for its GA source (weak pronouns are always unstressed). 

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

*Ea* also marks **conditionals** — "if/whether … at all." The conditional brackets the clause with a fronted *ebıĩ* — the inverted "am I," the same subject-auxiliary inversion that forms a question — and a clause-final *ea*:

> *…ebıĩ ounoheun meiknet ea.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> be.1SG LVC.VOL.IPFV come-CONCORD Q
> "…whether (I) was coming."

This is **formally identical to a yes/no question** (*ebıĩ ounoheun meiknet ea* "am I going to make it at all?"), distinguished only by intonation — the interrogative carries the rising contour, the conditional does not. It applies to matrix-scaffolded clauses as to any other (§11). **[Provisional]**

**Clipped questions.** In the interrogative, recoverable material (the subject, the verb) may be dropped: *bǫëiio ea* "(want) coffee?" The same clipping is licensed inside quoted questions (§12.3).

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

A grammaticalized construction operating on **deverbal nominals** — a verb's action treated as a noun, the territory GA covers with the gerund (*the running*, *the eating*). It is one of the conlang's flagship grammatical innovations and is analyzed as the **deverbal special case of the possession construction** (§13): the frames engage the nominal exactly as they engage any noun, and what is special here is the nominal's own morphology and one piece of supporting syntax.

**[Status: demoted from the verbal system.]** This construction is no longer analyzed as a verbal-system feature in its own right. Its shared-knowledge/habitual meaning is the **possession construction** (§13) applied to a deverbal nominal, and its *þ ~ y* / *o* exponents are **nominal/determiner morphology**; the canonical treatment — with the fossilized *þ/o* determiner doublet and its grammaticalization — is moving to `language_reference.md`'s nominal sections. This section is held as a pointer pending that migration. See §17 for the decision record.

### 7.1 The two morphemes

The construction stacks the **recognitional marker** (REC, *þ ~ y*, from GA *the*: shared-knowledge type reference) and optionally the **iterative marker** (ITER, *-ś*, from plural *-s*: repeated instances) on a deverbal nominal; attested together in *þ rishś* "the dishes (you know the chore)." Glossing pattern: REC-stem-ITER. The canonical morphological description — forms, stacking, and the morphology-scoped open questions — is `language_reference.md` §3.2.1; this document holds what the construction does with the frames.

### 7.2 The frame meets the recognitional nominal

> *Rimmase ię þ rishś, a bayen, een een.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> 1SG.LVC.NVOL.PST do.CONCORD REC dish-ITER on 1SG.end again again
> "I got (myself) doing the dishes, on my end, again and again."

The frame combinatorics — which frame, which frame aspect, what the combination means — are the possession construction's (§13), and the habitual reading is compositional: recognitional type + iteration + frame engagement. Two features distinguish the deverbal case from a plain noun in the same construction:

1. **The recognitional exponent.** The deverbal nominal takes *þ ~ y* where a plain noun takes the merged article *o*.
2. **Helper-verb support.** On the get-oneself side the deverbal nominal requires a helper verb (*ię* above, from GA *doing*); on the go-ahead side, the grammaticalized *with*. A plain noun combines bare on the get-oneself side. The helper-verb system is deliberately open — see §13.

> *Analytical note.* This construction was previously analyzed as free-standing, with the *with*-mediation treated as its own complement pattern. The possession data reanalyzed it as a special case: the same frame-plus-nominal machinery covers plain nouns ("got myself a drink") and deverbal nominals ("got myself doing the dishes"), with the residue listed above blocking full reduction. The reasoning record lives in `phase4-triage-2026-06.md` §2.1 and the registry entry.

### 7.3 Not a definite article

Glossing the *the*-morpheme as DEF would be etymologically accurate but functionally misleading: the morpheme does not pick out a definite referent. It presupposes addressee familiarity with the *type*, not uniqueness of reference. **[Settled]**

A consequence for the noun system: GA's definite article has not survived as a definite article. Definite reference, where needed, is conveyed through other means (the visibility particles, possessives, context); that system is the responsibility of the language reference's nominal sections (`language_reference.md` §3.2, §3.7), not this document.

> *Origin.* GA *the* is an etymological doublet (→ article *o* and recognitional *þ ~ y*; the Latin *ille* parallel); as nominal-determiner history, its canonical home is now `language_reference.md` §3.2.2. The functional claim above — recognitional ≠ definite — is unaffected.

### 7.4 Open questions

The morphology-scoped questions (bare REC; ITER without REC; scope relative to other nominal morphology) live with the morphemes at `language_reference.md` §3.2.1. Construction-scoped questions are the possession construction's (§13.5).

---

## 8. Verbs and the verbal system

This section is the descriptive home for the lexicon-side facts that bear on which verbs participate richly in the verbal system. The procedural counterpart — the methodology for fleshing out the verb lexicon — lives in `language_reference.md` Appendix B and points back here.

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

The not-quite negator has a **reduced form *nokw*** (< *nocquii*) in fast and reportative speech, attested under the matrix particles (*reś et quo nokw rin riiy* "guess it's not running"; merged *resquo*); a deliberate **volitional** negation alternative is *skip* (declining outright), distinct from the not-quite shortfall. How *nokw* interacts with the matrix particles (§11.7), with concord, and with the air-quote gesture that can accompany it (a multimodal cue; `ideophones.md`) remains open. **[Open]**

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

A small class of particles places a whole clause inside a modal or evidential frame — that something merely *ended up* so, that the speaker *knows* it, *needs* it, *gathers* it to be so, or, summing up, that *in short* it is so. These are the **matrix particles** (informally, *scaffold particles*): each colors everything that follows it, and each sits at the front of its clause.

> *Enniip ounoheun splitn.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> MP.ENDUP.PST LVC.VOL.IPFV split-CONCORD
> "It ended up that (they) went ahead and left."

The class is defined **syntactically**, by two diagnostics: a matrix particle takes **clause scope** (it colors a whole clause, not one constituent) and a **fixed clause-initial position**. Membership does not turn on what the particle is made of — most members are eroded GA matrix clauses (*it ended up…, I know that…, what I need is…*), but at least one, the summary particle, descends from an adverbial phrase with no verb in it at all (§11.5).

Two further facts are worth holding onto. First, the class is the **home of the language's only surviving tense**: the verbal system otherwise runs on aspect, carried by the weak pronouns (§5.2), and the members descended from a finite GA clause carry a past/non-past contrast inherited from it — though, as the syntactic criterion implies, not every member does (the guess and summary particles are tenseless). Second, the particles are unmarked for **person** — *enniip* reports an outcome without saying whose.

### 11.1 Forms

| Member | Non-past | Past | GA source | Meaning |
|---|---|---|---|---|
| end-up particle | *enp* | *enniip* | *(it) end(ed) up …* | happenstance outcome |
| know-that particle | *no* | *nii* | *(I) know/knew (that) …* | knowledge, awareness |
| really-need particle | *rhi·iiniies* | *rhi·iiniir·ros* | *what I need(ed) is …* | desire; weak obligation |
| guess particle | *reś* | — *(tenseless)* | *I guess …* | indirect evidence: hearsay or inference |
| summary particle | *nóuśshè* | — *(tenseless)* | *in a nutshell …* | summation; "in short" |

The really-need particle has a reduplicated intensive, *rhi·ii·rhii·niies*, from GA *what I **really** need is …*. The guess particle is tenseless because its source, GA *I guess*, has converged in form with *I guessed* — there is no surface contrast left to carry tense (§11.5). `[Lexicon: all five members pending dictionary entries]`

### 11.2 Function

Among the three members that carry tense, the contrast is **privative**: the non-past member is unmarked and combines freely with habitual and future time adverbs, while the past member asserts a realized state of affairs. `[Placeholder: adverb-combination examples pending — "always end up …", "tomorrow, probably end up …" attested as judgments only]` The guess and summary particles have no such contrast (§11.1).

The really-need particle codes want and, more weakly, must:

> *Rhi·iiniies ounahen splitn.*
> /—/ `[Placeholder: IPA pending phonology pass; frame form spelling pending the §2.4 paradigm question]`
> MP.NEED LVC.VOL.HAB split-CONCORD
> "What I need is to leave."

The **guess particle** *reś* marks the clause as something the speaker holds at one remove — by hearsay or by inference, with no commitment to which (the source phrase *I guess* spans both, and so does the particle):

> *Reś beųheun split.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> MP.GUESS LVC.VOL split
> "Apparently (they) left."

The **summary particle** *nóuśshè* caps a clause as a summation — "in short," the conversational *insomma*:

> *Nóuśshè beųheun split.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> MP.SUMM LVC.VOL split
> "Long story short, (they) left."
>
> `[Placeholder: constructed example — *nóuśshè* is attested as a member (Translation Exercise #2); this particular clause has not been elicited and awaits confirmation.]`

### 11.3 Distribution

- **Position.** The matrix particle precedes the clause it scaffolds; a topic precedes the matrix particle: **topic particle > matrix particle > clause**.
- **Aspect government.** Each tensed particle lexically specifies whether the scaffolded clause keeps its own aspect. The end-up particle forces the imperfect — the clause surrenders its aspect (*Beųheun split* "went ahead and left," but *Enniip **ounoheun** splitn*, with the imperfect frame). The know-that particle imposes nothing: *No ei beųheun split* "I know that they went ahead and left." The government of the guess and summary particles is not yet surveyed (§11.7). **[Open]**
- **Person.** Unmarked throughout. Ambiguity is resolved, when needed, by a strong-pronoun *on-X-end* phrase (§5.3), with flexible placement.
- **Stacking.** Matrix particles stack over each other and under topics, but parseability demands strong-pronoun buffering between the layers; speakers avoid depth beyond two. Attested at depth two: *Resquo enniip ounohen splitm oðerren* "I heard she ended up leaving," where the guess particle (merged with the quotation marker *quo*, see *Quotation*) scaffolds over the end-up particle, and the strong pronoun *oðerren* buffers the join. **[Provisional]**
- **Questions.** The polarity-question particle *ea* applies to a scaffolded clause as to any other (§5.5). `[Placeholder: example pending]`
- **Negation.** Interaction with the negators of §10 is undecided; the reduced negator *nokw* and the merged *resquo* are the first data (§11.7). **[Open]**

### 11.4 Interactions

- **With the visibility particles.** The know-that particle is homophonous with the know-particle but syntactically distinct: matrix *no* takes a noun phrase or a full clause and yields a complete sentence; the topic particle's clausal form *noho* instead raises a topic the listener expects elaborated. The two can co-occur (*No Báuyà, no Báuyà* — topic, then assertion).
- **With the frames.** The end-up particle supplies happenstance from above when the bare get-oneself frame under-delivers it (§4.2): *Enniip remmaseto split* "I ended up leaving."
- **With the evidential division of labor.** Under the **guess particle**, the choice of visibility particle distinguishes perceptible from non-perceptible evidence: *Hiie ossii, reś aų nibii hii* "Look at the outside — it looks nippy" versus *Nou ossii, reś aų nibii hii* "You know the outside — it seems nippy." A personal or quoted source is added instead with the quotation marker *quo*, which fuses with *reś* → *resquo* (see *Quotation*).
- **With mood.** The really-need particle carries the desiderative territory §14 anticipates; the guess and know-that particles carry evidential territory.

### 11.5 Origin

Most members fuse a GA matrix clause — finite verb included — into a single particle: *it ended up*, *I know that*, *what I need is*. That shared source is why the class is named for the *matrix* clause and why several members bear tense — the finite verb brought its past/non-past contrast along. But the source is a **correlate, not the membership criterion** (§11): the summary particle *nóuśshè* descends from the verbless adverbial *in a nutshell* yet behaves exactly like the others — clause-scoping and clause-initial — which is what shows the class to be held together by syntax rather than by etymology. The guess particle *reś* is the revealing intermediate case: it comes from a finite clause (*I guess*) but is tenseless, because *I guess* and *I guessed* erode to the same form, leaving no contrast to inherit.

The grammaticalization path is well-attested cross-linguistically. Latin American Spanish *dizque* (from *dice que* "says that") is a matrix verb fused with its complementizer into a hearsay particle — a close parallel to the guess particle, which covers the same hearsay-and-inference territory. The person syncretism follows from phonetic erosion at the pronominal slot: in *what I need is*, the GA pronouns */i, jɪ, ɛj, ɻi/* merge acoustically after /ɻ/ and before /iː/. The end-up particle's aspect government recalls the conjunct order of Algonquian languages such as Ojibwe, where a subordinating element selects a dedicated dependent verb form.

### 11.6 Glossing

Composite tags: `MP.ENDUP`, `MP.KNOW`, `MP.NEED`, `MP.GUESS`, `MP.SUMM`, with `.PST` on the past member of the three tensed particles (`MP.ENDUP.PST` = *enniip*). The guess and summary particles take no `.PST`.

### 11.7 Open questions

Each probe below is a **designed test item, not attested data** — a sentence whose acceptability or reading would settle the question.

- **Government class per particle.** Each matrix particle either forces an aspect on the clause it scaffolds (as the end-up particle forces the imperfect) or leaves the clause's own aspect intact (as the know-that particle does). Which behavior the really-need, guess, and summary particles show is unsurveyed. *Probe:* place a particle over the same clause in two aspects and see whether both survive — *Reś beųheun split* "guess she left" beside *Reś ounoheun splitn* "guess she's leaving"; if both stand with their aspect intact, *reś* governs nothing, unlike *enniip*, which forces the imperfect. **[Open]**
- **Negation interaction.** How the negators of §10 combine with a matrix particle is undecided: whether a negator can scope the particle itself ("it is not the case that one gathers…") or only the clause beneath it, and how the reduced negator *nokw* and the merged *resquo* behave. *Probe:* negate inside and, if possible, outside the scaffold — *Reś nokw rin riiy* "guess it doesn't run" (negation under the particle) against any form that denies the gathering itself; whichever is grammatical fixes the scope. **[Open]**
- **Stacking depth and ordering.** Matrix particles stack, buffered by strong pronouns (§11.3), but the maximum depth and whether the order is fixed are open. *Probe:* reverse an attested two-particle stack and push to three — beside attested *Resquo enniip … oðerren* "I heard she ended up leaving," test *enniip resquo …* for a meaning difference, and add a third particle to find where parseability breaks. **[Open]**
- **The summary particle's distribution.** Whether *nóuśshè* governs the aspect of its clause, and whether (and where) it stacks — in particular whether "in short" must sit outermost, summarizing a clause another particle has already scaffolded. *Probe:* *Nóuśshè enniip …* "long story short, she ended up…" — test whether the summary particle can sit above the end-up particle while the end-up's imperfect government still reaches the verb. **[Open]**

---

## 12. Quotation

The language has no lexical verb "say." Reported speech, thought, and stance all run on a single quotative verb, *o* (< GA *go*), which takes its content after it — either the quoted material itself or, when nothing is quoted, an obligatory ideophone that carries the manner. Whether a quote is **direct** or **indirect** is signalled by particle choice, not by a complementizer.

> *Ei o nóè.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> 3SG QUOT "no.way"
> "She was like, 'No way.'"

### 12.1 Forms

The construction has one verb and three optional markers:

| Element | Form | GA source | Role |
|---|---|---|---|
| quotative verb | *o* (perfect *rhentt*) | *go* (*went*) | the "say/be-like" verb; intransitive |
| source marker | *quo* | *quote* | marks a personal/quoted source |
| opener | *o* | *oh* | opens a stretch of reported speech |
| direct-question marker | *ohei* | *oh hey* | marks a quoted question |

The perfect of the verb is suppletive-looking *rhentt* (< GA *went*), used for completed speech acts. `[Lexicon: o, quo, ohei, rhentt pending dictionary entries — batch D4]`

> *Beunheumm rhentt, rhemmemmêm.*
> /—/ `[Placeholder: IPA pending phonology pass; the *an'+went* → *-mm* gemination in *beunheumm* is a pending phonology item]`
> 1SG.VOL say.PRF, IDEO
> "I said it — [boom-boom-boom]."

### 12.2 Function

**Direct vs indirect is carried by the particles.** An indirect report needs nothing but the source marker *quo*; the embedded clause keeps its own shape and there is no quote boundary:

> *Eia quo ounoheun meiknet.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> 3SG QUO LVC.VOL.IPFV come-CONCORD
> "She said she'd come."

A **direct** quote is set off by a clause-initial *quo* plus the opener *o*, and the quoted material is reproduced verbatim — including its own first person:

> *Bentt oðerren quo, o mau ouhen meiktt.*
> /—/ `[Placeholder: IPA pending phonology pass; *bentt* frame morphology pending]`
> say.PST 3SG.STR QUO, Q.OPEN 1SG LVC.VOL.HAB come-CONCORD
> "She was like, 'I'll come.'"

**Quote-oneself: stance with nothing uttered.** Turning *quo* on one's own thought reports an internal reaction that was never spoken aloud. The left-dislocated strong pronoun reads as taking a conversational turn:

> *Bauyen, e o quo "þiiaii".*
> /—/ `[Placeholder: IPA pending phonology pass]`
> 1SG.STR, 1SG QUOT QUO "finally"
> "Me, I was like, 'Finally!'"

This works cleanly only in the **first person**: a speaker can quote their own unspoken thought, but reporting someone *else's* unspoken reaction this way fails, and the adverbs *eńhii* "internally" and *rhiþoupii* (< GA *without a peep*) step in instead. **[Provisional]** *(The internal-thought use overlaps the quotable-thought territory of cognition verbs — to be treated when that domain is worked.)*

### 12.3 Distribution

- **Position of *quo*.** *quo* precedes the salient part of the quote, and its placement is meaningful — moved earlier or later it shifts which span is foregrounded and can color the report with speaker doubt. **[Provisional — fine semantics want more data]**
- **Clipped questions.** A quoted question may be clipped (subjectless), licensed by the interrogative just as elsewhere (§5.5), and marked by *ohei*:

> *Ei o, ohei meikntt ea.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> 3SG QUOT, Q.DIR come-CONCORD Q
> "She went, 'Coming?'"

### 12.4 Interactions

- **Split TAM (confirmation).** The quotative confirms the language's division of labor: aspect is hosted on the weak pronoun (*ei*, *e*), while *o* stays the bare lexical verb — exactly the aspect-on-pronoun pattern of §5.2. The quotative carries no tense or aspect of its own.
- **With the matrix particles.** After the guess particle, *quo* fuses with *reś* → *resquo*, layering a personal/quoted source onto indirect evidence (§11.3–§11.4): *Resquo enniip ounohen splitm oðerren* "I heard she ended up leaving."
- **With the ideophone layer.** When *o* introduces no quoted content — the bare "say it / blurt it" use — the slot after it is filled obligatorily by an **ideophone** characterizing the manner of the act (as in §12.1's *rhemmemmêm*). The ideophone class, its phonotactics, and its co-speech gesture are described in `ideophones.md`.
- **With the strong pronouns.** A left-dislocated strong pronoun (*bauyen*, *oðerren*) frames a quote as a conversational turn or sets up a direct report (§5.3).
- **The three *o*'s.** Quotative *o* (< *go*), the opener *o* (< *oh*), and the referential article *o* (< merged *the/a*) are distinct lexemes that have fallen together in form; context and position keep them apart.

### 12.5 Origin

The construction is the conlang's reflex of the colloquial GA *be like / go* quotative. Of the GA competitors, ***go* won and *be all* did not survive**: the quotative verb is *o* (< *go*), with perfect *rhentt* (< *went*). The markers come from discourse routines frozen into particles — *quo* from *quote*, the opener *o* from *oh*, *ohei* from *oh hey*. That a language should build its reported-speech system out of *go* and *oh* rather than a verb of saying is itself the GA inheritance: the colloquial register, not the formal *say*, is what grammaticalized.

### 12.6 Glossing

Tags: `QUOT` (the verb *o*; perfect `QUOT.PRF` ~ *say.PRF*), `QUO` (*quo*), `Q.OPEN` (opener *o*), `Q.DIR` (*ohei*). Quoted material is wrapped in double quotes in both the surface line and the gloss line, so the quote boundary is visible in the interlinear.

### 12.7 Open questions

- The *talk/speak* register split — whether *ospii* (< *speak*) and the *o*-plus-ideophone strategy divide by formality — is unresolved on a weak diagnostic. **[Open — round 3]**
- Whether quote-oneself's first-person restriction is absolute, and how it relates to cognition-verb reported thought. **[Open]**
- The fine semantics of *quo*-position (salience vs doubt). **[Open]**

---

## 13. The possession construction

The language has no everyday verb *have*. Possession, acquisition, choosing, and giving are carried by the frames combining directly with a nominal — the **possession construction**. What GA spreads across *have*, *get*, *pick*, and *give*, the conlang derives from frame choice and frame aspect over a bare noun.

> *Rimmaseu beikw.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> 1SG.LVC.NVOL.PST=ART vehicle
> "I have a vehicle." (lit. "got myself a vehicle")

The final lengthened vowel of *rimmaseu* is the fused etymological article. `[Placeholder: gloss segmentation of the article fusion pending]`

### 13.1 Forms and function

- **get-oneself + nominal, perfect frame aspect** → possession ("have"): *Rimmaseu beikw*.
- **get-oneself + nominal, imperfect frame aspect** → acquisition in progress ("getting"). `[Placeholder: example pending]`
- **go-ahead (+ *with*) + nominal** → deliberate selection ("picking and choosing"). `[Placeholder: plain-noun example pending; the deverbal case is attested at §7.2]`
- The frame choice carries the usual coloring: *Rimmaseu rhink* "got myself a drink" reads self-benefit; *Rimmaseu þlii* "got the flu" reads affliction — the same construction, with the nominal's semantics selecting the flavor.
- **Lexical alternatives** modulate intentionality: *rib* "give" for explicit volition in transfer; *ǫıĩ* "own" for neutral mere-having. `[Lexicon: rib, ǫıĩ not yet entered]`

### 13.2 The transfer extension

With a recipient in the *get*-slot, the construction causativizes into giving, volition-neutral by default:

> *Ritm o rhémstwè.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> get.3PL ART book
> "(I/they) gave them the book." (lit. "got them the book")

The extension resists a topic-marked definite object; explicit-volition *rib* with the go-ahead frame is used instead. **[Open: transfer-extension object restrictions]**

**Abstract possessa: informing.** The transfer pattern reaches beyond handing over objects to causing someone to come to possess *information*. The verb *þilnn* (< GA *fill in*) "fill (someone) in, inform" instantiates it with an abstract possessum: the recipient and the thing told agglutinate in sequence onto the perfective stem.

> *Beunheun þil·tm·ę·aų·et, o riųś.*
> /—/ `[Placeholder: IPA pending phonology pass]`
> LVC.VOL fill.in-PFV-3PL-on-3SG, ART news
> "I told her the news." (lit. "went ahead and filled 'em in on it — the news")
>
> `[Placeholder: fine segmentation of *þil·tm·ę·aų·et* — *þil* fill, *-tm* perfective, *-ę* recipient ('em), *-aų* "on," *-et* theme ('it') — pending confirmation]`

The go-ahead frame matches the deliberateness of informing. The same **definite-object restriction** seen above recurs on the abstract possessum: definite *riųś* "the news" does not occupy the theme slot — that is filled by the clitic *-et* "it" — and the possessum is supplied separately, as an appended clarification. A second attestation of the constraint, now on an abstract possessum, strengthens it. **[Open]** `[Lexicon: þilnn pending — senses: inform / replace-substitute / intransitive "read the room"; dictionary batch D4]`

### 13.3 The deverbal special case and the helper-verb question

A deverbal nominal in the construction is the recognitional-iterative nominal of §7, distinguished by the recognitional exponent (*þ ~ y* for merged *o*) and by **helper-verb support** on the get-oneself side (*Rimmase ię þ rishś* — §7.2).

**The helper-verb question is deliberately open.** *Do* is the default helper, but GA's own collocations vary by lexical item (*do* the dishes, but *take out* the trash, *pull* the trigger, *push* the issue), and importing that variety wholesale would both drift toward relexification and nest light verbs inside the already-grammaticalized frames. The working disposition, **[Open]** in all four parts:

1. A **small licensed set** of helper-verb pairings, admitted only where the lexical item earns it.
2. **Default avoidance**: most such meanings are phrased another way — Latinate verbs in particular tend to supply frame-free lexical routes (*baŕep* "cook" rather than a do-the-cooking construction).
3. A **tentative additional helper** under consideration (candidate source GA *bop*), unconfirmed.
4. Some deverbal nominals may simply be **incompatible** with the get-oneself frame — a gap, not a workaround.

> *Analytical note.* A related lexical decision is recorded here because it bears on the helper's eventual citation shape: GA *do* is assigned an **irregular** sound-change path, yielding *o* rather than the regular reflex in ⟨ii⟩ — merging with the descendant of GA *go*, which already covers "become" and is expected to extend to motion and speech senses. The default helper, the become-verb, and the merged article would then share the surface form *o*; the collision load on *o* is flagged for review, and the attested concord form *ię* (from GA *doing*) must be reconciled with the merger. `[New rule needed: irregular reflex of GA *do* → o (designed exception)]` `[Lexicon: o (do/go merger) pending — senses: do-helper, become, go]`

### 13.4 Interactions

- **With the recognitional-iterative nominal** (§7): the deverbal special case, above.
- **With the frame's argument structure** (§4.1): the *with*-mediation facts live here; §4.1's open question is fed, not closed.
- **With the separative satellite** *oþw* (§4.2): unrelated mechanisms — the satellite shapes the verb's event structure; the helper supports a nominal.

### 13.5 Open questions

- Helper-verb ecology — the four-part disposition of §13.3. **[Open]**
- Transfer-extension object restrictions — the definite-possessum displacement, now attested for both concrete (*rhémstwè*) and abstract (*þilnn*, *riųś*) possessa. **[Open]**
- The *bop* helper candidate. **[Open]**
- The imperfect-aspect acquisition reading — confirm with attested examples. **[Open]**

---

## 14. Mood

Beyond the go-ahead/get-oneself contrast (which arguably is mood), the system likely includes:

- **Imperative** — formation and inventory not yet committed. **[Open]**
- **Optative / desiderative** — the desiderative territory is carried by the really-need particle (§11); whether a separate *want to*-derived optative also exists is **[Open]**.
- **Evidential distinctions** — partly carried at the matrix layer (the appears and know-that particles, with the visibility particles dividing perceptible from non-perceptible evidence — §11.4); whether further evidential machinery exists is **[Open]**.

These are placeholders for sections that will be developed as design proceeds.

---

## 15. A clause, assembled

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

## 16. Cross-references

- `terminology-registry.md` — canonical terminology, gloss tags, and naming history.
- `verb-paradigm-verdict.md` — full cell-by-cell predictions, the three live questions on self-benefit selectivity / threshold-for-statives / habitual-plus-infinitive reading, and the analytical history behind this consolidation.
- `translation-frequency-task.md` — the translation-task instrument designed to gather the usage-weighted data §9 calls for.
- `language_reference.md` §3.4 — the high-level summary that points at this document.
- `phonology.md` — phonological details of the frame and verb-stem forms.
- `language_reference.md` Appendix B — the verb-lexicon-building methodology (folded out of this document, June 2026).

---

## 17. Versioning notes

### v2.10, June 2026 — Appendix A (verb-lexicon methodology) folded out to language_reference Appendix B

The verb-lexicon-building methodology, held here as Appendix A since v1.2, is relocated to `language_reference.md` as its **Appendix B** — part of the project-wide consolidation of conlanging-process/methodology material into that document's design appendices (`language_reference.md` v3.8). The recipe is moved intact (rebased A.→B.); its bare in-document `§N` references (to §3/§6/§7/§8/§9/§10 here) are filename-qualified in the new home. The genre principle is unchanged — methodology still lives in an appendix, not the descriptive body; only its host document changed, so the cross-cutting design appendix could hold all process material in one place. In-document pointers updated: §8's procedural-counterpart sentence and the §16 cross-reference bullet now point at `language_reference.md` Appendix B. No descriptive section changed or renumbered; §16 and §17 unaffected in numbering.

### v2.9, June 2026 — concord morphophonology settled (B12 elicitation)

§4.2.2 rewritten from a stub into the **coda-class paradigm**: the B12 elicitation (`drafts/translation_exercise_2/verb-coda-morpho-phon-study.xlsx`) settles the surface morphophonology of the two principal concord increments. Key results recorded: (1) the inflected form is predicted by the **GA source coda**, not the bare citation form, via **fossil resurrection + onset re-lenition** — the increment re-syllabifies the etymological coda as an onset, which re-runs the stratum-1 lenitions (*click* → *kli* → *klihıĩ*, the /k/ breathing); (2) **PROG = suffix /‑ıĩ/**, **PRET = coronal /‑ɾi ~ ‑t/** with a strong-verb class; (3) **infixation** of ‑n‑ (PROG) / ‑t‑ (PRET) at the root–particle seam for phrasal and object-incorporating stems (*beussou* → *beussnou*/*beustou*, *meiktt* → *meiknet*); (4) the ‑le subclass returns its **lateral** (*barnkw* → *barnklm*), not a rhotic. Attested classes promoted to **[Settled]**; residual gaps (Db beyond labials, ‑le beyond *barnacle*, *preb* PROG, *rhıĩ* PRET, sibilant-PROG conditioning) left **[Open]**. §4.2.1 upgraded from "small set" to a structural strong-verb class (*bentt, ospo, rhob, reib, split, meirt*). §4.2 intro flag narrowed: surface shapes now settled, feature content still open. This supersedes the B12 coda-survey predictions (revising its "nasal increment docks onto the coda" model). **Propagation completed same session:** `phonology.md` v4.5 (new §4.4.14 "the fossil resurrection" family; the re-syllabification → onset-lenition rule + PROG/PRET exponents; *apply* gemination reanalyzed → "labial gemination" [unattested]); `orthography.md` v3.9 (`pp` now predicted-but-unattested); `language_reference.md` v3.7 (§7 concord-surface-forms question closed). All six dictionary corrections applied (*eplii*, *reut/reutto* note, *rhikriutt* glottal coda, *bényǫ* noun-only, *ospokwþ* already under *ospii*); the sixth, ***preb* → *baŕep***, resolved via the new **prep-breaking** rule (`phonology.md` v4.6), which also standardized the *promise*/*process* onsets (see `dictionary.md` 2026-06-23).

### v2.8, June 2026 — §7.3 Origin reduced to pointer (Session L, SAYING round)

§7.3's etymological-doublet Origin (the GA *the* doublet; the Latin *ille* parallel) relocated to its canonical nominal-determiner home, `language_reference.md` §3.2.2 (Session L); §7.3 retains the functional recognitional ≠ definite claim plus a pointer. Part of the round-2 REC/ITER demotion (`phase4-triage-saying-2026-06.md` §2.3).

### v2.7, June 2026 — frame colorings, ideophone predicates, conditional, negation flag (Session V, SAYING round)

Batch from `phase4-triage-saying-2026-06.md`: **§3.3** the malefactive flip of the get-oneself benefactive [Provisional]; **§4.1** inanimate-subject framing is non-neutral, with the existential *pons* as the unmarked default [Provisional]; **§4.2** the concord-shape contrast exemplified on the quotative stem (*Rimmaśeto o* / *Rimmaśe oę*), plus new **§4.2.3 Ideophones as predicates** (ideophones verbalize with frame + concord, *rekriiâkm*; → `ideophones.md`); **§5.5** the *ebıĩ … ea* conditional filled in (inverted "am I," formally identical to the yes/no question, split by intonation) and clipped questions added — resolving the §12.3 forward-reference; **§7** demotion status note (the recognitional-iterative construction is no longer a verbal-system feature — round-2 decision, `…saying-2026-06.md` §2.3; full relocation to `language_reference.md` nominal/determiner morphology pending Session L); **§10** the reduced not-quite negator *nokw* (< *nocquii*) and volitional *skip* parked [Open]. `[Lexicon: baurzıĩ, pons, rekriiâ, nopiem, ebıĩ, nokw, skip pending — dictionary batch D4]`

### v2.6, June 2026 — §11 open questions detailed (Session V, SAYING round)

§11.7 expanded: each open question now states what is at issue and sketches a **designed probe sentence** that would settle it (per-particle aspect government; matrix-particle negation scope; stacking depth and ordering; the summary particle's distribution). The bare cross-document "battery" labels (B4–B6) were removed from §11.3/§11.7 body prose in favor of self-contained phrasing; that tracking lives in `phase4-triage-saying-2026-06.md` §6.

### v2.5, June 2026 — possession: abstract-possessum transfer (Session V, SAYING round)

§13.2 extended: the transfer/give pattern reaches **abstract possessa** — *þilnn* (< *fill in*) "inform," with the recipient and theme agglutinated onto the perfective stem (*þil·tm·ę·aų·et* "filled 'em in on it"; *-tm* PFV, *-ę* recipient, *-aų* "on," *-et* theme). The **definite-object restriction recurs** on the abstract possessum — definite *riųś* "the news" is displaced from the theme slot to an appended clarification — a second attestation that sharpens the §13.5 open question (now spanning concrete and abstract possessa). Source: `phase4-triage-saying-2026-06.md` §1.1/§3.7. `[Lexicon: þilnn pending — dictionary batch D4]`

### v2.4, June 2026 — Quotation section added (Session V, SAYING round)

New **§12 Quotation** (`phase4-triage-saying-2026-06.md` §1.1/§1.3/§1.5; registry v1.6). The colloquial-quotative construction: the quotative verb *o* (< *go*; perfect *rhentt*), with direct vs indirect carried by particle choice — *quo* (source), the opener *o* (< *oh*), *ohei* (< *oh hey*, direct question); GA *be all* does not survive. Quote-oneself (first-person internal stance) **[Provisional]**; clipped quoted questions; the split-TAM confirmation (aspect on the weak pronoun, *o* the bare verb); *resquo* fusion with the guess particle; the obligatory-ideophone tie forward-referenced to `ideophones.md`; the three-*o* homophony. Glossing convention: quoted material wrapped in double quotes in both surface and gloss lines. **Renumbering:** former §12–§16 → §13–§17 (possession §13, mood §14, a-clause-assembled §15, cross-references §16, versioning §17); in-document cross-references swept, and `language_reference.md` (§3.4 doc list and verbal-system cross-refs) and `terminology-registry.md` (possession and recognitional-iterative homes; quotation entries pinned to §12) updated. The §11 named "Quotation" cross-references now resolve to §12. `[Lexicon: o, quo, ohei, rhentt, nóè, þiiaii, eńhii, rhiþoupii pending — dictionary batch D4]`

### v2.3, June 2026 — matrix-particle criterion revised (Session V, SAYING round)

§11 rewritten from the SAYING translation round (`phase4-triage-saying-2026-06.md` §2.1–2.2; registry v1.6). **Membership criterion** changed from "the etymon contains a finite verb" to two **syntactic** diagnostics — clause scope and fixed clause-initial position — with the finite-verb source demoted to an origin correlate that explains which members bear tense. **Members:** added the **guess particle** *reś* (general indirect evidential — hearsay and inference; tenseless) and the **summary particle** *nóuśshè* (< *in a nutshell*; verbless etymon, the criterion's vindication); the **appears particle** *piies* **retired**, superseded by *reś* — closing the former §11.7 "*piies* past form" open question and the predicted-reportative question by deletion. The seem/look division of labor *piies* held is reassigned to *reś* + visibility-particle choice (§11.4); personal source via *quo*/*resquo*. The §1 Overview sentence and §11.6 gloss tags updated (`MP.APPEAR` → `MP.GUESS`/`MP.SUMM`); split-TAM framing narrowed (tense is a member sub-property, not a class trait — the class remains the home of the language's only surviving tense). Header version reconciled (was lagging at v2.1 while §16 carried a v2.2 note). **Forward reference:** *quo*/*resquo* point to a Quotation section to be added later in Session V; until then the cross-reference is named, not numbered. `[Lexicon: reś, nóuśshè, quo pending — dictionary batch D4-D]`

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
