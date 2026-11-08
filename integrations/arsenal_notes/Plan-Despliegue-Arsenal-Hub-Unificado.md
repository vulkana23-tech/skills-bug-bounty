---
title: "Plan de Despliegue: Arsenal Hub Unificado (AI Red Team, Pentesting Swarm & Network Tools)"
date: 2026-11-08
category: "Harness-Engineering"
status: "Activo (Capa 1 operativa; Capas 2 y 3 preparadas para ampliación de disco)"
tags:
  - "arsenal"
  - "harness-engineering"
  - "red-team"
  - "pentest"
  - "ai-security"
  - "ad-security"
  - "roadmap"
---

# 🏛️ Plan de Despliegue: Arsenal Hub Unificado (War Room 2026)

> [!IMPORTANT] **Estado del Ecosistema**:
> - **Capa 1 (Activa y Operativa)**: `T3MP3ST`, `Terminal-MCP`, `NetExec-mcp`, `nmap-vulners`, `obscura` (skill), `pwn-hunter` (skill), `Semgrep`, `Trivy`, `HackNexus`.
> - **Capas 2 y 3 (Catalogadas y preparadas para cuando haya >= 25 GB libres)**: `AD-PathFinder`, `SpiderFoot`, `DroidHunter`, `HT-Forge`, `Wifite2`, `AgentPilot`, `Garak`, `PyRIT`, `Promptfoo`, `OpenVAS`, `Strix`.

---

## 📊 1. Matriz Integral del Arsenal Unificado

```
                               [ OPERADOR HUMANO ]
                                       │
                                       ▼
                     [ ORQUESTADOR CENTRAL DE AGENTES ]
                 (Cursor, OpenCode, DeepSeek Harness, WorkBuddy)
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
   CAPA 1: ACTIVAS              CAPA 2: AI RED TEAM            CAPA 3: PENTESTING PESADO
   (Operativas en local)        (Venv Python con `uv`)         (Docker Efímero / Lab)
   [Consumo mínimo]             [~3.5 GB compartidos]          [0 GB fijos en reposo]
```

### Tabla Maestra de Herramientas:

| Herramienta | Tier | Categoría | Estado Actual | Rol Operativo |
| :--- | :---: | :--- | :---: | :--- |
| **`nmap-vulners`** | **S** | Recon / Escaneo de Vulnerabilidades | ✅ **Instalada** | Convierte Nmap en escáner de CVEs automático en segundos (`--script nmap-vulners`). |
| **`NetExec-mcp`** | **S** | Active Directory / Redes Windows | ✅ **Activo MCP** | Movimiento lateral, Pass-the-Hash y enumeración SMB/LDAP/WinRM desde el chat de agentes. |
| **`obscura`** | **S** | Headless Browser Sigiloso (Rust) | ✅ **Skill Activa** | Navegador de 30 MB RAM compatible con CDP y evasión anti-bot para agentes web. |
| **`t3mp3st`** | **S** | Meta-Arnés Ofensivo Multiagente | ✅ **Activo MCP** | Orquestación autónoma de escaneo, recon y explotación en 8 fases MITRE ATT&CK. |
| **`terminal-mcp`** | **S** | Capturador Forense de Evidencias | ✅ **Activo MCP** | Genera capturas PNG profesionales con marcos y colores ANSI para reportes de Bug Bounty. |
| **`pwn-hunter`** | **S** | Explotación Binaria & Memoria | ✅ **Skill Activa** | ROP chains, Heap, Format Strings, Seccomp y Kernel con Refusal Engineering. |
| **`NetSPI/AD-PathFinder`**| **A** | Active Directory & BloodHound CE | 📋 *Anotada* | Mapeo de rutas de ataque cruzando ADCS, MSSQL, SCCM y contraseñas débiles. |
| **`SpiderFoot`** | **A** | OSINT & Mapeo de Superficie | 📋 *Skill Lista* | Consulta automática de más de 200 fuentes públicas e inteligencia en grafo. |
| **`hexsecteam/DroidHunter`**| **A** | Pentesting Móvil Android | 📋 *Anotada* | Auditoría de APKs, ADB, logcat y bypasses móviles (complemento de ARTEMIS). |
| **`HT-Forge`** | **B** | Suite Web Modular | 📋 *Anotada* | Fuzzing de parámetros y comprobación de inyecciones web y APIs. |
| **`HKUDS/AgentPilot`** | **B** | Harness Engineering & 9B Models| 📋 *Anotada* | Referencia de arquitectura para guiar pasos de agentes con modelos pequeños. |
| **`wifite2`** | **B** | Auditoría Wi-Fi / Wireless | 📋 *Anotada* | Captura desatendida de handshakes WPA2 y ataques WPS (requiere hardware USB externo). |
| **`skitter-creek-bath-salts`**| **C** | Hardware Security / DRAM Scramble| 📋 *Anotada* | PoC avanzada de investigación de hardware x86 por Chris Domas. |
| **`Garak / PyRIT / Promptfoo`**| **A** | AI Red Teaming & LLM Security | 📋 *Capa 2* | Batería de auditoría para modelos de IA, inyecciones de prompt y jailbreaks. |
| **`OpenVAS / Strix`** | **A** | Pentesting Automatizado | 📋 *Capa 3* | Escáneres de infraestructura completa sobre Docker efímero. |

---

## 🛠️ 2. Guía de Ejecución Rápida de las Nuevas Herramientas Activas

### 1. Escaneo de CVEs Inmediato con Nmap:
```bash
# En WSL Ubuntu o en consola:
nmap -sV --script nmap-vulners <IP-o-Dominio>
```
*Devolverá los puertos abiertos con su lista directa de CVEs, CVSS y enlaces a exploits.*

### 2. Uso de NetExec MCP desde tus Agentes:
En Cursor, OpenCode, DSH o WorkBuddy solo debes pedir:
> *"Agente, usa NetExec para comprobar si las credenciales de este usuario tienen acceso administrativo vía SMB o WinRM sobre este rango."*

### 3. Navegación Web Ligera con Obscura:
> *"Agente, utiliza la skill de Obscura para navegar este sitio web, extraer el DOM con JavaScript activo y eludir los bloqueos de Cloudflare usando su huella aleatoria."*

---
*Ficha técnica actualizada y sincronizada en el Cyber-Vault y repositorio de control de versiones.*