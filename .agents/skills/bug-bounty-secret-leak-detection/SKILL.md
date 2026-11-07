---
name: bug-bounty-secret-leak-detection
description: Detección automatizada de secretos expuestos en código fuente y repositorios. Escaneo de tokens de API, JWTs, claves AWS y credenciales con trufflehog, gitleaks y secretfinder.
---

# Skill: Secret Leak Detection & Repository Scanning

Esta habilidad capacita al agente para auditar repositorios de código fuente, código cliente JavaScript compilado y conjuntos de archivos de configuración en búsqueda de credenciales expuestas y claves de API privadas.

## 📌 Reglas de Detección de Secretos

### 1. Claves Criptográficas y de Proveedores Cloud
- **AWS Key**: `AKIA[0-9A-Z]{16}`
- **GitHub Personal Access Token**: `ghp_[a-zA-Z0-9]{36}`
- **Slack Webhook URL**: `https://hooks.slack.com/services/T[a-zA-Z0-9_]+/B[a-zA-Z0-9_]+/[a-zA-Z0-9_]+`

---

## 📚 Referencias Técnicas

Consulta las reglas completas en:
[secret-scanning-rules.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-secret-leak-detection/references/secret-scanning-rules.md)
