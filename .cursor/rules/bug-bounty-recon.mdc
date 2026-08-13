---
name: bug-bounty-recon
description: Metodología avanzada de reconocimiento, descubrimiento de activos, enumeración de subdominios y mapeo de superficie expuesta para Bug Bounty. Utilizar al iniciar una auditoría sobre un objetivo web o dominio.
---

# Skill: Bug Bounty Reconnaissance & Asset Discovery

Esta habilidad guía al agente en las fases de reconocimiento pasivo y activo, mapeo de infraestructura, descubrimiento de subdominios, extracción de URLs/endpoints de archivos JavaScript y fingerprinting de tecnologías.

## 📌 Guía de Inicio Rápido

Cuando el usuario solicite realizar un recon o mapear un objetivo:
1. **Reconocimiento Pasivo**: Consultar registros ASN, certificaciones SSL/TLS (Certificate Transparency logs via `crt.sh`), registros DNS históricos y VirusTotal.
2. **Enumeración de Subdominios**: Combinar técnicas de fuerza bruta con listas de palabras y consultas de fuentes públicas.
3. **Mapeo de Endpoints & JavaScript Mining**: Analizar archivos JS estáticos para extraer rutas de API, tokens expuestos y parámetros ocultos.
4. **Fingerprinting & Content Discovery**: Identificar tecnologías (Wappalyzer, HTTP headers), versiones de CMS y servidores web.

---

## 🛠️ Metodología por Pasos

### Paso 1: Mapeo de Organización y ASN
- Identificar rangos IP y ASN de la empresa.
- Buscar dominios raíz asociados, adquisiciones y marcas secundarias en registros WHOIS.

### Paso 2: Enumeración de Subdominios (Passive & Active)
- **Fuentes pasivas**: `crt.sh`, `sublist3r`, `amass`, `alienvault`, `hackertarget`.
- **Fuerza Bruta DNS**: Uso de resolutores masivos y diccionarios de subdominios (`commonspeak2`, `all.txt`).
- **Permutación y alteración de subdominios**: Uso de palabras clave como `dev`, `staging`, `test`, `api`, `internal`, `admin`, `v1`, `v2`, `beta`.

### Paso 3: Identificación de Servicios Activos y Puertos (Port Scanning)
- Escaneo de puertos comunes HTTP/HTTPS y servicios de administración (80, 443, 8080, 8443, 8000, 8888, 3000, 9000).
- Verificación de Subdomain Takeover (CNAME huérfanos apuntando a S3, GitHub Pages, Heroku, Azure, Surge, etc.).

### Paso 4: Extracción de Parámetros y Endpoints de JavaScript
- Descargar y analizar archivos `.js` bundle (Webpack, Vite, React, Angular).
- Extraer expresiones regulares de URLs, claves API, credenciales hardcoded y endpoints no documentados.

---

## 📚 Documentación de Referencia

Para consultar la lista detallada de herramientas, comandos exactos y lista de comprobación de Subdomain Takeover, lee la guía de referencia:
[recon-checklist.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-recon/references/recon-checklist.md)
