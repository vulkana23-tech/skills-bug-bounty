---
name: bug-bounty-active-dns-alterations
description: Alteraciones activas de nombres de dominio y sondeo dinámico con Amass Enum. Generación de permutaciones en tiempo de ejecución y comprobación de nombres de host candidatos.
---

# Skill: Active DNS Alterations & Dynamic Probing

Esta habilidad capacita al agente para activar las reglas de alteración de nombres de Amass (añadir/quitar números, combinar palabras claves, sustitución de guiones) para descubrir subdominios adicionales mediante consultas DNS activas.

## 📌 Configuración de Alteraciones Activas

### 1. Activar Reglas de Alteración en Amass
```bash
amass enum -d target.com -active -alts -aw /path/to/alterations_wordlist.txt
```

---

## 📚 Referencias Técnicas

Consulta el playbook en:
[dns-alterations-playbook.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-active-dns-alterations/references/dns-alterations-playbook.md)
