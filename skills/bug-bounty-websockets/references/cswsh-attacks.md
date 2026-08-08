# WebSocket & CSWSH Security Reference

## 1. Riesgos en Implementaciones WebSocket

1. **CSWSH**: Secuestro de conexión WebSocket desde un origen de navegador malicioso debido a la ausencia de validación del encabezado `Origin`.
2. **Falta de Re-Autenticación**: Confianza indefinida en el apretón de manos inicial sin invalidar sockets tras el cierre de sesión.

## 2. Remediación Segura

- Valide estrictamente la cabecera `Origin` durante la solicitud de Handshake HTTP (`101 Switching Protocols`).
- Utilice tokens aleatorios de un solo uso (CSRF-like tickets) transmitidos como parámetro o subprotocolo en la conexión inicial.
- Forzar siempre el uso del protocolo seguro `wss://`.
