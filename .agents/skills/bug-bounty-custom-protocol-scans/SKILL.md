---
name: bug-bounty-custom-protocol-scans
description: Escaneo de protocolos no-web (TCP, DNS, SSL, Network) con Nuclei. Detección de relays SMTP abiertos, resolutores DNS vulnerables y certificados SSL caducados.
---

# Skill: Custom Protocol Scanning with Nuclei

Esta habilidad capacita al agente para evaluar protocolos no basados en HTTP (DNS, TCP, SMTP, SSL/TLS, SSH) utilizando el motor de protocolos de Nuclei.

## 📌 Categorías de Escaneo por Protocolo

### 1. Escaneo DNS (Open Resolvers / Zone Transfer)
- Identificar servidores DNS que permiten transferencias de zona AXFR no autorizadas o resolución abierta.

### 2. Escaneo de Certificados SSL/TLS
- Detección de certificados de servidor expirados, autofirmados o con versiones obsoletas de TLS 1.0/1.1.

---

## 📚 Referencias Técnicas

Consulta los detalles en:
[network-protocol-templates.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-custom-protocol-scans/references/network-protocol-templates.md)
