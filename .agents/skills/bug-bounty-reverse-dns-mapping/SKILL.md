---
name: bug-bounty-reverse-dns-mapping
description: Mapeo de registros Reverse DNS (PTR) y rangos CIDR organizacionales. Descubrimiento de nombres de host mediante resolución inversa de bloques IP.
---

# Skill: Reverse DNS Mapping & Range Discovery

Esta habilidad capacita al agente para descubrir subdominios adicionales realizando consultas DNS inversas (registros PTR) sobre rangos de direcciones IP (bloques CIDR y ASN) pertenecientes a la organización objetivo.

## 📌 Metodología de Mapeo PTR

### 1. Identificación de Rangos de Red (ASN/CIDR)
- Obtener el ASN de la empresa a partir de sus nombres de dominio raíz.

### 2. Consultas PTR Masivas
- Consultar la dirección IP dentro del bloque para resolver el nombre de host canónico asociado (ej. `192.0.2.45` -> `internal-api.target.com`).

---

## 📚 Referencias Técnicas

Consulta la guía en:
[ptr-mapping-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-reverse-dns-mapping/references/ptr-mapping-guide.md)
