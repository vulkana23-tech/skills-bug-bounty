---
name: bug-bounty-js-file-collection
description: Recolección y descarga automatizada de archivos JavaScript de un objetivo. Uso de subjs, gau, waybackurls y hakrawler para agrupar bundles JS activos e históricos.
---

# Skill: JavaScript File Collection & Gathering Pipeline

Esta habilidad capacita al agente para recopilar y descargar todos los archivos JavaScript (`.js`) servidos por una aplicación web objetivo, combinando consultas históricas y rastreo activo (crawling).

## 📌 Pipeline de Recolección JS

### 1. Extracción Histórica (Wayback Machine / AlienVault OTX)
```bash
echo "target.com" | gau | grep -iE "\.js$" | httpx -silent -mc 200 -o live_js_urls.txt
```

### 2. Crawling Activo con Hakrawler / Subjs
```bash
echo "https://target.com" | hakrawler -js -depth 3 -plain | grep -iE "\.js$" >> live_js_urls.txt
```

---

## 📚 Referencias Técnicas

Consulta la guía de tuberías en:
[js-collection-pipeline.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-js-file-collection/references/js-collection-pipeline.md)
