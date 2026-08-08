# File Upload Security & Remediation Reference

## 1. Riesgos Principales en la Carga de Archivos

1. **Remote Code Execution (RCE)**: Carga e inclusión directa de archivos con extensiones ejecutables por el servidor web (`.php`, `.jsp`, `.asp`).
2. **Stored Cross-Site Scripting (XSS)**: Carga de archivos HTML o SVG con scripts incrustados ejecutados cuando la víctima los visualiza.
3. **Denegación de Servicio (DoS)**: Carga de archivos de tamaño desmedido o bombas de descomposición (Zip Bombs).

## 2. Remediación Segura

- Genere nombres de archivo aleatorios únicos (ej. UUIDv4) en el servidor y reemplace el nombre original suministrado por el cliente.
- Guarde los archivos fuera del directorio raíz web (`webroot`) o en un servicio de almacenamiento independiente (S3 / Cloud Storage).
- Sirva los archivos desde un dominio secundario independiente (ej. `user-content.com`) con encabezados `Content-Disposition: attachment` y `X-Content-Type-Options: nosniff`.
- Valide el contenido del archivo procesando o re-codificando imágenes mediante librerías seguras.
