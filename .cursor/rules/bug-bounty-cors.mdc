---
name: bug-bounty-cors
description: Auditoría de configuraciones inseguras de Cross-Origin Resource Sharing (CORS). Detección de reflejo arbitrario de orígenes, Null Origin, subdominios no confiables y acceso credencializado.
---

# Skill: CORS Misconfiguration Assessment

Esta habilidad capacita al agente para evaluar la política CORS de la aplicación web y determinar si permite a dominios de terceros leer respuestas arbitrarias o datos confidenciales mediante JavaScript con credenciales de usuario (`Access-Control-Allow-Credentials: true`).

## 📌 Vectores Principales de CORS

### 1. Reflejo Arbitrario de Origen (Arbitrary Origin Reflection)
- Enviar encabezado: `Origin: https://attacker.com`
- Respuesta insegura:
  ```http
  Access-Control-Allow-Origin: https://attacker.com
  Access-Control-Allow-Credentials: true
  ```

### 2. Confianza en Origen `null` (Null Origin Trust)
- Enviar encabezado: `Origin: null`
- Útil al realizar peticiones dentro de un `iframe` con el atributo `sandbox="allow-scripts"`.

### 3. Wildcard de Origen con Subdominios / Prefijos
- `Origin: https://victim.com.attacker.com`
- `Origin: https://attacker-victim.com`

---

## 📚 Referencias Técnicas

Consulta la guía de mitigación en:
[cors-matrix.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-cors/references/cors-matrix.md)
