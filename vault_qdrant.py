#!/usr/bin/env python3
"""
vault_qdrant.py - Motor de Vectorización e Indexación de Obsidian en Qdrant
Sincroniza todas las notas de G:\\Mi unidad\\Cyber-Vault hacia Qdrant.
Utiliza embeddings multilingües acelerados por GPU vía Ollama (bge-m3 / nomic-embed-text).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import qdrant_client
from qdrant_client import models

# Rutas estándar
ROOT = Path(__file__).resolve().parent
DEFAULT_VAULT = Path("G:/Mi unidad/Cyber-Vault")
DB_PATH = ROOT / "rag" / "qdrant_db"
COLLECTION_NAME = "cyber_vault"
OLLAMA_API_URL = os.environ.get("OLLAMA_API_URL", "http://127.0.0.1:11434")
EMBED_MODEL = "bge-m3"  # 1024 dims, multilingüe de alta precisión


def get_embedding(text: str, model: str = EMBED_MODEL) -> List[float]:
    """Genera vector denso usando Ollama GPU."""
    try:
        data = json.dumps({
            "model": model,
            "prompt": text[:4000],
            "keep_alive": -1  # mantener el modelo cargado en GPU
        }).encode("utf-8")
        req = urllib.request.Request(
            f"{OLLAMA_API_URL}/api/embeddings",
            data=data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            return res.get("embedding", [])
    except Exception as e:
        # Reintento con el MISMO modelo (nomic-embed-text daba 768 dims y la coleccion es de 1024)
        last = e
        for espera in (2, 5, 10):
            time.sleep(espera)
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    vec = json.loads(resp.read().decode("utf-8")).get("embedding", [])
                    if vec:
                        return vec
            except Exception as e2:
                last = e2
        raise RuntimeError(f"Error generando embeddings con Ollama ({model}): {last}")


def get_qdrant_client(storage_path: Optional[Path] = None) -> qdrant_client.QdrantClient:
    url = os.environ.get("QDRANT_URL")
    if url and storage_path is None:  # Modo servidor: varios agentes a la vez
        return qdrant_client.QdrantClient(url=url, api_key=os.environ.get("QDRANT_API_KEY") or None)
    p = storage_path or DB_PATH
    p.mkdir(parents=True, exist_ok=True)
    return qdrant_client.QdrantClient(path=str(p))


def ensure_collection(client: qdrant_client.QdrantClient, name: str = COLLECTION_NAME, dim: int = 1024):
    if not client.collection_exists(name):
        client.create_collection(
            name,
            vectors_config=models.VectorParams(size=dim, distance=models.Distance.COSINE)
        )
        for field in ("rel_path", "tags", "wikilinks", "title"):
            try:
                client.create_payload_index(name, field, models.PayloadSchemaType.KEYWORD)
            except Exception:
                pass


def parse_markdown_note(path: Path, vault_root: Path) -> Dict[str, Any]:
    """Extrae frontmatter, wikilinks, tags y texto de una nota."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    rel_path = str(path.relative_to(vault_root)).replace("\\", "/")
    
    # 1. Tags
    tags = set(re.findall(r"#([a-zA-Z0-9_-]+)", text))
    
    # 2. Frontmatter YAML básico
    frontmatter = {}
    content = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            raw_fm = parts[1]
            content = parts[2].strip()
            for line in raw_fm.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    k = k.strip()
                    v = v.strip().strip('"\'')
                    if k == "tags":
                        continue
                    frontmatter[k] = v
                elif line.strip().startswith("- "):
                    tags.add(line.strip()[2:])

    # 3. Wikilinks [[Nota]] o [[Nota|Alias]]
    raw_wikilinks = re.findall(r"\[\[([^\]]+)\]\]", text)
    wikilinks = []
    for wl in raw_wikilinks:
        target = wl.split("|")[0].strip()
        wikilinks.append(target)

    # 4. Hash para detectar cambios
    content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()

    title = frontmatter.get("title") or path.stem

    return {
        "title": title,
        "stem": path.stem,
        "rel_path": rel_path,
        "content": content,
        "full_text": text,
        "tags": sorted(list(tags)),
        "wikilinks": sorted(list(set(wikilinks))),
        "frontmatter": frontmatter,
        "hash": content_hash,
        "mtime": path.stat().st_mtime
    }


def chunk_note(note_data: Dict[str, Any], max_chunk_chars: int = 1500) -> List[Dict[str, Any]]:
    """Divide notas largas en secciones lógicas manteniendo contexto."""
    content = note_data["content"]
    if len(content) <= max_chunk_chars:
        return [{
            "chunk_idx": 0,
            "text": f"Nota: {note_data['title']} ({note_data['rel_path']})\nEtiquetas: {', '.join(note_data['tags'])}\nEnlaces: {', '.join(note_data['wikilinks'])}\n\n{content}",
            "raw_text": content,
            "parent_id": note_data["rel_path"]
        }]
    
    # Dividir por encabezados Markdown (# o ##)
    sections = re.split(r"(?m)^(?=#{1,3}\s)", content)
    chunks = []
    for idx, sec in enumerate(sections):
        sec = sec.strip()
        if not sec:
            continue
        chunks.append({
            "chunk_idx": idx,
            "text": f"Nota: {note_data['title']} (Sección {idx+1})\nEtiquetas: {', '.join(note_data['tags'])}\n\n{sec}",
            "raw_text": sec,
            "parent_id": note_data["rel_path"]
        })
    return chunks


def sync_vault(vault_path: Optional[Path] = None, force: bool = False) -> Dict[str, Any]:
    """Escanea la bóveda e indexa notas nuevas o modificadas en Qdrant."""
    vault = vault_path or DEFAULT_VAULT
    if not vault.exists():
        raise FileNotFoundError(f"La bóveda de Obsidian no existe en: {vault}")

    client = get_qdrant_client()
    # Detectar dimensión del modelo activo
    test_vec = get_embedding("test")
    dim = len(test_vec)
    ensure_collection(client, dim=dim)

    # Registro de estado indexado (cache de hashes)
    state_file = DB_PATH / "vault_index_state.json"
    state = {}
    if state_file.exists() and not force:
        try:
            state = json.loads(state_file.read_text(encoding="utf-8"))
        except Exception:
            state = {}

    EXCLUIR = {".obsidian", ".trash", "templates", "_archivo"}
    md_files = [f for f in vault.rglob("*.md")
                if not (EXCLUIR & set(f.relative_to(vault).parts))]
    rutas_actuales = {str(f.relative_to(vault)).replace("\\", "/") for f in md_files}
    notas_reindexadas = []
    total = len(md_files)
    indexed_count = 0
    skipped_count = 0
    points_to_upsert = []

    for f in md_files:
        try:
            note = parse_markdown_note(f, vault)
            rel_path = note["rel_path"]
            curr_hash = note["hash"]

            if not note["content"].strip():  # nota vacia: no se indexa (y se purga si estaba)
                state.pop(rel_path, None)
                skipped_count += 1
                continue

            if not force and state.get(rel_path) == curr_hash:
                skipped_count += 1
                continue
            puntos_nota = []
            chunks = chunk_note(note)
            for ch in chunks:
                vec = get_embedding(ch["text"])
                point_id = hashlib.md5(f"{rel_path}_{ch['chunk_idx']}".encode("utf-8")).hexdigest()
                payload = {
                    "title": note["title"],
                    "stem": note["stem"],
                    "rel_path": rel_path,
                    "chunk_idx": ch["chunk_idx"],
                    "text": ch["raw_text"],
                    "tags": note["tags"],
                    "wikilinks": note["wikilinks"],
                    "hash": curr_hash
                }
                puntos_nota.append(models.PointStruct(
                    id=point_id,
                    vector=vec,
                    payload=payload
                ))
            
            points_to_upsert.extend(puntos_nota)  # solo si todos los trozos se generaron bien
            notas_reindexadas.append(rel_path)
            state[rel_path] = curr_hash
            indexed_count += 1
        except Exception as err:
            print(f"[!] Error procesando nota {f}: {err}", file=sys.stderr)

    # Borrar fragmentos antiguos de las notas reindexadas (evita trozos huerfanos)
    if notas_reindexadas:
        client.delete(COLLECTION_NAME, points_selector=models.FilterSelector(filter=models.Filter(
            must=[models.FieldCondition(key="rel_path", match=models.MatchAny(any=notas_reindexadas))])), wait=True)

    if points_to_upsert:
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points_to_upsert,
            wait=True
        )

    # Purgar notas borradas, excluidas o vacias que sigan en Qdrant
    huerfanos, offset = [], None
    while True:
        pts, offset = client.scroll(COLLECTION_NAME, limit=512, offset=offset, with_payload=["rel_path"], with_vectors=False)
        huerfanos += [p.id for p in pts if p.payload.get("rel_path") not in rutas_actuales
                      or p.payload.get("rel_path") not in state]
        if offset is None:
            break
    if huerfanos:
        client.delete(COLLECTION_NAME, points_selector=models.PointIdsList(points=huerfanos), wait=True)
    state = {k: v for k, v in state.items() if k in rutas_actuales}

    # Guardar nuevo estado
    state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")

    info = client.get_collection(COLLECTION_NAME)
    total_points = info.points_count
    try:
        client.close()
    except Exception:
        pass

    return {
        "ok": True,
        "total_notes": total,
        "indexed_notes": indexed_count,
        "skipped_notes": skipped_count,
        "total_points_in_qdrant": total_points,
        "dimension": dim,
        "embed_model": EMBED_MODEL,
        "purged_points": len(huerfanos)
    }


def query_vault(query: str, top_k: int = 3, score_threshold: float = 0.35) -> List[Dict[str, Any]]:
    """Consulta semántica rápida sobre la base vectorial de Obsidian."""
    client = get_qdrant_client()
    try:
        if not client.collection_exists(COLLECTION_NAME):
            return []

        q_vec = get_embedding(query)
        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=q_vec,
            limit=top_k,
            score_threshold=score_threshold
        )

        matches = []
        for r in getattr(results, "points", []):
            p = r.payload or {}
            matches.append({
                "score": round(r.score, 4),
                "title": p.get("title", "Sin título"),
                "stem": p.get("stem", ""),
                "rel_path": p.get("rel_path", ""),
                "tags": p.get("tags", []),
                "wikilinks": p.get("wikilinks", []),
                "content": p.get("text", "")
            })
        return matches
    finally:
        try:
            client.close()
        except Exception:
            pass


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Gestor Qdrant para Obsidian Vault")
    parser.add_argument("--sync", action="store_true", help="Sincronizar notas con Qdrant")
    parser.add_argument("--force", action="store_true", help="Re-indexar todo forzosamente")
    parser.add_argument("--query", "-q", type=str, help="Hacer una consulta semántica")
    parser.add_argument("--top", type=int, default=3, help="Cantidad de resultados")
    args = parser.parse_args()

    if args.sync:
        print("[+] Iniciando sincronización de Obsidian Vault con Qdrant...")
        res = sync_vault(force=args.force)
        print(f"✅ Sincronización completa:")
        print(f"   - Notas totales: {res['total_notes']}")
        print(f"   - Notas indexadas: {res['indexed_notes']}")
        print(f"   - Notas omitidas (sin cambios): {res['skipped_notes']}")
        print(f"   - Puntos vectoriales en Qdrant: {res['total_points_in_qdrant']}")
        print(f"   - Modelo de embeddings: {res['embed_model']} ({res['dimension']} dimensiones)")
    elif args.query:
        print(f"[🔍] Buscando en Obsidian: '{args.query}'...\n")
        matches = query_vault(args.query, top_k=args.top)
        if not matches:
            print("No se encontraron notas con suficiente similitud.")
        for idx, m in enumerate(matches, 1):
            print(f"--- [{idx}] {m['title']} (Similitud: {m['score']}) ---")
            print(f"📁 Ruta: {m['rel_path']}")
            if m['tags']:
                print(f"🏷️  Etiquetas: {', '.join(m['tags'])}")
            if m['wikilinks']:
                print(f"🔗 Enlaces wiki: {', '.join(m['wikilinks'])}")
            print(f"\n{m['content'][:400]}...\n")
    else:
        parser.print_help()
