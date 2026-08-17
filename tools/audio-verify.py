#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
audio-verify.py — content gate: is the extracted token actually the word?

Every check in this pipeline before 2026-08-17 was structural — utterance counts, anchor
spacing, parameter-grid stability, coverage against the manifest. A one-position shift in
the slate/word assignment preserves all of them, so all of them passed while stage 2 was
exporting the English digit slates and calling them words. 120 tokens were measured on
spoken numerals, three canon documents were updated from the results, and the error
surfaced only when a human played the audio and heard "one, two, three".

Neither the author (across 122 files) nor an LLM (which cannot hear at all) will catch
that by listening. So it has to be machine-checkable, and the check has to be about
CONTENT, not structure.

The test is deliberately negative, and that is the whole design
---------------------------------------------------------------
This does NOT ask "does this token sound like `hóhonìt`". Whisper has no acoustic model
for Rickett Yack and its transcription of a conlang word is noise — that is exactly why
stage 1 trusts it for digits and discards everything else it emits.

It asks the one question Whisper is reliable on, which is the same question stage 1
already bets the pipeline on: **is this an English digit?** A token that transcribes as
its own item's number is a slate that leaked into the word slot. A token that transcribes
as any digit at all is suspect. Anything else passes, including confident nonsense —
"Bonilla" for *benıîä* and "Eat so" for *rhiitsô* are exactly what a correct extraction
looks like.

The asymmetry is what makes this cheap and trustworthy: a positive result is decisive
(digits are the one thing the recogniser knows), and a negative result costs nothing
because it is not being read as evidence about the conlang.

Usage:
    python tools/audio-verify.py --segments audio/work/session-01-segments.csv \
        --master audio/masters/session-01.wav --out audio/work/session-01-verify.csv

    python tools/audio-verify.py --items audio/work/items --out ...

Requires: numpy, scipy, torch, transformers. Slow on CPU (~1 s per token); run in the
background for a full session.
"""
import argparse
import csv
import math
import os
import re
import sys

import numpy as np
from scipy.signal import resample_poly

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audiolib import load  # noqa: E402

ASR_SR = 16000
MODEL = "openai/whisper-base.en"

# Spelled and numeric forms both appear in Whisper output ("Five." and "5.").
DIGIT_WORDS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20,
}
# Homophone traps: these are plausible transcriptions of a real conlang word, so they
# must not be read as digit evidence on their own.
AMBIGUOUS = {"one": "won/wan", "two": "to/too", "four": "for/fore", "eight": "ate"}


def numbers_in(text):
    """Every integer the transcript asserts, from numerals and spelled forms alike."""
    t = text.lower()
    found = set(int(m) for m in re.findall(r"\b(\d{1,2})\b", t))
    for w, v in DIGIT_WORDS.items():
        if re.search(r"\b%s\b" % w, t):
            found.add(v)
    return found


def classify(text, item_id):
    """(verdict, note). Verdict is one of ok / SLATE-LEAK / digit-present / empty."""
    if not text.strip():
        return "empty", "no transcript"
    nums = numbers_in(text)
    if item_id in nums:
        amb = [w for w, v in DIGIT_WORDS.items()
               if v == item_id and w in AMBIGUOUS and re.search(r"\b%s\b" % w, text.lower())]
        if amb and len(nums) == 1:
            # "one" could be the conlang word or the slate. Flag, do not condemn.
            return "digit-present", "own number, but homophone-ambiguous (%s)" % AMBIGUOUS[amb[0]]
        return "SLATE-LEAK", "transcribes as its own item number (%d)" % item_id
    if nums:
        return "digit-present", "digit(s) %s present, not this item's" % sorted(nums)
    return "ok", ""


def main():
    ap = argparse.ArgumentParser(description="Verify extracted tokens are not slates.")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--segments", help="segments CSV; reads word_t0/word_t1 from master")
    src.add_argument("--items", help="directory of per-item WAVs")
    ap.add_argument("--master", default="", help="master WAV (required with --segments)")
    ap.add_argument("--out", default="")
    ap.add_argument("--pad", type=float, default=0.10)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    from transformers import pipeline
    asr = pipeline("automatic-speech-recognition", model=MODEL, device=-1)

    jobs = []   # (item_id, headword, block, samples, sr)
    if args.segments:
        if not args.master:
            sys.exit("--segments requires --master")
        x, sr = load(args.master)
        g = math.gcd(ASR_SR, sr)
        X = resample_poly(x, ASR_SR // g, sr // g)
        with open(args.segments, encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if not (r.get("word_t0") or "").strip():
                    continue
                t0 = float(r["word_t0"]) - args.pad
                t1 = float(r["word_t1"]) + args.pad
                seg = X[max(0, int(t0 * ASR_SR)):int(t1 * ASR_SR)]
                jobs.append((int(r["item_id"]), r["headword"], r["block"], seg, ASR_SR))
    else:
        for name in sorted(os.listdir(args.items)):
            if not name.lower().endswith(".wav"):
                continue
            m = re.match(r"item-(\d+)_(.+)_b(\d+)\.wav$", name)
            if not m:
                continue
            xx, ss = load(os.path.join(args.items, name))
            g = math.gcd(ASR_SR, ss)
            jobs.append((int(m.group(1)), m.group(2), m.group(3),
                         resample_poly(xx, ASR_SR // g, ss // g), ASR_SR))

    if args.limit:
        jobs = jobs[:args.limit]

    rows, counts = [], {}
    for item_id, headword, block, seg, sr in jobs:
        if len(seg) < sr // 20:
            text = ""
        else:
            text = asr({"raw": seg.astype(np.float32),
                        "sampling_rate": sr})["text"].strip()
        verdict, note = classify(text, item_id)
        counts[verdict] = counts.get(verdict, 0) + 1
        rows.append({"item_id": item_id, "headword": headword, "block": block,
                     "transcript": text, "verdict": verdict, "note": note})
        if verdict != "ok":
            print("%-9s item %2d b%s %-12s %r  %s"
                  % (verdict, item_id, block, headword, text, note))

    total = len(rows)
    leak = counts.get("SLATE-LEAK", 0)
    print("\n%d tokens checked" % total)
    for k in ("ok", "digit-present", "SLATE-LEAK", "empty"):
        if k in counts:
            print("  %-14s %4d  (%.1f%%)" % (k, counts[k], 100.0 * counts[k] / total))

    if args.out:
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        with open(args.out, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print("wrote %s" % args.out)

    # A handful of leaks is a bad row; a systematic rate is a bad RULE. The 2026-08-17
    # shift would have tripped this at ~100%.
    if total and leak / total > 0.10:
        print("\nFAIL: %.0f%% of tokens are their own slate. This is a systematic "
              "assignment error, not bad rows." % (100.0 * leak / total))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
