---
name: bug-bounty-account-takeover
description: Matriz completa de vectores de secuestro de cuenta (Account Takeover - ATO). Incluye ataques por restablecimiento de contraseña, OAuth leaks, session fixation, IDOR en perfiles y credenciales por defecto.
---

# Skill: Account Takeover (ATO) Playbook

Esta habilidad entrena al agente para consolidar y aplicar la suite completa de técnicas de secuestro de cuenta (ATO), clasificando la severidad como **Critical** y detallando el flujo de ataque exacto para los reportes de bug bounty.

## 📌 Vectores Principales de ATO

1. **Restablecimiento de Contraseña Inseguro (Password Reset Flaws)**:
   - Tokens de restablecimiento numéricos de 4 o 6 dígitos sin limitación de tasa (Rate Limiting).
   - Fuga del token de restablecimiento en la respuesta HTTP o en la URL de referer.
   - Modificación del ID de usuario o correo en la solicitud POST de restablecimiento (IDOR).
2. **Secuestro de Autenticación Social (OAuth ATO)**:
   - Fuga del `code` o `access_token` a un dominio atacante vía `redirect_uri` o `postMessage`.
   - Inexistencia de comprobación de correo verificado en logins con Google/Facebook (Pre-Account Takeover).
3. **Session Fixation & Session Management**:
   - Reutilización de cookies de sesión antiguas tras el cambio de contraseña o logout.
   - Tokens JWT firmados con clave débil (`none` algorithm o clave secreta descubierta por fuerza bruta).

---

## 📚 Playbook Completo y Casos HackerOne

Consulta el playbook y la matriz de reportes en:
[ato-playbook.md](file:///C:/Users/logir\.gemini\antigravity-ide\scratch\bug-bounty-skills\skills\bug-bounty-account-takeover\references\ato-playbook.md)
