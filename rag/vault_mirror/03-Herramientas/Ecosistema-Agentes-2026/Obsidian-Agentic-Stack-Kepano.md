---
title: El Ecosistema Agéntico Oficial de Obsidian (Stack de Kepano & Obsidian Team)
tags:
  - obsidian
  - kepano
  - agent-skills
  - claude-code
  - defuddle
  - knap
  - antigravity
date: 2026-11-07
version: v1.0.0
author: Steph Ango (Kepano) / Integrado por Antigravity
---

# 🧠 El Stack Agéntico Oficial de Obsidian: Por qué la IA debe escribir Obsidian Nativo

> "El propio CEO de Obsidian (Kepano) y su equipo hicieron open-source las herramientas que permiten a cualquier agente de IA (Claude Code, Antigravity, OpenCode, Codex) interactuar de forma nativa con tu bóveda de notas, consumiendo menos tokens y produciendo grafos reales de conocimiento."

---

## 1. El Problema del Markdown Genérico vs. Markdown Nativo
La mayoría de LLMs y agentes producen Markdown estándar plano. Cuando se les pide documentar en Obsidian:
- Usan enlaces HTML o enlaces estándar `[texto](url)` en vez de **Wikilinks nativos** `[[Nota]]` o `[[Nota#Encabezado|Alias]]`.
- No aprovechan los **Callouts** semánticos (`> [!NOTE]`, `> [!BUG]`, `> [!INFO]`).
- Ignoran las **Propiedades YAML (Frontmatter)** estructuradas para DataView o Bases.
- No generan diagramas interactivos **JSON Canvas (`.canvas`)** ni bases de datos relacionales locales **Obsidian Bases (`.base`)**.

El stack oficial liberado por **Kepano** resuelve esto convirtiendo a los agentes en operadores nativos de Obsidian desde el primer prompt.

---

## 2. Los 5 Componentes Esenciales del Ecosistema

### 1️⃣ `kepano/obsidian-skills` (El Paquete de Habilidades para Agentes)
Conjunto oficial de 6 habilidades bajo el estándar abierto **Agent Skills** (agentskills.io):

1. **`obsidian-markdown`**: Enseña al agente a redactar en *Obsidian Flavored Markdown*, respetando wikilinks, incrustaciones de imágenes/audio (`![[archivo]]`), notas al pie y propiedades normalizadas.
2. **`obsidian-bases`**: Creación y edición de archivos `.base` para modelar vistas, filtros relacionales, resúmenes y fórmulas en la bóveda.
3. **`json-canvas`**: Creación y modificación quirúrgica de archivos visuales `.canvas` (nodos de texto, enlaces, grupos y flechas direccionadas).
4. **`obsidian-cli`**: Interacción directa con bóvedas locales a través de la interfaz de línea de comandos oficial.
5. **`defuddle`**: Limpieza de páginas web para extraer únicamente el cuerpo del artículo en Markdown.
6. **`knap`**: Motor de plantillas (templates) para transformar datos estructurados JSON o CSV en notas Markdown masivas.

---

### 2️⃣ `kepano/defuddle` (Extractor Web Inteligente anti-quema de tokens)
- **Problema**: Cuando un agente descarga una página web mediante fetch o scraping convencional, se traga barras de navegación, popups de cookies, widgets sociales y anuncios (desperdiciando hasta el 80% de los tokens de contexto).
- **Solución**: `defuddle` procesa el DOM como un lector nativo y genera un Markdown minimalista con sólo el contenido relevante, metadatos y enlaces limpios.
- **Instalación Global**: `npm install -g defuddle`
- **Uso por el Agente**:
  ```bash
  defuddle parse https://ejemplo.com/articulo > nota.md
  ```

---

### 3️⃣ `obsidianmd/knap` (Templating Engine para Generación Masiva)
- **Propósito**: Renderizar plantillas Markdown alimentadas por variables JSON o registros CSV.
- **Instalación Global**: `npm install -g knap`
- **Ejemplo de Generación por Lotes**:
  ```bash
  knap batch template_cve.md --data cves_activos.json --output-dir ./Vulnerabilidades/
  ```

---

### 4️⃣ `obsidianmd/obsidian-importer` (Migración Universal sin Pérdida)
Plugin y herramienta oficial para traer el historial completo de conocimiento disperso en silos propietarios:
- **Fuentes soportadas**: Notion, Evernote, Apple Notes, Roam Research, Bear, OneNote, HTML, Google Keep.
- **Beneficio para la IA**: Unifica todo el historial previo en texto plano Markdown indexable en memoria semántica Qdrant y vectorial.

---

### 5️⃣ `obsidianmd/obsidian-help` & `AGENTS.md` (La Fuente de la Verdad)
La documentación oficial de Obsidian está escrita en Markdown puro y contiene su propio archivo de orquestación `AGENTS.md`. Esto permite clonar o consultar la documentación para que el agente aprenda inmediatamente cualquier cambio de sintaxis o función nueva sin alucinaciones.

---

## 3. Estado de Despliegue en Nuestro Sistema

Todas las herramientas y habilidades han sido desplegadas y verificadas:

| Componente | Ruta en el Sistema | Estado |
| :--- | :--- | :--- |
| **Skills en Cyber-Vault** | `G:\Mi unidad\Cyber-Vault\.claude\skills\` | ✅ Desplegado (Activo para Claude Code en la Bóveda) |
| **Skills Globales Claude** | `~/.claude/skills/` | ✅ Desplegado (Activo globalmente en Claude Code) |
| **Skills en Antigravity** | `~/.gemini/config/skills/` | ✅ Desplegado & Activo |
| **Repositorio Bug Bounty** | `integrations/obsidian-skills/` | ✅ Versionado en Git |
| **CLI Defuddle** | `npm install -g defuddle` (`defuddle parse`) | ✅ Instalado en PATH |
| **CLI Knap** | `npm install -g knap` (`knap render / batch`) | ✅ Instalado en PATH |

---

## 4. Guía Rápida para Claude Code & Antigravity

A partir de este momento, en cualquier conversación puedes pedir:
- *"Crea un Canvas con los vectores de ataque de este hallazgo"* -> Usará automáticamente **`json-canvas`**.
- *"Extrae el artículo de esta URL y guárdalo como nota sin barras laterales"* -> Usará **`defuddle`**.
- *"Genera notas individuales para cada dominio del CSV de Slack"* -> Usará **`knap batch`**.
- *"Crea una base de datos de los CVEs críticos"* -> Usará **`obsidian-bases`**.
- *"Escribe la nota técnica enlazando a las metodologías existentes"* -> Usará **`obsidian-markdown`** con Wikilinks `[[...]]` exactos.
