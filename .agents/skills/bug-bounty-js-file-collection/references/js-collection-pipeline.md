# JavaScript File Collection Reference Guide

## 1. Descarga Local y Almacenamiento Estructurado

- Almacene los archivos JS descargados en una carpeta `js_files/` local etiquetados por hash MD5 para evitar redundancia en archivos minificados comunes (ej. jQuery/React).

## 2. Remediación Segura

- Evite incluir entornos de desarrollo o código de pruebas no ofuscado en bundles servidos públicamente a producción.
