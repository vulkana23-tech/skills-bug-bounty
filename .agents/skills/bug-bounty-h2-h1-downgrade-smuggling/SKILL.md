---
name: bug-bounty-h2-h1-downgrade-smuggling
description: HTTP/2 a HTTP/1.1 Downgrade Smuggling. Explotación de discrepancias cuando proxies frontales aceptan HTTP/2 y traducen la comunicación a HTTP/1.1 en servidores backend.
---

# Skill: HTTP/2 to HTTP/1.1 Downgrade Smuggling

Esta habilidad capacita al agente para identificar y auditar vulnerabilidades derivadas del proceso de "downgrade" (traducción de protocolo) entre servidores frontales que aceptan HTTP/2 y servidores backend que se comunican internamente en HTTP/1.1.

## 📌 Vectores de H2 Downgrade

### 1. Inyección de Encabezados HTTP/1.1 en Tramas H2
- Inyectar saltos de línea `\r\n` dentro de pseudo-encabezados o valores de encabezados HTTP/2 (ej. `:path` o `Foo: Bar\r\nTransfer-Encoding: chunked`).

---

## 📚 Referencias Técnicas

Consulta la guía de remediación en:
[h2-downgrade-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-h2-h1-downgrade-smuggling/references/h2-downgrade-guide.md)
