#!/usr/bin/env python3
"""
==============================================================================
Bug Bounty Agent Skills Workflow Orchestrator
==============================================================================
"""

import sys
import json
import os

PROFILES = {
    "1": ("Recon & OSINT", "profiles/profile-recon-osint.json"),
    "2": ("Web & API Audit", "profiles/profile-web-api-audit.json"),
    "3": ("Cloud & DevOps", "profiles/profile-cloud-devops.json"),
    "4": ("Advanced Exploitation", "profiles/profile-advanced-exploitation.json"),
    "5": ("Mobile, IoT & Binary", "profiles/profile-mobile-iot-binary.json"),
    "6": ("Wild Exploits (CISA KEV Feed)", "profiles/wild-exploits.json")
}

def main():
    print("==================================================================")
    print("  🤖 Bug Bounty Agent Skills Workflow Orchestrator")
    print("==================================================================")
    print("Select current Pentesting Phase or Dynamic Feed:\n")
    for key, (name, path) in PROFILES.items():
        print(f"  [{key}] {name} ({path})")
    
    print("  [7] Few-Shot Learning Case Studies (knowledge/writeups/)")
    print("  [8] Generate Vulnerability Report (templates/)")
    print("  [0] Exit\n")
    
    choice = input("Enter option [1-8]: ").strip()
    
    if choice in PROFILES:
        name, path = PROFILES[choice]
        print(f"\n[*] Activating Profile: '{name}'")
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"✅ Loaded Skills / Exploits Manifest.")
            if "tools" in data:
                print(f"🛠️ Suggested Tools to execute: {', '.join(data.get('tools', []))}")
            if "exploits" in data:
                print(f"🔥 Actively Exploited CVEs Tracked: {len(data['exploits'])}")
        else:
            print(f"❌ Error: Profile manifest not found at '{path}'")
    elif choice == "7":
        print("\n[*] Real-World Write-ups & Few-Shot Studies:")
        print("  - knowledge/writeups/uber-oauth-account-takeover-chain.md")
        print("  - knowledge/writeups/shopify-graphql-idor-bfla.md")
        print("  - knowledge/writeups/aws-imdsv2-ssrf-cloud-pivot.md")
    elif choice == "8":
        print("\n[*] Available Report Templates:")
        print("  - templates/hackerone-report-template.md")
        print("  - templates/bugcrowd-report-template.md")
        print("  - templates/cvss-v31-calculator.md")
    else:
        print("Exiting orchestrator.")

if __name__ == "__main__":
    main()
