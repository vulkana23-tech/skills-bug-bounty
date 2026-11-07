# CSV & Formula Injection Remediation Reference

## 1. Riesgos de CSV Injection

Cuando un usuario descarga una hoja de cálculo generada por la aplicación e interactúa con ella, las fórmulas inyectadas pueden ejecutar comandos locales en su sistema operativo o exfiltrar automáticamente los contenidos de otras celdas hacia servidores remotos.

## 2. Remediación Segura

- Si el primer carácter de cualquier campo de texto exportado a CSV es `=`, `+`, `-`, `@` o `%`, anteceda un carácter de comilla simple (`'`) al inicio de la celda.
- Encierre todos los campos de texto dentro de comillas dobles (`"..."`) y sanitice las comillas internas.
