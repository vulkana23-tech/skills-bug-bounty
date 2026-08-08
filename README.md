# Bug Bounty & Security Skills Collection for OpenCode & Claude Code

Colección completa y estructurada de **60 Agent Skills** diseñadas para **OpenCode**, **Claude Code** y asistentes basados en agentes de IA (como Antigravity y Cursor). Esta suite integra las mejores fuentes y repositorios de ciberseguridad de la comunidad (`ngalongc/bug-bounty-reference`, `awesome-bug-bounty`, `reddelexc/hackerone-reports`, `swisskyrepo/PayloadsAllTheThings`, `EdOverflow/bugbounty-cheatsheet`, `vitalysim/Awesome-Hacking-Resources`, `nahamsec/Resources-for-Beginner-Bug-Bounty-Hunters`, `The-Art-of-Hacking/h4cker`, `Bug-Bounty-Hunting-Methodology-2025`, `hackThacker/Bug-Bounty-Tools` y `projectdiscovery/nuclei-templates`).

---

## 📁 Estructura del Repositorio

```
bug-bounty-skills/
├── README.md                           # Guía principal de uso e integración
├── skills.json                         # Registro de 60 skills para importación automática
└── skills/
    ├── bug-bounty-recon/               # Reconocimiento, trazado de superficie y discovery
    ├── bug-bounty-xss/                 # Cross-Site Scripting (XSS, XSSI, DOM, HTMLi)
    ├── bug-bounty-sqli/                # Inyección SQL & Exfiltración de datos
    ├── bug-bounty-ssrf/                # Server-Side Request Forgery & Cloud Metadata (AWS/GCP/Azure)
    ├── bug-bounty-idor/                # Insecure Direct Object Reference (IDOR) & API Authz
    ├── bug-bounty-oauth-token/         # Hijacking de Access Tokens, OAuth Flows & Session Flaws
    ├── bug-bounty-rce-deserial/        # Remote Code Execution, Deserialización & Command Injection
    ├── bug-bounty-csrf-logic/          # CSRF, Fallos de Lógica de Negocio & Race Conditions
    ├── bug-bounty-reporting/           # Formato de Reportes de Vulnerabilidad, CVSSv3.1 y Triage
    ├── bug-bounty-xxe/                 # External XML Entity Attack (XXE) & OOB Exfiltration
    ├── bug-bounty-open-redirect/       # Open Redirect Bypasses & Chaining
    ├── bug-bounty-graphql/             # GraphQL Security, Introspección, Aliases & Query Batching
    ├── bug-bounty-subdomain-takeover/  # Subdomain Takeover Fingerprints (S3, GitHub, Azure, Heroku)
    ├── bug-bounty-account-takeover/    # Account Takeover (ATO) Playbook & Vulnerability Matrix
    ├── bug-bounty-ssti/                # Server-Side Template Injection (Jinja2, Twig, Smarty, ERB)
    ├── bug-bounty-lfi-rfi/             # Local/Remote File Inclusion, Path Traversal & PHP Wrappers
    ├── bug-bounty-jwt-security/        # Security Assessment de JWT, Alg: None & Key Confusion
    ├── bug-bounty-file-upload/         # Unrestricted File Upload, Extension Bypasses & Polyglots
    ├── bug-bounty-cve-exploits/        # Matriz de Vulnerabilidades CVEs Conocidos & Parcheo Defensivo
    ├── bug-bounty-cors/                # CORS Misconfigurations, Origin Reflection & Null Origin
    ├── bug-bounty-prototype-pollution/ # Prototype Pollution Client/Server (Node.js & JS)
    ├── bug-bounty-request-smuggling/   # HTTP Request Smuggling (CL.TE, TE.CL, TE.TE) & Desync
    ├── bug-bounty-websockets/          # Seguridad en WebSockets & Cross-Site WebSocket Hijacking
    ├── bug-bounty-html-injection/      # HTML Injection, Dangling Markup & Content Spoofing
    ├── bug-bounty-rate-limit-bypass/   # Evasión de Limitación de Tasa (Rate Limiting) & IP Headers
    ├── bug-bounty-crlf-injection/      # CRLF Injection & HTTP Response Splitting
    ├── bug-bounty-csv-injection/       # CSV / Formula Injection & DDE Execution
    ├── bug-bounty-xslt-injection/      # XSLT Injection & XML Document Reading
    ├── bug-bounty-command-injection/   # OS Command Injection & Filter Bypasses
    ├── bug-bounty-content-injection/   # Content Injection & Text Spoofing
    ├── bug-bounty-ai-redteaming/       # AI & LLM Security (Prompt Injection, OWASP Top 10 for LLMs)
    ├── bug-bounty-osint-threat-intel/  # OSINT, Secretos Expuestos & Threat Intelligence
    ├── bug-bounty-mobile-assessment/   # Seguridad Móvil (Android & iOS, OWASP Mobile Top 10)
    ├── bug-bounty-reverse-engineering/ # Ingeniería Inversa & Auditoría de Binarios
    ├── bug-bounty-privilege-escalation/# Escalación de Privilegios (Linux & Windows)
    ├── bug-bounty-target-selection/    # Selección de Objetivos, Alcance & VDP vs Bounties
    ├── bug-bounty-methodology-playbook/# Playbook Sistemático de Auditoría & Flujo de Trabajo
    ├── bug-bounty-vulnerability-disclosure/# Divulgación Responsable, Safe Harbor & Triage
    ├── bug-bounty-environment-setup/  # Configuración de Entorno, Proxies & Extensiones
    ├── bug-bounty-information-disclosure/# Auditoría de Fuga de Información & Archivos Backup
    ├── bug-bounty-dfir-incident-response/# DFIR, Análisis de Logs de Servidor & Triaje Forense
    ├── bug-bounty-cloud-security-audit/# Auditoría Cloud (AWS, Azure, GCP) & Políticas IAM
    ├── bug-bounty-container-k8s-security/# Seguridad en Contenedores (Docker & Kubernetes RBAC)
    ├── bug-bounty-threat-hunting/      # Caza de Amenazas (SIGMA & YARA Detection Rules)
    ├── bug-bounty-api-security-top10/  # OWASP API Security Top 10 & API Hardening
    ├── bug-bounty-recon-pipeline-2025/ # Pipeline de Reconocimiento Automatizado 2025
    ├── bug-bounty-port-service-discovery/# Descubrimiento Eficiente de Puertos & Servicios No-Web
    ├── bug-bounty-parameter-mining/    # Parameter Mining & Extracción de Endpoints JS
    ├── bug-bounty-business-logic-2025/ # Explotación Avanzada de Lógica de Negocio 2025
    ├── bug-bounty-automation-scripts/  # Custom Scripts & Automatización de Auditoría
    ├── bug-bounty-cms-assessment/      # Auditoría de Vulnerabilidades en CMS (WP, Drupal, Joomla)
    ├── bug-bounty-visual-recon/        # Reconocimiento Visual & Screenshots (Gowitness/Aquatone)
    ├── bug-bounty-secret-leak-detection/# Detección de Secretos Expuestos (Trufflehog/Gitleaks)
    ├── bug-bounty-cloud-s3-audit/      # Auditoría & Descubrimiento de Storage Buckets S3
    ├── bug-bounty-web-fuzzing/         # Fuzzing Web Estratégico & SecLists (FFUF/Wfuzz)
    ├── bug-bounty-nuclei-template-authoring/# Creación de Plantillas Declarativas YAML de Nuclei
    ├── bug-bounty-cve-fast-scanning/   # Escaneo Rápido de CVEs de Alta Severidad con Nuclei
    ├── bug-bounty-misconfig-detection/ # Detección Automatizada de Malas Configuraciones de Servidor
    ├── bug-bounty-exposed-panels-detection/# Descubrimiento & Fingerprinting de Paneles Expuestos
    └── bug-bounty-custom-protocol-scans/# Escaneo de Protocolos No-Web (TCP/DNS/SSL/Network)
```

---

## 🚀 Cómo Usar e Integrar estas Skills

### 1. En OpenCode / Agent Frameworks (.agents/skills)
Copia la carpeta `skills/` en la raíz de tu proyecto dentro de `.agents/skills/` o vincula el archivo `skills.json`:

```bash
# Copiar las skills al workspace actual en OpenCode
cp -r skills/ .agents/skills/
```

### 2. En Claude Code (CLI)
Para hacer que Claude Code reconozca estas habilidades global o localmente:

- **A nivel de proyecto**: Coloca las carpetas de habilidades dentro de `.agents/skills/` o `.claude/skills/` en la raíz del proyecto.
- **A nivel global**: Copia las carpetas en el directorio global de configuración de Claude Code (ej. `~/.claude/skills/`).

### 3. En Antigravity / Agentic IDEs
Puedes añadir la ruta en tu archivo `skills.json` global (`C:\Users\<usuario>\.gemini\config\skills.json` o en `.agents/skills.json`):

```json
{
  "entries": [
    { "path": "./skills" }
  ]
}
```

---

## 💡 Catálogo Completo de Habilidades (60 Agent Skills)

| Skill Name | Descripción |
| :--- | :--- |
| `bug-bounty-recon` | Reconocimiento activo/pasivo, fingerprinting y recolección de endpoints |
| `bug-bounty-xss` | Vectores XSS, WAF/CSP bypasses e índice de reportes top de HackerOne/Google/Uber |
| `bug-bounty-sqli` | Detección y explotación de Inyecciones SQL (Blind, Time-Based, Error, Union, OOB) |
| `bug-bounty-ssrf` | Explotación SSRF y pivotaje hacia endpoints internos y Cloud Metadata (AWS, GCP, Azure) |
| `bug-bounty-idor` | Auditoría de APIs REST/GraphQL para detectar IDOR, BOLA y BFLA |
| `bug-bounty-oauth-token` | Explotación de OAuth 2.0, fuga de Tokens de acceso, postMessage leaks y session hijacking |
| `bug-bounty-rce-deserial` | Identificación de RCE, deserialización insegura (Java, PHP, Python, Node) y command injection |
| `bug-bounty-csrf-logic` | CSRF, inconsistencias de lógica de negocio y Race Conditions (Single-Packet Attack) |
| `bug-bounty-reporting` | Estructuración de reportes de impacto con severidad CVSSv3.1 y pasos de reproducción claros |
| `bug-bounty-xxe` | Ataques XXE, lectura de archivos locales, SSRF via XXE y exfiltración Out-Of-Band |
| `bug-bounty-open-redirect` | Redirecciones abiertas, evasión de filtros y encadenamiento hacia XSS/OAuth Hijacking |
| `bug-bounty-graphql` | Introspección GraphQL, BOLA en mutaciones y bypass de rate limiting via Query Aliases |
| `bug-bounty-subdomain-takeover` | Reclamación de subdominios huérfanos en AWS S3, GitHub Pages, Azure, Heroku, Shopify |
| `bug-bounty-account-takeover` | Playbook integral de secuestro de cuenta (ATO) y matriz de vulnerabilidades |
| `bug-bounty-ssti` | Inyección de plantillas en el servidor (Jinja2, Twig, Smarty, Freemarker, ERB) |
| `bug-bounty-lfi-rfi` | Inclusión de archivos local/remota, directory traversal y wrappers PHP |
| `bug-bounty-jwt-security` | Auditoría de JWT, omisión de firma (alg: none), JKU injection y RS256/HS256 confusion |
| `bug-bounty-file-upload` | Carga de archivos desprotegida, bypasses de extensión/MIME-type y polyglots |
| `bug-bounty-cve-exploits` | Matriz de parches y remediación de CVEs conocidos (Log4Shell, Spring4Shell, Shellshock) |
| `bug-bounty-cors` | CORS Misconfigurations, origin reflection, null origin y credenciales de usuario |
| `bug-bounty-prototype-pollution` | Vulnerabilidades Prototype Pollution Client/Server (Node.js & JavaScript) |
| `bug-bounty-request-smuggling` | HTTP Request Smuggling (CL.TE, TE.CL, TE.TE) y desincronización de solicitudes |
| `bug-bounty-websockets` | Seguridad en conexiones WebSocket y Cross-Site WebSocket Hijacking (CSWSH) |
| `bug-bounty-html-injection` | HTML Injection, Dangling Markup Injection y exfiltración de tokens sin JS |
| `bug-bounty-rate-limit-bypass` | Evasión de controles de Rate Limiting e IP spoofing via encabezados HTTP |
| `bug-bounty-crlf-injection` | CRLF Injection, HTTP Response Splitting y Set-Cookie injection |
| `bug-bounty-csv-injection` | CSV / Formula Injection en hojas de cálculo y ejecución DDE |
| `bug-bounty-xslt-injection` | XSLT Injection, lectura de documentos XML locales y RCE en procesadores |
| `bug-bounty-command-injection` | Inyección de comandos OS, bypass de espacios y blind exfiltration |
| `bug-bounty-content-injection` | Content Spoofing, Text Injection y alteración de UI |
| `bug-bounty-ai-redteaming` | AI & LLM Security Assessment, Prompt Injection y OWASP Top 10 for LLMs |
| `bug-bounty-osint-threat-intel` | OSINT pasivo, investigación de credenciales expuestas y Threat Intelligence |
| `bug-bounty-mobile-assessment` | Auditoría de aplicaciones móviles (Android & iOS, OWASP Mobile Top 10) |
| `bug-bounty-reverse-engineering` | Ingeniería Inversa, descompilación de binarios y protecciones del compilador |
| `bug-bounty-privilege-escalation` | Escalación de privilegios en sistemas operativos Linux (SUID/SUDO) y Windows |
| `bug-bounty-target-selection` | Selección estratégica de objetivos, reglas de compromiso y análisis de alcance |
| `bug-bounty-methodology-playbook` | Playbook sistemático de pruebas, mapeo de funciones y hábitos de auditoría |
| `bug-bounty-vulnerability-disclosure` | Divulgación responsable de vulnerabilidades, Safe Harbor y comunicación profesional |
| `bug-bounty-environment-setup` | Configuración de entorno de auditoría, proxies (Burp/ZAP) y extensiones |
| `bug-bounty-information-disclosure` | Auditoría de fuga de información sensible, stack traces y archivos de respaldo |
| `bug-bounty-dfir-incident-response` | DFIR, análisis de logs de servidor web (Apache, Nginx, IIS) y triaje forense |
| `bug-bounty-cloud-security-audit` | Auditoría de infraestructura en la nube (AWS, Azure, GCP) y políticas IAM |
| `bug-bounty-container-k8s-security` | Seguridad en contenedores Docker y orquestación con Kubernetes RBAC |
| `bug-bounty-threat-hunting` | Caza de amenazas y desarrollo de reglas de detección SIGMA y YARA |
| `bug-bounty-api-security-top10` | Metodología de auditoría OWASP API Security Top 10 y hardening de APIs |
| `bug-bounty-recon-pipeline-2025` | Pipeline de reconocimiento automatizado 2025 (Subfinder, HTTPx, GAU) |
| `bug-bounty-port-service-discovery` | Descubrimiento rápido de puertos y servicios no-web (Naabu/Masscan) |
| `bug-bounty-parameter-mining` | Parameter Mining (Arjun/x8) y extracción de endpoints en JS |
| `bug-bounty-business-logic-2025` | Explotación avanzada de lógica de negocio 2025 (API sync & Payment flows) |
| `bug-bounty-automation-scripts` | Desarrollo de scripts de automatización custom y canalizaciones bash/python |
| `bug-bounty-cms-assessment` | Auditoría de vulnerabilidades en CMS (WordPress, Drupal, Joomla, Magento) |
| `bug-bounty-visual-recon` | Reconocimiento visual y captura automatizada de pantallas (Gowitness/Aquatone) |
| `bug-bounty-secret-leak-detection` | Detección de secretos expuestos en repositorios y JS (Trufflehog/Gitleaks) |
| `bug-bounty-cloud-s3-audit` | Auditoría y descubrimiento especializado de buckets de almacenamiento S3 |
| `bug-bounty-web-fuzzing` | Estrategia de fuzzing web estructurado con FFUF/Wfuzz y SecLists |
| `bug-bounty-nuclei-template-authoring` | Creación y diseño de plantillas declarativas YAML para Nuclei |
| `bug-bounty-cve-fast-scanning` | Escaneo rápido de CVEs de alta severidad con filtros Nuclei |
| `bug-bounty-misconfig-detection` | Detección automatizada de malas configuraciones de servidor con Nuclei |
| `bug-bounty-exposed-panels-detection` | Descubrimiento e identificación de paneles de administración expuestos |
| `bug-bounty-custom-protocol-scans` | Escaneo de protocolos no-web (TCP, DNS, SSL, Network) con Nuclei |

---

## 📄 Licencia & Créditos
Basado en los repositorios de ciberseguridad:
- `ngalongc/bug-bounty-reference`
- `djadmin/awesome-bug-bounty`
- `reddelexc/hackerone-reports`
- `swisskyrepo/PayloadsAllTheThings`
- `EdOverflow/bugbounty-cheatsheet`
- `vitalysim/Awesome-Hacking-Resources`
- `nahamsec/Resources-for-Beginner-Bug-Bounty-Hunters`
- `The-Art-of-Hacking/h4cker`
- `Bug-Bounty-Hunting-Methodology-2025`
- `hackThacker/Bug-Bounty-Tools`
- `projectdiscovery/nuclei-templates`
