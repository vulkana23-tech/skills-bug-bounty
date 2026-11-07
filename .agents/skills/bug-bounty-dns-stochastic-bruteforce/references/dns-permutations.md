# DNS Bruteforcing & Permutations Reference

## 1. Cadena de Comandos para Fuerza Bruta DNS

```bash
# Permutaciones DNS con puredns
puredns bruteforce /path/to/wordlist.txt target.com -r /path/to/resolvers.txt -o found_subdomains.txt
```

## 2. Remediación Segura

- Utilice configuraciones DNS de tipo Wildcard (`*.target.com` apuntando a una página neutra) únicamente si desea disuadir la enumeración por fuerza bruta.
- Restrinja la visibilidad de registros DNS internos utilizando zonas DNS divididas (Split-Horizon DNS).
