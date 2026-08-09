# Bug Bounty & Security Skills Collection for OpenCode & Claude Code

Colección completa y estructurada de **100 Agent Skills (Hito Cien)** diseñadas para **OpenCode**, **Claude Code** y asistentes basados en agentes de IA (como Antigravity y Cursor).

> [!TIP]
> **🚀 Carga Ligera Anti-Saturación de IA**: Para evitar consumir excesivos tokens o ralentizar tu asistente de IA cargando las 100 habilidades simultáneamente, puedes importar **Perfiles Especializados (`profiles/*.json`)** que contienen únicamente entre 15 y 30 skills relevantes para tu tarea actual.

---

## ⚡ Guía Rápida: Cómo Seleccionar tu Perfil de Carga

En lugar de vincular el archivo maestro `skills.json` (100 skills), añade a la configuración de tu agente (`.agents/skills.json`) la ruta hacia el perfil que corresponda a tu objetivo actual:

| Perfil | Manifiesto | Nº Skills | Ideal Para |
| :--- | :--- | :---: | :--- |
| **🔍 Recon & OSINT** | [`profiles/profile-recon-osint.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-recon-osint.json) | 25 | Subdominios, ASNs, Certificados, Dorks, SpiderFoot, Amass |
| **🌐 Web & API Audit** | [`profiles/profile-web-api-audit.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-web-api-audit.json) | 30 | XSS, SQLi, IDOR, GraphQL, JWT, JS Recon, SSRF, CORS |
| **☁️ Cloud & DevOps** | [`profiles/profile-cloud-devops.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-cloud-devops.json) | 15 | AWS S3, Docker, Kubernetes RBAC, IAM, Nuclei Fast Scans |
| **🔥 Explotación Avanzada** | [`profiles/profile-advanced-exploitation.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-advanced-exploitation.json) | 19 | Request Smuggling, Turbo Intruder, BChecks, Race Conditions |
| **📱 Mobile, IoT & Binary** | [`profiles/profile-mobile-iot-binary.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-mobile-iot-binary.json) | 11 | Android/iOS, Firmware IoT, Binarios ELF/PE, KYC Deepfakes |
| **📦 Paquete Completo** | [`skills.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills.json) | 100 | Importación completa de las 100 habilidades |

---

## 📁 Estructura del Repositorio

```
bug-bounty-skills/
├── README.md                           # Guía principal e índice de perfiles
├── skills.json                         # Manifiesto Maestro (100 skills)
├── profiles/                           # 🚀 PERFILES DE CARGA SELECCIONADA ANTI-SATURACIÓN
│   ├── profile-recon-osint.json        # Manifiesto de Reconocimiento y OSINT
│   ├── profile-web-api-audit.json      # Manifiesto de Auditoría Web y APIs
│   ├── profile-cloud-devops.json       # Manifiesto Cloud, S3 y Contenedores
│   ├── profile-advanced-exploitation.json# Manifiesto de Explotación Avanzada y Smuggling
│   └── profile-mobile-iot-binary.json  # Manifiesto Móvil, IoT y Binarios
└── skills/                             # 100 Habilidades en formato SKILL.md + references/
```

---

## 💡 Catálogo Completo de Habilidades (100 Agent Skills)

| Skill Name | Perfil | Descripción |
| :--- | :--- | :--- |
| `bug-bounty-recon` | Recon & OSINT | Reconocimiento activo/pasivo, fingerprinting y recolección de endpoints |
| `bug-bounty-xss` | Web & API | Vectores XSS, WAF/CSP bypasses e índice de reportes top |
| `bug-bounty-sqli` | Web & API | Detección y explotación de Inyecciones SQL (Blind, Time, Union, OOB) |
| `bug-bounty-ssrf` | Web & API | Explotación SSRF y pivotaje hacia endpoints internos y Cloud Metadata |
| `bug-bounty-idor` | Web & API | Auditoría de APIs REST/GraphQL para detectar IDOR, BOLA y BFLA |
| `bug-bounty-oauth-token` | Web & API | Explotación de OAuth 2.0, fuga de Tokens de acceso y session hijacking |
| `bug-bounty-rce-deserial` | Explotación | Identificación de RCE, deserialización insegura y command injection |
| `bug-bounty-csrf-logic` | Web & API | CSRF, inconsistencias de lógica de negocio y Race Conditions |
| `bug-bounty-reporting` | Mobile/IoT | Estructuración de reportes de impacto con CVSSv3.1 |
| `bug-bounty-xxe` | Web & API | Ataques XXE, lectura de archivos locales y SSRF OOB |
| `bug-bounty-open-redirect` | Web & API | Redirecciones abiertas, evasión de filtros y encadenamiento |
| `bug-bounty-graphql` | Web & API | Introspección GraphQL, BOLA en mutaciones y Query Aliases |
| `bug-bounty-subdomain-takeover` | Cloud & DevOps | Reclamación de subdominios huérfanos (S3, GitHub, Azure) |
| `bug-bounty-account-takeover` | Web & API | Playbook integral de secuestro de cuenta (ATO) |
| `bug-bounty-ssti` | Web & API | Inyección de plantillas en el servidor (Jinja2, Twig, Smarty, ERB) |
| `bug-bounty-lfi-rfi` | Web & API | Inclusión de archivos local/remota, path traversal y wrappers PHP |
| `bug-bounty-jwt-security` | Web & API | Auditoría de JWT, omisión de firma (alg: none) y JKU injection |
| `bug-bounty-file-upload` | Web & API | Carga de archivos desprotegida, bypasses de extensión y polyglots |
| `bug-bounty-cve-exploits` | Cloud & DevOps | Matriz de parches y remediación de CVEs conocidos |
| `bug-bounty-cors` | Web & API | CORS Misconfigurations, origin reflection y null origin |
| `bug-bounty-prototype-pollution` | Web & API | Vulnerabilidades Prototype Pollution Client/Server (Node.js & JS) |
| `bug-bounty-request-smuggling` | Explotación | HTTP Request Smuggling (CL.TE, TE.CL, TE.TE) y desincronización |
| `bug-bounty-websockets` | Web & API | Seguridad en conexiones WebSocket y Cross-Site WebSocket Hijacking |
| `bug-bounty-html-injection` | Web & API | HTML Injection, Dangling Markup Injection y exfiltración |
| `bug-bounty-rate-limit-bypass` | Web & API | Evasión de controles de Rate Limiting e IP spoofing |
| `bug-bounty-crlf-injection` | Web & API | CRLF Injection, HTTP Response Splitting y Set-Cookie injection |
| `bug-bounty-csv-injection` | Web & API | CSV / Formula Injection en hojas de cálculo y ejecución DDE |
| `bug-bounty-xslt-injection` | Web & API | XSLT Injection, lectura de documentos XML locales y RCE |
| `bug-bounty-command-injection` | Explotación | Inyección de comandos OS, bypass de espacios y blind exfiltration |
| `bug-bounty-content-injection` | Explotación | Content Spoofing, Text Injection y alteración de UI |
| `bug-bounty-ai-redteaming` | Cloud & DevOps | AI & LLM Security Assessment, Prompt Injection y OWASP LLMs |
| `bug-bounty-osint-threat-intel` | Recon & OSINT | OSINT pasivo, investigación de credenciales expuestas y Threat Intel |
| `bug-bounty-mobile-assessment` | Mobile/IoT | Auditoría de aplicaciones móviles (Android & iOS, OWASP Mobile) |
| `bug-bounty-reverse-engineering` | Mobile/IoT | Ingeniería Inversa, descompilación de binarios y protecciones |
| `bug-bounty-privilege-escalation` | Mobile/IoT | Escalación de privilegios en Linux (SUID/SUDO) y Windows |
| `bug-bounty-target-selection` | Recon & OSINT | Selección estratégica de objetivos, reglas de compromiso y alcance |
| `bug-bounty-methodology-playbook` | Mobile/IoT | Playbook sistemático de pruebas, mapeo de funciones y auditoría |
| `bug-bounty-vulnerability-disclosure` | Mobile/IoT | Divulgación responsable de vulnerabilidades y Safe Harbor |
| `bug-bounty-environment-setup` | Cloud & DevOps | Configuración de entorno de auditoría, proxies (Burp/ZAP) |
| `bug-bounty-information-disclosure` | Recon & OSINT | Auditoría de fuga de información sensible y archivos de respaldo |
| `bug-bounty-dfir-incident-response` | Cloud & DevOps | DFIR, análisis de logs de servidor web y triaje forense |
| `bug-bounty-cloud-security-audit` | Cloud & DevOps | Auditoría de infraestructura cloud (AWS, Azure, GCP) e IAM |
| `bug-bounty-container-k8s-security` | Cloud & DevOps | Seguridad en contenedores Docker y Kubernetes RBAC |
| `bug-bounty-threat-hunting` | Cloud & DevOps | Caza de amenazas y desarrollo de reglas SIGMA y YARA |
| `bug-bounty-api-security-top10` | Web & API | OWASP API Security Top 10 y hardening de APIs |
| `bug-bounty-recon-pipeline-2025` | Recon & OSINT | Pipeline de reconocimiento automatizado 2025 (Subfinder, HTTPx) |
| `bug-bounty-port-service-discovery` | Recon & OSINT | Descubrimiento rápido de puertos y servicios no-web (Naabu/Masscan) |
| `bug-bounty-parameter-mining` | Recon & OSINT | Parameter Mining (Arjun/x8) y extracción de endpoints en JS |
| `bug-bounty-business-logic-2025` | Web & API | Explotación avanzada de lógica de negocio 2025 (API sync & Payment) |
| `bug-bounty-automation-scripts` | Explotación | Desarrollo de scripts de automatización custom y canalizaciones bash |
| `bug-bounty-cms-assessment` | Cloud & DevOps | Auditoría de vulnerabilidades en CMS (WordPress, Drupal, Joomla) |
| `bug-bounty-visual-recon` | Recon & OSINT | Reconocimiento visual y screenshots (Gowitness/Aquatone) |
| `bug-bounty-secret-leak-detection` | Recon & OSINT | Detección de secretos expuestos en repositorios y JS (Trufflehog) |
| `bug-bounty-cloud-s3-audit` | Cloud & DevOps | Auditoría y descubrimiento especializado de buckets S3 |
| `bug-bounty-web-fuzzing` | Web & API | Estrategia de fuzzing web estructurado con FFUF/Wfuzz y SecLists |
| `bug-bounty-nuclei-template-authoring` | Cloud & DevOps | Creación y diseño de plantillas declarativas YAML para Nuclei |
| `bug-bounty-cve-fast-scanning` | Cloud & DevOps | Escaneo rápido de CVEs de alta severidad con filtros Nuclei |
| `bug-bounty-misconfig-detection` | Cloud & DevOps | Detección automatizada de malas configuraciones de servidor |
| `bug-bounty-exposed-panels-detection` | Cloud & DevOps | Descubrimiento e identificación de paneles expuestos |
| `bug-bounty-custom-protocol-scans` | Cloud & DevOps | Escaneo de protocolos no-web (TCP, DNS, SSL) con Nuclei |
| `bug-bounty-subdomain-osint-enum` | Recon & OSINT | Enumeración pasiva de subdominios vía OSINT (Sublist3r) |
| `bug-bounty-reverse-dns-mapping` | Recon & OSINT | Mapeo de registros Reverse DNS (PTR) y bloques CIDR |
| `bug-bounty-search-engine-dorking` | Recon & OSINT | Search Engine Dorking avanzado para exposición de paneles |
| `bug-bounty-cert-transparency-logs` | Recon & OSINT | Análisis de logs de transparencia de certificados (crt.sh) |
| `bug-bounty-dns-stochastic-bruteforce` | Recon & OSINT | Fuerza bruta estocástica y permutación de nombres DNS |
| `bug-bounty-attack-surface-mapping` | Recon & OSINT | Mapeo integral de superficie de ataque (OWASP Amass) |
| `bug-bounty-asn-infrastructure-recon` | Recon & OSINT | Reconocimiento de ASNs, prefijos BGP y rangos IP (Amass) |
| `bug-bounty-graph-database-analytics` | Recon & OSINT | Análisis de grafos de infraestructura con la DB de Amass |
| `bug-bounty-oam-asset-modeling` | Recon & OSINT | Modelado estandarizado de activos con Open Asset Model (OAM) |
| `bug-bounty-active-dns-alterations` | Recon & OSINT | Alteraciones activas de nombres de dominio y sondeo dinámico |
| `bug-bounty-osint-automation-framework` | Recon & OSINT | Marco de automatización OSINT multimodular (SpiderFoot) |
| `bug-bounty-darkweb-leak-monitoring` | Recon & OSINT | Monitoreo de Dark Web y fugas de credenciales en breaches |
| `bug-bounty-entity-extraction-metadata` | Recon & OSINT | Extracción de entidades (emails, wallets) y metadatos |
| `bug-bounty-threat-intel-feeds` | Recon & OSINT | Correlación con feeds de inteligencia de amenazas (Shodan/OTX) |
| `bug-bounty-yaml-correlation-rules` | Recon & OSINT | Motor de reglas de correlación YAML para vincular eventos |
| `bug-bounty-js-file-collection` | Recon & OSINT | Recolección automatizada de archivos JavaScript (JSFScan) |
| `bug-bounty-js-endpoint-extraction` | Web & API | Extracción de endpoints y rutas de API en JS (LinkFinder) |
| `bug-bounty-js-secret-scanning` | Web & API | Escaneo de secretos, tokens de API y credenciales en JS |
| `bug-bounty-dom-xss-source-sink` | Web & API | Identificación de Fuentes (Sources) y Sumideros (Sinks) DOM XSS |
| `bug-bounty-js-custom-wordlists` | Web & API | Generación de diccionarios personalizados (Wordlists) desde JS |
| `bug-bounty-http-desync-mutations` | Explotación | Detección de Desincronización CL.TE & TE.CL (Smuggler) |
| `bug-bounty-socket-poisoning-mitigation` | Explotación | Mitigación de Socket Poisoning & Web Cache Poisoning |
| `bug-bounty-single-packet-desync` | Explotación | Orquestación de Ataques Single-Packet TCP para Desincronización |
| `bug-bounty-h2-h1-downgrade-smuggling` | Explotación | HTTP/2 a HTTP/1.1 Downgrade Smuggling en Proxies Frontales |
| `bug-bounty-smuggling-payload-bypasses` | Explotación | Evasión de Filtros WAF en HTTP Request Smuggling |
| `bug-bounty-turbo-intruder-python-scripting` | Explotación | Orquestación de ataques con scripts Python en Turbo Intruder |
| `bug-bounty-race-condition-single-packet-h2` | Explotación | Pruebas de condiciones de carrera (Race Conditions) con HTTP/2 |
| `bug-bounty-custom-http-engine-tuning` | Explotación | Optimización y ajuste fino del motor HTTP personalizado |
| `bug-bounty-response-diffing-filtering` | Explotación | Algoritmo de comparación estructural y filtrado inteligente |
| `bug-bounty-mcp-ai-automated-fuzzing` | Explotación | Automatización de fuzzing con servidores MCP y agentes de IA |
| `bug-bounty-iot-device-auditing` | Mobile/IoT | Auditoría de seguridad en dispositivos IoT y firmware (Binwalk) |
| `bug-bounty-session-ip-binding` | Mobile/IoT | Auditoría de fijación de sesión y vinculación de IP de cliente |
| `bug-bounty-deepfake-ai-spoofing` | Mobile/IoT | Evaluación de riesgos en verificación biométrica (KYC) |
| `bug-bounty-ctf-binary-exploitation` | Mobile/IoT | Fundamentos de análisis de binarios y protecciones (NX/ASLR) |
| `bug-bounty-anomaly-login-blocking` | Mobile/IoT | Evaluación de mecanismos de detección de anomalías y bloqueo |
| `bug-bounty-bchecks-automation` | Explotación | Automatización con Burp Suite BChecks en YAML/BScript |
| `bug-bounty-403-401-bypasses` | Explotación | Técnicas avanzadas de omisión de controles 403/401 |
| `bug-bounty-vulnerability-chaining` | Explotación | Encadenamiento estratégico de vulnerabilidades de bajo impacto |
| `bug-bounty-js-secret-crawling` | Web & API | Rastreo y extracción de secretos JS con NightCrawler |
| `bug-bounty-waf-csp-evasions` | Explotación | Evasión avanzada de WAF y CSP con Script Gadgets |

---

## 📄 Licencia & Créditos
Repositorio mantenido bajo licencia de uso educativo y auditoría autorizada.
