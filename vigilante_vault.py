"""Vigilante de Cyber-Vault: indexa en Qdrant automaticamente las notas nuevas,
modificadas o borradas de Obsidian. Pensado para correr en segundo plano (pythonw).
Registro en rag/vigilante.log"""
import os, sys, time, socket, traceback
from pathlib import Path

os.environ.setdefault("QDRANT_URL", "http://127.0.0.1:6333")
BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
from vault_qdrant import sync_vault, DEFAULT_VAULT  # noqa: E402

LOG = BASE / "rag" / "vigilante.log"
EXCLUIR = {".obsidian", ".trash", "templates", "_archivo"}
INTERVALO = 20        # segundos entre comprobaciones
ESPERA_ESTABLE = 15   # segundos sin cambios antes de indexar (Obsidian guarda mientras escribes)


def log(msg):
    try:
        if LOG.exists() and LOG.stat().st_size > 1_000_000:
            LOG.replace(LOG.with_suffix(".log.1"))
        with open(LOG, "a", encoding="utf-8") as fh:
            fh.write(time.strftime("%Y-%m-%d %H:%M:%S  ") + msg + "\n")
    except Exception:
        pass


def firma(vault):
    items = []
    for f in vault.rglob("*.md"):
        try:
            if EXCLUIR & set(f.relative_to(vault).parts):
                continue
            st = f.stat()
            items.append((str(f), st.st_mtime_ns, st.st_size))
        except OSError:
            pass
    return hash(frozenset(items))


def main():
    # Una sola instancia: si el puerto ya esta ocupado, otro vigilante esta corriendo
    lock = socket.socket()
    try:
        lock.bind(("127.0.0.1", 47833))
    except OSError:
        return
    log("Vigilante iniciado. Bóveda: " + str(DEFAULT_VAULT))
    ultima = None
    while True:
        try:
            if DEFAULT_VAULT.exists():
                actual = firma(DEFAULT_VAULT)
                if actual != ultima:
                    # Esperar a que dejes de escribir
                    time.sleep(ESPERA_ESTABLE)
                    estable = firma(DEFAULT_VAULT)
                    if estable == actual:
                        res = sync_vault()
                        if ultima is None or res.get("indexed_notes") or res.get("purged_points"):
                            log(f"Sync: {res.get('indexed_notes')} indexadas, "
                                f"{res.get('purged_points')} fragmentos purgados, "
                                f"{res.get('total_points_in_qdrant')} en Qdrant")
                        ultima = estable
            else:
                log("Bóveda no accesible (¿Google Drive aún sin montar?)")
        except Exception as e:
            log("ERROR: " + str(e).splitlines()[0][:300])
            time.sleep(60)  # Ollama/Qdrant aun arrancando: reintentar mas tarde
        time.sleep(INTERVALO)


if __name__ == "__main__":
    main()
