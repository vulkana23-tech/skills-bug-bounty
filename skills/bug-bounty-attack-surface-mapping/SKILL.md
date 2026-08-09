---
name: bug-bounty-attack-surface-mapping
description: Mapeo integral de superficie de ataque corporativa (Attack Surface Management - ASM) con OWASP Amass Intel y Enum. Consolidación de huellas digitales de grandes organizaciones.
---

# Skill: Attack Surface Mapping (ASM)

Esta habilidad capacita al agente para trazar la huella digital completa de una organización objetivo, combinando múltiples fuentes de inteligencia para identificar todos los nombres de dominio, subdominios, bloques IP e infraestructuras asociadas.

## 📌 Comandos de Mapeo con Amass

### 1. Descubrimiento de Inteligencia de Organización (`amass intel`)
- Buscar dominios raíz pertenecientes a una empresa por nombre de organización:
  `amass intel -org "Example Corp"`

### 2. Enumeración Activa y Pasiva (`amass enum`)
- Ejecutar enumeración completa integrando APIs configuradas y resolución activa:
  `amass enum -d target.com -active -cidr 192.0.2.0/24`

---

## 📚 Referencias Técnicas

Consulta la guía de mapeo en:
[surface-mapping-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-attack-surface-mapping/references/surface-mapping-guide.md)
