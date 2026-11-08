---
title: "OpenSandbox"
tool_name: "OpenSandbox"
github_repo: "https://github.com/opensandbox-group/OpenSandbox"
category: "Harness-Engineering"
language: "Python / Go / Multiplataforma"
tags:
  - "herramienta"
  - "harness-engineering"
  - "sandbox"
  - "mcp"
  - "seguridad-defensiva"
  - "docker"
status: "Operativo"
---

# 🛡️ OpenSandbox — Plataforma Estándar de Sandboxes para Agentes de IA

> [!NOTE] **Propósito Táctico**: Plataforma de ejecución aislada en infraestructura propia (Docker / microVMs Firecracker) que protege el host físico frente a comandos destructivos o malware ejecutado por agentes de IA autónomos.
> **Organización**: `Agentic AI Foundation (AAIF)` | **Repositorio**: [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)

---

## ⚡ Características Clave
- **Arranque ultra-rápido en 64 ms**: Sandboxes efímeros basados en microVMs Firecracker con preservación de estado (pause / resume).
- **Credential Vault**: Permite al agente interactuar con servicios externos sin exponer las credenciales y claves API reales dentro del sandbox.
- **Políticas de Egress Estrictas**: Cortafuegos a nivel de contenedor para que los agentes sólo ataquen los objetivos autorizados dentro del scope.
- **Soporte Nativo MCP**: Incluye el servidor `opensandbox-mcp` operable sobre transporte `stdio`.

---

## 🔌 Conexión en Clientes MCP (Ya Configurado en tu Entorno)
- **Binario ejecutable**: `C:\Users\logir\Projects\bug-bounty-skills\integrations\cve-mcp-server\.venv\Scripts\opensandbox-mcp.exe`
- **Transporte**: `stdio`
- **Activo en**: Cursor, OpenCode, DeepSeek Harness y WorkBuddy AI.

---
*Ficha táctica catalogada para la sección de Harness Engineering del Cyber-Vault.*