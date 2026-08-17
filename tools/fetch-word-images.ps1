# fetch-word-images.ps1 — pull one CC-licensed photo per dictionary word from the
# Openverse API (openverse.org), center-crop/resize to a 900px square JPEG under
# site/public/img/words/, and record attribution in site/src/data/word-images.json.
#
#   powershell -File tools/fetch-word-images.ps1
#
# Idempotent: words already present in the manifest are skipped, so extending
# tools/word-image-queries.json and rerunning only fetches the new ones.
# Only cc0 / pdm / by / by-sa images are requested (no NC, no ND — cropping is a
# derivative). The explore UI shows the credit; keep the manifest committed.

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$repo = Split-Path -Parent $PSScriptRoot
$queriesPath = Join-Path $PSScriptRoot 'word-image-queries.json'
$manifestPath = Join-Path $repo 'site\src\data\word-images.json'
$imgDir = Join-Path $repo 'site\public\img\words'
$SIZE = 900

New-Item -ItemType Directory -Force $imgDir | Out-Null
New-Item -ItemType Directory -Force (Split-Path -Parent $manifestPath) | Out-Null

$queries = [IO.File]::ReadAllText($queriesPath, [Text.Encoding]::UTF8) | ConvertFrom-Json
$manifest = @{}
if (Test-Path $manifestPath) {
    $existing = [IO.File]::ReadAllText($manifestPath, [Text.Encoding]::UTF8) | ConvertFrom-Json
    foreach ($p in $existing.PSObject.Properties) { $manifest[$p.Name] = $p.Value }
}

function Save-CroppedSquare([string]$srcPath, [string]$outPath, [int]$size) {
    $img = [System.Drawing.Image]::FromFile($srcPath)
    try {
        $side = [Math]::Min($img.Width, $img.Height)
        $srcX = [int](($img.Width - $side) / 2)
        $srcY = [int](($img.Height - $side) / 2)
        $bmp = New-Object System.Drawing.Bitmap($size, $size)
        $g = [System.Drawing.Graphics]::FromImage($bmp)
        $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $g.DrawImage($img,
            (New-Object System.Drawing.Rectangle(0, 0, $size, $size)),
            (New-Object System.Drawing.Rectangle($srcX, $srcY, $side, $side)),
            [System.Drawing.GraphicsUnit]::Pixel)
        $g.Dispose()
        $jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() |
            Where-Object { $_.MimeType -eq 'image/jpeg' }
        $encParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
        $encParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter(
            [System.Drawing.Imaging.Encoder]::Quality, [long]82)
        $bmp.Save($outPath, $jpegCodec, $encParams)
        $bmp.Dispose()
    } finally { $img.Dispose() }
}

$LICENSE_NAME = @{ 'cc0' = 'CC0'; 'pdm' = 'Public Domain Mark'; 'by' = 'CC BY'; 'by-sa' = 'CC BY-SA' }
$fetched = 0; $skipped = 0; $failed = @()

foreach ($p in $queries.PSObject.Properties) {
    $head = $p.Name
    if ($head -eq '_comment') { continue }
    if ($manifest.ContainsKey($head)) { $skipped++; continue }
    $spec = $p.Value
    $q = [uri]::EscapeDataString($spec.q)
    $api = "https://api.openverse.org/v1/images/?q=$q&license=cc0,pdm,by,by-sa&page_size=8"
    Write-Host "[$head] searching: $($spec.q)"
    try {
        $res = Invoke-RestMethod -Uri $api -TimeoutSec 30 -UserAgent 'ref-grammar-site/1.0 (word picture fetch)'
    } catch {
        Write-Warning "  search failed: $($_.Exception.Message)"; $failed += $head
        Start-Sleep -Seconds 4; continue
    }
    $got = $false
    foreach ($r in $res.results) {
        if ($r.mature) { continue }
        if ($r.width -lt 640 -or $r.height -lt 480) { continue }
        $tmp = Join-Path $env:TEMP ("ov-" + $spec.file + [IO.Path]::GetExtension(($r.url -split '\?')[0]))
        try {
            Invoke-WebRequest -Uri $r.url -OutFile $tmp -TimeoutSec 60 -UserAgent 'ref-grammar-site/1.0 (word picture fetch)'
            $out = Join-Path $imgDir ($spec.file + '.jpg')
            Save-CroppedSquare $tmp $out $SIZE
            $lic = $LICENSE_NAME[[string]$r.license]
            if (-not $lic) { $lic = 'CC ' + ([string]$r.license).ToUpper() }
            $manifest[$head] = [ordered]@{
                file       = 'img/words/' + $spec.file + '.jpg'
                title      = [string]$r.title
                creator    = [string]$r.creator
                creatorUrl = [string]$r.creator_url
                license    = $lic + ' ' + [string]$r.license_version
                licenseUrl = [string]$r.license_url
                source     = [string]$r.foreign_landing_url
                provider   = [string]$r.provider
            }
            Write-Host "  ok: $($r.title) by $($r.creator) [$lic]"
            $got = $true; $fetched++
            break
        } catch {
            Write-Warning "  candidate failed, trying next: $($_.Exception.Message)"
        } finally {
            if (Test-Path $tmp) { Remove-Item $tmp -Force -Confirm:$false }
        }
    }
    if (-not $got) { $failed += $head }
    Start-Sleep -Seconds 4   # stay under Openverse's anonymous rate limit
}

# write manifest sorted by headword, UTF-8 no BOM
$sorted = [ordered]@{}
foreach ($k in ($manifest.Keys | Sort-Object)) { $sorted[$k] = $manifest[$k] }
$json = ($sorted | ConvertTo-Json -Depth 4)
[IO.File]::WriteAllText($manifestPath, $json + "`n", (New-Object Text.UTF8Encoding($false)))

Write-Host "`nfetched $fetched, skipped $skipped (already in manifest), failed $($failed.Count)"
if ($failed.Count) { Write-Host ('failed: ' + ($failed -join ', ')) }
