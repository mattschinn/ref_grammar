# Spelling → IPA (first-pass drafter)

**Version:** v0.1 (June 2026)
**Companion implementation:** `spell2ipa.py`
**Pinned to:** `orthography.md` v3.

A deterministic single-pass converter that turns a dialect-spelled word into a broad IPA transcription. It is a *drafter*, not an oracle: the output is meant to be read and corrected by a human, and it deliberately does not model phonetic detail that the spelling does not encode. The reverse direction (IPA → spelling) is out of scope for this version, because it depends on a canonical machine-IPA convention that does not exist yet (pitch is absent from current transcriptions, and notation drifts across the lexicon).

Status tags follow the project convention (**[Settled]** / **[Provisional]** / **[Open]**).

---

## What it does and does not do

It converts spelling to a broad phonemic IPA good enough to seed a dictionary entry or feed a rough pronunciation. It does **not** aim for surface-phonetic accuracy, does not resolve morphological structure (compounds, clitics), and does not consult the lexicon. Everything it knows comes from the grapheme string in front of it.

Because it is purely string-driven, a handful of phenomena that depend on information the spelling withholds are out of scope by design (see *Known divergences*). These are documented, not bugs.

---

## Pipeline

The converter runs one left-to-right pass in five stages:

1. **Normalize.** NFC-normalize the input; map dotless `ı` → `i`; drop the interpunct `·` (hiatus is already carried by the doubled-vowel graphemes).
2. **Peel prosody.** Separate pitch and stress off the vowels into side channels — acute on a vowel is pitch, grave is stress, circumflex is both. Crucially, marks that are *phonemic* stay attached: ogonek and tilde (nasalization), acute on a consonant (devoicing: `ś ń ḿ ŕ`), and caron (`š`).
3. **Tokenize.** Maximal-munch match against the ordered grapheme list (Table A, then Table B). Longest grapheme wins at each position.
4. **Resolve context.** Apply the rules that need neighbours: `s`-voicing, doubled-consonant gemination, labialized `kw`, the syllabic appendix, and nasal-glide assimilation.
5. **Re-apply prosody.** Put the high-tone mark back on any pitched vowel, and place a single primary stress (`ˈ`) — at the grave if one was written, otherwise before the final syllable (stress is predictably final).

---

## Table A — multigraph graphemes (matched first, longest to shortest)

| Grapheme | IPA | Note |
|---|---|---|
| `iiy` | /iː/ | beats `ii` |
| `iia` | /i.a/ | hiatus |
| `iyi` | /i.i/ | hiatus, `y` is the boundary |
| `iie` | /iɛ/ | bimoraic long diphthong |
| `aų` `eų` `ių` `oų` | /ɑ̃ː ɛ̃ː ɪ̃ː õː/ | long nasals (ogonek on `u`) |
| `rh` `rr` | /ɻ/ | `rr` = non-initial spelling of `rh` (orthography.md); beats `r` |
| `tt` | /ʔ/ | glottal-stop spelling, **not** a `t`-geminate |
| `ts` | /ts/ | affricate; also keeps the `s` voiceless |
| `cqu` `kkw` | /kʷː/ | labialized geminate |
| `qu` | /kʷ/ | |
| `au` `eu` `iu` `ou` | /ɑ ɛː ɪː oː/ | `au` is **short** /ɑ/ (the one non-lengthening `Vu`; orthography.md v3.7); `eu iu ou` long; `iu` phonemic /ɪː/ |
| `ei` | /ei/ | diphthong |
| `ii` | /i/ | short tense |
| `iĩ` | /ĩ/ | nasalized `ii` digraph (the dotless-i rule, with tilde) |
| `ia` | /ia/ | diphthong |
| `ea` `aa` `ee` `oo` | /e.a a.a e.e o.o/ | hiatus |

`kw` is **not** in this table: it is /kʷ/ only before a vowel and is resolved contextually (see below), so that a word-final `w` can instead be read as a syllabic appendix.

## Table B — single graphemes

| Grapheme | IPA | | Grapheme | IPA |
|---|---|---|---|---|
| `s` | /s/ or /z/ (contextual) | | `i` | /ɪ/ |
| `ś` | /s/ | | `e` | /ɛ/ |
| `š` | /ʃ/ | | `a` | /ɑ/ |
| `r` | /ɾ/ | | `o` | /o/ |
| `ŕ` | /ɾ̥/ | | `æ` | /æ/ |
| `ń` `ḿ` | /n̥ m̥/ | | `œ` | /oe/ |
| `þ` `ð` | /θ ð/ | | `ą` `ę` `ǫ` | /ɑ̃ ɛ̃ õ/ |
| `y` `w` | /j w/ | | `ĩ` | /ĩ/ |
| `ỹ` `w̃` | /j̃ w̃/ | | `ʔ` | /ʔ/ (literal) |
| `b d f g h k l m n p t` | expected values | | | |

## Overlay — diacritics on vowels

- **Acute → pitch.** High tone on that vowel: `é` → /ɛ́/.
- **Grave → stress.** Places `ˈ`; otherwise stress defaults to the final syllable.
- **Circumflex → pitch + stress** on the same vowel.
- **Dotless `ı` → `i`** before matching.

---

## Contextual rules

**`s`-voicing.** `s` is /s/ word-initially **or** when adjacent to a voiceless obstruent (`p t k`, including the `ts` affricate); it is /z/ elsewhere. The voiceless-adjacency clause is now **[Settled]** — committed to `orthography.md` §2.2 (v3.5) after validation against the dictionary's cluster forms (*beusp* /bɛːsp/, *benskyi* /bɛnˈski/, *ritsstw*). Word-*final* bare `s` is **/z/** (no word-final devoicing — owner ruling, `orthography.md` §2.2); the converter's /z/ output is correct, and a form with a true final /s/ is spelled `ś` (e.g. *récquıìś*).

**Doubled-consonant gemination.** Any doubled consonant letter → geminate /Cː/. This generalizes the documented `ss nn pp` to whatever else appears — validation surfaced `mm` and `ww` (*emmáwwè* /ɛmːˈɑwːɛ/). The two exceptions are `tt` (→ /ʔ/) and the labialized geminates `cqu`/`kkw`, both handled in Table A before this rule fires.

**Labialized `kw`.** /kʷ/ only when a vowel follows (*rékwıì* /ɾɛˈkʷi/); a word-final `w` is left for the appendix rule.

**Syllabic appendix.** A word-final `w` or `y` after a consonant is a syllabic appendix: /w̩/, /j̩/ (*barnkw* /ˈbɑɾnkw̩/, *toutw* /ˈtoːtw̩/). This is a cheap heuristic, not a real syllabifier.

**Nasal-glide assimilation.** A glide immediately after a nasalized vowel is itself nasalized (*ęy* → /ɛ̃j̃/), since the orthography leaves this predictable nasalization unwritten.

---

## Known divergences (documented scope limits)

Validated against 59 dictionary headwords with non-`[Open]` IPA. After setting aside the divergences below, segmental agreement is **44/57** comparable forms (two dictionary entries had no usable IPA). The gap is mostly the dictionary's own inconsistency, not converter error — which is itself a useful by-product: round-tripping the lexicon through this tool flags entries to clean up.

- **Pitch is added, not matched.** The converter marks pitch from the acute; most dictionary IPA omits it. Converter output is *more* marked, and arguably more correct.
- **Stress position differs.** The dictionary marks stress inconsistently (sometimes on the historical-pitch syllable, sometimes final, sometimes not at all). The converter always emits one stress at the final syllable (or the written grave). Don't expect stress-position parity.
- **Final-stop glottalization is not modelled.** Word-final `t` surfaces as [ʔ] in the dictionary (*nobêt* /noˈbɛʔ/) but the converter emits /t/. Allophonic, out of scope.
- **`iu` is phonemic /ɪː/** by decision; the dictionary sometimes writes phonetic /ɨː/.
- **Non-ligature `oe`** is read as /oɛ/ (its compositional value). Whether the letter sequence `oe` is a licensed spelling of the diphthong /oe/ is `orthography.md` §6 **[Open]**; *boeś* /boes/ assumes the diphthong reading.
- **`ŕ` → /ɾ̥/ and `ę` → /ɛ̃/** per `orthography.md`. The dictionary writes /r̥/ and /ẽ/ for these. The converter follows the orthography document; the mismatch is a dictionary-side inconsistency to reconcile in a dictionary session.
- **Reduplicated ideophones** (*skwkw* /skʷkʷ/) carry lexical labialization on a final `kw` that the appendix default reads as /kw̩/. Rare; lexical.

---

## Open decisions (need a ruling before v0.2)

1. **Word-final bare `s` — [Resolved 2026-06-22].** Ruled /z/: there is no word-final devoicing. Committed to `orthography.md` §2.2 (v3.5). The sole counter-datum, *récquıìs* /ˈɾɛkʷːis/, was respelled *récquıìś* (its final /s/ < GA *likewise* /z/ is a lexical exception, spelled with the devoicing diacritic). The converter already emits /z/ for a bare final `s` and needs no change.
2. **`ŕ` and `ę` values.** Confirm the orthography's /ɾ̥/ and /ɛ̃/ over the dictionary's /r̥/ and /ẽ/, or update one source. This is an `orthography.md` ↔ `dictionary.md` reconciliation, not a converter change.
3. **`oe` letter-sequence** (`orthography.md` §6) — diphthong, hiatus, or error. Resolving it lets the converter stop guessing.

---

## Companion implementation

`spell2ipa.py` (stdlib only). Importable: `from spell2ipa import convert; convert("rhiiynii")` → `/ɻiːni/`. CLI: `python3 spell2ipa.py rhiiynii beussou`. The grapheme tables in the code are the single source of truth and mirror Tables A/B above; if the orthography changes, edit the tables there and re-run validation against the dictionary.

---

## Changelog

### 2026-06-20 — v0.1

Initial draft. Spelling → IPA only. Grapheme tables and overlay finalized with user sign-off; `ts` adopted as a digraph, `iu` set to phonemic /ɪː/, stress emitted finally, hiatus coverage left as-is. Validation against 59 dictionary headwords (44/57 segmental after documented divergences). Refinements surfaced during validation and folded in: voiceless-adjacency clause for `s`; general doubled-consonant gemination (`mm`, `ww`); contextual `kw`; `tt` → /ʔ/; nasalized `ii` digraph; nasal-glide assimilation. Three open decisions logged.
