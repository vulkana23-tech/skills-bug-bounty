---
name: bug-bounty-xss
description: Detección, explotación y bypass de filtros para vulnerabilidades Cross-Site Scripting (XSS Reflejado, Almacenado, DOM, XSSI, HTML Injection). Incluye referencias a write-ups célebres de Google, Uber, Yahoo y Facebook.
---

# Skill: Cross-Site Scripting (XSS) & Front-End Injection Attacks

Esta habilidad instruye al agente en el análisis exhaustivo de vulnerabilidades XSS (Reflected, Stored, DOM-based, XSSI), evasión de filtros (WAF, CSP, JSON encoding) y elevación del impacto de Self-XSS a Stored XSS global.

## 📌 Contextos de Inyección y Metodología

### 1. Inyección en HTML Body
- Buscar caracteres no escapados: `< > ' " `
- **Payload básico**: `<script>alert(domain)</script>`
- **Payload sin `<script>`**: `<img src=x onerror=alert(domain)>`, `<svg onload=alert(domain)>`

### 2. Inyección dentro de Atributos HTML
- Si está encerrado en comillas dobles: `" onfocus="alert(1)" autofocus="`
- Si está en atributios `href` / `src`: `javascript:alert(document.cookie)`

### 3. Inyección en Contexto JavaScript / Script Block
- Romper el string actual: `';alert(1);//` o `"-alert(1)-"`
- Romper la etiqueta script actual: `</script><img src=x onerror=alert(1)>`

### 4. DOM-Based XSS & Sink Analysis
- **Sources peligrosos**: `location.search`, `location.hash`, `document.referrer`, `window.name`, `postMessage`.
- **Sinks peligrosos**: `eval()`, `innerHTML`, `document.write()`, `element.src`, `$.html()`, `setTimeout()`.

---

## 🛠️ Elevación de Impacto (Escalación)

1. **Self-XSS a Stored XSS**:
   - Combinar con CSRF para inyectar el payload en el perfil de la víctima.
   - Combinar con OAuth / Login CSRF o Clickjacking.
2. **Bypass de CSP (Content Security Policy)**:
   - Abusar de endpoints JSONP en dominios permitidos (Google, Yahoo, etc.).
   - Utilizar Polyglots e inyección de Gadgets JS.

---

## 📚 Write-ups de Referencia Real (`ngalongc/bug-bounty-reference`)

Consulta la base de datos de casos reales expuesta en:
[xss-vectors-and-writeups.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-xss/references/xss-vectors-and-writeups.md)
