---
name: vigilantes-cti
description: Sincronización y consulta de boletines de Ciberinteligencia (CTI), actores de amenazas (APTs), campañas de Dark Web y avisos CISA/INCIBE desde el motor LOS VIGILANTES · v3 (Custodes Intellegentiae).
---

# Vigilantes CTI (Custodes Intellegentiae)

Permite sincronizar y consultar en tiempo real los boletines de Ciberinteligencia estratégica (`cyber-intelligence-digest`), Ciberseguridad defensiva (`cybersecurity-digest`) e Inteligencia de Modelos (`ai-builders-digest`) directamente en tu bóveda Obsidian (`05-Cyber-Intel/`) y en la memoria vectorial de Qdrant.

## Comandos

### Sincronización
```bash
rag/pentesting-everything/.venv/Scripts/python.exe sync_vigilantes_intel.py
```
O vía API HTTP:
```bash
curl -X POST http://127.0.0.1:7860/api/vigilantes/sync
```

### Consulta
```bash
rag/pentesting-everything/.venv/Scripts/python.exe vault_qdrant.py --query "campaña APT o exploit reciente"
```

