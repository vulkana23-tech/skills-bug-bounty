---
name: bug-bounty-yaml-correlation-rules
description: Motor de reglas de correlación YAML. Definición de reglas estandarizadas para vincular eventos de infraestructura, detectar activos vulnerables y relaciones ocultas.
---

# Skill: YAML Correlation Engine & Rule Design

Esta habilidad capacita al agente para escribir e interpretar reglas de correlación estructuradas en YAML (como las utilizadas por el motor de correlación de SpiderFoot), vinculando múltiples eventos de descubrimiento para identificar riesgos compuestos.

## 📌 Ejemplo de Regla de Correlación YAML

```yaml
name: Exposed Admin Panel with Breached Password
meta:
  author: auditor
  severity: HIGH
  description: Detects exposed administrative interfaces associated with accounts in data breaches.
condition:
  and:
    - event: EXPOSED_ADMIN_PORTAL
    - event: ACCOUNT_IN_DATA_BREACH
```

---

## 📚 Referencias Técnicas

Consulta las especificaciones en:
[correlation-rules-spec.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-yaml-correlation-rules/references/correlation-rules-spec.md)
