---
name: ai-infra-guard
description: Audita y evalúa la seguridad de servidores MCP, Agent Skills, infraestructuras de IA (Ollama, vLLM, ComfyUI) y modelos LLM frente a jailbreaks usando la suite oficial AI-Infra-Guard (A.I.G) de Tencent Zhuque Lab. Usar cuando el usuario pida auditar un servidor MCP, escanear skills de agentes, buscar vulnerabilidades en endpoints de IA o realizar AI Red Teaming.
---

# Tencent AI-Infra-Guard (A.I.G) — Operaciones de Auditoría de IA y MCP

Suite oficial de seguridad ofensiva y defensiva para ecosistemas de Inteligencia Artificial de Tencent Zhuque Lab.

## Binarios Disponibles en el Entorno
Ruta base del entorno Python:
`C:\Users\logir\Projects\bug-bounty-skills\integrations\cve-mcp-server\.venv\Scripts\`

- `aig-mcp-scan.exe`: Auditoría de servidores Model Context Protocol (MCP) locales o remotos.
- `aig-skill-scan.exe`: Auditoría estática y dinámica de carpetas de Agent Skills (`SKILL.md`).
- `aig-infra-scan.exe`: Escaneo de huellas y CVEs en plataformas de IA (Ollama, vLLM, ComfyUI, etc.).
- `aig-model-scan.exe`: Baterías de jailbreak y evaluación de robustez adversarial de LLMs.

## Comandos Tácticos

### 1. Auditar un Servidor MCP (Buscar fallos de ejecución o fuga de datos)
```bash
C:\Users\logir\Projects\bug-bounty-skills\integrations\cve-mcp-server\.venv\Scripts\aig-mcp-scan.exe --repo "C:\Users\logir\Projects\NetExec-mcp" --language en -o mcp-audit-report.json
```

### 2. Auditar una Skill de Agente (Buscar prompt injection o código inseguro)
```bash
C:\Users\logir\Projects\bug-bounty-skills\integrations\cve-mcp-server\.venv\Scripts\aig-skill-scan.exe --repo "skills/pwn-hunter" --language en -o skill-audit-report.json
```

### 3. Escanear Infraestructura de IA de un Objetivo (Ollama, vLLM, Ray, etc.)
```bash
C:\Users\logir\Projects\bug-bounty-skills\integrations\cve-mcp-server\.venv\Scripts\aig-infra-scan.exe -t "http://target-ip:11434"
```

### 4. Evaluación de Jailbreaks y Robustez de un Modelo LLM
```bash
C:\Users\logir\Projects\bug-bounty-skills\integrations\cve-mcp-server\.venv\Scripts\aig-model-scan.exe --model "deepseek-chat" --base_url "https://api.deepseek.com/v1" --api_key "$KEY" --scenarios Bias --techniques Raw
```