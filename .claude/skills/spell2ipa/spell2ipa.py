#!/usr/bin/env python3
"""
spell2ipa.py — first-pass spelling -> IPA converter for the dialect.

Deterministic single pass. Not phonetically exact: it is a drafter whose
output a human reviews. Known, deliberate divergences from surface phonetics
are documented in the companion skill file (spell2ipa-skill.md).

Pipeline:
  1. NFC-normalize; map dotless i -> i; interpunct -> syllable dot.
  2. Peel pitch/stress (acute/grave/circumflex on VOWELS) off into side
     channels; keep nasalization (ogonek/tilde) and consonant devoicing
     (acute/caron on consonants) attached to the grapheme.
  3. Maximal-munch tokenize against an ordered grapheme list.
  4. Resolve s-voicing, gemination, labialized stops, syllabic appendix.
  5. Reapply pitch (high tone on the vowel) and place final stress.
"""

import unicodedata

ACUTE, GRAVE, CIRC = "\u0301", "\u0300", "\u0302"
OGONEK, TILDE, CARON = "\u0328", "\u0303", "\u030c"
VOWEL_BASES = set("aeiou")            # y is a consonant in this orthography
VOICELESS_OBSTR = set("ptk")          # for s-adjacency devoicing
IPA_VOWELS = set("ɑɛɪioeaæɨ")         # bare vowel symbols pitch can land on

# --- Ordered multigraph table: longest first. (grapheme, ipa) -------------
MULTI = [
    # 3-unit
    ("iiy", "iː"), ("iia", "i.a"), ("iyi", "i.i"), ("iie", "iɛ"),
    ("aų", "ɑ̃ː"), ("eų", "ɛ̃ː"), ("ių", "ɪ̃ː"), ("oų", "õː"),
    # 2-unit
    ("rh", "ɻ"), ("rr", "ɻ"), ("tt", "ʔ"), ("ts", "ts"),
    ("cqu", "kʷː"), ("kkw", "kʷː"), ("qu", "kʷ"),
    ("au", "ɑ"), ("eu", "ɛː"), ("iu", "ɪː"), ("ou", "oː"),
    ("ei", "ei"),
    ("ii", "i"), ("i" + "ĩ", "ĩ"), ("ia", "ia"),
    ("ea", "e.a"), ("aa", "a.a"), ("ee", "e.e"), ("oo", "o.o"),
]
# --- Single graphemes ------------------------------------------------------
SINGLE = {
    "ś": "s", "š": "ʃ", "r": "ɾ", "ŕ": "ɾ̥", "ń": "n̥", "ḿ": "m̥",
    "þ": "θ", "ð": "ð", "y": "j", "w": "w",
    "b": "b", "d": "d", "f": "f", "g": "g", "h": "h", "k": "k",
    "l": "l", "m": "m", "n": "n", "p": "p", "t": "t", "ʔ": "ʔ",
    "i": "ɪ", "e": "ɛ", "a": "ɑ", "o": "o", "æ": "æ", "œ": "oe",
    "ą": "ɑ̃", "ę": "ɛ̃", "ǫ": "õ", "ĩ": "ĩ",
}
# nasalized approximants (base + combining tilde, no precomposed form)
SINGLE["y" + TILDE] = "j̃"
SINGLE["w" + TILDE] = "w̃"

CONSONANT_LETTERS = set("bdfghklmnpqrstwyþðśšŕńḿ")


def _peel(s):
    """Split into (units, pitch_idx, stress_idx) where units are letter-level
    graphemes (precomposed where possible) and the index sets mark which units
    carry pitch / stress."""
    s = unicodedata.normalize("NFD", s)
    groups = []
    for ch in s:
        if unicodedata.combining(ch) and groups:
            groups[-1].append(ch)
        else:
            groups.append([ch])
    units, pitch, stress = [], set(), set()
    for g in groups:
        base, marks, keep = g[0], g[1:], []
        is_vowel = base in VOWEL_BASES
        for m in marks:
            if m == ACUTE and is_vowel:
                pitch.add(len(units))
            elif m == GRAVE:
                stress.add(len(units))
            elif m == CIRC:
                pitch.add(len(units)); stress.add(len(units))
            else:
                keep.append(m)          # ogonek, tilde, caron, consonant acute
        units.append(unicodedata.normalize("NFC", base + "".join(keep)))
    return units, pitch, stress


def _tokenize(units):
    """Greedy longest-match into [(grapheme, ipa, start_idx, end_idx)]."""
    toks, i, n = [], 0, len(units)
    while i < n:
        matched = False
        # kw is labialized /kʷ/ only before a vowel; word-final w is a
        # syllabic appendix (handled later), so don't consume it here.
        if (units[i] == "k" and i + 1 < n and units[i + 1] == "w"
                and i + 2 < n and _is_vowel_unit(units[i + 2])):
            toks.append(("kw", "kʷ", i, i + 2)); i += 2; continue
        for graph, ipa in MULTI:
            glen = len(graph)               # grapheme key length in codepoints
            # build candidate by consuming whole units until we cover graph
            cand, j = "", i
            while j < n and len(cand) < glen:
                cand += units[j]; j += 1
            if cand == graph:
                toks.append((graph, ipa, i, j)); i = j; matched = True
                break
        if matched:
            continue
        u = units[i]
        # general doubled-consonant gemination (subsumes ss/nn/pp/mm/ww/ll)
        if (i + 1 < n and u == units[i + 1]
                and u in CONSONANT_LETTERS and u not in "ty"):
            base_ipa = SINGLE.get(u, u)
            toks.append((u + u, base_ipa + "ː", i, i + 2)); i += 2; continue
        toks.append((u, SINGLE.get(u, u), i, i + 1)); i += 1
    return toks


def _is_voiceless_edge(ipa, left):
    if not ipa:
        return False
    seg = ipa[-1] if left else ipa[0]
    return seg in VOICELESS_OBSTR or seg == "ʔ"


def _is_vowel_unit(u):
    return bool(u) and (u[0] in VOWEL_BASES or u[0] in "æœąęǫĩ")


def convert(word, mark_stress=True):
    word = unicodedata.normalize("NFC", word).replace("ı", "i").replace("·", "")
    units, pitch, stress = _peel(word)
    toks = _tokenize(units)
    out = []
    vowel_tok_positions = []            # indices into `out` that are syllable nuclei
    for ti, (graph, ipa, a, b) in enumerate(toks):
        # s-voicing: word-initial OR adjacent to a voiceless obstruent -> /s/
        if graph == "s":
            word_initial = (a == 0)
            prev_ipa = toks[ti - 1][1] if ti > 0 else ""
            next_ipa = toks[ti + 1][1] if ti + 1 < len(toks) else ""
            voiceless_ctx = (_is_voiceless_edge(prev_ipa, left=True)
                             or _is_voiceless_edge(next_ipa, left=False))
            ipa = "s" if (word_initial or voiceless_ctx) else "z"
        # syllabic appendix: word-final w/y after a consonant
        if graph in ("y", "w") and b == len(units) and ti > 0:
            prev_graph = toks[ti - 1][0]
            if prev_graph and prev_graph[-1] in CONSONANT_LETTERS:
                ipa = ("j" if graph == "y" else "w") + "\u0329"  # syllabic
        # nasalized glide after a nasalized vowel (predictable, §3.6)
        if graph in ("y", "w") and out and TILDE in unicodedata.normalize("NFD", out[-1]):
            ipa = ("j" if graph == "y" else "w") + TILDE
        # pitch: acute on any source unit in this grapheme -> high tone
        if any(k in pitch for k in range(a, b)):
            ipa = _add_pitch(ipa)
        out.append(ipa)
        if _has_vowel(ipa) or "\u0329" in ipa:
            vowel_tok_positions.append((len(out) - 1, any(k in stress
                                       for k in range(a, b))))
    # stress placement
    if mark_stress and vowel_tok_positions:
        target = None
        for pos, marked in vowel_tok_positions:
            if marked:
                target = pos; break
        if target is None:
            target = vowel_tok_positions[-1][0]      # predictable final
        # back up over the onset consonants of that syllable
        ins = target
        while ins > 0 and not _has_vowel(out[ins - 1]) and "\u0329" not in out[ins - 1]:
            ins -= 1
        out.insert(ins, "ˈ")
    return "/" + "".join(out) + "/"


def _has_vowel(ipa):
    return any(c in IPA_VOWELS for c in ipa)


def _add_pitch(ipa):
    for idx, c in enumerate(ipa):
        if c in IPA_VOWELS:
            return ipa[:idx + 1] + ACUTE + ipa[idx + 1:]
    return ipa


# --------------------------------------------------------------------------
if __name__ == "__main__":
    import sys
    # IPA output is UTF-8; the Windows console defaults to cp1252 and would
    # raise UnicodeEncodeError on glyphs like /ɻ/. Force UTF-8 where supported
    # (Python 3.7+), so the CLI works without a PYTHONUTF8/PYTHONIOENCODING env.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    if len(sys.argv) > 1:
        for w in sys.argv[1:]:
            print(f"{w}\t{convert(w)}")
