---
name: bug-bounty-rate-limit-bypass
description: Evaluación y omisión de controles de limitación de tasa (Rate Limiting) y protección contra fuerza bruta mediante manipulación de encabezados HTTP, GraphQL Aliases e IP Rotation.
---

# Skill: Rate Limit Bypass Assessment

Esta habilidad instruye al agente sobre cómo evaluar la robustez de las reglas de límite de velocidad en endpoints críticos (login, restablecimiento de contraseña, código 2FA, OTP por SMS).

## 📌 Vectores de Bypass de Límite de Velocidad

### 1. Manipulación de Encabezados de Redirección e IP Spoofing
- Probar modificar o alternar en cada solicitud los siguientes encabezados HTTP:
  - `X-Forwarded-For: 127.0.0.1` / `10.0.0.X`
  - `X-Client-IP: 10.0.0.X`
  - `X-Real-IP: 10.0.0.X`
  - `CF-Connecting-IP: 10.0.0.X`

### 2. Evasión por Normalización de URL / Case Sensitivity
- `POST /api/v1/login`
- `POST /API/V1/LOGIN`
- `POST /api/v1/login;` / `POST /api/v1/login?`

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[rate-limit-headers.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-rate-limit-bypass/references/rate-limit-headers.md)
