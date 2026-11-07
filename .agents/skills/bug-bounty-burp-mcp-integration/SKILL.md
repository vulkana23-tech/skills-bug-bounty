---
name: bug-bounty-burp-mcp-integration
description: Configuración e integración de agentes de IA con Burp Suite vía REST API y servidor MCP para inspección de historial proxy, repetición de peticiones y análisis HTTP.
---

# Skill: Burp Suite MCP Integration

Esta habilidad permite a los agentes de IA interactuar directamente con Burp Suite Professional / Community mediante el servidor MCP (Model Context Protocol) o la API REST de Burp.

## 📌 Funcionalidades de la Integración

### 1. Inspección del Historial Proxy
- Filtrado y búsqueda de solicitudes HTTP en el historial proxy de Burp mediante consultas estructuradas.
- Inspección de cabeceras, cuerpos JSON/XML y códigos de respuesta.

### 2. Repetición y Fuzzing de Solicitudes (Repeater & Intruder)
- Envío de solicitudes modificadas directamente al módulo Repeater de Burp.
- Análisis comparativo de respuestas (`diffing`) tras modificar parámetros de autenticación.

---

## 📚 Referencias Técnicas

Consulta la guía de configuración del servidor Burp MCP en:
[burp-mcp-setup-guide.md](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-burp-mcp-integration/references/burp-mcp-setup-guide.md)
