#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
audio-polish.py — stage 5: deterministic conditioning of the selected takes.

Implements the processing chain in planning/audio-pipeline-plan.md section 6:
high-pass -> (optional) noise reduction -> trim with padding -> loudness normalisation.

  ***  PUBLICATION BRANCH ONLY. NEVER MEASURE THE OUTPUT OF THIS TOOL.  ***

That warning is the load-bearing comment in this file. Loudness normalisation
deliberately destroys cross-item amplitude relationships -- it exists precisely to make
every published word land at the same perceived level. The V1 length-and-amplitude
prediction (phonology.md section 3.4) is tested on amplitude, so measuring polished
audio would answer that question with an artefact of this script. The corpus forks
here: analysis reads the stage-2 per-item WAVs, publication reads these.

Design notes
------------
*Zero-phase filtering throughout.* Every filter runs through `filtfilt`, not `lfilter`.
A causal filter imposes frequency-dependent group delay, which smears exactly the
transients that carry this language's contrasts -- glottal stops, geminate releases.
Zero-phase costs nothing offline and leaves timing untouched, which matters because
duration is a measure under test and the polished files should not disagree with the
measured ones about where a word starts.

*The high-pass stays at 60 Hz.* No higher. The speaker median is 84.5 Hz and the F0
floor was lowered to 55 Hz after the tracker was caught railing (audiolib.py); a 100 Hz
"cleanup" high-pass of the sort usually recommended for speech would cut into the bottom
of this speaker's range.

*Noise reduction is OFF by default.* Plan section 9 lists its aggressiveness as an open
question and notes the SNR may make it skippable -- measured median SNR is 45 dB. Spectral
gating eats fricative energy and adds musical noise, and this language's inventory leans
on /h/, /theta/, /s:/. Enable with --denoise only after listening to the result.

*Loudness: R128 where it is meaningful, K-weighted RMS where it is not.* ITU-R BS.1770
integrated loudness gates the signal in 400 ms blocks. A 0.5 s citation word yields two
blocks, so the gating that makes the measure robust on program material is meaningless
here. Above --gate-min-blocks the full gated measurement runs; below it the tool falls
back to ungated K-weighted RMS over the (already trimmed) token, which is what the gate
would have converged to anyway once the silence was gone. The fallback is reported per
file rather than applied silently.

Usage:
    python tools/audio-polish.py \
        --picks audio/work/session-01-picks.csv \
        --out audio/work/polished

    python tools/audio-polish.py --in-dir audio/work/items --out audio/work/polished

Requires: numpy, scipy.
"""
import argparse
import csv
import os
import sys

import numpy as np
from scipy import signal
from scipy.io import wavfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audiolib import load, refine_bounds, db  # noqa: E402

HPF_HZ = 60.0
HPF_ORDER = 4
# Calibrated, not chosen. Isolated citation words have a high crest factor -- measured
# over pilot 01 the peak-to-loudness ratio runs 17.1 to 22.6 dB (median 18.9). Any
# target closer to the ceiling than the WORST crest factor leaves the loudest-peaking
# files ceiling-limited, landing short of target: at -20 LUFS, 12 of 25 files missed.
# -24 is the first whole dB at which all 25 reach target, which is the only condition
# under which this stage delivers the uniformity it exists for. It also sits beside the
# EBU R128 broadcast target of -23. Re-derive if a future session changes gain staging.
TARGET_LUFS = -24.0
PEAK_CEILING_DBFS = -1.0
PAD_S = 0.150
GATE_MIN_BLOCKS = 10


def k_weight(x, sr):
    """ITU-R BS.1770 K-weighting: a high-shelf then an RLB high-pass.

    The standard tabulates coefficients at 48 kHz. Rather than resample, the two
    biquads are re-derived at the actual rate from the prototype parameters via the
    usual bilinear-transform formulas, which is rate-independent and exact at 48 k.
    """
    # Stage 1: high shelf, +4 dB.
    f0, G, Q = 1681.974450955533, 3.999843853973347, 0.7071752369554196
    K = np.tan(np.pi * f0 / sr)
    Vh = 10.0 ** (G / 20.0)
    Vb = Vh ** 0.4996667741545416
    den = 1.0 + K / Q + K * K
    b_shelf = np.array([(Vh + Vb * K / Q + K * K) / den,
                        2.0 * (K * K - Vh) / den,
                        (Vh - Vb * K / Q + K * K) / den])
    a_shelf = np.array([1.0, 2.0 * (K * K - 1.0) / den, (1.0 - K / Q + K * K) / den])

    # Stage 2: RLB high-pass at ~38 Hz.
    f0, Q = 38.13547087602444, 0.5003270373238773
    K = np.tan(np.pi * f0 / sr)
    den = 1.0 + K / Q + K * K
    b_hp = np.array([1.0, -2.0, 1.0])
    a_hp = np.array([1.0, 2.0 * (K * K - 1.0) / den, (1.0 - K / Q + K * K) / den])

    y = signal.lfilter(b_shelf, a_shelf, x)
    return signal.lfilter(b_hp, a_hp, y)


def loudness_lufs(x, sr, gate_min_blocks=GATE_MIN_BLOCKS):
    """Loudness in LUFS. Returns (value, method) where method is 'gated' or 'rms'."""
    y = k_weight(x, sr)
    block, step = int(0.400 * sr), int(0.100 * sr)
    if len(y) < block or (len(y) - block) // step + 1 < gate_min_blocks:
        ms = float(np.mean(y ** 2))
        if ms <= 0:
            return -np.inf, "rms"
        return -0.691 + 10.0 * np.log10(ms), "rms"

    z = np.array([np.mean(y[i:i + block] ** 2)
                  for i in range(0, len(y) - block + 1, step)])
    z = np.maximum(z, 1e-20)
    l = -0.691 + 10.0 * np.log10(z)
    keep = l >= -70.0                       # absolute gate
    if not keep.any():
        return -np.inf, "gated"
    gamma = -0.691 + 10.0 * np.log10(np.mean(z[keep])) - 10.0   # relative gate
    keep &= l >= gamma
    if not keep.any():
        return -np.inf, "gated"
    return -0.691 + 10.0 * np.log10(np.mean(z[keep])), "gated"


def polish(path, args, room=None):
    """Run the chain on one file. Returns (samples, sr, report-dict)."""
    x, sr = load(path)
    rep = {"file": os.path.basename(path), "in_dur": len(x) / sr,
           "in_peak": float(db(np.max(np.abs(x)))) if len(x) else -np.inf}

    sos = signal.butter(HPF_ORDER, HPF_HZ, btype="highpass", fs=sr, output="sos")
    x = signal.sosfiltfilt(sos, x)

    if args.denoise and room is not None:
        x = spectral_gate(x, sr, room, args.denoise_db)
        rep["denoised"] = True

    # Trim to the token's own endpoints, then restore a fixed pad. refine_bounds
    # bridges internal dips up to 150 ms so it does not stop at a word-internal
    # /h/, /?/ or geminate closure and hand back one syllable of a disyllable.
    t0, t1 = refine_bounds(x, sr, 0.0, len(x) / sr)
    a = max(0, int((t0 - args.pad) * sr))
    b = min(len(x), int((t1 + args.pad) * sr))
    if b - a > int(0.05 * sr):
        x = x[a:b]
    rep["out_dur"] = len(x) / sr

    lufs, method = loudness_lufs(x, sr, args.gate_min_blocks)
    rep["lufs_in"], rep["loud_method"] = lufs, method
    if np.isfinite(lufs):
        gain = 10.0 ** ((args.target_lufs - lufs) / 20.0)
        peak = float(np.max(np.abs(x))) if len(x) else 0.0
        ceiling = 10.0 ** (args.peak_ceiling / 20.0)
        # Normalise to target, but never past the peak ceiling. When the ceiling
        # binds, the file lands quiet rather than clipped and the shortfall is
        # reported -- a limiter would change the amplitude envelope, which is the
        # one thing this chain must not do casually.
        if peak * gain > ceiling:
            gain = ceiling / max(peak, 1e-12)
            rep["ceiling_limited"] = True
        x = x * gain
        rep["gain_db"] = 20.0 * np.log10(max(gain, 1e-12))
        rep["lufs_out"] = lufs + rep["gain_db"]
    rep["out_peak"] = float(db(np.max(np.abs(x)))) if len(x) else -np.inf
    return x, sr, rep


def spectral_gate(x, sr, room, reduce_db):
    """Conservative spectral subtraction against a room-tone noise profile."""
    n = 1024
    f, t, Z = signal.stft(x, sr, nperseg=n)
    _, _, R = signal.stft(room, sr, nperseg=n)
    prof = np.median(np.abs(R), axis=1, keepdims=True)
    mag, phase = np.abs(Z), np.angle(Z)
    floor = 10.0 ** (-abs(reduce_db) / 20.0)
    mask = np.maximum((mag - prof) / np.maximum(mag, 1e-12), floor)
    _, y = signal.istft(mag * mask * np.exp(1j * phase), sr, nperseg=n)
    return y[:len(x)]


def main():
    ap = argparse.ArgumentParser(description="Polish selected takes for publication.")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--picks", help="picks CSV from audio-select.py")
    src.add_argument("--in-dir", help="polish every WAV in this directory")
    ap.add_argument("--out", required=True, help="output directory")
    ap.add_argument("--target-lufs", type=float, default=TARGET_LUFS)
    ap.add_argument("--peak-ceiling", type=float, default=PEAK_CEILING_DBFS)
    ap.add_argument("--pad", type=float, default=PAD_S)
    ap.add_argument("--gate-min-blocks", type=int, default=GATE_MIN_BLOCKS)
    ap.add_argument("--denoise", action="store_true",
                    help="enable spectral subtraction (off by default; see docstring)")
    ap.add_argument("--denoise-db", type=float, default=6.0)
    ap.add_argument("--room", default="", help="room-tone WAV for the noise profile")
    ap.add_argument("--report", default="", help="write a per-file CSV report here")
    args = ap.parse_args()

    if args.picks:
        with open(args.picks, encoding="utf-8") as fh:
            files = [(r["wav"], r["headword"], r["item_id"])
                     for r in csv.DictReader(fh) if r.get("wav")]
    else:
        files = [(os.path.join(args.in_dir, n), "", "")
                 for n in sorted(os.listdir(args.in_dir)) if n.lower().endswith(".wav")]
    if not files:
        sys.exit("no input files")

    room = None
    if args.denoise:
        if not args.room:
            sys.exit("--denoise requires --room (a room-tone WAV)")
        room, _ = load(args.room)

    os.makedirs(args.out, exist_ok=True)
    reports = []
    for path, headword, item_id in files:
        if not os.path.exists(path):
            print("MISSING %s" % path)
            continue
        x, sr, rep = polish(path, args, room)
        dest = os.path.join(args.out, os.path.basename(path))
        wavfile.write(dest, sr, x.astype(np.float32))
        rep["headword"], rep["item_id"] = headword, item_id
        reports.append(rep)
        print("%-28s %5.2fs -> %5.2fs  %6.1f LUFS %-5s gain %+5.1f dB  peak %5.1f%s"
              % (rep["file"], rep["in_dur"], rep["out_dur"], rep.get("lufs_in", 0),
                 rep.get("loud_method", ""), rep.get("gain_db", 0), rep["out_peak"],
                 "  CEILING" if rep.get("ceiling_limited") else ""))

    n_rms = sum(1 for r in reports if r.get("loud_method") == "rms")
    n_ceil = sum(1 for r in reports if r.get("ceiling_limited"))
    print("\n%d polished -> %s" % (len(reports), args.out))
    print("%d used the RMS fallback (too short to gate); %d hit the peak ceiling"
          % (n_rms, n_ceil))

    if args.report and reports:
        keys = sorted({k for r in reports for k in r})
        with open(args.report, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=keys)
            w.writeheader()
            w.writerows(reports)
        print("wrote %s" % args.report)


if __name__ == "__main__":
    main()
