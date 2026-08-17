#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
audio-metrics.py — session characterisation and reconciliation for the audio pipeline.

Reads one session master WAV and emits a structured report: format, levels, noise
floor, clipping, utterance inventory, and the pause-hierarchy test that decides
whether the session can be split automatically at all.

This is the "metrics output" stage of `planning/audio-pipeline-plan.md` — everything
acoustic is measured here, in code. Nothing in this file listens to or recognises
speech; identity comes from controlled order plus slating, never from recognition.

Usage:
    python tools/audio-metrics.py audio/masters/session-01.wav [--items 125]

Requires: numpy, scipy.  Run with the anaconda interpreter (see CLAUDE.md notes).
"""
import argparse
import sys

import numpy as np
from scipy.io import wavfile

FRAME_S = 0.010          # analysis frame / hop
FULL_SCALE_16 = 32768.0


def db(v):
    return 20.0 * np.log10(np.maximum(v, 1e-12))


def load(path):
    sr, raw = wavfile.read(path)
    if raw.ndim > 1:
        raw = raw.mean(axis=1)
    if raw.dtype.kind in "iu":
        bits = raw.dtype.itemsize * 8
        x = raw.astype(np.float64) / float(2 ** (bits - 1))
    else:
        bits = raw.dtype.itemsize * 8
        x = raw.astype(np.float64)
    return sr, x, bits, raw.dtype


def frame_levels(x, sr):
    hop = int(FRAME_S * sr)
    nf = len(x) // hop
    fr = x[: nf * hop].reshape(nf, hop)
    return db(np.sqrt(np.mean(fr ** 2, axis=1))), hop


def segment(fdb, floor, thresh_off, max_gap, min_dur, peak_off):
    """Energy segmentation: frames above floor+thresh_off, bridging gaps <= max_gap."""
    idx = np.where(fdb > floor + thresh_off)[0]
    if not len(idx):
        return []
    gap_f = int(max_gap / FRAME_S)
    brk = np.where(np.diff(idx) > gap_f)[0]
    starts = np.concatenate(([idx[0]], idx[brk + 1]))
    ends = np.concatenate((idx[brk], [idx[-1]]))
    out = []
    for a, b in zip(starts, ends):
        if (b + 1 - a) * FRAME_S < min_dur:
            continue
        if fdb[a : b + 1].max() <= floor + peak_off:
            continue
        out.append((a * FRAME_S, (b + 1) * FRAME_S))
    return out


def stability_sweep(fdb, floor, expected):
    """Segment count across a parameter grid.

    A recording with a real pause hierarchy shows a plateau: the count sits near the
    true value across a broad range. No plateau means silence-based splitting cannot
    be trusted on this material, whatever single setting happens to hit the target.
    """
    rows = []
    for off in (10, 12, 14, 16, 18):
        for gap in (0.20, 0.25, 0.30, 0.40):
            n = len(segment(fdb, floor, off, gap, 0.08, 20))
            rows.append((off, gap, n, n - expected))
    counts = np.array([r[2] for r in rows], dtype=float)
    spread = counts.max() - counts.min()
    return rows, spread


def pause_hierarchy_test(segs):
    """The protocol asks for a short within-item pause and a long between-item pause.

    If that hierarchy survived the reading, gaps alternate short/long and the two
    medians separate. If they do not separate, no splitter can tell an item boundary
    from the pause between a slate and its word.
    """
    if len(segs) < 6:
        return None
    st = np.array([a for a, _ in segs])
    en = np.array([b for _, b in segs])
    gaps = st[1:] - en[:-1]
    a, b = np.median(gaps[0::2]), np.median(gaps[1::2])
    return a, b, abs(a - b), gaps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("wav")
    ap.add_argument("--items", type=int, default=125,
                    help="expected item count (reps x list length)")
    ap.add_argument("--extra", type=int, default=7,
                    help="expected non-item utterances (block slates, session/end slates)")
    args = ap.parse_args()

    sr, x, bits, dtype = load(args.wav)
    n = len(x)
    dur = n / sr
    expected = args.items * 2 + args.extra   # slate + word per item

    print(f"# Session metrics - {args.wav}\n")
    print("## Format")
    print(f"  sample rate     : {sr} Hz")
    print(f"  bit depth       : {bits} ({dtype})")
    print(f"  duration        : {dur:.1f} s  ({int(dur//60)}m {dur%60:04.1f}s)")

    peak = np.max(np.abs(x))
    rms = np.sqrt(np.mean(x ** 2))
    clipped = int(np.sum(np.abs(x) >= 1.0 - 1.0 / FULL_SCALE_16))
    print("\n## Levels")
    print(f"  peak            : {db(peak):+.2f} dBFS")
    print(f"  overall RMS     : {db(rms):+.2f} dBFS")
    print(f"  DC offset       : {np.mean(x):+.6f}")
    print(f"  clipped samples : {clipped}")

    fdb, hop = frame_levels(x, sr)
    floor = np.percentile(fdb, 10)
    print(f"  noise floor(p10): {floor:.1f} dBFS")

    rows, spread = stability_sweep(fdb, floor, expected)
    print(f"\n## Segmentation stability (expected ~{expected} utterances)")
    print("  off  gap   count  delta")
    for off, gap, cnt, delta in rows:
        print(f"  +{off:2d}  {gap:.2f}  {cnt:5d}  {delta:+5d}")
    print(f"\n  count spread across the grid: {spread:.0f}")
    if spread > 0.25 * expected:
        print("  VERDICT: no plateau - silence-based splitting is NOT reliable here.")
    else:
        print("  VERDICT: stable plateau - silence-based splitting is viable.")

    # best-effort inventory using the grid point closest to expected
    off, gap, _, _ = min(rows, key=lambda r: abs(r[3]))
    segs = segment(fdb, floor, off, gap, 0.08, 20)
    print(f"\n## Utterance inventory (+{off} dB / {gap:.2f} s bridge) - {len(segs)} found")

    ph = pause_hierarchy_test(segs)
    if ph:
        a, b, diff, gaps = ph
        print("\n## Pause-hierarchy test")
        print(f"  gaps at even positions : {a:.2f} s")
        print(f"  gaps at odd  positions : {b:.2f} s")
        print(f"  separation             : {diff:.2f} s")
        if diff < 0.25:
            print("  VERDICT: hierarchy COLLAPSED - within-item and between-item pauses")
            print("           are indistinguishable. Slate/word boundaries cannot be")
            print("           inferred from silence. Re-record with a longer between-")
            print("           item pause, or label boundaries by hand.")
        else:
            print("  VERDICT: hierarchy intact.")

    if segs:
        st = np.array([a for a, _ in segs])
        en = np.array([b for _, b in segs])
        d = en - st
        pk = np.array([fdb[int(a / FRAME_S):int(b / FRAME_S)].max() for a, b in segs])
        rm = np.array([db(np.sqrt(np.mean(x[int(a * sr):int(b * sr)] ** 2))) for a, b in segs])
        print("\n## Per-utterance distribution")
        print(f"  duration  : median {np.median(d):.2f}s  p10 {np.percentile(d,10):.2f}  p90 {np.percentile(d,90):.2f}")
        print(f"  peak dBFS : p5 {np.percentile(pk,5):.1f}  median {np.median(pk):.1f}  p95 {np.percentile(pk,95):.1f}")
        print(f"  level spread (p95-p5) : {np.percentile(pk,95)-np.percentile(pk,5):.1f} dB")
        print(f"  SNR (median RMS - floor) : {np.median(rm)-floor:.1f} dB")
        if np.percentile(pk, 95) - np.percentile(pk, 5) > 12:
            print("  FLAG: level spread >12 dB - mic distance or delivery varied.")

        cl = np.array([int(np.sum(np.abs(x[int(a*sr):int(b*sr)]) >= 1.0 - 1.0/FULL_SCALE_16))
                       for a, b in segs])
        nbad = int((cl > 0).sum())
        print(f"\n## Clipping\n  utterances containing clipped samples: {nbad} of {len(segs)}")
        for i in np.where(cl > 0)[0]:
            print(f"    {st[i]:8.2f}s  {cl[i]:5d} samples  peak {pk[i]:5.1f} dBFS")

        long = [(a, b) for a, b in segs if b - a > 2.0]
        print(f"\n## Long utterances (>2.0 s): {len(long)}")
        print("  Merged runs or extraneous speech; inspect before splitting.")
        for a, b in long[:25]:
            print(f"    {a:8.2f}-{b:8.2f}  {b-a:5.2f}s")
        if len(long) > 25:
            print(f"    ... {len(long)-25} more")

    return 0


if __name__ == "__main__":
    sys.exit(main())
