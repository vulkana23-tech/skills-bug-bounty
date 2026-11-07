import json
import pathlib
import shutil
import sys

PYTHON_EXE = r"C:\Users\logir\.gemini\antigravity-ide\scratch\bug-bounty-skills\rag\pentesting-everything\.venv\Scripts\python.exe"
MONOMI_SERVER = r"C:\Users\logir\.gemini\antigravity-ide\scratch\bug-bounty-skills\integrations\monomi\mcp_server.py"

MONOMI_MCP_BLOCK = {
    "command": PYTHON_EXE,
    "args": [MONOMI_SERVER]
}

def update_cursor():
    p = pathlib.Path.home() / ".cursor" / "mcp.json"
    if p.exists():
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            data = {}
        if "mcpServers" not in data:
            data["mcpServers"] = {}
        data["mcpServers"]["monomi"] = MONOMI_MCP_BLOCK
        p.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print("Updated Cursor mcp.json with monomi")

def update_opencode():
    p = pathlib.Path.home() / ".config" / "opencode" / "opencode.json"
    if p.exists():
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            data = {}
        if "mcp" not in data:
            data["mcp"] = {}
        data["mcp"]["monomi"] = MONOMI_MCP_BLOCK
        p.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print("Updated OpenCode opencode.json with monomi")

def update_codex():
    p = pathlib.Path.home() / ".codex" / "mcp.json"
    if p.exists():
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            data = {}
        if "mcpServers" not in data:
            data["mcpServers"] = {}
        data["mcpServers"]["monomi"] = MONOMI_MCP_BLOCK
        p.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print("Updated Codex mcp.json with monomi")

def update_claude_desktop():
    appdata = pathlib.Path.home() / "AppData" / "Roaming" / "Claude" / "claude_desktop_config.json"
    if appdata.exists():
        try:
            data = json.loads(appdata.read_text(encoding="utf-8"))
        except Exception:
            data = {}
        if "mcpServers" not in data:
            data["mcpServers"] = {}
        data["mcpServers"]["monomi"] = MONOMI_MCP_BLOCK
        appdata.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print("Updated Claude Desktop config with monomi")

def export_antigravity_mcp():
    mcp_dir = pathlib.Path("C:/Users/logir/.gemini/antigravity/mcp/monomi")
    mcp_dir.mkdir(parents=True, exist_ok=True)

    instructions = """# Monomi MCP Best Practices

Monomi is a passive attack surface reconnaissance and threat intelligence tool.
All operations are 100% passive (using Certificate Transparency logs, DNS lookups, and Shodan InternetDB).
No direct offensive traffic is sent to target hostnames or IPs.

Available Tools:
- `find_subdomains`: Discover subdomains from crt.sh & Cert Spotter with rule-based categorization.
- `check_email_auth`: Check SPF, DMARC, and DKIM for email spoofing susceptibility.
- `check_takeover`: Follow CNAMEs to detect dangling cloud targets (Azure, AWS, etc.).
- `enrich_hosts`: Resolve hostnames to IPs, ASNs, providers, and countries.
- `check_ports`: Check open ports and CVEs passively via Shodan InternetDB.
- `investigate_ip`: Triage suspicious IPs (Tor exits, VPNs, CDN edges, ASN info).
"""
    (mcp_dir / "instructions.md").write_text(instructions, encoding="utf-8")

    sys.path.insert(0, "integrations/monomi")
    import mcp_server
    tools = mcp_server.mcp._tool_manager.list_tools()

    for t in tools:
        schema = {
            "name": t.name,
            "description": t.description,
            "parameters": t.parameters if hasattr(t, "parameters") else {}
        }
        (mcp_dir / f"{t.name}.json").write_text(json.dumps(schema, indent=2), encoding="utf-8")
        print(f"Exported Antigravity schema {t.name}.json")

    print(f"Exported {len(tools)} Monomi tools to {mcp_dir}")

def deploy_skills():
    skill_content = """---
name: monomi-recon
description: "Reconocimiento pasivo de superficie de ataque (Attack Surface Recon) e inteligencia de amenazas (Threat Intel) con Monomi. Descubrimiento de subdominios por Certificate Transparency, auditoría de puertos y CVEs pasiva vía Shodan InternetDB, detección de Subdomain Takeover y triaje de IPs sospechosas."
---

# Monomi · Passive Recon & Threat Intel

Herramienta de reconocimiento 100% pasivo y Threat Intel.

## 🚀 Uso Rápido CLI
```powershell
# Descubrimiento de subdominios
.\\monomi.cmd target.com

# Enriquecimiento completo (IPs, ASN, Proveedor Cloud)
.\\monomi.cmd target.com --enrich

# Detección pasiva de puertos abiertos y CVEs (Shodan InternetDB)
.\\monomi.cmd target.com --ports

# Detección de vulnerabilidades de Subdomain Takeover (CNAMEs huérfanos)
.\\monomi.cmd target.com --takeover

# Auditoría de spoofing de email (SPF/DMARC/DKIM)
.\\monomi.cmd target.com --email

# Triaje de IPs sospechosas (Tor, VPN, Hosting)
.\\monomi.cmd --investigate-ip 1.1.1.1 8.8.8.8
```

## 🤖 Servidor MCP Integrado
Expone 7 herramientas pasivas en Claude, Cursor, Codex, OpenCode y Antigravity:
- `find_subdomains`
- `check_email_auth`
- `check_takeover`
- `enrich_hosts`
- `check_ports`
- `investigate_ip`
- `ping`
"""
    skills_dir = pathlib.Path("skills/monomi-recon")
    skills_dir.mkdir(parents=True, exist_ok=True)
    (skills_dir / "SKILL.md").write_text(skill_content, encoding="utf-8")

    home = pathlib.Path.home()
    destinations = [
        home / ".agents" / "skills" / "monomi-recon",
        home / ".claude" / "skills" / "monomi-recon",
        home / ".codex" / "skills" / "monomi-recon"
    ]
    for d in destinations:
        d.mkdir(parents=True, exist_ok=True)
        shutil.copy(skills_dir / "SKILL.md", d / "SKILL.md")
    print("Deployed monomi-recon skills to .agents, .claude and .codex")

def main():
    update_cursor()
    update_opencode()
    update_codex()
    update_claude_desktop()
    export_antigravity_mcp()
    deploy_skills()
    print("Monomi completamente integrado en todos los entornos!")

if __name__ == "__main__":
    main()

