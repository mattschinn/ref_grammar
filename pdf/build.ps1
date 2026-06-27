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

# Parse examples.md into EID -> { conlang; etym; translation } so the
# `<!-- example: EID -->` transclusion tokens can be expanded in place (the PDF
# counterpart to the site compiler's expandExamples). examples.md is source only
# — never a chapter — so it is parsed here but absent from $sources.
$script:examples = @{}
$examplesPath = Join-Path $docsRoot 'reference\examples.md'
if (Test-Path $examplesPath) {
    $curId = $null
    foreach ($line in [IO.File]::ReadAllLines($examplesPath, [Text.Encoding]::UTF8)) {
        $h = [regex]::Match($line, '^###\s+(E\d{3})\b')
        if ($h.Success) { $curId = $h.Groups[1].Value; $script:examples[$curId] = @{ conlang=''; etym=''; translation='' }; continue }
        if (-not $curId) { continue }
        $m = [regex]::Match($line, '^- \*\*Conlang:\*\*\s*(.+?)\s*$');      if ($m.Success) { $script:examples[$curId].conlang = ($m.Groups[1].Value -replace '\s*\|\s*',' ').Trim(); continue }
        $m = [regex]::Match($line, '^- \*\*Etymological:\*\*\s*(.+?)\s*$'); if ($m.Success) { $script:examples[$curId].etym = ($m.Groups[1].Value -replace '\s*\|\s*',' ').Trim(); continue }
        $m = [regex]::Match($line, '^- \*\*Translation:\*\*\s*(.+?)\s*$');  if ($m.Success) { $script:examples[$curId].translation = $m.Groups[1].Value.Trim().Trim('"'); continue }
    }
}

# Expand `<!-- example: EID -->` in $text. dictionary.md host -> inline
# `*conlang* "translation"`; other hosts -> a simple stacked blockquote. (The
# deterministic monospace-aligned PDF gloss is roadmap G2.)
function Expand-Examples([string]$text, [bool]$isDict) {
    $script:exIsDict = $isDict
    [regex]::Replace($text, '<!--\s*example:\s*(E\d{3})\s*(?:\|\s*([A-Za-z]+)\s*)?-->', {
        param($mm)
        $eid = $mm.Groups[1].Value; $style = $mm.Groups[2].Value
        if (-not $script:examples.ContainsKey($eid)) { return "**[missing example $eid]**" }
        $ex = $script:examples[$eid]
        if ([string]::IsNullOrEmpty($style)) { $style = if ($script:exIsDict) { 'dictionary' } else { 'grammar' } }
        if ($style.ToLower() -eq 'dictionary') { return ('*{0}* "{1}"' -f $ex.conlang, $ex.translation) }
        return ("`n> *{0}*  `n> {1}  `n> ""{2}""`n" -f $ex.conlang, $ex.etym, $ex.translation)
    })
}

$inputs = @()
foreach ($f in $sources) {
    $text = [IO.File]::ReadAllText((Join-Path $docsRoot $f), [Text.Encoding]::UTF8)
    foreach ($k in $mathSubs.Keys) {
        $text = $text.Replace([string]$k, $mathSubs[$k])
    }
    $base = Split-Path -Leaf $f
    $text = Expand-Examples $text ($base -eq 'dictionary.md')
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
