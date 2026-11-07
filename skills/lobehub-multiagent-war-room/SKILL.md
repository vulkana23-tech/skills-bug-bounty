---
name: lobehub-multiagent-war-room
description: Orquestación y despliegue del War Room multi-agente en LobeHub para auditorías de Bug Bounty. Integra roles especializados (Triage, Auditor, Validador 7-Gate), memoria de Obsidian y servidores MCP en una interfaz visual colaborativa.
---

# LobeHub Multi-Agent War Room for Bug Bounty

## Cuándo usar esta habilidad
Utiliza esta habilidad cuando el usuario desee interactuar visualmente con múltiples agentes de seguridad en equipo, coordinar auditorías en un espacio de trabajo colaborativo o desplegar la interfaz gráfica de LobeHub conectada al ecosistema MCP.

---

## Arquitectura de la Sala de Guerra (3 Agentes Coordinados)

```
┌────────────────────────────────────────────────────────┐
│                   LOBEHUB WAR ROOM                     │
│  (Interfaz Gráfica Colaborativa - http://localhost:3210)│
└───────────┬───────────────────┬────────────────────────┘
            │                   │
            ▼                   ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ 1. CENTINELA     │    │ 2. AUDITOR       │    │ 3. VALIDADOR     │
│    DE TRIAGE     │───>│    ÉTICO         │───>│    7-GATE        │
│                  │    │                  │    │                  │
│ • Escucha CTI    │    │ • 164 Skills     │    │ • 7-Question Gate│
│ • Filtra Scopes  │    │ • Auto-Ontology  │    │ • CVSS v3.1 Calc │
│ • inventario.json│    │ • PoC benigno    │    │ • Informe MD     │
└───────────┬──────┘    └──────────┬───────┘    └──────────┬───────┘
            │                      │                       │
            └──────────────────────┼───────────────────────┘
                                   │
                                   ▼
             SERVIDORES MCP (obsidian-qdrant, ares, rea,
             auto-ontology, opencheck, craft-anything)
```

---

## Procedimiento de Despliegue y Conexión

### 1. Iniciar el Contenedor de LobeHub
```bash
docker compose -f integrations/lobehub/docker-compose.yml up -d
```
Verifica que el servicio esté arriba visitando `http://localhost:3210` (Clave de acceso: `CyberWarRoom2026!`).

### 2. Cargar los Agentes Especializados
En la interfaz de LobeHub:
1. Ve a **Ajustes de Agentes / Gestión de Roles**.
2. Importa los 3 archivos JSON ubicados en `integrations/lobehub/agents/`:
   - `1-triager-sentinel.json`
   - `2-bounty-auditor.json`
   - `3-report-validator-7gate.json`

### 3. Vincular los Servidores MCP
Configura las URLs de los servidores MCP locales definidos en `integrations/lobehub/lobehub_mcp_config.json`:
- **`obsidian-qdrant`**: `http://localhost:8765/mcp`
- **`auto-ontology`**: `http://localhost:3003`

---

## Reglas de Interacción en el War Room

1. **Regla de Alcance**: Ningún agente puede proponer acciones sobre dominios o IPs no listados en `scopes/*.csv`.
2. **Validación Previa al Reporte**: El *Bounty Auditor* jamás da por confirmada una vulnerabilidad sin que el *Report Validator* haya verificado las 7 preguntas de la compuerta de calidad.
3. **Persistencia del Conocimiento**: Todo nuevo hallazgo validado debe enviarse a la memoria vectorial mediante `save_note_to_vault` para alimentar al Cyber-Vault.
