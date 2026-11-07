---
{{ title | yaml_property:"title" }}
{{ tags | yaml_property:"tags" }}
{{ url | yaml_property:"source_url" }}
{{ date | yaml_property:"date" }}
author: {{ author | default:"Defuddle Harvester" }}
status: Ingested
---

# 🎯 {{ title | trim }}

> [!INTEL] **Fuente Original**: {{ url }}
> **Capturado**: {{ date }} | **Motor**: Defuddle + Knap

## 📝 Resumen Táctico
{{ summary | default:"Resumen pendiente de análisis" }}

## 🔍 Contenido Limpio
{{ content | trim }}

---
*Ingestado automáticamente por el pipeline de Cyber-Vault.*
