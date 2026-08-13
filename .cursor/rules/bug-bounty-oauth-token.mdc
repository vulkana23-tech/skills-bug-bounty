---
name: bug-bounty-oauth-token
description: Análisis de seguridad en flujos de autenticación OAuth 2.0 / OpenID Connect, extracción indebida de Access Tokens, robos de nonces, bypasses de redirect_uri y vulnerabilidades en postMessage/WebSockets.
---

# Skill: OAuth 2.0 & Token Hijacking Exploitation

Esta habilidad instruye al agente sobre cómo auditar implementaciones de OAuth 2.0 / SSO (Google, Facebook, Microsoft, Apple, GitHub), identificar fugas de tokens de acceso (`access_token`, `authorization_code`, `id_token`) y ejecutar secuestros de cuenta (Account Takeover).

## 📌 Principales Vectores de Ataque en OAuth 2.0

### 1. Bypass de Validación de `redirect_uri`
- **Path Traversal**: `https://victim.com/oauth/callback?redirect_uri=https://client.com/oauth/callback/../../attacker`
- **Bypass por Subdominio / Wildcard**: `https://attacker.client.com` o `https://client.com.attacker.com`
- **Inyección de Parámetros**: `https://client.com/callback?next=https://attacker.com`
- **Bypass via Open Redirect**: Si `client.com/redirect?url=attacker.com` existe, usarlo como `redirect_uri` para filtrar el token o código en el fragmento de la URL (`#access_token=...`).

### 2. Ausencia o Reutilización del Estado (`state` parameter - OAuth CSRF)
- Si la solicitud `/authorize` no incluye parámetro `state` aleatorio único ligado a la sesión, un atacante puede vincular su propia cuenta social a la cuenta de la víctima (Login CSRF).

### 3. Fuga de Tokens via `postMessage`
- En aplicaciones SPA que usan ventanas emergentes (`window.open`) para SSO:
  Verificar si la ventana receptora utiliza `postMessage(data, "*")` con el comodín `*` en lugar del origen exacto (`https://app.com`). Un sitio malicioso puede escuchar el evento `message` y robar el token devuelto.

---

## 📚 Referencias y Casos Reales (`ngalongc/bug-bounty-reference`)

Lee la documentación técnica sobre vulnerabilidades reales en Facebook, Periscope, Microsoft, Slack y LastPass:
[oauth-flaws.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-oauth-token/references/oauth-flaws.md)
