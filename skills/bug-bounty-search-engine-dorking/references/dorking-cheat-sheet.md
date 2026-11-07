# Search Engine & Multi-Engine Dorking Cheat Sheet (Ignite Technologies Standard)

Compendio táctico exhaustivo de operadores de búsqueda avanzada y patrones de dorking para recolección pasiva de inteligencia, descubrimiento de activos expuestos y detección de fugas de credenciales.

---

## 1. Google Search Operators Reference

### Operadores Básicos & Lógica Booleana
* `"cadena exacta"`: Búsqueda estricta de términos consecutivos; ignora sinónimos.
* `OR` / `|`: Operador booleano disyuntivo (debe ir en MAYÚSCULAS).
* `( )`: Agrupación lógica de operadores complejos.
* `-termino`: Exclusión estricta de palabras de los resultados.
* `*`: Comodín (*wildcard*) sustituto de una o más palabras desconocidas.
* `#..#`: Rango numérico continuo (ejemplo: `2024..2026`).

### Operadores Estructurales
* `site:target.com`: Restricción estricta al dominio o subdominio objetivo.
* `filetype:ext` / `ext:ext`: Filtrado por tipo o extensión de archivo.
* `inurl:texto` / `allinurl:t1 t2`: Cadena presente en la URL o ruta del recurso.
* `intitle:texto` / `allintitle:t1 t2`: Cadena presente en el título HTML (`<title>`).
* `intext:texto` / `allintext:t1 t2`: Cadena presente en el cuerpo del texto (`<body>`).
* `cache:url`: Recuperación de la última copia estática indexada en el caché del buscador.
* `related:dominio.com`: Sitios con perfil temático o infraestructura similar.

---

## 2. Catálogo Táctico de Google Dorks

### A. Listado de Directorios Expuestos (`Index of /`)
Identifica servidores sin página índice que listan su sistema de archivos:
```text
"intitle:Index of /" + "passwords.txt"
"intitle:Index of /" + "admin" + "password.txt"
"intitle:Index of" + ".htpasswd"
"Index of/" + "config.php" wordpress demo
"allinurl:/cgibin/" + "?" + "password"
"intitle:Index of" .ssh/id_rsa
"intitle:Index of" "apache at"
"intitle:Index of /admin"
```

### B. Fuga de Credenciales, Llaves y Documentos Sensibles
```text
site:target.com ext:xls password
site:target.com ext:xlsx password
site:target.com ext:doc password
site:target.com ext:docx password
site:target.com filetype:pdf username password
filetype:log intext:password
filetype:pem "private key" site:target.com
filetype:config site:target.com
site:urlscan.io "activity" "target.com"
```

### C. Paneles de Control y Volcados de Bases de Datos
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

## 3. GitHub Dorks: Caza de Secretos en Repositorios

Consultas dirigidas en el buscador de código de GitHub (`github.com/search`):

| Tipo de Secreto | Dork de Búsqueda | Riesgo |
| :--- | :--- | :--- |
| **Variables de Entorno** | `filename:.env DB_USERNAME NOT homestead` | Credenciales de base de datos |
| **Configuración SMTP** | `filename:.env MAIL_HOST=smtp.gmail.com` | Servidores y contraseñas de correo |
| **Credenciales Git** | `filename:.git-credentials NOT username` | Tokens de acceso personal de Git |
| **Tokens Cloud AWS** | `filename:.bash_profile aws` | API keys con acceso a infraestructura |
| **Registros Docker** | `filename:.dockercfg auth` / `filename:config.json auths` | Credenciales de registry de contenedores |
| **Registros NPM** | `filename:.npmrc _auth` | Tokens de publicación de paquetes |
| **PostgreSQL** | `filename:.pgpass` | Contraseñas de acceso a base de datos |
| **SSH / SFTP** | `filename:.ftpconfig` / `filename:.remote-sync.json` | Credenciales guardadas por editores |
| **Historial de Shell** | `filename:.bash_history` / `filename:.sh_history` | Comandos con contraseñas en texto plano |
| **Contraseñas Web** | `filename:.htpasswd` | Hashes de autenticación básica |
| **Almacenamiento S3** | `filename:.s3cfg` | Credenciales de buckets AWS S3 |

---

## 4. Red Team Multi-Engine Queries (Shodan, Censys, FOFA, GreyNoise)

Consultas sincronizadas para mapeo de componentes de infraestructura expuestos:

### Servidores Web (Nginx / Apache)
* **Shodan:** `"nginx" http.component:nginx` | `http.component:apache`
* **Censys:** `"nginx" AND tags:web AND tags:https` | `"apache" AND tags:web AND tags:https`
* **FOFA:** `title="nginx" || header="nginx"` | `title="apache" || header="apache"`
* **GreyNoise:** `service.name:nginx` | `service.name:apache`
* **LeakIX:** `server:nginx` | `server:apache`

### Elasticsearch & Kibana
* **Shodan:** `product:elasticsearch`
* **Censys:** `elasticsearch.protocol:tcp`
* **FOFA:** `title="Elasticsearch" || body="Elasticsearch"`
* **GreyNoise:** `port:9200`
* **LeakIX:** `title:"kibana" && title:"elastic"`

### Reconocimiento de ASNs Corporativos
* **Shodan:** `asn:ASXXXXXXX org:"Objetivo"`
* **Censys:** `asn:ASXXXXXXX AND tags:web`
* **FOFA:** `header="ASXXXXXXX"`
* **SecurityTrails:** `include:asn:ASXXXXXXX AND type:organization`
