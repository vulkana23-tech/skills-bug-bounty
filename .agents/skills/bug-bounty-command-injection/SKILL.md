---
name: bug-bounty-command-injection
description: Identificación y remediación de vulnerabilidades OS Command Injection. Bypass de filtros de espacio, caracteres especiales, concatenadores de shell y blind command injection.
---

# Skill: OS Command Injection Assessment

Esta habilidad capacita al agente para evaluar aplicaciones web que invocan comandos del sistema operativo (`exec`, `system`, `popen`, `child_process`) pasando parámetros suministrados por los usuarios sin parametrización.

## 📌 Vectores de Diagnóstico

### 1. Separadores y Concatenadores de Shell
`;`, `|`, `||`, `&`, `&&`, `%0a` (Salto de línea), `` `command` ``, `$(command)`

### 2. Bypass de Filtros de Espacio
- **Linux**: `$IFS`, `${IFS}`, `<` (redirección de entrada), `%20`, `%09` (Tab).
- Ejemplo: `cat${IFS}/etc/passwd`

### 3. Blind Command Injection (Inyección Ciega)
- Provocar demoras de tiempo: `; sleep 10`
- Confirmar vía peticiones DNS Out-of-Band (`ping`, `nslookup`).

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[cmd-injection-bypasses.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-command-injection/references/cmd-injection-bypasses.md)
