---
name: bug-bounty-subdomain-osint-enum
description: Enumeración pasiva de subdominios utilizando fuentes OSINT y motores de búsqueda (Google, Bing, Baidu, Ask, Netcraft, VirusTotal, ThreatCrowd, DNSdumpster).
---

# Skill: OSINT Subdomain Enumeration

Esta habilidad capacita al agente para recopilar subdominios pertenecientes a un dominio objetivo mediante la consulta pasiva de fuentes de datos de inteligencia pública (OSINT) sin enviar tráfico directo a la infraestructura del cliente.

## 📌 Fuentes de Inteligencia Pasiva

### 1. Motores de Búsqueda Públicos
- Consultar índices de búsqueda utilizando operadores de exclusión: `site:target.com -www`.

### 2. Plataformas de Seguridad y Reputación DNS
- **VirusTotal API / DNSdumpster / Netcraft / ThreatCrowd**: Extracción de registros de resolvedores pasivos e historial de resoluciones IP.

---

## 📚 Referencias Técnicas

Consulta la matriz de fuentes en:
[osint-sources-matrix.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-subdomain-osint-enum/references/osint-sources-matrix.md)
