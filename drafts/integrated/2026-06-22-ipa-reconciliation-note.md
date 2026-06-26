# IPA Reconciliation Note

**Created:** 2026-06-20
**Author context:** surfaced by `spell2ipa.py` validation against the dictionary (spelling→IPA converter, v0.1).
**Purpose:** record three confirmed IPA decisions and enumerate every place the source documents diverge from them, so a future session can apply the edits deterministically. This note is a worklist, not an edit — nothing in `dictionary.md`, `orthography.md`, or `phonology.md` has been changed.

The three decisions were confirmed by the project owner. Two of them require edits to `dictionary.md`; one requires an addition to `orthography.md` and touches no dictionary entry. Each is laid out below with its conclusion, its home document, and the exact occurrences.

---

## Decision 1 — `s` is voiceless next to a voiceless obstruent

**Conclusion [Settled].** A non-onset `s` is /z/ by default, **except** when it is immediately adjacent to a voiceless obstruent (`p t k`, including the `ts` affricate), where it is /s/. This generalizes the previously-approved word-initial-only rule and resolves the open registry question of whether the voiceless-adjacency clause (covering `sp`/`sk`) supersedes the narrower rule. It does.

**Home document:** `orthography.md` §2.2 (the `s` / `ś` / `ss` system). The clause should be added there as the governing statement; the converter already implements it.

**Dictionary impact: none.** The affected entries already transcribe these clusters with /s/, so they are *consistent with* the confirmed rule and need no change. They are listed here only as the evidence base and as regression anchors for the converter:

- *beusp* /bɛːsp/ — `sp`
- *benskyi* /bɛnˈski/ — `sk`
- *ritsstw* /ˈritsstw̩/ — `ts` + `st`
- *bessts* /ˈbɛsːts/ — geminate `ss` + `ts`
- *spyi* /spjɪ/ — word-initial `sp`
- *éuskrıì* /ɛːˈskɾi/ — `sk` at the *ice-cream* juncture

**Open sub-question [Open] — do NOT resolve here.** *récquıìs* /ˈɾɛkʷːis/ is the only attestation of a non-onset bare `s` that is neither word-initial nor in a voiceless cluster, and it surfaces as /s/, not /z/. This hints at general word-final obstruent devoicing. A single datum is too thin to act on; flagged for a future judgment call. Note also that no bare intervocalic-medial `s` → /z/ is attested anywhere in the lexicon yet, so the /z/ default is currently un-exercised.

---

## Decision 2 — the devoiced rhotic is /ɾ̥/, not /r̥/

**Conclusion [Settled].** `ŕ` is the devoiced counterpart of the tap `r` /ɾ/, so its value is the devoiced tap **/ɾ̥/**, matching `orthography.md` §2.3. The dictionary transcribes it as /r̥/, which reads as a devoiced trill/approximant the language does not otherwise have. The orthography is authoritative; the dictionary is the side to correct.

**Home document:** `orthography.md` is already correct (`ŕ` → /ɾ̥/). Edits are confined to `dictionary.md`.

### Dictionary occurrences to change (`/r̥/` → `/ɾ̥/`)

Definite — IPA fields:

| Line | Entry | Current | Target |
|---|---|---|---|
| 1138 | *ŕe* | `**IPA:** /ˈr̥ɛ/` | `/ˈɾ̥ɛ/` |
| 1160 | *ŕeut* | `**IPA:** /ˈr̥eːʔ/` | `/ˈɾ̥eːʔ/` |

Consistency — etymology prose and cross-refs in the same two entries (same phoneme, so update for internal consistency):

| Line | Entry | Occurrence |
|---|---|---|
| 1140 | *ŕe* | "/h/ + tap coalescence → /r̥/" |
| 1142 | *ŕe* | cross-ref: "parallel /r̥/ onset" |
| 1162 | *ŕeut* | "…/h/ reanalyzed as devoicing feature → /r̥/" |
| 1164 | *ŕeut* | cross-ref: "parallel /r̥/ onset" |

Judgment — hypothetical pathway note (lower priority):

| Line | Entry | Occurrence | Note |
|---|---|---|---|
| 501 | *éuskrıì* | "…or /kr/→/r̥/ (§4.4.1) collapses the cluster…" | Inside an `[Open]` speculative etymology note about an uncertain pathway. It refers to the same devoiced rhotic, so for consistency it should also read /ɾ̥/, but because the whole clause is provisional, defer to the editor. |

**Leave verbatim — do NOT change (house-style: historical changelog entries are preserved):**

- Line 1321 (changelog 2026-04-30): "the /h/ + tap → /r̥/ coalescence…"
- Line 1322 (changelog 2026-04-30): "*ŕe*'s light-monosyllabic foot /ˈr̥ɛ/ is a counterexample…"

These record past decisions as they were made and should not be retroactively edited.

---

## Decision 3 — nasalized `ę` is /ɛ̃/, not /ẽ/

**Conclusion [Settled].** `ę` is the ogonek nasalization of `e` /ɛ/, so /ɛ̃/, matching `orthography.md` §3.6. The dictionary is in fact almost entirely consistent with this already — *bayarę* /bɑˈjɑɾɛ̃/, *bąêų* /bɑ̃ˈɛ̃ː/, *bęiink* /bɛ̃ˈink/, *beųtw* /bɛ̃ːtw̩/, *reųś* /ˈɾɛ̃ːs/ all use /ɛ̃/. A single entry diverges.

**Home document:** `orthography.md` is already correct. One `dictionary.md` edit.

### Dictionary occurrence to change (`/ẽ/` → `/ɛ̃/`)

Definite — IPA field (keep the nasalized glide /j̃/, change only the vowel):

| Line | Entry | Current | Target |
|---|---|---|---|
| 514 | *ęy* | `**IPA:** /ẽj̃/` | `/ɛ̃j̃/` |

Verify-then-update — non-changelog cross-reference:

| Line | Entry | Occurrence | Note |
|---|---|---|---|
| 1297 | *ęy* | "…glide nasalization in /ẽj̃/ left unmarked…" | Appears to sit in a collation/cross-reference section rather than a dated changelog. If so, update to /ɛ̃j̃/ for consistency. If it turns out to be inside a dated changelog block, leave it verbatim. |

---

## Suggested changelog entry for `dictionary.md`

After applying the edits, add a new dated entry under `## 5. Changelog` (do not overwrite existing ones):

```markdown
### 2026-MM-DD

- IPA reconciliation pass (per ipa-reconciliation-note.md): corrected the devoiced
  rhotic from /r̥/ to /ɾ̥/ in *ŕe* and *ŕeut* (IPA fields, etymology prose, and
  cross-refs), and the nasal vowel from /ẽ/ to /ɛ̃/ in *ęy*. Both align the
  dictionary with orthography.md (`ŕ` → /ɾ̥/, §2.3; `ę` → /ɛ̃/, §3.6). Historical
  changelog mentions of /r̥/ left verbatim. Deferred: the *éuskrıì* hypothetical
  /kr/→/r̥/ note (provisional pathway) and the open question of whether word-final
  bare `s` (see *récquıìs* /ˈɾɛkʷːis/) devoices.
```

## Suggested addition for `orthography.md` (separate session)

In §2.2, record Decision 1 as a [Settled] clause: non-onset `s` is /z/ except when adjacent to a voiceless obstruent (`p t k`, `ts`), where it is /s/. This is the converter's implemented behaviour and resolves the registry's open voiceless-adjacency question.

---

## Summary worklist

- **`dictionary.md`:** 3 definite IPA-field edits (lines 1138, 1160, 514); 4 consistency prose/cross-ref edits (lines 1140, 1142, 1162, 1164); 2 verify-then-update items (lines 501, 1297); 2 leave-verbatim (lines 1321, 1322); 1 new changelog entry.
- **`orthography.md`:** 1 addition (§2.2 `s` voiceless-adjacency clause).
- **Deferred / open:** word-final bare `s` devoicing (one datum, *récquıìs*).
