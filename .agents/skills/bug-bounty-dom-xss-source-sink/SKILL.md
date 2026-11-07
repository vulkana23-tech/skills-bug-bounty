---
name: bug-bounty-dom-xss-source-sink
description: Identificación de fuentes (Sources) y sumideros (Sinks) vulnerables a DOM XSS en archivos JavaScript. Inspección de location.search, location.hash, innerHTML, eval y document.write.
---

# Skill: DOM XSS Source-Sink Analysis

Esta habilidad capacita al agente para rastrear el flujo de datos controlado por el usuario desde su origen (`Source`) hasta un punto de ejecución en el navegador (`Sink`), identificando vulnerabilidades de DOM-based Cross-Site Scripting.

## 📌 Principales Sources y Sinks

### 1. Fuentes Inseguras (`Sources`)
- `location.search`, `location.hash`, `document.referrer`, `window.name`, `postMessage`.

### 2. Sumideros Peligrosos (`Sinks`)
- `element.innerHTML`, `document.write()`, `eval()`, `setTimeout()`, `location.href`.

---

## 📚 Referencias Técnicas

Consulta la matriz de pares en:
[dom-xss-matrix.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-dom-xss-source-sink/references/dom-xss-matrix.md)
