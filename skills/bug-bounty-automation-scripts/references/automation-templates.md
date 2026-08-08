# Automation Templates & Scripting Reference

## 1. Ejemplos de Scripts Wrapper (Bash)

```bash
#!/bin/bash
# Wrapper sencillo de recon para subdominios
DOMAIN=$1
subfinder -d $DOMAIN -silent | httpx -silent -title -mc 200
```

## 2. Recomendaciones de Automatización

- Evite sobrecargar los servidores del objetivo ejecutando hilos excesivos (`threads`) en scripts automatizados.
- Incluya manejo de excepciones e interrupciones (`Ctrl+C`) en todos los scripts de prueba.
