---
name: bug-bounty-methodology-playbook
description: Playbook de metodología sistemática para pruebas de seguridad en Bug Bounty. Gestión del tiempo, toma de notas estructurada, auditoría por módulos funcionales y rotación de técnicas.
---

# Skill: Bug Bounty Methodology & Testing Playbook

Esta habilidad entrena al agente para estructurar un proceso de auditoría sistemático y repetible, evitando el análisis caótico y maximizando la cobertura funcional del objetivo.

## 📌 Pasos del Flujo de Trabajo (Workflow)

### 1. Mapeo de Funcionalidades (Feature Mapping)
- Crear una cuenta en la aplicación y probar cada función disponible (registro, inicio de sesión, recuperación de contraseña, actualización de perfil, carga de archivos, integración de pagos, roles de equipo).
- Documentar todos los roles de usuario disponibles (Guest, Standard User, Manager, Org Admin).

### 2. Auditoría por Capas de Funcionalidad
- **Autenticación**: Probar OAuth, rate-limiting, tokens de sesión y MFA.
- **Autorización**: Intercambiar tokens de sesión entre roles iguales (IDOR) y roles superiores (BFLA).
- **Procesamiento de Datos**: Inyectar caracteres especiales (`'`, `"`, `<`, `>`, `${}`) en todos los campos de texto e hipervínculos.

---

## 📚 Referencias Técnicas

Consulta los detalles en:
[testing-workflow.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-methodology-playbook/references/testing-workflow.md)
