---
name: bug-bounty-crlf-injection
description: Detección y mitigación de vulnerabilidades CRLF Injection (Carriage Return Line Feed) y HTTP Response Splitting. Inyección de cabeceras arbitrarias (Set-Cookie) y XSS via CRLF.
---

# Skill: CRLF Injection & HTTP Response Splitting

Esta habilidad capacita al agente para identificar y evaluar vulnerabilidades donde una aplicación web concatena entradas no sanitizadas del usuario dentro de los encabezados de respuesta HTTP utilizando secuencias de retorno de carro y salto de línea (`\r\n` o `%0d%0a`).

## 📌 Vectores de Diagnóstico

### 1. Inyección de Cabeceras HTTP
- Inyectar `%0d%0aSet-Cookie:%20session=evil_session` en parámetros reflejados en encabezados (ej. `Location`, `Set-Cookie`, `X-Custom-Header`).
- Solicitud de prueba:
  `GET /redirect?url=http://example.com%0d%0aSet-Cookie:%20injected=true HTTP/1.1`

### 2. HTTP Response Splitting (Inyección de Cuerpo HTML/XSS)
- Inyectar dos secuencias CRLF consecutivas (`%0d%0a%0d%0a`) para finalizar los encabezados HTTP e iniciar un cuerpo de respuesta inyectado:
  `GET /?lang=en%0d%0a%0d%0a<html><body>Injected</body></html>`

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[crlf-bypasses.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-crlf-injection/references/crlf-bypasses.md)
