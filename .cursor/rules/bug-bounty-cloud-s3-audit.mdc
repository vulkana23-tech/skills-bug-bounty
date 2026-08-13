---
name: bug-bounty-cloud-s3-audit
description: Auditoría y descubrimiento especializado de almacenamiento de objetos (AWS S3, Azure Blob, GCP Storage Bucket). Enumeración de buckets, permisos de lectura/escritura y misconfigurations.
---

# Skill: Cloud Object Storage Assessment (S3 Audit)

Esta habilidad capacita al agente para realizar descubrimiento y auditoría de buckets de almacenamiento en la nube asociadas a dominios de prueba, verificando permisos de acceso público de lectura o escritura desconfigurados.

## 📌 Metodología de Auditoría S3

### 1. Generación de Permutaciones de Nombre de Bucket
- Generar combinaciones de nombres basadas en la marca del objetivo (ej. `target-data`, `target-backup`, `target-assets`, `target-staging-s3`).

### 2. Verificación de Permisos
- Evaluar solicitudes HTTP directas a los buckets descubiertos para comprobar si devuelven `200 OK` con listado XML de archivos o `403 Forbidden`.

---

## 📚 Referencias Técnicas

Consulta la guía de enumeración en:
[s3-enumeration-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-cloud-s3-audit/references/s3-enumeration-guide.md)
