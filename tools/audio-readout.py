#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build audio/work/contours.html from contours.json + the token table."""
import csv
import json
import html
import numpy as np

J = json.load(open("audio/work/contours.json", encoding="utf-8"))
META, TOK = J["meta"], J["tokens"]
ALL = list(csv.DictReader(open("audio/work/session-01-tokens-all.csv", encoding="utf-8")))

C1, C2 = "var(--s1)", "var(--s2)"
NP = 60


def esc(s):
    return html.escape(str(s))


# ---------------------------------------------------------------- contour panel
def contour_panel(a, b, title, sub):
    W, H = 700, 250
    PL, PR, PT, PB = 52, 108, 14, 34
    iw, ih = W - PL - PR, H - PT - PB
    series = [(a, C1), (b, C2)]
    vals = [v for it, _ in series for t in TOK[str(it)] for v in t["f0_contour"]]
    lo, hi = min(vals), max(vals)
    pad = max(3.0, (hi - lo) * 0.12)
    lo, hi = lo - pad, hi + pad

    def X(f):
        return PL + f * iw

    def Y(v):
        return PT + ih - (v - lo) / (hi - lo) * ih

    p = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(title)}">']
    # recessive grid + axis
    step = 10 if (hi - lo) > 40 else 5
    g0 = int(np.ceil(lo / step) * step)
    for v in range(g0, int(hi) + 1, step):
        p.append(f'<line class="grid" x1="{PL}" x2="{PL+iw}" y1="{Y(v):.1f}" '
                 f'y2="{Y(v):.1f}"/>')
        p.append(f'<text class="tick" x="{PL-9}" y="{Y(v)+4:.1f}" '
                 f'text-anchor="end">{v}</text>')
    for f, lab in ((0, "0%"), (0.25, "25"), (0.5, "50"), (0.75, "75"), (1, "100%")):
        p.append(f'<text class="tick" x="{X(f):.1f}" y="{H-12}" '
                 f'text-anchor="middle">{lab}</text>')
    p.append(f'<line class="axis" x1="{PL}" x2="{PL+iw}" y1="{PT+ih}" y2="{PT+ih}"/>')

    for item, col in series:
        toks = TOK[str(item)]
        for t in toks:                                    # per-repetition, recessive
            d = " ".join(f"{X(i/(NP-1)):.1f},{Y(v):.1f}"
                         for i, v in enumerate(t["f0_contour"]))
            p.append(f'<polyline class="rep" points="{d}" stroke="{col}"/>')
        mean = np.array([t["f0_contour"] for t in toks], float).mean(axis=0)
        d = " ".join(f"{X(i/(NP-1)):.1f},{Y(v):.1f}" for i, v in enumerate(mean))
        p.append(f'<polyline class="mean" points="{d}" stroke="{col}"/>')
        hw = META[str(item)]["headword"]
        p.append(f'<text class="lbl" x="{PL+iw+10}" y="{Y(mean[-1])+4:.1f}" '
                 f'fill="{col}">{esc(hw)}</text>')
        p.append(f'<circle cx="{X(1):.1f}" cy="{Y(mean[-1]):.1f}" r="4" fill="{col}"/>')
    p.append(f'<text class="axlbl" x="{PL}" y="{PT-2}">Hz</text>')
    p.append("</svg>")

    leg = "".join(
        f'<span class="key"><i style="background:{c}"></i>'
        f'{esc(META[str(i)]["headword"])} <em>{esc(META[str(i)]["frame"])}</em></span>'
        for i, c in series)
    return (f'<figure class="panel"><figcaption><h3>{esc(title)}</h3>'
            f'<p>{sub}</p></figcaption><div class="legend">{leg}</div>'
            f'<div class="plot">{"".join(p)}</div>'
            f'<p class="cap">Thin lines are single repetitions; heavy lines the mean of '
            f'five. Time normalised to each token’s own length.</p></figure>')


# ---------------------------------------------------------------- slope chart
def slope_panel(a, b, title, sub):
    W, H = 700, 260
    PL, PR, PT, PB = 60, 108, 18, 40
    iw, ih = W - PL - PR, H - PT - PB
    da = {t["block"]: t["dur"] for t in TOK[str(a)]}
    dbv = {t["block"]: t["dur"] for t in TOK[str(b)]}
    blocks = sorted(set(da) & set(dbv))
    vals = [da[k] for k in blocks] + [dbv[k] for k in blocks]
    lo, hi = min(vals) - 0.06, max(vals) + 0.06
    xa, xb = PL + iw * 0.18, PL + iw * 0.82

    def Y(v):
        return PT + ih - (v - lo) / (hi - lo) * ih

    p = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(title)}">']
    for v in np.arange(np.ceil(lo * 10) / 10, hi, 0.2):
        p.append(f'<line class="grid" x1="{PL}" x2="{PL+iw}" y1="{Y(v):.1f}" '
                 f'y2="{Y(v):.1f}"/>')
        p.append(f'<text class="tick" x="{PL-9}" y="{Y(v)+4:.1f}" '
                 f'text-anchor="end">{v:.1f}s</text>')
    for k in blocks:
        p.append(f'<line class="slope" x1="{xa:.1f}" y1="{Y(da[k]):.1f}" '
                 f'x2="{xb:.1f}" y2="{Y(dbv[k]):.1f}"><title>block {k}: '
                 f'{da[k]:.2f}s → {dbv[k]:.2f}s</title></line>')
        p.append(f'<circle cx="{xa:.1f}" cy="{Y(da[k]):.1f}" r="5" fill="var(--s1)"/>')
        p.append(f'<circle cx="{xb:.1f}" cy="{Y(dbv[k]):.1f}" r="5" fill="var(--s2)"/>')
        p.append(f'<text class="blk" x="{xa-13:.1f}" y="{Y(da[k])+4:.1f}" '
                 f'text-anchor="end">{k}</text>')
    ma = float(np.mean([da[k] for k in blocks]))
    mb = float(np.mean([dbv[k] for k in blocks]))
    p.append(f'<line class="slopemean" x1="{xa:.1f}" y1="{Y(ma):.1f}" '
             f'x2="{xb:.1f}" y2="{Y(mb):.1f}"/>')
    for x, v, col, item, anc in ((xa, ma, C1, a, "end"), (xb, mb, C2, b, "start")):
        hw = META[str(item)]["headword"]
        dx = -16 if anc == "end" else 16
        p.append(f'<text class="lbl" x="{x+dx:.1f}" y="{Y(v)-14:.1f}" '
                 f'text-anchor="{anc}" fill="{col}">{esc(hw)} {v:.2f}s</text>')
    p.append(f'<text class="tick" x="{xa:.1f}" y="{H-12}" text-anchor="middle">'
             f'{esc(META[str(a)]["headword"])}</text>')
    p.append(f'<text class="tick" x="{xb:.1f}" y="{H-12}" text-anchor="middle">'
             f'{esc(META[str(b)]["headword"])}</text>')
    p.append(f'<text class="axlbl" x="{PL}" y="{PT-4}">token duration</text>')
    p.append("</svg>")
    return (f'<figure class="panel wide"><figcaption><h3>{esc(title)}</h3>'
            f'<p>{sub}</p></figcaption><div class="plot">{"".join(p)}</div>'
            f'<p class="cap">One line per block; the numbered end is the block. The heavy '
            f'line joins the two means. Every block runs the same direction.</p></figure>')


# ---------------------------------------------------------------- token table
def token_table():
    rows = {}
    for r in ALL:
        rows.setdefault(r["item_id"], []).append(r)
    out = ['<div class="tablewrap"><table><thead><tr>'
           '<th>item</th><th>headword</th><th>frame</th><th class="n">n</th>'
           '<th class="n">dur (s)</th><th class="n">F0 med</th>'
           '<th class="n">centroid</th><th class="n">peak dBFS</th>'
           '<th class="n">clipped</th></tr></thead><tbody>']
    for k in sorted(rows, key=int):
        v = rows[k]
        d = np.array([float(q["dur"]) for q in v])
        f = np.array([float(q["f0_med"]) for q in v])
        c = np.array([float(q["f0_centroid"]) for q in v])
        pk = np.array([float(q["peak_dbfs"]) for q in v])
        nclip = sum(1 for q in v if int(q["clipped"]) > 0)
        warn = ' class="warn"' if nclip else ""
        out.append(
            f'<tr><td class="n">{k}</td><td class="hw">{esc(v[0]["headword"])}</td>'
            f'<td>{esc(v[0]["frame"])}</td><td class="n">{len(v)}</td>'
            f'<td class="n">{d.mean():.3f} <span class="sd">±{d.std():.3f}</span></td>'
            f'<td class="n">{f.mean():.1f}</td><td class="n">{100*c.mean():.0f}%</td>'
            f'<td class="n">{pk.mean():.1f}</td>'
            f'<td class="n"{warn}>{nclip or "–"}</td></tr>')
    out.append("</tbody></table></div>")
    return "".join(out)


PAGE = f"""<title>Pilot 01 Acoustics</title>
<style>
:root {{
  --bg:#fbfaf8; --surface:#ffffff; --ink:#1c1a17; --ink2:#4a4640; --ink3:#7d7770;
  --rule:#e3ded6; --s1:#2a78d6; --s2:#eb6834; --warn:#a8442a; --flag:#f5efe4;
  --serif: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  --sans: "Segoe UI", system-ui, -apple-system, sans-serif;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg:#16151a; --surface:#1e1d23; --ink:#eceaf0; --ink2:#b6b2bd; --ink3:#837e8c;
    --rule:#33313b; --s1:#3987e5; --s2:#d95926; --warn:#e08363; --flag:#26242c;
  }}
}}
:root[data-theme="dark"] {{
  --bg:#16151a; --surface:#1e1d23; --ink:#eceaf0; --ink2:#b6b2bd; --ink3:#837e8c;
  --rule:#33313b; --s1:#3987e5; --s2:#d95926; --warn:#e08363; --flag:#26242c;
}}
:root[data-theme="light"] {{
  --bg:#fbfaf8; --surface:#ffffff; --ink:#1c1a17; --ink2:#4a4640; --ink3:#7d7770;
  --rule:#e3ded6; --s1:#2a78d6; --s2:#eb6834; --warn:#a8442a; --flag:#f5efe4;
}}
* {{ box-sizing:border-box; }}
body {{ background:var(--bg); color:var(--ink); font-family:var(--sans);
  line-height:1.6; margin:0; padding:clamp(1.5rem,4vw,3.5rem) 1.25rem 5rem; }}
main {{ max-width:760px; margin:0 auto; display:flex; flex-direction:column; gap:2rem; }}
h1 {{ font-family:var(--serif); font-size:clamp(1.9rem,4.5vw,2.6rem); line-height:1.15;
  margin:0; font-weight:600; text-wrap:balance; letter-spacing:-.01em; }}
h2 {{ font-family:var(--serif); font-size:1.45rem; margin:0 0 .5rem; font-weight:600;
  text-wrap:balance; }}
h3 {{ font-family:var(--serif); font-size:1.12rem; margin:0 0 .2rem; font-weight:600; }}
p {{ margin:0 0 .85rem; }}
p:last-child {{ margin-bottom:0; }}
.eyebrow {{ font-size:.74rem; letter-spacing:.14em; text-transform:uppercase;
  color:var(--ink3); margin:0 0 .6rem; font-weight:600; }}
.lede {{ font-size:1.06rem; color:var(--ink2); }}
section {{ display:flex; flex-direction:column; gap:.35rem; }}
section.note {{ background:var(--flag); border:1px solid var(--rule); border-radius:10px;
  padding:1.1rem 1.25rem; gap:.6rem; }}
section.note h2 {{ margin-top:0; }}
.flag {{ background:var(--flag); border-left:3px solid var(--s2); padding:.9rem 1.1rem;
  border-radius:0 6px 6px 0; font-size:.93rem; color:var(--ink2); }}
.flag strong {{ color:var(--ink); }}
.panel {{ margin:0; background:var(--surface); border:1px solid var(--rule);
  border-radius:10px; padding:1.15rem 1.25rem 1rem; display:flex;
  flex-direction:column; gap:.7rem; }}
.panel figcaption p {{ margin:0; color:var(--ink2); font-size:.92rem; }}
.plot {{ overflow-x:auto; }}
.plot svg {{ width:100%; min-width:520px; height:auto; display:block; }}
.legend {{ display:flex; gap:1.1rem; flex-wrap:wrap; font-size:.85rem;
  color:var(--ink2); }}
.key {{ display:inline-flex; align-items:center; gap:.4rem; }}
.key i {{ width:11px; height:11px; border-radius:2px; display:inline-block; }}
.key em {{ color:var(--ink3); font-style:normal; font-size:.78rem; }}
.cap {{ font-size:.8rem; color:var(--ink3); margin:0; }}
.rep {{ fill:none; stroke-width:1.15; opacity:.3; }}
.mean {{ fill:none; stroke-width:2.6; stroke-linejoin:round; stroke-linecap:round; }}
.grid {{ stroke:var(--rule); stroke-width:1; }}
.axis {{ stroke:var(--rule); stroke-width:1.5; }}
.slope {{ stroke:var(--ink3); stroke-width:1.6; opacity:.5; }}
.slopemean {{ stroke:var(--ink); stroke-width:2.8; opacity:.85; }}
text {{ font-family:var(--sans); font-variant-numeric:tabular-nums; }}
.tick {{ font-size:11px; fill:var(--ink3); }}
.blk {{ font-size:10px; fill:var(--ink3); }}
.axlbl {{ font-size:10.5px; fill:var(--ink3); letter-spacing:.08em;
  text-transform:uppercase; }}
.lbl {{ font-size:13px; font-weight:600; }}
.tablewrap {{ overflow-x:auto; border:1px solid var(--rule); border-radius:10px;
  background:var(--surface); }}
table {{ border-collapse:collapse; width:100%; font-size:.86rem; min-width:560px; }}
th, td {{ padding:.42rem .7rem; text-align:left;
  border-bottom:1px solid var(--rule); }}
th {{ font-size:.72rem; letter-spacing:.06em; text-transform:uppercase;
  color:var(--ink3); font-weight:600; }}
tbody tr:last-child td {{ border-bottom:none; }}
.n {{ text-align:right; font-variant-numeric:tabular-nums; }}
.hw {{ font-family:var(--serif); font-size:1rem; }}
.sd {{ color:var(--ink3); font-size:.78em; }}
td.warn {{ color:var(--warn); font-weight:600; }}
dl {{ display:grid; grid-template-columns:auto 1fr; gap:.3rem 1rem; margin:0;
  font-size:.9rem; }}
dt {{ color:var(--ink3); }}
dd {{ margin:0; font-variant-numeric:tabular-nums; }}
footer {{ border-top:1px solid var(--rule); padding-top:1rem; font-size:.83rem;
  color:var(--ink3); }}
code {{ font-size:.86em; background:var(--flag); padding:.1em .35em;
  border-radius:3px; }}
</style>

<main>
<header>
  <p class="eyebrow">Rickett Yack &middot; session 01 &middot; 12 Aug 2026</p>
  <h1>Does prominence placement survive into production?</h1>
  <p class="lede">122 of 125 recorded tokens, segmented automatically and measured.
  Two claims were on trial: that pitch marks V&#8321; where the spec says it does, and
  that <em>n&oacute;&egrave;</em>&thinsp;/&thinsp;<em>no&ecirc;</em> is a pitch minimal
  pair. The first is suggestive. The second appears to be carried by something else
  entirely.</p>
</header>

<section>
  <div class="flag"><strong>Provisional.</strong> One speaker &mdash; the language&rsquo;s
  designer &mdash; producing citation forms he wrote the rules for. This can show whether
  his production matches the spec; it cannot confirm the pitch-accent residue analysis in
  <code>phonology.md</code> &sect;3.4. Nothing here should be written into the grammar as
  confirmation. Five repetitions detect large effects only.</div>
</section>

<section>
  <h2>The one consistent effect is duration, not pitch</h2>
  <p><code>dictionary.md</code> declares <em>n&oacute;&egrave;</em> &lsquo;no way&rsquo;
  and <em>no&ecirc;</em> &lsquo;in a way&rsquo; a minimal pair separated &ldquo;by spelling
  and pitch, not the broad IPA.&rdquo; Both are /no&#603;/. Their F0 centroids differ by
  4.3&nbsp;pp with a standard deviation of 23.4 &mdash; noise. Their durations differ by
  280&nbsp;ms, and every block agrees.</p>
</section>
{slope_panel(5, 6, "Frame B — nóè vs noê, duration",
             "Same segments, same speaker, five blocks. 5/5 same-sign.")}

<section>
  <p>280&nbsp;ms is 57% of the shorter token &mdash; not a subtle effect. But length is
  not what the pair is documented to contrast, and a confound is available: <em>n&oacute;&egrave;</em>
  is an emphatic interjection and <em>no&ecirc;</em> a hedging adverb, so the difference
  may be delivery rather than phonology. Testing that needs the pair in frames that hold
  pragmatics constant, which pilot 01 does not contain.</p>
</section>

<section class="note">
  <h2>Follow-up: the pitch the entry describes is not in the recording</h2>
  <p>Neither member of this pair has a V&#8321; accent. <em>n&oacute;&egrave;</em>&rsquo;s
  mean contour is flat &mdash; its first third averages <strong>1.8&nbsp;Hz lower</strong>
  than its last third, i.e. very slightly <em>rising</em> &mdash; and <em>no&ecirc;</em> is
  equally flat at +1.5&nbsp;Hz. The Frame&nbsp;A items, which do carry an accent, decline
  from it: <em>&oacute;h&ograve;</em> by 16.3&nbsp;Hz, <em>h&oacute;hon&igrave;t</em> by
  10.9, <em>oh&ocirc;</em> by 9.1. Both Frame&nbsp;B words also begin some 16&nbsp;Hz below
  the Frame&nbsp;A onsets, at the floor of the speaker&rsquo;s range. The 4.3&nbsp;pp
  centroid &ldquo;shift&rdquo; above is two flat contours differing by noise.</p>
  <p>The author&rsquo;s reading, on seeing this: both words descend from GA phrases accented
  on their <em>second</em> element &mdash; <em>in a WAY</em> and <em>no, WAY!</em> &mdash; so
  <em>no</em> is unstressed in both. The entry&rsquo;s &ldquo;residual high pitch on
  <em>no</em>&rdquo; was derived from a <em>NO way!</em> realization, which exists but is
  much rarer. The production followed GA; the prescription did not.</p>
  <p><strong>The pause explanation for the 280&nbsp;ms was tested and does not hold.</strong>
  If the extra length were the comma in <em>no, WAY!</em> it would be silence. The longest
  internal sub-threshold run is 44&nbsp;ms in <em>both</em> words, and removing every
  internal low-energy frame still leaves 252 of the 280&nbsp;ms. The independent check is
  sharper: the endpointer bridges dips only up to 150&nbsp;ms, so a real 200&ndash;300&nbsp;ms
  pause would have halted the boundary walk and left a second sounding chunk outside the
  token. In all five blocks the token is one unbroken run. The extra length is sounding
  material, and the emphatic-vs-hedging confound is still standing.</p>
</section>

<section>
  <h2>Pitch placement: the predicted direction, inconsistently</h2>
  <p>All three segmentally-matched pairs shift their F0 centroid the way the spec
  predicts. Only the /oho/ pair does so with a large effect, and no pair is consistent
  across all five blocks.</p>
</section>
{contour_panel(1, 2, "Frame A — pitch on V₁ vs V₂",
               "Both /oho/. Prediction: óhò front-loaded, ohô later.")}
{contour_panel(4, 3, "Frame A supporting — hóhonìt vs hohô",
               "Same vowel quality throughout; hóhonìt adds a third syllable.")}
{contour_panel(5, 6, "Frame B — the declared minimal pair",
               "The contrast the dictionary asserts. The tracks overlap.")}

<section>
  <h2>Consistency, block by block</h2>
  <p>Each block contributes one token per item, so pairs can be compared within a block
  &mdash; which is what the blocked reading order was for. With five blocks, all five
  agreeing is the weakest result that means anything.</p>
  <dl>
    <dt>&oacute;h&ograve; &rarr; oh&ocirc;, centroid</dt><dd>+10.1 pp &middot; d = +1.13 &middot; 4/5 blocks</dd>
    <dt>h&oacute;hon&igrave;t &rarr; hoh&ocirc;, centroid</dt><dd>+5.9 pp &middot; d = +0.54 &middot; 3/5 blocks</dd>
    <dt>n&oacute;&egrave; &rarr; no&ecirc;, centroid</dt><dd>+4.7 pp &middot; d = +0.30 &middot; 3/5 blocks</dd>
    <dt>n&oacute;&egrave; &rarr; no&ecirc;, duration</dt><dd>&minus;280 ms &middot; <strong>5/5 blocks</strong></dd>
  </dl>
</section>

<section>
  <h2>All 25 items</h2>
  <p>Centroid is the F0-weighted mean time across the token; a flat contour lands near
  50%. Clipped counts are tokens with samples at full scale &mdash; their amplitude is
  destroyed, which is why loudness is absent from every claim above.</p>
</section>
{token_table()}

<section>
  <h2>How the numbers were made</h2>
  <p>Whisper reads only the spoken English digit slates, never the conlang, and its
  timestamps are used to say <em>which item is where</em> &mdash; never where a word
  begins. Boundaries come from a local energy search inside each pinned interval, cut at a
  threshold relative to each token&rsquo;s own peak so that a loud token is not measured
  longer than a quiet one for being loud. F0 is a normalised-autocorrelation track with
  octave repair, 55&ndash;200&nbsp;Hz.</p>
  <p>That floor was 70&nbsp;Hz until this revision, which was a defect: the speaker&rsquo;s
  median is 84.5&nbsp;Hz, leaving about four semitones of headroom, and creak at the end of a
  citation word fell straight through it. The tracker did not report those frames as
  unvoiced &mdash; it returned the octave above, and 27 of 120 tokens had their minimum
  sitting exactly on the rail. At a 55&nbsp;Hz floor the railing disappears while the median
  voiced fraction is unmoved (0.40&nbsp;&rarr;&nbsp;0.41), which is the check that the change
  admits signal rather than noise. Every F0 figure on this page is from the corrected run.</p>
  <p>Read the voiced fractions in the table before leaning on any single F0 number: the
  median is 0.47 and 19 of 120 tokens fall below 0.30, meaning roughly half the frames of a
  typical token contribute nothing to its pitch summary. The duration result requires no
  pitch tracking at all, which is much of why it is the sturdiest number here.</p>
  <p>Three tokens of 125 resolved ambiguously and were dropped rather than guessed at:
  block 1 <em>to&#347;</em>, block 2 <em>b&eacute;nts&#305;&igrave;y</em>, block 5
  <em>rhiits&ocirc;</em>. They are listed with timestamps in the segment table for a
  listen.</p>
</section>

<footer>
  <p>Generated from <code>audio/masters/session-01.wav</code> by
  <code>audio-slate-align.py</code> &rarr; <code>audio-split.py</code> &rarr;
  <code>audio-contour.py</code>. Plan and milestones:
  <code>planning/audio-pipeline-plan.md</code>.</p>
</footer>
</main>
"""

open("audio/work/contours.html", "w", encoding="utf-8").write(PAGE)
print("wrote audio/work/contours.html", len(PAGE), "bytes")
