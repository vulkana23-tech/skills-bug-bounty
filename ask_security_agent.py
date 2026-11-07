#!/usr/bin/env python3
"""
Interactive Cybersecurity Assistant powered by Local Ollama + RAG Knowledge Base.

Models supported:
  - qwen2.5-coder:7b     (Code review, web logic analysis, AST & vulnerabilities)
  - whiterabbitneo:latest (Offensive red teaming, PoCs, evasion & exploitation)

Knowledge bases included:
  - rag/offseccyber/chunks.jsonl (PortSwigger Labs, HackerOne reports, WAHH)
  - rag/vulnerability-notes/chunks.jsonl (Deep dive notes on 10 web vuln classes)
  - rag/pentesting-everything/chunks.jsonl (24 pentesting domains, active directory, cloud, etc.)
  - rag/awesome-vehicle-security/chunks.jsonl (CAN bus, ECU, hardware, SDR)

Usage:
  python ask_security_agent.py
  python ask_security_agent.py --model whiterabbitneo --query "¿Cómo resuelvo el lab de HTTP request smuggling TE.CL?"
  python ask_security_agent.py --model qwen2.5-coder:7b --query "Analiza este código PHP buscando IDOR"
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent

DEFAULT_MODEL = "qwen2.5-coder:7b"
OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"

DATASETS = [
    ROOT / "rag" / "offseccyber" / "chunks.jsonl",
    ROOT / "rag" / "vulnerability-notes" / "chunks.jsonl",
    ROOT / "rag" / "pentesting-everything" / "chunks.jsonl",
    ROOT / "rag" / "awesome-vehicle-security" / "chunks.jsonl",
]


def load_all_chunks(max_per_dataset=5000):
    chunks = []
    for path in DATASETS:
        if not path.exists():
            continue
        count = 0
        with path.open(encoding="utf-8") as f:
            for line in f:
                try:
                    c = json.loads(line)
                    chunks.append(c)
                    count += 1
                    if count >= max_per_dataset:
                        break
                except Exception:
                    continue
    return chunks


def keyword_search(chunks, query, top_k=3):
    """Fast lexical ranking using token matching, title weights, and tag overlap."""
    query_tokens = [w.lower() for w in re.findall(r"\w+", query) if len(w) > 2]
    if not query_tokens:
        return chunks[:top_k]

    scored = []
    for c in chunks:
        content_low = c["content"].lower()
        title_low = str(c.get("metadata", {}).get("document_title", "")).lower()
        tags = [t.lower() for t in c.get("tags", [])]

        score = 0
        for tok in query_tokens:
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


def call_ollama(model: str, prompt: str, stream: bool = True):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream,
        "options": {
            "temperature": 0.3,
            "num_predict": 1500,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(OLLAMA_API_URL, data=data, headers={"Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req) as resp:
            if stream:
                for line in resp:
                    if line:
                        chunk = json.loads(line.decode("utf-8"))
                        token = chunk.get("response", "")
                        print(token, end="", flush=True)
                        if chunk.get("done"):
                            print()
                            break
            else:
                body = json.loads(resp.read().decode("utf-8"))
                return body.get("response", "")
    except Exception as e:
        print(f"\n[!] Error conectando con Ollama: {e}", file=sys.stderr)
        print("Asegúrate de que Ollama esté abierto en segundo plano.", file=sys.stderr)


def answer_query(query: str, model: str, chunks):
    print(f"\n🔍 Buscando referencias técnicas relevantes...")
    top_chunks = keyword_search(chunks, query, top_k=3)

    context_blocks = []
    sources = []
    for i, c in enumerate(top_chunks, 1):
        m = c.get("metadata", {})
        title = m.get("document_title") or c.get("domain") or "Doc"
        src = m.get("source_path") or m.get("training_source") or "RAG"
        sources.append(f"{i}. [{c.get('domain')}] {title} ({src})")
        context_blocks.append(f"--- REFERENCIA {i}: {title} ---\n{c['content'][:1400]}")

    context_text = "\n\n".join(context_blocks)

    master_file = ROOT / "prompts" / "whiterabbitneo_master.txt"
    if master_file.exists():
        system_instruction = master_file.read_text(encoding="utf-8").strip()
    else:
        system_instruction = (
            "Eres WHITERABBITNEO, actuando como un instructor experto en ciberseguridad ofensiva ética.\n"
            "Responde siempre en ESPAÑOL fluido, con profundidad técnica, código completo y formato estándar.\n"
        )

    full_instruction = (
        f"{system_instruction}\n\n"
        f"### KNOWLEDGE BASE CONTEXT (RAG):\n{context_text}\n\n"
        f"### USER QUERY:\n{query}\n\n"
        "### RESPUESTA ESTÁNDAR (EN ESPAÑOL):"
    )

    print(f"🤖 Modelo activo: [{model}]")
    if sources:
        print("📚 Fuentes consultadas:")
        for s in sources:
            print(f"   {s}")
    print("\n" + "=" * 60)
    call_ollama(model, full_instruction, stream=True)
    print("=" * 60 + "\n")


def main():
    ap = argparse.ArgumentParser(description="Cybersecurity Assistant (Local LLM + RAG)")
    ap.add_argument("--model", "-m", default=DEFAULT_MODEL, choices=["qwen2.5-coder:7b", "whiterabbitneo:latest", "whiterabbitneo"],
                    help="Modelo local a utilizar")
    ap.add_argument("--query", "-q", help="Pregunta directa en lugar de modo interactivo")
    args = ap.parse_args()

    model_name = "whiterabbitneo:latest" if "whiterabbit" in args.model else args.model

    print(f"[+] Cargando índice RAG local...")
    chunks = load_all_chunks()
    print(f"[+] {len(chunks)} fragmentos de conocimiento cargados.")

    if args.query:
        answer_query(args.query, model_name, chunks)
        return

    print("\n" + "=" * 60)
    print("🛡️  ASISTENTE DE CIBERSEGURIDAD LOCAL (OLLAMA + RAG)")
    print(f"   Modelo actual: {model_name}")
    print("   Escribe tu pregunta o 'salir' para terminar.")
    print("   Para cambiar de modelo escribe: '/modelo qwen' o '/modelo rabbit'")
    print("=" * 60 + "\n")

    while True:
        try:
            prompt = input(f"[{model_name}] > ").strip()
            if not prompt:
                continue
            if prompt.lower() in ("salir", "exit", "quit"):
                break
            if prompt.startswith("/modelo"):
                parts = prompt.split()
                if len(parts) > 1 and "rabbit" in parts[1].lower():
                    model_name = "whiterabbitneo:latest"
                else:
                    model_name = "qwen2.5-coder:7b"
                print(f"[i] Modelo cambiado a: {model_name}\n")
                continue

            answer_query(prompt, model_name, chunks)
        except (KeyboardInterrupt, EOFError):
            print("\n¡Hasta pronto!")
            break


if __name__ == "__main__":
    main()

