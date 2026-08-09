# ==============================================================================
# Bug Bounty & Security Skills Collection Installer (PowerShell for Windows)
# ==============================================================================

param (
    [string]$Profile = "all"
)

$ErrorActionPreference = "Stop"

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "  🚀 Bug Bounty Agent Skills Installer (100 Skills Collection)" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

$TargetDir = ""

# Detect environment
$ClaudeDir = Join-Path $HOME ".claude\skills"
$AgentsDir = ".agents\skills"

if (Test-Path $ClaudeDir) {
    $TargetDir = $ClaudeDir
    Write-Host "[*] Detected Claude Code environment at: $TargetDir" -ForegroundColor Yellow
} elseif (Test-Path ".agents") {
    $TargetDir = $AgentsDir
    Write-Host "[*] Detected OpenCode environment at: $TargetDir" -ForegroundColor Yellow
} else {
    $TargetDir = Join-Path $HOME ".agents\skills"
    Write-Host "[*] Defaulting to OpenCode skills directory at: $TargetDir" -ForegroundColor Yellow
}

if (-not (Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
}

Write-Host "[*] Selected Installation Profile: '$Profile'" -ForegroundColor Green

switch ($Profile.ToLower()) {
    { $_ -in "recon", "recon-osint" } {
        Write-Host "[*] Installing Recon & OSINT Profile..." -ForegroundColor Green
        Copy-Item -Path "skills\bug-bounty-recon*" -Destination $TargetDir -Recurse -Force -ErrorAction SilentlyContinue
        Copy-Item -Path "skills\bug-bounty-osint*" -Destination $TargetDir -Recurse -Force -ErrorAction SilentlyContinue
        Copy-Item -Path "skills\bug-bounty-subdomain*" -Destination $TargetDir -Recurse -Force -ErrorAction SilentlyContinue
        Copy-Item -Path "skills\bug-bounty-spiderfoot*" -Destination $TargetDir -Recurse -Force -ErrorAction SilentlyContinue
        Copy-Item -Path "skills\bug-bounty-amass*" -Destination $TargetDir -Recurse -Force -ErrorAction SilentlyContinue
    }
    { $_ -in "web", "web-api" } {
        Write-Host "[*] Installing Web & API Audit Profile..." -ForegroundColor Green
        Copy-Item -Path "skills\bug-bounty-xss*" -Destination $TargetDir -Recurse -Force -ErrorAction SilentlyContinue
        Copy-Item -Path "skills\bug-bounty-sqli*" -Destination $TargetDir -Recurse -Force -ErrorAction SilentlyContinue
        Copy-Item -Path "skills\bug-bounty-ssrf*" -Destination $TargetDir -Recurse -Force -ErrorAction SilentlyContinue
        Copy-Item -Path "skills\bug-bounty-idor*" -Destination $TargetDir -Recurse -Force -ErrorAction SilentlyContinue
        Copy-Item -Path "skills\bug-bounty-jwt*" -Destination $TargetDir -Recurse -Force -ErrorAction SilentlyContinue
        Copy-Item -Path "skills\bug-bounty-js*" -Destination $TargetDir -Recurse -Force -ErrorAction SilentlyContinue
    }
    Default {
        Write-Host "[*] Installing Full Master Collection (100 Skills)..." -ForegroundColor Green
        Copy-Item -Path "skills\*" -Destination $TargetDir -Recurse -Force
    }
}

Write-Host ""
Write-Host "✅ Installation completed successfully!" -ForegroundColor Green
Write-Host "📍 Installed Skills Location: $TargetDir" -ForegroundColor Cyan
Write-Host "💡 Restart your AI Agent (OpenCode / Claude Code / Antigravity) to load the skills." -ForegroundColor Yellow
