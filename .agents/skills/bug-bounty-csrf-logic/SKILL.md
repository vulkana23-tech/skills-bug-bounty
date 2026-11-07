---
name: bug-bounty-csrf-logic
description: Auditoría de Cross-Site Request Forgery (CSRF), condiciones de carrera (Race Conditions), bypasses de límites de uso/rate-limiting y fallos de lógica de negocio en transacciones o compras.
---

# Skill: CSRF, Race Conditions & Business Logic Flaws

Esta habilidad orienta al agente en el análisis de vulnerabilidades donde las garantías de integridad de la aplicación fallan por falta de verificación de tokens anti-CSRF, por ejecuciones concurrentes no atómicas (Race Conditions) o por fallos lógicos en flujos de trabajo financieros / de cupones.

## 📌 Metodología de Pruebas

### 1. Cross-Site Request Forgery (CSRF)
- Verificar si las solicitudes POST/PUT/DELETE sensibles dependen únicamente de Cookies de Sesión sin encabezado `SameSite=Strict` ni Tokens anti-CSRF únicos.
- **Bypasses de Token CSRF**:
  - Eliminar el parámetro del token por completo.
  - Enviar token vacío o sustituirlo por el token de otra sesión válida.
  - Cambiar el método HTTP de `POST` a `GET`.
  - Probar manipulación de Content-Type a `text/plain` o `application/x-www-form-urlencoded` para evitar peticiones preflight CORS (OPTIONS).

### 2. Race Conditions (Condiciones de Carrera / Concurrencia)
- **Escenarios**:
  - Canje múltiple de un único cupón de descuento promocional.
  - Transferencia doble de saldo o puntos de fidelidad.
  - Votaciones o me gusta duplicados.
  - Generación de múltiples tarjetas de regalo con una única compra.
- **Técnica Single-Packet Attack**: Enviar decenas de peticiones HTTP en paralelo asegurando que el último byte del paquete TCP viaje simultáneamente (usando herramientas como Burp Suite Turbo Intruder).

### 3. Business Logic Flaws (Fallos en Lógica de Negocio)
- **Precios negativos o cero**: Modificar `price=-100` o `quantity=-1` en peticiones de carrito de compras.
- **Omitir pasos en workflows**: Saltar el paso de pago llamando directamente a `POST /checkout/confirm` sin pasar por el gateway de pasarela de pago.

---

## 📚 Casos Históricos de Referencia (`ngalongc/bug-bounty-reference`)

Consulta detalles de exploits de PayPal y Messenger en:
[logic-race-conditions.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-csrf-logic/references/logic-race-conditions.md)
