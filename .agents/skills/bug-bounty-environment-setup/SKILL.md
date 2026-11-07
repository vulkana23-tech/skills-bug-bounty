---
name: bug-bounty-environment-setup
description: Configuración de entornos de auditoría y automatización. Instalación de Burp Suite/OWASP ZAP, extensiones esenciales, herramientas CLI y flujos de automatización de recon.
---

# Skill: Environment Setup & Tooling Configuration

Esta habilidad guía al agente en la preparación de entornos de trabajo eficientes para pruebas de penetración y auditorías web (Linux/WSL, macOS, Windows).

## 📌 Configuración de Herramientas Esenciales

### 1. Intercepting Proxies (Burp Suite / OWASP ZAP)
- Importar el certificado CA de Burp Suite en el almacén de certificados del navegador para interceptar tráfico HTTPS sin advertencias TLS.
- Configurar reglas de ámbito (Target Scope) para incluir únicamente los dominios autorizados y evitar la captura inútil de tráfico de fondo.

### 2. Extensiones Recomendadas de Burp Suite (BApp Store)
- **Autorize**: Auditoría automatizada de autorización (IDOR/BOLA).
- **Param Miner**: Descubrimiento de parámetros GET/POST no documentados y cabeceras ocultas.
- **Turbo Intruder**: Envío masivo de peticiones HTTP en paralelo para ataques de condiciones de carrera (Race Conditions).

---

## 📚 Referencias Técnicas

Consulta los detalles en:
[tools-config-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-environment-setup/references/tools-config-guide.md)
