#!/usr/bin/env python3
"""
CANVAS-GEN // Generador Automatizado de Mapas Tácticos JSON Canvas 1.0
Convierte listas de subdominios o CSVs de scope en diagramas interactivos de Obsidian.
"""
import sys, os, csv, json, hashlib, re

def make_id(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:16]

def classify_domain(domain):
    d = domain.lower()
    if any(k in d for k in ["api", "rest", "graphql", "v1", "v2", "gateway", "backend"]):
        return "api", "🔥 APIS & SERVICIOS DE BACKEND (Tier 1)", "1" # Red
    elif any(k in d for k in ["app", "auth", "login", "sso", "portal", "account"]) or d.count(".") <= 1:
        return "core", "⚡ CORE PLATFORM & AUTENTICACIÓN (Tier 1)", "5" # Cyan
    elif any(k in d for k in ["img", "media", "cdn", "static", "redir", "edge", "asset", "cache"]):
        return "media", "🛰️ PROXIES, CDNS & CONTENT DELIVERY (Tier 2)", "3" # Yellow
    else:
        return "collab", "🟣 INTEGRACIONES & COLABORACIÓN (Tier 2)", "6" # Purple

def parse_input(filepath):
    domains = []
    if filepath.endswith(".csv"):
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            reader = csv.reader(f)
            for row in reader:
                for col in row:
                    c = col.strip().lower().lstrip("*.").strip()
                    if "." in c and " " not in c and "/" not in c and c not in domains:
                        domains.append(c)
    else:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                c = line.strip().lower().lstrip("*.").strip()
                if "." in c and " " not in c and "/" not in c and c not in domains:
                    domains.append(c)
    return domains

def main():
    if len(sys.argv) < 2:
        print("Uso: python canvas_gen.py <archivo.csv|hosts.txt> [nombre_canvas] [carpeta_destino]")
        print("Ejemplo: python canvas_gen.py scopes_for_slack.csv Slack-Tactical 04-Scopes")
        sys.exit(1)
        
    in_file = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(os.path.basename(in_file))[0]
    folder = sys.argv[3] if len(sys.argv) > 3 else "04-Scopes"
    
    if not os.path.exists(in_file):
        print(f"[!] Error: Archivo no encontrado: {in_file}")
        sys.exit(1)
        
    domains = parse_input(in_file)
    print(f"[*] Activos detectados: {len(domains)}")
    
    # Agrupar por categoría
    categorized = {"core": [], "api": [], "media": [], "collab": []}
    labels = {}
    colors = {}
    
    for d in domains:
        cat, label, col = classify_domain(d)
        categorized[cat].append(d)
        labels[cat] = label
        colors[cat] = col
        
    nodes = []
    edges = []
    
    # Coordenadas base para 4 cuadrantes
    grid_coords = {
        "core": (-700, -350),
        "api": (50, -350),
        "media": (-700, 200),
        "collab": (50, 200)
    }
    
    first_node_by_cat = {}
    
    for cat, items in categorized.items():
        if not items:
            continue
        gx, gy = grid_coords[cat]
        c_color = colors[cat]
        c_label = labels[cat]
        
        card_w = 480
        card_h = 130
        spacing = 30
        group_padding = 40
        
        gh = group_padding * 2 + len(items) * (card_h + spacing)
        gw = card_w + (group_padding * 2)
        
        # Grupo bounding box
        gid = make_id(f"group_{name}_{cat}")
        nodes.append({
            "id": gid,
            "type": "group",
            "label": c_label,
            "x": gx,
            "y": gy,
            "width": gw,
            "height": gh,
            "color": c_color
        })
        
        for idx, d in enumerate(items):
            nid = make_id(f"node_{name}_{d}")
            nx = gx + group_padding
            ny = gy + group_padding + idx * (card_h + spacing)
            
            node_body = f"## 🎯 {d}\n**Scope**: `In-Scope Verificado`\n**Triage**: [[{d}]]\n> [!TARGET]\n> Auditoría autorizada. Dorks: `site:{d}`"
            
            n_obj = {
                "id": nid,
                "type": "text",
                "text": node_body,
                "x": nx,
                "y": ny,
                "width": card_w,
                "height": card_h,
                "color": c_color
            }
            nodes.append(n_obj)
            
            if cat not in first_node_by_cat:
                first_node_by_cat[cat] = nid

    # Crear enlaces entre categorías si existen
    if "core" in first_node_by_cat and "api" in first_node_by_cat:
        edges.append({
            "id": make_id(f"edge_{name}_core_api"),
            "fromNode": first_node_by_cat["core"],
            "fromSide": "right",
            "toNode": first_node_by_cat["api"],
            "toSide": "left",
            "label": "API Calls / Microservicios",
            "toEnd": "arrow"
        })
        
    if "core" in first_node_by_cat and "media" in first_node_by_cat:
        edges.append({
            "id": make_id(f"edge_{name}_core_media"),
            "fromNode": first_node_by_cat["core"],
            "fromSide": "bottom",
            "toNode": first_node_by_cat["media"],
            "toSide": "top",
            "label": "Content CDN Delivery",
            "toEnd": "arrow"
        })
        
    canvas_dict = {
        "nodes": nodes,
        "edges": edges
    }
    
    # Guardar en Cyber-Vault y espejos
    filename = f"{name}.canvas"
    vault_base = r"G:\Mi unidad\Cyber-Vault"
    out_vault = os.path.join(vault_base, folder, filename)
    os.makedirs(os.path.dirname(out_vault), exist_ok=True)
    
    with open(out_vault, "w", encoding="utf-8") as f:
        json.dump(canvas_dict, f, indent=2)
    print(f"[+] Canvas generado en Cyber-Vault: {out_vault}")
    
    # Guardar espejo en local
    mirror_paths = [
        os.path.join(r"c:\Users\logir\.gemini\antigravity-ide\scratch\bug-bounty-skills\rag\vault_mirror", folder, filename),
        os.path.join(r"C:\Users\logir\Projects\bug-bounty-skills\rag\vault_mirror", folder, filename)
    ]
    for mp in mirror_paths:
        os.makedirs(os.path.dirname(mp), exist_ok=True)
        with open(mp, "w", encoding="utf-8") as f:
            json.dump(canvas_dict, f, indent=2)
            
    print("[+] ¡Canvas táctico generado e indexado exitosamente!")

if __name__ == "__main__":
    main()
