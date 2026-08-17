#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
audio-compare.py — build a self-contained A/B listening page.

Pairs each item's raw stage-2 WAV against its processed counterpart, encodes both to
MP3, and embeds them as data URIs in a single HTML file that needs no server and no
network. Written for auditioning `audio-polish.py`, but the same page is what the
voice-conversion QC stage will want (plan M9d) -- the only thing that changes is which
directory the "after" column points at.

Why there are THREE players per row, not two
--------------------------------------------
Loudness dominates A/B judgement. The louder of two clips is reliably preferred
regardless of its actual quality, and the polish stage applies +8 to +16 dB of gain, so
a naive raw-vs-polished comparison mostly measures the gain and tells you nothing about
the filtering. That is the same class of confound as ranking takes by SNR
(audio-select.py) or measuring duration against a session-relative threshold
(audiolib.refine_bounds) -- a processing artefact masquerading as the thing under test.

So each row offers:

  raw            the stage-2 file as it is, quieter. Shows the whole difference.
  raw (matched)  the same file with gain ONLY -- no high-pass, no trim -- brought to
                 the same loudness as the polished version. Compare against this one
                 to hear what the filtering and trimming actually did.
  polished       the stage-5 output.

If polished and raw-matched are indistinguishable, that is a good result: it means the
chain cleaned up level and endpoints without colouring the recording.

Usage:
    python tools/audio-compare.py \
        --picks audio/work/session-01-picks.csv \
        --after audio/work/polished \
        --out audio/work/compare.html

Requires: numpy, scipy, and ffmpeg on PATH (or --ffmpeg).
"""
import argparse
import base64
import csv
import html
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from scipy.io import wavfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util  # noqa: E402

from audiolib import load  # noqa: E402

# The hyphen in audio-polish.py makes it un-importable by name. Load it by path rather
# than renaming the tool, so loudness is measured by the same code that applied it.
_spec = importlib.util.spec_from_file_location(
    "audio_polish", os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio-polish.py"))
_ap = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ap)
loudness_lufs = _ap.loudness_lufs

WINGET_FFMPEG = os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\WinGet\Packages"
    r"\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\ffmpeg-9.0-full_build\bin\ffmpeg.exe")


def find_ffmpeg(explicit=""):
    """Resolve ffmpeg. winget appends to PATH, which existing shells do not see."""
    for cand in (explicit, shutil.which("ffmpeg"), WINGET_FFMPEG):
        if cand and os.path.exists(cand):
            return cand
    sys.exit("ffmpeg not found; pass --ffmpeg")


def to_mp3_datauri(ff, x, sr, kbps):
    """Encode float samples to MP3 and return a base64 data URI."""
    td = tempfile.mkdtemp()
    try:
        w = os.path.join(td, "a.wav")
        m = os.path.join(td, "a.mp3")
        peak = float(np.max(np.abs(x))) if len(x) else 0.0
        if peak > 1.0:                       # never let the encoder wrap
            x = x / peak * 0.999
        wavfile.write(w, sr, x.astype(np.float32))
        subprocess.run([ff, "-hide_banner", "-loglevel", "error", "-y", "-i", w,
                        "-codec:a", "libmp3lame", "-b:a", "%dk" % kbps, "-ac", "1", m],
                       check=True)
        with open(m, "rb") as fh:
            return "data:audio/mpeg;base64," + base64.b64encode(fh.read()).decode()
    finally:
        shutil.rmtree(td, ignore_errors=True)


ROW = """<tr>
<td class="hw">{hw}<span class="meta">item {iid} &middot; block {blk}{flag}</span></td>
<td><audio controls preload="none" src="{raw}"></audio><span class="lbl">{rawl}</span></td>
<td><audio controls preload="none" src="{mat}"></audio><span class="lbl">matched</span></td>
<td><audio controls preload="none" src="{pol}"></audio><span class="lbl">{poll}</span></td>
</tr>"""

PAGE = """<title>Polish A/B — session 01</title>
<style>
:root{{--bg:#fbfaf8;--fg:#1c1a17;--mut:#6b645c;--line:#e2ddd6;--acc:#7a5c3e}}
:root:not([data-theme="light"]){{}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{
--bg:#171614;--fg:#eceae6;--mut:#a49c92;--line:#332f2a;--acc:#c9a87c}}}}
:root[data-theme="dark"]{{--bg:#171614;--fg:#eceae6;--mut:#a49c92;--line:#332f2a;--acc:#c9a87c}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--fg);margin:0;padding:2rem 1.25rem 4rem;
font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
.wrap{{max-width:1040px;margin:0 auto}}
h1{{font-size:1.5rem;margin:0 0 .35rem}}
p.sub{{color:var(--mut);margin:0 0 1.5rem;max-width:64ch}}
.note{{border-left:3px solid var(--acc);padding:.7rem 1rem;background:rgba(122,92,62,.07);
margin:0 0 1.75rem;max-width:72ch;font-size:.93rem}}
.scroll{{overflow-x:auto}}
table{{border-collapse:collapse;width:100%;min-width:760px}}
th{{text-align:left;font-size:.75rem;letter-spacing:.06em;text-transform:uppercase;
color:var(--mut);font-weight:600;padding:0 .5rem .5rem;border-bottom:1px solid var(--line)}}
td{{padding:.6rem .5rem;border-bottom:1px solid var(--line);vertical-align:middle}}
.hw{{font-size:1.15rem;white-space:nowrap}}
.meta,.lbl{{display:block;font-size:.72rem;color:var(--mut);margin-top:.2rem}}
.flag{{color:var(--acc);font-weight:600}}
audio{{height:34px;width:230px;max-width:100%}}
</style>
<div class="wrap">
<h1>Polish A/B — session 01</h1>
<p class="sub">{n} items. Raw stage-2 takes against their <code>audio-polish.py</code> output.</p>
<div class="note"><strong>Compare against the middle column, not the left one.</strong>
The polish stage applies +8 to +16&nbsp;dB of gain, and in an A/B test the louder clip
wins regardless of quality. <em>Matched</em> is the raw file with gain only — no
high-pass, no trim — at the polished file's loudness, so the difference you hear against
it is the filtering and trimming alone. If <em>matched</em> and <em>polished</em> sound
the same, the chain did its job without colouring the recording.</div>
<div class="scroll"><table>
<tr><th>word</th><th>raw</th><th>raw, level-matched</th><th>polished</th></tr>
{rows}
</table></div>
</div>"""


def main():
    ap = argparse.ArgumentParser(description="Build an A/B listening page.")
    ap.add_argument("--picks", required=True)
    ap.add_argument("--after", required=True, help="directory of processed WAVs")
    ap.add_argument("--out", required=True)
    ap.add_argument("--kbps", type=int, default=96)
    ap.add_argument("--ffmpeg", default="")
    args = ap.parse_args()

    ff = find_ffmpeg(args.ffmpeg)
    with open(args.picks, encoding="utf-8") as fh:
        picks = [r for r in csv.DictReader(fh) if r.get("wav")]

    rows = []
    for r in picks:
        raw_path = r["wav"]
        pol_path = os.path.join(args.after, os.path.basename(raw_path))
        if not (os.path.exists(raw_path) and os.path.exists(pol_path)):
            print("SKIP %s" % os.path.basename(raw_path))
            continue

        xr, sr = load(raw_path)
        xp, srp = load(pol_path)
        lr, _ = loudness_lufs(xr, sr)
        lp, _ = loudness_lufs(xp, srp)

        # Gain-only twin of the raw file at the polished file's loudness.
        gain = 10.0 ** ((lp - lr) / 20.0) if np.isfinite(lr) and np.isfinite(lp) else 1.0
        xm = xr * gain

        flag = r.get("flag", "")
        rows.append(ROW.format(
            hw=html.escape(r["headword"]), iid=r["item_id"], blk=r["block"],
            flag=(' &middot; <span class="flag">%s</span>' % html.escape(flag)) if flag else "",
            raw=to_mp3_datauri(ff, xr, sr, args.kbps),
            mat=to_mp3_datauri(ff, xm, sr, args.kbps),
            pol=to_mp3_datauri(ff, xp, srp, args.kbps),
            rawl="%.1f LUFS" % lr if np.isfinite(lr) else "raw",
            poll="%.1f LUFS" % lp if np.isfinite(lp) else "polished"))
        print("%-28s raw %6.1f -> polished %6.1f LUFS" % (
            os.path.basename(raw_path), lr, lp))

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(PAGE.format(n=len(rows), rows="\n".join(rows)))
    mb = os.path.getsize(args.out) / 1e6
    print("\nwrote %s (%.1f MB, %d items)" % (args.out, mb, len(rows)))


if __name__ == "__main__":
    main()
