# Cloud S3 Audit & Hardening Reference

## 1. Riesgos de Buckets Abiertos

La lectura pública sin restricciones permite la exfiltración de copias de seguridad de datos de clientes, código fuente o claves privadas. La escritura pública permite alojar malware o reemplazar librerías JavaScript servidas al cliente.

## 2. Remediación Segura

- Aplique la configuración `S3 Block Public Access` a nivel de cuenta global.
- Utilice firmas de URL de acceso temporal (`Signed URLs`) para otorgar descargas puntuales a usuarios autenticados.
