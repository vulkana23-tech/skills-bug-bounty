---
name: bug-bounty-search-engine-dorking
description: Uso avanzado de operadores de motores de búsqueda (Search Engine Dorks) para descubrir paneles expuestos, archivos sensibles, subdominios ocultos e interfaces de administración.
---

# Skill: Search Engine Dorking & Index Analysis

Esta habilidad capacita al agente para formular expresiones de búsqueda avanzadas (Dorks en Google, GitHub, Shodan, Censys y FOFA) para exponer información confidencial indexada públicamente por error, respetando siempre el alcance de autorización.

---

## 📌 Operadores de Dorking Principales

- `site:target.com`: Limita la búsqueda al dominio objetivo.
- `filetype:pdf OR filetype:xls OR filetype:docx OR filetype:log`: Filtra documentos internos y registros expuestos.
- `inurl:admin OR inurl:login OR inurl:dashboard OR inurl:/vpn/tmindex.html`: Descubre paneles administrativos y consolas.
- `intitle:"index of"`: Identifica servidores con listado de directorios activo.
- `intitle:"index of" .ssh/id_rsa`: Detecta claves privadas SSH indexadas.
- `intext:"phpMyAdmin SQL Dump" filetype:sql`: Localiza volcados directos de bases de datos.

---

## 🧭 Metodología de Ejecución Paso a Paso

1. **Delimitación de Alcance**:
   - Antes de lanzar cualquier consulta con `site:`, valida que el dominio base esté presente en los archivos `scopes/*.csv`.
2. **Reconocimiento Pasivo de Superficie**:
   - Rastrea subdominios indexados: `site:*.target.com -site:www.target.com`.
   - Localiza endpoints de desarrollo/staging: `site:target.com inurl:dev OR inurl:test OR inurl:staging`.
3. **Detección de Fugas de Secretos**:
   - Consulta archivos de entorno y claves en GitHub: `filename:.env DB_USERNAME` apuntando al nombre de la organización o proyecto.
4. **Validación Ética (7-Question Gate)**:
   - Verifica que el archivo encontrado no contenga datos falsos o de prueba (*honeypots*).
   - Confirma accesibilidad directa sin evadir autenticación activa.

---

## 📚 Referencias Técnicas y Cheat Sheet Completo

Consulta el compendio detallado de sintaxis, operadores de Google, GitHub y matriz multi-motor (Shodan/Censys/FOFA) en:
[dorking-cheat-sheet.md](references/dorking-cheat-sheet.md)
