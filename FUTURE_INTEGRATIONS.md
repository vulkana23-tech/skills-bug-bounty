# 🔮 Integraciones Futuras & Hoja de Ruta (Backlog de Capacidad)

Este documento registra herramientas, arquitecturas y módulos avanzados evaluados para el ecosistema local de ciberseguridad, listados para su despliegue cuando se disponga de mayor capacidad de hardware y almacenamiento en disco.

---

## 1. APX v2 (Agent Project Context)
* **Repositorio:** [https://github.com/agentprojectcontext/apx.git](https://github.com/agentprojectcontext/apx.git)
* **Tipo:** Agent OS / Orquestador Multi-Agente Local / Interfaz Multiplataforma.
* **Propósito:**
  - Desplegar cuadrillas (*crews*) de agentes de seguridad autónomos que se deleguen tareas entre sí (Recon -> Análisis -> PoC).
  - Control y notificaciones remotas vía bots de **Telegram / WhatsApp / Discord**.
  - Tareas programadas en segundo plano tipo *cron* que se ejecutan automáticamente de noche.
  - Navegador web Chromium visual guiado por los agentes.
* **Prerrequisitos de Hardware recomendados:**
  - **Disco C:** Al menos 25-30 GB libres (evitar riesgos de saturación del sistema por Electron, Node.js y dependencias de Chromium).
  - **VRAM / Cómputo:** Mantener o ampliar VRAM (>8-12 GB) o utilizar modelos más ligeros/cuantizados para permitir múltiples turnos de inferencia simultáneos sin encolamientos lentos.
* **Plan de Integración Futuro:**
  - Conectar APX directamente al demonio de Ollama local (`whiterabbitneo:latest` y `qwen2.5-coder:7b`).
  - Cargar el servidor MCP de **Scrapling** (`scrapling mcp`) como herramienta de navegación sigilosa nativa de los agentes de APX.
  - Conectar la memoria de los agentes a los fragmentos RAG locales (`rag/`).

---

## 2. Estado Actual de la Suite Local (Activa y Optimizada)
* **Memoria RAG Local:** 24.700+ recursos indexados (PortSwigger, HackerOne, CVEs, Vehicle Security).
* **Motor LLM:** Ollama en GPU RTX 3060 (`whiterabbitneo:latest` + `qwen2.5-coder:7b`).
* **Extracción Web Sigilosa:** `stealth_intel.py` (Scrapling con bypass TLS Chrome + Agent-Reach para GitHub/Reddit).
* **Interfaz de Usuario:** `cyber_chat_app.py` en [http://localhost:7860](http://localhost:7860).
* **Espacio en Disco:** Protegido y estable (~12.5 GB libres).

