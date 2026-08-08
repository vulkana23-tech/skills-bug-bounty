---
name: bug-bounty-content-injection
description: Detección y mitigación de inyección de contenido estático (Content Injection), suplantación de texto (Text Spoofing) y engaño de interfaz en aplicaciones web.
---

# Skill: Content & Text Injection Assessment

Esta habilidad capacita al agente para identificar vulnerabilidades donde una aplicación web refleja cadenas de texto arbitrarias dentro de la interfaz de usuario sin escapar caracteres especiales, permitiendo alterar el mensaje mostrado o desplegar texto engañoso para ingeniería social.

## 📌 Diagnóstico

### 1. Inyección de Texto / Text Spoofing
- Inyectar cadenas de texto en parámetros de error o búsqueda:
  `GET /login?error=System+Maintenance.+Please+send+your+credentials+to+admin@evil.com`
- Si la aplicación muestra: `"Error: System Maintenance. Please send your credentials to admin@evil.com"`, existe un **Text Injection / Content Spoofing**.

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[text-spoofing.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-content-injection/references/text-spoofing.md)
