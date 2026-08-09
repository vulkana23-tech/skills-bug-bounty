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
