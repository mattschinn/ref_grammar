#requires -Version 5.1
<#
Experimental two-column build of dictionary.md only.

Output: dictionary.pdf

Differs from build.ps1:
  - Single source (dictionary.md), not the 5-doc set.
  - Article class with twocolumn classoption (vs. book + oneside).
  - Smaller fontsize, tighter geometry tuned for dense reference layout.
  - Pruned preamble at assets/preamble-dictionary.tex (no chapter formatting,
    no fancyhdr running headers, no custom titlepage — pandoc's \maketitle
    handles the title from metadata).
  - Same Brill / DejaVu Sans Mono fonts as the main build.
#>

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

# Reuse the main build's tool-discovery preamble.
$candidateDirs = @(
    "$env:LOCALAPPDATA\Programs\Tectonic",
    "$env:LOCALAPPDATA\Pandoc",
    "$env:ProgramFiles\Pandoc"
)
foreach ($d in $candidateDirs) {
    if ((Test-Path $d) -and ($env:Path -notlike "*$d*")) {
        $env:Path = "$env:Path;$d"
    }
}

foreach ($cmd in @('pandoc','tectonic')) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        throw "$cmd not found on PATH. See requirements at top of build.ps1."
    }
}

# Canonical dictionary now lives under ../docs/dictionary (this script sits in pdf/).
$dictSrc = Join-Path $root '..\docs\dictionary\dictionary.md'
if (-not (Test-Path $dictSrc)) { throw "Missing input: $dictSrc" }

# Math pre-pass (parallel to build.ps1's setup): rewrite U+2208 to inline math.
# Same defensive measure for longtable cell font-selection.
$tmpDir = Join-Path $root 'build_tmp'
New-Item -ItemType Directory -Force -Path $tmpDir | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $root 'out') | Out-Null
$mathSubs = @{
    [char]0x2208 = '$\in$'
}

# Refresh on-disk example previews from examples.md before reading the dictionary
# (roadmap G0b — auto-regenerate in build). The Node preview-sync step is the single
# renderer; this build only strips token+preview markers below.
$syncScript = Join-Path $root '..\site\scripts\sync-previews.mjs'
if (Get-Command node -ErrorAction SilentlyContinue) {
    & node $syncScript
    if ($LASTEXITCODE -ne 0) { throw "sync-previews.mjs failed (exit $LASTEXITCODE)" }
} else {
    Write-Warning "node not found; example previews not refreshed (PDF may use stale previews). Run 'npm run content' in site/ first."
}

# Collapse `<!-- example: EID --> <!-- preview -->…<!-- /preview -->` to just the
# rendered preview content. The preview was rendered into the doc by the Node sync
# step above, so this side needs no renderer — only marker stripping. Mirrors
# `site/scripts/examples-render.mjs` stripExamples.
function Strip-Examples([string]$text) {
    $pattern = '<!--\s*example:[^>]*-->[ \t]*\r?\n?<!--\s*preview\b[^>]*-->([\s\S]*?)<!--\s*/preview\s*-->'
    $lines = $text -split "`n", 0
    $result = New-Object System.Collections.Generic.List[string]
    $buf = New-Object System.Collections.Generic.List[string]
    $inFence = $false
    foreach ($line in $lines) {
        if ($line -match '^\s*```') {
            if ($buf.Count) { $result.Add([regex]::Replace([string]::Join("`n", $buf), $pattern, '$1')); $buf.Clear() }
            $result.Add($line); $inFence = -not $inFence; continue
        }
        if ($inFence) { $result.Add($line); continue }
        $buf.Add($line)
    }
    if ($buf.Count) { $result.Add([regex]::Replace([string]::Join("`n", $buf), $pattern, '$1')) }
    [string]::Join("`n", $result)
}

$text = [IO.File]::ReadAllText($dictSrc, [Text.Encoding]::UTF8)
foreach ($k in $mathSubs.Keys) {
    $text = $text.Replace([string]$k, $mathSubs[$k])
}
$text = Strip-Examples $text
$dst = Join-Path $tmpDir 'dictionary.md'
[IO.File]::WriteAllText($dst, $text, (New-Object Text.UTF8Encoding $false))

$pandocArgs = @(
    '--pdf-engine=tectonic',
    '--toc',
    '--toc-depth=2',
    '-V', 'documentclass=article',
    '-V', 'classoption=twocolumn',
    '-V', 'fontsize=10pt',
    '-V', 'geometry:margin=0.75in',
    '-V', 'geometry:top=0.85in',
    '-V', 'geometry:bottom=0.85in',
    '-V', 'colorlinks=true',
    '-V', 'linkcolor=black',
    '-V', 'filecolor=black',
    '-V', 'citecolor=black',
    '-V', 'urlcolor=black!55',
    '--metadata', 'title=Reference Grammar — Dictionary',
    '-H', 'assets/preamble-dictionary.tex',
    '-o', 'out/dictionary.pdf'
)

Write-Host "Building dictionary.pdf (two-column experiment)..." -ForegroundColor Cyan
& pandoc @pandocArgs 'build_tmp/dictionary.md'
if ($LASTEXITCODE -ne 0) { throw "pandoc exited with code $LASTEXITCODE" }

$out = Get-Item 'out/dictionary.pdf'
Write-Host ("Built: {0} ({1:N1} KB)" -f $out.FullName, ($out.Length / 1KB)) -ForegroundColor Green
