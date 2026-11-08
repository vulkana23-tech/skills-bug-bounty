---
title: "T3MP3ST Meta-Harness"
tool_name: "T3MP3ST"
github_repo: "https://github.com/elder-plinius/T3MP3ST"
category: "Harness-Engineering"
language: "TypeScript / Node.js"
tags:
  - "herramienta"
  - "harness-engineering"
  - "red-team"
  - "multiagente"
  - "mcp"
  - "seguridad-ofensiva"
status: "Operativo"
---

# 🌩️ T3MP3ST — Meta-Arnés Ofensivo Multiagente & Servidor MCP

> [!NOTE] **Propósito Táctico**: Plataforma de Red Team autónomo que transforma cualquier asistente de codificación de IA local (Claude Code, Antigravity, Codex, Ollama) en un operador ofensivo de élite mediante una arquitectura multiagente coordinada.
> **Autor**: `Pliny the Prompter` (`@elder_plinius`) | **Licencia**: AGPL-3.0 | **Repositorio**: [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)

---

## ⚡ Arquitectura del Meta-Arnés
T3MP3ST no depende de un modelo LLM propietario ni de APIs de pago adicionales (*Keyless Warfare*); funciona como una **capa de meta-arnés (harness)** que orquesta un enjambre de 8 operadores especializados mapeados a MITRE ATT&CK:

1. **Recon**: Descubrimiento y huella digital pasiva/activa.
2. **Scanner**: Identificación de puertos, servicios y superficies de ataque.
3. **Exploiter**: Generación y prueba de PoCs benignos y específicos.
4. **Infiltrator**: Simulación de movimiento lateral y evaluación de privilegios.
5. **Exfiltrator**: Validación de impacto y rutas de exfiltración de datos.
6. **Ghost**: Técnicas de evasión de WAF/EDR y análisis de persistencia.
7. **Coordinator**: Orquestación de estado y turnos de trabajo entre agentes.
8. **Analyst**: Triaje de falsos positivos y síntesis del informe final.

---

## 🔌 Integración como Servidor MCP (Model Context Protocol)

T3MP3ST incluye soporte nativo MCP (`stdio`) en `src/mcp-server.ts`. Permite que agentes de IA en **DeepSeek Harness (DSH)**, **WorkBuddy AI**, **Claude Code** o **Antigravity** invoquen herramientas de seguridad directamente.

### 1. Herramientas MCP Expuestas
* **`security_recon`**: Reconocimiento de red que combina resoluciones DNS (`dig`) y escaneos de `nmap` con perfiles configurables (`quick`, `standard`, `full`, `stealth`).
  - *Validación estricta*: Todo objetivo es filtrado por la regex `^[A-Za-z0-9._:-]+$` impidiendo cualquier inyección de comandos en el shell.
* **`t3mp3st-chef-specials`**: Consulta programática de bases de datos de payloads, técnicas de evasión WAF (*Typhon*), escalada de privilegios (*Cerberus*) y detección de patrones de secretos (*Griffin*).

### 2. Configuración en Clientes MCP

#### En DeepSeek Harness (`~/.dsh/mcp-servers.json`):
```json
{
  "serverName": "t3mp3st",
  "transport": "stdio",
  "command": "node",
  "args": ["C:\\Users\\logir\\Projects\\T3MP3ST\\dist\\mcp-server.js"],
  "env": {},
  "enabled": true
}
```

#### En WorkBuddy AI (`~/.workbuddy-ai/mcp.json`):
```json
"t3mp3st": {
  "command": "node",
  "args": ["C:\\Users\\logir\\Projects\\T3MP3ST\\dist\\mcp-server.js"]
}
```

---

## 💻 Instalación y Despliegue Rápido
```bash
# 1. Clonar el repositorio
git clone https://github.com/elder-plinius/T3MP3ST.git
cd T3MP3ST

# 2. Instalar dependencias y compilar
npm install
npm run build

# 3. Lanzar la interfaz War Room (Web UI en http://127.0.0.1:3333/ui/)
npm run server

# 4. O probar el servidor MCP en consola:
npm run mcp:prod
```

---

## 🎯 Casos de Uso y Sinergia con Cyber-Vault
- **Auditorías de Laboratorio Autónomas**: Despliegue del enjambre contra entornos autorizados (CTFs, HackTheBox, VulnHub) con supervisión humana.
- **Inyección de Metodologías**: Alimenta a los operadores de T3MP3ST con los manuales de [[02-Metodologias/Tacticas-Bug-Bounty/]] de nuestra bóveda.
- **Conexión con Qdrant y CTI**: Correlación de telemetría de ataque con los boletines de [[05-Cyber-Intel/Boletin-Ciberseguridad-Defensiva|Los Vigilantes · v3]].

---
*Ficha táctica catalogada en la sección de Harness Engineering del Cyber-Vault.*