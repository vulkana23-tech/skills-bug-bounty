#!/usr/bin/env python3
"""
==============================================================================
CISA Known Exploited Vulnerabilities (KEV) Catalog Fetcher & Profile Generator
==============================================================================
"""

import json
import urllib.request
import os

CISA_KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
OUTPUT_PROFILE = "profiles/wild-exploits.json"

def fetch_cisa_kev():
    print(f"[*] Fetching CISA KEV feed from: {CISA_KEV_URL}...")
    req = urllib.request.Request(CISA_KEV_URL, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            vulnerabilities = data.get('vulnerabilities', [])
            print(f"[+] Total CISA KEV entries fetched: {len(vulnerabilities)}")
            
            # Select top 50 most recent actively exploited CVEs
            recent_cves = vulnerabilities[:50]
            
            cve_list = []
            for item in recent_cves:
                cve_list.append({
                    "cveID": item.get("cveID"),
                    "vendorProject": item.get("vendorProject"),
                    "product": item.get("product"),
                    "vulnerabilityName": item.get("vulnerabilityName"),
                    "dateAdded": item.get("dateAdded"),
                    "shortDescription": item.get("shortDescription")
                })
            
            profile_data = {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "name": "bug-bounty-skills-wild-exploits",
                "version": "1.0.0",
                "description": "Dynamic Profile: CISA Known Exploited Vulnerabilities (Actively Exploited in the Wild)",
                "total_cves_tracked": len(cve_list),
                "tools": ["nuclei", "nmap", "httpx"],
                "exploits": cve_list,
                "entries": [
                    { "path": "../skills/bug-bounty-cve-exploits" },
                    { "path": "../skills/bug-bounty-cve-fast-scanning" },
                    { "path": "../skills/bug-bounty-misconfig-detection" }
                ]
            }
            
            os.makedirs(os.path.dirname(OUTPUT_PROFILE), exist_ok=True)
            with open(OUTPUT_PROFILE, 'w', encoding='utf-8') as f:
                json.dump(profile_data, f, indent=2)
                
            print(f"✅ Generated active profile at: '{OUTPUT_PROFILE}' with {len(cve_list)} high-priority CVEs.")
            
    except Exception as e:
        print(f"❌ Failed to fetch CISA KEV feed: {e}")

if __name__ == "__main__":
    fetch_cisa_kev()
