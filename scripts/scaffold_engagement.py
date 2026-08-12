#!/usr/bin/env python3
"""
Engagement Workspace Scaffolding CLI Script
Bootstraps structured directory scaffolding for bug bounty engagements.
"""

import os
import sys
import argparse

DEFAULT_DIRS = ["scans", "evidence", "poc"]

SCOPE_TEMPLATE = """# 🛡️ Engagement Scope Contract & Authorization

## In-Scope Targets
- Target Domain/API: `{target}`

## Out-of-Scope Rules
- DoS / DDoS attacks
- Destructive actions or data modification
"""

NOTES_TEMPLATE = """# 📝 Engagement Notes - {target}

## 🎯 Test Matrix
- [ ] Subdomain Reconnaissance & Service Discovery
- [ ] Access Control & IDOR Testing
- [ ] Input Validation & Injection Testing
- [ ] Authentication & Session Security

## 📑 Findings Log
"""

REPORT_TEMPLATE = """# 📑 Security Assessment Report - {target}

## 🎯 Executive Summary

## 📌 Findings Table
| ID | Severity | Title | Status |
|---|---|---|---|

## 🔍 Detailed Vulnerability PoCs
"""

def scaffold(target, base_dir=".", dry_run=False):
    target_name = target.replace("/", "_").replace(":", "_")
    workdir = os.path.join(base_dir, f"engagement-{target_name}")

    print(f"[+] Initializing engagement directory: {workdir}")
    if dry_run:
        print("[*] Dry run mode enabled. No directories or files created.")
        return

    os.makedirs(workdir, exist_ok=True)
    for folder in DEFAULT_DIRS:
        os.makedirs(os.path.join(workdir, folder), exist_ok=True)

    with open(os.path.join(workdir, "scope.md"), "w", encoding="utf-8") as f:
        f.write(SCOPE_TEMPLATE.format(target=target))

    with open(os.path.join(workdir, "notes.md"), "w", encoding="utf-8") as f:
        f.write(NOTES_TEMPLATE.format(target=target))

    with open(os.path.join(workdir, "report.md"), "w", encoding="utf-8") as f:
        f.write(REPORT_TEMPLATE.format(target=target))

    print(f"[✓] Engagement workspace scaffolded successfully at: {workdir}")

def main():
    parser = argparse.ArgumentParser(description="Scaffold Bug Bounty Engagement Workdir")
    parser.add_argument("--target", required=True, help="Target name or domain (e.g. targetapp.com)")
    parser.add_argument("--dir", default=".", help="Base output directory")
    parser.add_argument("--dry-run", action="store_true", help="Simulate creation without writing files")

    args = parser.parse_args()
    scaffold(args.target, args.dir, args.dry_run)

if __name__ == "__main__":
    main()
