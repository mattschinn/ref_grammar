#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
audio-slate-align.py — recover item identity from spoken English digit slates.

The pilot showed that silence structure alone cannot segment a session: within-item
and between-item pauses are indistinguishable (see planning/audio-pipeline-plan.md).
This tool replaces the timing anchor with a *content* anchor.

Design, in one line: Whisper is used as an ANCHOR FINDER, not as a transcriber.

Only English digit tokens are trusted. Everything Whisper says about the conlang is
discarded -- it has no acoustic model for Rickett Yack and will hallucinate English at
it, exactly as the plan predicts. That does not matter, because the expected slate
sequence is known in advance: the detected digits only have to pin enough points for
the known order to fill in the rest. A run of 125 items tolerates a large fraction of
missed digits, since any gap between two correctly-pinned anchors is unambiguous.

Two-stage by design:
  stage 1 (this file)  identity   -- which item is where, to ~0.3 s
  stage 2 (splitter)   boundaries -- precise onsets/offsets by local energy search
                                     inside each pinned interval

Whisper's word timestamps come from cross-attention and are coarse. They are good
enough to say "item 17 is in here" and useless for measuring V1 duration. Never let
stage-1 times reach the measurement stage.

Usage:
    python tools/audio-slate-align.py audio/masters/session-01.wav \
        --order-file planning/audio-pilot-01.md --model openai/whisper-base.en

Requires: numpy, scipy, torch, transformers.
"""
import argparse
import re
import sys
import warnings

import numpy as np
from scipy.io import wavfile
from scipy.signal import resample_poly

warnings.filterwarnings("ignore")

TARGET_SR = 16000
WINDOW_S = 25.0
OVERLAP_S = 5.0
DEDUPE_S = 1.0

ONES = ("zero one two three four five six seven eight nine ten eleven twelve thirteen "
        "fourteen fifteen sixteen seventeen eighteen nineteen").split()
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50}
WORD2NUM = {w: i for i, w in enumerate(ONES)}
WORD2NUM.update(TENS)


def parse_number(tok):
    """Return int for '7', 'seven', 'twenty-two', 'twentytwo'; else None."""
    t = tok.strip().lower().strip(".,!?;:'\"")
    if not t:
        return None
    if t.isdigit():
        return int(t)
    t = t.replace("-", " ")
    parts = t.split()
    if len(parts) == 1:
        return WORD2NUM.get(parts[0])
    if len(parts) == 2 and parts[0] in TENS:
        lo = WORD2NUM.get(parts[1])
        if lo is not None and lo < 10:
            return TENS[parts[0]] + lo
    return None


def load_16k(path):
    sr, x = wavfile.read(path)
    if x.ndim > 1:
        x = x.mean(axis=1)
    if x.dtype.kind in "iu":
        x = x.astype(np.float32) / float(2 ** (x.dtype.itemsize * 8 - 1))
    else:
        x = x.astype(np.float32)
    if sr != TARGET_SR:
        from math import gcd
        g = gcd(sr, TARGET_SR)
        x = resample_poly(x, TARGET_SR // g, sr // g)
    return x.astype(np.float32), sr


def parse_order_file(path):
    """Pull the per-block reading orders out of the generated pilot sheet."""
    blocks, cur = [], None
    with open(path, encoding="utf-8") as f:
        for line in f:
            if re.match(r"^### Block \d+", line):
                if cur:
                    blocks.append(cur)
                cur = []
            elif cur is not None:
                m = re.match(r"^\*\*(\d+)\.\*\*", line)
                if m:
                    cur.append(int(m.group(1)))
    if cur:
        blocks.append(cur)
    return blocks


def detect_digits(y, model_name):
    from transformers import pipeline
    asr = pipeline("automatic-speech-recognition", model=model_name, device=-1)
    hits, texts = [], []
    step = WINDOW_S - OVERLAP_S
    n_win = int(np.ceil((len(y) / TARGET_SR - OVERLAP_S) / step))
    for k in range(n_win):
        t0 = k * step
        a, b = int(t0 * TARGET_SR), int((t0 + WINDOW_S) * TARGET_SR)
        chunk = y[a:b]
        if len(chunk) < TARGET_SR // 2:
            break
        out = asr(chunk.copy(), return_timestamps="word")
        texts.append((t0, out["text"].strip()))
        for ch in out.get("chunks", []):
            ts = ch.get("timestamp") or (None, None)
            if ts[0] is None:
                continue
            v = parse_number(ch["text"])
            if v is not None and 1 <= v <= 99:
                hits.append((t0 + float(ts[0]), v))
        print(f"  window {k+1}/{n_win}  t={t0:6.1f}s  digits so far: {len(hits)}",
              file=sys.stderr)
    hits.sort()
    # dedupe overlap-region duplicates
    ded = []
    for t, v in hits:
        if ded and v == ded[-1][1] and t - ded[-1][0] < DEDUPE_S:
            continue
        ded.append((t, v))
    return ded, texts


def align(detected, expected):
    """Monotonic LCS alignment of detected digit values onto the expected sequence."""
    m, n = len(detected), len(expected)
    dp = np.zeros((m + 1, n + 1), dtype=np.int32)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if detected[i][1] == expected[j]:
                dp[i, j] = dp[i + 1, j + 1] + 1
            else:
                dp[i, j] = max(dp[i + 1, j], dp[i, j + 1])
    pairs, i, j = [], 0, 0
    while i < m and j < n:
        if detected[i][1] == expected[j]:
            pairs.append((j, detected[i][0], expected[j]))
            i, j = i + 1, j + 1
        elif dp[i + 1, j] >= dp[i, j + 1]:
            i += 1
        else:
            j += 1
    return pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("wav")
    ap.add_argument("--order-file", default="planning/audio-pilot-01.md")
    ap.add_argument("--model", default="openai/whisper-base.en")
    ap.add_argument("--out", default=None,
                    help="write anchor table as CSV (input to stage 2)")
    ap.add_argument("--dump-text", action="store_true",
                    help="print raw per-window transcripts (debugging only)")
    args = ap.parse_args()

    y, orig_sr = load_16k(args.wav)
    print(f"# Slate alignment - {args.wav}")
    print(f"  source {orig_sr} Hz -> {TARGET_SR} Hz, {len(y)/TARGET_SR:.1f} s")

    blocks = parse_order_file(args.order_file)
    expected = [v for b in blocks for v in b]
    print(f"  expected: {len(blocks)} blocks x {len(blocks[0]) if blocks else 0} "
          f"= {len(expected)} slates\n")

    print("Detecting digits (Whisper as anchor finder; conlang output discarded)...")
    detected, texts = detect_digits(y, args.model)
    print(f"\n  raw digit detections: {len(detected)}")

    pairs = align(detected, expected)
    print(f"  aligned to expected sequence: {len(pairs)} / {len(expected)} "
          f"({100*len(pairs)/max(len(expected),1):.0f}% recall)\n")

    nb = len(blocks[0]) if blocks else 25
    print("## Anchors by block")
    for bi in range(len(blocks)):
        got = [p for p in pairs if bi * nb <= p[0] < (bi + 1) * nb]
        miss = sorted(set(range(bi * nb, (bi + 1) * nb)) - {p[0] for p in got})
        span = f"{got[0][1]:7.1f}-{got[-1][1]:7.1f}s" if got else "   --   "
        print(f"  block {bi+1}: {len(got):2d}/{nb} anchors  {span}"
              + (f"   missing items: {[expected[i] for i in miss]}" if miss else ""))

    print("\n## Interpolation check")
    print("  A missing slate between two correct anchors is still unambiguous:")
    print("  its position in the known order fixes its identity.")
    covered = 0
    idxs = sorted(p[0] for p in pairs)
    for i in range(len(expected)):
        if i in set(idxs):
            covered += 1
        else:
            lo = [j for j in idxs if j < i]
            hi = [j for j in idxs if j > i]
            if lo and hi:
                covered += 1
    print(f"  items recoverable (anchored or bracketed): {covered}/{len(expected)} "
          f"({100*covered/max(len(expected),1):.0f}%)")

    # Spacing anomalies: a gap far larger than the running median means extra
    # material sits between two anchors -- a retake, a break, or commentary.
    if len(pairs) > 4:
        dts = np.array([pairs[i + 1][1] - pairs[i][1] for i in range(len(pairs) - 1)])
        med = float(np.median(dts))
        print(f"\n## Spacing anomalies (median anchor spacing {med:.1f} s)")
        flagged = 0
        for i, dt in enumerate(dts):
            npos = pairs[i + 1][0] - pairs[i][0]      # expected items in between
            if dt > max(3.0 * med, med * npos + 2.5 * med):
                flagged += 1
                print(f"  {pairs[i][1]:7.1f}-{pairs[i+1][1]:7.1f}s  {dt:5.1f}s for "
                      f"{npos} item(s)  <- inspect: retake / break / commentary")
        if not flagged:
            print("  none")

    print("\n## Anchor table (item_id, time)")
    for j, t, v in pairs:
        print(f"  block {j//nb+1:>1} pos {j%nb+1:>2}  item {v:>2}  t={t:8.2f}s")

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write("block,position,item_id,anchor_t,anchored\n")
            got = {p[0]: p for p in pairs}
            for i, v in enumerate(expected):
                p = got.get(i)
                t = f"{p[1]:.3f}" if p else ""
                f.write(f"{i//nb+1},{i%nb+1},{v},{t},{1 if p else 0}\n")
        print(f"\nwrote anchors -> {args.out}")
        print("  Rows with anchored=0 are identity-known but time-unknown; stage 2")
        print("  resolves them by local search between the surrounding anchors.")

    if args.dump_text:
        print("\n## Raw window transcripts")
        for t0, txt in texts:
            print(f"  [{t0:6.1f}s] {txt}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
