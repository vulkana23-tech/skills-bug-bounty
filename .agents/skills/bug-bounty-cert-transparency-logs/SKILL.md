---
name: bug-bounty-cert-transparency-logs
description: Extracción y análisis de registros de Transparencia de Certificados (Certificate Transparency - CT). Descubrimiento de subdominios recién certificados con crt.sh, CertSpotter y Censys.
---

# Skill: Certificate Transparency Logs Analysis

Esta habilidad capacita al agente para consultar los registros públicos e inmutables de emisión de certificados SSL/TLS (Certificate Transparency), descubriendo subdominios activos, entornos de desarrollo y servicios recién desplegados.

## 📌 Consultas a Logs CT

### 1. Registros `crt.sh`
- Extracción JSON de subdominios certificados: `https://crt.sh/?q=%.target.com&output=json`

### 2. Monitoreo en Tiempo Real
- Conexión a streams de CT Logs para recibir alertas inmediatas cuando la organización emite un nuevo certificado SSL/TLS.

---

## 📚 Referencias Técnicas

Consulta los scripts en:
[ct-log-queries.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-cert-transparency-logs/references/ct-log-queries.md)
