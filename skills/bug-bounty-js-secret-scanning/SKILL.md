---
name: bug-bounty-js-secret-scanning
description: Escaneo de secretos, tokens de API y credenciales hardcoded en archivos JavaScript. Uso de SecretFinder y patrones Regex para detectar claves AWS, Firebase, JWT y Stripe.
---

# Skill: JavaScript Secret & Key Scanning

Esta habilidad capacita al agente para escanear el contenido fuente de scripts JavaScript servidos en producción en búsqueda de claves de API privadas, tokens de autenticación hardcoded y credenciales de servicios integrados.

## 📌 Patrones de Claves a Monitorear

- **Firebase Config**: `apiKey:\s*["'][A-Za-z0-9_-]{39}["']`
- **Stripe Public/Secret Key**: `(pk|sk)_(live|test)_[0-9a-zA-Z]{24}`
- **JWT Hardcoded Tokens**: `eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+`

---

## 📚 Referencias Técnicas

Consulta los patrones de expresión regular en:
[secretfinder-regex.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-js-secret-scanning/references/secretfinder-regex.md)
