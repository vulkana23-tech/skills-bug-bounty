---
name: bug-bounty-js-endpoint-extraction
description: Extracción de endpoints y rutas de API en archivos JavaScript. Parsing AST y expresiones regulares con LinkFinder para descubrir URLs no documentadas.
---

# Skill: JavaScript Endpoint Extraction & Link Mining

Esta habilidad capacita al agente para analizar archivos JavaScript minificados y empacados (Webpack/Vite/Rollup), extrayendo rutas relativas y absolutas de endpoints de API expuestos en el código.

## 📌 Herramientas de Extracción

### 1. LinkFinder & JSParser
```bash
python3 linkfinder.py -i https://target.com/static/js/main.chunk.js -o cli
```

### 2. Extracción Regex Directa
```bash
grep -E -o "(?:\/|\w+\/)[a-zA-Z0-9_?=%&.\/-]+" file.js
```

---

## 📚 Referencias Técnicas

Consulta las reglas en:
[linkfinder-rules.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-js-endpoint-extraction/references/linkfinder-rules.md)
