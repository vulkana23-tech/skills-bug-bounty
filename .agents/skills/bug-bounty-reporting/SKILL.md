---
name: bug-bounty-reporting
description: Guía de redacción de reportes de vulnerabilidad profesionales para plataformas de Bug Bounty (HackerOne, Bugcrowd, Intigriti, YesWeHack). Cálculo de severidad CVSSv3.1 y estructuración de Proof of Concept (PoC).
---

# Skill: Professional Vulnerability Reporting & Triage

Esta habilidad permite al agente actuar como un auditor de ciberseguridad profesional que redacta o valida reportes de vulnerabilidades para plataformas como HackerOne, Bugcrowd, Intigriti o programas VDP corporativos.

## 📌 Estructura Fundamental de un Reporte Exitoso

Un reporte de calidad debe ser claro, conciso y fácilmente reproducible para evitar estados `Needs More Info` o desestimaciones como `Informational` / `N/A`.

1. **Título Descriptivo**: Resumir la vulnerabilidad, el endpoint afectado y el impacto real.
   - *Mal título*: `XSS en sitio`
   - *Buen título*: `Stored XSS en el campo de comentarios de /profile/settings conduce a filtración de tokens de sesión`
2. **Severidad y Vector CVSSv3.1**: Proporcionar el cálculo exacto de la métrica (ej. `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N` - Score 9.3 Critical).
3. **Resumen de Vulnerabilidad (Summary)**: Descripción concisa del fallo en 2-3 párrafos.
4. **Pasos para Reproducir (Steps To Reproduce)**: Pasos secuenciales 1, 2, 3 numerados sin ambigüedades.
5. **Prueba de Concepto (PoC)**: Código HTTP raw (Burp request/response), script de Python o enlace/video demostrativo.
6. **Impacto Real en el Negocio (Impact)**: Explicar qué puede lograr un atacante con este fallo sin especulaciones infundadas.
7. **Recomendación de Mitigación (Remediation)**: Sugerencias específicas de parcheo (ej. escapado de caracteres, consultas preparadas, cookies SameSite).

---

## 📚 Plantillas de Reportes

Para consultar plantillas predeterminadas para XSS, SQLi, SSRF e IDOR:
[report-templates.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-reporting/references/report-templates.md)
