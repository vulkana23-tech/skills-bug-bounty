# Rate Limiting & Brute Force Protection Reference

## 1. Riesgos de la Ausencia de Rate Limiting

Permitir solicitudes ilimitadas en endpoints de autenticación faculta a atacantes a realizar ataques de fuerza bruta masivos en contraseñas o enumeración de PINs/OTPs de 4 o 6 dígitos.

## 2. Remediación Segura

- Utilice la IP del socket remoto (proporcionada por el proxy de confianza validado) combinada con el identificador de usuario para calcular el Rate Limit.
- No confíe ciegamente en encabezados `X-Forwarded-For` no verificados provenientes del cliente.
- Implemente bloqueos progresivos con tiempo de espera exponencial y mecanismos CAPTCHA tras múltiples intentos fallidos.
