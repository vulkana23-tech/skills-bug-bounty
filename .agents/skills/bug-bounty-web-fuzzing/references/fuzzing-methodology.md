# Structured Web Fuzzing Reference

## 1. Cadena de Comandos FFUF

```bash
ffuf -u https://target.com/FUZZ -w /path/to/SecLists/Discovery/Web-Content/raft-medium-directories.txt -mc 200,301,302,403
```

## 2. Recomendaciones de Seguridad

- Adapte el número de hilos (`-t`) para no causar denegaciones de servicio no intencionadas en la infraestructura auditada.
- Configure agentes de usuario válidos para evitar bloqueos automatizados por WAF.
