# 🏰 LobeHub Multi-Agent War Room for Bug Bounty & Defensive Audit

Este módulo transforma a **LobeHub / LobeChat** en la **Sala de Guerra Visual (War Room)** del ecosistema de Bug Bounty, integrando todos los conectores MCP, la memoria vectorial de Obsidian y cuadrillas (*crews*) de agentes especializados.

---

## 🚀 Despliegue Rápido (Local Docker)

Para iniciar tu War Room en tu máquina o servidor local:

```bash
docker compose -f integrations/lobehub/docker-compose.yml up -d
```

Acceso web inmediato:
* **URL:** `http://localhost:3210`
* **Contraseña por defecto:** `CyberWarRoom2026!`

---

## 🤖 Cuadrilla de Agentes Preconfigurados (`agents/`)

LobeHub permite importar roles en formato JSON. En `integrations/lobehub/agents/` dispones de 3 agentes listos:

1. **`1-triager-sentinel.json` (El Centinela de Triage)**:
   - **Misión:** Escucha boletines CTI (Los Vigilantes, NVD, CISA KEV), cruza las tecnologías afectadas con `inventario.json`, respeta estrictamente los `scopes/*.csv` y genera la cola de candidatos priorizados.
   - **Herramientas MCP conectadas:** `obsidian-qdrant`, `ares`.

2. **`2-bounty-auditor.json` (El Auditor Ofensivo Ético)**:
   - **Misión:** Toma un objetivo de la cola y ejecuta pruebas de concepto no destructivas guiadas por los 164 skills tácticos (IDOR, BOLA, Google Cloud IAM, SSRF, 403 Bypass, SSTI).
   - **Herramientas MCP conectadas:** `auto-ontology`, `opencheck`, `rea`, `vulnclaw`, `interceptor`.

3. **`3-report-validator-7gate.json` (El Validador y Redactor 7-Gate)**:
   - **Misión:** Aplica la compuerta de calidad de 7 preguntas para descartar falsos positivos, calcula la métrica CVSS v3.1 y redacta el informe en Markdown con pasos de reproducción verificados listo para HackerOne, Bugcrowd o Intigriti.
   - **Herramientas MCP conectadas:** `obsidian-qdrant`, `craft-anything`.

---

## 🔌 Conexión MCP en LobeHub

Copia o importa la configuración de `integrations/lobehub/lobehub_mcp_config.json` en los ajustes de LobeHub (Settings -> Plugins / MCP):

* **Obsidian-Qdrant:** `http://127.0.0.1:8765/mcp` o `http://100.96.50.20:8765/mcp` (Tailscale)
* **Auto-Ontology (NVIDIA):** `http://127.0.0.1:3003`
* **ARES / ScopeFirewall:** Vía stdio o bridge local
* **OpenCheck:** `python integrations/opencheck/mcp_server.py`
