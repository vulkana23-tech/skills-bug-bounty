# Master Bug Bounty & Security Knowledge Base Compendium (100 Agent Skills)

Este documento es una base de conocimiento consolidada que agrupa la metodología técnica, patrones de prueba y guías de remediación de las **100 Agent Skills de Ciberseguridad**. Está optimizado para **RAG (Retrieval-Augmented Generation)**, bases de datos vectoriales (ChromaDB, Pinecone, Qdrant) y lectura de contexto persistente en asistentes de IA.

---

## 📌 DOMINIO 1: RECONOCIMIENTO & OSINT (Skills 01–25)

### Skill 01–05: Active & Passive Reconnaissance
- **Subdomain Discovery**: Combinación de fuentes pasivas (`subfinder`, `assetfinder`) y sondeo estocástico (`puredns`, `shuffledns`).
- **ASN & BGP Mapping**: Identificación de prefijos IP de la organización objetivo mediante registros WHOIS y consultas a motores de búsqueda con `amass intel -asn <ASN>`.
- **Certificate Transparency Logs**: Extracción de subdominios históricos mediante monitoreo de logs SSL en `crt.sh`.

### Skill 06–15: Attack Surface & Asset Modeling (Amass & OAM)
- **Open Asset Model (OAM)**: Normalización de activos (nombres de dominio, direcciones IP, servicios, certificados, ASNs) en una estructura de grafos unificada.
- **Graph Database Analytics**: Uso del comando `amass db` para visualizar las relaciones entre servidores web, balanceadores de carga e infraestructura en la nube.

### Skill 16–25: OSINT & Threat Intelligence (SpiderFoot & Secret Leak Detection)
- **SpiderFoot Automation**: Canalización de más de 200 módulos de recolección de inteligencia (Shodan, GreyNoise, AlienVault OTX, HaveIBeenPwned).
- **Secret Leak Detection**: Detección de claves de API expuestas (AWS, Stripe, JWT, Firebase) en repositorios públicos y archivos JavaScript con `Trufflehog` y `Gitleaks`.

---

## 📌 DOMINIO 2: VULNERABILIDADES WEB & APIS (Skills 26–55)

### Skill 26–35: Client-Side Vulnerabilities (XSS, CORS, DOM, Prototype Pollution)
- **Cross-Site Scripting (XSS)**: Identificación de XSS Reflejado, Almacenado y DOM-based. Uso de payloads limpios y evasión de filtros CSP mediante Script Gadgets.
- **CORS Misconfigurations**: Detección de reflejo arbitrario de encabezado `Origin`, `Access-Control-Allow-Credentials: true` y vectores con `Origin: null`.
- **Prototype Pollution**: Explotación de modificaciones en `Object.prototype` en librerías JavaScript cliente y servidores Node.js para lograr bypasses de autorización o RCE.

### Skill 36–45: Server-Side & Authorization Flaws (SQLi, SSRF, IDOR, GraphQL)
- **SQL Injection**: Explotación de SQLi Ciega, Basada en Tiempo, Basada en Error y Out-Of-Band (OOB).
- **Server-Side Request Forgery (SSRF)**: Pivotaje desde solicitudes web vulnerables hacia endpoints de metadatos cloud (`169.254.169.254` para AWS/GCP) y servicios internos (`127.0.0.1`).
- **IDOR / BOLA / BFLA**: Auditoría de APIs RESTful y GraphQL mediante la sustitución de identificadores de recursos en peticiones de usuario sin privilegios.

### Skill 46–55: Token Security & Business Logic (OAuth, JWT, Race Conditions)
- **OAuth 2.0 Flaws**: Fuga de `access_token` en URL fragment (`#`), omisión de `state` (CSRF en OAuth) y secuestro de cuentas vía `redirect_uri` no validado.
- **JWT Assessment**: Prueba de algoritmo `none`, inyección de claves públicas vía encabezado `jku`/`x5u`, y confusión de clave simétrica/asimétrica (RS256 vs HS256).

---

## 📌 DOMINIO 3: CLOUD, DEVOPS & CONTENEDORES (Skills 56–70)

### Skill 56–65: Cloud Hardening & Storage (AWS, GCP, Azure, S3)
- **S3 Bucket Auditing**: Descubrimiento y prueba de permisos de lectura/escritura pública en buckets de almacenamiento AWS S3 (`s3scanner`, `cloudfox`).
- **Cloud IAM Audit**: Identificación de políticas de roles IAM excesivamente permisivas (`sts:AssumeRole`, `iam:PassRole`) que conducen a escalación de privilegios cloud.

### Skill 66–70: Containers & Declarative Scanning (Docker, K8s, Nuclei)
- **Kubernetes RBAC**: Auditoría de ServiceAccounts con permisos elevados y contenedores ejecutados en modo privilegiado (`--privileged`).
- **Nuclei Template Authoring**: Creación de plantillas de escaneo declarativas YAML con extractores y matcheadores de alta precisión para CVEs recientes.

---

## 📌 DOMINIO 4: EXPLOTACIÓN AVANZADA Y PROTOCOLOS (Skills 71–85)

### Skill 71–75: HTTP Request Smuggling & Desync (CL.TE / TE.CL / H2 Downgrade)
- **HTTP Request Smuggling**: Detección de desacuerdos entre proxies frontales y backends en el cálculo de límites de petición usando `Content-Length` y `Transfer-Encoding` (`defparam/smuggler`).
- **H2 Downgrade Smuggling**: Explotación de inyecciones `\r\n` en tramas HTTP/2 traducidas a HTTP/1.1 en el backend.

### Skill 76–85: High-Speed Fuzzing & Custom Handlers (Turbo Intruder & BChecks)
- **Single-Packet Attack (Last-Byte Sync)**: Envíos sincronizados del último byte TCP para ejecutar peticiones concurrentes sin diferencia de latencia en Turbo Intruder (`PortSwigger/turbo-intruder`).
- **Burp Suite BChecks**: Automatización de controles pasivos y activos personalizados mediante scripts declarativos BScript/YAML en Burp Suite.

---

## 📌 DOMINIO 5: MÓVIL, IOT, BINARIOS & DEFENDABILITY (Skills 86–100)

### Skill 86–92: Mobile, IoT Firmware & Biometric Verification
- **Mobile Assessment**: Auditoría de aplicaciones Android/iOS (OWASP Mobile Top 10), bypassing de SSL Pinning con Frida, análisis de componentes expuestos (`AndroidManifest.xml`).
- **IoT Firmware Security**: Extracción e inspección de imágenes de firmware embebido (`binwalk`), análisis de claves SSH/Web hardcodeadas y servidores embebidos.
- **Biometric eKYC & Deepfakes**: Evaluación de vulnerabilidades en sistemas de verificación de identidad y controles de Liveness Detection.

### Skill 93–100: Binary Protections & Defensive Controls
- **Binary Hardening**: Verificación de protecciones de compilación en ejecutables ELF/PE (`NX`, `ASLR`, `PIE`, `Stack Canaries`).
- **Anomaly Detection**: Implementación de rate limiting adaptativo por IP y monitoreo de comportamiento anormal en mecanismos de inicio de sesión.
