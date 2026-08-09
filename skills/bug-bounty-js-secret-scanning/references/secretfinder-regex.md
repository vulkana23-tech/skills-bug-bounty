# SecretFinder Regex Reference Patterns

## 1. Comando de Análisis con SecretFinder

```bash
python3 SecretFinder.py -i https://target.com/app.js -o cli
```

## 2. Remediación Segura

- No almacene nunca claves secretas de API en código JavaScript que se descargue y ejecute en el navegador del usuario final.
- Utilice proxies backend para intermediar las peticiones a servicios de terceros.
