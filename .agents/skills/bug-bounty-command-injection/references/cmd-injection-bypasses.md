# OS Command Injection Remediation Reference

## 1. Riesgos de OS Command Injection

Permitir la inyección de comandos del sistema operativo faculta a un atacante a tomar control total del servidor web, ejecutar código arbitrario con los privilegios del servicio web (`www-data`, `nginx`, `SYSTEM`) y pivotar dentro de la red interna.

## 2. Remediación Segura

- Evite invocar funciones de shell del sistema operativo siempre que exista una API o biblioteca nativa del lenguaje (ej. usar `fs.readFile()` en lugar de `cat`).
- Si debe invocar binarios externos, utilice arreglos de argumentos con ejecución directa sin pasar por un interprete de shell (ej. `execFile('ping', ['-c', '4', host])`).
