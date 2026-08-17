#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
audiolib.py — shared primitives for the audio pipeline tools.

Not a CLI. `audio-split.py` and `audio-contour.py` both import from here so that
segmentation exists in exactly one place: the pilot showed that a segmentation bug
fixed in one tool and not the other produces two incompatible views of the same
recording, which is worse than one wrong view.

Loaded by hyphenated siblings via a sys.path insert of their own directory.

Requires: numpy, scipy.
"""
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfiltfilt, medfilt

HOP_S = 0.010            # energy-envelope hop; 10 ms is finer than any boundary we claim
# Speaker median is 84.5 Hz on pilot 01. The floor was 70 Hz until 2026-08-12, which is
# only ~4 semitones below that median -- creak at the end of an isolated citation word
# falls straight through it. 27 of 120 tokens had f0_min sitting exactly on the rail, and
# the tracker answered by reporting the octave above (noê block 2 read 103.7 Hz; at a
# 55 Hz floor the same token reads 82.0). Lowering the floor removes the railing without
# admitting noise -- median voiced_frac moves 0.40 -> 0.41.
F0_MIN, F0_MAX = 55.0, 200.0   # a wider ceiling invites doubling; the floor must clear creak
F0_FRAME_S = 0.005
F0_WIN_S = 0.040


def db(v):
    return 20.0 * np.log10(np.maximum(v, 1e-12))


def load(path):
    """Read a WAV as float64 mono in [-1, 1], plus its sample rate."""
    sr, x = wavfile.read(path)
    if x.ndim > 1:
        x = x.mean(axis=1)
    if x.dtype.kind in "iu":
        x = x.astype(np.float64) / float(2 ** (x.dtype.itemsize * 8 - 1))
    return x.astype(np.float64), sr


def envelope(x, sr, hop_s=HOP_S):
    """Frame-wise RMS in dB. Returns (levels, hop_samples)."""
    hop = int(hop_s * sr)
    nf = len(x) // hop
    if nf < 1:
        return np.zeros(0), hop
    fr = x[:nf * hop].reshape(nf, hop)
    return db(np.sqrt(np.mean(fr ** 2, axis=1))), hop


def detect_blobs(lv, on_db=12.0, peak_db=22.0, min_dur_s=0.04,
                 join_s=0.04, hop_s=HOP_S):
    """Contiguous above-floor runs of the energy envelope.

    Two thresholds, and the second one matters more than it looks. `on_db` decides
    where a blob starts and stops; `peak_db` decides whether it is speech at all.
    Real utterances in pilot 01 sit 28-47 dB above the local floor while breath, mouth
    noise and room ticks sit at 13-24 dB. Without the peak filter those get clustered
    as though they were the slate, which silently shifts every boundary after them.

    Returns (blobs, floor_db) where blobs is a list of (start_frame, end_frame).
    """
    if len(lv) < 3:
        return [], 0.0
    floor = float(np.percentile(lv, 15))
    idx = np.where(lv > floor + on_db)[0]
    if not len(idx):
        return [], floor
    join_f = max(1, int(round(join_s / hop_s)))
    brk = np.where(np.diff(idx) > join_f)[0]
    starts = np.concatenate(([idx[0]], idx[brk + 1]))
    ends = np.concatenate((idx[brk], [idx[-1]]))
    blobs = [(int(s), int(e)) for s, e in zip(starts, ends)
             if (e - s) * hop_s >= min_dur_s and lv[s:e + 1].max() >= floor + peak_db]
    return blobs, floor


def blob_gaps(blobs, hop_s=HOP_S):
    """Silent gap in seconds between each consecutive blob pair."""
    return [(blobs[i + 1][0] - blobs[i][1]) * hop_s for i in range(len(blobs) - 1)]


def cluster_blobs(blobs, sep_s, hop_s=HOP_S):
    """Group blobs into utterances: any gap >= sep_s starts a new group.

    A word fragments into several blobs whenever it contains voiceless internal
    material -- /h/, a geminate, /theta/, a glottal stop. Rickett Yack does this
    constantly, which is why global silence splitting failed. Locally it is tractable:
    internal closures run 50-150 ms while the slate-to-word pause runs ~0.9 s.
    """
    if not blobs:
        return []
    groups, cur = [], [blobs[0]]
    for i, g in enumerate(blob_gaps(blobs, hop_s)):
        if g >= sep_s:
            groups.append(cur)
            cur = [blobs[i + 1]]
        else:
            cur.append(blobs[i + 1])
    groups.append(cur)
    return groups


def cluster_to_count(blobs, m, hop_s=HOP_S):
    """Max-gap clustering: split at the (m-1) largest gaps, giving exactly m groups.

    The fallback when a fixed separator returns the wrong group count. Optimal for
    1-D single-linkage clustering, and it uses the interval's own gap distribution
    rather than a threshold that has to generalise -- but it will happily split a word
    at an internal closure if the interval genuinely holds fewer utterances than
    expected, so the caller must sanity-check the durations it gets back.
    """
    if not blobs or m < 1:
        return []
    if m == 1 or len(blobs) == 1:
        return [list(blobs)]
    gaps = np.array(blob_gaps(blobs, hop_s))
    cut = set(np.argsort(gaps)[-(m - 1):].tolist())
    groups, cur = [], [blobs[0]]
    for i in range(len(gaps)):
        if i in cut:
            groups.append(cur)
            cur = [blobs[i + 1]]
        else:
            cur.append(blobs[i + 1])
    groups.append(cur)
    return groups


def group_span(group, hop_s=HOP_S):
    """(start_s, end_s) of a blob group, relative to the envelope's own origin."""
    return group[0][0] * hop_s, (group[-1][1] + 1) * hop_s


def refine_bounds(x, sr, t0, t1, pad_s=0.12, rel_db=25.0, min_above_floor=8.0,
                  bridge_s=0.15, hop_s=HOP_S):
    """Re-cut a token's endpoints at a threshold relative to its OWN peak.

    Utterance clustering finds boundaries at a fixed level above the session noise
    floor. That is fine for grouping but wrong for measurement: pilot 01 has a 25 dB
    spread across items, so a loud token clears a session-relative threshold earlier
    and drops below it later than a quiet one, and its duration comes out longer for
    reasons that have nothing to do with phonology. Since duration is one of the two
    measures under test, that bias has to go.

    Peak-relative endpointing removes it -- every token is cut at the same point on
    its own decay curve. The floor guard keeps a very quiet token from chasing its
    threshold down into room noise.

    The defaults are calibrated, not chosen: across a pad/rel_db/bridge grid, the
    within-item correlation between a token's peak level and its measured duration runs
    -0.31 at rel_db=20 and falls to -0.05 here. That correlation is the bias itself, so
    minimising it is the criterion. See planning/audio-pipeline-plan.md section 6.

    Returns (t0, t1) refined, or the input unchanged if the window is unusable.
    """
    a = max(0, int((t0 - pad_s) * sr))
    b = min(len(x), int((t1 + pad_s) * sr))
    if b - a < int(0.05 * sr):
        return t0, t1
    lv, _ = envelope(x[a:b], sr)
    if len(lv) < 3:
        return t0, t1
    floor = float(np.percentile(lv, 10))
    i0 = int(round((t0 - (a / sr)) / hop_s))
    i1 = int(round((t1 - (a / sr)) / hop_s))
    i0, i1 = max(0, i0), min(len(lv) - 1, i1)
    if i1 <= i0:
        return t0, t1
    pk_i = i0 + int(np.argmax(lv[i0:i1 + 1]))
    thr = max(lv[pk_i] - rel_db, floor + min_above_floor)
    # Walk out from the peak, bridging dips shorter than bridge_s. Without the bridge
    # the walk halts at the first internal closure -- and this language puts /h/, /ʔ/,
    # geminates and /sː/ inside words constantly, so a naive walk returns one syllable
    # of a disyllable and calls it the token.
    br = max(1, int(round(bridge_s / hop_s)))
    s = pk_i
    while s > 0:
        prev = np.where(lv[max(0, s - br - 1):s] > thr)[0]
        if not len(prev):
            break
        s = max(0, s - br - 1) + int(prev[0])
    e = pk_i
    while e < len(lv) - 1:
        nxt = np.where(lv[e + 1:min(len(lv), e + br + 2)] > thr)[0]
        if not len(nxt):
            break
        e = e + 1 + int(nxt[-1])
    return a / sr + s * hop_s, a / sr + (e + 1) * hop_s


def f0_track(x, sr, f0_min=None, f0_max=None):
    """Normalised-autocorrelation F0 tracker (YIN-flavoured, numpy only).

    Returns (f0, voiced, confidence, rms) per 5 ms frame. parselmouth would be the
    obvious tool here but is not installed; this is adequate for whole-word contour
    comparison, which is all the pilot design asks of it.

    Check `voiced.mean()` before trusting any per-token summary: a floor set too close
    to the speaker's median does not fail loudly, it reports the octave above.
    """
    f0_min = F0_MIN if f0_min is None else f0_min
    f0_max = F0_MAX if f0_max is None else f0_max
    sos = butter(4, [f0_min * 0.7, min(1200.0, sr / 2 - 100)], btype="band",
                 fs=sr, output="sos")
    xb = sosfiltfilt(sos, x)
    win, hop = int(F0_WIN_S * sr), int(F0_FRAME_S * sr)
    lo_lag, hi_lag = int(sr / f0_max), int(sr / f0_min)
    n = max(0, (len(xb) - win) // hop + 1)
    f0 = np.zeros(n)
    conf = np.zeros(n)
    rms = np.zeros(n)
    for i in range(n):
        w = xb[i * hop: i * hop + win]
        rms[i] = np.sqrt(np.mean(w ** 2))
        w = w - w.mean()
        e0 = np.dot(w, w)
        if e0 <= 1e-12:
            continue
        ac = np.correlate(w, w, "full")[win - 1:] / e0
        seg = ac[lo_lag:hi_lag]
        if len(seg) < 3:
            continue
        k = int(np.argmax(seg))
        if 0 < k < len(seg) - 1:                       # parabolic peak refinement
            y0, y1, y2 = seg[k - 1], seg[k], seg[k + 1]
            d = y0 - 2 * y1 + y2
            shift = 0.5 * (y0 - y2) / d if abs(d) > 1e-12 else 0.0
        else:
            shift = 0.0
        lag = lo_lag + k + shift
        conf[i] = seg[k]
        if lag > 0:
            f0[i] = sr / lag
    thr = max(0.40, float(np.percentile(conf, 40)))
    voiced = (conf > thr) & (rms > 0.02 * rms.max()) & (f0 > f0_min) & (f0 < f0_max)
    sm = f0.copy()
    if voiced.sum() > 5:
        sm[voiced] = medfilt(f0[voiced], 5)
        # Octave repair: at this speaker's range a frame far off the token's own median
        # is a doubling/halving error, not a real excursion.
        med = np.median(sm[voiced])
        hi = voiced & (sm > 1.6 * med)
        sm[hi] = sm[hi] / 2.0
        lo = voiced & (sm < 0.6 * med)
        sm[lo] = sm[lo] * 2.0
    return sm, voiced, conf, rms


def resample_contour(t, v, npts=60):
    """Time-normalise a track to npts points over 0-100% of its own extent."""
    if len(t) < 3:
        return None
    tn = (t - t[0]) / (t[-1] - t[0] + 1e-12)
    return np.interp(np.linspace(0, 1, npts), tn, v)
