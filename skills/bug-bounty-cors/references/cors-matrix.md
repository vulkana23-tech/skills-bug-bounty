# CORS Misconfiguration Remediation Reference

## 1. Riesgos de Malas Configuraciones CORS

Permitir orígenes no confiables con credenciales permite que un sitio web malicioso mediante una petición `fetch()` o `XMLHttpRequest` extraiga tokens, datos personales o ejecute acciones en nombre del usuario autenticado.

## 2. Configuración Segura de CORS

- Implemente una lista blanca estricta (`whitelist`) de orígenes explícitos permitidos en el backend.
- Nunca refleje dinámicamente el valor de la cabecera `Origin` sin validación previa contra la lista blanca.
- Evite habilitar `Access-Control-Allow-Origin: *` en endpoints que requieran autenticación o manejen datos privados.
