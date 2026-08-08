# OWASP Top 10 for LLM & Remediation Reference

## 1. Riesgos de Seguridad en LLMs

1. **Prompt Injection**: Anulación de las salvaguardas del modelo para extraer secretos del sistema o ejecutar acciones no autorizadas.
2. **Exposición de Datos Sensibles**: Fuga de datos de entrenamiento o secretos organizacionales incrustados en el contexto del modelo.
3. **Poisoning de Datos de Entrenamiento**: Inserción de datos maliciosos durante la fase de ajuste fino (`Fine-tuning`).

## 2. Remediación Segura

- Aplique capas estricta de validación e inspección tanto en la entrada (`Input Guardrails`) como en la salida (`Output Sanitization`).
- Trate las salidas generadas por los LLM como contenido no confiable de terceros antes de pasarlas a evaluadores como `eval()`, consultas SQL o renderizadores HTML.
- Utilice el principio de mínimo privilegio en las herramientas y llamadas a funciones (`Function Calling` / `Plugins`) otorgadas al agente de IA.
