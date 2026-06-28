# Examples

**Version:** v0.5 (June 2026)
**Status:** Sibling reference document, parallel to `phonology.md`, `orthography.md`, `verbal-system.md`, and `dictionary.md`. Holds a single source of truth for glossed example sentences; other reference documents and dictionary entries cite by ID rather than reproducing glosses inline.

A working corpus of glossed example sentences in the conlang. Each entry is a numbered, dated block with five gloss layers (Conlang, IPA, Etymological, Leipzig, Translation) plus metadata. The corpus is not a translation set or a teaching grammar — it is a record of material that surfaced something interesting about phonology, morphology, syntax, or pragmatics, retained so the observation is recoverable later.

---

## 1. Purpose

Centralizing examples serves three ends:

1. **Single source of truth.** A given sentence is fully glossed in exactly one place. Dictionary entries and grammar discussions reference the entry by ID (`examples.md §E001`); they do not duplicate the gloss.
2. **LLM-feedable context.** A flat, structured corpus is easier to load as context than examples scattered across siblings.
3. **Diachronic record.** Entries are dated at creation, and substantive revisions to an entry are logged inside the entry. The corpus doubles as a record of how analysis has shifted — useful when a gloss is revised because of a downstream phonology or grammar decision.

---

## 2. Entry format

Each entry is a Markdown subsection headed `### EXXX {#EXXX}` (the explicit anchor enables stable linking) with the following fields, in order:

- **Conlang** — orthographic surface form, sentence-cased and punctuated as written. **Chunked with `|`** into alignment units (see *Chunk alignment* below); each chunk carries its own trailing punctuation.
- **Etymological** — word-for-word English etymological transcription, **chunked with `|` in lockstep with the Conlang line**: equal chunk counts, and chunk *i* glosses Conlang chunk *i*. See §3 for within-chunk notation.
- **IPA** — broad phonemic transcription. Use `‖` for sentence break, `|` for clause break, `.` for syllable break only where ambiguous. Stress marked with `ˈ`. Conform to `phonology.md` §4. This is a **free** line — *not* chunked; a `|` here is a clause break, never an alignment delimiter.
- **Leipzig** — *(deferred)* standard Leipzig interlinear gloss. Held dormant: the gloss labels/terms have not settled, so no renderer emits this line yet. Existing Leipzig lines are preserved but not displayed; omit on new entries until the gloss inventory is committed.
- **Translation** — idiomatic English translation in double quotes. A **free** line (not chunked); rendered whole beneath the gloss.
- **Tags** — `#`-prefixed keywords for grouping (phenomena, semantic fields, constructions). See §4.
- **Cited from** — backlinks to siblings or dictionary entries that reference this example. Maintained manually; `—` if none.
- **Added** — ISO date (YYYY-MM-DD) of first inclusion.
- **Revised** — dated bullets describing substantive changes to the entry. Use `—` until first revision. Format: `- YYYY-MM-DD: <what changed and why>`. Trivial fixes (typos, formatting) do not require an entry.
- **Notes** — optional. Open questions, contested glosses, layer-confidence flags, pointers to the discussion that generated the example.

IDs are assigned sequentially and zero-padded to three digits (`E001`, `E002`, …). They are stable and never reused, even if an entry is retired. A retired entry's block is kept in place with the body replaced by `**Retired YYYY-MM-DD:** <reason>` and the original content moved to the Revised log.

**Chunk alignment.** The Conlang and Etymological lines are split on `|` into aligned chunks — chunk *i* of one corresponds to chunk *i* of the other. A chunk is the unit a renderer highlights (HTML hover) or pads into a column (PDF). The build **requires equal chunk counts** on the two lines and fails the build loudly on a mismatch. Keep chunks at a sensible grain — usually one conlang word and its etymological gloss — and let punctuation ride with its chunk (`noê.`). The Translation and IPA lines are free; they are never chunked.

- **Gesture (χ)** — optional. For multimodal entries (ideophones), the conventionalized co-speech gesture, in the **χ** notation of `ideophones.md` §6. A free line; not chunked. Renderers opt in.

**Open schema.** The fields above are the current set, but a record is **extensible**: later milestones may add fields (e.g. `Audio`, per-chunk `Notes`/`Footnotes`) without changing existing entries. Parsers ignore fields they don't recognize.

**Deferred Etymological line.** An entry may omit the Etymological line when its GA derivation is not yet recoverable (e.g. source words still pending in the dictionary). The Conlang line is still chunked — the chunk grain is set now so the aligned Etymological line can be slotted in later at equal count. Until then the entry carries no alignment partner, and renderers that need the pseudo-etym row fall back to Conlang + Translation. (This is why the equal-chunk guard fires only when *both* lines are present.)

**This document is build-time source only.** It is not published as an HTML page or a PDF chapter. Citing documents pull examples in at compile time via the `<!-- example: EXXX -->` transclusion token; an inline `§EXXX` mention resolves to a hover-card on the site. See §6.

---

## 3. Etymological-gloss conventions

The Etymological line is conlang-specific and not part of standard Leipzig conventions. Its purpose is to make the diachronic derivation visible at a glance — what GA material each conlang word descends from. Conventions in current use:

- `today.is` — periods join elements that descend from separate GA morphemes but surface as a single conlang word. The dot is read as "fused with."
- `(a)bit.more` — parentheses mark a GA element that has been phonologically reduced to the point of unrecoverability or fully lost, but is etymologically present. The parenthesized material is what the GA reading would supply; it is not pronounced.
- `nippy.side` — applies to compounds: GA open compounds that surface as a single conlang word are joined with `.`.
- `rĩbii·hii` (in the **Conlang** line, not the Etymological line) — the middle dot `·` marks an internal morpheme boundary that the orthography fuses but that the etymology preserves. Use sparingly, only when the boundary is load-bearing for a discussion or a cross-reference.

The Etymological line is not a Leipzig gloss substitute. When grammatical role is what matters (case, TAM, agreement), use the Leipzig line. The Etymological line answers a different question: "what GA material is this?"

---

## 4. Tag registry

Tags are open-class and added as needed. Maintain the flat list here when introducing a new tag, so tag drift stays visible and consolidation is possible later.

- `#weather` — weather and atmospheric description
- `#comparative` — comparative and superlative constructions
- `#hedging` — epistemic / pragmatic hedging
- `#recognitional-habitual` — uses of the recognitional-habitual nominal (see `verbal-system.md` §6)
- `#concord` — concord-affix / stem-extension shapes (`verbal-system.md` §4.2)
- `#frame` — light-verb frame constructions (go-ahead / get-oneself)
- `#frame-aspect` — frame-aspect contrasts (habitual / imperfect / perfect)
- `#ideophone` — ideophones, as predicate or after the quotative (`ideophones.md`)
- `#quotative` — the quotative verb *o* and its markers (`verbal-system.md` §12)
- `#matrix-particle` — clause-scoping matrix / scaffold particles (`verbal-system.md` §11)
- `#evidential` — evidential / hearsay / inference marking
- `#possession` — the possession construction (`verbal-system.md` §13)
- `#transfer` — the transfer extension of the possession construction
- `#interrogative` — questions and the polarity particle *ea* (`verbal-system.md` §5.5)
- `#conditional` — conditional clauses
- `#existential` — existential / presentational clauses (`language_reference.md` §4)
- `#speech` — talk / speak verbs and the register contrast (`verbal-system.md` §12.7)
- `#duration` — durative / "for a long time" adverbials

---

## 5. Entries

### E001 {#E001}

- **Conlang:** Ŕeus | bémmo | oų | rĩbii·hii. | Oų | riis·hii | o | noê.
- **IPA:** /ɾ̥ɛ:s bɛm:o õ: ɾɪbihi. õ: ɾis:i o no'ɛ/
- **Etymological:** Today.is | (a)bit.more | on.the | nippy.side. | On.the | nice.side | though | (i)n.a.way.
- **Leipzig:** today\COP bit-CMPR on-DEF nippy-NMLZ ‖ on-DEF nice-NMLZ though in-DEF-way
- **Translation:** "It's a little more chillier today, in a pleasant kind of way."
- **Tags:** #weather #comparative #hedging
- **Cited from:** `dictionary.md` (ŕe)
- **Added:** 2026-05-10
- **Revised:**
  - 2026-06-26: Re-encoded the Conlang and Etymological lines into `|`-aligned chunks (v0.2 format). Content, IPA, and analysis unchanged.
- **Notes:** Seed entry for the corpus. The IPA and Leipzig layers are first-pass and pending author review. Specific items flagged: (a) the realization of `Ŕ` (acute over r) is transcribed as voiceless /r̥/ on placeholder grounds and needs reconciliation with `phonology.md`; (b) the nasalization marked by `ų` is transcribed as a coda /ŋ/ rather than vowel nasalization — also pending reconciliation with `phonology.md` §4; (c) the morpheme-boundary middle dot in `rĩbii·hii` and `riis·hii` is treated as orthographic-only and is not reflected in the IPA; (d) the Leipzig glosses `NMLZ` for `-hii` and the analysis of `o noê` as `in-DEF-way` are tentative and will firm up as the recognitional-habitual and adverbial constructions are committed.

---

### E002 {#E002}

- **Conlang:** Rimmase | spli·oþw.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** 1SG.LVC.NVOL.PST split-CONCORD
- **Translation:** "I drifted off / I got split off (from the group)."
- **Tags:** #concord #frame
- **Cited from:** `verbal-system.md` §4.2
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §4.2 (passive-shaped concord); now transcluded via token (roadmap B1b). Etymological line deferred — source words un-entered (dictionary batch D4). The passive shape is conflated here with the separative satellite *oþw*; disambiguating shape from satellite needs an overt-participle stem. **[Open]**

### E003 {#E003}

- **Conlang:** Rhii | riauset | rekriiâkm | nopiiem.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** 1PL get.oneself.IPFV chat.IDEO-CONCORD evening
- **Gesture (χ):** wrist rotation, "and so on"
- **Translation:** "We were chatting in the evening."
- **Tags:** #ideophone #concord #frame
- **Cited from:** `verbal-system.md` §4.2.3; `ideophones.md` §4
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from inline blocks that appeared in **two** documents — `verbal-system.md` §4.2.3 (ideophone-as-predicate) and `ideophones.md` §4 (the gesture-bearing copy) — now collapsed to one record (the dedup case that motivates centralization). Both sites now transclude via token. Etymological line deferred — *rekriiâ*, *nopiiem* pending (dictionary batch D4). `nopiiem` < *on the P.M.* "(in the) evening."

### E004 {#E004}

- **Conlang:** Rimmase | ię | þ | rishś, | a | bayen, | een | een.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** 1SG.LVC.NVOL.PST do.CONCORD REC dish-ITER on 1SG.end again again
- **Translation:** "I got (myself) doing the dishes, on my end, again and again."
- **Tags:** #recognitional-habitual #possession #frame
- **Cited from:** `verbal-system.md` §7.2
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §7.2 (frame meets the recognitional nominal); now transcluded via token. Etymological line deferred. The deverbal nominal *þ rishś* takes the recognitional exponent *þ* (not the merged article *o*) and the helper verb *ię* (< GA *doing*) on the get-oneself side.

### E005 {#E005}

- **Conlang:** Enniip | ounoheun | splitn.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** MP.ENDUP.PST LVC.VOL.IPFV split-CONCORD
- **Translation:** "It ended up that (they) went ahead and left."
- **Tags:** #matrix-particle #frame-aspect
- **Cited from:** `verbal-system.md` §11
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §11 (matrix particles); now transcluded via token. Etymological line deferred (particle members pending dictionary entries). The end-up particle forces the imperfect: the clause surrenders its own aspect to the imperfect frame *ounoheun*.

### E006 {#E006}

- **Conlang:** Rhi·iiniies | ounahen | splitn.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** MP.NEED LVC.VOL.HAB split-CONCORD
- **Translation:** "What I need is to leave."
- **Tags:** #matrix-particle
- **Cited from:** `verbal-system.md` §11.2
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §11.2 (really-need particle); now transcluded via token. Etymological line deferred. Frame-form spelling *ounahen* pending the §2.4 paradigm question. **[Provisional]**

### E007 {#E007}

- **Conlang:** Reś | beųheun | split.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** MP.GUESS LVC.VOL split
- **Translation:** "Apparently (they) left."
- **Tags:** #matrix-particle #evidential
- **Cited from:** `verbal-system.md` §11.2
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §11.2 (guess particle); now transcluded via token. Etymological line deferred. *Reś* (< GA *I guess*) marks the clause as held at one remove — hearsay or inference, with no commitment to which.

### E008 {#E008}

- **Conlang:** Nóuśshè | beųheun | split.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** MP.SUMM LVC.VOL split
- **Translation:** "Long story short, (they) left."
- **Tags:** #matrix-particle
- **Cited from:** `verbal-system.md` §11.2
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §11.2 (summary particle); now transcluded via token. Etymological line deferred. **Constructed example:** *nóuśshè* is attested as a member (Translation Exercise #2), but this particular clause has not been elicited and awaits confirmation. **[Provisional]**

### E009 {#E009}

- **Conlang:** Ei | o | nóè.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** 3SG QUOT "no.way"
- **Translation:** "She was like, 'No way.'"
- **Tags:** #quotative
- **Cited from:** `verbal-system.md` §12
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §12 (quotation); now transcluded via token. Etymological line deferred. The quotative verb *o* (< GA *go*) takes its content after it.

### E010 {#E010}

- **Conlang:** Beunheumm | rhentt, | rhemmemmêm.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** 1SG.VOL say.PRF, IDEO
- **Gesture (χ):** back-of-hand rhythmic clap
- **Translation:** "I said it — boom, boom, boom."
- **Tags:** #quotative #ideophone
- **Cited from:** `verbal-system.md` §12.1; `ideophones.md` §1
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from inline blocks in **two** documents — `verbal-system.md` §12.1 and `ideophones.md` §1 (the gesture-bearing copy) — collapsed to one record (a dedup case). Both sites now transclude via token; the verbal-system copy glossed the ideophone slot as "[boom-boom-boom]," the ideophones copy as "boom, boom, boom" (the latter taken as canonical). Etymological line deferred; the *an'+went* → *-mm* gemination in *beunheumm* is a pending phonology item.

### E011 {#E011}

- **Conlang:** Eia | quo | ounoheun | meiknet.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** 3SG QUO LVC.VOL.IPFV come-CONCORD
- **Translation:** "She said she'd come."
- **Tags:** #quotative
- **Cited from:** `verbal-system.md` §12.2
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §12.2 (indirect report); now transcluded via token. Etymological line deferred. An indirect report needs only the source marker *quo*; the embedded clause keeps its own shape, with no quote boundary.

### E012 {#E012}

- **Conlang:** Bentt | oðerren | quo, | o | mau | ouhen | meiktt.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** say.PST 3SG.STR QUO, Q.OPEN 1SG LVC.VOL.HAB come-CONCORD
- **Translation:** "She was like, 'I'll come.'"
- **Tags:** #quotative
- **Cited from:** `verbal-system.md` §12.2
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §12.2 (direct quote); now transcluded via token. Etymological line deferred; *bentt* frame morphology pending. A direct quote is set off by clause-initial *quo* plus the opener *o*, and reproduces the quoted material verbatim — including its own first person (*mau*).

### E013 {#E013}

- **Conlang:** Bauyen, | e | o | quo | "þiiaii".
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** 1SG.STR, 1SG QUOT QUO "finally"
- **Translation:** "Me, I was like, 'Finally!'"
- **Tags:** #quotative
- **Cited from:** `verbal-system.md` §12.2
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §12.2 (quote-oneself); now transcluded via token. Etymological line deferred. Turning *quo* on one's own thought reports an internal reaction never spoken aloud; the left-dislocated strong pronoun *bauyen* reads as taking a conversational turn. Works cleanly only in the first person. **[Provisional]**

### E014 {#E014}

- **Conlang:** Ei | o, | ohei | meikntt | ea.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** 3SG QUOT, Q.DIR come-CONCORD Q
- **Translation:** "She went, 'Coming?'"
- **Tags:** #quotative
- **Cited from:** `verbal-system.md` §12.3
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §12.3 (clipped quoted question); now transcluded via token. Etymological line deferred. The quoted question is clipped (subjectless), licensed by the interrogative and marked by *ohei* (< GA *oh hey*).

### E015 {#E015}

- **Conlang:** Rimmaseu | beikw.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** 1SG.LVC.NVOL.PST=ART vehicle
- **Translation:** "I have a vehicle."
- **Tags:** #possession #frame
- **Cited from:** `verbal-system.md` §13
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §13 (possession construction); now transcluded via token. Literally "got myself a vehicle." Etymological line deferred; the final lengthened vowel of *rimmaseu* is the fused etymological article, and its gloss segmentation is pending.

### E016 {#E016}

- **Conlang:** Ritm | o | rhémstwè.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** get.3PL ART book
- **Translation:** "(I/they) gave them the book."
- **Tags:** #possession #transfer
- **Cited from:** `verbal-system.md` §13.2
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §13.2 (transfer extension); now transcluded via token. Literally "got them the book." Etymological line deferred. With a recipient in the *get*-slot the possession construction causativizes into giving, volition-neutral by default.

### E017 {#E017}

- **Conlang:** Beunheun | þil·tm·ę·aų·et, | o | riųś.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** LVC.VOL fill.in-PFV-3PL-on-3SG, ART news
- **Translation:** "I told her the news."
- **Tags:** #possession #transfer
- **Cited from:** `verbal-system.md` §13.2
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §13.2 (abstract-possessum transfer / informing); now transcluded via token. Literally "went ahead and filled 'em in on it — the news." Etymological line deferred; fine segmentation of *þil·tm·ę·aų·et* — *þil* fill, *-tm* perfective, *-ę* recipient ('em), *-aų* "on," *-et* theme ('it') — pending confirmation. Definite *riųś* "the news" does not occupy the theme slot (filled by clitic *-et*) and is supplied separately as an appended clarification. **[Open]**

### E018 {#E018}

- **Conlang:** …ebıĩ | ounoheun | meiknet | ea.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** be.1SG LVC.VOL.IPFV come-CONCORD Q
- **Translation:** "…whether (I) was coming."
- **Tags:** #interrogative #conditional
- **Cited from:** `verbal-system.md` §5.5
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `verbal-system.md` §5.5 (transcluded via token). Etymological line deferred. The conditional brackets the clause with a fronted *ebıĩ* (the inverted "am I") and a clause-final *ea*; it is formally identical to a yes/no question, distinguished only by intonation. The leading `…` marks the embedded fragment. **[Provisional]**

### E019 {#E019}

- **Conlang:** pons | rheĩ.
- **IPA:** /—/ — pending phonology pass
- **Leipzig:** EXIST rain
- **Translation:** "There is rain."
- **Tags:** #existential
- **Cited from:** `language_reference.md` §4
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** Ported from the inline glossed block in `language_reference.md` §4 (transcluded via token). Etymological line deferred; the existential particle *pons* (< GA *(there is) upon us*) is pending a dictionary entry. The unmarked way to predicate of an inanimate or weather subject.

### E020 {#E020}

- **Conlang:** Beunheun | ospokwþ | o | bäeĩyi.
- **Etymological:** (I).went.ahead.and | spoke.with | the | manager.
- **Translation:** "I spoke with the manager."
- **Tags:** #frame #speech
- **Cited from:** `drafts/translation_exercise_2/0615_transl_activity.converted.md` (§A.4.b)
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** **[Provisional — author review pending]** Imported from Translation Exercise #2 (the SAYING round); not yet transcluded anywhere. Demonstrates *ospii* "speak" with the *-wþ* "with" suffix (< GA *with*), which preserves the original *-k* coda as *kw* → *ospokwþ*. Dictionary check: *ospii*, *ospokwþ*, *bäeĩyi* "manager", and the article *o* are all attested. Pairs with the talk/speak register contrast (`verbal-system.md` §12.7, **[Open]**).

### E021 {#E021}

- **Conlang:** Rhii | riauseto | rekriiâ | þri·ei·iiǫ.
- **Etymological:** we | got.ourselves.to | yakitty-yak | for.a.eon.
- **Translation:** "We talked for hours."
- **Tags:** #frame #ideophone #duration
- **Cited from:** `drafts/translation_exercise_2/0615_transl_activity.converted.md` (§A.4.a)
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** **[Provisional — author review pending]** Imported from Translation Exercise #2. The ideophone *rekriiâ* "chat / yak" heads the clause under the get-oneself frame (cf. E003), with infinitive-shaped concord reading the chatter as completed. Dictionary check: *rekriiâ* and *þri·ei·iiǫ* "for a long time" are attested. **Reconciled to canon spelling (flag for review):** the draft wrote *Rhi* (1PL) → canon *rhii* (`verbal-system.md` §5.2), and *riaśeto* → *riauseto* (the get-oneself stem is *riause-*).

### E022 {#E022}

- **Conlang:** Nóuśshè | eia | ounoheun | rhikriutt.
- **Translation:** "Long story short, they're hiring."
- **Tags:** #matrix-particle
- **Cited from:** `drafts/translation_exercise_2/0615_transl_activity.converted.md` (§B.8.a)
- **Added:** 2026-06-28
- **Revised:** —
- **Notes:** **[Provisional — author review pending]** Imported from Translation Exercise #2. An **attested** use of the summary particle *nóuśshè* "in short" (< GA *in a nutshell*) — complements E008, whose *nóuśshè* clause was constructed/unconfirmed. Etymological line deferred (the draft gave no word-for-word gloss). **Reconciled to canon (flag for review):** the draft wrote *rhikriitm* → canon *rhikriutt* "hire / recruit" (dictionary), and *ounohen* → canon *ounoheun* (go-ahead imperfect frame). Demonstrates the matrix particle's clause-initial scope over a framed clause.

---

## 6. Display conventions

This document holds the canonical record (§2). Citing documents do **not** reproduce it; they pull it in at build time with a transclusion token, and each pipeline renders it in the style that context wants. The token:

```
<!-- example: E001 -->
```

The build expands it in place, resolving the style from the host document (overridable as `<!-- example: E001 | dictionary -->`). The three target styles:

- **Dictionary (inline).** Conlang + Translation only, flowing inline in the entry's prose — conlang italicized, translation in double quotes — so the dictionary body stays dense. No block, no ID, no gloss.

  > *Ŕeus bémmo oų rĩbii·hii. Oų riis·hii o noê.* "It's a little more chillier today, in a pleasant kind of way."

- **Reference grammar, HTML.** The aligned Conlang and Etymological chunks render as an **interactive** two-row gloss: hovering a chunk highlights its counterpart on the other row, each chunk in a distinct color. The Translation runs free below. (Leipzig is held dormant — §2.)
- **Reference grammar, PDF.** The same two rows, set in a fixed-width face with **deterministic column padding** so the chunks align in print. Translation free below.

The `|`-chunk alignment in §2 is what makes both the HTML highlight and the PDF columns possible — chunk *i* of the two rows is one unit. The renderers themselves are built in a later milestone (see `planning/examples-system-roadmap.md`, Milestones A2/G); this section fixes the contract they implement.

An inline `§E001` *mention* (as opposed to the transclusion token) resolves to a hover-card on the site, not a rendered block.

---

## Versioning notes

### v0.5, June 2026 — draft-translation import begun (roadmap B2, pilot)

First entries imported from the `/drafts` translation exercises per the locked draft-import bar — **E020–E022**, a pilot batch from Translation Exercise #2 (`drafts/translation_exercise_2/0615_transl_activity.converted.md`): "I spoke with the manager," "We talked for hours," "Long story short, they're hiring." All marked **[Provisional — author review pending]**; each carries a source-draft pointer, a dictionary stub-check, and explicit **conflict flags** where a draft spelling was reconciled to canon (e.g. *Rhi*→*rhii*, *rhikriitm*→*rhikriutt*, *ounohen*→*ounoheun*) — reconciled, not silently overwritten, for the author to confirm. These entries are **corpus-only**: not transcluded into any document until reviewed. Where the draft supplied a brace gloss it became the Etymological line (E020/E021 align 4/4); otherwise it is deferred (E022). Tags `#speech`, `#duration` registered. The remaining ~25 exercise sentences and the other draft sources are pending (multi-session).

### v0.4, June 2026 — grammar examples tokenized; corpus to E019 (roadmap B1b)

Tokenization of the ported grammar examples (B1b), unblocked by the greedy renderer (which shows the present Leipzig line and skips the absent etym / placeholder IPA) and the auto-regenerated previews (G0a/G0b). Changes:

- **Inline grammar blocks replaced with tokens.** `verbal-system.md` (E002–E018), `ideophones.md` (E003, E010), and `language_reference.md` (E019) now transclude their examples at build time; the corpus is the single source in fact, not only in principle. Each ported entry's Notes updated from "retained pending tokenization" to "transcluded via token."
- **Two further examples swept in (E018, E019).** The first-pass survey missed the conditional *…ebıĩ ounoheun meiknet ea* (`verbal-system.md` §5.5) and the existential *pons rheĩ* (`language_reference.md` §4) — the survey regex required a capitalized first word and did not cover `language_reference.md`. Both added; tags `#interrogative`, `#conditional`, `#existential` registered.
- **Per-call layer suppression in use.** The two cross-doc duplicates (E003, E010) render greedily in `ideophones.md` (χ gesture shown) but with `| -gesture` in `verbal-system.md`, keeping the χ convention scoped to the document that defines it — the first real use of the blockable-layer feature.

### v0.3, June 2026 — grammar examples ported (roadmap B1)

Corpus grew from one entry to seventeen: the standalone glossed example blocks in `verbal-system.md` and `ideophones.md` were swept in as **E002–E017** (roadmap Milestone B1). What changed:

- **Sixteen examples ported.** Each entry preserves the source block's layers — Conlang (now `|`-chunked, grain set by the Leipzig units), IPA (placeholders carried verbatim), Leipzig (preserved, not displayed), Translation — plus the analytical `[Placeholder]` caveats moved into Notes. GA-English paraphrases (e.g. `verbal-system.md` §6.2/§6.3) and all-placeholder paradigm skeletons (§4.3, §15) were **not** ported — they are illustrations, not attested corpus material.
- **Two cross-doc duplicates collapsed.** *Beunheumm rhentt, rhemmemmêm* (E010) and *Rhii riauset rekriiâkm nopiiem* (E003) each appeared in two documents; each is now one record, with both sites listed under *Cited from*. This is the dedup case that motivates centralization.
- **Gesture (χ) field (§2).** Added to the open schema for the multimodal (ideophone) entries that carried a χ gesture line in `ideophones.md`.
- **Deferred Etymological line (§2).** New convention: an entry may omit the Etymological line while its GA derivation is unrecoverable (source words pending dictionary batch D4). The Conlang line is chunked regardless, so the aligned row slots in later at equal count; the equal-chunk guard fires only when both lines are present. All sixteen new entries use this — none has an Etymological line yet.
- **Tag registry (§4).** Added `#concord`, `#frame`, `#frame-aspect`, `#ideophone`, `#quotative`, `#matrix-particle`, `#evidential`, `#possession`, `#transfer`.

**In-prose tokenization deferred.** The inline copies in `verbal-system.md`/`ideophones.md` are **retained**, not yet replaced with `<!-- example: EXXX -->` tokens. Flipping them waits on either the D4 dictionary batch (to author the Etymological lines) or a grammar renderer that emits the preserved interlinear — otherwise tokenizing now would drop the visible Leipzig gloss for a thinner block. Tracked in `planning/examples-system-roadmap.md` (B1). The corpus is the single source from this point; the inline copies are a temporary, flagged overlap.

### v0.2, June 2026 — chunk-aligned, open-schema, build-time source

Data-model overhaul for the centralized-examples system (`planning/examples-system-roadmap.md`, Milestone A1). Changes:

- **`|`-chunk alignment (§2).** The Conlang and Etymological lines are now split on `|` into aligned chunks (chunk *i* ↔ chunk *i*), the unit renderers highlight (HTML) or pad into columns (PDF). The build requires equal chunk counts and fails loudly on a mismatch. E001 re-encoded; content/analysis unchanged.
- **Leipzig deferred (§2).** Held dormant — no renderer emits it until the gloss inventory settles. Existing lines preserved, not displayed.
- **Open schema (§2).** Records are extensible; future fields (audio, per-chunk notes) add without migration. Parsers ignore unknown fields.
- **Build-time source only (§2, §6).** This document is no longer published as an HTML page or PDF chapter. Citing docs transclude via `<!-- example: EXXX -->`; `§EXXX` mentions resolve to a site hover-card. §6's reference-grammar display, formerly `[Open]`, is now specified: interactive aligned gloss (HTML), monospace columns (PDF), inline conlang+translation (dictionary).
- **Parser (`site/scripts/parse.mjs`).** `parseExamples` now emits `{ conlang, segments[], ipa, translation, tags, slug }` (the joined `conlang` kept for the existing hover-card). The transclusion renderers and the site-page removal land in Milestone A2.

### v0.1, May 2026 — initial scaffold

Document created as a sibling reference, parallel to `phonology.md`, `orthography.md`, `verbal-system.md`, and `dictionary.md`. Established:

- **Sibling-doc status.** This document is the single source of truth for glossed example sentences. Other documents cite entries by ID (`examples.md §EXXX`) rather than reproducing glosses inline.
- **Entry format (§2).** Five gloss layers (Conlang, IPA, Etymological, Leipzig, Translation) plus metadata fields (Tags, Cited from, Added, Revised, Notes). Stable zero-padded IDs (`E001`, `E002`, …); IDs never reused.
- **Etymological-gloss conventions (§3).** Periods for fused morphemes, parentheses for phonologically lost GA material, middle dot `·` in the Conlang line for fused-orthography morpheme boundaries.
- **Tag registry (§4).** Seeded with `#weather`, `#comparative`, `#hedging`, `#recognitional-habitual`.
- **Per-entry change tracking.** `Added` field for creation date; `Revised` field for substantive-change log inside the entry. Doc-level versioning notes here track structural changes to the document itself, not per-entry edits.

Corpus seeded with **E001** (weather / comparative / hedging). E001's IPA and Leipzig layers are flagged in its Notes as first-pass and pending author review.

**Not yet propagated.** No sibling document yet cites this file. When the first cross-reference is added, update `language_reference.md` §8 (doc set list) and `CLAUDE.md` (Document hierarchy) to register `examples.md` as a sibling reference.
