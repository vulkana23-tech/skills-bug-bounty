<#
.SYNOPSIS
    Engagement Workspace Scaffolding PowerShell Script
    Bootstraps structured directory scaffolding for bug bounty engagements.
#>

param (
    [Parameter(Mandatory=$true)]
    [string]$Target,

    [string]$BaseDir = ".",

    [switch]$DryRun
)

$TargetName = $Target -replace "[:/]", "_"
$WorkDir = Join-Path $BaseDir "engagement-$TargetName"

Write-Host "[+] Initializing engagement directory: $WorkDir"

if ($DryRun) {
    Write-Host "[*] Dry run mode enabled. No directories or files created."
    exit 0
}

New-Item -ItemType Directory -Path $WorkDir -Force | Out-Null
foreach ($folder in @("scans", "evidence", "poc")) {
    New-Item -ItemType Directory -Path (Join-Path $WorkDir $folder) -Force | Out-Null
}

$ScopeContent = @"
# 🛡️ Engagement Scope Contract & Authorization

## In-Scope Targets
- Target Domain/API: $Target

## Out-of-Scope Rules
- DoS / DDoS attacks
- Destructive actions or data modification
"@

$NotesContent = @"
# 📝 Engagement Notes - $Target

## 🎯 Test Matrix
- [ ] Subdomain Reconnaissance & Service Discovery
- [ ] Access Control & IDOR Testing
- [ ] Input Validation & Injection Testing
- [ ] Authentication & Session Security

## 📑 Findings Log
"@

$ReportContent = @"
# 📑 Security Assessment Report - $Target

## 🎯 Executive Summary

## 📌 Findings Table
| ID | Severity | Title | Status |
|---|---|---|---|

## 🔍 Detailed Vulnerability PoCs
"@

Set-Content -Path (Join-Path $WorkDir "scope.md") -Value $ScopeContent -Encoding UTF8
Set-Content -Path (Join-Path $WorkDir "notes.md") -Value $NotesContent -Encoding UTF8
Set-Content -Path (Join-Path $WorkDir "report.md") -Value $ReportContent -Encoding UTF8

Write-Host "[✓] Engagement workspace scaffolded successfully at: $WorkDir"
