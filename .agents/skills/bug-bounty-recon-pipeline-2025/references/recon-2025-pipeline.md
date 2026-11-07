# Modern Reconnaissance Pipeline Reference (2025)

## 1. Cadena de Comandos Integrada (Bash Pipeline)

```bash
# Discovery pasivo + verificación de hosts HTTP activos
subfinder -d target.com -silent | httpx -silent -mc 200,301,302,403 -title -o live_hosts.txt
```

## 2. Recomendaciones de Eficiencia

- Almacene los resultados intermedios en archivos de texto estructurados para permitir filtrados secundarios con `grep` y `awk`.
- Respete las tasas de peticiones (`rate-limit`) de APIs públicas para evitar bloqueos por parte de los proveedores DNS/CT.
