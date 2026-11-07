---
name: bug-bounty-nuclei-template-authoring
description: Creación y diseño de plantillas declarativas YAML para Nuclei. Definición de peticiones HTTP/DNS/TCP, extractores de expresiones regulares (Regex), matchers y dorks.
---

# Skill: Nuclei Template Authoring & Custom Rule Design

Esta habilidad capacita al agente para escribir y validar plantillas YAML declarativas para el escáner Nuclei, permitiendo automatizar la detección de vulnerabilidades recién descubiertas mediante patrones de solicitud y respuesta.

## 📌 Estructura de una Plantilla Nuclei

```yaml
id: custom-xss-detection

info:
  name: Reflected XSS Parameter Test
  author: auditor
  severity: medium
  description: Detects reflected XSS in search parameter.

http:
  - method: GET
    path:
      - "{{BaseURL}}/?q=<script>alert(document.domain)</script>"

    matchers-condition: and
    matchers:
      - type: word
        words:
          - "<script>alert(document.domain)</script>"
        part: body

      - type: status
        status:
          - 200
```

---

## 📚 Referencias Técnicas

Consulta la guía de diseño en:
[nuclei-yaml-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-nuclei-template-authoring/references/nuclei-yaml-guide.md)
