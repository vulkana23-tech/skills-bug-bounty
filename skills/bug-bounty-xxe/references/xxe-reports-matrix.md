# XXE HackerOne Reports Matrix

## Top Disclosed XXE Reports (HackerOne Index)

- **Twitter XXE in SVG Parsing ($10,880 Bounty)**: Inyección XXE al procesar metadatos XML en avatares SVG subidos por usuarios.
- **Uber XXE via SAML Metadata Import ($10,000 Bounty)**: Inyección de entidades externas al importar metadatos XML SSO SAML en la configuración de socios.
- **US DoD XXE in Document Conversion ($5,000 Bounty)**: XXE en convertidor de formatos Office/PDF procesando archivos `.docx` malformados.
- **Shopify XXE in Theme Upload ($8,000 Bounty)**: Inyección XXE en archivos XML de temas e internacionalización.

## Bypasses de Sanitización XML
- Utilizar codificaciones UTF-16BE / UTF-16LE para evadir WAFs basados en expresiones regulares que solo inspeccionan UTF-8.
- Abusar de DTDs locales existentes en el sistema operativo (ej. `/usr/share/xml/...`) para provocar Blind XXE mediante la redefinición de entidades paramétricas.
