---
name: bug-bounty-information-disclosure
description: Detección y evaluación de vulnerabilidades de fuga de información sensible (Information Disclosure). Archivos de respaldo (.bak/.swp), trazas de error (Stack Traces), comentarios HTML/JS y exposición de claves API.
---

# Skill: Information Disclosure Assessment

Esta habilidad capacita al agente para auditar aplicaciones web e interfaces API en búsqueda de fugas inadvertidas de datos sensibles que puedan revelar detalles de arquitectura, credenciales o datos privados de usuarios.

## 📌 Vectores de Fuga de Información

### 1. Archivos Temporales y de Respaldo (.bak, .swp, .old)
- Búsqueda de versiones anteriores de archivos de código fuente creados por editores (ej. Vim, Nano) o scripts de despliegue:
  `index.php.bak`, `config.php.swp`, `web.config.old`, `.env`, `.git/HEAD`.

### 2. Trazas de Error y Mensajes de Depuración (Stack Traces)
- Provocar errores 500 inyectando caracteres malformados en parámetros JSON o numéricos para exponer la estructura interna de rutas de directorio, librerías backend y versiones de software.

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[info-leakage-checklist.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-information-disclosure/references/info-leakage-checklist.md)
