---
name: bug-bounty-automation-scripts
description: Desarrollo de scripts de automatización custom y canalizaciones de auditoría. Creación de wrappers bash/python, integración de webhooks y filtrado de respuestas.
---

# Skill: Automation Scripts & Custom Tooling

Esta habilidad instruye al agente sobre cómo desarrollar scripts de automatización a medida (en Bash y Python) para canalizar y filtrar salidas de herramientas CLI sin generar ruido o solapamientos.

## 📌 Principios de Automatización de Auditoría

### 1. Modulario y Reutilización
- Crear scripts independientes que acepten entradas por tuberías de UNIX (`stdin`) y emitan resultados limpios (`stdout`).

### 2. Integración de Alertas (Slack/Discord Webhooks)
- Notificar automáticamente al investigador cuando se descubra un activo nuevo o una vulnerabilidad de severidad alta mediante webhooks HTTP POST.

---

## 📚 Referencias Técnicas

Consulta las plantillas en:
[automation-templates.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-automation-scripts/references/automation-templates.md)
