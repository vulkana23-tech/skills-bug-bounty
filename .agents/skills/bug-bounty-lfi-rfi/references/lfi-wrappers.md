# LFI & RFI Techniques and Remediation Reference

## 1. Conceptos de Inclusión de Archivos

- **LFI (Local File Inclusion)**: La aplicación incluye y procesa un archivo almacenado localmente en el servidor debido a la falta de sanitización del nombre de la ruta.
- **RFI (Remote File Inclusion)**: La aplicación permite cargar e incluir un recurso remoto accesible por URL (ej. `http://` o `https://`).

## 2. Remediación Segura

1. Evite pasar entradas de usuario directamente a funciones de inclusión de archivos (`include`, `require`, `file_get_contents`, `readFile`).
2. Utilice una lista blanca estricta de archivos permitidos o asocie índices numéricos a las rutas de archivos.
3. Deshabilite `allow_url_include` y `allow_url_fopen` en la configuración `php.ini`.
4. Utilice funciones que resuelvan la ruta canónica (ej. `realpath()`) y verifique que comience con el directorio base permitido.
