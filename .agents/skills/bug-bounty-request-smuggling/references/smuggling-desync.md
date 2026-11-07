# HTTP Request Smuggling Remediation Reference

## 1. Riesgos de HTTP Request Smuggling

La desincronización de solicitudes HTTP permite a un atacante inyectar solicitudes arbitrarias en la cola del servidor backend, derivando en la intercepción de cookies de sesión de otros usuarios, omisión de controles de acceso del proxy frontend o envenenamiento de la caché web (Cache Poisoning).

## 2. Remediación Segura

- Utilice HTTP/2 de extremo a extremo (End-to-End HTTP/2) entre el cliente, el proxy frontend y los servidores backend.
- Configure el servidor frontend y backend para reutilizar la misma especificación estricta en el análisis de solicitudes HTTP.
- Rechace o descarte peticiones HTTP/1.1 que contengan simultáneamente `Content-Length` y `Transfer-Encoding`.
