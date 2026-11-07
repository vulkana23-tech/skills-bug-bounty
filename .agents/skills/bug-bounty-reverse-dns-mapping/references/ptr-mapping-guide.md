# Reverse DNS Mapping Reference Guide

## 1. Comandos de Consulta PTR

```bash
# Resolución PTR pasiva mediante dnsx
dnsx -l ips.txt -ptr -resp-only -o ptr_results.txt
```

## 2. Remediación Segura

- Evite nombrar registros PTR de forma que revelen la función crítica del servidor (ej. usar `host-192-0-2-10.target.com` en lugar de `db-master-prod.target.com`).
