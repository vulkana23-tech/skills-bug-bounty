# Módulo de Conocimiento Persistente & RAG Integration (`rag/`)

Esta sección está diseñada para usuarios que **no desean cargar habilidades dinámicamente** mediante manifiestos `skills.json` o llamadas a herramientas en cada ejecución, sino que prefieren **inyectar la base de conocimiento completa** directamente en sus **System Prompts**, **Bases Vectoriales** o **Entornos RAG**.

---

## 🛠️ Opciones de Integración

### 1. Inyección Directa en System Prompts (`system-prompt-master.md`)
Si utilizas **Custom GPTs**, **Claude Projects**, **Cursor (.cursorrules)**, **OpenCode (AGENTS.md)** o **Ollama/LM Studio**:
- Abre [`rag/system-prompt-master.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/rag/system-prompt-master.md).
- Copia y pega el bloque de código completo en las instrucciones de sistema de tu asistente.

### 2. Carga de Documento Único RAG (`full-bug-bounty-knowledge-base.md`)
Si utilizas **AnythingLLM**, **NotebookLM**, **Open WebUI** o **LangChain Document Loaders**:
- Importa directamente el archivo [`rag/full-bug-bounty-knowledge-base.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/rag/full-bug-bounty-knowledge-base.md).
- El documento contiene marcas H1/H2/H3 diseñadas para ser procesadas eficientemente por algoritmos de *RecursiveCharacterTextSplitter* o *MarkdownTextSplitter*.

### 3. Importación Vectorial Estructurada (`rag/chunks/*.json`)
Si estás construyendo un pipeline RAG en **Python (LangChain / LlamaIndex / ChromaDB / Qdrant / Pinecone)**:
- Utiliza los datasets JSON en `rag/chunks/` que incluyen metadatos estructurados (`domain`, `skills`, `remediation`, `tags`).

### 4. Dataset externo: PentestingEverything (`rag/pentesting-everything/`)
Más de 5.000 chunks del repositorio [m14r41/PentestingEverything](https://github.com/m14r41/PentestingEverything) (24 dominios, Markdown + PDFs) en el mismo esquema, con metadatos de origen y licencia. Consulta [`rag/pentesting-everything/README.md`](pentesting-everything/README.md).

### 5. Dataset automotriz: Awesome Vehicle Security (`rag/awesome-vehicle-security/`)
Dataset estructurado del repositorio [jaredthecoder/awesome-vehicle-security](https://github.com/jaredthecoder/awesome-vehicle-security) (CAN bus, hardware, SDR, ECU, UDS, OBD-II, telemetría y explotación vehicular). Consulta [`rag/awesome-vehicle-security/README.md`](awesome-vehicle-security/README.md).

### 6. Dataset técnico profundo: Vulnerability Notes (`rag/vulnerability-notes/`)
Más de 7.000 chunks con 190 guías exhaustivas y notas de investigación del repositorio [parsamajidipour/vulnerability-notes](https://github.com/parsamajidipour/vulnerability-notes) sobre 10 vulnerabilidades web críticas (HTTP Request Smuggling, IDOR/BOLA, Web Cache Poisoning, OAuth/OIDC, SQLi, SSRF, SSTI, CSRF, Race Conditions, XXE). Consulta [`rag/vulnerability-notes/README.md`](vulnerability-notes/README.md).

### 7. Dataset de entrenamiento ofensivo: OffsecCyber (`rag/offseccyber/`)
Más de 12.400 pares instructivos y casos del dataset [PentesterFlow/OffsecCyber](https://huggingface.co/datasets/PentesterFlow/OffsecCyber) (PortSwigger Labs con soluciones paso a paso, reportes reales de HackerOne con root cause y severidad, tradecraft ofensivo de WAHH 2e, workarounds y CVE/NVD intelligence). Consulta [`rag/offseccyber/README.md`](offseccyber/README.md).

---

## 🐍 Ejemplo de Integración en Python (LangChain + ChromaDB)

```python
import json
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

# Cargar dataset de chunks RAG
with open('rag/chunks/02-web-api-vulnerabilities.json', 'r', encoding='utf-8') as f:
    chunks_data = json.load(f)

documents = [
    Document(
        page_content=item['content'],
        metadata={
            "domain": item['domain'],
            "skills": item['skills'],
            "tags": item['tags']
        }
    )
    for item in chunks_data
]

# Inicializar Base Vectorial
vectorstore = Chroma.from_documents(documents, OpenAIEmbeddings())
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

print("✅ Base Vectorial RAG cargada con éxito.")
```
