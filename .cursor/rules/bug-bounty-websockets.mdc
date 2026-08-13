---
name: bug-bounty-websockets
description: Auditoría de seguridad en comunicaciones WebSocket. Cross-Site WebSocket Hijacking (CSWSH), falta de autenticación en handshake y filtración de mensajes bidireccionales.
---

# Skill: WebSocket Security & CSWSH Assessment

Esta habilidad instruye al agente sobre cómo evaluar la seguridad de la conexión bidireccional mediante WebSockets (`ws://` o `wss://`), verificando la autenticación del apretón de manos (handshake) y la protección contra secuestros de sesión en tiempo real.

## 📌 Vectores de Ataque en WebSockets

### 1. Cross-Site WebSocket Hijacking (CSWSH)
- Si el apretón de manos HTTP (`GET /socket HTTP/1.1`) utiliza únicamente cookies para autenticación y no valida la cabecera `Origin`, un sitio atacante puede iniciar una conexión WebSocket en segundo plano en nombre de la víctima.

### 2. Mensajes No Encriptados / Manipulación de Eventos
- Uso de `ws://` en lugar de `wss://` (TLS).
- Inyección de comandos o payloads de datos dentro de mensajes JSON formateados enviados sobre la conexión activa.

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[cswsh-attacks.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-websockets/references/cswsh-attacks.md)
