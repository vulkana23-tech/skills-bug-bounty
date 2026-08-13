---
name: bug-bounty-jwt-security
description: Auditoría de seguridad en JSON Web Tokens (JWT). Diagnóstico de omisión de firma (alg: none), inyección de claves públicas (JKU/JWKS), confusión de clave simétrica/asimétrica (HMAC vs RSA) y ataques de kid injection.
---

# Skill: JSON Web Token (JWT) Security Assessment

Esta habilidad entrena al agente para analizar la implementación de tokens JWT en aplicaciones web, APIs y microservicios, asegurando que la verificación de firma sea criptográficamente robusta.

## 📌 Estructura del Token JWT
Un token JWT consta de 3 partes codificadas en Base64URL separadas por puntos:
`Header.Payload.Signature`

---

## 🛠️ Diagnóstico de Fallos de Firma

### 1. Algoritmo `none` (Unsigned Tokens)
- Modificar el header JSON para establecer `"alg": "none"` o `"alg": "NONE"`.
- Eliminar la tercera sección (la firma) dejando el punto final: `eyJhb...eyJ1...`

### 2. Confusión de Algoritmo (RSA to HMAC Attack)
- Si el servidor espera una clave pública RSA (RS256) para verificar la firma, probar cambiar el header a `"alg": "HS256"` y firmar el token localmente utilizando la clave pública disponible comercialmente como el secreto simétrico HMAC.

### 3. Inyección en Encabezado `jku` / `jwks_uri` / `kid`
- **`jku` Injection**: Apuntar `"jku"` a un servidor remoto controlado por el auditor que sirva una clave pública falsa.
- **`kid` Injection (Path Traversal / SQLi)**:
  - `"kid": "../../../dev/null"` (si la clave secreta resulta estar vacía).
  - `"kid": "key' UNION SELECT 'secret'--"`

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[jwt-attacks.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-jwt-security/references/jwt-attacks.md)
