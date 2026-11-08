---
title: "Plan de Despliegue: Arsenal Hub Unificado (AI Red Team & Pentesting Swarm)"
date: 2026-11-08
category: "Harness-Engineering"
status: "Pendiente (Esperando liberación de espacio en disco)"
tags:
  - "arsenal"
  - "harness-engineering"
  - "red-team"
  - "pentest"
  - "ai-security"
  - "roadmap"
---

# 🏛️ Plan de Despliegue: Arsenal Hub Unificado (War Room 2026)

> [!IMPORTANT] **Estado del Proyecto**: Documentado y estructurado para su despliegue cuando se disponga de margen de almacenamiento en disco (`C:\` u otra unidad).
> **Diagnóstico del Sistema**: Windows host, WSL2 Ubuntu, Docker v29.9.2, GPU NVIDIA RTX 3060.
> **Espacio actual en C:** ~11.4 GB libres | **Espacio recomendado para inicio:** >= 25-30 GB libres.

---

## 📊 1. Matriz de Herramientas y Requerimientos de Espacio

Si se intentara instalar todo de forma tradicional, el espacio requerido superaría los **35-45 GB**. Con la arquitectura **Modular Bajo Demanda (Just-In-Time)**, el consumo fijo se reduce a solo **~5 GB**, delegando lo pesado a contenedores temporales.

```
                               [ OPERADOR HUMANO ]
                                       │
                                       ▼
                     [ ORQUESTADOR CENTRAL DE AGENTES ]
                 (Cursor, OpenCode, DeepSeek Harness, WorkBuddy)
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
   CAPA 1: LIGERAS              CAPA 2: AI RED TEAM            CAPA 3: PESADAS
   (Siempre en disco)           (Venv Python con `uv`)         (Docker Efímero)
   [~1.5 GB total]              [~3.5 GB compartidos]          [0 GB en reposo]
```

### Clasificación por Capas Operativas:

| Capa | Herramientas | Espacio Estimado | Método de Ejecución |
| :--- | :--- | :---: | :--- |
| **Capa 1: Ligeras (Operativas ya)** | **T3MP3ST**, **Terminal-MCP**, **Semgrep**, **Trivy**, **HackNexus** | ~1.5 GB | Binarios locales y Node.js en `C:\Users\logir\Projects\` (Ya configuradas en MCP). |
| **Capa 2: Suite AI Red Team** | **NVIDIA Garak**, **Azure PyRIT**, **Promptfoo**, **LLM Guard**, **NeMo Guardrails**, **Giskard** | ~3.5 GB | Entorno virtual único con `uv` (`C:\Users\logir\Projects\Arsenal-Hub\venv-ai`). |
| **Capa 3: Agentes Swarm & Escáneres** | **OpenVAS**, **Strix**, **PentestGPT**, **OpenSandbox**, **CyberStrike**, **MAPTA**, **Shannon**, **hackingBuddyGPT** | ~0 GB fijos (~10 GB al correr) | Contenedores Docker temporales (`docker run --rm`), destruidos tras generar informe. |

---

## 🛠️ 2. Playbook de Despliegue Paso a Paso (Para cuando haya espacio)

### Paso 1: Preparación del Directorio Raíz
```bash
# Crear el directorio del Hub unificado
mkdir -p "C:\Users\logir\Projects\Arsenal-Hub"
cd "C:\Users\logir\Projects\Arsenal-Hub"
```

### Paso 2: Creación del Entorno Compartido de AI Red Team (Capa 2)
Para evitar que cada herramienta duplique librerías masivas como PyTorch o Transformers, se compila un único entorno con `uv`:
```bash
# Crear venv con Python 3.12
uv venv venv-ai --python 3.12

# Instalar suites de evaluación y seguridad de LLM en un solo paso
uv pip install --python venv-ai/Scripts/python.exe \
  garak \
  promptfoo \
  pyrit \
  llm-guard \
  giskard
```

### Paso 3: Configuración de la Capa Docker Efímera (Capa 3)
Para herramientas que requieren bases de datos pesadas o sistemas Linux aislados:

1. **OpenVAS / Greenbone**:
   - Usar el contenedor ligero de evaluación: `docker run -d -p 9392:9392 --name openvas greenbone/gvm` sólo durante la auditoría.
2. **Strix / PentestGPT / OpenSandbox**:
   - Ejecutarlos montando volúmenes compartidos hacia `C:\Users\logir\Projects\terminal-screenshots` para almacenar evidencias.

---

## 🎯 3. Modo de Operación Integrado (Lenguaje Natural)

Una vez desplegado el Hub, no será necesario recordar comandos. El agente actuará como **Director de Operaciones**:

1. **Auditoría de Código y Dependencias**:
   - *"Agente, ejecuta Semgrep y Trivy sobre este proyecto y filtra vulnerabilidades críticas."*
2. **Seguridad y Robustez de Modelos IA**:
   - *"Agente, lanza una batería de pruebas con Garak y PyRIT contra el endpoint del LLM para detectar inyecciones de prompt y fugas de datos."*
3. **Pentesting Autónomo y Reporte con Evidencias**:
   - *"Agente, inicia T3MP3ST contra el laboratorio autorizado, utiliza Strix para el análisis web y genera capturas PNG estilizadas con Terminal-MCP."*

---
*Ficha técnica de planificación persistida en el Cyber-Vault para reanudación inmediata.*