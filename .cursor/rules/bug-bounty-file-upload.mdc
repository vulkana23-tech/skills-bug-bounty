---
name: bug-bounty-file-upload
description: Auditoría y pruebas de seguridad en funciones de carga de archivos (Unrestricted File Upload). Evasión de validaciones de extensión, MIME-Type, Polyglots, inyección de metadatos EXIF y ejecución de scripts.
---

# Skill: File Upload Security & Bypass Assessment

Esta habilidad capacita al agente para evaluar mecanismos de carga de archivos (avatares, documentos, adjuntos, imágenes) para garantizar que no puedan subirse archivos ejecutables u objetos dañinos para el servidor web.

## 📌 Diagnóstico y Evasión de Validaciones

### 1. Evasión de Extensión (Extension Bypasses)
- **Extensión secundaria / alternativa**: `.php5`, `.phtml`, `.phar`, `.shtml`, `.jspx`, `.jspa`, `.aspx`, `.ashx`.
- **Doble extensión**: `image.php.jpg`, `image.jpg.php`.
- **Caracteres nulos / Trailing Dots**: `image.php%00.jpg`, `image.php....`, `image.php::$DATA` (NTFS alternate data stream).
- **Mayúsculas / Minúsculas mezcladas**: `image.pHp`, `image.Phtml`.

### 2. Evasión de MIME-Type / Magic Bytes
- Reemplazar `Content-Type: application/x-php` por `Content-Type: image/jpeg` o `image/png`.
- Incluir la firma de encabezado de imagen (Magic Bytes):
  - **GIF89a**: `GIF89a; <?php ... ?>`
  - **PNG**: `\x89PNG\r\n\x1a\n...`

---

## 📚 Referencias Técnicas

Consulta los detalles completos de mitigación en:
[file-upload-bypasses.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-file-upload/references/file-upload-bypasses.md)
