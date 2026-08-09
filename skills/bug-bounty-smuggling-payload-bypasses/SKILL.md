---
name: bug-bounty-smuggling-payload-bypasses
description: Evasión de filtros WAF en HTTP Request Smuggling. Uso de caracteres nulos, tabulaciones, saltos de línea inusuales y mutaciones Mayúsculas/Minúsculas.
---

# Skill: Request Smuggling WAF Bypasses

Esta habilidad capacita al agente para formular variaciones de payloads de desincronización que evadan la inspección estricta de WAFs (Web Application Firewalls) mediante la inclusión de delimitadores no estándar.

## 📌 Evasiones Comunes de Encabezados

- `Transfer-Encoding: \tchunked`
- `Transfer-Encoding\x00: chunked`
- `X: X\rTransfer-Encoding: chunked`

---

## 📚 Referencias Técnicas

Consulta los bypasses en:
[smuggling-waf-bypasses.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-smuggling-payload-bypasses/references/smuggling-waf-bypasses.md)
