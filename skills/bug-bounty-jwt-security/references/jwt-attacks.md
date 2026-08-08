# JWT Security & Remediation Reference

## 1. Riesgos Comunes en JWT

1. **Falta de Verificación de Firma**: Confiabilidad ciega en las afirmaciones (`claims`) del payload sin validar la firma.
2. **Clave Secreta Débil**: Secretos HMAC que pueden ser adivinados mediante ataques de diccionario fuera de línea (`john`, `hashcat`).
3. **Falta de Expiración (`exp`)**: Tokens con vida infinita que no expiran tras el cierre de sesión.

## 2. Recomendaciones de Seguridad para JWT

- Utilice bibliotecas probadas y actualizadas para el manejo de JWT que fuercen la especificación explícita de los algoritmos permitidos (ej. rechazar implícitamente `none`).
- Encriptes o firme los tokens con claves asimétricas robustas (RS256, ES256) con almacenamiento seguro de claves privadas (KMS / HSM).
- Incluya siempre las notaciones de expiración (`exp`), emisión (`iat`) y audiencia (`aud`).
