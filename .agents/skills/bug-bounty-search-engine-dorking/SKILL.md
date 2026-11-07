---
name: bug-bounty-search-engine-dorking
description: Uso avanzado de operadores de motores de búsqueda (Search Engine Dorks) para descubrir paneles expuestos, archivos sensibles, subdominios ocultos e interfaces de administración.
---

# Skill: Search Engine Dorking & Index Analysis

Esta habilidad capacita al agente para formular expresiones de búsqueda avanzadas (Dorks en Google, Bing, DuckDuckGo y Shodan) para exponer información confidencial indexada públicamente por error.

## 📌 Operadores de Dorking Principales

- `site:target.com`: Limita la búsqueda al dominio objetivo.
- `filetype:pdf OR filetype:xls OR filetype:docx`: Filtra documentos internos expuestos.
- `inurl:admin OR inurl:login OR inurl:dashboard`: Descubre paneles administrativos.
- `intitle:"index of"`: Identifica servidores con listado de directorios activo.

---

## 📚 Referencias Técnicas

Consulta los dorks en:
[dorking-cheat-sheet.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-search-engine-dorking/references/dorking-cheat-sheet.md)
