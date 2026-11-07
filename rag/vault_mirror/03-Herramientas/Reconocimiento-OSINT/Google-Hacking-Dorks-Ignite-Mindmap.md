---
tipo: herramienta
subtipo: osint-recon
categoria: reconocimiento
herramienta: Google Hacking Dorks & Search Operators
fuente: Ignite Technologies / Hacking Articles (Raj Chandel)
repositorio: https://github.com/Ignitetechnologies/Mindmap
fecha_ingesta: 2026-11-07
tags:
  - osint
  - google-dorks
  - recon
  - github-dorks
  - red-team-dorks
  - shodan
  - censys
  - fofa
---

# 🔎 Compendio Maestro de Dorking: Google, GitHub & Red Team Multi-Engine

Basado en la investigación y mapas mentales de **Ignite Technologies (Hacking Articles)**, este compendio estructura las técnicas de formulación de consultas avanzadas para recolección de inteligencia de fuentes abiertas (OSINT), descubrimiento de paneles expuestos, fugas de credenciales y mapeo de infraestructura.

---

## 1. 🌐 Google Search Operators: Sintaxis y Operadores

### Operadores Básicos y Booleanos
* `"frase exacta"`: Búsqueda de coincidencia literal estricta. Desactiva sinónimos automáticos.
* `OR` / `|`: Operador booleano O (en mayúsculas obligatorias).
* `( )`: Agrupación lógica de operadores para definir precedencia.
* `-palabra`: Exclusión estricta de términos en los resultados.
* `*`: Comodín (*wildcard*) que reemplaza una o varias palabras desconocidas.
* `#..#`: Rango numérico secuencial (ejemplo: `2024..2026` o `1000..5000`).
* `$` / `€`: Búsqueda de precios y monedas.
* `+término`: Fuerza coincidencia exacta sobre un término específico.

### Operadores Estructurales y de Servidor
* `site:dominio.com`: Restringe la búsqueda exclusivamente al dominio o subdominio.
* `filetype:ext` / `ext:ext`: Filtra archivos por extensión física (`pdf`, `sql`, `env`, `xls`, `log`).
* `inurl:texto`: Busca cadenas dentro de la ruta o parámetros de la URL.
* `allinurl:t1 t2`: Exige que todas las palabras aparezcan en la URL.
* `intitle:texto`: Busca términos dentro de la etiqueta `<title>` del HTML.
* `allintitle:t1 t2`: Exige que todas las palabras aparezcan en el título.
* `intext:texto`: Busca palabras en el cuerpo del documento (`<body>`).
* `allintext:t1 t2`: Exige todos los términos en el cuerpo del texto.
* `cache:url`: Recupera la última versión en caché almacenada por los rastreadores de Google.
* `related:dominio.com`: Descubre dominios o sitios con perfil semántico y tecnológico similar.
* `inanchor:texto`: Busca páginas vinculadas con un texto de anclaje (*anchor text*) específico.
* `info:dominio.com`: Proporciona metadatos y resúmenes que Google mantiene sobre un dominio.

---

## 2. 🎯 Google Hacking Dorks Tácticos

### A. Listado de Directorios Expuesto (`Index of /`)
Permite acceder a estructuras de carpetas donde el servidor no tiene página por defecto (`index.html` / `index.php`):
```text
"intitle:Index of /" + "passwords.txt"
"intitle:Index of /" + "admin" + "password.txt"
"intitle:Index of" + ".htpasswd"
"Index of/" + "config.php" wordpress demo
"allinurl:/cgibin/" + "?" + "password"
"intitle:Index of" .ssh/id_rsa
"intitle:Index of" /wp-content/uploads/
"intitle:Index of" "apache at"
"intitle:Index of /admin"
```

### B. Fuga de Credenciales y Archivos Sensibles
```text
site:target.com ext:xls password
site:target.com ext:xlsx password
site:target.com ext:doc password
site:target.com ext:docx password
site:target.com filetype:pdf username password
site:target.com filetype:ppt username password
filetype:log intext:password
filetype:pem "private key" site:target.com
filetype:config site:target.com
site:urlscan.io "activity" "target.com"
```

### C. Paneles de Administración y Volcados de Bases de Datos
```text
inurl:admin.php site:target.com
intitle:"Please login with admin pass"
inurl:/vpn/tmindex.html
intext:"phpMyAdmin SQL Dump" filetype:sql
site:target.com inurl:/phpmyadmin/* ext:sql ext:sql.gz ext:sql.bz2
intitle:phpmyadmin inurl:server_privileges OR intitle:"login for server * at"
inurl:/elfinder/connector.php
intitle:"WAMPSERVER homepage"
inurl:/proc/self/cwd
```

### D. Huellas de CMS y Detección de Errores SQL
```text
intext:"WordPress" inurl:"wp-config.php" filetype:log
intext:Drupal + "Powered By Drupal forums"
"powered by PHPmotion v3"
"Powered by osCommerce"
"Powered by TinyMCE"
"Powered by Vanilla forums"
"Powered by vBulletin"
intext:"Powered by phpBB" inurl:/viewtopic.php
intext:"sql syntax near" OR intext:"syntax error has occurred" OR intext:"incorrect syntax near"
intext:"MyBB SQL Error" site:target.com
```

---

## 3. 🐙 GitHub Dorks: Caza de Secretos en Repositorios

Consultas especializadas para detectar credenciales y tokens filtrados en commits públicos:

| Archivo / Patrón | Dork de Búsqueda en GitHub | Riesgo Asociado |
| :--- | :--- | :--- |
| **Variables de Entorno** | `filename:.env DB_USERNAME NOT homestead` | Credenciales de bases de datos de producción |
| **Configuración de Correo** | `filename:.env MAIL_HOST=smtp.gmail.com` | Credenciales SMTP expuestas |
| **Credenciales Git** | `filename:.git-credentials NOT username` | Tokens de acceso personal de Git con permisos push |
| **Tokens AWS** | `filename:.bash_profile aws` | `AWS_ACCESS_KEY_ID` y `AWS_SECRET_ACCESS_KEY` |
| **Docker Registry** | `filename:.dockercfg auth` / `filename:config.json auths` | Credenciales de registro Docker / Kubernetes |
| **NPM Registry** | `filename:.npmrc _auth` | Tokens de publicación en repositorios privados NPM |
| **PostgreSQL** | `filename:.pgpass` | Contraseñas de conexión a bases Postgres |
| **SSH & SFTP** | `filename:.ftpconfig` / `filename:.remote-sync.json` | Claves y credenciales SSH guardadas por editores |
| **Historial de Shell** | `filename:.bash_history` / `filename:.sh_history` | Comandos con contraseñas y flags inline |
| **Autenticación Web** | `filename:.htpasswd` | Hashes de autenticación básica Apache/Nginx |
| **S3 Buckets** | `filename:.s3cfg` | Credenciales de acceso a almacenamiento S3 |

---

## 4. 🛡️ Red Team Multi-Engine Matrix: Shodan, Censys, FOFA & Más

Sintaxis transversal estandarizada por Ignite Technologies para consultar componentes tecnológicos en múltiples motores de escaneo de internet:

### A. Detección de Servidores Web (Nginx / Apache)
* **Shodan:** `"nginx" http.component:nginx` | `http.component:apache`
* **Censys:** `"nginx" AND tags:web AND tags:https` | `"apache" AND tags:web AND tags:https`
* **FOFA:** `title="nginx" || header="nginx"` | `title="apache" || header="apache"`
* **GreyNoise:** `service.name:nginx` | `service.name:apache`
* **ZoomEye:** `app:"nginx"` | `app:"apache"`
* **Netlas:** `http.server:nginx` | `http.server:apache`
* **LeakIX:** `server:nginx` | `server:apache`

### B. Bases de Datos y Motores de Búsqueda (Elasticsearch / Kibana)
* **Shodan:** `product:elasticsearch`
* **Censys:** `elasticsearch.protocol:tcp`
* **FOFA:** `title="Elasticsearch" || body="Elasticsearch" || header="Elasticsearch"`
* **GreyNoise:** `port:9200`
* **ZoomEye:** `app:"Elasticsearch" port:"9200"`
* **LeakIX:** `title:"kibana" && title:"elastic"`

### C. Bloques de Red y Números de Sistema Autónomo (ASN)
* **Shodan:** `asn:ASXXXXXXX org:"Nombre"`
* **Censys:** `asn:ASXXXXXXX AND tags:web`
* **SecurityTrails:** `include:asn:ASXXXXXXX AND type:organization`
* **FOFA:** `header="ASXXXXXXX"`
* **GreyNoise:** `asn:ASXXXXXXX organization:"Nombre"`

---

## 🔗 Conexión con el Ecosistema de Bug Bounty

1. **Habilidad Táctica:** Integrado en `skills/bug-bounty-search-engine-dorking/` para reconocimiento asistido por IA.
2. **Filtrado de Scope:** Todas las búsquedas `site:target.com` se validan contra los límites definidos en `scopes/*.csv`.
3. **Calidad de Hallazgos:** Los resultados de dorking se someten al `7-Question Gate` para confirmar accesibilidad sin autenticación y evaluar impacto real de negocio.
