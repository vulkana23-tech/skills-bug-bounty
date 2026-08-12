#!/usr/bin/env python3
"""
Tool Index Bootstrapper Script
Scans system PATH for installed cybersecurity and reverse engineering tools,
generating a machine-readable tools-index.json manifest.
"""

import json
import shutil
import os
import sys
from datetime import datetime

TARGET_TOOLS = [
    "jadx",
    "apktool",
    "frida",
    "objection",
    "ghidra",
    "radare2",
    "r2",
    "gdb",
    "checksec",
    "binwalk",
    "node",
    "python",
    "nmap",
    "nuclei",
    "subfinder",
    "ffuf",
    "httpx",
    "amass",
    "sqlmap"
]

def scan_tools():
    index = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "system": sys.platform,
        "installed_count": 0,
        "tools": {}
    }

    for tool in TARGET_TOOLS:
        path = shutil.which(tool)
        is_installed = path is not None
        if is_installed:
            index["installed_count"] += 1
        index["tools"][tool] = {
            "installed": is_installed,
            "path": path if path else None
        }

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools-index.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    print(f"[+] Scanned {len(TARGET_TOOLS)} tools. Found {index['installed_count']} installed tools.")
    print(f"[+] Tool index updated at: {output_path}")

if __name__ == "__main__":
    scan_tools()
