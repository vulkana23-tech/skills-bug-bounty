---
name: bug-bounty-exposed-panels-detection
description: Detección e identificación de paneles de administración expuestos. Fingerprinting con Nuclei de interfaces como Spring Boot Actuator, phpMyAdmin, Swagger UI, Grafana, Kibana y Jenkins.
---

# Skill: Exposed Admin Panels Detection & Fingerprinting

Esta habilidad capacita al agente para identificar portales de administración, páneles de monitoreo y consolas de desarrollo expuestas a Internet mediante el uso de firmas y favicons en plantillas Nuclei.

## 📌 Principales Paneles Detectables

### 1. Spring Boot Actuator
- Endpoints sensibles: `/actuator/env`, `/actuator/heapdump`, `/actuator/logfile`.

### 2. Swagger UI / OpenAPI Docs
- Endpoints de documentación de API no autenticados: `/swagger-ui.html`, `/v2/api-docs`, `/v3/api-docs`.

---

## 📚 Referencias Técnicas

Consulta los fingerprints en:
[exposed-panels-fingerprints.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-exposed-panels-detection/references/exposed-panels-fingerprints.md)
