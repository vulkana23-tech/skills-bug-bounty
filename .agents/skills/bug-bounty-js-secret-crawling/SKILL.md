---
name: bug-bounty-js-secret-crawling
description: Rastreo y extracción avanzada de secretos en código JavaScript. Metodología estilo NightCrawler para auditar bundles JS minificados y extraer credenciales expuestas.
---

# Skill: JavaScript Secret Crawling & NightCrawler Methodology

Esta habilidad capacita al agente para rastrear dinámicamente bundles de JavaScript compilados en aplicaciones SPA (React, Angular, Vue), aplicando expresiones regulares avanzadas para extraer credenciales, tokens de API y rutas sensibles.

## 📌 Flujo de Rastreo de Secretos JS

- Descarga de bundles minificados -> Descompilación de Source Maps (`.map`) -> Análisis de AST y Regex -> Validación de tokens activos.

---

## 📚 Referencias Técnicas

Consulta las reglas en:
[nightcrawler-rules.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-js-secret-crawling/references/nightcrawler-rules.md)
