#!/usr/bin/env python3
"""
sync_vigilantes_intel.py - Integrador de CTI de 'LOS VIGILANTES · v3' (Custodes Intellegentiae)
Descarga los últimos boletines y fuentes de inteligencia (editions.js y sources.js),
los convierte en notas enriquecidas para Obsidian (Cyber-Vault) y los indexa en Qdrant.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VAULT_DIR = Path("G:/Mi unidad/Cyber-Vault")
INTEL_DIR = VAULT_DIR / "05-Cyber-Intel"
BASE_URL = "https://custodes-intellegentiae.exdataveritas.com"
EDITIONS_URL = f"{BASE_URL}/data/editions.js"
SOURCES_URL = f"{BASE_URL}/v3/sources.js"


def fetch_js_variable(url: str, var_name: str) -> dict:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        raw = resp.read().decode("utf-8", errors="ignore")
    
    first_brace = raw.find('{')
    if first_brace != -1:
        data, _ = json.JSONDecoder().raw_decode(raw[first_brace:])
        return data
    return {}


def format_blocks_to_markdown(blocks: list) -> str:
    md_lines = []
    for b in blocks:
        b_type = b.get("type", "generic")
        if b_type == "section":
            md_lines.append(f"\n## 📌 {b.get('text')}\n")
        elif b_type == "header":
            md_lines.append(f"\n### 🚨 {b.get('title')}\n")
        elif "fields" in b:
            for fld in b.get("fields", []):
                label = fld.get("label", "Dato")
                val = fld.get("value")
                if isinstance(val, list):
                    parts = []
                    for item in val:
                        if isinstance(item, dict):
                            txt = item.get("text", "")
                            href = item.get("href")
                            if href:
                                parts.append(f"[{txt}]({href})")
                            else:
                                parts.append(txt)
                        else:
                            parts.append(str(item))
                    val_str = "".join(parts).strip()
                else:
                    val_str = str(val).strip()
                md_lines.append(f"- **{label}:** {val_str}")
            md_lines.append("")
        elif "text" in b:
            md_lines.append(f"{b.get('text')}\n")
    return "\n".join(md_lines)


def sync_vigilantes(force_qdrant: bool = True) -> dict:
    print("=" * 60)
    print("📡 Sincronizando con LOS VIGILANTES · v3 (Custodes Intellegentiae)")
    print("=" * 60)

    INTEL_DIR.mkdir(parents=True, exist_ok=True)
    now_str = time.strftime("%Y-%m-%d %H:%M:%S")

    # 1. Descargar ediciones
    print("[+] Obteniendo boletines recientes desde editions.js...")
    editions = fetch_js_variable(EDITIONS_URL, "window.WATCHERS_EDITIONS")
    
    # 2. Descargar fuentes
    print("[+] Obteniendo catálogo de fuentes CTI desde sources.js...")
    sources = fetch_js_variable(SOURCES_URL, "window.WATCHERS_SOURCES")

    created_notes = []

    # 2.1 Procesar cybersecurity-digest
    cybersec = editions.get("cybersecurity-digest", {})
    if cybersec and "blocks" in cybersec:
        cybersec_md = f"""---
title: "Boletín de Ciberseguridad Defensiva (Los Vigilantes)"
date: {now_str}
tags:
  - cti
  - vigilantes
  - defensivo
  - cisa
  - rce
source: "{BASE_URL}/v3/#cybersecurity-digest"
---

# 🛡️ Boletín de Ciberseguridad Defensiva

> **Fuente:** [LOS VIGILANTES · v3 / Ex Data Veritas]({BASE_URL}/v3/#cybersecurity-digest)
> **Última actualización:** {now_str}
> **Relacionado con:** [[00-Indice]] | [[05-Cyber-Intel/Fuentes-Monitoreadas-CTI]]

{format_blocks_to_markdown(cybersec.get("blocks", []))}
"""
        note_path = INTEL_DIR / "Boletin-Ciberseguridad-Defensiva.md"
        note_path.write_text(cybersec_md, encoding="utf-8")
        created_notes.append("Boletin-Ciberseguridad-Defensiva.md")
        print("  ✅ Guardado: 05-Cyber-Intel/Boletin-Ciberseguridad-Defensiva.md")

    # 2.2 Procesar cyber-intelligence-digest
    cyberintel = editions.get("cyber-intelligence-digest", {})
    if cyberintel and "blocks" in cyberintel:
        cyberintel_md = f"""---
title: "Boletín de Ciberinteligencia & Dark Web (PIR)"
date: {now_str}
tags:
  - cti
  - vigilantes
  - darkweb
  - pir
  - threat-intel
source: "{BASE_URL}/v3/#cyber-intelligence-digest"
---

# 🕵️‍♂️ Boletín de Ciberinteligencia & Dark Web (PIR)

> **Fuente:** [LOS VIGILANTES · v3 / Ex Data Veritas]({BASE_URL}/v3/#cyber-intelligence-digest)
> **Última actualización:** {now_str}
> **Relacionado con:** [[00-Indice]] | [[05-Cyber-Intel/Fuentes-Monitoreadas-CTI]]

{format_blocks_to_markdown(cyberintel.get("blocks", []))}
"""
        note_path = INTEL_DIR / "Boletin-Ciberinteligencia-PIR-DarkWeb.md"
        note_path.write_text(cyberintel_md, encoding="utf-8")
        created_notes.append("Boletin-Ciberinteligencia-PIR-DarkWeb.md")
        print("  ✅ Guardado: 05-Cyber-Intel/Boletin-Ciberinteligencia-PIR-DarkWeb.md")

    # 2.3 Procesar ai-builders-digest
    aibuilders = editions.get("ai-builders-digest", {})
    if aibuilders and "blocks" in aibuilders:
        aibuilders_md = f"""---
title: "Boletín de Inteligencia en IA & Modelos (AI Builders)"
date: {now_str}
tags:
  - ai
  - llm
  - vigilantes
source: "{BASE_URL}/v3/#ai-builders-digest"
---

# 🤖 Boletín de Inteligencia en IA & Modelos

> **Fuente:** [LOS VIGILANTES · v3 / Ex Data Veritas]({BASE_URL}/v3/#ai-builders-digest)
> **Última actualización:** {now_str}
> **Relacionado con:** [[00-Indice]]

{format_blocks_to_markdown(aibuilders.get("blocks", []))}
"""
        note_path = INTEL_DIR / "Boletin-AI-Builders.md"
        note_path.write_text(aibuilders_md, encoding="utf-8")
        created_notes.append("Boletin-AI-Builders.md")
        print("  ✅ Guardado: 05-Cyber-Intel/Boletin-AI-Builders.md")

    # 2.4 Generar Directorio de Fuentes CTI
    sec_sources = sources.get("cybersecurity-digest", {})
    intel_sources = sources.get("cyber-intelligence-digest", {})

    sources_md = f"""---
title: "Directorio de Fuentes CTI & Dark Web (Los Vigilantes)"
date: {now_str}
tags:
  - osint
  - cti
  - feeds
  - darkweb
---

# 📡 Directorio de Fuentes de Ciberinteligencia (Los Vigilantes · v3)

Este catálogo reúne las fuentes monitorizadas activamente por el sistema Custodes Intellegentiae.

## 🕵️‍♂️ Cuentas de X / Threat Intel & Dark Web
"""
    x_accounts = intel_sources.get("x", []) + sec_sources.get("x", [])
    seen_handles = set()
    for acc in x_accounts:
        handle = acc.get("handle")
        if handle and handle not in seen_handles:
            seen_handles.add(handle)
            name = acc.get("name", handle)
            sources_md += f"- **{name}**: [@{handle}](https://x.com/{handle})\n"

    sources_md += "\n## 📰 Blogs y CERTs Internacionales Monitoreados\n"
    blogs = intel_sources.get("blogs", []) + sec_sources.get("blogs", [])
    seen_blogs = set()
    for b in blogs:
        name = b.get("name")
        feed = b.get("feedUrl") or b.get("siteUrl") or ""
        if name and name not in seen_blogs:
            seen_blogs.add(name)
            if feed:
                sources_md += f"- [{name}]({feed})\n"
            else:
                sources_md += f"- **{name}**\n"

    sources_file = INTEL_DIR / "Fuentes-Monitoreadas-CTI.md"
    sources_file.write_text(sources_md, encoding="utf-8")
    created_notes.append("Fuentes-Monitoreadas-CTI.md")
    print("  ✅ Guardado: 05-Cyber-Intel/Fuentes-Monitoreadas-CTI.md")

    # 3. Actualizar 00-Indice.md con el nuevo módulo
    indice_file = VAULT_DIR / "00-Indice.md"
    if indice_file.exists():
        idx_content = indice_file.read_text(encoding="utf-8")
        if "05-Cyber-Intel" not in idx_content:
            new_section = """
### 4. [[05-Cyber-Intel/Boletin-Ciberinteligencia-PIR-DarkWeb|Ciberinteligencia en Vivo (Los Vigilantes · v3)]]
- [[05-Cyber-Intel/Boletin-Ciberseguridad-Defensiva|Boletín Defensivo (Vulnerabilidades CISA & Parches)]]
- [[05-Cyber-Intel/Boletin-Ciberinteligencia-PIR-DarkWeb|Boletín Dark Web & Campañas de Amenazas (PIR)]]
- [[05-Cyber-Intel/Fuentes-Monitoreadas-CTI|Directorio de Fuentes CTI (105+ Feeds & Cuentas)]]
"""
            idx_content += new_section
            indice_file.write_text(idx_content, encoding="utf-8")
            print("  ✅ 00-Indice.md actualizado con enlaces a Los Vigilantes.")

    # 4. Sincronizar inmediatamente con Qdrant
    if force_qdrant:
        print("\n[+] Indexando nuevos boletines en Qdrant (GPU RTX 3060)...")
        try:
            import vault_qdrant
            res = vault_qdrant.sync_vault()
            print(f"  ✅ Qdrant sincronizado: {res.get('indexed_notes')} notas indexadas, {res.get('total_points_in_qdrant')} vectores totales.")
        except Exception as ex:
            print(f"  [!] Error sincronizando con Qdrant: {ex}", file=sys.stderr)

    print("\n🎉 Sincronización con 'LOS VIGILANTES' completada exitosamente.")
    return {
        "ok": True,
        "notes": created_notes,
        "intel_dir": str(INTEL_DIR)
    }


if __name__ == "__main__":
    sync_vigilantes()
