# Plan: Website design system — deploy fix, token SSOT, design sandbox, presets, apply pipeline

**Status:** approved by author 2026-07-03, not started · **Opened:** 2026-07-03 · **Owner:** author (Matt) + Claude

A multi-session plan to (1) unblock GitHub Pages deployment, (2) centralize every visual design decision into one token file, (3) build a standalone design-sandbox tool for exploring typography/layout on real content, (4) ship a set of curated presets, and (5) wire a one-command path from a saved configuration to the deployed site. Written to be executable step-by-step by another model (e.g. Opus) with no prior context beyond this file and `CLAUDE.md`.

How to use: tasks are `- [ ]` (todo) / `- [x]` (done). Milestones are ordered by dependency; D0 is independent and can run first or in parallel. Do not skip the **Execution notes** section at the end — it holds the environment gotchas.

---

## 1. Context (read before executing)

**The site.** `site/` is an Astro + Starlight static-site build that compiles the canonical Markdown under `docs/` into HTML. It deploys to GitHub Pages at `https://mattschinn.github.io/ref_grammar/` via `.github/workflows/deploy-pages.yml`. The build is: `scripts/build-content.mjs` (content compiler: assembles sibling docs into one `language_reference` page, syncs example previews, emits JSON artifacts to `src/generated/`) → `astro build` (with `src/plugins/remark-conlang.mjs` resolving §-references, dictionary headwords, and gloss tags into hover-carded links).

**How styling works today (the problem).** Design decisions are scattered across four places:
- `site/src/styles/site-theme.css` — Brill `@font-face`, `--sl-font` overrides, 6 palette variables per theme, one body-size nudge.
- `site/src/styles/hovercard.css` — hovercard + reference-link styling, mixing `--sl-*` variables and literals.
- `site/src/styles/diacritic-typer.css` — the typer widget, same mix.
- `site/astro.config.mjs` — the EB Garamond Google Fonts `<link>` tags and the inline client-script injection (`diacritics.js` → `hovercard.js` → `search-diacritics.js`, order load-bearing).

**How examples reach the page (critical for D5e).** `examples.md` records are chunk-aligned (`|`-delimited; see `examples.md` §2 for which layers are aligned vs free-line). `sync-previews.mjs` renders each `<!-- example: EID | spec -->` token's preview *as markdown* into the canonical docs; `build-content.mjs` then calls `stripExamples()` (`site/scripts/examples-render.mjs`) which collapses token+preview to the plain markdown blockquote. So today the site's example HTML is just `<blockquote>` lines — no chunk structure survives to HTML. The per-chunk data *does* survive in `site/src/generated/examples.json` (`segments[]` per record). The PDF pipeline (`pdf/build.ps1`) does its own strip of the same previews and must remain untouched by this plan.

**Deployment failure (diagnosed 2026-07-03).** The author saw "Node.js 20 is deprecated… forced to run on Node.js 24" and read it as the failure. It is a benign annotation about the actions' internal runtime. The actual blocker (high confidence, not log-confirmed — no `gh` CLI locally): the workflow's `node-version: 20` while the installed Astro requires **Node ≥ 22.12.0** (`site/node_modules/astro/package.json` → `engines.node`). Additionally, the workflow triggers only on push to `main`, but `main` is the stale pre-reorg "first commit" (contains neither `site/` nor the workflow); all work is on `interactive-grammar-site`, which is also ahead of its own remote. Deploys therefore cannot trigger automatically at all.

**Author's aesthetic brief.** The site feels like a wall of text. Wanted: examples visually set off as eye-catching breaks from body text (bigger, different face/color); per-gloss-layer differentiation; slightly larger body text; stronger heading differentiation; two-column treatment for dense stretches; interlinear glosses with (a) hover highlighting coordinated across lines and (b) easier column-wise reading; deliberately differentiated light vs dark modes; lots of pictures *later* (gated on the author producing them). Everything **understated** — pleasing, not distracting. Author is partial to EB Garamond (bookish), Inter, and Inconsolata, but wants a wide net cast.

## 2. Desired end state

When this plan is complete:

1. The site deploys automatically to GitHub Pages on push, green.
2. **One file — `site/src/styles/tokens.css` — is the single source of truth** for every color, font, size, spacing, and feature-flag decision. All other stylesheets consume tokens; none define design values. The file is generated, never hand-edited.
3. **`tools/design-sandbox.html`** is a self-contained, double-click-to-open page showing real grammar prose + real interlinear examples, with a control panel that live-edits the same tokens, curated presets, named save slots (localStorage), and JSON export/import.
4. **`site/design/presets/*.json`** hold curated + author-saved configurations; `node site/scripts/apply-design.mjs site/design/presets/<name>.json` regenerates `tokens.css` (and `fonts.css`). Applying a look to the deployed site is: export from sandbox → drop file in presets/ → run script → commit → push.
5. Examples render on the site as chunk-column interlinear blocks with pure-CSS coordinated hover-highlighting; body/heading/example typography and the light/dark palettes are whatever preset the author last applied.
6. The PDF pipeline, the canonical docs' content, and the examples corpus are byte-identical to before (except the gated D5d column markers, if the author approves them).

## 3. Decisions locked (author Q&A, 2026-07-03)

- **Sandbox form:** standalone single HTML file in `tools/` (like `diacritic-typer.html`). No build, no server, opens from `file://`.
- **Apply path:** preset JSON + apply script (option chosen over copy-paste and File System Access API).
- **Fonts:** explore via Google Fonts CDN in the sandbox; whichever fonts the *final applied preset* uses get self-hosted into `site/public/fonts/` (all candidates are OFL/free). End state: deployed site makes no external font requests.
- **Two-column:** per-block opt-in ("columned prose islands"), never a global prose switch. Author's refinement: prose runs that sit *between* full-width examples/media are short enough that the scroll-back-up objection mostly vanishes — the sandbox must include exactly this mixed layout to judge. Examples themselves always stay single-column/full-width.
- **Pictures:** gated on author-made assets. Reserve figure tokens now (D6); no image work in this plan.
- **Tone:** understated. Presets should differ in voice, not loudness.

## 4. Milestone D0 — unblock deployment (independent; do first)

- [x] **D0a. Fix the workflow.** In `.github/workflows/deploy-pages.yml`: change `node-version: 20` → `node-version: 24`; bump `actions/checkout@v4` → `@v5` and `actions/setup-node@v4` → `@v5` (or newest majors — check the actions' repos if unsure). Keep everything else (npm cache config, `working-directory: site`, the two-job build/deploy shape) unchanged. *(Done 2026-07-03: checkout@v5, setup-node@v5, node 24; upload-pages-artifact@v3/deploy-pages@v4 left as current.)*
- [ ] **D0b. Merge to `main` (decided 2026-07-03).** Push the branch, then fast-forward main: `git push origin interactive-grammar-site`, then `git checkout main && git merge --ff-only interactive-grammar-site && git push origin main`. If `--ff-only` fails (diverged history), do a regular merge instead. `main` becomes the live trunk from here on; future work merges to it to deploy.
- [ ] **D0c. Verify Pages settings** (author, on github.com): repo → Settings → Pages → Source = "GitHub Actions".
- [ ] **D0d. Confirm deploy.** After push, the workflow runs; check `https://mattschinn.github.io/ref_grammar/` renders, sidebar navigation works, and hovers appear on a `§`-reference and a dictionary headword (this exercises the `/ref_grammar` base path end to end). If the build *still* fails, get the failing step's log text from the author — the Node-engines diagnosis is high-confidence but was made without log access.

## 5. Milestone D1 — token SSOT (foundation for everything below)

**Goal:** all design values live in `site/src/styles/tokens.css`; the site looks pixel-identical before/after (this milestone moves values, it does not change them).

- [x] **D1a. Create `site/src/styles/tokens.css`** with the schema below, populated with the *current* site's values (so nothing visibly changes). Header comment: `/* GENERATED — single source of truth for site design. Edit via site/design/presets + apply-design.mjs, not by hand. */` (hand-write it this once; D4 makes it generated for real).

  Token schema (names are normative — the sandbox and apply script must use exactly these):

  *(Done 2026-07-03. Deviations from the illustrative schema, all to preserve pixel-parity with the current site: `--cl-font-code` uses the current site's full mono stack, not the shortened one shown here; `--cl-leading-body`/`--cl-measure` are defined but not yet applied to `.sl-markdown-content` — leading/measure wiring is deferred to D5a so nothing changes now. Added tokens for consumers: `--cl-card-title`, `--cl-card-body`, `--cl-ref-section-border`, `--cl-ui-text`, `--cl-ui-text-accent`, `--cl-ui-muted`, `--cl-code-bg`, `--cl-typer-trigger`, `--cl-typer-receiver`.)*

  ```css
  :root {
    /* — fonts (stacks include self-hosted/system fallbacks) — */
    --cl-font-body: 'EB Garamond', 'Brill', Georgia, serif;
    --cl-font-heading: var(--cl-font-body);
    --cl-font-ui: var(--cl-font-body);            /* nav, sidebar, buttons */
    --cl-font-code: ui-monospace, 'Cascadia Code', Consolas, 'Brill', monospace;
    --cl-font-conlang: 'Brill', 'EB Garamond', serif;   /* example conlang line */
    --cl-font-etym: var(--cl-font-body);
    --cl-font-ipa: 'Brill', serif;
    --cl-font-leipzig: var(--cl-font-body);
    --cl-font-translation: var(--cl-font-body);

    /* — type scale & rhythm — */
    --cl-size-body: 1.125rem;
    --cl-leading-body: 1.6;
    --cl-measure: 72ch;                 /* max text column width; Starlight default ≈ 67.5rem content — apply via .sl-markdown-content */
    --cl-scale-conlang: 1.35;           /* multipliers on body size */
    --cl-scale-etym: 0.9;
    --cl-scale-ipa: 0.95;
    --cl-scale-leipzig: 0.8;
    --cl-scale-translation: 1.0;
    --cl-heading-weight: 600;
    --cl-heading-tracking: 0;
    --cl-heading-variant: normal;        /* e.g. small-caps */
    --cl-heading-space-above: 2.2em;
    --cl-heading-space-below: 0.7em;
    --cl-heading-rule: none;             /* e.g. 1px solid var(--cl-accent-low) */

    /* — example block ("island") — */
    --cl-example-pad: 0.9em 1.1em;
    --cl-example-radius: 0.4rem;
    --cl-example-rule: 3px solid var(--cl-accent);   /* left rule */
    --cl-chunk-gap: 1.25em;

    /* — columned prose islands — */
    --cl-cols-count: 2;
    --cl-cols-gap: 2.5em;
    --cl-cols-rule: none;

    /* — reserved for figures (D6, gated) — */
    --cl-figure-border: 1px solid var(--cl-accent-low);
    --cl-figure-caption-scale: 0.85;
  }

  /* — per-theme colors (dark = default, matching Starlight) — */
  :root {
    --cl-bg: #1a1a1a;          --cl-bg-nav: #242422;      --cl-bg-sidebar: #1f1f1d;
    --cl-accent: #b85a92;      --cl-accent-high: #ecb6d6;  --cl-accent-low: #3a2630;
    --cl-conlang-color: var(--cl-accent-high);
    --cl-example-bg: color-mix(in srgb, var(--cl-accent) 8%, transparent);
    --cl-highlight-bg: color-mix(in srgb, var(--cl-accent) 22%, transparent);
    --cl-badge-settled: #4a8f5c; --cl-badge-provisional: #b0802b; --cl-badge-open: #a8555f;
    --cl-card-bg: var(--cl-bg-nav); --cl-card-border: var(--sl-color-gray-5);
  }
  :root[data-theme='light'] {
    --cl-bg: #fafaf8;          --cl-bg-nav: #ffffff;      --cl-bg-sidebar: #f3f1ec;
    --cl-accent: #a8447e;      --cl-accent-high: #7c3158;  --cl-accent-low: #f6e3ef;
    --cl-conlang-color: var(--cl-accent);
    --cl-example-bg: color-mix(in srgb, var(--cl-accent) 5%, transparent);
    --cl-highlight-bg: color-mix(in srgb, var(--cl-accent) 14%, transparent);
    --cl-badge-settled: #2e7042; --cl-badge-provisional: #8a6114; --cl-badge-open: #93404a;
    --cl-card-bg: var(--cl-bg-nav); --cl-card-border: var(--sl-color-gray-5);
  }

  /* — bridge: Starlight consumes the tokens — */
  :root {
    --sl-font: var(--cl-font-body);
    --sl-font-mono: var(--cl-font-code);
    --sl-color-bg: var(--cl-bg); --sl-color-bg-nav: var(--cl-bg-nav); --sl-color-bg-sidebar: var(--cl-bg-sidebar);
    --sl-color-accent: var(--cl-accent); --sl-color-accent-high: var(--cl-accent-high); --sl-color-accent-low: var(--cl-accent-low);
  }
  ```

- [x] **D1b. Refactor consumers.** `site-theme.css` keeps only the Brill `@font-face` blocks and rules that *apply* tokens (`.sl-markdown-content { font-size: var(--cl-size-body); line-height: var(--cl-leading-body); }` etc.). `hovercard.css` and `diacritic-typer.css`: replace every `--sl-*` read and hard-coded design literal with the matching `--cl-*` token (add tokens if a value has no home — the schema above is a floor, not a ceiling). Register `tokens.css` **first** in `astro.config.mjs` `customCss`.
- [x] **D1c. Split font loading into `site/src/styles/fonts.css`.** Move the Google Fonts EB Garamond loading out of `astro.config.mjs` head-`<link>`s into an `@import url(...)` at the top of `fonts.css` (imports must precede other rules; register it before `tokens.css`). Brill `@font-face` moves here too. Rationale: D4's apply script owns this file; `astro.config.mjs` never needs editing again for fonts. Remove the three font `<link>`/preconnect tags from the config.
- [x] **D1d. Verify parity.** `npm run build` in `site/` (clear `node_modules/.astro` first). Compare against a pre-refactor build: same fonts render (body EB Garamond, IPA glyphs via Brill), same palette both themes, hovercards styled, typer page intact. `node scripts/link-check.mjs` clean. *(Done 2026-07-03: build green, 9 pages. Verified in built CSS: EB Garamond `@import` present, `--cl-accent` = `#b85a92` dark / `#a8447e` light, bridge `--sl-color-accent: var(--cl-accent)` present. §11 acceptance grep now returns only `tokens.css`/`fonts.css`. Build had to be run against committed `examples.md` — the working-tree copy has an author WIP edit that breaks the parser, see note to author. link-check output is the usual pre-existing assembly-refactor bare-ref list, unchanged by this work.)*

## 6. Milestone D2 — the design sandbox (`tools/design-sandbox.html`)

**Goal:** one self-contained HTML file (inline CSS+JS, no dependencies, no build; the only network use is Google Fonts). It renders a realistic mock page governed entirely by the D1 token names, with live controls, presets, saves, and export.

- [ ] **D2a. Gather embedded content** (at generation time — bake into the file as literals):
  - Prose: 2–3 subsections from `docs/reference/verbal-system.md` (post-B1b it contains `<!-- example: -->` tokens + previews; take the preview-rendered text, strip the HTML-comment markers). Pick sections that mix prose, an example, more prose — needed for the columned-island trial. Include at least one `[Settled]`/`[Provisional]` status tag and a few gloss tags (VOL, NVOL…) for badge/hover mocking.
  - Examples: run `node site/scripts/build-content.mjs`, then take 3 records from `site/src/generated/examples.json`: E001 (8 chunks), one carrying a `gesture` layer (E003 or E010), and one long one from the E020+ range. Check `docs/reference/examples.md` §2 first for which layers are chunk-aligned (conlang/etym at minimum) vs free lines (translation; verify ipa and leipzig) — the mock markup must reflect reality.
  - Glyph gauntlet inventories: the full letter+diacritic inventory from `docs/quickref/orthography-quickref.md` and the IPA inventory from `docs/quickref/phonology-quickref.md`.
- [ ] **D2b. Page skeleton.** Two panes: fixed-position control panel (left, collapsible groups, its own neutral styling — *not* token-governed, so it never contaminates judgment) and the mock page (right). The mock page: a slim fake top-nav and sidebar stub (so density reads realistically), then the content column. Every mock-page style reads `var(--cl-*)` — the same names as D1, set on the mock-page container. Theme toggle button flips `data-theme="light"`/`"dark"` on the container; both theme palettes are held in JS and written as inline custom properties on toggle/edit.
- [ ] **D2c. Interlinear markup (normative — D5e must ship this exact shape).** Chunk-as-column: each chunk is a flex column containing that chunk's cell from every *aligned* layer; free layers are full-width lines below. This makes 4a hover-coordination **pure CSS** (hovering a chunk column highlights all its layers at once) and gives graceful narrow-screen wrapping (chunks wrap as units):

  ```html
  <figure class="cl-example" id="E003">
    <div class="cl-ex-grid">
      <div class="cl-ex-chunk">
        <span class="cl-ex-conlang">hoiom</span>
        <span class="cl-ex-etym">*human</span>
        <span class="cl-ex-leipzig">man</span>
      </div>
      <!-- …one .cl-ex-chunk per chunk… -->
    </div>
    <div class="cl-ex-free cl-ex-ipa">/ˈhoiom …/</div>      <!-- only if ipa is a free line -->
    <div class="cl-ex-free cl-ex-gesture">χ …</div>
    <div class="cl-ex-free cl-ex-translation">"…"</div>
  </figure>
  ```
  ```css
  .cl-ex-grid { display: flex; flex-wrap: wrap; column-gap: var(--cl-chunk-gap); row-gap: .6em; }
  .cl-ex-chunk { display: flex; flex-direction: column; border-radius: .25em; }
  .cl-ex-chunk:hover { background: var(--cl-highlight-bg); }   /* 4a, zero JS */
  .cl-ex-conlang { font-family: var(--cl-font-conlang); font-size: calc(1em * var(--cl-scale-conlang)); color: var(--cl-conlang-color); font-style: italic; }
  /* …etym/ipa/leipzig/translation analogous, each from its own font+scale tokens… */
  .cl-example { background: var(--cl-example-bg); border-left: var(--cl-example-rule); border-radius: var(--cl-example-radius); padding: var(--cl-example-pad); }
  ```
- [ ] **D2d. Control panel.** Groups mirroring the token schema: Fonts (one `<select>` per font role from the candidate list below + a free-text input; selecting a Google font injects its `<link>` once, lazily), Type scale (sliders with numeric readouts for sizes/scales/leading/measure), Headings (weight/variant/tracking/rule/spacing), Colors (color inputs for the *active* theme; switching theme switches which set you edit), Example block (pad/radius/rule/gap), Features (checkboxes: example island on/off, chunk-grid vs plain-blockquote example rendering, hover highlight, columned islands, status badges, heading rules). Every control writes the custom property immediately.
  Candidate font list: *serif* EB Garamond, Literata, Source Serif 4, Alegreya, Vollkorn, Crimson Pro, Gentium Book Plus, Charis SIL, Brill (self-hosted note); *sans* Inter, Source Sans 3, IBM Plex Sans, Andika; *mono* Inconsolata, JetBrains Mono, IBM Plex Mono, Fira Code, Iosevka (⚠ not on Google Fonts — list it but mark "self-host only"; sandbox may load it from jsDelivr's `iosevka-webfont` package or skip); *display/headings* Fraunces. All OFL.
- [ ] **D2e. Glyph gauntlet.** A pinned strip rendering the D2a inventories in `--cl-font-conlang` and `--cl-font-ipa` **with no fallback fonts appended** (e.g. `font-family: 'Literata'` alone), so missing glyphs show as tofu immediately. A small caption explains this. This is the coverage audit: a font that tofus the inventory can still be used for prose, but not for the conlang/IPA roles.
- [ ] **D2f. Presets, saves, export.** Embed the five D3 presets as a JS array (copied verbatim from `site/design/presets/` at build-of-sandbox time; comment noting the copy must be refreshed if presets change). Preset `<select>` applies one wholesale. "Save as…" stores the current full config under a name in `localStorage`; saved list with Load/Delete. "Export JSON" downloads the current config as a preset-schema file (this is the file D4's apply script consumes — name it `<preset-name>.json`). "Import JSON" via `<input type=file>` round-trips.
- [ ] **D2g. Columned-island trial.** The mock's prose runs are wrapped in `.cl-prose-run` divs; the Features toggle adds `.cl-cols` → `column-count: var(--cl-cols-count); column-gap: var(--cl-cols-gap); column-rule: var(--cl-cols-rule)`, with a `@media (max-width: 60rem)` collapse to one column. The mock must include one short run (≤ half viewport) and one long run between examples, so the author can feel where the scroll-back problem starts.
- [ ] **D2h. Acceptance.** Opens from `file://` in a Chromium browser and Firefox; all controls live-update; theme toggle flips palettes; presets apply; save/load/delete/export/import round-trip; gauntlet shows tofu for a known-incomplete font (e.g. Inconsolata on IPA); no console errors; works offline except font fetches.

## 7. Milestone D3 — curated presets (`site/design/presets/*.json`)

- [ ] **D3a. Define the preset JSON schema** (documented in `site/design/README.md`):

  ```json
  {
    "name": "bookish",
    "description": "one line",
    "fonts": {
      "body":    { "family": "EB Garamond", "source": "google", "fallbacks": ["Brill", "Georgia", "serif"] },
      "heading": { "family": "EB Garamond", "source": "google", "fallbacks": ["serif"] },
      "conlang": { "family": "Brill", "source": "self", "fallbacks": ["EB Garamond", "serif"] },
      "ipa":     { "family": "Brill", "source": "self", "fallbacks": ["serif"] },
      "etym": {}, "leipzig": {}, "translation": {}, "ui": {}, "code": {}
    },
    "type": { "sizeBody": "1.125rem", "leadingBody": 1.6, "measure": "72ch",
              "scaleConlang": 1.35, "scaleEtym": 0.9, "scaleIpa": 0.95, "scaleLeipzig": 0.8, "scaleTranslation": 1.0,
              "headingWeight": 600, "headingTracking": "0", "headingVariant": "normal",
              "headingSpaceAbove": "2.2em", "headingSpaceBelow": "0.7em", "headingRule": "none" },
    "example": { "pad": "0.9em 1.1em", "radius": "0.4rem", "rule": "3px solid var(--cl-accent)", "chunkGap": "1.25em" },
    "cols": { "count": 2, "gap": "2.5em", "rule": "none" },
    "themes": {
      "dark":  { "bg": "#1a1a1a", "bgNav": "#242422", "bgSidebar": "#1f1f1d", "accent": "#b85a92", "accentHigh": "#ecb6d6", "accentLow": "#3a2630", "conlangColor": "var(--cl-accent-high)", "badgeSettled": "#4a8f5c", "badgeProvisional": "#b0802b", "badgeOpen": "#a8555f" },
      "light": { "…": "…" }
    },
    "features": { "exampleIsland": true, "interlinearGrid": true, "hoverHighlight": true, "colsIslands": false, "badges": true, "headingRules": false }
  }
  ```
  Empty font-role objects inherit `body`. `source` ∈ `google | self | system`. Unknown keys must make the apply script fail loudly.

- [ ] **D3b. Author the five presets** (values are starting points — the sandbox exists to tune them; keep all understated):
  1. **`bookish.json`** — the current site, refined. EB Garamond body+headings (headings gain `small-caps` variant + accent-colored §-numbers), conlang line Brill ×1.35 in the rose accent, warm paper light theme / soft charcoal dark, current rose palette.
  2. **`field-notes.json`** — Gentium Book Plus body (SIL linguistics-monograph voice, near-complete IPA — may serve conlang *and* ipa roles alone), Inter headings (weight 600), Inconsolata leipzig line, olive/ochre palette (light: bg `#faf9f4`, accent `#6b7f3a`; dark: bg `#20221c`, accent `#a8bf6a`).
  3. **`studio.json`** — Inter body/headings/ui (the figure-ground inversion: sans body makes serif examples pop), conlang line EB Garamond italic ×1.45, Literata translation line, Inconsolata leipzig, cool gray palette with slate-blue accent (light `#4a6fa5` / dark `#8ab4e8`).
  4. **`plex.json`** — IBM Plex Serif body, Plex Sans headings/ui, Plex Mono leipzig+code: one superfamily, three coordinated voices. Neutral palette, Plex-blue accent.
  5. **`concordance.json`** — Source Serif 4 body, Source Sans 3 headings, entire gloss block in **JetBrains Mono** (decided 2026-07-03: Iosevka is vendored and swapped in only if this preset becomes the finalist — do not self-host it speculatively), hover highlight prominent, amber accent (light `#8a6114` / dark `#e0a84f`). The "corpus tool" voice.
- [ ] **D3c. Sync into the sandbox** (refresh the embedded copies from D2f) and verify each preset applies cleanly in both themes; run the glyph gauntlet against each preset's conlang/ipa fonts and note gaps in the preset's `description`.

## 8. Milestone D4 — apply pipeline

- [ ] **D4a. Write `site/scripts/apply-design.mjs`.** Node, zero deps. Usage: `node site/scripts/apply-design.mjs site/design/presets/<name>.json`. Behavior: validate against the D3a schema (fail loudly on unknown/missing keys); deterministically emit (1) `site/src/styles/tokens.css` — the full D1a schema populated from the preset, header `/* GENERATED from site/design/presets/<name>.json on <date> — do not edit by hand */`; (2) `site/src/styles/fonts.css` — for each unique `source:"google"` family, one combined `@import url(https://fonts.googleapis.com/css2?...)` line (weights 400;600;700 + italics); for each `source:"self"` family, `@font-face` blocks pointing at `/ref_grammar/fonts/<family-slug>/<file>` (the `/ref_grammar` base prefix is required — public assets are served under it); `source:"system"` emits nothing. If a `self` family's folder is missing under `site/public/fonts/`, print a red warning listing the expected path and the font's OFL download source, and exit 1.
- [ ] **D4b. Self-host the winners.** When the author settles on a final preset: download its `google`-sourced families (Google Fonts "Download family", or google-webfonts-helper for woff2), place files in `site/public/fonts/<family-slug>/`, flip those roles to `source:"self"` in the preset, re-run the script. End state: `fonts.css` has no `@import`, the site makes zero external requests. (Until then, running with CDN fonts is fine — this step is deliberately last.)
- [ ] **D4c. Round-trip test.** `apply-design.mjs bookish.json` → build → site matches pre-plan look. Apply a second preset → build → site visibly restyled → re-apply bookish → back to baseline. Confirm `tokens.css` diffs are clean/deterministic (stable key order, so git diffs are readable).
- [ ] **D4d. Register.** Update `CLAUDE.md`'s `site/` bullet (one line: design tokens are generated from `site/design/presets/` via `apply-design.mjs`; sandbox at `tools/design-sandbox.html`) and `site/README.md` (replace the untouched Starlight starter README with a short real one: build commands, design-system pointer, this plan).

## 9. Milestone D5 — site-side features (gated on sandbox verdicts)

Each sub-item ships only after the author has seen it in the sandbox and kept its feature flag on in the applied preset. Order within D5 is free except D5e before D5f.

- [ ] **D5a. Heading system + measure.** CSS in `site-theme.css` applying the heading tokens to `.sl-markdown-content h2–h4` (weight, variant, tracking, rule, asymmetric spacing) and `--cl-measure` as `max-width` on the content column. Tokens only — no markup changes.
- [ ] **D5b. Status-tag badges.** `[Settled]` / `[Provisional]` / `[Open]` are plain text in the docs (load-bearing — do not alter the docs). Add a `findAndReplace` pattern in `remark-conlang.mjs` matching `\[(Settled|Provisional|Open)(?: — [^\]]*)?\]` → `<span class="cl-badge cl-badge--settled">…</span>` (keep the original bracket text as the span's content so copy-paste and no-CSS reading are unchanged). CSS: small caps, `--cl-badge-*` color, subtle pill. Feature-flag: emit spans always; the preset's `badges:false` simply styles them as plain text.
- [ ] **D5c. Example islands (plain form).** Until D5e lands, examples are blockquotes — but so are orientation abstracts. Do **not** style bare `blockquote` as an example island. Either wait for D5e (recommended) or have `stripExamples` wrap block renders in `<div class="cl-example">` (small change in `examples-render.mjs`; PDF unaffected — its own strip in `build.ps1` is separate; **verify** `pdf/build.ps1`'s strip regex tolerates nothing new leaking into previews — this change touches only the *site's* stripped output, not the on-disk previews).
- [ ] **D5d. Columned prose islands** ⚠ touches canonical docs — needs explicit author sign-off per stretch of text. Mechanism: `<!-- cols -->` … `<!-- /cols -->` HTML-comment pair in a doc (invisible in PDF and raw reading); `build-content.mjs` converts the pair to `<div class="cl-cols">` / `</div>` for the site. CSS from the cols tokens + narrow-screen collapse. Sequencing (decided 2026-07-03): candidate sections are chosen only *after* the author has judged the sandbox mock (D2g) and kept `colsIslands` on — then Claude nominates 2–3 dense stretches and the author approves each individually before any marker lands.
- [ ] **D5e. Rich interlinear renderer (the big one — implements 4a+4b for real).** In `examples-render.mjs`, add `renderExampleHtml(ex, spec)` producing the **exact D2c markup** from an `examples.json` record (aligned layers → `.cl-ex-chunk` columns; free layers → `.cl-ex-free` rows; consult `parse.mjs`/`examples.md` §2 for which is which; escape HTML; conlang line as `<em>`). In `build-content.mjs`, replace the site's `stripExamples(body)` call with a variant that, for **block-form** tokens, emits `renderExampleHtml` output instead of the markdown preview (inline dictionary-form tokens keep the markdown strip — they flow in prose). The on-disk previews, `sync-previews.mjs`, and the PDF path are untouched — this branches only what the *site* emits. Two integration cautions: (1) raw HTML blocks pass through remark untouched, so gloss tags in the leipzig line will NOT get hovercards from `remark-conlang.mjs` — have `renderExampleHtml` consult `glosses.json` itself and wrap known tags in the same `<a class="cl-ref cl-gloss" data-card-*>` shape the plugin emits; (2) `§EID` hovercards and the `<!-- example: -->` token pipeline must keep working — run the full `npm run check` after.
- [ ] **D5f. Hover polish.** Verify the pure-CSS chunk highlight reads well on the built site in both themes; add `:focus-within` for keyboard users. Only if the author wants cross-example or free-line coordination does a tiny JS file get added (inline it into `headJS` in `astro.config.mjs`, after `hovercard.js`). Closing this task **closes roadmap G1** — mark it done in `planning/examples-system-roadmap.md`.

## 10. Milestone D6 — figures (deferred, author-gated)

Reserved, not scheduled. When the author starts producing images: decide the asset home (`docs/assets/` so PDF and site both consume; site copies via `public/`), a `<!-- figure: -->` token or plain Markdown images, and caption styling from the reserved `--cl-figure-*` tokens. Do not start without author images in hand.

## 11. Overall acceptance

- [ ] Deploy green; site live at the Pages URL with hovers working (D0).
- [ ] `grep -R "sl-color\|#[0-9a-f]\{3,6\}" site/src/styles --include="*.css"` shows design literals only in `tokens.css`/`fonts.css` (bridge mappings excepted) (D1).
- [ ] Sandbox passes D2h; author has saved ≥1 config and re-loaded it in a later session (D2).
- [ ] All five presets apply cleanly via the script; a full sandbox-export → apply → build → deploy loop has been run once end-to-end (D3/D4).
- [ ] PDF pipeline verification after D5e: run `pdf/build.ps1` (or at minimum its strip step) and confirm output is unchanged — canonical docs and previews must be byte-identical to pre-plan except approved D5d markers.
- [ ] Light and dark themes both reviewed for every shipped feature.

## 12. Execution notes for the implementing model

- **Read-only zones:** never hand-edit `docs/` content (exception: D5d markers with author sign-off), `docs/quickref/` (generated), example previews (auto-regenerated by `sync-previews.mjs` — they will overwrite your edits), or `pdf/`. `tokens.css`/`fonts.css` are generated after D4 — change presets, not outputs.
- **Environment:** Windows 11; PowerShell primary. `python`/`python3` are broken Store stubs — irrelevant here (everything is Node). Node ≥22.12 required for `astro build` locally too — check `node --version` before diagnosing "mystery" build failures. `gh` CLI is not installed.
- **Build gotchas:** clear `site/node_modules/.astro` before builds when output looks stale. `npm run check` = content build + link check; run it after any change to scripts/plugins. Client scripts are inlined in `astro.config.mjs` `headJS` in load-bearing order: `diacritics.js` → `hovercard.js` → `search-diacritics.js`.
- **Base path:** every URL to a public asset (fonts!) needs the `/ref_grammar` prefix; every internal link goes through the `BASE` constants already in `build-content.mjs` / `remark-conlang.mjs`.
- **Versioning:** this plan touches no reference-doc content, so no doc version bumps — except D5b/D5d if the author wants the mechanism noted; ask. Update this file's checkboxes and the memory index as milestones land.
- **Style:** match the existing scripts' voice — plain Node ESM, no dependencies added without need, comments explain constraints not narration.

## 13. Open questions (author)

Resolved 2026-07-03 (decisions folded into the milestones above): ~~branch strategy~~ → merge to `main` (D0b); ~~columned-island trial sections~~ → defer until after the sandbox verdict, Claude nominates then (D5d); ~~Iosevka~~ → JetBrains Mono now, vendor Iosevka only if `concordance` is the finalist (D3b).

Still open:

1. After the sandbox round: which preset (or saved custom config) becomes the applied default? *(Unanswerable until D2/D3 exist — this is the decision the sandbox is built to inform. Revisit at D4c.)*
