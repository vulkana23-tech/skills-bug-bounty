# XSLT Injection Remediation Reference

## 1. Riesgos de XSLT Injection

Las transformaciones XSLT inseguras permiten a un atacante leer archivos locales del servidor web, realizar peticiones HTTP arbitrarias hacia la red interna (SSRF) o ejecutar comandos del sistema operativo si la librería XSLT tiene habilitadas las extensiones de código.

## 2. Remediación Segura

- Nunca permita que los usuarios suministren archivos XSLT arbitrarios.
- Deshabilite el soporte para funciones externas como `document()` y extensiones de lenguaje en la configuración del procesador XSLT (ej. `setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true)`).
