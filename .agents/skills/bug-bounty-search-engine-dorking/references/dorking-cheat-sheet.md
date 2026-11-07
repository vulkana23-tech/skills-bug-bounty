# Search Engine Dorking Cheat Sheet Reference

## 1. Ejemplos de Dorks para Bug Bounty

- **Fuga de Credenciales/Secretos**: `site:target.com ext:env OR ext:yaml OR ext:json "password"`
- **Paneles Swagger/API**: `site:target.com inurl:api-docs OR inurl:swagger`

## 2. Remediación Segura

- Utilice el archivo `robots.txt` para desaconsejar el rastreo de áreas privadas e implemente encabezados `X-Robots-Tag: noindex` en archivos sensibles.
- Solicite la eliminación inmediata de URLs almacenadas en caché a través de las herramientas para webmasters (Google Search Console).
