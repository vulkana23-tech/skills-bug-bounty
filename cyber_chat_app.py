#!/usr/bin/env python3
"""
CyberChat UI: Aplicación Web Local para Asistente de Ciberseguridad + RAG.
Conecta Ollama (WhiteRabbitNeo, Qwen2.5-Coder) con la memoria vectorial RAG.

Zero-dependencies: Funciona con la librería estándar de Python sin instalar nada extra.
Ejecución:
  python cyber_chat_app.py
"""
from __future__ import annotations

import json
import os
import re
import sys
import threading
import time
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PORT = 7860
OLLAMA_API_URL = "http://127.0.0.1:11434"

# Datasets RAG locales
DATASETS = [
    ROOT / "rag" / "offseccyber" / "chunks.jsonl",
    ROOT / "rag" / "vulnerability-notes" / "chunks.jsonl",
    ROOT / "rag" / "pentesting-everything" / "chunks.jsonl",
    ROOT / "rag" / "awesome-vehicle-security" / "chunks.jsonl",
]

CHUNKS_CACHE = []


def load_rag_cache():
    global CHUNKS_CACHE
    if CHUNKS_CACHE:
        return CHUNKS_CACHE
    chunks = []
    for path in DATASETS:
        if not path.exists():
            continue
        try:
            with path.open(encoding="utf-8") as f:
                for idx, line in enumerate(f):
                    if idx >= 4000:
                        break
                    try:
                        chunks.append(json.loads(line))
                    except Exception:
                        continue
        except Exception as e:
            print(f"[!] Error leyendo {path}: {e}", file=sys.stderr)
    CHUNKS_CACHE = chunks
    print(f"[+] Memoria RAG precargada: {len(CHUNKS_CACHE)} fragmentos.")
    return CHUNKS_CACHE


def search_rag(query: str, top_k: int = 3):
    chunks = load_rag_cache()
    tokens = [w.lower() for w in re.findall(r"\w+", query) if len(w) > 2]
    if not tokens:
        return []

    scored = []
    for c in chunks:
        content_low = c.get("content", "").lower()
        title_low = str(c.get("metadata", {}).get("document_title", "")).lower()
        tags = [t.lower() for t in c.get("tags", [])]

        score = 0
        for tok in tokens:
            if tok in title_low:
                score += 5
            if any(tok in t for t in tags):
                score += 3
            matches = content_low.count(tok)
            score += min(matches, 4)

        if score > 0:
            scored.append((score, c))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [c for _, c in scored[:top_k]]


OBSIDIAN_VAULT = Path("G:/Mi unidad/Cyber-Vault")


def search_obsidian_vault(query: str, top_k: int = 2):
    """Busca notas relevantes en tu bóveda personal de Obsidian usando Qdrant Vectorial + fallback léxico."""
    # 1. Intentar búsqueda semántica vectorial con Qdrant (bge-m3 / GPU)
    try:
        import vault_qdrant
        v_matches = vault_qdrant.query_vault(query, top_k=top_k, score_threshold=0.42)
        if v_matches:
            return [(m["stem"], m["rel_path"], m["content"]) for m in v_matches]
    except Exception as e:
        print(f"[!] Qdrant vector search fallback: {e}", file=sys.stderr)

    # 2. Fallback léxico en caso de que Qdrant esté sincronizándose
    if not OBSIDIAN_VAULT.exists():
        return []
    tokens = [w.lower() for w in re.findall(r"\w+", query) if len(w) > 2]
    if not tokens:
        return []
    scored = []
    try:
        for f in OBSIDIAN_VAULT.rglob("*.md"):
            if ".obsidian" in str(f):
                continue
            text = f.read_text(encoding="utf-8", errors="ignore")
            title_low = f.stem.lower()
            text_low = text.lower()
            score = 0
            for t in tokens:
                if t in title_low:
                    score += 6
                score += min(text_low.count(t), 4)
            if score > 0:
                rel = str(f.relative_to(OBSIDIAN_VAULT))
                scored.append((score, f.stem, rel, text))
    except Exception as e:
        print(f"[!] Error buscando en Obsidian: {e}", file=sys.stderr)
    scored.sort(key=lambda x: x[0], reverse=True)
    return [(stem, rel, content) for _, stem, rel, content in scored[:top_k]]


def live_web_search(query: str, max_results: int = 4):
    """Búsqueda web en vivo sin API keys utilizando el motor DuckDuckGo HTML."""
    import html
    import urllib.parse
    encoded = urllib.parse.quote(query)
    url = f"https://html.duckduckgo.com/html/?q={encoded}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    results = []
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            page = resp.read().decode("utf-8", errors="ignore")
        
        matches = re.findall(r'<a class="result__snippet[^"]*"[^>]*>(.*?)</a>', page, re.DOTALL)
        urls = re.findall(r'<a class="result__url"[^>]*href="([^"]+)"[^>]*>', page, re.DOTALL)
        
        for idx, m in enumerate(matches[:max_results]):
            clean = html.unescape(re.sub(r"<[^>]+>", "", m)).strip()
            link = urls[idx] if idx < len(urls) else "Web Result"
            if "uddg=" in link:
                match_u = re.search(r"uddg=([^&]+)", link)
                if match_u:
                    link = urllib.parse.unquote(match_u.group(1))
            if clean:
                results.append({"snippet": clean, "url": link})
    except Exception as e:
        print(f"[!] Error en búsqueda web: {e}", file=sys.stderr)
    return results


def get_installed_models():
    try:
        req = urllib.request.Request(f"{OLLAMA_API_URL}/api/tags")
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return [m.get("name") for m in data.get("models", [])]
    except Exception:
        return ["whiterabbitneo:latest", "qwen2.5-coder:7b"]


HTML_UI = r"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CyberChat - AI Pentesting & Security Assistant</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <style>
    :root {
      --bg: #0d1117;
      --panel: #161b22;
      --border: #30363d;
      --text: #e6edf3;
      --muted: #8b949e;
      --accent: #58a6ff;
      --accent-green: #238636;
      --user-bubble: #1f6feb22;
      --bot-bubble: #161b22;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; }
    body { background: var(--bg); color: var(--text); height: 100vh; display: flex; flex-direction: column; }
    
    /* Header */
    header {
      background: var(--panel);
      border-bottom: 1px solid var(--border);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .logo { display: flex; align-items: center; gap: 10px; font-weight: 700; font-size: 1.15rem; }
    .logo span { color: var(--accent); }
    .controls { display: flex; align-items: center; gap: 16px; }
    
    select, button {
      background: #21262d;
      color: var(--text);
      border: 1px solid var(--border);
      padding: 7px 12px;
      border-radius: 6px;
      font-size: 0.9rem;
      cursor: pointer;
    }
    select:focus, button:focus { outline: 1px solid var(--accent); }
    
    .toggle-rag {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.88rem;
      cursor: pointer;
      user-select: none;
    }
    .toggle-rag input { cursor: pointer; accent-color: var(--accent); }
    
    /* Chat Area */
    #chat-container {
      flex: 1;
      overflow-y: auto;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      max-width: 900px;
      width: 100%;
      margin: 0 auto;
    }
    .message {
      display: flex;
      flex-direction: column;
      max-width: 90%;
      line-height: 1.6;
      font-size: 0.96rem;
    }
    .message.user {
      align-self: flex-end;
      background: #1f6feb33;
      border: 1px solid #1f6feb66;
      padding: 12px 18px;
      border-radius: 12px 12px 2px 12px;
    }
    .message.bot {
      align-self: flex-start;
      background: var(--panel);
      border: 1px solid var(--border);
      padding: 16px 20px;
      border-radius: 12px 12px 12px 2px;
      width: 100%;
    }
    .sender-badge {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--muted);
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .sources-box {
      margin-top: 12px;
      padding: 10px 14px;
      background: #0d111788;
      border-left: 3px solid var(--accent);
      border-radius: 4px;
      font-size: 0.85rem;
    }
    .sources-box summary { font-weight: 600; cursor: pointer; color: var(--accent); }
    .sources-box ul { margin-top: 6px; padding-left: 20px; color: var(--muted); }
    
    pre {
      background: #0d1117;
      padding: 14px;
      border-radius: 8px;
      overflow-x: auto;
      margin: 10px 0;
      border: 1px solid var(--border);
    }
    code { font-family: "Fira Code", Consolas, monospace; font-size: 0.9em; }
    p { margin-bottom: 8px; }
    p:last-child { margin-bottom: 0; }
    
    /* Input Area */
    footer {
      background: var(--panel);
      border-top: 1px solid var(--border);
      padding: 16px 24px;
    }
    .input-box {
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      gap: 12px;
    }
    textarea {
      flex: 1;
      background: #0d1117;
      color: var(--text);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 16px;
      font-size: 1rem;
      resize: none;
      height: 52px;
      line-height: 1.4;
    }
    textarea:focus { outline: 1px solid var(--accent); }
    .send-btn {
      background: var(--accent-green);
      color: #fff;
      border: none;
      font-weight: 600;
      padding: 0 24px;
      border-radius: 8px;
      transition: opacity 0.2s;
    }
    .send-btn:hover { opacity: 0.9; }
    .send-btn:disabled { opacity: 0.5; cursor: not-allowed; }
  </style>
</head>
<body>

  <header>
    <div class="logo">
      🛡️ <span>CyberChat</span> Studio
    </div>
    <div class="controls">
      <label class="toggle-rag" title="Inyecta referencias de PortSwigger, HackerOne, Pentesting y Vehicle Sec">
        <input type="checkbox" id="rag-toggle" checked>
        <span>🛡️ Base RAG</span>
      </label>
      <label class="toggle-rag" title="Extracción web sigilosa con Scrapling (Anti-Bot / Bypass Cloudflare) y Agent-Reach (GitHub, Reddit)">
        <input type="checkbox" id="web-toggle">
        <span>🕷️ Web Sigilosa (Scrapling)</span>
      </label>
      <select id="model-select">
        <option value="whiterabbitneo:latest" selected>🐇 WhiteRabbitNeo 2.5 (Red Teaming / PoC)</option>
        <option value="qwen2.5-coder:7b">⚡ Qwen 2.5 Coder 7B (Auditoría Web & Código)</option>
        <option value="qwen2.5:14b">🧠 Qwen 2.5 14B (Razonamiento Profundo)</option>
      </select>
      <button id="cti-sync-btn" type="button" onclick="syncVigilantes()" style="background: #1f6feb; border-color: #388bfd; color: #fff; font-weight: 600;" title="Sincroniza los últimos boletines de Ciberinteligencia de Los Vigilantes · v3">📡 CTI Vigilantes</button>
      <a href="http://127.0.0.1:5173/?token=cybervault2026" target="_blank" style="text-decoration: none;">
        <button type="button" style="background: #238636; border-color: #2ea043; color: #fff; font-weight: 600;">📊 Grafo 3D</button>
      </a>
      <a href="http://127.0.0.1:7788" target="_blank" style="text-decoration: none;">
        <button type="button" style="background: #da3633; border-color: #f85149; color: #fff; font-weight: 600;" title="Panel Autónomo de Pentesting VulnClaw">🦞 VulnClaw</button>
      </a>
      <a href="http://127.0.0.1:5174/dashboard/" target="_blank" style="text-decoration: none;">
        <button type="button" style="background: #8957e5; border-color: #a371f7; color: #fff; font-weight: 600;" title="Orquestador Red Team y Grafos de Ataque ARES">⚔️ ARES</button>
      </a>
      <button onclick="clearChat()">🗑️ Limpiar</button>
    </div>
  </header>

  <div id="chat-container">
    <div class="message bot">
      <div class="sender-badge">Sistema</div>
      <div>¡Hola! Soy tu asistente local de ciberseguridad acelerado por tu GPU RTX 3060. Estoy potenciado por tu base de conocimiento local (<strong>24.700+ recursos RAG</strong>) y equipado con <strong>Scrapling</strong> (extracción web sigilosa indetectable con bypass de Cloudflare) y <strong>Agent-Reach</strong> (inteligencia técnica en GitHub, Reddit y comunidades). Puedes pegarme enlaces directos a repositorios o páginas web, o pedirme investigar temas en vivo. ¿En qué auditoría vamos a trabajar hoy?</div>
    </div>
  </div>

  <footer>
    <div class="input-box">
      <textarea id="prompt-input" placeholder="Haz una pregunta técnica, pega un fragmento de código o solicita un payload... (Enter para enviar, Shift+Enter para nueva línea)" onkeydown="handleKey(event)"></textarea>
      <button class="send-btn" id="send-btn" onclick="sendMessage()">Enviar</button>
    </div>
  </footer>

  <script>
    const chatContainer = document.getElementById('chat-container');
    const promptInput = document.getElementById('prompt-input');
    const sendBtn = document.getElementById('send-btn');
    const modelSelect = document.getElementById('model-select');
    const ragToggle = document.getElementById('rag-toggle');
    const webToggle = document.getElementById('web-toggle');

    function handleKey(e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
      }
    }

    function clearChat() {
      chatContainer.innerHTML = '';
    }

    async function syncVigilantes() {
      const btn = document.getElementById('cti-sync-btn');
      btn.disabled = true;
      btn.textContent = '⏳ Sincronizando CTI...';
      try {
        const res = await fetch('/api/vigilantes/sync', { method: 'POST' });
        const d = await res.json();
        if (d.ok) {
          btn.textContent = '✅ CTI Actualizado';
          setTimeout(() => { btn.textContent = '📡 CTI Vigilantes'; btn.disabled = false; }, 3000);
        } else {
          btn.textContent = '❌ Error Sync';
          setTimeout(() => { btn.textContent = '📡 CTI Vigilantes'; btn.disabled = false; }, 3000);
        }
      } catch(e) {
        btn.textContent = '❌ Error';
        setTimeout(() => { btn.textContent = '📡 CTI Vigilantes'; btn.disabled = false; }, 3000);
      }
    }

    async function sendMessage() {
      const text = promptInput.value.trim();
      if (!text) return;

      promptInput.value = '';
      sendBtn.disabled = true;

      // User Bubble
      const userMsg = document.createElement('div');
      userMsg.className = 'message user';
      userMsg.textContent = text;
      chatContainer.appendChild(userMsg);

      // Bot Bubble
      const botMsg = document.createElement('div');
      botMsg.className = 'message bot';
      const senderBadge = document.createElement('div');
      senderBadge.className = 'sender-badge';
      senderBadge.textContent = modelSelect.value.split(':')[0].toUpperCase();
      botMsg.appendChild(senderBadge);

      const contentBox = document.createElement('div');
      contentBox.className = 'content';
      contentBox.innerHTML = '<em>Consultando conocimiento y razonando...</em>';
      botMsg.appendChild(contentBox);
      chatContainer.appendChild(botMsg);
      chatContainer.scrollTop = chatContainer.scrollHeight;

      try {
        const res = await fetch('/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            prompt: text,
            model: modelSelect.value,
            use_rag: ragToggle.checked,
            use_web: webToggle.checked
          })
        });

        const data = await res.json();
        contentBox.innerHTML = marked.parse(data.response || 'Sin respuesta.');

        if (data.sources && data.sources.length > 0) {
          const sourcesBox = document.createElement('details');
          sourcesBox.className = 'sources-box';
          const summary = document.createElement('summary');
          summary.textContent = `📚 Fuentes Técnicas Consultadas (${data.sources.length})`;
          sourcesBox.appendChild(summary);

          const ul = document.createElement('ul');
          data.sources.forEach(s => {
            const li = document.createElement('li');
            li.textContent = s;
            ul.appendChild(li);
          });
          sourcesBox.appendChild(ul);
          botMsg.appendChild(sourcesBox);
        }

        // Highlight code
        botMsg.querySelectorAll('pre code').forEach((el) => {
          hljs.highlightElement(el);
        });

        // Botón para Guardar la Respuesta directamente en Obsidian
        const saveBar = document.createElement('div');
        saveBar.style.cssText = 'margin-top: 10px; display: flex; gap: 8px;';
        const saveBtn = document.createElement('button');
        saveBtn.style.cssText = 'background: #21262d; border: 1px solid var(--border); color: #58a6ff; padding: 5px 12px; font-size: 0.8rem; border-radius: 6px; cursor: pointer; transition: all 0.2s;';
        saveBtn.textContent = '💾 Guardar en Obsidian (Google Drive)';
        saveBtn.onclick = async () => {
          saveBtn.disabled = true;
          saveBtn.textContent = '⏳ Guardando en Obsidian...';
          try {
            const firstLine = text.split('\n')[0].replace(/[#*`[\]]/g, '').trim().slice(0, 45) || 'Nota-Cyber';
            const sRes = await fetch('/api/save_obsidian', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                title: firstLine,
                content: data.response,
                folder: '00-Inbox'
              })
            });
            const sData = await sRes.json();
            if (sData.ok) {
              saveBtn.textContent = `✅ Guardada en ${sData.path}`;
              saveBtn.style.borderColor = 'var(--accent-green)';
              saveBtn.style.color = '#3fb950';
            } else {
              saveBtn.textContent = '❌ Error al guardar';
            }
          } catch(e) {
            saveBtn.textContent = '❌ Error al conectar';
          }
        };
        saveBar.appendChild(saveBtn);
        botMsg.appendChild(saveBar);

      } catch (err) {
        contentBox.innerHTML = `<span style="color: #f85149;">Error de conexión con el servidor local: ${err}</span>`;
      } finally {
        sendBtn.disabled = false;
        chatContainer.scrollTop = chatContainer.scrollHeight;
        promptInput.focus();
      }
    }
  </script>
</body>
</html>
"""


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path.startswith("/?"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_UI.encode("utf-8"))
        elif self.path == "/api/models":
            models = get_installed_models()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(models).encode("utf-8"))
        elif self.path.startswith("/api/vault/query"):
            import urllib.parse
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)
            q = params.get("q", [""])[0]
            top_k = int(params.get("top", ["3"])[0])
            try:
                import vault_qdrant
                matches = vault_qdrant.query_vault(q, top_k=top_k)
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True, "query": q, "matches": matches}, ensure_ascii=False).encode("utf-8"))
            except Exception as ex:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(ex)}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/chat":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            req_data = json.loads(body)

            user_prompt = req_data.get("prompt", "")
            model = req_data.get("model", "whiterabbitneo:latest")
            use_rag = req_data.get("use_rag", True)
            use_web = req_data.get("use_web", False)

            sources_list = []
            context_blocks = []

            # 1. Detección automática de URLs en el prompt (Deep Stealth Scraping: Scrapling + Agent-Reach)
            url_matches = re.findall(r"https?://[^\s<>\"']+", user_prompt)
            if url_matches:
                try:
                    import stealth_intel
                    for u in url_matches[:2]:
                        intel = stealth_intel.smart_fetch(u, max_chars=8000)
                        if intel.get("ok") and intel.get("content"):
                            eng = intel.get("engine", "web")
                            icon = "🕷️ [Scrapling Stealth]" if eng == "scrapling" else "⚡ [Agent-Reach]"
                            title = intel.get("title") or u
                            sources_list.append(f"{icon} {title} ({u})")
                            context_blocks.append(f"--- CONTENIDO WEB EN VIVO ({icon} | {u}) ---\n{intel['content']}")
                except Exception as ex:
                    print(f"[!] Error procesando URL con stealth_intel: {ex}", file=sys.stderr)

            # 2. Búsqueda en memoria RAG local y Bóveda Obsidian
            if use_rag:
                # 2.1 Buscar en notas personales de Obsidian (Google Drive)
                obs_notes = search_obsidian_vault(user_prompt, top_k=2)
                for o_stem, o_rel, o_text in obs_notes:
                    sources_list.append(f"📓 [Bóveda Obsidian] {o_stem} ({o_rel})")
                    context_blocks.append(f"--- NOTA DE TU BÓVEDA OBSIDIAN: {o_stem} ({o_rel}) ---\n{o_text[:1400]}")

                # 2.2 Buscar en 24,700+ vectores técnicos locales
                chunks = search_rag(user_prompt, top_k=3)
                for idx, c in enumerate(chunks, 1):
                    m = c.get("metadata", {})
                    title = m.get("document_title") or c.get("domain") or "Doc"
                    src = m.get("source_path") or m.get("training_source") or "RAG"
                    sources_list.append(f"🛡️ [RAG Local] {title} ({src})")
                    context_blocks.append(f"--- REFERENCIA LOCAL {idx}: {title} ---\n{c['content'][:1200]}")

            # 3. Búsqueda web en vivo (si el usuario la activa y no pegó URLs directas)
            if use_web and not url_matches:
                try:
                    import stealth_intel
                    search_res = stealth_intel.smart_fetch(user_prompt, max_chars=6000)
                    if search_res.get("ok") and search_res.get("content"):
                        sources_list.append(f"🌐 [Web Stealth] {search_res.get('title', 'Búsqueda')} ({search_res.get('url', '')})")
                        context_blocks.append(f"--- RESULTADOS DE INVESTIGACIÓN WEB ---\n{search_res['content']}")
                    else:
                        web_results = live_web_search(user_prompt, max_results=3)
                        for w_idx, res in enumerate(web_results, 1):
                            sources_list.append(f"🌐 [Web en Vivo] {res['url']}")
                            context_blocks.append(f"--- RESULTADO WEB {w_idx} ({res['url']}) ---\n{res['snippet']}")
                except Exception as ex:
                    print(f"[!] Error en búsqueda web: {ex}", file=sys.stderr)
                    web_results = live_web_search(user_prompt, max_results=3)
                    for w_idx, res in enumerate(web_results, 1):
                        sources_list.append(f"🌐 [Web en Vivo] {res['url']}")
                        context_blocks.append(f"--- RESULTADO WEB {w_idx} ({res['url']}) ---\n{res['snippet']}")

            context_text = "\n\n".join(context_blocks)

            # Cargar Master Prompt si está disponible
            master_file = ROOT / "prompts" / "whiterabbitneo_master.txt"
            if master_file.exists():
                system_instruction = master_file.read_text(encoding="utf-8").strip()
            else:
                system_instruction = (
                    "Eres WHITERABBITNEO, actuando como un instructor experto en ciberseguridad ofensiva ética. "
                    "Responde siempre en ESPAÑOL fluido, con profundidad técnica, código completo y la estructura estándar."
                )

            if context_text:
                full_prompt = (
                    f"{system_instruction}\n\n"
                    f"### REFERENCIAS TÉCNICAS (RAG / Web en Vivo):\n{context_text}\n\n"
                    f"### CONSULTA DEL USUARIO:\n{user_prompt}\n\n"
                    "### RESPUESTA ESTÁNDAR (EN ESPAÑOL):"
                )
            else:
                full_prompt = (
                    f"{system_instruction}\n\n"
                    f"### CONSULTA DEL USUARIO:\n{user_prompt}\n\n"
                    "### RESPUESTA ESTÁNDAR (EN ESPAÑOL):"
                )

            ollama_req_data = json.dumps({
                "model": model,
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 1800,
                }
            }).encode("utf-8")

            try:
                ollama_req = urllib.request.Request(
                    f"{OLLAMA_API_URL}/api/generate",
                    data=ollama_req_data,
                    headers={"Content-Type": "application/json"}
                )
                with urllib.request.urlopen(ollama_req, timeout=120) as resp:
                    resp_data = json.loads(resp.read().decode("utf-8"))
                    answer = resp_data.get("response", "")
            except Exception as e:
                answer = f"Error comunicando con Ollama: {e}"

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({
                "response": answer,
                "sources": sources_list
            }, ensure_ascii=False).encode("utf-8"))
        elif self.path == "/api/save_obsidian":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            req_data = json.loads(body)
            raw_title = req_data.get("title", "Nota-Cyber")
            content = req_data.get("content", "")
            folder_name = req_data.get("folder", "00-Inbox")

            safe_title = re.sub(r'[\\/*?:"<>|]', "", raw_title).strip()
            if not safe_title:
                safe_title = f"Nota-{int(time.time())}"

            target_dir = OBSIDIAN_VAULT / folder_name
            target_dir.mkdir(parents=True, exist_ok=True)
            note_file = target_dir / f"{safe_title}.md"

            now_str = time.strftime("%Y-%m-%d %H:%M:%S")
            md_content = f"""---
title: "{safe_title}"
date: {now_str}
tags:
  - cyber
  - ai-generated
  - whiterabbitneo
vault_path: "{folder_name}/{safe_title}.md"
---

# {safe_title}

> Guardado desde CyberChat AI (GPU RTX 3060) el {now_str}.
> Relacionado con: [[00-Indice]]

{content}
"""
            try:
                note_file.write_text(md_content, encoding="utf-8")
                rel_path = f"{folder_name}/{safe_title}.md"

                # Sincronizar automáticamente en segundo plano hacia Qdrant
                def _bg_sync():
                    try:
                        time.sleep(0.5)
                        import vault_qdrant
                        vault_qdrant.sync_vault()
                    except Exception as ex:
                        print(f"[!] Error auto-sync Qdrant: {ex}", file=sys.stderr)
                threading.Thread(target=_bg_sync, daemon=True).start()

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True, "path": rel_path}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(e)}).encode("utf-8"))
        elif self.path == "/api/vault/sync":
            try:
                import vault_qdrant
                res = vault_qdrant.sync_vault()
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(res, ensure_ascii=False).encode("utf-8"))
            except Exception as ex:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(ex)}).encode("utf-8"))
        elif self.path == "/api/vigilantes/sync":
            try:
                import sync_vigilantes_intel
                res = sync_vigilantes_intel.sync_vigilantes(force_qdrant=True)
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(res, ensure_ascii=False).encode("utf-8"))
            except Exception as ex:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(ex)}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # Silenciar logs HTTP estándar en consola para mantenerla limpia


def run_server():
    server = ThreadingHTTPServer(("127.0.0.1", PORT), RequestHandler)
    print(f"\n" + "=" * 60)
    print(f"🛡️  CyberChat UI iniciada con éxito.")
    print(f"🌐  Abre tu navegador en: http://localhost:{PORT}")
    print(f"   Modelos listos: WhiteRabbitNeo 2.5 & Qwen 2.5 Coder")
    print(f"   Presiona Ctrl + C en esta consola para detener la app.")
    print("=" * 60 + "\n")

    # Abrir navegador automáticamente tras 1 segundo
    threading.Thread(target=lambda: (time.sleep(1), webbrowser.open(f"http://localhost:{PORT}")), daemon=True).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido. ¡Hasta pronto!")


if __name__ == "__main__":
    load_rag_cache()
    run_server()

