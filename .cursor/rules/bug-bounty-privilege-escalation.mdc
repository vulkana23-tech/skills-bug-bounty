---
name: bug-bounty-privilege-escalation
description: Auditoría de escalación de privilegios en entornos Linux y Windows. Identificación de permisos SUID/SUDO vulnerables, servicios desconfigurados, DLL Hijacking y permisos de registro.
---

# Skill: Privilege Escalation Assessment (Linux & Windows)

Esta habilidad capacita al agente para auditar la configuración de permisos del sistema operativo y detectar rutas de elevación de privilegios desde un usuario con privilegios restringidos hacia `root` (en Linux) o `SYSTEM` / `Administrator` (en Windows).

## 📌 Vectores Principales de Elevación de Privilegios

### 1. Linux Privilege Escalation
- **SUID Binaries**: Binarios con el bit SUID activo que permiten la ejecución con privilegios de root (`GTFOBins`).
- **SUDO Misconfigurations**: Reglas en `/etc/sudoers` que permiten ejecutar comandos específicos como root sin contraseña (`sudo -l`).

### 2. Windows Privilege Escalation
- **Unquoted Service Paths**: Servicios del sistema con rutas sin comillas y espacios en el nombre de directorio.
- **DLL Hijacking**: Carga de librerías DLL maliciosas en directorios escribibles del PATH.

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[privesc-vectors.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-privilege-escalation/references/privesc-vectors.md)
