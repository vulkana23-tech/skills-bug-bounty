#!/usr/bin/env python3
import sys, os, subprocess, json, datetime, re

def clean_filename(title):
    s = re.sub(r'[^\w\s-]', '', title).strip()
    s = re.sub(r'[-\s]+', '-', s)
    return s[:60] if s else "intel-note"

def main():
    if len(sys.argv) < 2:
        print("Uso: python clip_intel.py <URL> [tag1,tag2,...] [categoria]")
        sys.exit(1)
        
    url = sys.argv[1]
    tags_arg = sys.argv[2] if len(sys.argv) > 2 else "writeup,bug-bounty"
    tags = [t.strip() for t in tags_arg.split(",") if t.strip()]
    categoria = sys.argv[3] if len(sys.argv) > 3 else "01-Vulnerabilidades"
    
    print(f"[*] Parseando URL con Defuddle: {url}")
    try:
        res = subprocess.run(["defuddle", "parse", url], capture_output=True, text=True, check=True)
        raw_md = res.stdout.strip()
    except Exception as e:
        print(f"[!] Error ejecutando defuddle: {e}")
        return

    # Extraer titulo si existe como primer h1
    lines = raw_md.splitlines()
    title = "Artículo Extraído"
    content_lines = []
    for l in lines:
        if l.startswith("# ") and title == "Artículo Extraído":
            title = l.replace("# ", "").strip()
        else:
            content_lines.append(l)
    
    content = "\n".join(content_lines).strip()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    data = {
        "title": title,
        "tags": tags,
        "url": url,
        "date": now_str,
        "author": "Defuddle + Knap Pipeline",
        "summary": f"Artículo extraído limpiamente de {url}. Sin ruido de navegación ni scripts.",
        "content": content
    }
    
    vault_base = r"G:\Mi unidad\Cyber-Vault"
    tpl_file = os.path.join(vault_base, "templates", "tactical-intel-template.md")
    
    dest_dir = os.path.join(vault_base, categoria)
    os.makedirs(dest_dir, exist_ok=True)
    
    filename = f"{clean_filename(title)}.md"
    out_file = os.path.join(dest_dir, filename)
    
    print(f"[*] Renderizando plantilla Knap hacia: {out_file}")
    json_data = json.dumps(data)
    
    try:
        res_knap = subprocess.run(
            ["knap", "render", tpl_file, "--data-json", json_data, "-o", out_file],
            capture_output=True, text=True, check=True
        )
        print(f"[+] ¡Nota creada exitosamente en Cyber-Vault!")
        print(f"    Ruta: {out_file}")
    except Exception as e:
        print(f"[!] Error ejecutando knap: {e}")
        # Fallback directo en python
        fallback = f"""---
title: "{title}"
tags: {json.dumps(tags)}
source_url: "{url}"
date: "{now_str}"
---

# 🎯 {title}

> [!INTEL] **Fuente Original**: {url}
> **Capturado**: {now_str} | **Motor**: Defuddle Fallback

{content}
"""
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(fallback)
        print(f"[+] Nota guardada vía fallback: {out_file}")

if __name__ == "__main__":
    main()
