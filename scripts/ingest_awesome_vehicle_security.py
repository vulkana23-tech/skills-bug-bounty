#!/usr/bin/env python3
"""
Ingest jaredthecoder/awesome-vehicle-security into RAG-ready vector store chunks.

Outputs (under rag/awesome-vehicle-security/):
  chunks.jsonl              -> one chunk per line
  chunks/<domain>.json      -> domain-specific JSON arrays
  knowledge-base/<domain>.md -> consolidated markdown documents
  manifest.json             -> schema, statistics, tags
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_URL = "https://github.com/jaredthecoder/awesome-vehicle-security"
ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "rag" / "awesome-vehicle-security"

TAG_KEYWORDS = {
    "can-bus": ["can bus", "can-bus", "socketcan", "canopen", "can messages", "controller area network", "canutils", "can-utils"],
    "obd-ii": ["obd-ii", "obd2", "obd ii", "elm327", "telematics", "dtc"],
    "ecu": ["ecu", "electronic control unit", "engine control", "seed-key", "reflash", "firmware"],
    "uds-diagnostics": ["uds", "unified diagnostic services", "diagnostic", "iso 14229", "iso 15765"],
    "j1939-heavy-duty": ["j1939", "fms", "heavy vehicle", "truck"],
    "automotive-protocols": ["flexray", "lin ", "lin-bus", "most ", "automotive ethernet", "broadr-reach", "doip"],
    "sdr-wireless": ["sdr", "software defined radio", "hackrf", "sub-1 ghz", "433mhz", "315mhz", "key fob", "rfid", "pandwarf", "tpms"],
    "v2x-connected": ["v2x", "v2v", "v2i", "v2g", "geonetworking", "etsi its", "charging", "evcc"],
    "adas-autonomous": ["adas", "openpilot", "autonomous", "self driving", "radar", "lidar", "vision"],
    "infotainment-ivi": ["infotainment", "ivi", "mzd", "head unit", "cmu", "telematics kit", "android auto", "carplay"],
    "hardware-tools": ["chipwhisperer", "red pitaya", "canbadger", "canspy", "cantact", "carloop", "usb2can", "macchina", "arduino"],
    "fuzzing-injection": ["injection", "fuzzing", "mitm", "spoofing", "replay", "canalyzat0r", "caring caribou"],
    "reverse-engineering": ["reverse engineering", "reversing", "disassembly", "dbc file", "dbc", "deserialize"],
    "electric-vehicles": ["electric vehicle", "ev ", "charging", "obc", "v2gevil", "battery management", "bms", "tesla"],
    "standards-frameworks": ["iso 26262", "iso 21434", "asrg", "sae", "cyber safety", "coordinated disclosure", "i am the cavalry"],
    "defcon-village": ["car hacking village", "chv", "rootcon", "defcon", "def con"],
}

TAG_PATTERNS = {
    t: re.compile(r"\b(?:" + "|".join(re.escape(k.strip()) for k in kws) + r")\b", re.IGNORECASE)
    for t, kws in TAG_KEYWORDS.items()
}

DOMAIN_MAPPING = {
    "Articles": "Research & Learning",
    "Presentations": "Research & Learning",
    "Books": "Research & Learning",
    "Research Papers": "Research & Learning",
    "Courses": "Research & Learning",
    "Blogs": "Research & Learning",
    "Websites": "Community & Ecosystem",
    "Newsletters": "Community & Ecosystem",
    "Conferences": "Community & Ecosystem",
    "Who to Follow": "Community & Ecosystem",
    "Podcasts and Episodes": "Community & Ecosystem",
    "Podcasts": "Community & Ecosystem",
    "Episodes": "Community & Ecosystem",
    "Miscellaneous": "Research & Learning",
    "Projects": "Automotive Software & Projects",
    "Hardware": "Hardware & Interfacing",
    "Software": "Automotive Software & Projects",
    "Applications": "Automotive Software & Projects",
    "Libraries and Tools": "Libraries & Exploitation Tools",
    "C": "Libraries & Exploitation Tools",
    "C++": "Libraries & Exploitation Tools",
    "Java": "Libraries & Exploitation Tools",
    "Python": "Libraries & Exploitation Tools",
    "Go": "Libraries & Exploitation Tools",
    "JavaScript": "Libraries & Exploitation Tools",
    "Companies and Jobs": "Industry & Coordinated Disclosure",
    "Coordinated disclosure": "Industry & Coordinated Disclosure",
}

LOCAL_SKILLS_FOR_DOMAIN = {
    "Research & Learning": ["bug-bounty-recon", "bug-bounty-methodology-playbook"],
    "Hardware & Interfacing": ["bug-bounty-iot-device-auditing", "bug-bounty-firmware-iot-routing"],
    "Automotive Software & Projects": ["bug-bounty-reverse-engineering", "bug-bounty-port-service-discovery"],
    "Libraries & Exploitation Tools": ["bug-bounty-reverse-engineering", "bug-bounty-automation-scripts"],
    "Community & Ecosystem": ["bug-bounty-osint-threat-intel"],
    "Industry & Coordinated Disclosure": ["bug-bounty-vulnerability-disclosure"],
}

MD_HEADER = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return s or "root"


def tag_text(text: str, domain: str) -> list[str]:
    low = text.lower()
    tags = {t for t, rx in TAG_PATTERNS.items() if rx.search(low)}
    tags.add("automotive-security")
    tags.add(slugify(domain))
    return sorted(tags)


def split_sections_md(text: str):
    stack: list[tuple[int, str]] = []
    buf: list[str] = []

    def path():
        return [h for _, h in stack]

    current_path: list[str] = []
    for line in text.splitlines():
        m = MD_HEADER.match(line)
        if m:
            if "\n".join(buf).strip():
                yield current_path, "\n".join(buf).strip()
            buf = []
            level, title = len(m.group(1)), re.sub(r"[*_`\[\]]|!\[.*?\]\(.*?\)", "", m.group(2)).strip()
            # Clean trailing badge markdown from title if any
            title = re.sub(r"\(http.*?\)", "", title).strip()
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, title))
            current_path = path()
        else:
            buf.append(line)
    if "\n".join(buf).strip():
        yield current_path, "\n".join(buf).strip()


def pack_list_items(body: str, max_chars: int = 1500) -> list[str]:
    """Group markdown list items into coherent chunks without splitting individual entries."""
    lines = body.splitlines()
    items = []
    cur_item = []

    for line in lines:
        if re.match(r"^\s*[-*+]\s+", line) or re.match(r"^\s*\d+\.\s+", line):
            if cur_item:
                items.append("\n".join(cur_item))
                cur_item = []
        cur_item.append(line)
    if cur_item:
        items.append("\n".join(cur_item))

    if not items:
        # Paragraph fallback
        return [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]

    chunks = []
    acc = []
    acc_len = 0

    for it in items:
        it_clean = it.strip()
        if not it_clean:
            continue
        if acc_len + len(it_clean) + 2 > max_chars and acc:
            chunks.append("\n\n".join(acc))
            acc = []
            acc_len = 0
        acc.append(it_clean)
        acc_len += len(it_clean) + 2

    if acc:
        chunks.append("\n\n".join(acc))
    return chunks


def make_chunk(*, content, rel_path, domain, heading, idx=0):
    heading_str = " > ".join(heading) if heading else "Overview"
    raw_id = f"avs|{rel_path}|{heading_str}|{idx}|{content[:60]}"
    cid = "avs-" + hashlib.sha1(raw_id.encode("utf-8")).hexdigest()[:16]
    title = heading[-1] if heading else Path(rel_path).stem
    context_line = f"[Vehicle Security: {domain}] {heading_str}"
    
    return {
        "id": cid,
        "domain": domain,
        "skills": LOCAL_SKILLS_FOR_DOMAIN.get(domain, []),
        "tags": tag_text(content + " " + heading_str, domain),
        "content": f"{context_line}\n\n{content}",
        "metadata": {
            "source_repo": REPO_URL,
            "source_path": rel_path,
            "source_url": f"{REPO_URL}/blob/master/{rel_path}".replace(" ", "%20"),
            "document_title": title,
            "heading_path": heading,
            "doc_type": "markdown",
            "license": "CC0-1.0 (Public Domain / Awesome List)",
            "char_count": len(content),
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", type=Path)
    ap.add_argument("--max-chars", type=int, default=1500)
    args = ap.parse_args()
    repo = args.repo.resolve()

    readme_path = repo / "README.md"
    if not readme_path.exists():
        sys.exit(f"[!] README.md not found at {repo}")

    text = readme_path.read_text(encoding="utf-8", errors="ignore")
    # Clean images and trailing junk
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)

    chunks = []
    stats = {"total_items_processed": 0, "sections": 0}

    for heading, body in split_sections_md(text):
        if not heading:
            continue
        top_heading = heading[0] if len(heading) > 0 else ""
        sub_heading = heading[-1] if len(heading) > 1 else top_heading

        # Skip Table of Contents, intro and meta sections
        if any(h.lower() in ("contents", "related lists", "other awesome lists", "contributing", "awesome vehicle security") for h in heading):
            continue
        if len(heading) == 1 and heading[0].lower() == "awesome vehicle security":
            continue

        domain = DOMAIN_MAPPING.get(sub_heading) or DOMAIN_MAPPING.get(top_heading) or "Automotive Security General"
        items = pack_list_items(body, max_chars=args.max_chars)
        stats["sections"] += 1

        for idx, piece in enumerate(items):
            piece_clean = piece.strip()
            if len(piece_clean) < 30:
                continue
            if re.search(r"^\s*\[Welcoming contributions\]", piece_clean, re.IGNORECASE):
                continue
            chunk = make_chunk(
                content=piece_clean,
                rel_path="README.md",
                domain=domain,
                heading=heading,
                idx=idx,
            )
            chunks.append(chunk)

    print(f"[+] Processed {len(chunks)} chunks across {stats['sections']} sections.")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "chunks").mkdir(exist_ok=True)
    (OUT_DIR / "knowledge-base").mkdir(exist_ok=True)

    # 1. chunks.jsonl
    with (OUT_DIR / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    # 2. per domain json & markdown
    by_domain = defaultdict(list)
    for c in chunks:
        by_domain[c["domain"]].append(c)

    for domain, items in sorted(by_domain.items()):
        slug = slugify(domain)
        # JSON
        (OUT_DIR / "chunks" / f"{slug}.json").write_text(
            json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        # Markdown
        lines = [
            f"# Vehicle Security: {domain}",
            "",
            f"> Source: [{REPO_URL}]({REPO_URL})",
            f"> Curated knowledge on automotive cybersecurity, CAN bus, hardware, ECU and exploitation.",
            "",
        ]
        for c in items:
            heading_text = " > ".join(c["metadata"]["heading_path"])
            body = c["content"].split("\n\n", 1)[-1]
            lines += [f"### {heading_text}", "", body, ""]
        (OUT_DIR / "knowledge-base" / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")

    # 3. manifest.json
    manifest = {
        "source_repo": REPO_URL,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_chunks": len(chunks),
        "domains": dict(Counter(c["domain"] for c in chunks).most_common()),
        "top_tags": dict(Counter(t for c in chunks for t in c["tags"]).most_common(25)),
        "schema": {
            "id": "str (avs-<sha1>)",
            "domain": "str",
            "skills": "list[str] (associated bug-bounty-skills)",
            "tags": "list[str]",
            "content": "str (contextual retrieval format)",
            "metadata": "source_repo, source_path, source_url, document_title, heading_path, doc_type, license, char_count",
        },
        "license": "CC0-1.0 (Public Domain)",
    }
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[+] Output written to {OUT_DIR}")


if __name__ == "__main__":
    main()
