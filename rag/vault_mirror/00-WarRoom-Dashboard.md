---
title: "WAR ROOM // CYBER-VAULT TACTICAL DASHBOARD"
tags:
  - dashboard
  - war-room
  - cti
  - bug-bounty
  - agents
date: 2026-11-07
version: v2.0.0
---

# 🛸 WAR ROOM // CENTRO DE MANDO TÁCTICO

> [!INTEL] **ESTADO DEL SISTEMA**: OPERACIONAL
> **Agente Activo**: Antigravity / Claude Code | **Memoria**: Qdrant Vector DB | **Stack**: Kepano Obsidian Tools

---

## 🛰️ MAPAS TÁCTICOS Y ALCANCE (CANVAS)

> [!TARGET] **PROGRAMA ACTIVO: SLACK (HackerOne)**
> - **Canvas Táctico**: [[Slack-Scope-Tactical-HUD.canvas|Abrir Mapa Táctico de Slack]]
> - **Activos Clave**: `slack.com` (Auth/Core), `api.slack.com` (REST API), `app.slack.com` (WebSockets), `slack-redir.net` (Redirect Shim), `quip.com` (Salesforce Docs)
> - **Archivo de Scope**: `scopes/scopes_for_slack.csv` (12 dominios en scope)

---

## ⚡ FLUIDEZ AGÉNTICA & HERRAMIENTAS ACTIVAS

| Herramienta / MCP | Rol Operativo | Comando / Acceso |
| :--- | :--- | :--- |
| **`cve-mcp-server`** | 28 APIs de CTI, NVD 2.0, FIRST EPSS y Orquestador | `triage_cve <CVE-ID>` |
| **`defuddle + knap`** | Ingesta limpia de URLs y renderizado de plantillas | `clip-intel.cmd <URL>` |
| **`XSSRush`** | Escáner XSS con Playwright DOM | `xssrush.cmd -u <URL>` |
| **`ARES MCP`** | ScopeFirewall defensivo y validación benigna | `python -m ares.mcp` |
| **`auto-ontology`** | Semántica NVIDIA y mapeo de relaciones | `http://localhost:3003` |

---

## 🧪 MATRIZ DE SEÑALIZACIÓN (CALLOUTS TÁCTICOS)

> [!TARGET] **TARGET VERIFICADO**: In-scope autorizado para auditoría.
> [!BREACH] **BREACH / VULN CRÍTICA**: Hallazgo verificado o entrada en CISA KEV.
> [!INTEL] **CTI & THREAT INTEL**: Correlación con actores de amenazas y campañas.
> [!PAYLOAD] **PAYLOAD BENIGNO (PoC)**: Validadores de concepto no destructivos.
> [!RECON] **RECON / ASSET DISCOVERY**: Huella digital, DNS pasivo y puertos expuestos.

---

## 📂 NAVEGACIÓN RÁPIDA DE LA BÓVEDA
- 📁 [[01-Vulnerabilidades/]] — Fichas técnicas de fallos y PoCs.
- 📁 [[02-Metodologias/]] — Playbooks de auditoría defensiva y bug bounty.
- 📁 [[03-Herramientas/]] — Suites de agentes, herramientas CLI y servidores MCP.
- 📁 [[04-Scopes/]] — Alcances autorizados, inventarios y mapas Canvas.
