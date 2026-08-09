# Race Condition HTTP/2 Single-Packet Sync Reference

## 1. Escenarios Principales de Prueba

- **Doble Canje de Cupones**: Enviar 20 peticiones simultáneas de canje del mismo cupón promocional.
- **Transferencias Monetarias Múltiples**: Enviar peticiones concurrentes de retiro de fondos desde el mismo saldo disponible.

## 2. Remediación Segura

- Utilice bloqueos a nivel de fila de base de datos (`SELECT FOR UPDATE`) o semáforos/mutexes atómicos (Redis locks) durante la validación y ejecución de transacciones sensibles.
