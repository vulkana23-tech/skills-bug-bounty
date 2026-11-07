---
name: obsidian-vault-search
description: Consulta semántica y búsqueda vectorial en el Segundo Cerebro de Obsidian sincronizado con Qdrant y Google Drive (Cyber-Vault). Utilizar para recuperar notas técnicas, vulnerabilidades documentadas, herramientas y auditorías.
---

# Obsidian Vault Vector Search (Qdrant)

Esta habilidad permite a los agentes de IA (Claude Code, OpenCode, Antigravity, Ollama) consultar instantáneamente la base de conocimiento personal en **Obsidian** (`G:\Mi unidad\Cyber-Vault`) mediante búsqueda vectorial en **Qdrant** acelerada por GPU.

## Métodos de Consulta

### 1. Vía Servidor MCP (`obsidian-qdrant`)
Registrado globalmente en Claude Desktop, Claude Code (`.mcp.json` y `~/.claude.json`), Cursor (`.cursor/mcp.json`) y OpenCode (`opencode.json`):
- `save_note_to_vault(title, content, category, tags, wikilinks)`: **Memoriza y guarda nueva información**. Crea la nota en Obsidian (Google Drive o espejo local) y la indexa al instante en Qdrant para todas las IAs.
- `search_vault(query, top_k)`: **Búsqueda semántica vectorial** en Obsidian con fallback automático si Ollama estuviera offline.
- `get_note_content(rel_path)`: **Lectura completa de notas** por ruta o título (ej: `01-Vulnerabilidades/Web/Bypass de Rate Limiting con GraphQL Aliases.md`).
- `list_vault_topics()`: Lista todos los temas y notas indexados en Qdrant.
- `sync_vault_now(force)`: Dispara la sincronización masiva y re-indexación desde `G:\Mi unidad\Cyber-Vault`.

### 2. Vía CLI Directo
Ejecuta la búsqueda semántica en la terminal:

```bash
rag/pentesting-everything/.venv/Scripts/python.exe vault_qdrant.py --query "<término o pregunta técnica>" --top 3
```

Ejemplos:
- `rag/pentesting-everything/.venv/Scripts/python.exe vault_qdrant.py --query "ataques a Kerberos y tickets AS-REP"`
- `rag/pentesting-everything/.venv/Scripts/python.exe vault_qdrant.py --query "desincronización HTTP request smuggling CL.TE"`

### 2. Vía API HTTP Local (CyberChat Microservicio)
Si el servidor CyberChat está corriendo en segundo plano:

```bash
curl -s "http://127.0.0.1:7860/api/vault/query?q=active+directory&top=3"
```

Respuesta JSON estructurada:
```json
{
  "ok": true,
  "query": "active directory",
  "matches": [
    {
      "score": 0.658,
      "title": "AS-REP Roasting",
      "rel_path": "01-Vulnerabilidades/Active-Directory/AS-REP Roasting.md",
      "tags": ["active-directory", "kerberos"],
      "wikilinks": ["Kerberos", "WhiteRabbitNeo"],
      "content": "..."
    }
  ]
}
```

### 3. Sincronización Manual o Forzada
Para forzar una re-indexación completa tras añadir o editar muchas notas en Obsidian:

```bash
rag/pentesting-everything/.venv/Scripts/python.exe vault_qdrant.py --sync
```
O vía API:
```bash
curl -X POST "http://127.0.0.1:7860/api/vault/sync"
```

