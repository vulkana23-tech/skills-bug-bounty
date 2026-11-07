#!/usr/bin/env python3
"""
launch_dashboard.py - Lanzador del Dashboard Visual 3D de Understand-Anything
Conecta la base de conocimiento de Obsidian (Cyber-Vault) o el proyecto con el visor interactivo.
"""
from __future__ import annotations

import os
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DASHBOARD_DIR = ROOT / "integrations" / "Understand-Anything" / "understand-anything-plugin" / "packages" / "dashboard"
DEFAULT_VAULT = "G:/Mi unidad/Cyber-Vault"
TOKEN = "cybervault2026"
PORT = 5173


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_VAULT
    print("=" * 60)
    print("🌐 Iniciando Dashboard Visual 3D (Understand-Anything)")
    print(f"📁 Bóveda / Proyecto: {target}")
    print("=" * 60)

    # 1. Verificar o generar knowledge-graph.json
    target_path = Path(target)
    ua_dir = target_path / ".ua"
    graph_file = ua_dir / "knowledge-graph.json"

    if not graph_file.exists():
        print(f"[+] Generando grafo de conocimiento inicial para: {target}...")
        parser_script = ROOT / "integrations" / "Understand-Anything" / "understand-anything-plugin" / "skills" / "understand-knowledge" / "parse-knowledge-base.py"
        merge_script = ROOT / "integrations" / "Understand-Anything" / "understand-anything-plugin" / "skills" / "understand-knowledge" / "merge-knowledge-graph.py"
        
        py_exe = ROOT / "rag" / "pentesting-everything" / ".venv" / "Scripts" / "python.exe"
        if not py_exe.exists():
            py_exe = sys.executable

        subprocess.run([str(py_exe), str(parser_script), str(target)], check=False)
        subprocess.run([str(py_exe), str(merge_script), str(target)], check=False)
        
        assembled = ua_dir / "intermediate" / "assembled-graph.json"
        if assembled.exists():
            import shutil
            shutil.copy(assembled, graph_file)
            print(f"✅ Grafo compilado en {graph_file}")

    # 2. Configurar entorno y arrancar Vite
    env = os.environ.copy()
    env["GRAPH_DIR"] = str(target)
    env["UNDERSTAND_ACCESS_TOKEN"] = TOKEN

    dashboard_url = f"http://127.0.0.1:{PORT}/?token={TOKEN}"
    print(f"\n🔑 Dashboard URL: {dashboard_url}")
    print("🚀 Abriendo navegador...")

    # Abrir navegador tras 2 segundos
    import threading
    threading.Thread(target=lambda: (time.sleep(2), webbrowser.open(dashboard_url)), daemon=True).start()

    # Ejecutar vite en DASHBOARD_DIR
    cmd = ["npx.cmd" if sys.platform == "win32" else "npx", "vite", "--port", str(PORT), "--host", "127.0.0.1"]
    try:
        subprocess.run(cmd, cwd=str(DASHBOARD_DIR), env=env)
    except KeyboardInterrupt:
        print("\n[+] Dashboard detenido.")


if __name__ == "__main__":
    main()

