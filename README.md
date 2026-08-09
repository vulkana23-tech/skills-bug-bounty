# Bug Bounty & Security Skills Collection for OpenCode & Claude Code

Colección completa y estructurada de **100 Agent Skills (Hito Cien)** diseñadas para **OpenCode**, **Claude Code** y asistentes basados en agentes de IA (como Antigravity, Cursor, LangChain y AnythingLLM).

---

## ⚡ Dos Modos de Uso Disponibles

### Option A: Carga Dinámica Ligera (Dynamic Profiles)
Para quienes usan agentes que importan skills en caliente (`.agents/skills.json`):
- Usa perfiles especializados en [`profiles/`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles) (15–30 skills por fase) para no saturar el prompt.

| Perfil | Manifiesto | Nº Skills | Ideal Para |
| :--- | :--- | :---: | :--- |
| **🔍 Recon & OSINT** | [`profiles/profile-recon-osint.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-recon-osint.json) | 25 | Subdominios, ASNs, Certificados, Dorks, SpiderFoot, Amass |
| **🌐 Web & API Audit** | [`profiles/profile-web-api-audit.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-web-api-audit.json) | 30 | XSS, SQLi, IDOR, GraphQL, JWT, JS Recon, SSRF, CORS |
| **☁️ Cloud & DevOps** | [`profiles/profile-cloud-devops.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-cloud-devops.json) | 15 | AWS S3, Docker, Kubernetes RBAC, IAM, Nuclei Fast Scans |
| **🔥 Explotación Avanzada** | [`profiles/profile-advanced-exploitation.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-advanced-exploitation.json) | 19 | Request Smuggling, Turbo Intruder, BChecks, Race Conditions |
| **📱 Mobile, IoT & Binary** | [`profiles/profile-mobile-iot-binary.json`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/profiles/profile-mobile-iot-binary.json) | 11 | Android/iOS, Firmware IoT, Binarios ELF/PE, KYC Deepfakes |

---

### Option B: Conocimiento Persistente e Integración RAG (`rag/`) [NUEVO]
Para quienes no quieren cargar habilidades dinámicamente, sino inyectar el conocimiento directamente en su **System Prompt** o en su **Base de Datos Vectorial (RAG)**:

1. **🤖 System Prompt Maestro**: Copia y pega [`rag/system-prompt-master.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/rag/system-prompt-master.md) en las instrucciones de tu asistente (Custom GPTs, Claude Projects, Cursor `.cursorrules`, OpenCode `AGENTS.md`).
2. **📄 Compendio de Documento Único**: Importa [`rag/full-bug-bounty-knowledge-base.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/rag/full-bug-bounty-knowledge-base.md) en AnythingLLM, NotebookLM o Open WebUI.
3. **📊 Chunks para Vector DBs**: Carga los datasets JSON en [`rag/chunks/`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/rag/chunks) en ChromaDB, Qdrant, Pinecone o LangChain.

Consulta la guía técnica completa en [`rag/README.md`](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/rag/README.md).

---

## 📁 Estructura del Repositorio

```
bug-bounty-skills/
├── README.md                           # Guía principal de uso e integración
├── skills.json                         # Manifiesto Maestro (100 skills completas)
├── profiles/                           # 🚀 Option A: Perfiles de Carga Dinámica Ligera
├── rag/                                # 🧠 Option B: Conocimiento Persistente & RAG Integrado
│   ├── README.md                       # Guía de integración RAG y Vector DBs
│   ├── system-prompt-master.md         # System Prompt Maestro de Copiar y Pegar
│   ├── full-bug-bounty-knowledge-base.md# Compendio consolidado (100 skills)
│   └── chunks/                         # Datasets JSON divididos semánticamente
└── skills/                             # 100 Habilidades en formato SKILL.md + references/
```

---

## 📄 Licencia & Créditos
Repositorio mantenido bajo licencia de uso educativo y auditoría autorizada.
