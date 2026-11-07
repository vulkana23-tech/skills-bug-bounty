---
name: bug-bounty-7-question-gate
description: Lista de verificación y puerta de calidad de 7 preguntas para la validación rigurosa de hallazgos de seguridad y eliminación de falsos positivos previa a la redacción de informes.
---

# Skill: 7-Question Report Validation Gate

Esta habilidad implementa una puerta de validación en 7 etapas para garantizar que solo se envíen informes de vulnerabilidad legítimos, de alto impacto, verificados y sin falsos positivos.

## 📌 Las 7 Preguntas de Validación

Antes de redactar o finalizar cualquier informe de vulnerabilidad, el agente debe validar afirmativamente cada una de las 7 preguntas:

1. **¿El activo objetivo está 100% dentro del alcance autorizado en `scope.md`?**
2. **¿El impacto de seguridad es real, demostrable y alineado con las reglas del programa?**
3. **¿El hallazgo puede ser ejecutado AHORA MISMO con una solicitud HTTP o CLI práctica y real?**
4. **¿Se ha anonimizado y redactado correctamente cualquier dato sensible (PII, credenciales de usuarios reales) en capturas y registros?**
5. **¿Se ha aislado la causa raíz del problema en lugar de describir únicamente un síntoma superficial?**
6. **¿El vector CVSS v3.1/v4.0 y la severidad VRT están calculados de manera precisa y objetiva?**
7. **¿Las recomendaciones de remediación son claras, accionables y basadas en defensas sólidas?**

---

## 📚 Referencias Técnicas

Consulta la lista de verificación detallada en:
[7-question-gate-checklist.md](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-7-question-gate/references/7-question-gate-checklist.md)
