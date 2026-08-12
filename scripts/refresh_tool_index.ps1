<#
.SYNOPSIS
    Tool Index Bootstrapper PowerShell Script
    Scans system PATH for installed security & reversing tools and writes tools-index.json.
#>

$Tools = @(
    "jadx", "apktool", "frida", "objection", "ghidra", "radare2", "r2",
    "gdb", "checksec", "binwalk", "node", "python", "nmap", "nuclei",
    "subfinder", "ffuf", "httpx", "amass", "sqlmap"
)

$Result = @{
    timestamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    system = "win32"
    installed_count = 0
    tools = @{}
}

foreach ($tool in $Tools) {
    $command = Get-Command $tool -ErrorAction SilentlyContinue
    if ($command) {
        $Result.installed_count++
        $Result.tools[$tool] = @{
            installed = $true
            path = $command.Source
        }
    } else {
        $Result.tools[$tool] = @{
            installed = $false
            path = $null
        }
    }
}

$OutputPath = Join-Path (Get-Item $PSScriptRoot).Parent.FullName "tools-index.json"
$Result | ConvertTo-Json -Depth 4 | Set-Content -Path $OutputPath -Encoding UTF8

Write-Host "[+] Scanned $($Tools.Count) tools. Found $($Result.installed_count) installed tools."
Write-Host "[+] Tool index updated at: $OutputPath"
