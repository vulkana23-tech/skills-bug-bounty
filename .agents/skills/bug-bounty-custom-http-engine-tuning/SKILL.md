---
name: bug-bounty-custom-http-engine-tuning
description: Optimización y ajuste fino del motor HTTP personalizado de Turbo Intruder. Configuración de concurrentConnections, requestsPerConnection, pipeline y bajo consumo de memoria.
---

# Skill: Custom HTTP Engine Tuning & Optimization

Esta habilidad capacita al agente para optimizar la velocidad y el rendimiento del motor HTTP en Turbo Intruder, ajustando parámetros de conexión, canalización (pipelining) y reuso de sockets.

## 📌 Parámetros de Configuración del Motor

- `concurrentConnections`: Número de sockets TCP abiertos simultáneamente.
- `requestsPerConnection`: Número de peticiones enviadas por cada conexión TCP reutilizada.
- `pipeline`: Habilita HTTP Pipelining enviando múltiples solicitudes sin esperar las respuestas intermedias.

---

## 📚 Referencias Técnicas

Consulta la matriz de ajuste en:
[engine-tuning-matrix.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-custom-http-engine-tuning/references/engine-tuning-matrix.md)
