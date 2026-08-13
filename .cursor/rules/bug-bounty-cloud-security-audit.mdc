---
name: bug-bounty-cloud-security-audit
description: Auditoría de seguridad en entornos Cloud (AWS, Azure, GCP). Malas configuraciones de políticas IAM, almacenamiento de objetos S3/Blob públicamente accesible e inspección de Security Groups.
---

# Skill: Cloud Infrastructure Security Assessment

Esta habilidad capacita al agente para auditar la configuración de seguridad en servicios de infraestructura en la nube (AWS, Microsoft Azure, Google Cloud Platform), identificando sobre-permisos en políticas IAM y buckets de almacenamiento expuestos.

## 📌 Vectores de Auditoría Cloud

### 1. Misconfiguración de Almacenamiento (AWS S3 / Azure Blob)
- Buckets con lectura o escritura pública activa (`AllUsers` / `AuthenticatedUsers` con permisos `READ` o `WRITE`).
- Listado de contenido habilitado públicamente (`s3:ListBucket`).

### 2. Políticas IAM sobre-permisivas
- Roles con asignaciones `*:*` o permisos para elevar privilegios (ej. `iam:CreatePolicyVersion`, `iam:AttachUserPolicy`).

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[cloud-hardening.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-cloud-security-audit/references/cloud-hardening.md)
