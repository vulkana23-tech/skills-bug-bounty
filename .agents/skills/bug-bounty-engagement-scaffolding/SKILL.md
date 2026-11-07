---
name: bug-bounty-engagement-scaffolding
description: Metodología y automatización para la creación estructurada de directorios de trabajo de auditoría (engagement workspaces), seguimiento de evidencias y notas de prueba.
---

# Skill: Bug Bounty Engagement Workdir Scaffolding

Esta habilidad proporciona una metodología estándar para inicializar entornos de trabajo estructurados durante auditorías y programas de Bug Bounty.

## 📁 Estructura del Directorio de Engagement

```
engagement-[target]/
├── scope.md             # Límites de autorización y objetivos en alcance
├── notes.md             # Notas de avance, hipótesis y hallazgos
├── report.md            # Borrador final del informe de vulnerabilidades
├── scans/               # Resultados de subfinder, nmap, httpx, nuclei
├── evidence/            # Capturas de pantalla, respuestas HTTP y registros
└── poc/                 # Scripts de prueba de concepto (PoC) benignos
```

---

## 📚 Referencias Técnicas

Consulta la plantilla de andamiaje en:
[engagement-workspace-template.md](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-engagement-scaffolding/references/engagement-workspace-template.md)
