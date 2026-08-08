# Privilege Escalation Hardening & Remediation Reference

## 1. Riesgos de Errores de Permisos

Las malas configuraciones en permisos del sistema operativo permiten a cualquier proceso o usuario local de baja jerarquía comprometer completamente el servidor y tomar control del sistema operativo.

## 2. Remediación Segura

- Aplique el principio de mínimo privilegio en las reglas del archivo `/etc/sudoers`.
- Remueva el bit SUID de binarios que no lo requieran estrictamente.
- Encierre entre comillas todas las rutas de ejecutables de servicios en Windows (`"C:\Program Files\Service\app.exe"`).
- Restrinja los permisos de escritura en los directorios del sistema para usuarios no administradores.
