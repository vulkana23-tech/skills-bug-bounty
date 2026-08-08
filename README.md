# Bug Bounty & Security Skills Collection for OpenCode & Claude Code

Colección completa y estructurada de **30 Agent Skills** diseñadas para **OpenCode**, **Claude Code** y asistentes basados en agentes de IA (como Antigravity y Cursor). Esta suite integra las mejores fuentes y repositorios de ciberseguridad de la comunidad (`ngalongc/bug-bounty-reference`, `awesome-bug-bounty`, `reddelexc/hackerone-reports`, `swisskyrepo/PayloadsAllTheThings` y `EdOverflow/bugbounty-cheatsheet`).

---

## 📁 Estructura del Repositorio

```
bug-bounty-skills/
├── README.md                           # Guía principal de uso e integración
├── skills.json                         # Registro de 30 skills para importación automática
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
    └── bug-bounty-content-injection/   # Content Injection & Text Spoofing
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

## 💡 Catálogo Completo de Habilidades (30 Agent Skills)

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

---

## 📄 Licencia & Créditos
Basado en los repositorios de ciberseguridad:
- `ngalongc/bug-bounty-reference`
- `djadmin/awesome-bug-bounty`
- `reddelexc/hackerone-reports`
- `swisskyrepo/PayloadsAllTheThings`
- `EdOverflow/bugbounty-cheatsheet`
