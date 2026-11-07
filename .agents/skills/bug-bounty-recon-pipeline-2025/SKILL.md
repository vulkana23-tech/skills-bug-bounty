---
name: bug-bounty-recon-pipeline-2025
description: Pipeline de Reconocimiento Automatizado 2025. Integración de subfinder, httpx, gau, waybackurls y filtrado de activos HTTP/HTTPS vivos con resolución DNS en tiempo real.
---

# Skill: Modern Reconnaissance Pipeline (2025 Edition)

Esta habilidad capacita al agente para aplicar la metodología moderna de reconocimiento 2025, encadenando herramientas CLI de alto rendimiento para mapear la superficie de ataque de dominios wildcard en minutos.

## 📌 Etapas del Pipeline Moderno

### 1. Subdomain Discovery (Pasivo y Activo)
- Ejecutar descubrimiento pasivo en paralelo: `subfinder -d target.com -all | httpx -silent`
- Cruzar resultados con registros de Certificate Transparency (`crt.sh`) e históricas de URLs (`gau`, `waybackurls`).

### 2. Live Host Probing & HTTP Fingerprinting
- Probar respuestas HTTP/HTTPS vivas filtrando por códigos de estado, títulos de página y hashes Favicon:
  `httpx -l subdomains.txt -title -tech-detect -status-code -mc 200,302,403`

---

## 📚 Referencias Técnicas

Consulta los detalles y comandos en:
[recon-2025-pipeline.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-recon-pipeline-2025/references/recon-2025-pipeline.md)
