# Open Redirect Bypass Matrix & HackerOne Cases

## Top Disclosed Open Redirect Reports (HackerOne Index)

- **Twitter Open Redirect to OAuth Token Theft ($2,500 Bounty)**: Encadenamiento de un Open Redirect en `twitter.com` para filtrar tokens OAuth en la URL.
- **Shopify Open Redirect via Double Slash ($1,500 Bounty)**: Bypass de filtro de URL permitiendo redirección arbitraria mediante `//evil.com`.
- **HackerOne Open Redirect via Parameter Injection ($1,000 Bounty)**: Manipulación de parámetros de redirección tras flujos de autenticación.

## Encadenamiento de Vulnerabilidades (Chaining)

```
[Open Redirect] + [OAuth Flow] ==> Steal Access Token / Account Takeover
[Open Redirect] + [DOM XSS Sink] ==> Exec JS Payload
[Open Redirect] + [SSRF Endpoint] ==> Internal Network Recon
```
