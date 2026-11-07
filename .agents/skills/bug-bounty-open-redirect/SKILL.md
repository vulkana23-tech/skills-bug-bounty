---
name: bug-bounty-open-redirect
description: Detección y evasión de filtros en vulnerabilidades Open Redirect. Incluye técnicas para encadenar redirecciones hacia XSS, OAuth Token Hijacking y ataques de Phishing.
---

# Skill: Open Redirect Exploitation & Chaining

Esta habilidad instruye al agente sobre cómo identificar y evadir filtros en endpoints que redirigen a los usuarios a sitios externos sin una lista blanca estricta de dominios permitidos.

## 📌 Parámetros Típicos
`redirect=`, `url=`, `next=`, `target=`, `r=`, `checkout_url=`, `return_to=`, `dest=`, `goto=`, `out=`.

---

## 🛠️ Matriz de Bypass de Filtros de Redirección

1. **Doble Slash / Protocol-Relative**:
   - `//attacker.com`
   - `/\attacker.com` / `\\attacker.com`
2. **Manipulación de Autoridad de URL / Caracteres Especiales**:
   - `https://expected.com@attacker.com`
   - `https://attacker.com#expected.com`
   - `https://attacker.com?expected.com`
3. **Encoding & Null Byte**:
   - `https%3A%2F%2Fattacker.com`
   - `https://attacker.com%2523expected.com`
4. **Bypass por IP / Subdominio**:
   - `https://expected.com.attacker.com`

---

## 📚 Referencias y Caso de Uso en HackerOne Reports

Consulta las técnicas avanzadas en:
[redirect-bypass-matrix.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-open-redirect/references/redirect-bypass-matrix.md)
