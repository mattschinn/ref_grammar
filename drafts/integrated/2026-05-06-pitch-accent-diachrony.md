# Pitch Accent as Diachronic Residue

**Status:** Working note, May 2026. Open pending acoustic data.
**Relation to existing docs:** Refines `phonology.md` §3.4 (pitch-stress dissociation). Does not replace it; offered as a candidate reanalysis to be confirmed or revised once recordings are available.

---

## 1. The proposal in one paragraph

The dialect's pitch accent is best analyzed not as an independent prosodic feature but as the **phonetic residue of GA-style prominence** after stress has migrated to the final vocalic position. Speakers do not target pitch as a separate articulatory dimension. They retain the GA prominence on its original syllable (where prominence in English already bundles loudness, length, and F0) and superimpose the conlang's final-stress rule on top. Loudness and length transfer to the final vowel; F0 stays behind on the etymological-stress syllable. The audible "pitch on V₁" pattern falls out of this redistribution, rather than being assigned by a separate rule.

---

## 2. The diachronic pathway

```
Stage 0 (GA):           σ₁ {loud + long + high F0}    σ₂ ...    σₙ {weak}
                        ── full English prominence on the lexically-stressed syllable

Stage 1 (transitional): σ₁ {long + high F0}            σ₂ ...    σₙ {emerging final prominence}
                        ── final-stress constraint begins applying; loudness starts to migrate

Stage 2 (current):      σ₁ {high F0, slight length}    σ₂ ...    σₙ {loud + long, primary stress}
                        ── stress now on σₙ; F0 residue on σ₁
```

The end state has two prominences competing on one word: an inherited one phonetically reduced to mostly F0, and a new one carrying loudness and length. This is the dissociation pattern documented in `phonology.md` §3.4.

The pathway has cross-linguistic parallels. The standard analysis of how Tokyo Japanese pitch accent emerged from earlier accent-with-stress is roughly this — stress simplifies to its F0 correlate while a separate prominence dimension takes over. The development of tone from accent in some Bantu lineages follows a similar shape. The conlang's situation is well-precedented; the design is not inventing a typologically odd configuration.

---

## 3. Status of pitch under this analysis

Pitch is **lexically determined but not synchronically predictable**. This distinction matters and was sharpened in the May 2026 discussion:

- *Etymologically determined* — pitch placement is fully derivable from the GA etymon's stress location. From the historical-linguist's viewpoint, it is a regular reflex.
- *Not synchronically predictable* — from the speaker's viewpoint, with the GA source no longer accessible, pitch placement is lexical information attached to each word. A speaker cannot derive it from the conlang surface form. They have to know it word by word, exactly as English speakers know that *récord* and *recórd* differ.

This is the same epistemic status English lexical stress has. Calling pitch "predictable" in earlier framing was sloppy — it conflated "predictable from the etymon" with "predictable from the surface form," which are very different things.

The implication for typology: pitch is **lexical**, in the sense that lexical-stress systems are lexical. It is not derivable from word shape. Whether it is also **contrastive** (i.e., whether it carries minimal-pair distinctions) is a separate question, treated below.

---

## 4. Why minimal pairs are scarce

The minimal-pair scarcity is not evidence that pitch is weak. It is evidence that English stress is loud — in the information-theoretic sense — and has already eaten most of the territory in which pitch could carry contrast.

The mechanism: English stress is not just a prominence diacritic. It restructures everything around itself. Stressed vowels are full; unstressed vowels reduce to schwa (or elide entirely). Syllable weight, vowel quality, and sometimes segment count all depend on where the GA prominence fell. By the time GA stress has done its work, two words sharing the same stress pattern have largely the same shape; two words with different stress patterns have largely different shapes.

The conlang's cascade compounds this. Vowel mergers, consonant mergers, schwa elision, the appendix system — all of these operate on already-stress-conditioned material. The result is that the residual segmental skeletons that could converge on a homophonous form, while differing only in pitch, almost never exist.

The territory left for pitch to carry contrast is mostly **GA stress-shift derivational pairs** — pairs like *récord* / *recórd*, *présent* / *presént*, *súbject* / *subjéct*, where both members share the same segments under different prominences. These are the cleanest candidates for true conlang minimal pairs distinguishable by pitch alone, because they are exactly the cases where GA's segment-shaping power is held constant across the pair.

**Reframed design question.** The dialect's pitch accent isn't a feature struggling to do work. It is a feature whose potential workspace was mostly absorbed by the segmental consequences of the prominence pattern it descends from. The system isn't failing; it has been outcompeted for territory by its own diachronic ancestor. Low functional load on pitch follows directly — and is not, on its own, evidence about whether pitch is contrastive, allophonic, or vestigial.

---

## 5. Phonetic predictions

If pitch is the residue of softened English prominence rather than an independent F0 target, the V₁ syllable should retain phonetic correlates beyond pure F0:

- **Slight length.** V₁ should be marginally longer than a comparable unstressed vowel, because length was part of the inherited prominence package and would not fully transfer to the final.
- **Slight fullness or amplitude.** V₁ should not reduce all the way to schwa-like quality, even when stress has clearly moved off it.
- **F0 peak roughly aligned with the syllable nucleus**, not displaced to the syllable margin (which would suggest a contour-tone analysis).

A "true" pitch-accent system that had grammaticalized away from its stress origin would have F0 doing the work alone, with V₁ otherwise indistinguishable from any other unstressed vowel. The dialect should *not* look like that under the residue analysis.

These are testable. Acoustic recordings should show whether V₁ is purely an F0 phenomenon or a multi-cue prominence-residue phenomenon. The proposal here predicts the latter.

---

## 6. Implications for the open question

`phonology.md` §3.4 currently has pitch *placement* settled and pitch *contrastiveness* open. Under this analysis:

- Placement is settled (lexically determined, etymologically derivable, synchronically not derivable from surface form).
- Contrastiveness is best treated as a question about whether enough surviving GA stress-shift pairs exist to populate a minimal-pair set. The diachronic cascade does not predict many; whatever exists will be in that derivational corner.
- "Could pitch disappear without disruption?" is a separate question from contrastiveness. Even with low minimal-pair density, the dissociation pattern is acoustically robust and signals etymological-stress location, which is recoverable lexical information. Loss is possible (cf. dialect-level loss of tonal accent in Swedish) but not entailed by low functional load.

The design choice is to leave all of this open pending data, and to commit only to the diachronic framing: pitch as residue, not as independent feature.

---

## 7. Pending work

- **Acoustic recordings** of the designer-speaker (and eventually any acquired speakers) producing forms with predicted dissociation. Specifically: measure F0, length, and amplitude on V₁ versus V_final, and compare V₁ against truly unstressed syllables in matched environments.
- **Stress-shift pair survey.** Identify GA derivational pairs (noun/verb stress shifts; suffix-induced shifts) whose conlang reflexes converge segmentally. These are the candidates for genuine pitch-only minimal pairs.
- **Revision of `phonology.md` §3.4** if the residue analysis is confirmed: reframe pitch from "separate prosodic dimension" to "phonetic residue of preserved GA prominence after stress migration." Keep the orthographic conventions unchanged — pitch still needs marking because it is still lexical, regardless of whether it is analyzed as feature or residue.

---

## 8. Pedagogical note (separate from the analysis)

For GA-speaking learners, the framing matters. "Pitch accent" as a label triggers a mental block: learners begin consciously controlling F0 in unnatural ways and overshoot. The technique implicit in the residue analysis avoids this entirely — say the word with English-style prominence on the etymological-stress syllable, then put extra weight on the final vowel. The pitch pattern emerges automatically without being thought of as pitch.

This is a teaching artifact, not a phonological claim. But it matches the analysis: if pitch is residue rather than target, the right way to teach it is as residue too.
