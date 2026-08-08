---
name: bug-bounty-dns-stochastic-bruteforce
description: Fuerza bruta estocástica y permutación de nombres DNS. Uso de subbrute, massthresh y diccionarios de resolución masiva para descubrir subdominios no indexados.
---

# Skill: Stochastic DNS Bruteforcing & Permutations

Esta habilidad capacita al agente para realizar pruebas de fuerza bruta DNS activas y permutaciones de palabras clave (`dev`, `staging`, `test`, `api`, `v1`, `v2`, `admin`) para descubrir subdominios válidos que no figuran en ninguna fuente pasiva u OSINT.

## 📌 Permutación y Alteración de Nombres

### 1. Inserción de Prefijos y Sufijos
- `target-dev.com`, `dev.target.com`, `target-staging.com`, `api-target.com`.

### 2. Fuerza Bruta Masiva con Resolutores DNS
- Utilizar resolutores DNS públicos validados con herramientas de alta velocidad (`puredns`, `massdns`, `dnsx`) para resolver millones de nombres por minuto.

---

## 📚 Referencias Técnicas

Consulta las permutaciones en:
[dns-permutations.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-dns-stochastic-bruteforce/references/dns-permutations.md)
