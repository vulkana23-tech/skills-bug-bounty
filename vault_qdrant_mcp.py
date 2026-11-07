#!/usr/bin/env python3
"""
vault_qdrant_mcp.py - Servidor MCP de Memoria Vectorial Obsidian + Qdrant
Expone la base de conocimiento de Obsidian (Cyber-Vault) como herramientas MCP (Model Context Protocol)
para Claude Desktop, Claude Code, Cursor, OpenCode y Codex.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

os.environ.setdefault("FASTMCP_CHECK_FOR_UPDATES", "off")
os.environ.setdefault("FASTMCP_SHOW_SERVER_BANNER", "false")
os.environ.setdefault("FASTMCP_LOG_LEVEL", "ERROR")
os.environ.setdefault("NO_PROXY", "127.0.0.1,localhost")

from fastmcp import FastMCP
import qdrant_client
from qdrant_client import models

# Directorios de referencia
WORKSPACE_ROOT = Path(__file__).resolve().parent
DB_PATH = WORKSPACE_ROOT / "rag" / "qdrant_db"
DEFAULT_VAULT = Path("G:/Mi unidad/Cyber-Vault")
COLLECTION_NAME = "cyber_vault"

# Inicializar FastMCP
mcp = FastMCP("obsidian-qdrant-memory", instructions="Memoria semántica vectorial y acceso al Cyber-Vault de Obsidian mediante Qdrant.")


def get_client(max_wait: float = 8.0) -> qdrant_client.QdrantClient:
    """Abre Qdrant embebido local; si hay QDRANT_URL intenta servidor y si no responde cae al local embebido."""
    import time
    deadline = time.time() + max_wait
    while True:
        try:
            url = os.environ.get("QDRANT_URL")
            if url:
                try:
                    c = qdrant_client.QdrantClient(
                        url=url,
                        api_key=os.environ.get("QDRANT_API_KEY") or None,
                        timeout=2.0,
                        check_compatibility=False
                    )
                    c.get_collections()
                    return c
                except Exception:
                    # Si el servidor Qdrant en puerto 6333 no está corriendo, usar la BD local embebida
                    pass
            return qdrant_client.QdrantClient(path=str(DB_PATH))
        except Exception as e:
            if time.time() >= deadline:
                raise RuntimeError(
                    f"Qdrant bloqueado por otro proceso (otro agente/app usando rag/qdrant_db): {e}"
                )
            time.sleep(0.5)


_OLLAMA_DOWN_UNTIL = 0.0


def get_embedding_safe(text: str) -> Optional[List[float]]:
    """Embedding con Ollama solo si responde rápido; si no, None (fallback léxico).
    Si Ollama falla, no se reintenta durante 120 s para no bloquear al agente."""
    global _OLLAMA_DOWN_UNTIL
    import socket
    import time
    import urllib.request
    if time.time() < _OLLAMA_DOWN_UNTIL:
        return None
    url = os.environ.get("OLLAMA_API_URL", "http://127.0.0.1:11434")
    try:
        host, port = url.split("//", 1)[1].split(":")[0], int(url.rsplit(":", 1)[1].split("/")[0])
        socket.create_connection((host, port), timeout=1.0).close()
        body = json.dumps({"model": "bge-m3", "prompt": text[:4000], "keep_alive": -1}).encode("utf-8")
        req = urllib.request.Request(
            f"{url}/api/embeddings", data=body, headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=8) as resp:
            vec = json.loads(resp.read().decode("utf-8")).get("embedding", [])
        return vec or None
    except Exception:
        _OLLAMA_DOWN_UNTIL = time.time() + 120
        return None


def _todos_los_puntos(client):
    pts, offset = [], None
    while True:
        lote, offset = client.scroll(collection_name=COLLECTION_NAME, limit=512, offset=offset,
                                     with_payload=True, with_vectors=False)
        pts.extend(lote)
        if offset is None:
            return pts


_VACIAS = set("""a al algo algun alguna ante antes como cómo con contra cual cuál cuando de del desde donde dónde e el él ella en entre era es esa ese eso esta está este esto estos ha hay la las le les lo los mas más me mi mis muy ni no nos o os para pero por porque que qué se ser si sí sin sobre su sus tambien también te tu tus un una uno unos unas y ya yo
the a an and or of to in on for with by from is are was be it this that as at how what which who why when where do does can not no into about""".split())


def _tokens(texto: str) -> List[str]:
    # Conserva terminos tecnicos completos: CVE-2024-1234, as-rep, t1558.004, x-forwarded-for
    return [t.lower() for t in re.findall(r"[\w][\w.\-]*[\w]|\w", texto) if len(t) > 1]


@mcp.tool()
def search_vault(query: str, top_k: int = 5, tag: str = "", folder: str = "", min_score: float = 0.45) -> str:
    """
    Busqueda HIBRIDA en la memoria de Obsidian / Qdrant:
    - Semantica (vectores bge-m3): encuentra notas por significado.
    - Lexica (palabras exactas, tipo BM25): encuentra CVEs, nombres de herramientas, IDs, comandos.
    Ambas se combinan (Reciprocal Rank Fusion) y se devuelve una sola entrada por nota.
    Filtros opcionales: tag="kerberos" (etiqueta), folder="01-Vulnerabilidades" (carpeta/prefijo de ruta).
    min_score: relevancia semantica minima (0-1) para aceptar un resultado sin coincidencia exacta.
    """
    import math
    client = get_client()
    try:
        if not client.collection_exists(COLLECTION_NAME):
            return f"Coleccion '{COLLECTION_NAME}' no encontrada."

        tag_f = tag.strip().lstrip("#").lower()
        folder_f = folder.strip().strip("/").replace("\\", "/").lower()

        def pasa_filtros(p):
            if tag_f and tag_f not in [str(t).lower() for t in p.get("tags", [])]:
                return False
            if folder_f and not str(p.get("rel_path", "")).lower().startswith(folder_f):
                return False
            return True

        candidatos = {}  # id -> dict

        def registrar(pid, payload):
            if pid not in candidatos:
                candidatos[pid] = {"p": payload, "dense": None, "lex": 0.0}
            return candidatos[pid]

        # 1. Semantica
        rank_dense = []
        vec = get_embedding_safe(query)
        if vec:
            res = client.query_points(collection_name=COLLECTION_NAME, query=vec, limit=60, with_payload=True)
            for r in getattr(res, "points", []):
                p = r.payload or {}
                if not pasa_filtros(p):
                    continue
                c = registrar(r.id, p)
                c["dense"] = round(r.score, 4)
                rank_dense.append(r.id)

        # 2. Lexica (BM25 simplificado sobre todos los fragmentos)
        q_terms = [t for t in dict.fromkeys(_tokens(query)) if t not in _VACIAS]
        rank_lex = []
        if q_terms:
            puntos = [pt for pt in _todos_los_puntos(client) if pasa_filtros(pt.payload or {})]
            docs = []
            for pt in puntos:
                p = pt.payload or {}
                txt = " ".join([str(p.get("title", ""))] * 3 + [" ".join(map(str, p.get("tags", [])))] * 2 + [str(p.get("text", ""))])
                docs.append((pt, _tokens(txt), txt.lower()))
            n = len(docs) or 1
            avgdl = sum(len(d[1]) for d in docs) / n if docs else 1
            df = {t: sum(1 for d in docs if t in d[1]) for t in q_terms}
            frase = query.lower().strip()
            puntuados = []
            for pt, toks, low in docs:
                sc = 0.0
                for t in q_terms:
                    tf = toks.count(t)
                    if tf:
                        idf = math.log(1 + (n - df[t] + 0.5) / (df[t] + 0.5))
                        sc += idf * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * len(toks) / avgdl))
                if len(q_terms) > 1 and frase in low:
                    sc *= 1.5  # bonus por frase exacta
                if sc > 0:
                    puntuados.append((sc, pt))
            puntuados.sort(key=lambda x: x[0], reverse=True)
            for sc, pt in puntuados[:60]:
                c = registrar(pt.id, pt.payload or {})
                c["lex"] = round(sc, 2)
                rank_lex.append(pt.id)

        # 3. Fusion RRF + umbral + una entrada por nota
        rrf = {}
        for lista in (rank_dense, rank_lex):
            for pos, pid in enumerate(lista):
                rrf[pid] = rrf.get(pid, 0.0) + 1.0 / (60 + pos + 1)
        # Corte relativo: solo entra lo que esta cerca del mejor resultado (semantico o exacto)
        top_dense = max([c["dense"] for c in candidatos.values() if c["dense"] is not None] or [0])
        top_lex = max([c["lex"] for c in candidatos.values()] or [0])
        corte_dense = max(min_score, top_dense - 0.08)
        mejores = {}
        for pid, c in candidatos.items():
            ok_dense = c["dense"] is not None and c["dense"] >= corte_dense
            ok_lex = top_lex > 0 and c["lex"] >= 0.5 * top_lex
            aceptado = ok_dense or ok_lex
            if not aceptado:
                continue
            ruta = c["p"].get("rel_path", str(pid))
            puntuacion = rrf.get(pid, 0.0)
            if ruta not in mejores or puntuacion > mejores[ruta][0]:
                mejores[ruta] = (puntuacion, c)
        ordenados = sorted(mejores.values(), key=lambda x: x[0], reverse=True)[:top_k]

        filtros = (f" | tag={tag_f}" if tag_f else "") + (f" | carpeta={folder_f}" if folder_f else "")
        if not ordenados:
            return (f"No se encontraron notas relevantes para '{query}'{filtros} "
                    f"(umbral semantico {min_score}). Prueba con otras palabras o baja min_score.")

        modo = "hibrida" if vec else "solo lexica (Ollama no disponible)"
        out = [f"Resultados de Memoria Obsidian ({len(ordenados)} notas para '{query}'{filtros}, busqueda {modo}):\n"]
        for idx, (_, c) in enumerate(ordenados, 1):
            p = c["p"]
            detalle = []
            if c["dense"] is not None:
                detalle.append(f"semantica {c['dense']}")
            if c["lex"]:
                detalle.append(f"coincidencia exacta {c['lex']}")
            out.append(f"### [{idx}] {p.get('title', 'Sin titulo')} ({', '.join(detalle)})")
            out.append(f"- **Ruta:** `{p.get('rel_path', '')}`")
            if p.get("tags"):
                out.append(f"- **Etiquetas:** {', '.join(map(str, p['tags']))}")
            if p.get("wikilinks"):
                out.append(f"- **Enlaces:** {', '.join(map(str, p['wikilinks']))}")
            out.append(f"\n```markdown\n{str(p.get('text', ''))[:1200]}\n```\n")
        return "\n".join(out)
    finally:
        try:
            client.close()
        except Exception:
            pass


@mcp.tool()
def get_note_content(rel_path: str) -> str:
    """
    Obtiene el contenido completo de una nota específica por su ruta relativa o título (ej: '01-Vulnerabilidades/Active-Directory/AS-REP Roasting.md').
    Lee primero del sistema de archivos de Obsidian (G:/Mi unidad/Cyber-Vault), luego del espejo local y finalmente reconstruye los chunks desde Qdrant.
    """
    clean_path = rel_path.strip().replace("\\", "/")
    stem_target = Path(clean_path).stem.lower().replace("-", " ")

    # 1. Intentar archivo físico en Obsidian (G:)
    file_path = DEFAULT_VAULT / clean_path
    try:
        if file_path.exists():
            return file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        pass

    # 2. Intentar espejo local de respaldo (rag/vault_mirror)
    local_mirror = WORKSPACE_ROOT / "rag" / "vault_mirror" / clean_path
    try:
        if local_mirror.exists():
            return local_mirror.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        pass

    # 3. Fallback a reconstrucción desde Qdrant (búsqueda flexible por rel_path o stem)
    client = get_client()
    try:
        points, _ = client.scroll(
            collection_name=COLLECTION_NAME,
            limit=300,
            with_payload=True
        )
        matched_chunks = []
        for p in points:
            pay = p.payload or {}
            rp = pay.get("rel_path", "").replace("\\", "/")
            stem = pay.get("stem", "").lower().replace("-", " ")
            title = pay.get("title", "").lower()
            if (rp == clean_path or 
                stem == stem_target or 
                title == stem_target or 
                rp.replace("-", " ") == clean_path.replace("-", " ")):
                matched_chunks.append(pay)

        if not matched_chunks:
            return f"Nota no encontrada en Obsidian ni en Qdrant para la ruta: '{clean_path}'."

        matched_chunks.sort(key=lambda x: x.get("chunk_idx", 0))
        full_text = "\n\n".join([c.get("text", "") for c in matched_chunks])
        first = matched_chunks[0]
        meta = f"# {first.get('title', 'Nota')}\n**Ruta:** `{first.get('rel_path', clean_path)}`\n"
        if first.get("tags"):
            meta += f"**Etiquetas:** {', '.join(first['tags'])}\n"
        meta += "\n---\n\n"
        return meta + full_text
    finally:
        try:
            client.close()
        except Exception:
            pass


@mcp.tool()
def list_vault_topics() -> str:
    """
    Lista todos los temas, títulos de notas y rutas indexadas actualmente en la memoria de Qdrant.
    """
    client = get_client()
    try:
        if not client.collection_exists(COLLECTION_NAME):
            return "No existe la colección de memoria en Qdrant."

        points, _ = client.scroll(
            collection_name=COLLECTION_NAME,
            limit=500,
            with_payload=True,
            with_vectors=False
        )

        seen_notes = {}
        for p in points:
            pay = p.payload or {}
            rp = pay.get("rel_path", "")
            if rp and rp not in seen_notes:
                seen_notes[rp] = {
                    "title": pay.get("title", "Sin título"),
                    "tags": pay.get("tags", []),
                    "rel_path": rp
                }

        out = [f"Resumen de Memoria Obsidian / Qdrant ({len(seen_notes)} notas indexadas):\n"]
        for rp, data in sorted(seen_notes.items()):
            tags_str = f" [tags: {', '.join(data['tags'])}]" if data['tags'] else ""
            out.append(f"- **{data['title']}** -> `{rp}`{tags_str}")

        return "\n".join(out)
    finally:
        try:
            client.close()
        except Exception:
            pass


@mcp.tool()
def save_note_to_vault(
    title: str,
    content: str,
    category: str = "00-Inbox",
    tags: str = "",
    wikilinks: str = ""
) -> str:
    """
    Guarda y memoriza una nueva nota técnica en Obsidian (Cyber-Vault) y en la base vectorial Qdrant.
    La información queda inmediatamente disponible para todas las IAs (Claude, Cursor, OpenCode).
    
    Parámetros:
    - title: Título descriptivo (ej: 'Bypass WAF via HTTP2 Header Framing')
    - content: Contenido detallado en formato Markdown
    - category: Carpeta destino (ej: '00-Inbox', '01-Vulnerabilidades/Web', '03-Herramientas', '05-Cyber-Intel')
    - tags: Etiquetas separadas por comas (ej: 'waf, bypass, http2')
    - wikilinks: Enlaces a otras notas separadas por comas (ej: 'HTTP Request Smuggling, Burp Suite')
    """
    import datetime
    import hashlib

    # 1. Normalizar etiquetas y enlaces
    tag_list = [t.strip().lstrip("#") for t in tags.split(",") if t.strip()]
    link_list = [l.strip().lstrip("[").rstrip("]") for l in wikilinks.split(",") if l.strip()]

    # Sanitizar nombre de archivo
    safe_name = re.sub(r'[\\/*?:"<>|]', "-", title.strip())
    if not safe_name:
        safe_name = f"Nota-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"

    # Formatear contenido con frontmatter YAML
    now_iso = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    frontmatter_tags = "\n".join([f"  - {t}" for t in tag_list]) if tag_list else "  - nota"
    wikilinks_md = "\n".join([f"- [[{l}]]" for l in link_list]) if link_list else ""
    
    full_markdown = (
        f"---\n"
        f"title: \"{title}\"\n"
        f"date: {now_iso}\n"
        f"author: AI-Agent\n"
        f"tags:\n{frontmatter_tags}\n"
        f"---\n\n"
        f"# {title}\n\n"
        f"{content}\n"
    )
    if wikilinks_md:
        full_markdown += f"\n## 🔗 Notas Relacionadas\n{wikilinks_md}\n"

    rel_path = f"{category.strip('/')}/{safe_name}.md".replace("\\", "/")

    # 2. Guardar en el sistema de archivos (Obsidian Vault o Backup Local)
    saved_locations = []
    # Intento en G:/Mi unidad/Cyber-Vault
    vault_file = DEFAULT_VAULT / rel_path
    try:
        vault_file.parent.mkdir(parents=True, exist_ok=True)
        vault_file.write_text(full_markdown, encoding="utf-8")
        saved_locations.append(str(vault_file))
    except Exception as e:
        # Fallback a espejo local
        local_mirror = WORKSPACE_ROOT / "rag" / "vault_mirror" / rel_path
        local_mirror.parent.mkdir(parents=True, exist_ok=True)
        local_mirror.write_text(full_markdown, encoding="utf-8")
        saved_locations.append(f"Local Mirror ({local_mirror}) [G: no accesible: {e}]")

    # 3. Guardar directamente en la memoria vectorial de Qdrant
    client = get_client()
    try:
        if not client.collection_exists(COLLECTION_NAME):
            client.create_collection(
                COLLECTION_NAME,
                vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE)
            )

        content_hash = hashlib.sha256(full_markdown.encode("utf-8")).hexdigest()
        vec = get_embedding_safe(f"{title}\n{content}")
        vector_emergencia = not vec or len(vec) != 1024
        if vector_emergencia:
            # Vector fallback determinista de 1024 dims basado en hash para garantizar indexación
            h_int = int(content_hash[:8], 16)
            vec = [(float((h_int >> (i % 32)) & 1) * 0.05) for i in range(1024)]

        point_id = hashlib.md5(f"{rel_path}_0".encode("utf-8")).hexdigest()
        payload = {
            "title": title,
            "stem": safe_name,
            "rel_path": rel_path,
            "chunk_idx": 0,
            "text": content,
            "tags": tag_list,
            "wikilinks": link_list,
            "hash": content_hash,
            "timestamp": now_iso
        }
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=[models.PointStruct(id=point_id, vector=vec, payload=payload)],
            wait=True
        )

        # Actualizar estado de indexación
        state_file = DB_PATH / "vault_index_state.json"
        state = {}
        if state_file.exists():
            try:
                state = json.loads(state_file.read_text(encoding="utf-8"))
            except Exception:
                pass
        if vector_emergencia:
            state.pop(rel_path, None)  # sync_vault_now la reindexara con bge-m3
        else:
            state[rel_path] = content_hash
        state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")

        total_points = client.get_collection(COLLECTION_NAME).points_count
    finally:
        try:
            client.close()
        except Exception:
            pass

    return (
        f"✅ Nota '{title}' memorizada e indexada con éxito:\n"
        f"- Ruta en bóveda: `{rel_path}`\n"
        f"- Archivo guardado en: {', '.join(saved_locations)}\n"
        f"- Etiquetas: {', '.join(tag_list) if tag_list else 'ninguna'}\n"
        f"- Puntos en Qdrant: {total_points}\n"
        f"- Estado: Inmediatamente consultable por todas las IAs vía `search_vault`."
    )


@mcp.tool()
def sync_vault_now(force: bool = False) -> str:
    """
    Sincroniza y actualiza la base de datos vectorial Qdrant con las notas más recientes de Obsidian (G:/Mi unidad/Cyber-Vault).
    """
    try:
        from vault_qdrant import sync_vault
        res = sync_vault(force=force)
        return (
            f"✅ Sincronización exitosa:\n"
            f"- Total notas en bóveda: {res['total_notes']}\n"
            f"- Notas nuevas/actualizadas: {res['indexed_notes']}\n"
            f"- Notas omitidas (sin cambios): {res['skipped_notes']}\n"
            f"- Total puntos vectoriales: {res['total_points_in_qdrant']}\n"
            f"- Modelo: {res['embed_model']} ({res['dimension']} dimensiones)"
        )
    except Exception as e:
        return f"❌ Error durante la sincronización: {e}"


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("--test", "-t", "test", "--status", "-s"):
        print("=" * 60)
        print("🧠 TEST DE MEMORIA OBSIDIAN + QDRANT (Servidor MCP)")
        print("=" * 60)
        print("\n[1] Listado de temas y notas:")
        print(list_vault_topics())
        print("\n[2] Prueba de búsqueda semántica ('kerberos'):")
        print(search_vault("kerberos", top_k=2))
        print("=" * 60)
        print("✅ Servidor MCP operativo y listo para Claude, Cursor y OpenCode.")
    elif len(sys.argv) > 1 and sys.argv[1] in ("--query", "-q"):
        q = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "ciberseguridad"
        print(search_vault(q))
    elif len(sys.argv) > 1 and sys.argv[1] in ("--help", "-h"):
        print("Uso:")
        print("  Sin argumentos: Inicia el servidor MCP en modo stdio (para Claude/Cursor/OpenCode)")
        print("  --test        : Realiza un autotest de la memoria y la búsqueda")
        print("  --query <txt> : Busca notas semánticamente")
    else:
        mcp.run(show_banner=False)

