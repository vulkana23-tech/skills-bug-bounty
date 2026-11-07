---
name: ares-redteam
description: "Orquestación y ejecución de operaciones Red Team con ARES (Automated Red Team Engagement System v6.0). Incluye 66 módulos MITRE ATT&CK para Active Directory, movimiento lateral, evasión de EDR, grafos de ataque hacia Domain Admin y simulación pre-flight gobernada."
---

# ARES · Automated Red Team Engagement System (v6.0 Enterprise)

ARES es la plataforma de orquestación de Red Teaming y simulación de brechas (BAS) instalada en el entorno local.

## 🚀 Ruta de Ejecución Local
```powershell
rag\pentesting-everything\.venv\Scripts\ares.exe <comando>
```

---

## 🛠️ Comandos Esenciales de ARES

### 1. Diagnóstico de Salud
```powershell
rag\pentesting-everything\.venv\Scripts\ares.exe doctor
rag\pentesting-everything\.venv\Scripts\ares.exe mcp doctor
```

### 2. Gestión de Campañas y Alcance (ScopeGuard)
```powershell
# Crear campaña autorizada con alcance estricto
rag\pentesting-everything\.venv\Scripts\ares.exe campaign create --name "Lab-Auditoria" --client "Internal" --targets "10.0.0.0/24,192.168.1.0/24"

# Listar campañas activas
rag\pentesting-everything\.venv\Scripts\ares.exe campaign list
```

### 3. Exploración de Módulos MITRE ATT&CK (66 módulos)
```powershell
# Listar todos los módulos cargados
rag\pentesting-everything\.venv\Scripts\ares.exe module list

# Filtrar por categoría (ad, lateral, credential, persistence, windows, recon)
rag\pentesting-everything\.venv\Scripts\ares.exe module list --category ad

# Ver detalles y parámetros de un módulo
rag\pentesting-everything\.venv\Scripts\ares.exe module info ad.kerberoast
```

### 4. Simulación Pre-Flight y Ejecución
ARES utiliza el principio de **Fail-Closed Governance**:
1. **Pre-flight Dry Run (Sin paquetes):** Valida sintaxis, verifica que el host esté en el ScopeGuard, calcula el nivel de ruido OPSEC y emite un token HMAC de confirmación válido por 60 segundos.
2. **Ejecución Real:** Requiere autorización o el token de confirmación previo.

```powershell
# Ejecución directa de enumeración de usuarios en Active Directory
rag\pentesting-everything\.venv\Scripts\ares.exe module run ad.enum_users --dc 10.0.0.5 --domain corp.local

# Ejecución de Kerberoasting
rag\pentesting-everything\.venv\Scripts\ares.exe module run ad.kerberoast --dc 10.0.0.5 --domain corp.local
```

### 5. Grafos de Ataque hacia Domain Admin
```powershell
# Consultar caminos más cortos hacia Domain Admin en una campaña
rag\pentesting-everything\.venv\Scripts\ares.exe graph query --campaign-id <ID> --target "Domain Admins"
```

### 6. Generación de Reportes Profesionales
```powershell
rag\pentesting-everything\.venv\Scripts\ares.exe report generate --campaign-id <ID> --format html
rag\pentesting-everything\.venv\Scripts\ares.exe report generate --campaign-id <ID> --format markdown
```

---

## 🤖 Servidor MCP Integrado (Claude Desktop & Antigravity)

ARES expone 9 herramientas MCP para agentes autónomos:
- `ares_list_campaigns`
- `ares_get_campaign_status`
- `ares_list_findings`
- `ares_get_remediation_guidance` (Mitigaciones MITRE D3FEND)
- `ares_query_attack_graph` (Ruta a Crown Jewels)
- `ares_inspect_module_catalog` (Catálogo 66 módulos)
- `ares_verify_target_scope` (Validación ScopeGuard)
- `ares_dry_run_module` (Pre-flight simulación + token 60s)
- `ares_execute_module` (Ejecución gobernada)

