#!/usr/bin/env python3
"""
BATCH-TARGETS // Generador masivo de fichas de reconocimiento táctico vía Knap Batch
Cruza scopes CSV con Dorks de Ignite Technologies y checklists automatizadas.
"""
import sys, os, csv, json, subprocess, datetime

def classify_tier(d):
    d = d.lower()
    if any(k in d for k in ["api", "rest", "graphql", "v1"]):
        return "Tier 1 Critical"
    elif any(k in d for k in ["app", "auth", "login", "sso"]) or d.count(".") <= 1:
        return "Tier 1"
    else:
        return "Tier 2"

def main():
    if len(sys.argv) < 2:
        print("Uso: python batch_targets.py <archivo.csv> [programa] [carpeta_salida]")
        print("Ejemplo: python batch_targets.py scopes_for_slack.csv Slack 04-Scopes/Slack")
        sys.exit(1)
        
    csv_file = sys.argv[1]
    program = sys.argv[2] if len(sys.argv) > 2 else "Slack"
    subfolder = sys.argv[3] if len(sys.argv) > 3 else f"04-Scopes/{program}"
    
    if not os.path.exists(csv_file):
        print(f"[!] Error: Archivo CSV no encontrado: {csv_file}")
        sys.exit(1)
        
    domains = []
    with open(csv_file, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.reader(f)
        for row in reader:
            for col in row:
                c = col.strip().lower().lstrip("*.").strip()
                if "." in c and " " not in c and "/" not in c and c not in domains:
                    domains.append(c)
                    
    now_str = datetime.datetime.now().strftime("%Y-%m-%d")
    items = []
    for d in domains:
        items.append({
            "domain": d,
            "program": program,
            "tier": classify_tier(d),
            "date": now_str
        })
        
    print(f"[*] Procesando {len(items)} activos para el programa {program}...")
    
    vault_base = r"G:\Mi unidad\Cyber-Vault"
    tpl_file = os.path.join(vault_base, "templates", "target-recon-template.md")
    dest_dir = os.path.join(vault_base, subfolder)
    os.makedirs(dest_dir, exist_ok=True)
    
    # Espejo local
    mirror_dir = os.path.join(r"C:\Users\logir\Projects\bug-bounty-skills\rag\vault_mirror", subfolder)
    os.makedirs(mirror_dir, exist_ok=True)
    
    json_batch_file = "scratch_batch.json"
    with open(json_batch_file, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)
        
    cmd = [
        "knap", "batch", tpl_file,
        "--data", json_batch_file,
        "--output-dir", dest_dir,
        "--filename", "{{ domain }}.md",
        "--overwrite"
    ]
    
    print("[*] Ejecutando knap batch...")
    try:
        subprocess.run(cmd, check=True, shell=True)
        print(f"[+] ¡{len(items)} fichas generadas exitosamente en: {dest_dir}!")
    except Exception as e:
        print(f"[!] Knap batch falló, aplicando render individual: {e}")
        for item in items:
            out_file = os.path.join(dest_dir, f"{item['domain']}.md")
            subprocess.run([
                "knap", "render", tpl_file,
                "--data-json", json.dumps(item),
                "-o", out_file
            ], check=False, shell=True)
            
    # Sincronizar copias en espejo
    for f in os.listdir(dest_dir):
        if f.endswith(".md"):
            with open(os.path.join(dest_dir, f), "r", encoding="utf-8") as rf:
                c = rf.read()
            with open(os.path.join(mirror_dir, f), "w", encoding="utf-8") as wf:
                wf.write(c)

    if os.path.exists(json_batch_file):
        os.remove(json_batch_file)
        
    print(f"[+] ¡Fichas tácticas de {program} listas en Cyber-Vault!")

if __name__ == "__main__":
    main()
