# HTML & Dangling Markup Remediation Reference

## 1. Riesgos de HTML Injection

Aunque la CSP bloquee la ejecución de JavaScript (`script-src`), la inyección de marcado HTML abierto permite modificar la interfaz visual de la página y exfiltrar contenido privado del usuario (tokens anti-CSRF, claves de API, datos personales) mediante la carga de recursos externos.

## 2. Remediación Segura

- Aplique codificación de entidades HTML (`HTML Entity Encoding`) a todas las variables reflejadas en la vista.
- Configure Content Security Policy (CSP) restringiendo los orígenes de imágenes y marcos: `img-src 'self'`, `default-src 'self'`.
