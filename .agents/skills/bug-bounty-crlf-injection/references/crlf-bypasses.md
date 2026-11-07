# CRLF Injection & Response Splitting Remediation Reference

## 1. Riesgos de CRLF Injection

1. **HTTP Response Splitting**: Inyección de respuestas HTTP secundarias para secuestrar conexiones de otros usuarios.
2. **Session Fixation / Cookie Injection**: Inyección de cabeceras `Set-Cookie` para fijar la sesión de la víctima a una cuenta controlada por el atacante.
3. **Cross-Site Scripting (XSS)**: Bypass de WAF inyectando código JavaScript directamente en la sección de cuerpo generada.

## 2. Remediación Segura

- Remueva o reemplace todos los caracteres de salto de línea (`\r`, `\n`, `%0d`, `%0a`) de cualquier entrada de usuario reflejada en los encabezados HTTP.
- Utilice métodos o frameworks HTTP modernos que descarten automáticamente caracteres de control al establecer encabezados de respuesta.
