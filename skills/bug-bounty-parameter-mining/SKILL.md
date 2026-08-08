---
name: bug-bounty-parameter-mining
description: Descubrimiento masivo de parámetros ocultos (Parameter Mining) y extracción de endpoints en código fuente JavaScript. Uso de arjun, x8, Param Miner y JS analyzers.
---

# Skill: Parameter Mining & Endpoint Extraction

Esta habilidad capacita al agente para descubrir parámetros no documentados en solicitudes GET/POST/JSON y extraer rutas de API ocultas analizando archivos JavaScript estáticos bundle.

## 📌 Metodología de Descubrimiento de Parámetros

### 1. Parameter Fuzzing con Arjun / x8
- Probar parámetros no expuestos en la interfaz de usuario que puedan activar funciones avanzadas o de depuración (`debug=true`, `admin=1`, `test=1`, `enable_feature=1`).

### 2. Extracción de Endpoints en JavaScript
- Analizar archivos `.js` descargados mediante expresiones regulares para identificar rutas de API no expuestas en el HTML principal.

---

## 📚 Referencias Técnicas

Consulta los detalles en:
[param-discovery-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-parameter-mining/references/param-discovery-guide.md)
