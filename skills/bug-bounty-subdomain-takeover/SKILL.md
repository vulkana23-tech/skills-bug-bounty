---
name: bug-bounty-subdomain-takeover
description: Identificación y reclamación de subdominios huérfanos con CNAMEs apuntando a servicios desconfigurados de terceros (AWS S3, GitHub Pages, Heroku, Azure, Shopify, Tumblr, Engine Yard).
---

# Skill: Subdomain Takeover Analysis & Exploitation

Esta habilidad permite al agente realizar auditorías de trazado DNS para descubrir subdominios que apuntan (vía CNAME) a servicios de terceros que han sido desmantelados o eliminados sin actualizar las entradas DNS del dominio principal.

## 📌 Principales Proveedores Vulnerables y Huellas (Fingerprints)

| Servicio | CNAME típico | Error/Fingerprint |
| :--- | :--- | :--- |
| **AWS S3** | `s3.amazonaws.com` | `NoSuchBucket` |
| **GitHub Pages** | `github.io` | `There isn't a GitHub Pages site here.` |
| **Heroku** | `herokuapp.com` | `No such app` |
| **Shopify** | `myshopify.com` | `Sorry, this shop is currently unavailable.` |
| **Azure** | `azurewebsites.net` | `404 Web Site not found.` |
| **Surge.sh** | `surge.sh` | `project not found` |

---

## 🛠️ Metodología de Auditoría

1. Extraer todas las entradas CNAME de la lista de subdominios recolectados.
2. Hacer solicitudes HTTP/HTTPS a cada subdominio y comprobar si la respuesta coincide con las huellas digitales de servicios no reclamados.
3. Verificar si el registro DNS es vulnerable antes de generar el reporte de bug bounty.

---

## 📚 Matriz de Huellas y Casos Reales

Lee la documentación de fingerprinting y reportes destacados en:
[takeover-fingerprints.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-subdomain-takeover/references/takeover-fingerprints.md)
