---
name: bug-bounty-xss
description: Detección, explotación y bypass de filtros para vulnerabilidades Cross-Site Scripting (XSS Reflejado, Almacenado, DOM, XSSI, HTML Injection). Incluye referencias a write-ups célebres de Google, Uber, Yahoo y Facebook.
---

# Skill: Cross-Site Scripting (XSS) & Front-End Injection Attacks

Esta habilidad instruye al agente en el análisis exhaustivo de vulnerabilidades XSS (Reflected, Stored, DOM-based, XSSI), evasión de filtros (WAF, CSP, JSON encoding), sondeo contextual mediante canarios y verificación en navegador real con Playwright para eliminar falsos positivos.

---

## 🔬 Metodología de Detección en 3 Pasos (Zero False-Positive)

### 1. Sondeo Canario & Matriz de Caracteres Especiales
Antes de enviar un payload ruidoso que alerte al WAF, inyectar un token canario único y evaluar cuáles de los siguientes caracteres son reflejados sin escapar:
```text
'  "  <  >  /  ;  (  )  {  }  =  `
```
* Si `< >` están filtrados pero `' "` y `( )` pasan: Enfocar en **Inyección en Atributos** o **Contexto JavaScript**.
* Si todos los delimitadores HTML pasan: Proceder con inyección directa en el cuerpo del documento.

### 2. Clasificación Sintáctica del Contexto
* **HTML Body**: `<script>alert(1)</script>`, `<img src=x onerror=alert(1)>`, `<svg onload=alert(1)>`.
* **Atributos HTML**: `" onfocus="alert(1)" autofocus="`, `javascript:alert(1)`.
* **Bloques JavaScript (`<script>`)**: `'-alert(1)-'`, `";alert(1);//`, `</script><svg onload=alert(1)>`.
* **Fragmentos Hash en SPAs (React/Vue/Angular)**: Inyección en `location.hash` / routers del lado del cliente (`#payload`).

### 3. Verificación Real con Motor Headless (Playwright / XSSRush)
No considerar un XSS confirmado únicamente por coincidencia de texto en la respuesta HTTP:
* Ejecutar en navegador real y escuchar el evento de diálogo:
  ```python
  page.on("dialog", lambda dialog: dialog.accept())
  ```
* Utilizar la herramienta nativa integrada en el repositorio:
  ```bash
  xssrush.cmd -u "https://target.com/page?id=test" --scan all
  ```

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
[xss-vectors-and-writeups.md](references/xss-vectors-and-writeups.md)
