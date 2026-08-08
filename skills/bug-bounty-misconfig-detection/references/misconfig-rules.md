# Server Misconfiguration Remediation Reference

## 1. Riesgos de Errores de Configuración

La exposición de carpetas `.git` permite la descarga completa del código fuente de la aplicación, mientras que la falta de cabeceras de seguridad facilita ataques de Clickjacking y XSS.

## 2. Remediación Segura

- Restrinja el acceso a directorios ocultos (`.*`) en la configuración del servidor web (Nginx/Apache).
- Configure cabeceras de seguridad globales en la respuesta del proxy inverso.
