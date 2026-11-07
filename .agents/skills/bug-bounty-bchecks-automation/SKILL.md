---
name: bug-bounty-bchecks-automation
description: Automatización con Burp Suite BChecks. Creación de scripts BChecks declarativos para detección automática de bypasses 403, rotación de cabeceras y fallos de seguridad.
---

# Skill: Burp Suite BChecks Automation & Scripting

Esta habilidad capacita al agente para escribir y validar scripts declarativos en formato BChecks para la extensión Burp Suite Scanner, automatizando la auditoría pasiva y activa de vulnerabilidades.

## 📌 Ejemplo de Estructura de BCheck

```bcheck
metadata:
    language: v1-beta
    name: "Custom 403 Bypass Check"
    description: "Inserta cabeceras de omisión en peticiones prohibidas"
    author: "CyberTechAjju"
    tags: "bounty", "bypass", "403"

given request then
    if {latest.response.status_code} matches "403" then
        send request:
            headers:
                "X-Original-URL": {latest.request.url.path}
        
        if {latest.response.status_code} matches "200" then
            report issue:
                severity: high
                confidence: firm
                detail: "Omisión de control de acceso 403 vía X-Original-URL"
        end if
    end if
```

---

## 📚 Referencias Técnicas

Consulta la guía de diseño en:
[bchecks-authoring-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-bchecks-automation/references/bchecks-authoring-guide.md)
