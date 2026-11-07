---
name: bug-bounty-request-smuggling
description: Diagnóstico de vulnerabilidades HTTP Request Smuggling (CL.TE, TE.CL, TE.TE), desincronización de proxies/servidores de frontend y backend, y secuestro de peticiones.
---

# Skill: HTTP Request Smuggling & Desync Assessment

Esta habilidad capacita al agente para evaluar discrepancias entre cómo el proxy/frontend reverse proxy y el servidor de backend procesan los encabezados HTTP `Content-Length` (CL) y `Transfer-Encoding` (TE).

## 📌 Variantes Principales

### 1. CL.TE (Frontend usa Content-Length, Backend usa Transfer-Encoding)
- La petición HTTP incluye ambos encabezados. El frontend lee el tamaño indicado por `Content-Length`, mientras que el backend procesa el cuerpo codificado en bloques (`chunked`).

### 2. TE.CL (Frontend usa Transfer-Encoding, Backend usa Content-Length)
- El frontend lee el paquete chunked hasta el bloque final `0`, mientras que el backend solo procesa los bytes indicados por `Content-Length`, dejando el resto en el búfer para la siguiente solicitud.

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[smuggling-desync.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-request-smuggling/references/smuggling-desync.md)
