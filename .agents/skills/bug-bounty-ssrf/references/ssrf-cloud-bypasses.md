# SSRF Cloud Metadata & Filter Bypass Reference

## 1. Técnicas Avanzadas de Bypass de WAF/Filtros SSRF

### DNS Rebinding
Consiste en configurar un dominio bajo control del atacante con un TTL de 0 segundos que alterne entre responder una IP pública válida (para pasar la validación inicial) y `127.0.0.1` o `169.254.169.254` al realizar la petición real.
- Herramientas: `singularity`, `rbndr`.

### URL Parsing Confusion (RFC Standard Divergence)
Diferencias entre cómo el validador de la aplicación y la biblioteca HTTP interna (ej. cURL vs Python requests) interpreta la URL:
- `http://expected-domain.com@127.0.0.1/`
- `http://127.0.0.1#@expected-domain.com/`
- `http://127.0.0.1:80\.expected-domain.com/`

### Redirección HTTP (301/302 Redirects)
Si el validador verifica la URL de destino pero el cliente HTTP sigue redirecciones de forma automática:
- Apuntar la solicitud inicial a `http://attacker.com/redirect.php` que devuelva `Header("Location: http://169.254.169.254/latest/meta-data/");`.

---

## 2. Casos Reales de Bug Bounty
- **Google DSPL Stored XSS & SSRF**: *s1gnalcha0s* - SSRF en el analizador de archivos Dataset Publishing Language de Google que permitió leer recursos internos.
- **Capital One Cloud Breach**: Vulnerabilidad SSRF en WAF de AWS que permitió exfiltrar credenciales de IAM de la métrica `169.254.169.254`.
