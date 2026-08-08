---
name: bug-bounty-ai-redteaming
description: Evaluación de seguridad en modelos de Inteligencia Artificial (LLM Top 10 OWASP). Diagnóstico de Prompt Injection, Jailbreaking, Data Poisoning y sanitización de respuestas en aplicaciones basadas en IA.
---

# Skill: AI & LLM Security Assessment

Esta habilidad capacita al agente para evaluar aplicaciones que integran modelos de lenguaje (LLM) e inteligencia artificial, identificando riesgos de inyección de prompts, fugas de datos de entrenamiento y procesamiento inseguro de salidas.

## 📌 Principales Riesgos OWASP para LLMs

### 1. Prompt Injection (Directa e Indirecta)
- **Directa**: Manipulación deliberada de la instrucción del usuario para sobreescribir las reglas del sistema (`System Prompt`).
- **Indirecta**: Inyección de instrucciones ocultas dentro de documentos externos, webs o archivos consumidos por el modelo (ej. PDFs, emails).

### 2. Insecure Output Handling (Procesamiento Inseguro de Salidas)
- Ocurre cuando la salida generada por el LLM se pasa directamente a funciones del navegador o del servidor sin sanitizar (derivando en XSS, RCE o SQLi).

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[llm-top10.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-ai-redteaming/references/llm-top10.md)
