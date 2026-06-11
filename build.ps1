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

$sources = @(
    'language_reference.md',
    'phonology.md',
    'orthography.md',
    'verbal-system.md',
    'dictionary.md'
)

foreach ($f in $sources) {
    if (-not (Test-Path $f)) { throw "Missing input: $f" }
}

# Pre-pass: copy sources to build_tmp/ and rewrite a small set of Unicode
# math operators to inline LaTeX math. The interchar font fallback covers
# IPA glyphs in body text but doesn't fire reliably inside longtable cells,
# which is where ∈ et al. show up. Routing them through pandoc's math
# parser sidesteps the problem entirely (amssymb provides the glyph).
$tmpDir = Join-Path $root 'build_tmp'
New-Item -ItemType Directory -Force -Path $tmpDir | Out-Null
$mathSubs = @{
    [char]0x2208 = '$\in$'        # element of
}
$inputs = @()
foreach ($f in $sources) {
    $text = [IO.File]::ReadAllText((Join-Path $root $f), [Text.Encoding]::UTF8)
    foreach ($k in $mathSubs.Keys) {
        $text = $text.Replace([string]$k, $mathSubs[$k])
    }
    $dst = Join-Path $tmpDir $f
    [IO.File]::WriteAllText($dst, $text, (New-Object Text.UTF8Encoding $false))
    $inputs += "build_tmp/$f"
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
    '-o', 'ref-grammar.pdf'
)

Write-Host "Building ref-grammar.pdf..." -ForegroundColor Cyan
& pandoc @pandocArgs @inputs
if ($LASTEXITCODE -ne 0) { throw "pandoc exited with code $LASTEXITCODE" }

$out = Get-Item 'ref-grammar.pdf'
Write-Host ("Built: {0} ({1:N1} KB)" -f $out.FullName, ($out.Length / 1KB)) -ForegroundColor Green
