---
name: monomi-recon
description: "Reconocimiento pasivo de superficie de ataque (Attack Surface Recon) e inteligencia de amenazas (Threat Intel) con Monomi. Descubrimiento de subdominios por Certificate Transparency, auditoría de puertos y CVEs pasiva vía Shodan InternetDB, detección de Subdomain Takeover y triaje de IPs sospechosas."
---

# Monomi · Passive Recon & Threat Intel

Herramienta de reconocimiento 100% pasivo y Threat Intel.

## 🚀 Uso Rápido CLI
```powershell
# Descubrimiento de subdominios
.\monomi.cmd target.com

# Enriquecimiento completo (IPs, ASN, Proveedor Cloud)
.\monomi.cmd target.com --enrich

# Detección pasiva de puertos abiertos y CVEs (Shodan InternetDB)
.\monomi.cmd target.com --ports

# Detección de vulnerabilidades de Subdomain Takeover (CNAMEs huérfanos)
.\monomi.cmd target.com --takeover

# Auditoría de spoofing de email (SPF/DMARC/DKIM)
.\monomi.cmd target.com --email

# Triaje de IPs sospechosas (Tor, VPN, Hosting)
.\monomi.cmd --investigate-ip 1.1.1.1 8.8.8.8
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
