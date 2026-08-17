#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
audio-split.py — stage 2: exact word boundaries for every item in a session.

Stage 1 (`audio-slate-align.py`) answers *which item is where*, to about +-0.5 s.
This answers *where exactly does the word start and stop*, to about 10 ms. The two are
separate problems, and splitting them is what makes the pipeline work — see
planning/audio-pipeline-plan.md section 4.

Method
------
The session is first clustered into *utterances* — runs of speech separated by at least
SEP_S of silence. This is not the segmentation the pilot proved impossible: that one had
to infer item boundaries from silence alone, and failed because within-item and
between-item pauses are identical (0.02 s apart). Clustering into utterances asks a much
weaker question, and it is stable: the group count moves only 303->327 across the whole
parameter grid, a genuine plateau.

Utterances alone still cannot say which is a slate and which is a word. The anchors do
that. Measured on pilot 01 across all 113 rows carrying a real anchor, the digit onset
follows the anchor by +0.22 to +2.67 s (median +1.38, p95 +2.67) and **never precedes
it**. So:

    digit = the first utterance starting at or after the anchor
    word  = the next utterance after it

CORRECTED 2026-08-17 — this rule previously read "the last utterance starting at or
BEFORE the anchor", on the strength of a claim in plan section 4 that the anchor lands
inside its digit while "the word follows 1.3-1.8 s later". The 1.3-1.8 s offset was
measured correctly and labelled wrong: the thing 1.3-1.8 s after the anchor is the
DIGIT, not the word. Taking the last utterance before the anchor therefore grabbed the
PREVIOUS item's word, and everything shifted one position — `slate_t0/t1` held the
previous word, `word_t0/t1` held the slate digit, and the actual word was never
extracted at all. 120 tokens were measured on spoken English numerals before a human
listened to the output and heard "one, two, three".

The shift was invisible to every check that ran, because a uniform shift preserves
utterance counts, anchor spacing and grid stability. Only content identity exposes it,
which is why `--verify` now exists (see audio-verify.py).

Every item is then two utterances, and unanchored items (Whisper missed 11 of 125 slates)
are filled in by consuming utterance pairs between one anchor's word and the next anchor's
digit. Their identity was never in doubt — the reading order fixes it — only their time.

Usage:
    python tools/audio-split.py audio/masters/session-01.wav \
        --anchors audio/work/session-01-anchors.csv \
        --out audio/work/session-01-segments.csv --write-wav audio/work/items

    python tools/audio-split.py audio/masters/session-01.wav --anchors ... --dump 5-60

Requires: numpy, scipy.
"""
import argparse
import csv
import os
import re
import sys

import numpy as np
from scipy.io import wavfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audiolib import (load, envelope, detect_blobs, cluster_blobs,        # noqa: E402
                      group_span, blob_gaps, refine_bounds, db, HOP_S)

SEP_S = 0.30          # utterance separator: above internal closures (50-150 ms), well
                      # below the measured 1.3-1.8 s slate-to-word pause
PEAK_DB = 26.0        # an utterance sits 30-59 dB above the session floor; breath and
                      # mouth noise sit at 13-24 dB and must not be clustered as speech
ANCHOR_SLACK = 0.25   # an anchor may land just AFTER its digit's detected onset
ANCHOR_LEAD_MAX = 3.0 # ...but the digit must start within this long after the anchor.
                      # Measured on pilot 01: anchor->digit onset is +0.22 to +2.67 s
                      # over p95 (median +1.38), and negative on 0 of 113 rows. 3.0 s
                      # admits p95 with margin; the 6 rows beyond it are demoted, not
                      # dropped, and pass 2 recovers them from the reading order.
D2W_MAX = 5.0         # slate-to-word gap ceiling. The typical gap is 1.3-1.8 s, but the
                      # author does occasionally pause for 4 s, and per the revised
                      # protocol that is allowed. A generous ceiling is safe because the
                      # following anchor bounds the search anyway (NEXT_GUARD).
NEXT_GUARD = 0.25     # a word must start before the next item's slate
WORD_MIN, WORD_MAX = 0.20, 1.60
DIGIT_MIN, DIGIT_MAX = 0.15, 1.20
RESPLIT_GAP = 0.15    # internal gap used to rescue an over-long word utterance
WAV_PAD_S = 0.15      # exported WAVs keep padding: word-initial /h/ and aspiration are
                      # real signal, and trimming tight amputates them


def parse_manifest(path):
    """Pull the embedded item CSV out of the generated pilot sheet."""
    if not os.path.exists(path):
        return {}
    m = re.search(r"```csv\s*\n(item_id,.*?)```", open(path, encoding="utf-8").read(), re.S)
    if not m:
        return {}
    return {int(r["item_id"]): r
            for r in csv.DictReader(m.group(1).strip().splitlines())}


def read_anchors(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append({"block": int(r["block"]), "pos": int(r["position"]),
                         "item": int(r["item_id"]),
                         "t": float(r["anchor_t"]) if r["anchor_t"] else None,
                         "anchored": r["anchored"] == "1"})
    rows.sort(key=lambda r: (r["block"], r["pos"]))
    return rows


def utterances(x, sr, sep_s=SEP_S, peak_db=PEAK_DB):
    """Cluster the whole session into utterance spans (start_s, end_s)."""
    lv, _ = envelope(x, sr)
    blobs, floor = detect_blobs(lv, peak_db=peak_db)
    out = []
    for g in cluster_blobs(blobs, sep_s):
        s, e = group_span(g)
        out.append((s, e, float(lv[g[0][0]:g[-1][1] + 1].max() - floor), g))
    return out, floor


def resplit(g, hop_s=HOP_S):
    """Rescue an over-long utterance by taking the last piece after its largest gap.

    An utterance running past WORD_MAX is normally a word with commentary or a false
    start attached. Protocol is last-take-wins, so the tail is the one to keep.
    """
    gaps = blob_gaps(g, hop_s)
    if not gaps or max(gaps) < RESPLIT_GAP:
        return None
    k = int(np.argmax(gaps))
    return group_span(g[k + 1:], hop_s)


def main():
    # Headwords carry diacritics the Windows console codepage cannot encode; without
    # this the report crashes partway through on a legal item name.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("wav")
    ap.add_argument("--anchors", required=True)
    ap.add_argument("--manifest", default="planning/audio-pilot-01.md")
    ap.add_argument("--out", default=None, help="segment CSV")
    ap.add_argument("--write-wav", default=None, help="directory for per-item WAVs")
    ap.add_argument("--sep", type=float, default=SEP_S)
    ap.add_argument("--dump", default=None, help="time range like 5-60; print utterances")
    ap.add_argument("--no-refine", action="store_true",
                    help="skip peak-relative endpoint refinement (for calibration)")
    args = ap.parse_args()

    x, sr = load(args.wav)
    utts, floor = utterances(x, sr, args.sep)
    rows = read_anchors(args.anchors)
    manifest = parse_manifest(args.manifest)

    print(f"# Stage 2 split - {args.wav}")
    print(f"  {len(x)/sr:.1f} s, {sr} Hz, floor {floor:.1f} dBFS")
    print(f"  {len(utts)} utterances clustered at sep={args.sep:.2f}s")
    print(f"  {len(rows)} expected items ({sum(r['anchored'] for r in rows)} anchored)\n")

    if args.dump:
        lo, hi = (float(v) for v in args.dump.split("-"))
        anch = [(r["t"], r["item"]) for r in rows if r["t"] and lo <= r["t"] <= hi]
        ai = 0
        for s, e, pk, _ in utts:
            if not (lo <= s <= hi):
                continue
            while ai < len(anch) and anch[ai][0] < s:
                print(f"      >>> anchor item {anch[ai][1]} @ {anch[ai][0]:.2f}")
                ai += 1
            print(f"  {s:8.2f}-{e:8.2f}  {e-s:5.2f}s  +{pk:.0f}dB")
        return 0

    # --- assign utterances to items ---------------------------------------------
    seg = {}          # row index -> dict
    used_digit = {}   # utterance index -> row index, to catch two anchors colliding
    n = len(utts)

    def take_word(di, limit=None):
        """Utterance after digit index `di` that can be a word; (index, t0, t1, note)."""
        for wi in range(di + 1, min(di + 4, n)):
            s, e, pk, g = utts[wi]
            if s - utts[di][1] > D2W_MAX or (limit is not None and s > limit):
                return None
            if e - s > WORD_MAX:
                r = resplit(g)
                if r and WORD_MIN <= r[1] - r[0] <= WORD_MAX:
                    return wi, s + (r[0] - group_span(g)[0]), s + (r[1] - group_span(g)[0]), \
                        "resplit"
                return wi, s, e, f"long:{e-s:.2f}s"
            if e - s >= WORD_MIN:
                return wi, s, e, ""
        return None

    # Pass 1 - anchored rows. A row whose anchor does not resolve is DEMOTED, not dropped.
    # A bad anchor is a stage-1 misdetection (block 1 item 1 anchored on the session slate
    # "Session one"), and the reading order still fixes the item's identity, so pass 2
    # recovers it exactly as if Whisper had never seen that slate.
    demoted = {}
    for idx, r in enumerate(rows):
        if not r["anchored"]:
            continue
        nxt = next((rows[q]["t"] for q in range(idx + 1, len(rows)) if rows[q]["t"]), None)
        why, w, di, ds, de = None, None, None, None, None
        # The digit is the FIRST utterance starting at or after the anchor. See the
        # module docstring: taking the last one BEFORE the anchor is what produced the
        # one-position shift, because the anchor sits ~1.4 s ahead of its own digit.
        cand = [i for i, u in enumerate(utts) if u[0] >= r["t"] - ANCHOR_SLACK]
        if not cand:
            why = "no utterance after anchor"
        else:
            di = cand[0]
            ds, de = utts[di][0], utts[di][1]
            if ds - r["t"] > ANCHOR_LEAD_MAX:
                why = f"digit {ds-r['t']:.1f}s past anchor"
            elif di in used_digit:
                other = rows[used_digit[di]]
                why = f"slate collides with block {other['block']} item {other['item']}"
            else:
                w = take_word(di, (nxt - NEXT_GUARD) if nxt else None)
                if w is None:
                    why = "no word utterance after slate"
        if why:
            demoted[idx] = why
            continue
        wi, w0, w1, note = w
        used_digit[di] = idx
        seg[idx] = {"di": di, "wi": wi, "d0": ds, "d1": de,
                    "w0": w0, "w1": w1, "note": note}

    # Pass 2 - rows with no usable anchor consume the utterance pairs between the previous
    # item's word and the next resolved item's slate. Identity was never in question.
    anchored_idx = [i for i in sorted(seg) if "wi" in seg[i]]
    for k in range(-1, len(anchored_idx)):
        i = anchored_idx[k] if k >= 0 else None
        j = anchored_idx[k + 1] if k + 1 < len(anchored_idx) else len(rows)
        start = (i + 1) if i is not None else 0
        gap_rows = [q for q in range(start, min(j, len(rows))) if q not in seg]
        if not gap_rows:
            continue
        lo = (seg[i]["wi"] + 1) if i is not None else 0
        hi = seg[j]["di"] if j in seg and "di" in seg[j] else n
        avail = list(range(lo, hi))
        need = 2 * len(gap_rows)
        note = "interpolated"
        if len(avail) > need:
            # Extra utterances mean a retake, a block slate, or commentary. Protocol is
            # last-take-wins and the next slate already caps the range, so the last
            # `need` utterances before it are the takes that count.
            note = f"interpolated|trimmed {len(avail)}->{need}"
            avail = avail[-need:]
        if len(avail) != need:
            for q in gap_rows:
                seg[q] = {"note": f"unanchored: {len(avail)} utterances for "
                                  f"{len(gap_rows)} item(s)"}
            continue
        for m, q in enumerate(gap_rows):
            di, wi = avail[2 * m], avail[2 * m + 1]
            s, e, pk, g = utts[wi]
            if e - s > WORD_MAX:
                rs = resplit(g)
                if rs:
                    s, e = (utts[wi][0] + rs[0] - group_span(g)[0],
                            utts[wi][0] + rs[1] - group_span(g)[0])
            seg[q] = {"di": di, "wi": wi, "d0": utts[di][0], "d1": utts[di][1],
                      "w0": s, "w1": e, "note": note}
    for idx, why in demoted.items():
        s = seg.setdefault(idx, {})
        s["note"] = (s.get("note", "") + "|" if s.get("note") else "") + f"anchor: {why}"

    # --- refine and validate -----------------------------------------------------
    for idx, r in enumerate(rows):
        s = seg.setdefault(idx, {"note": "not reached"})
        if "w0" not in s:
            s["usable"] = 0
            continue
        if not args.no_refine:
            s["w0"], s["w1"] = refine_bounds(x, sr, s["w0"], s["w1"])
        wd, dd = s["w1"] - s["w0"], s["d1"] - s["d0"]
        if not (WORD_MIN <= wd <= WORD_MAX):
            s["usable"], s["note"] = 0, f"word {wd:.2f}s out of range"
        else:
            s["usable"] = 1
            # An odd-length slate is a warning, not a disqualification: nothing is
            # measured on the slate. It only means the utterance the anchor landed on
            # was merged or fragmented, so the word boundary deserves a listen.
            if not (DIGIT_MIN <= dd <= DIGIT_MAX):
                s["note"] = (s.get("note", "") + "|" if s.get("note") else "") \
                    + f"slate {dd:.2f}s odd"

    good = [i for i in seg if seg[i].get("usable")]
    print(f"## Resolution\n  usable segments : {len(good)}/{len(rows)} "
          f"({100*len(good)/len(rows):.0f}%)")
    kinds = {}
    for i in seg:
        k = (seg[i].get("note") or "clean").split(":")[0]
        kinds[k] = kinds.get(k, 0) + 1
    print("  by note         : " + ", ".join(f"{k} {v}" for k, v in sorted(kinds.items())))

    bad = [i for i in sorted(seg) if not seg[i].get("usable")]
    if bad:
        print(f"\n## Rejected ({len(bad)})")
        for i in bad:
            r = rows[i]
            hw = manifest.get(r["item"], {}).get("headword", "")
            at = f"{r['t']:8.2f}s" if r["t"] else "  (unanch)"
            print(f"  block {r['block']} pos {r['pos']:2d} item {r['item']:2d} "
                  f"{hw:<10} {at}  {seg[i].get('note')}")

    print("\n## Per-item yield")
    per = {}
    for i in good:
        per.setdefault(rows[i]["item"], []).append(seg[i]["w1"] - seg[i]["w0"])
    for item in sorted(manifest or per):
        d = np.array(per.get(item, []))
        mi = manifest.get(item, {})
        hw, fr = mi.get("headword", ""), mi.get("frame", "")
        if len(d):
            print(f"  [{fr}] item {item:>2} {hw:<10} n={len(d)}  "
                  f"dur {d.mean():.3f}+-{d.std():.3f}s  ({d.min():.2f}-{d.max():.2f})")
        else:
            print(f"  [{fr}] item {item:>2} {hw:<10} n=0   -- no usable tokens")

    if args.out:
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        with open(args.out, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["block", "position", "item_id", "headword", "frame",
                        "slate_t0", "slate_t1", "word_t0", "word_t1", "dur",
                        "peak_dbfs", "clipped_samples", "usable", "note"])
            for i, r in enumerate(rows):
                s = seg[i]
                mi = manifest.get(r["item"], {})
                base = [r["block"], r["pos"], r["item"], mi.get("headword", ""),
                        mi.get("frame", "")]
                if "w0" not in s:
                    w.writerow(base + ["", "", "", "", "", "", "", 0, s.get("note")])
                    continue
                tok = x[int(s["w0"] * sr):int(s["w1"] * sr)]
                pk = float(db(np.abs(tok).max())) if len(tok) else -99.0
                w.writerow(base + [f"{s['d0']:.3f}", f"{s['d1']:.3f}",
                                   f"{s['w0']:.3f}", f"{s['w1']:.3f}",
                                   f"{s['w1']-s['w0']:.3f}", f"{pk:.1f}",
                                   int(np.sum(np.abs(tok) >= 0.999)),
                                   s.get("usable", 0), s.get("note", "")])
        print(f"\nwrote segments -> {args.out}")

    if args.write_wav:
        os.makedirs(args.write_wav, exist_ok=True)
        for i in good:
            r, s = rows[i], seg[i]
            hw = manifest.get(r["item"], {}).get("headword", "x")
            a = max(0, int((s["w0"] - WAV_PAD_S) * sr))
            b = min(len(x), int((s["w1"] + WAV_PAD_S) * sr))
            wavfile.write(os.path.join(args.write_wav,
                                       f"item-{r['item']:02d}_{hw}_b{r['block']}.wav"),
                          sr, (x[a:b] * 32767).astype(np.int16))
        print(f"wrote {len(good)} per-item WAVs -> {args.write_wav}")
        print("  Padded, unnormalised, unfiltered. Measurement uses the CSV boundaries;")
        print("  these files are for listening and for the site encode.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
