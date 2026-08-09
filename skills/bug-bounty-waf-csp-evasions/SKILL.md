---
name: bug-bounty-waf-csp-evasions
description: Evasión avanzada de WAF y Content Security Policy (CSP). Uso de Script Gadgets en librerías comunes (AngularJS/JQuery), reutilización de Nonces y conectores Polyglots.
---

# Skill: WAF & CSP Advanced Evasion Techniques

Esta habilidad capacita al agente para evaluar políticas de seguridad de contenido (Content Security Policy - CSP) y Web Application Firewalls (WAF), identificando inconsistencias o gadgets de script que permitan ejecutar JavaScript legítimo en el navegador.

## 📌 Vectores de Evasión de CSP

- **Script Gadgets**: Explotar librerías JS confiables como AngularJS o jQuery cargadas en el dominio para ejecutar atributos de plantilla (`ng-app`, `ng-focus`).
- **Bypass de Nonce vía Dangling Markup**: Exfiltrar el token nonce mediante inyecciones HTML parciales antes de ejecutar el script.

---

## 📚 Referencias Técnicas

Consulta los gadgets en:
[csp-script-gadgets.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-waf-csp-evasions/references/csp-script-gadgets.md)
