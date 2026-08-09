---
name: bug-bounty-session-ip-binding
description: Auditoría de fijación de sesión y vinculación de dirección IP/huella digital de cliente. Verificación de políticas de revocación automática de tokens ante cambios de red.
---

# Skill: Session IP Binding & Fixation Assessment

Esta habilidad capacita al agente para evaluar los mecanismos de control de sesión en aplicaciones web y APIs, verificando si los identificadores de sesión (cookies o JWTs) quedan invalidados cuando cambia la dirección IP o la huella del navegador del cliente.

## 📌 Vectores de Pruebas de Sesión

### 1. Pruebas de Fijación de Sesión (Session Fixation)
- Iniciar sesión utilizando un identificador de sesión fijado previamente por un atacante antes de la autenticación.

### 2. Cambios de Red / IP Switching
- Utilizar una cookie de sesión válida desde una dirección IP o User-Agent diferente para comprobar si el servidor revoca la sesión.

---

## 📚 Referencias Técnicas

Consulta los detalles en:
[session-binding-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-session-ip-binding/references/session-binding-guide.md)
