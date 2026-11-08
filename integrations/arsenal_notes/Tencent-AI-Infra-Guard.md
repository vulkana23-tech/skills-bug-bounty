---
title: "Tencent AI-Infra-Guard (A.I.G)"
tool_name: "AI-Infra-Guard"
github_repo: "https://github.com/Tencent/AI-Infra-Guard"
category: "Harness-Engineering"
language: "Go / Python"
tags:
  - "herramienta"
  - "ai-security"
  - "red-team"
  - "mcp"
  - "skills"
  - "harness-engineering"
  - "jailbreak"
status: "Operativo / Standalone CLI Disponible"
---

# 🛡️ Tencent AI-Infra-Guard (A.I.G) — Plataforma Full-Stack de AI Red Teaming

> [!NOTE] **Propósito Táctico**: Plataforma unificada de seguridad ofensiva para inteligencia artificial desarrollada por **Tencent Zhuque Lab**. Es la primera suite de un gigante tecnológico especializada en auditar la seguridad de **Servidores MCP** y **Skills de Agentes**, además de infraestructuras de IA (Ollama, vLLM) y modelos LLM frente a *jailbreaks*.
> **Autor**: `Tencent Zhuque Lab` | **Presentado en**: Black Hat Europe 2025 | **Licencia**: Apache 2.0 | **Repositorio**: [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard)

---

## ⚡ Los 5 Motores de Escaneo Especializados

A.I.G descompone la seguridad de la IA en 5 escáneres modulares independientes que pueden ejecutarse vía CLI ligero (`pip`) o mediante su dashboard centralizado en Docker (`:8088`):

### 1. 🔌 `aig-mcp-scan` (Auditor de Servidores MCP)
- Escanea el código fuente de cualquier servidor MCP o se conecta a uno en vivo para auditar si expone vulnerabilidades de ejecución arbitraria de comandos, inyecciones en tools o fuga de tokens.
- Salida en formato estándar SARIF / JSON.
```bash
pip install aig-mcp-scan
aig-mcp-scan --repo /ruta/al/mcp-server -o resultado.sarif.json
```

### 2. 🧩 `aig-skill-scan` (Auditor de Agent Skills)
- Analiza carpetas de skills de agentes (`SKILL.md`) en busca de inyecciones de prompt maliciosas, permisos abusivos o dependencias inseguras.
```bash
pip install aig-skill-scan
aig-skill-scan --repo /ruta/a/skills/mi-skill -o resultado.sarif.json
```

### 3. 🖥️ `aig-infra-scan` (Escáner de Infraestructura de IA)
- Reconocimiento de huellas y vulnerabilidades conocidas (CVEs) en motores de inferencia locales y plataformas de IA expuestas (*Ollama, vLLM, ComfyUI, Triton, Ray, etc.*).
```bash
pip install aig-infra-scan
aig-infra-scan -t https://ai-server.empresa.local
```

### 4. 🧠 `aig-model-scan` (Evaluación de Jailbreaks y Seguridad de LLMs)
- Lanza baterías automatizadas de ataques adversariales multi-turno (*Many-Shot, PAIR, GOAT, ActorAttack*) para medir la resistencia de un modelo o asistente antes de desplegarlo en producción.

### 5. 🤖 `agent-scan` (Seguridad de Flujos y Multiagentes)
- Evaluación de arquitecturas agentic corporativas (Dify, Coze, LangChain) conforme al **OWASP Top 10 for Agentic Applications**.

---

## 🚀 Despliegue de la Plataforma Completa (Web UI :8088)
```bash
# Vía Docker Compose (cuando se requiera la suite gráfica completa):
git clone https://github.com/Tencent/AI-Infra-Guard.git
cd AI-Infra-Guard
docker compose -f docker-compose.images.yml up -d
# Dashboard accesible en http://localhost:8088
```

---

## 🎯 Sinergia con Nuestro Ecosistema
1. **Auditoría de Nuestras Propias Skills y Servidores MCP**:
   Podemos usar `aig-skill-scan` y `aig-mcp-scan` para pasar control de calidad de seguridad sobre las 166 skills y los 10 servidores MCP que tenemos montados.
2. **Catalogada en la Capa 2 / 3 del Arsenal Hub**:
   Integrada en [[03-Herramientas/Harness-Engineering/Plan-Despliegue-Arsenal-Hub-Unificado|Plan de Despliegue del Arsenal Hub Unificado]].

---
*Ficha táctica catalogada en la sección de Harness Engineering y AI Security del Cyber-Vault.*