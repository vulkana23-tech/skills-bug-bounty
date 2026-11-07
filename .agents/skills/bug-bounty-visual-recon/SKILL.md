---
name: bug-bounty-visual-recon
description: Reconocimiento visual y captura automatizada de pantallas (Visual Recon / Screenshotting). Uso de gowitness, aquatone y eyewitness para clasificación rápida de aplicaciones por interfaz gráfica.
---

# Skill: Visual Reconnaissance & Screenshotting

Esta habilidad capacita al agente para aplicar técnicas de reconocimiento visual sobre listas extensas de subdominios y direcciones IP, automatizando la captura de pantallas de aplicaciones web para identificar paneles de login, errores por defecto e interfaces administrativas.

## 📌 Metodología de Clasificación Visual

### 1. Captura Masiva de Pantallas
- Renderizar headless páginas HTTP/HTTPS con herramientas como `gowitness` o `aquatone`.

### 2. Agrupamiento por Similaridad Visual
- Agrupar capturas con estructuras idénticas para descartar rápidamente páginas predeterminadas de servidores (ej. páginas "Welcome to Nginx" o "IIS Default Page") y enfocar la atención en portales personalizados.

---

## 📚 Referencias Técnicas

Consulta los detalles en:
[visual-recon-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-visual-recon/references/visual-recon-guide.md)
