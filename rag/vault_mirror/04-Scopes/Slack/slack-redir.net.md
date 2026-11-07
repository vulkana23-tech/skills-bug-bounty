---
title: "slack-redir.net"
tags:
  - scope
  - target
  - bug-bounty
  - recon
program: "Slack"
tier: "Tier 1"
status: "In-Scope"
bounty_eligible: true
date: "2026-11-08"
---

# 🎯 slack-redir.net

> [!TARGET] **Dominio In-Scope**: `slack-redir.net`
> Programa: **Slack** | Nivel: **Tier 1** | Estado: **Autorizado**

---

## 🔎 Google Dorks Pre-armados (Ignite Mindmap)
- 📄 **Archivos Expuestos**: [Buscar en Google](https://www.google.com/search?q=site:slack-redir.net+filetype:env+OR+filetype:log+OR+filetype:json+OR+filetype:yml+OR+filetype:sql)
- 🔑 **Tokens & Claves**: [Buscar en Google](https://www.google.com/search?q=site:slack-redir.net+inurl:token+OR+inurl:key+OR+inurl:auth+OR+inurl:secret)
- 🚪 **Endpoints Sensibles**: [Buscar en Google](https://www.google.com/search?q=site:slack-redir.net+inurl:api+OR+inurl:v1+OR+inurl:v2+OR+inurl:graphql+OR+inurl:swagger)
- ⚙️ **Paneles & Login**: [Buscar en Google](https://www.google.com/search?q=site:slack-redir.net+inurl:admin+OR+inurl:login+OR+inurl:signin+OR+inurl:dashboard)

---

## 🐙 GitHub Dorks de Código Filtrado
- 🔍 [Buscar Secretos en GitHub](https://github.com/search?q=%22slack-redir.net%22+password+OR+token+OR+secret+OR+apikey&type=code)

---

## 🧪 Checklist de Auditoría Benigna
- [ ] **Validación XSS (XSSRush)**: `xssrush.cmd -u "https://slack-redir.net/" --scan get`
- [ ] **Bypass 403 / 401**: Headers `X-Forwarded-For`, `X-Original-URL`, `X-Rewrite-URL`.
- [ ] **Control de Acceso / BOLA**: Probar endpoints API con tokens de diferentes privilegios.
- [ ] **Configuración CORS**: Reflejo de `Origin` arbitrario y `Access-Control-Allow-Credentials: true`.
