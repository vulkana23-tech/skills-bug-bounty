---
name: bug-bounty-dfir-incident-response
description: Auditoría de respuesta a incidentes y forensia digital (DFIR). Análisis de logs del servidor web (Apache, Nginx, IIS), recolección de artefactos digitales y triaje forense.
---

# Skill: DFIR & Incident Response Assessment

Esta habilidad capacita al agente para realizar análisis forense digital y respuesta a incidentes (DFIR), analizando registros de acceso y eventos en servidores web para identificar indicadores de compromiso (IoC) y reconstruir la línea de tiempo de un incidente.

## 📌 Vectores de Análisis Forense

### 1. Análisis de Logs de Servidor Web (Nginx / Apache / IIS)
- Inspeccionar patrones HTTP sospechosos en registros de acceso (`access.log`):
  - Solicitudes masivas a rutas no existentes (escaneo).
  - Presencia de caracteres de inyección (`UNION SELECT`, `../`, `<script>`).
  - Códigos de respuesta HTTP 200 en solicitudes hacia webshells o archivos `.php` subidos en `/uploads/`.

### 2. Triaje de Artefactos del Sistema
- Inspección de procesos activos, conexiones de red abiertas (`netstat`, `ss`), tareas programadas (`cron`, Windows Task Scheduler) y usuarios creados recientemente.

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[dfir-checklist.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-dfir-incident-response/references/dfir-checklist.md)
