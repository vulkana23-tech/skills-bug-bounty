# Certificate Transparency Queries Reference

## 1. Comando Curl para Extracción de crt.sh

```bash
curl -s "https://crt.sh/?q=%.target.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u
```

## 2. Remediación Segura

- Tenga en cuenta que cualquier certificado emitido por una CA pública quedará registrado públicamente en los logs CT de forma inmutable. Evite usar nombres de subdominios confidenciales en los Common Names (CN) de certificados públicos.
