---
name: bug-bounty-osint-automation-framework
description: Marco de automatización OSINT multimodular basado en la arquitectura de SpiderFoot. Ejecución paralela de más de 200 módulos de recolección pasiva, modelo Publisher/Subscriber y automatización CLI.
---

# Skill: OSINT Automation Framework (SpiderFoot Architecture)

Esta habilidad capacita al agente para aplicar la metodología de automatización OSINT multimodular de SpiderFoot, orquestando la recolección paralela de datos pasivos sobre nombres de dominio, subdominios, direcciones IP y entidades corporativas.

## 📌 Principios de Automatización OSINT

### 1. Modelo Publisher / Subscriber
- Cada módulo emite eventos (ej. `DOMAIN_NAME`, `IP_ADDRESS`, `EMAIL_ADDRESS`) que activan de forma encadenada a otros módulos consumidores de inteligencia.

### 2. Ejecución CLI de SpiderFoot (`sf.py`)
```bash
# Escaneo pasivo completo de un dominio objetivo
python3 sf.py -s target.com -m sfp_dns,sfp_whois,sfp_shodan,sfp_spider -q
```

---

## 📚 Referencias Técnicas

Consulta la guía CLI en:
[spiderfoot-cli-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-osint-automation-framework/references/spiderfoot-cli-guide.md)
