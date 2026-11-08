---
title: "Terminal MCP"
tool_name: "terminal-mcp"
github_repo: "https://github.com/JoasASantos/terminal-mcp"
category: "Seguridad-Ofensiva-Defensiva"
language: "TypeScript / Node.js"
tags:
  - "herramienta"
  - "mcp"
  - "terminal"
  - "reporting"
  - "screenshots"
  - "pentest"
status: "Operativo"
---

# 📸 Terminal MCP — Capturador Forense de Terminal & Generador de PoCs PNG

> [!NOTE] **Propósito Táctico**: Servidor MCP que ejecuta comandos en la terminal y renderiza automáticamente la salida como capturas de pantalla PNG de alta resolución con diseño profesional, colores ANSI de 24 bits, exit codes y metadatos.
> **Autor**: `Joas Antonio dos Santos` (`JoasASantos`) | **Repositorio**: [JoasASantos/terminal-mcp](https://github.com/JoasASantos/terminal-mcp)

---

## ⚡ Capacidades y Temas de Reporte
Terminal-MCP resuelve una necesidad crucial en Bug Bounty y auditorías: **generar evidencias visuales limpias (PoCs)** para plataformas como HackerOne, Bugcrowd y reportes ejecutivos sin intervención manual.

- **Preservación total de colores**: Soporta códigos ANSI de 16 colores, paleta de 256 colores y *truecolor* de 24 bits.
- **Marco de ventana profesional**: Renderizado headless vía Puppeteer emulando consolas modernas macOS/Linux.
- **20 Temas integrados**: *Tokyo Night, Dracula, Kali Linux, Gruvbox, Nord, GitHub Dark, Ubuntu*, etc.
- **Metadatos Forenses**: Marca de tiempo (*timestamp*), código de salida (*exit code*), títulos de comando y marcas de agua.

---

## 🔌 Conexión en Clientes MCP (Ya Configurado en tu Entorno)
- **Directorio de capturas**: `C:\Users\logir\Projects\terminal-screenshots`
- **Ruta de ejecución**: `node C:\Users\logir\Projects\terminal-mcp\dist\index.js`
- **Activo en**: Cursor, OpenCode, DeepSeek Harness y WorkBuddy AI.

---
*Ficha táctica catalogada para la base de conocimiento y orquestación de agentes de Cyber-Vault.*