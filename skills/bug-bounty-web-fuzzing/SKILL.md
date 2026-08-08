---
name: bug-bounty-web-fuzzing
description: Estrategia de fuzzing web estructurado. Uso de ffuf, wfuzz y gobuster para descubrimiento de rutas, archivos, encabezados HTTP y parámetros con diccionarios SecLists.
---

# Skill: Structured Web Fuzzing Strategy

Esta habilidad capacita al agente para formular estrategias de fuzzing web precisas sobre endpoints, parámetros y archivos no enlazados, utilizando diccionarios optimizados y filtros de longitud de respuesta.

## 📌 Principios de Fuzzing Eficiente

### 1. Filtrado de Respuestas Falsas
- Descartar respuestas de tamaño uniforme creadas por páginas de error personalizadas (`404` que devuelven `200 OK`):
  `ffuf -u https://target.com/FUZZ -w wordlist.txt -fs 1240`

### 2. Fuzzing de Encabezados HTTP
- Buscar comportamientos anómalos o bypasses inyectando valores en encabezados como `Host: FUZZ.target.com` o `X-Forwarded-For: FUZZ`.

---

## 📚 Referencias Técnicas

Consulta los detalles en:
[fuzzing-methodology.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-web-fuzzing/references/fuzzing-methodology.md)
