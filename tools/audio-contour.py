#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
audio-contour.py — stage 3: per-token measurement and contour comparison.

Reads the segment table produced by `audio-split.py`. It does no segmentation of its
own, deliberately: the pilot had two tools each finding their own word boundaries, and
they disagreed, which meant every disagreement between two measurements might have been
a segmentation artefact rather than a fact about the recording. Boundaries are decided
once, in stage 2, and everything downstream cites them.

What it measures, and why this design needs no forced aligner
-------------------------------------------------------------
The Frame A/B items are segmentally identical within a pair -- `óhò` and `ohô` are both
/oho/, `nóè` and `noê` are both /noɛ/. So the whole word is the unit of comparison: take
the F0 track across the token, normalise time to 0-100%, average the repetitions, and
overlay the pair. If prominence placement is real, the peak sits in different halves. No
phone boundaries are required, which matters because no forced aligner exists for
Rickett Yack (see planning/audio-pipeline-plan.md section 7).

Peak position is reported alongside the F0 centroid. Argmax is the intuitive statistic
and the fragile one -- on a nearly flat contour it latches onto noise, so a 2% and a 98%
peak can describe the same shape. The centroid (F0-weighted mean time) degrades
gracefully: a flat contour gives 50% rather than a coin flip.

Usage:
    python tools/audio-contour.py audio/masters/session-01.wav \
        --segments audio/work/session-01-segments.csv \
        --tokens audio/work/session-01-tokens.csv \
        --out audio/work/contours.json --items 1,2,3,4,5,6

Requires: numpy, scipy.
"""
import argparse
import csv
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audiolib import (load, envelope, f0_track, resample_contour,          # noqa: E402
                      db, F0_FRAME_S)

NORM_POINTS = 60


def read_segments(path):
    out = []
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["usable"] != "1" or not r["word_t0"]:
                continue
            out.append({"block": int(r["block"]), "pos": int(r["position"]),
                        "item": int(r["item_id"]), "headword": r["headword"],
                        "frame": r["frame"], "t0": float(r["word_t0"]),
                        "t1": float(r["word_t1"]), "note": r["note"]})
    return out


def measure(x, sr, s, floor_db):
    tok = x[int(s["t0"] * sr):int(s["t1"] * sr)]
    if len(tok) < int(0.05 * sr):
        return None
    f0, voiced, conf, rms = f0_track(tok, sr)
    if voiced.sum() < 5:
        return None
    tt = np.arange(len(f0)) * F0_FRAME_S
    c_f0 = resample_contour(tt[voiced], f0[voiced], NORM_POINTS)
    c_in = resample_contour(tt, db(np.maximum(rms, 1e-9)), NORM_POINTS)
    if c_f0 is None or c_in is None:
        return None
    vt, vf = tt[voiced], f0[voiced]
    span = (vt[-1] - vt[0]) or 1e-9
    # Centroid over the contour's own excursion above its floor, so a flat track lands
    # at 50% instead of being decided by a fraction of a hertz.
    w = np.maximum(c_f0 - c_f0.min(), 1e-9)
    grid = np.linspace(0, 1, NORM_POINTS)
    peak = float(db(np.abs(tok).max()))
    return {
        "block": s["block"], "position": s["pos"], "dur": round(s["t1"] - s["t0"], 3),
        "t0": round(s["t0"], 3), "t1": round(s["t1"], 3),
        "peak_dbfs": round(peak, 1),
        "rms_dbfs": round(float(db(np.sqrt(np.mean(tok ** 2)))), 1),
        "snr_db": round(peak - floor_db, 1),
        "clipped": int(np.sum(np.abs(tok) >= 0.999)),
        "f0_med": round(float(np.median(vf)), 1),
        "f0_min": round(float(vf.min()), 1), "f0_max": round(float(vf.max()), 1),
        "f0_peak_pos": round(float((vt[int(np.argmax(vf))] - vt[0]) / span), 3),
        "f0_centroid": round(float((grid * w).sum() / w.sum()), 3),
        "voiced_frac": round(float(voiced.mean()), 2),
        "f0_contour": [round(float(v), 1) for v in c_f0],
        "int_contour": [round(float(v), 1) for v in c_in],
    }


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("wav")
    ap.add_argument("--segments", required=True)
    ap.add_argument("--items", default=None, help="e.g. 1,2,3,4,5,6 (default: all)")
    ap.add_argument("--frames", default=None, help="e.g. A,B (default: all)")
    ap.add_argument("--tokens", default=None, help="per-token metrics CSV (M6)")
    ap.add_argument("--out", default=None, help="contours JSON (M7)")
    args = ap.parse_args()

    x, sr = load(args.wav)
    lv, _ = envelope(x, sr)
    floor_db = float(np.percentile(lv, 15))
    segs = read_segments(args.segments)
    if args.items:
        want = {int(v) for v in args.items.split(",")}
        segs = [s for s in segs if s["item"] in want]
    if args.frames:
        fr = {v.strip().upper() for v in args.frames.split(",")}
        segs = [s for s in segs if s["frame"].upper() in fr]

    print(f"# Stage 3 measurement - {args.wav}")
    print(f"  session floor {floor_db:.1f} dBFS")
    print(f"  segments in scope: {len(segs)}\n")

    results, meta, dropped = {}, {}, []
    for s in segs:
        m = measure(x, sr, s, floor_db)
        if m is None:
            dropped.append(s)
            continue
        results.setdefault(s["item"], []).append(m)
        meta.setdefault(s["item"], {"headword": s["headword"], "frame": s["frame"]})
    if dropped:
        print(f"## Unmeasurable ({len(dropped)}) - too few voiced frames")
        for s in dropped:
            print(f"  block {s['block']} item {s['item']:2d} {s['headword']}")
        print()

    print("## Per-token summary")
    print(f"  {'item':>4} {'headword':<10} {'fr':>2} {'n':>2}  {'dur':>13}  "
          f"{'F0 med':>8}  {'peak%':>6} {'cog%':>6}  {'peak dBFS':>10} {'clip':>4}")
    for item in sorted(results):
        t = results[item]
        d = np.array([q["dur"] for q in t])
        f = np.array([q["f0_med"] for q in t])
        pk = np.array([q["f0_peak_pos"] for q in t])
        cg = np.array([q["f0_centroid"] for q in t])
        lvl = np.array([q["peak_dbfs"] for q in t])
        nclip = sum(1 for q in t if q["clipped"])
        print(f"  {item:>4} {meta[item]['headword']:<10} {meta[item]['frame']:>2} "
              f"{len(t):>2}  {d.mean():.3f}+-{d.std():.3f}s  {f.mean():6.1f}Hz  "
              f"{100*pk.mean():5.0f}% {100*cg.mean():5.0f}%  {lvl.mean():9.1f} "
              f"{nclip:>4}")

    # Mean time-normalised contour, sampled for the console. The JSON keeps all 60 points.
    print("\n## Mean normalised F0 contour (Hz, 0->100% of token)")
    for item in sorted(results):
        arr = np.array([q["f0_contour"] for q in results[item]], dtype=float)
        mean = arr.mean(axis=0)
        print(f"  {item:>4} {meta[item]['headword']:<10} "
              + " ".join(f"{v:5.0f}" for v in mean[::NORM_POINTS // 12]))

    # Pairwise contrasts, the question the item list was built to answer.
    pairs = [(1, 2, "A: pitch on V1 vs V2, /oho/"),
             (5, 6, "B: declared pitch minimal pair, /noE/"),
             (4, 3, "A: supporting, /hoho(nIt)/")]
    live = [(a, b, lab) for a, b, lab in pairs if a in results and b in results]
    if live:
        print("\n## Contrasts")
        for a, b, lab in live:
            ca = np.array([q["f0_centroid"] for q in results[a]])
            cb = np.array([q["f0_centroid"] for q in results[b]])
            da = np.array([q["dur"] for q in results[a]])
            dbu = np.array([q["dur"] for q in results[b]])
            pooled = np.sqrt((ca.var(ddof=1) + cb.var(ddof=1)) / 2) if min(
                len(ca), len(cb)) > 1 else float("nan")
            d_eff = (cb.mean() - ca.mean()) / pooled if pooled and pooled > 1e-9 else float("nan")
            print(f"  {lab}")
            print(f"    {meta[a]['headword']:<10} n={len(ca)}  cog {100*ca.mean():5.1f}%"
                  f"  dur {da.mean():.3f}s")
            print(f"    {meta[b]['headword']:<10} n={len(cb)}  cog {100*cb.mean():5.1f}%"
                  f"  dur {dbu.mean():.3f}s")
            print(f"    centroid shift {100*(cb.mean()-ca.mean()):+5.1f} pp"
                  f"   Cohen's d {d_eff:+.2f}"
                  + ("   <- predicted direction" if d_eff > 0 else
                     "   <- OPPOSITE of prediction" if d_eff < 0 else ""))
            # Paired within block. The list was blocked precisely so that fatigue and
            # list-final lowering hit both members of a pair equally; pairing spends
            # that design instead of throwing it away. With 5 blocks the sign count is
            # the honest test -- 5/5 is p=0.03 two-tailed, 4/5 is not significant.
            for key, label, scale, unit in (("f0_centroid", "F0 centroid", 100.0, "pp"),
                                            ("dur", "duration   ", 1000.0, "ms")):
                byb_a = {q["block"]: q[key] for q in results[a]}
                byb_b = {q["block"]: q[key] for q in results[b]}
                common = sorted(set(byb_a) & set(byb_b))
                if len(common) < 3:
                    continue
                diff = np.array([byb_b[k] - byb_a[k] for k in common])
                agree = int((diff > 0).sum())
                agree = max(agree, len(common) - agree)   # consistency, either direction
                print(f"    paired {label} n={len(common)}  "
                      f"mean {scale*diff.mean():+7.1f} {unit} "
                      f"(sd {scale*diff.std(ddof=1):.1f})  "
                      f"same-sign blocks {agree}/{len(common)}"
                      + ("  [consistent]" if agree == len(common) else "  [mixed]"))

    if args.tokens:
        os.makedirs(os.path.dirname(args.tokens) or ".", exist_ok=True)
        cols = ["item_id", "headword", "frame", "block", "position", "t0", "t1", "dur",
                "peak_dbfs", "rms_dbfs", "snr_db", "clipped", "f0_med", "f0_min",
                "f0_max", "f0_peak_pos", "f0_centroid", "voiced_frac"]
        with open(args.tokens, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(cols)
            for item in sorted(results):
                for q in results[item]:
                    w.writerow([item, meta[item]["headword"], meta[item]["frame"]]
                               + [q[c] for c in cols[3:]])
        print(f"\nwrote per-token metrics -> {args.tokens}")

    if args.out:
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump({"meta": {str(k): v for k, v in meta.items()},
                       "tokens": {str(k): v for k, v in results.items()}}, f, indent=1)
        print(f"wrote contours -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
