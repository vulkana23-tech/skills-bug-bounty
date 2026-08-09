---
name: bug-bounty-graph-database-analytics
description: Análisis de grafos de infraestructura con la base de datos de Amass (`amass db`). Visualización de relaciones entre dominios, subdominios, direcciones IP y certificados.
---

# Skill: Graph Database Analytics with Amass DB

Esta habilidad capacita al agente para interactuar con la base de datos basada en grafos de Amass, realizando consultas de relación, visualizaciones de infraestructura y seguimiento histórico de cambios en la superficie de ataque.

## 📌 Consultas y Exportaciones de Amass DB

### 1. Inspección de Resultados Guardados (`amass db`)
- Listar los activos descubiertos en la sesión actual:
  `amass db -show -d target.com`

### 2. Exportación a Formato de Grafos (Vis.js / Graphviz)
- Generar diagramas de red visuales:
  `amass viz -vizjs -d target.com`

---

## 📚 Referencias Técnicas

Consulta las consultas en:
[amass-db-queries.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-graph-database-analytics/references/amass-db-queries.md)
