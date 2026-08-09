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
}

def main():
    print("==================================================================")
    print("  🤖 Bug Bounty Agent Skills Workflow Orchestrator")
    print("==================================================================")
    print("Select current Pentesting Phase:\n")
    for key, (name, path) in PROFILES.items():
        print(f"  [{key}] {name} ({path})")
    
    print("  [6] Generate Vulnerability Report (templates/)")
    print("  [0] Exit\n")
    
    choice = input("Enter option [1-6]: ").strip()
    
    if choice in PROFILES:
        name, path = PROFILES[choice]
        print(f"\n[*] Activating Profile: '{name}'")
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"✅ Loaded {len(data.get('entries', []))} Skills.")
            print(f"🛠️ Suggested Tools to execute: {', '.join(data.get('tools', []))}")
        else:
            print(f"❌ Error: Profile manifest not found at '{path}'")
    elif choice == "6":
        print("\n[*] Available Report Templates:")
        print("  - templates/hackerone-report-template.md")
        print("  - templates/bugcrowd-report-template.md")
        print("  - templates/cvss-v31-calculator.md")
    else:
        print("Exiting orchestrator.")

if __name__ == "__main__":
    main()
