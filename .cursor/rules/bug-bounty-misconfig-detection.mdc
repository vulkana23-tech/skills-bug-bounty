---
name: bug-bounty-misconfig-detection
description: Detección automatizada de malas configuraciones de servidor web con Nuclei. Detección de archivos .git expuestos, directorios con permisos de listado, SSL/TLS obsoletos y cabeceras de seguridad faltantes.
---

# Skill: Automated Server Misconfiguration Detection

Esta habilidad capacita al agente para auditar configuraciones de servidor web defectuosas mediante plantillas Nuclei especializadas en la detección de archivos de control de versiones expuestos, listado de directorios e inconsistencias de seguridad.

## 📌 Principales Malas Configuraciones Detectables

### 1. Directorios `.git` y `.env` Expuestos
```bash
nuclei -l targets.txt -tags git,env,exposure -silent
```

### 2. Cabeceras de Seguridad Faltantes
- Verificación de ausencia de `Strict-Transport-Security` (HSTS), `Content-Security-Policy` (CSP) o `X-Frame-Options`.

---

## 📚 Referencias Técnicas

Consulta los detalles en:
[misconfig-rules.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-misconfig-detection/references/misconfig-rules.md)
