---
name: bug-bounty-response-diffing-filtering
description: Algoritmo de comparación estructural y filtrado inteligente de respuestas en Turbo Intruder. Descarte automatizado de respuestas "aburridas" o repetitivas.
---

# Skill: Intelligent Response Diffing & Filtering

Esta habilidad capacita al agente para aplicar algoritmos de diferenciación estructural (diffing) en Turbo Intruder, ocultando miles de respuestas idénticas y resaltando únicamente las anómalas.

## 📌 Principio del Algoritmo Diffing

- Compara el árbol HTML, encabezados y código de estado de cada respuesta recibida con una muestra base de respuestas neutras, marcando como `interested=True` solo aquellas que difieren estructuralmente.

---

## 📚 Referencias Técnicas

Consulta los detalles en:
[diffing-algorithm-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-response-diffing-filtering/references/diffing-algorithm-guide.md)
