#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
audio-select.py — stage 4: choose one publishable take per item.

Reads the per-token table produced by `audio-contour.py --tokens`. It measures nothing
of its own: every number it decides on was already computed in stage 3, against
boundaries decided once in stage 2. This tool is pure policy.

Why the medoid, and not the best-sounding take
----------------------------------------------
The obvious rule -- "publish the take with the highest SNR" -- is wrong here, and
wrong in a direction this corpus is already sensitive to. Peak level and SNR track how
hard the item was produced, so ranking by them systematically selects the loudest, most
emphatic reading of each word. That is the same citation-form emphasis that confounds
the noê duration result (planning/audio-pipeline-plan.md section 7): it would publish
the least typical token of every headword and call it the reference pronunciation.

So selection runs in two stages, and only the first one is about quality:

  1. A hard gate on technical defects. Clipping destroys amplitude data outright; low
     SNR and out-of-range peaks make a file unpleasant to listen to. These are
     disqualifying, not scoreable -- a badly clipped take is not "worse", it is unusable.

  2. Among survivors, the medoid: the take closest to that item's OWN median on
     duration and F0. Deviations are z-scored within the item, so an item whose five
     reps vary a lot is not penalised against one that does not; the question is only
     which rep is most representative of its own set.

The gate never empties an item. If no take passes, the tool falls back to the full set,
picks the medoid of that, and flags the row -- demote, don't drop (learnings section 3.9).
A flagged row means "this headword's audio is publishable only under protest", which is
a decision for the author, not for this script.

Note this tool selects; it does not process. The chosen takes are raw per-item WAVs and
still need `audio-polish.py` before they are fit to publish.

Usage:
    python tools/audio-select.py \
        --tokens audio/work/session-01-tokens-all.csv \
        --items audio/work/items \
        --out audio/work/session-01-picks.csv

Requires: nothing beyond the standard library.
"""
import argparse
import csv
import os
import statistics as st
import sys

# Technical gate. Peak is bounded on BOTH sides: too quiet is noisy after
# normalisation, too hot is either clipped already or has no headroom for the
# polish stage's filtering to work in without wrapping.
SNR_MIN_DB = 35.0
PEAK_MIN_DBFS = -26.0
PEAK_MAX_DBFS = -1.0

# Fields the medoid is computed over. Duration and F0 are the two dimensions the
# analysis actually cares about, so "typical" is defined in exactly those terms.
MEDOID_FIELDS = ("dur", "f0_med")


def fnum(row, key):
    """Float from a CSV cell, or None for blank/nan."""
    v = (row.get(key) or "").strip()
    if v == "" or v.lower() == "nan":
        return None
    try:
        return float(v)
    except ValueError:
        return None


def gate_failures(row, snr_min, peak_min, peak_max):
    """Disqualifying technical defects for one take, as a list of short reasons."""
    why = []
    clipped = fnum(row, "clipped")
    snr = fnum(row, "snr_db")
    peak = fnum(row, "peak_dbfs")
    if clipped is not None and clipped > 0:
        why.append("clipped")
    if snr is not None and snr < snr_min:
        why.append("lowSNR")
    if peak is not None and peak < peak_min:
        why.append("quiet")
    if peak is not None and peak > peak_max:
        why.append("hot")
    return why


def abs_z(pool, key):
    """|z-score| of each take against its own item's mean, keyed by row identity.

    Absolute value because we want the CENTRE, not an extreme -- the medoid is the
    row minimising total deviation. A take missing the measurement is parked at 2.0
    (two sigma) so it loses to any take that has it without being excluded outright.
    """
    vals = [fnum(r, key) for r in pool]
    have = [v for v in vals if v is not None]
    if len(have) < 2:
        return {id(r): 0.0 for r in pool}
    mean = st.mean(have)
    sd = st.stdev(have) or 1.0
    out = {}
    for r, v in zip(pool, vals):
        out[id(r)] = 2.0 if v is None else abs((v - mean) / sd)
    return out


def pick_medoid(pool):
    """The take closest to its item's centre across MEDOID_FIELDS."""
    z = [abs_z(pool, k) for k in MEDOID_FIELDS]
    return min(pool, key=lambda r: sum(zi[id(r)] for zi in z))


def find_wav(items_dir, item_id, headword, block):
    """Locate the stage-2 per-item WAV for one take.

    Filenames are `item-<NN>_<headword>_b<N>.wav` and carry the headword with its
    diacritics intact. Match on the item/block frame rather than on the headword, so
    that any Unicode normalisation difference between the CSV and the filesystem
    cannot cause a miss.
    """
    if not items_dir or not os.path.isdir(items_dir):
        return ""
    prefix = "item-%02d_" % int(item_id)
    suffix = "_b%s.wav" % block
    for name in os.listdir(items_dir):
        if name.startswith(prefix) and name.endswith(suffix):
            return os.path.join(items_dir, name)
    return ""


def main():
    ap = argparse.ArgumentParser(description="Choose one publishable take per item.")
    ap.add_argument("--tokens", required=True,
                    help="per-token CSV from audio-contour.py --tokens")
    ap.add_argument("--items", default="",
                    help="directory of stage-2 per-item WAVs (optional; resolves paths)")
    ap.add_argument("--out", default="", help="write picks CSV here")
    ap.add_argument("--snr-min", type=float, default=SNR_MIN_DB)
    ap.add_argument("--peak-min", type=float, default=PEAK_MIN_DBFS)
    ap.add_argument("--peak-max", type=float, default=PEAK_MAX_DBFS)
    args = ap.parse_args()

    with open(args.tokens, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        sys.exit("no rows in %s" % args.tokens)

    items = {}
    for r in rows:
        items.setdefault((int(r["item_id"]), r["headword"]), []).append(r)

    picks = []
    for (item_id, headword) in sorted(items):
        takes = items[(item_id, headword)]
        passed = [r for r in takes
                  if not gate_failures(r, args.snr_min, args.peak_min, args.peak_max)]
        forced = not passed
        pool = takes if forced else passed
        best = pick_medoid(pool)
        picks.append({
            "item_id": item_id,
            "headword": headword,
            "frame": best.get("frame", ""),
            "block": best["block"],
            "takes": len(takes),
            "passed": len(passed),
            "dur": best.get("dur", ""),
            "peak_dbfs": best.get("peak_dbfs", ""),
            "snr_db": best.get("snr_db", ""),
            "f0_med": best.get("f0_med", ""),
            "wav": find_wav(args.items, item_id, headword, best["block"]),
            # Empty when the pick is clean. Populated rows want an author's eye:
            # either no take passed the gate, or the item has too few takes left
            # for "most typical" to mean much.
            "flag": ("no-take-passed-gate" if forced
                     else ("thin:%d-usable" % len(passed) if len(passed) < 3 else "")),
        })

    hdr = ("headword", "takes", "pass", "pick", "dur", "snr", "peak", "flag")
    print("%-14s%6s%6s%6s%7s%7s%7s  %s" % hdr)
    for p in picks:
        print("%-14s%6d%6d%6s%7.2f%7.1f%7.1f  %s" % (
            p["headword"], p["takes"], p["passed"], "b" + str(p["block"]),
            float(p["dur"] or 0), float(p["snr_db"] or 0), float(p["peak_dbfs"] or 0),
            p["flag"]))

    forced_n = sum(1 for p in picks if p["flag"] == "no-take-passed-gate")
    thin_n = sum(1 for p in picks if p["flag"].startswith("thin"))
    missing = sum(1 for p in picks if args.items and not p["wav"])
    print("\n%d items; %d forced past the gate; %d thin; %d without a located WAV"
          % (len(picks), forced_n, thin_n, missing))

    if args.out:
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        with open(args.out, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(picks[0].keys()))
            w.writeheader()
            w.writerows(picks)
        print("wrote %s" % args.out)


if __name__ == "__main__":
    main()
