# Terminology Registry

**Version:** v1.7 (June 2026)
**Status:** Canonical registry of the conlang's descriptive terminology. Maintained under `skills/reference-grammar-section-drafting-and-integration.md` §1.7. Prose in the reference documents must match the canonical terms here; this file is also the home for term history, so rejected alternatives never need to be re-litigated in body prose.

---

## 1. Rules of use

1. **One name per concept.** Body prose uses the canonical term exactly. Double-naming ("gnomic/habitual", "non-volitive ~ modulated") is a defect in new prose.
2. **Lean descriptive and long.** Spelled-out, self-explanatory terms are preferred over short opaque ones, even at the cost of wordiness. Opaque abbreviations (PH, PS, AB, INC, LVC.TAM) do not appear in body prose.
3. **Shorthands are licensed, not default.** A registered shorthand (e.g., *go-ahead*) may be used after the full term has appeared in the section.
4. **Gloss lines are a separate channel.** Interlinear glosses use the compact gloss tags registered here, per Leipzig convention. A gloss tag without a registry entry is a defect.
5. **New terms enter here first.** A draft proposing a term adds a `[Proposed]` entry; the user promotes or rejects it. Renames are executed registry-first, then swept through documents opportunistically.
6. **Statuses:** **[Settled]** — committed, in force. **[Provisional]** — in force, expected to hold, revisable when a named open question settles. **[Settled]** (accepted June 2026) — drafted by a session, awaiting the user's verdict. **[Retired]** — must not appear in new prose; listed in §6 so it is recognized in old text.

Entry schema: **Term** (canonical, full) · Shorthand · Gloss tag · Plain-language definition · Status · Canonical home · History & alternatives.

---

## 2. The verbal system

### Volitional go-ahead
- **Shorthand:** *go-ahead* (as in "the go-ahead frame", "go-ahead paradigm").
- **Gloss tag:** VOL.
- **Definition:** The paradigm side framing the event as deliberately undertaken by the subject. Grammaticalized from GA *go ahead and-*.
- **Status:** **[Settled]** (user decision, June 2026).
- **Canonical home:** `verbal-system.md` §2.
- **History & alternatives:** *volitive* (May 2026 term; retired in favor of the spelled-out, source-anchored form). The GA-source name is deliberately part of the term: it is the most intuitive handle for a general reader.

### Non-volitional get-oneself
- **Shorthand:** *get-oneself*.
- **Gloss tag:** NVOL.
- **Definition:** The paradigm side framing the subject's relationship to the event as qualified in some way other than straightforward agency; hosts the four readings (§ below). Grammaticalized from GA *get oneself-*.
- **Status:** **[Settled]** (user decision, June 2026).
- **Canonical home:** `verbal-system.md` §3.
- **History & alternatives:** *involitive* (rejected: privative name for the structurally richer side) → *modulated* (positive but opaque) → *non-volitive* (readable but clipped) → current form. The principled-asymmetry argument lives in `verbal-system.md` §8 prose, not in the term.

### Frame
- **Shorthand:** — (already short).
- **Gloss tag:** none (glosses name the specific frame: VOL / NVOL).
- **Definition:** The grammaticalized auxiliary unit that places the event in an attitudinal context: the go-ahead frame or the get-oneself frame. Carries volition, frame aspect, and (defective) person/number agreement.
- **Status:** **[Settled]** (accepted June 2026) — promote *frame* from informal synonym to the primary prose term, with *light verb complex* retained as the technical term for morphological discussion.
- **Canonical home:** `verbal-system.md` §4.
- **History & alternatives:** *light verb complex (LVC)* was the primary term (May 2026). It remains correct and is kept for morphology-internal prose; *frame* is more transparent for everything else, and the user has endorsed the source-anchored style it enables ("the go-ahead frame").

### Light verb complex
- **Shorthand:** LVC (gloss lines and morphology-internal prose only).
- **Gloss tag:** LVC (within composite tags, e.g., `LVC.VOL.HAB`).
- **Definition:** The technical name for the frame as a morphological object — the fused auxiliary cluster derived from the GA periphrases.
- **Status:** **[Settled]**, with prose preference shifting to *frame* (see previous entry).
- **Canonical home:** `verbal-system.md` §4.

### Frame aspect
- **Shorthand:** —.
- **Gloss tag:** the cell name (HAB, PROG, PST, PRF) within the composite frame tag.
- **Definition:** The tense/aspect cell carried by the frame: habitual, progressive, past, or (get-oneself only) perfect.
- **Status:** **[Settled]** (accepted June 2026) — replaces *LVC.TAM* in prose.
- **Canonical home:** `verbal-system.md` §2–3.
- **History & alternatives:** *LVC.TAM* (retired from prose: opaque acronym stack, and "TAM" is half-misleading — mood lives in the volition axis, not in these cells). The composite gloss notation (`LVC.VOL.HAB`) is unaffected.

### Habitual (frame aspect cell)
- **Gloss tag:** HAB.
- **Definition:** The frame aspect cell covering habitual and timeless/general statements.
- **Status:** **[Settled]** (accepted June 2026) — single name; the double-name *gnomic/habitual* is dropped, with "covers timeless/general statements" carried in the definition instead.
- **Canonical home:** `verbal-system.md` §2.4, §3.7.
- **History & alternatives:** *gnomic/habitual* (paradigm tables, May 2026). *Gnomic* alone rejected as jargon. Collision with the nominal "habitual marker" is resolved by renaming the latter (see *iterative marker*).

### Reading (of the get-oneself frame)
- **Shorthand:** —.
- **Gloss tag:** none (the individual readings carry tags).
- **Definition:** One of the four meanings hosted by the productive cells of the get-oneself paradigm, selected by the combination of frame aspect and concord shape.
- **Status:** **[Settled]** (accepted June 2026) — *reading* as the primary class term in prose ("the four readings of the get-oneself frame"), with *sub-modality* retained as the technical synonym where the paradigm-structural angle matters.
- **Canonical home:** `verbal-system.md` §3.3.
- **History & alternatives:** *sub-modality* (May 2026, kept as technical synonym); *modulation cell* (orphaned by the *modulated* → *non-volitive* rename; retired).

### Happenstance reading
- **Shorthand:** *happenstance*.
- **Gloss tag:** HAP.
- **Definition:** The subject finds themselves doing the verb without agency or effort — things that simply befall the subject. The default reading of the get-oneself frame. Hosted by habitual + progressive-shaped concord and past + progressive-shaped concord.
- **Status:** **[Settled]** (accepted June 2026) (rename of prose term; semantics unchanged).
- **Canonical home:** `verbal-system.md` §3.3.
- **History & alternatives:** *PH / pure happenstance* (May 2026). The name was already the best of the four; the change is dropping the opaque abbreviation from prose and registering a transparent gloss tag.

### Effortful self-benefit reading
- **Shorthand:** *self-benefit*.
- **Gloss tag:** SELF.BEN.
- **Definition:** The subject brought the event about on their own behalf, with effort; carries effortful and evaluative coloring (it took work; it served the subject). Inherits the dative-of-interest force of GA *myself*. Hosted by habitual + infinitive-shaped concord (marked) and past + infinitive-shaped concord.
- **Status:** **[Settled]** (accepted June 2026).
- **Canonical home:** `verbal-system.md` §3.3.
- **History & alternatives:** *AB / auto-benefactive* (May 2026). *Auto-benefactive* is retained as the typological synonym for analytical notes (it is the literature's term), but it is jargon to a general reader. *Self-serving* rejected (pejorative connotation); *own-behalf* considered, less natural in running prose. The "equal billing" question for this reading (`verbal-system.md` §9.3) is unaffected by the rename; if it is later demoted to a marked emphatic, the term can narrow with it.

### Threshold reading
- **Shorthand:** *threshold*.
- **Gloss tag:** THRESH.
- **Definition:** The subject is in the process of becoming such that the verb will happen — on the approach to a tipping point. The progressive frame supplies the becoming; the infinitive-shaped concord keeps the verb prospective. Hosted by progressive + infinitive-shaped concord.
- **Status:** **[Settled]** (accepted June 2026).
- **Canonical home:** `verbal-system.md` §3.3.
- **History & alternatives:** *INC / inchoative–threshold* (May 2026). *Inchoative* retained as the typological synonym for analytical notes; *threshold* was already half the working name and is the transparent half.

### Backdrop reading
- **Shorthand:** *backdrop*.
- **Gloss tag:** BACK.
- **Definition:** The verb's ongoing activity is the discourse-relevant backdrop — the *I-was-V-ing-when-X* framing, with experiential or narrative coloring. Hosted by perfect + progressive-shaped concord.
- **Status:** **[Settled]** (accepted June 2026).
- **Canonical home:** `verbal-system.md` §3.3.
- **History & alternatives:** *PS / pragmatic-stative / experiential* (May 2026) — three names, none of which evoked the function, and *stative* collided with two unrelated uses of the word (stative verbs; stative-domain strategies). *Scene-setting* considered; *backdrop* is shorter and equally transparent. Note: this reading's analytical status (agency-modulation vs. co-grammaticalized discourse function, `verbal-system.md` §9.1) is open; the descriptive name is deliberately neutral between the two views.

### Concord affix
- **Shorthand:** *concord* ("infinitive-shaped concord", "progressive-shaped concord").
- **Gloss tag:** CONCORD.
- **Definition:** The affix on the main verb showing concordance with the frame. In the get-oneself paradigm, the concord shape — infinitive-shaped vs. progressive-shaped — selects the reading.
- **Status:** **[Provisional]** — the term commits only to the agreement function; revisable if lexical-aspect or pragmatic-salience effects prove to do independent grammatical work (open question, `verbal-system.md` §4.2).
- **Canonical home:** `verbal-system.md` §4.2.
- **History & alternatives:** candidates held in reserve: *echo affixes* (if primarily feature-copying), *linker morphology* (if marking the frame–verb relation), *stem extensions* (maximally noncommittal), *coloring* (informal). The shape names *infinitive-derived / progressive-derived* are reworded to *-shaped* in prose — the suffix describes what the form looks like, which is the synchronic fact; "-derived" is the diachronic claim and belongs in the Origin subsection.

### Recognitional marker
- **Shorthand:** —.
- **Gloss tag:** REC. **Forms (attested 2026-06-10):** *þ* (pre-consonantal) ~ *y* /i/ (before etymological vowels, inheriting the GA allomorphy).
- **Definition:** The morpheme descended from GA *the*, marking shared-knowledge type reference on a deverbal nominal — "you know the kind." Not a definite article.
- **Status:** **[Settled]** (term sourced from the determiner-typology literature; Himmelmann). Surface forms close the former placeholder *[Open: REC and ITER surface forms]* (`verbal-system.md` §7.1).
- **Canonical home:** morphology at `language_reference.md` §3.2.1; the construction at `verbal-system.md` §7 and §13. The REC ≠ DEF claim's home is `verbal-system.md` §7.3.
- **History & alternatives:** glossing as DEF rejected — etymologically accurate, functionally misleading. Origin gains the **etymological doublet** analysis (v1.2): GA *the* → referential *o* (merged with *a*) and recognitional *þ ~ y* via divergent reduction paths (see *etymological doublet*, §2).

### Iterative marker
- **Shorthand:** —.
- **Gloss tag:** ITER. **Form (attested 2026-06-10):** *-ś*.
- **Definition:** The plural *-s* morpheme on a deverbal nominal, adding a repeated-instances reading on top of the recognitional marker.
- **Status:** **[Settled]** (accepted June 2026) — rename of the *habitual marker (HAB)*.
- **Canonical home:** morphology at `language_reference.md` §3.2.1; the construction at `verbal-system.md` §7 and §13.
- **History & alternatives:** *habitual marker / HAB* (May 2026). Retired to resolve the collision with the habitual frame aspect cell — two different "habituals" in one verbal system is a trap for any reader. The existing prose already glossed this morpheme's contribution as "iterative / repeated-instances," so the rename follows the documents' own description.

### Recognitional-iterative nominal construction
- **Shorthand:** *the recognitional nominal* (when the iterative layer is not at issue).
- **Gloss tag:** composite: REC-stem-ITER.
- **Definition:** The construction stacking the recognitional marker and (optionally) the iterative marker on a deverbal nominal: shared-knowledge type reference, optionally with iterated instantiation. **Analyzed (2026-06-11) as a special case of the possession construction** (§2): the habitual reading is compositional — REC (type) + ITER (iteration) + frame (engagement) — with a two-feature residue distinguishing the deverbal case: do-support *ię* on the get-oneself side (systematicity pending battery B1) and the *þ ~ y* REC exponent in place of merged *o*.
- **Status:** term **[Settled]** (accepted June 2026); the demotion analysis **[Settled]** with residue spec **[Provisional]** pending B1 (`phase4-triage-2026-06.md` §2.1).
- **Canonical home:** `verbal-system.md` §7 (special-case statement, worked example, Origin) and §13 (frame combinatorics); morphology at `language_reference.md` §3.2.1.
- **History & alternatives:** *recognitional-habitual nominal construction* (May 2026). The construction's "flagship innovation" framing survives the demotion as a nominal-side innovation.

### Deverbal nominal
- **Definition:** A verb's action treated as a noun — the territory GA covers with the gerund (*the running*, *the eating*).
- **Status:** **[Settled]**; standard term, but the plain-language paraphrase above accompanies first use in each document.
- **Canonical home:** `verbal-system.md` §7.

### Stative-domain strategies
- **Shorthand:** *the three strategies*.
- **Definition:** The three constructional routes for expressing states (feelings, attitudes, internal conditions), which the frames cannot host directly: **activity-coercion** (pick an activity verb that correlates with the state), **stimulus-promotion** (make the stimulus the subject and the experiencer the object), and **causative** (reuse the *get X to V* shape with an external causer).
- **Status:** **[Provisional]** — class name revisable when `verbal-system.md` §9.2 (core grammar vs. sibling resource) settles; the three member names are descriptive and **[Settled]**.
- **Canonical home:** `verbal-system.md` §6.

### Weak pronoun / strong pronoun
- **Gloss tags:** standard person/number tags.
- **Definition:** Weak (clitic) pronouns are the default subject expression and carry the grammatical fusions (aspect, modal, negation) — they are the system's **aspect carriers**. Strong (tonic) pronouns, from GA *on [POSS] end*, carry emphatic, possessive, and topic-frame readings and take no fusions.
- **Status:** **[Settled]**.
- **Canonical home:** `verbal-system.md` §5.
- **Addendum (v1.2):** a third strong-pronoun function identified 2026-06-11 — **antitopic tagging** in right dislocation (see §3), plus boundary-marking buffering in stacked matrix-particle constructions. Paradigm corrections recorded for Session V: 1SG weak = *e* (not *eu*); go-ahead habitual = *ouhen* (not *ohen*).

### Nested negation
- **Definition:** Stacking a get-oneself negative over a go-ahead negative — "failing to deliberately decline" — to yield obligation ("must do").
- **Status:** **[Settled]** as a phenomenon name; glossing convention **[Open]** (`verbal-system.md` §10.1).
- **Canonical home:** `verbal-system.md` §10.

### Matrix particle
- **Shorthand:** *scaffold particle* (informal; the user's coinage — the particle erects a modal frame the clause sits inside).
- **Gloss tag:** MP (class tag; members carry composite tags, see next entry).
- **Definition:** A member of the closed-ish class of particles defined by **two syntactic diagnostics**: (1) **clause scope** — the particle colors a whole clause with modal/evidential meaning — and (2) **fixed clause-initial position**. Many members are grammaticalized from GA matrix clauses (*it ended up..., I know (that)..., what I need is...*), which is the source of the name and of the **tense** that some of them carry (a privative non-past/past pair); but neither a matrix-clause source nor tense is criterial (see History). Members are unmarked for person, and each lexically specifies whether it governs the aspect of its clause.
- **Status:** **[Settled]** (user decision, 2026-06-11; membership criterion revised to the syntactic diagnostics by user decision 2026-06-18).
- **Canonical home:** `verbal-system.md` §11; decision records `phase4-triage-2026-06.md` §2.2 and `phase4-triage-saying-2026-06.md` §2.1.
- **History & alternatives:** *adverbial relativizer* (working label, 06-10) — retired: nothing is relativized. *Propositional modal particle*, *tense particle* considered; *matrix particle* is transparent about the diachronic source and commits to nothing contested. **Membership criterion revised 2026-06-18** (`phase4-triage-saying-2026-06.md` §2.1): the former criterion — *the etymon contains a finite verb* (hence tense-capable) — is **demoted to an origin correlate** (it explains why *enp/enniip* and *no/nii* carry tense; it does not decide membership). The class is now defined by clause-scope + clause-initial position. Consequences: (a) tenseless items are members in good standing (*reś*, *nóuśshè*, the retired *piies*); (b) new member **nóuśshè** (< *in a nutshell*; adverbial etymon, no finite verb) directly vindicates the position-based criterion; (c) flexible-position items (*meiyi*, *bauyiis*, *quo*) are **excluded** as modal/flexible adverbs — superseding the earlier finite-verb-based exclusion of *maybe*, *in my eyes*. Name kept (the prototype is still matrix-clause-derived). The **split-TAM** framing is narrowed accordingly: aspect on the weak pronouns is unchanged, but tense is a sub-property of finite-verb-sourced members, **not** a class trait.

### Matrix particle members and gloss scheme
- **Members (prose names, source-anchored per the see-particle pattern):** the **end-up particle** (*enp* / past *enniip*; happenstance outcome), the **know-that particle** (*no* / past *nii*; knowledge — distinct from the know-particle, see homophony note under that entry), the **really-need particle** (*rhi·iiniies* / past *rhi·iiniir·ros*; desiderative–weak deontic; reduplicated intensive *rhi·ii·rhii·niies*), the **guess particle** (*reś* < *I guess*; general indirect evidential — hearsay and inference alike; **tenseless**, no past form), and the **summary particle** (*nóuśshè* < *in a nutshell*; paraphrase / "long story short"). The former **appears particle** (*piies*) is **retired** — superseded by the guess particle (see §6 and the supersession note below).
- **Gloss tags:** composite MP.x with source-anchored member labels and .PST on the marked tense member: `MP.ENDUP` / `MP.ENDUP.PST`, `MP.KNOW` / `MP.KNOW.PST`, `MP.NEED` / `MP.NEED.PST`, `MP.GUESS` (no tense pair — tenseless), `MP.SUMM`. The reportative predicted for round 2 is filled by the **guess particle** (a general indirect evidential subsuming hearsay and inference), so the reserved `MP.REP` is **not** instantiated.
- **Status:** **[Settled]** for the standing members (accepted June 2026; *really-need particle* by user decision); the *reś*/*nóuśshè* additions and the *piies* retirement **[Settled 2026-06-18]** as phenomena, with the member names **guess particle** / **summary particle** and gloss tags `MP.GUESS` / `MP.SUMM` **[Settled]** (Batch III accepted 2026-06-20).
- **Supersession note (*piies* → *reś*).** *reś* is structurally **tenseless** (GA *I guess* / *I guessed* converge phonologically — speech-anchored, no surface tense contrast), which is why it can absorb the appearance role that *piies* held without inheriting the "past form unattested" problem (this **closes** `verbal-system.md` §11.7's open question by deletion of the member). The seem/look **division of labor** *piies* carried (perceptible vs non-perceptible appearance) is now borne by **topic-particle choice** under *reś*: *hii ossii* (perceptible) vs *no ossii* (non-perceptible). Personal-source vs general hearsay is carried by *reś* + the quotative marker *quo* (which can merge → *resquo*; see *quotation markers*).
- **History & alternatives:** semantic tags HAPP / KNOW / DESID / APPAR (triage draft) — reworked: HAPP collides visually with HAP (happenstance reading), and bare semantic tags hide class membership; the MP.x composite follows the registry's existing composite-tag pattern (`LVC.VOL.HAB`). The *appears particle* (*piies*) was a [candidate] member pending its past form (battery B3, now **CLOSED**); its retirement and the *reś* supersession are recorded at `phase4-triage-saying-2026-06.md` §2.2.

### Quotative construction
- **Shorthand:** *quotative o*.
- **Gloss tag:** QUOT (on the verb *o*; the quotation markers carry their own tags, next entry).
- **Definition:** The colloquial-quotative frame in which reported speech, thought, or stance is introduced by the verb *o* (< GA *go*) rather than by a lexical "say" verb. *o* is **intransitive** and is **obligatorily followed by an ideophone** characterizing the manner of the speech act (see *ideophone*, §3). Direct vs indirect quotation is carried by **particle choice**, not by a complementizer. GA *be all* does **not** survive as a quotative.
- **Status:** phenomenon **[Settled 2026-06-18]** (the colloquial *go*-quotative wins; *be all* dies — `phase4-triage-saying-2026-06.md` §1.3); the term *quotative construction* and gloss tag `QUOT` **[Settled]** (Batch III accepted 2026-06-20).
- **Canonical home:** `verbal-system.md` §12 (Quotation); ideophone obligatoriness cross-referenced to `ideophones.md`.
- **History & alternatives:** the **three-*o* homophony** is registered here: quotative *o* (< *go*), the reported-speech **opener** *o* (< *oh*; see next entry), and the referential **article** *o* (< merged *the*/*a*) are three distinct lexemes sharing a surface form — to be disentangled in the dictionary. Perfect aspect of the quotative is *rhentt* (< *went*).

### Quotation markers
- **Shorthand:** —. **Members:** *quo* (< *quote*), the **opener** *o* (< *oh*), *ohei* (< *oh hey*).
- **Gloss tags:** `QUO` (*quo*, source/quotative marker), `Q.OPEN` (opener *o*), `Q.DIR` (*ohei*, direct-question quotative).
- **Definition:** The optional particles that disambiguate quotation around the obligatory quotative verb *o*. **quo** marks a personal/quoted source; its **position is meaningful** (it precedes the salient/topical part of the quote and can color speaker doubt), and after *reś* it scopes the whole clause and merges → **resquo**. The **opener *o*** (< *oh*) opens a stretch of reported speech. ***ohei*** (< *oh hey*) marks a direct question as quoted. Direct vs indirect is signalled by which of these appear (clause-initial *quo* + opener = direct); no complementizer is used.
- **Status:** phenomena **[Settled 2026-06-18]**; the gloss tags `QUO` / `Q.OPEN` / `Q.DIR` **[Settled]** (Batch III accepted 2026-06-20).
- **Canonical home:** `verbal-system.md` §12 (Quotation); discourse cross-reference in `language_reference.md`.
- **History & alternatives:** see the three-*o* homophony note under *quotative construction*. *quo* also does evidential duty with the guess particle (*resquo*; see *matrix particle members*).

### Possession construction
- **Shorthand:** —.
- **Gloss tag:** none (composite frame tags carry the analysis).
- **Definition:** The frame-plus-nominal engagement construction: **get-oneself + nominal** in perfect frame aspect expresses possession ("have"), in imperfect frame aspect acquisition in progress ("getting"); **go-ahead (+ *with*) + nominal** expresses deliberate selection ("picking and choosing"). A **causative variant** with the recipient in the *get*-slot expresses transfer ("give"), volition-neutral by default; the lexical verbs *rib* (give) and *ǫıĩ* (own) supply explicit-volition and mere-having alternatives.
- **Status:** **[Settled]** (accepted June 2026).
- **Canonical home:** `verbal-system.md` §13.
- **History & alternatives:** none considered yet. Registered consequence: the recognitional-iterative nominal construction is a **special case** of this construction (the demotion decision — see that entry).

### Passive-shaped concord
- **Shorthand:** falls under *concord* once established.
- **Gloss tag:** CONCORD (shape noted in analysis lines as elsewhere).
- **Definition:** A third concord shape alongside the infinitive-shaped and progressive-shaped concords, patterned on the GA passive participle; attested in the *spli·oþw* class, where it delivers the completed-happenstance reading the progressive shape cannot (right aspect, no threshold coloring).
- **Status:** **[Settled]** as a shape name (accepted June 2026); attestation breadth **[Provisional]**. **Caveat registered:** in the discovery example the shape is conflated with the separative satellite *oþw*, because GA *split* has a zero-marked participle; disambiguation needs a verb with overt participle morphology (a *got myself taken-* class form).
- **Canonical home:** `verbal-system.md` §4.2.
- **History & alternatives:** the *-shaped* naming follows the settled convention (synchronic shape in prose; derivation claims belong in Origin subsections).

### Inherited irregularity
- **Shorthand:** *irregular concord* (for the concord-specific case).
- **Gloss tag:** none.
- **Definition:** A paradigm form preserving GA irregular (strong-verb) morphology where the regular derivation predicts the productive exponent — e.g., concord *meirtt* (< GA *made it*) for *meiktt*, where the regular concord infix *-t(t)-* is expected. Same stem, unexpected exponent: the *kept*-not-*keeped* pattern, not the *went*-for-*go* pattern.
- **Status:** **[Settled]** (accepted June 2026).
- **Canonical home:** `verbal-system.md` §4.2.1.
- **History & alternatives:** the working word in the 06-10 notes was *suppletion* — disentangled 2026-06-11 into this term plus *homophonous merger*, *convergent pair*, and *frame-conditioned satellite*, with *suppletion* held in reserve (see those entries).

### Homophonous merger
- **Shorthand:** *merger*.
- **Gloss tag:** none.
- **Definition:** Two GA etyma collapsing into a single conlang form via regular sound change, creating polysemy that the frames (or the reading system) then disambiguate — e.g., *ręim* (< *name* + *game*). A productive lexical source: the polysemy is created by the conlang's own diachrony, not inherited from GA.
- **Status:** **[Settled]** (accepted June 2026; promoted from `verb-recipe-v2.md` §5.3).
- **Canonical home:** `verb-recipe-v2.md` §5.3.

### Etymological doublet
- **Shorthand:** *doublet*.
- **Gloss tag:** none.
- **Definition:** One GA etymon yielding **two** conlang forms via divergent grammaticalization paths with divergent phonological outcomes — e.g., GA *the* → merged referential article *o* and recognitional marker *þ ~ y*. Cross-linguistic parallel: Latin *ille* → Romance articles and third-person pronouns.
- **Status:** **[Settled]** (accepted June 2026).
- **Canonical home:** Origin subsections of the affected entries; first worked case at `verbal-system.md` §7.3 Origin.

### Convergent pair
- **Shorthand:** —.
- **Gloss tag:** none.
- **Definition:** Two GA etyma whose conlang reflexes converge in form and semantic territory while remaining **distinct lexemes** — e.g., *nouś* (< *notice*) and *not* (< *note*), with frame affinities (get-oneself and go-ahead respectively) that are tendencies, not grammar: stem choice is meaning-conditioned, and the converse pairings are grammatical. The mirror image of the etymological doublet, and the watch-case for *suppletion* (see that entry).
- **Status:** **[Settled]** (accepted June 2026; the *nouś/not* analysis settled by user decision 2026-06-11).
- **Canonical home:** dictionary cross-references; `verbal-system.md` §8 (poly-resolving discussion).

### Frame-conditioned satellite
- **Shorthand:** *satellite*.
- **Gloss tag:** none yet (entry-level; *oþw* glossed lexically).
- **Definition:** A particle-derived element supplying event structure that one frame requires of its host verb — affinity, not agreement. First member: *oþw* (< GA *off*, the happenstance-detachment particle of *drift off, doze off, nod off*), which builds the befall-able path event that lexically volitional bare stems lack under the get-oneself frame.
- **Status:** class term **[Settled]** (accepted June 2026); *oþw* membership **[Provisional]** pending further verb classes (*doze/drift/nod* pass per user judgment, 2026-06-11). A possible *up*-satellite is queued for testing in the round-2 channel sub-category.
- **Canonical home:** `verbal-system.md` §4.2 vicinity + dictionary entry for *oþw*.

### Suppletion
- **Shorthand:** —.
- **Gloss tag:** none.
- **Definition:** Etymologically distinct stems filling cells of a single paradigm. **Attested (2026-06-12): one case** — *þokss/þott*, where *thought*'s reflex serves as the *focus*-verb's deverbal nominal (a paradigm cell, since deverbal nominalization is systematic via the REC construction). Mechanism: **orphaned-derivative adoption** — the nominal outlived its GA base verb and was adopted by the semantically nearest surviving verb; the vowel leveling (*þautt* → *þott*) is the unification evidence, and pre-leveling *þautt* survives as archaic speaker variation (lore-ready). The *nouś/not* convergent pair remains two lexemes (2026-06-11); the frame-suppletion prediction (poly-resolving collapse) stays open as a second potential source.
- **Status:** **[Settled]** as a disposition (user decision, 2026-06-11): the term is held in reserve and must not be used loosely in new prose; the 06-10 working uses are superseded by *inherited irregularity*, *homophonous merger*, *convergent pair*, and *frame-conditioned satellite*.
- **Canonical home:** `dictionary.md` *þott* and *þokss*; this entry for the term.

---

## 3. Discourse and the nominal side

### Visibility particles
- **Definition:** The closed two-member class of topic particles marking a fronted topic for perceptibility.
- **Status:** **[Settled]** as the class name.
- **Canonical home:** `language_reference.md` §3.7 (pending nominal-system spin-out).

### See-particle
- **Shorthand:** —. **Forms:** *hii* / *hiie* / *hiho*.
- **Gloss tag:** VIS (clausal form VIS-CLAUSAL).
- **Definition:** The visibility particle marking the topic as present and perceptible; from the imperative of GA *see*.
- **Status:** **[Settled]** (accepted June 2026) — descriptive member name for prose; the gloss tags are unchanged.
- **History & alternatives:** prose previously used the bare gloss tags ("VIS (*hii*, *hiie*)") as names; the source-anchored name follows the go-ahead/get-oneself pattern.

### Know-particle
- **Shorthand:** —. **Forms:** *no* / *nou* / *noho*.
- **Gloss tag:** NVIS (clausal form NVIS-CLAUSAL).
- **Definition:** The visibility particle marking the topic as absent, abstract, generic, or discourse-given; from the imperative of GA *know*.
- **Status:** **[Settled]** (accepted June 2026) (parallel to *see-particle*).
- **Homophony note (added v1.2):** distinct from the matrix **know-that particle** *no/nii* (§2), which takes an NP or a full clause and yields a complete sentence; the topic particle's clausal form *noho* instead introduces a topic awaiting elaboration. The pair can stack (*No Báuyà, no Báuyà* — topic, then assertion). Both descend from GA *know*; document the relationship in both canonical homes.

### Right dislocation
- **Shorthand:** *antitopic* (the construction); *antitopic tag* (the marking).
- **Gloss tag:** none (constructional).
- **Definition:** The postposed-topic construction: a nominal placed after the clause, co-referent with material inside it, retaining definite coloring. Marked **without** a visibility particle; tagged instead with the strong-pronoun *on-X-end* phrase. Pairs with the left-dislocation analysis into a registered asymmetry: **the visibility contrast is a left-periphery-only phenomenon.**
- **Status:** **[Settled]** as terms (accepted June 2026); the asymmetry itself **[Provisional]** — wants worked examples.
- **Canonical home:** `language_reference.md` §3.7.3 and §4; `verbal-system.md` §5.4.
- **History & alternatives:** *right dislocation* and *antitopic* are both standard literature terms; registered together, with *antitopic* preferred as the shorthand in running prose. Consequence registered against the *weak pronoun / strong pronoun* entry: antitopic tagging is a third strong-pronoun function.

### Ideophone
- **Shorthand:** —.
- **Gloss tag:** IDEO.
- **Definition:** A member of the productive expressive class that depicts the *manner* of a speech act (or, by extension, another event) — vivid, often onomatopoeic words such as *rhemmemmêm* (bullet-pointed, confrontational argument) or *rekriiâ* (speaking in dialect). Ideophones are **obligatory after the quotative verb *o*** (see *quotative construction*, §2), **phonotactically marginal** (they may contain rare or non-phonemes and may bear ultimate-syllable stress, breaking constraints binding on the core lexicon), **verbalizable** (they take frame + concord, e.g. *rekriiâkm* "chatting"), and frequently **multimodal** (paired with a conventionalized co-speech hand gesture).
- **Status:** the class is a **[Settled]** phenomenon (user decision 2026-06-18); the term *ideophone* and gloss tag `IDEO` are **[Settled]** (Batch III accepted 2026-06-20).
- **Canonical home:** **`ideophones.md`** — a new sibling deep-dive (home ratified 2026-06-20; to be created in Session I). Spokes: phonotactic-exemption rule in `phonology.md`; orthographic conventions (interpunct *·*, glottal-stop *t*, -*ðs*) in `orthography.md`; members in `dictionary.md`. A multimodal / co-speech-**gesture notation** convention is to be established in `ideophones.md`.
- **History & alternatives:** surfaced in the SAYING round as its largest finding (`phase4-triage-saying-2026-06.md` §2.5). *Ideophone* is the standard cross-linguistic term; *expressive*, *mimetic* held in reserve. Attested members include *rhemmemmêm*, *rekriiâ* (overrides the older *rékriiyæ*), *rhitmmtm*, *bauwouwou*, plus onomatopoeia (*riprprp*, *bet bät*) introduced by -*ðs*.

### Existential particle
- **Shorthand:** *pons*.
- **Gloss tag:** EXIST.
- **Definition:** *pons* (< GA *(there is) upon us*) — the neutral existential / presentational "there is" (cf. French *il y a*, Spanish *hay*): *pons rheĩ* "there is rain." The grammar **defaults inanimate predications to this impersonal existential**, reserving active framing (either frame) for non-neutral discourse effect.
- **Status:** phenomenon **[Settled 2026-06-18]**; gloss tag `EXIST` **[Settled]** (Batch III accepted 2026-06-20). The inanimate-active-framing color generalization is **[Provisional]** (battery B9; `verbal-system.md` §4.2).
- **Canonical home:** `language_reference.md` (existential / presentational).
- **History & alternatives:** irregular diachronic development (< *upon us*) parked for a phonology session (`phase4-triage-saying-2026-06.md` §5).

### Clause linkers
- **Shorthand:** —. **Members:** *rhishisben*, *kyii*.
- **Gloss tag:** LINK.
- **Definition:** Particles that join clauses with a discourse relation. ***rhishisben*** (< *which is when* / *which has been*) marks simultaneity / background — "while, as." ***kyii*** (< *cue*) marks succession with a mild causal tint — "and then, whereupon" — and can carry irony or sarcasm.
- **Status:** phenomena **[Settled 2026-06-18 — record]**; gloss tag `LINK` **[Settled]** (Batch III accepted 2026-06-20).
- **Canonical home:** `language_reference.md` (clause linkage / discourse).
- **History & alternatives:** the *rhishisben* form reflects a phonological convergence of two GA sources, flagged for a phonology session.

### Aboutness marker
- **Shorthand:** *-wiis*.
- **Gloss tag:** ABT.
- **Definition:** *-wiis* (< GA *-wise*) — a backgrounding marker flagging what a clause is *about* / with respect to. Interacts with the definite-object restriction and information structure.
- **Status:** phenomenon **[Settled 2026-06-18 — record]**; gloss tag `ABT` **[Settled]** (Batch III accepted 2026-06-20).
- **Canonical home:** `language_reference.md` (information structure).

### Reciprocity
- **Shorthand:** —.
- **Gloss tag:** none yet.
- **Definition:** The mutual-action relation ("argue with *each other*"). First data point (2026-06): on a we-subject the get-oneself frame carries reciprocity with **no dedicated marker** (*riauseto bekw* "we bickered (with each other)").
- **Status:** **[Open]** — stub. Whether reciprocity is ever overtly marked, and the fate of an *each other* exponent, await data (battery B10).
- **Canonical home:** `language_reference.md` (reciprocity stub).

---

## 4. Phonology and prosody

### Appendix (prosodic appendix)
- **Definition:** Post-stress syllabic-consonant material adjoined to the prosodic word above the foot — weight-bearing but invisible to stress.
- **Status:** **[Settled]**. Use the disambiguated form *prosodic appendix* wherever document appendices (e.g., `language_reference.md` Appendix A / Appendix B) are in scope.
- **Canonical home:** `phonology.md` §3.5.
- **History & alternatives:** *sesquisyllabic* — **[Retired]**, borrowed-but-misapplied (it names a left-edge phenomenon; the conlang's is right-edge). Retirement record: `phonology.md` §6 glossary.

### Pitch residue
- **Definition:** The analysis of pitch as the F0 left behind on the GA etymon's stressed syllable after loudness and length migrated to the final vowel under the conlang's final-stress rule — rather than an independently assigned prosodic feature.
- **Status:** **[Settled]** as the analytical framing (placement settled; contrastiveness **[Open]**).
- **Canonical home:** `phonology.md` §3.4.

### Mora
- **Definition:** The unit of syllable weight — roughly, one beat of vowel. A short vowel is one mora, a long vowel two, a syllabic consonant one.
- **Status:** **[Settled]**; standard term, paraphrase accompanies first use per document.
- **Canonical home:** `phonology.md` §3.1.

### Debuccalization
- **Definition:** A consonant losing its mouth posture and surfacing as bare /h/ — the path GA /s/ and onset /k/ took.
- **Status:** **[Settled]**; standard term, paraphrase accompanies first use per document.
- **Canonical home:** `phonology.md` §4.4.1.

---

## 5. June 2026 rename batch — accepted

Accepted by the user, June 2026. The batch: **frame** (prose-primary over *light verb complex*) · **frame aspect** (over *LVC.TAM*) · **habitual** (single name, over *gnomic/habitual*) · **reading** (class term, over prose *sub-modality*) · **happenstance reading** (HAP) · **effortful self-benefit reading** (SELF.BEN) · **threshold reading** (THRESH) · **backdrop reading** (BACK) · **infinitive-shaped / progressive-shaped concord** (over *-derived*) · **iterative marker** (ITER, over nominal *HAB*) · **recognitional-iterative nominal construction** · **see-particle / know-particle**.

Each can be accepted or rejected independently, except: *iterative marker* and *recognitional-iterative nominal* travel together, and the four reading names travel with the retirement of the PH/AB/INC/PS abbreviations.

### Batch II — June 2026 (post-translation-exercise), proposed

Drafted in Session T (2026-06-11); **accepted by the user 2026-06-11**, with one amendment: *need particle* → **really-need particle**. The batch: **matrix particle** *(already settled by user decision)* · **matrix-particle member names and MP.x gloss scheme** · **possession construction** · **passive-shaped concord** · **inherited irregularity** · **homophonous merger** (promotion) · **etymological doublet** · **convergent pair** · **frame-conditioned satellite** · **right dislocation / antitopic** · **suppletion disposition** *(already settled by user decision)*.

Coupling: *convergent pair*, *etymological doublet*, *inherited irregularity*, and *frame-conditioned satellite* travel with the *suppletion* reservation (they are its replacements in the four use-cases); the member names and gloss scheme travel with *matrix particle* but are separately revisable.

### Batch III — June 2026 (SAYING translation round), accepted

Drafted in Session T (2026-06-20) from `phase4-triage-saying-2026-06.md` §8.1; **accepted by the user 2026-06-20**, wholesale. **Settled by prior user decision (2026-06-18) and encoded here:** the *matrix particle* criterion revision (syntactic diagnostics; tense demoted to origin correlate); the *piies* → *reś* supersession; the *ideophone* phenomenon and its home (the sibling `ideophones.md`, **ratified 2026-06-20**); the *quotative o* result (*be all* dies). **Accepted 2026-06-20 (term and gloss-tag choices):** member names **guess particle** (*reś*, `MP.GUESS`) and **summary particle** (*nóuśshè*, `MP.SUMM`); **quotative construction** (`QUOT`); **quotation markers** *quo* / opener *o* / *ohei* (`QUO` / `Q.OPEN` / `Q.DIR`); the term **ideophone** (`IDEO`); **existential particle** *pons* (`EXIST`); **clause linkers** (`LINK`); **aboutness marker** *-wiis* (`ABT`); **reciprocity** (Open stub).

Coupling: the *reś* member entry travels with the *piies* retirement (one supersession); the *ideophone* term travels with the `ideophones.md` spin-out (Session I); the quotation entries (*quotative construction*, *quotation markers*) travel together.

---

## 6. Retired terms

Must not appear in new prose; listed so they are recognized in older text and session history.

| Retired term | Replaced by | Where the record lives |
|---|---|---|
| *involitive* | non-volitional get-oneself | `verbal-system.md` §17 |
| *modulated* | non-volitional get-oneself | `verbal-system.md` §17 |
| *volitive* | volitional go-ahead | this file (June 2026) |
| *non-volitive* | non-volitional get-oneself | this file (June 2026) |
| *modulation cell* | reading (sub-modality) | `verbal-system.md` §9.5 |
| *sesquisyllabic* | appendix | `phonology.md` §6 |
| *PH, AB, INC, PS* (in prose) | the four reading names | this file (June 2026) |
| *LVC.TAM* (in prose) | frame aspect | this file (June 2026) |
| *gnomic* (in prose) | habitual (cell), with timeless coverage stated in the definition | this file (June 2026) |
| *HAB* (nominal morpheme) | iterative marker (ITER) | this file (June 2026) |
| DEF (as gloss for the *the*-morpheme) | REC | `verbal-system.md` §7.3 |
| *adverbial relativizer* | matrix particle | this file (v1.2); `phase4-triage-2026-06.md` §2.2 |
| *suppletion* (as the 06-10 working catch-all) | inherited irregularity / homophonous merger / convergent pair / frame-conditioned satellite, per case | this file (v1.2), *suppletion* entry |
| *piies* / *appears particle* (MP.APPEAR) | the guess particle *reś* (MP.GUESS) | this file (v1.5); `phase4-triage-saying-2026-06.md` §2.2; matrix-particle members entry |

---

## 7. Versioning notes

### v1, June 2026 — registry created

Seeded from the May 2026 terminology state across `verbal-system.md` §14/§9.5, `phonology.md` §6, and `language_reference.md`. Incorporates the user's June 2026 decisions: spelled-out descriptive terms preferred over abbreviations; *volitional go-ahead* and *non-volitional get-oneself* adopted as full paradigm-side names with *go-ahead* / *get-oneself* as shorthands. The §5 proposed batch implements the same descriptive-and-long principle across the rest of the verbal-system terminology; each item awaits the user's verdict.

---

## Versioning notes

### v1.7, June 2026 — appendix cross-reference repointed

The *prosodic appendix* entry's disambiguation example updated: the former document-appendix exemplar `verbal-system.md` Appendix A is now `language_reference.md` Appendix A / Appendix B, following the relocation of the verb-lexicon methodology and the consolidation of design/process material into `language_reference.md`'s design appendices (`language_reference.md` v3.8, `verbal-system.md` v2.10). Terminology unchanged.

### v1.6, June 2026 — Batch III accepted

Batch III accepted by the user (2026-06-20), wholesale. All Batch III `[Proposed]` entries promoted to **[Settled]**: the matrix-particle member additions (**guess particle** *reś* / `MP.GUESS`, **summary particle** *nóuśshè* / `MP.SUMM`); **quotative construction** (`QUOT`); **quotation markers** (`QUO` / `Q.OPEN` / `Q.DIR`); **ideophone** (`IDEO`); **existential particle** *pons* (`EXIST`); **clause linkers** (`LINK`); **aboutness marker** *-wiis* (`ABT`). `MP.REP` remains un-instantiated (the guess particle subsumes the reportative role). *reciprocity* stays **[Open]** (stub). Names are now locked for Session V (`verbal-system.md` §11 rewrite + Quotation section).

### v1.5, June 2026 — Session T (SAYING round)

Executed from `phase4-triage-saying-2026-06.md` §8.1. **Matrix particle** membership criterion **revised** to two syntactic diagnostics (clause-scope + clause-initial); the finite-verb-etymon criterion demoted to an origin correlate, and the split-TAM framing narrowed (tense is a member sub-property, not a class trait) — user decision 2026-06-18. **Members updated:** added the **guess particle** *reś* (general indirect evidential, tenseless) and the **summary particle** *nóuśshè*; the **appears particle** *piies* **retired**, superseded by *reś* (closing the `verbal-system.md` §11.7 "piies past form" open question by deletion; the seem/look division of labor absorbed by *reś* via topic-particle choice). **New entries (Batch III, [Proposed] — awaiting verdict):** *quotative construction* / quotative *o* + the three-*o* homophony; *quotation markers* (*quo*, opener *o*, *ohei*); *ideophone* (new expressive class; home ratified as the sibling `ideophones.md` 2026-06-20; gesture / phonotactic-exception notes); *existential particle* *pons*; *clause linkers* (*rhishisben*, *kyii*); *aboutness marker* *-wiis*; *reciprocity* (Open stub). Retired-table: *piies* added. Conformance sweeps deferred to Sessions V, L, I and the dictionary batches.

### v1.1, June 2026 — June batch accepted

All `[Proposed]` entries from the June 2026 batch promoted to **[Settled]** on user acceptance. Conformance sweeps executed in `verbal-system.md` v2, `language_reference.md` v3, `phonology.md` v3, and `orthography.md` v3.

### v1.4, June 2026 — Session L homes settled

REC, ITER, and the recognitional-iterative construction entries updated to their post-migration canonical homes (morphology at `language_reference.md` §3.2.1; construction at `verbal-system.md` §7/§12); right dislocation homed at `language_reference.md` §3.7.3/§4 and `verbal-system.md` §5.4. Conformance state: verbal-system v2.2, language_reference v3.2. *(Addenda 2026-06-12: suppletion candidate annotated, then **activated** on the user's þott decision — first attested case, þokss/þott; entry updated.)*

### v1.3, June 2026 — Batch II accepted; Session V conformance

Batch II accepted by the user (2026-06-11) with one amendment: *need particle* renamed **really-need particle** (gloss tag MP.NEED unchanged). All Batch II `[Proposed]` entries promoted to **[Settled]**; *oþw* satellite membership and the periphery asymmetry remain **[Provisional]** on their named evidence questions. Canonical homes updated for verbal-system v2.1: matrix particles §11, possession construction §12, irregular concord §4.2.1; retired-table records repointed §14 → §16 (verbal-system renumbering). Conformance state: verbal-system v2.1 and language_reference v3.1 written against this registry version.

### v1.2, June 2026 — Session T (translation-exercise terminology)

Executed from `phase4-triage-2026-06.md` §8.1. Added: *matrix particle* (settled, user decision 06-11) with member names and MP.x gloss scheme (proposed); *possession construction*; *passive-shaped concord*; the suppletion disentangling — *inherited irregularity*, *homophonous merger* (promoted from `verb-recipe-v2.md` §5.3), *etymological doublet*, *convergent pair*, *frame-conditioned satellite*, and the *suppletion* reservation (settled, user decision 06-11); *right dislocation / antitopic*. Updated: REC and ITER entries with attested surface forms (*þ ~ y*; *-ś*), closing the §7.1 placeholder, and with Session-L migration notes; the recognitional-iterative construction entry with the demotion analysis; the know-particle entry with the matrix-homophony note; the weak/strong pronoun entry with the antitopic third function and paradigm corrections. Retired: *adverbial relativizer*; *suppletion* as a working catch-all. Batch II proposals listed in §5; conformance sweeps deferred to Sessions V and L.
