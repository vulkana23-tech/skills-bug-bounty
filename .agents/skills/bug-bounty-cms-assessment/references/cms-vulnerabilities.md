# CMS Security & Hardening Reference

## 1. Riesgos de Malas Configuraciones en CMS

Los sitios que emplean CMS sufren frecuentemente de vulnerabilidades en complementos (plugins) de terceros desactualizados o no mantenidos que permiten ejecución remota de código o volcado de la base de datos.

## 2. Remediación Segura

- Mantenga el núcleo del CMS (`core`), los temas y los plugins actualizados a la última versión disponible.
- Elimine todos los plugins y temas no utilizados o descontinuados.
- Deshabilite la edición en línea de archivos de código PHP (`DISALLOW_FILE_EDIT=true` en WordPress).
