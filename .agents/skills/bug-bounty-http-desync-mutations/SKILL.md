---
name: bug-bounty-http-desync-mutations
description: Detección de desincronización HTTP (CL.TE / TE.CL). Mutación de encabezados Content-Length y Transfer-Encoding para identificar desacuerdos de límites entre proxies frontales y backends.
---

# Skill: HTTP Request Desynchronization & Mutations (Smuggler)

Esta habilidad capacita al agente para evaluar vulnerabilidades de HTTP Request Smuggling enviando mutaciones de encabezados de longitud (`Content-Length`) y transferencia (`Transfer-Encoding`), detectando cuando el servidor proxy frontal y el servidor backend interpretan de forma contradictoria los límites de una petición.

## 📌 Categorías de Desincronización

### 1. Vulnerabilidades CL.TE
- El servidor frontal utiliza `Content-Length` y el backend utiliza `Transfer-Encoding`. El atacante envía un cuerpo `chunked` con un bloque secundario "contrabandeado".

### 2. Vulnerabilidades TE.CL
- El servidor frontal utiliza `Transfer-Encoding` y el backend utiliza `Content-Length`.

---

## 📚 Referencias Técnicas

Consulta la matriz de mutaciones en:
[desync-mutations-matrix.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-http-desync-mutations/references/desync-mutations-matrix.md)
