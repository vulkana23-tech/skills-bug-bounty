"""Copia la memoria del Qdrant embebido (rag/qdrant_db) al Qdrant servidor (QDRANT_URL).
No borra ni modifica la base embebida. Se puede ejecutar varias veces (upsert)."""
import os, sys
from pathlib import Path
import qdrant_client
from qdrant_client import models

COL = "cyber_vault"
src_path = Path(__file__).resolve().parent / "rag" / "qdrant_db"
url = os.environ.get("QDRANT_URL", "http://127.0.0.1:6333")

src = qdrant_client.QdrantClient(path=str(src_path))
dst = qdrant_client.QdrantClient(url=url, api_key=os.environ.get("QDRANT_API_KEY") or None)

if not dst.collection_exists(COL):
    dst.create_collection(COL, vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE))

total, offset = 0, None
while True:
    pts, offset = src.scroll(COL, limit=256, offset=offset, with_vectors=True, with_payload=True)
    if pts:
        dst.upsert(COL, points=[models.PointStruct(id=p.id, vector=p.vector, payload=p.payload) for p in pts])
        total += len(pts)
    if offset is None:
        break
src.close()
print(f"Migrados {total} puntos -> {url} | En servidor: {dst.count(COL).count}")
