---
title: "HackNexus Toolkit"
tool_name: "hacknexus"
github_repo: "https://github.com/D1se0/hacknexus"
category: "Seguridad-Ofensiva-Defensiva"
language: "TypeScript / JavaScript (Client-Side)"
tags:
  - "herramienta"
  - "seguridad-ofensiva-defensiva"
  - "jwt"
  - "pentest"
  - "crypto"
  - "web"
status: "Operativo"
---

# 🛠️ HackNexus Toolkit (Suite Client-Side & JWT Toolkit)

> [!NOTE] **Propósito Táctico**: Suite modular de más de 100 utilidades de pentesting, criptografía y análisis forense que corre **100% en el navegador (Client-Side)** con cero telemetría externa.
> **Autor / Organización**: `D1se0` | **Repositorio**: [D1se0/hacknexus](https://github.com/D1se0/hacknexus) | **Web Live**: [https://d1se0.github.io/hacknexus/](https://d1se0.github.io/hacknexus/)

---

## ⚡ Descripción Técnica y Módulos Clave
HackNexus reúne utilidades ofensivas y defensivas ejecutadas enteramente mediante la **Web Crypto API** y **Web Workers** nativos del navegador. Esto garantiza total privacidad operativa (OPSEC) al manipular datos confidenciales (claves, tokens, hashes o payloads) sin exponerlos a servicios en la nube de terceros.

### 🔑 Módulo Especializado: JWT Toolkit (`/#/jwt`)
El módulo de JSON Web Tokens permite realizar pruebas de seguridad avanzadas sobre autenticación moderna:
1. **Inspección Estructurada**: Desglose automático de Header, Payload y Signature, con traducción de marcas de tiempo (`iat`, `exp`, `nbf`).
2. **Ataque `alg: none`**: Mutación y forja instantánea de cabeceras sin firma para validar si el backend autoriza peticiones sin comprobación criptográfica.
3. **Manipulación de Claims (Escalación de Privilegios / IDOR)**: Edición de campos como `role`, `is_admin`, `tenant_id` o `sub` para generar tokens manipulados de prueba.
4. **Cracking de Secretos HMAC (HS256/384/512)**: Fuerza bruta y ataques por diccionario contra secretos simétricos directamente en el navegador mediante paralelización en Web Workers.
5. **Re-firmado en Caliente**: Firma inmediata de tokens alterados tras recuperar o definir la clave secreta.

### 🧰 Otros Módulos Destacados de la Suite
- **Criptografía & Hashes**: Generación, identificación y cracking de hashes (MD5, SHA1, SHA256, NTLM, Bcrypt).
- **Redes & OSINT**: Calculadora CIDR/VLSM, resolución de subredes, lookup de registros y cabeceras HTTP.
- **Generador de Shells Inversas**: Plantillas listas para bash, sh, python, php, socat y powershell.
- **Esteganografía & Forense**: Inspección de metadatos EXIF, strings y análisis de archivos.

---

## 💻 Acceso Rápido y Despliegue Local
```bash
# 1. Uso directo en navegador (sin instalación ni configuración):
https://d1se0.github.io/hacknexus/#/jwt

# 2. Despliegue local offline / Air-gapped (opcional para máxima seguridad):
git clone https://github.com/D1se0/hacknexus.git
cd hacknexus
npm install
npm run dev
# Abrir en http://localhost:5173
```

---

## 🎯 Casos de Uso para Agentes de IA / Pentest / Bug Bounty
- **Triaje de Autenticación en Bug Bounty**: Alternativa segura y privada a `jwt.io` durante auditorías de APIs REST, GraphQL y microservicios.
- **Validación Rápida de Vectores de Inyección**: Prueba de tokens con cabeceras `kid` alteradas, inyección de SQL en `kid` o bypass de validaciones de firma.
- **Integración con Metodologías de Cyber-Vault**:
  - [[02-Metodologias/Tacticas-Bug-Bounty/OAuth-Autenticacion|Tácticas de OAuth y Autenticación]]
  - [[01-Vulnerabilidades/vulnerabilities.base|Base de Vulnerabilidades (Bypasses JWT)]]

---

## 🔗 Referencias y Enlaces Oficiales
- 🌐 **Web en Vivo**: [https://d1se0.github.io/hacknexus/#/jwt](https://d1se0.github.io/hacknexus/#/jwt)
- 🐙 **Repositorio GitHub**: [https://github.com/D1se0/hacknexus](https://github.com/D1se0/hacknexus)

---
*Ficha táctica estructurada para la base de conocimiento y orquestación de agentes de Cyber-Vault.*