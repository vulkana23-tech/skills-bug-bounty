---
name: bug-bounty-js-reverse-deobfuscation
description: Metodología de análisis e ingeniería inversa de código JavaScript ofuscado. Desempaquetado Webpack, deofuscación con AST (Babel), bypass de anti-debugging y extracción de algoritmos de firma API.
---

# Skill: JavaScript Reverse Engineering & Deobfuscation

Esta habilidad capacita al agente para revertir ofuscaciones en scripts JS cliente, analizar bundles compilados y recuperar algoritmos de firma y parámetros de seguridad.

## 📌 Metodología de Deofuscación

### 1. Identificación del Tipo de Ofuscación
- **Packers**: Webpack, Browserify, Rollup bundles.
- **Obfuscator Types**: Obfuscator.io (variables Hex, cadenas codificadas en arrays), JSFuck, AAEncode, JJEncode.

### 2. Análisis AST (Abstract Syntax Tree)
- Uso de `@babel/parser` y `@babel/traverse` para:
  - Evaluar expresiones constantes simples (p. ej. `'a' + 'b'` -> `'ab'`).
  - Simplificar arrays de cadenas codificadas en Base64/Hex.
  - Renombrar identificadores aleatorios a nombres significativos.

### 3. Bypass de Anti-Debugging
- Sobrescribir constructores `Function("debugger")` o métodos `console.log` modificados por el script.

---

## 📚 Referencias Técnicas

Consulta la guía técnica de AST y deofuscación en:
[js-deobfuscation-guide.md](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-js-reverse-deobfuscation/references/js-deobfuscation-guide.md)
