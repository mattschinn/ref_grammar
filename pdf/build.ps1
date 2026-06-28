#requires -Version 5.1
<#
Build script for ref-grammar.pdf.

Pipeline:
  Markdown sources  ->  pandoc  ->  tectonic (XeLaTeX-class)  ->  ref-grammar.pdf

The five source files are merged in the order defined by `$inputs`. Each file's
top-level heading becomes a chapter (via --top-level-division=chapter).

Requirements:
  - pandoc on PATH (winget install JohnMacFarlane.Pandoc)
  - tectonic on PATH or in %LOCALAPPDATA%\Programs\Tectonic
  - assets/fonts/EBGaramond-{Regular,Italic,Bold,BoldItalic}.ttf
#>

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $root

# Ensure tool install dirs are on PATH for this session (User PATH changes
# don't always propagate to fresh shells).
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

# Canonical sources now live under ../docs (this script sits in pdf/).
$docsRoot = Join-Path $root '..\docs'
$sources = @(
    'reference\language_reference.md',
    'reference\phonology.md',
    'reference\orthography.md',
    'reference\verbal-system.md',
    'dictionary\dictionary.md'
)

foreach ($f in $sources) {
    if (-not (Test-Path (Join-Path $docsRoot $f))) { throw "Missing input: $f" }
}

# Pre-pass: copy sources to build_tmp/ and rewrite a small set of Unicode
# math operators to inline LaTeX math. The interchar font fallback covers
# IPA glyphs in body text but doesn't fire reliably inside longtable cells,
# which is where ∈ et al. show up. Routing them through pandoc's math
# parser sidesteps the problem entirely (amssymb provides the glyph).
$tmpDir = Join-Path $root 'build_tmp'
New-Item -ItemType Directory -Force -Path $tmpDir | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $root 'out') | Out-Null
$mathSubs = @{
    [char]0x2208 = '$\in$'        # element of
}

# Refresh the on-disk example previews from examples.md before reading the docs
# (roadmap G0b — auto-regenerate in build). The single renderer is the Node
# preview-sync step; this build only strips token+preview markers below. examples.md
# is source only and is never a chapter.
$syncScript = Join-Path $root '..\site\scripts\sync-previews.mjs'
if (Get-Command node -ErrorAction SilentlyContinue) {
    & node $syncScript
    if ($LASTEXITCODE -ne 0) { throw "sync-previews.mjs failed (exit $LASTEXITCODE)" }
} else {
    Write-Warning "node not found; example previews not refreshed (PDF may use stale previews). Run 'npm run content' in site/ first."
}

# Collapse `<!-- example: EID --> <!-- preview -->…<!-- /preview -->` to just the
# rendered preview content (what the PDF emits). The preview was rendered into the
# doc by the Node sync step above, so this side needs no renderer — only marker
# stripping. Fenced code is skipped so a documented token survives. Mirrors
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

$inputs = @()
foreach ($f in $sources) {
    $text = [IO.File]::ReadAllText((Join-Path $docsRoot $f), [Text.Encoding]::UTF8)
    foreach ($k in $mathSubs.Keys) {
        $text = $text.Replace([string]$k, $mathSubs[$k])
    }
    $base = Split-Path -Leaf $f
    $text = Strip-Examples $text
    $dst = Join-Path $tmpDir $base
    [IO.File]::WriteAllText($dst, $text, (New-Object Text.UTF8Encoding $false))
    $inputs += "build_tmp/$base"
}

$pandocArgs = @(
    '--pdf-engine=tectonic',
    '--toc',
    '--toc-depth=3',
    '--top-level-division=chapter',
    '-V', 'documentclass=book',
    '-V', 'classoption=oneside',
    '-V', 'fontsize=11pt',
    '-V', 'geometry:margin=1.1in',
    '-V', 'geometry:top=1.2in',
    '-V', 'geometry:bottom=1.2in',
    '-V', 'colorlinks=true',
    '-V', 'linkcolor=black',
    '-V', 'filecolor=black',
    '-V', 'citecolor=black',
    '-V', 'urlcolor=black!55',
    '--metadata', 'title=Reference Grammar',
    '-H', 'assets/preamble.tex',
    '-B', 'assets/titlepage.tex',
    '-o', 'out/ref-grammar.pdf'
)

Write-Host "Building ref-grammar.pdf..." -ForegroundColor Cyan
& pandoc @pandocArgs @inputs
if ($LASTEXITCODE -ne 0) { throw "pandoc exited with code $LASTEXITCODE" }

$out = Get-Item 'out/ref-grammar.pdf'
Write-Host ("Built: {0} ({1:N1} KB)" -f $out.FullName, ($out.Length / 1KB)) -ForegroundColor Green
