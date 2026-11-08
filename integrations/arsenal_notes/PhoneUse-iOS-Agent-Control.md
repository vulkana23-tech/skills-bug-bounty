---
title: "PhoneUse — Control Autónomo de iPhones para Agentes de IA"
author: "lxe (ex-OpenAI, Netflix, Uber)"
github_repo: "https://github.com/lxe/phoneuse"
category: "03-Herramientas/Harness-Engineering"
tags:
  - "herramienta"
  - "harness-engineering"
  - "ios"
  - "mobile"
  - "agent-control"
  - "mcp"
status: "Operativo / Skill Activa"
---

# 📱 PhoneUse — Plano de Control y Skill de IA para iPhones Reales

> [!NOTE] **Propósito Táctico**: Framework open-source que permite a agentes de IA ver y operar un **iPhone físico real y sin modificar** sin necesidad de jailbreak, sin cables y sin cuentas de desarrollador de pago.
> **Autor**: `lxe` | **Repositorio**: [lxe/phoneuse](https://github.com/lxe/phoneuse) | **Web**: [phoneuse.com](https://phoneuse.com)

---

## ⚡ El Truco de Ingeniería: Cómo Supera las Barreras de iOS

iOS es un ecosistema tradicionalmente cerrado y hostil para la automatización sin certificados de Apple. PhoneUse resuelve esto combinando **dos tecnologías nativas que ya vienen en cualquier iPhone**:

```
 ┌──────────────────────┐                     ┌──────────────────────────┐
 │    IPHONE FÍSICO     │                     │     PC DEL AGENTE IA     │
 │                      │  AirPlay Streaming  │                          │
 │  • Pantalla nativa   │ ──────────────────▶ │  • Captura de frames     │
 │  • Apps bancarias    │                     │    (GStreamer / UxPlay)  │
 │  • Redes sociales    │                     │  • Visión por computador │
 │                      │  Bluetooth HID      │                          │
 │  • AssistiveTouch    │ ◀────────────────── │  • Clics / Taps / Swipes │
 │    (Puntero táctil)  │   (Ratón y Teclado) │  • Tecleo de texto       │
 └──────────────────────┘                     └──────────────────────────┘
```

1. **Visión (AirPlay / Screen Mirroring)**:
   - El iPhone transmite su pantalla en tiempo real al PC por la red local mediante el protocolo AirPlay nativo (usando `UxPlay` y `GStreamer`).
   - El agente recibe capturas instantáneas de pantalla (`grim` o HTTP stream en `:8777`) para analizar el DOM visual y las apps.
2. **Control Táctil (Bluetooth HID + AssistiveTouch)**:
   - El PC (o un microcontrolador ESP32 puente) se empareja con el iPhone como si fuera un **ratón y teclado Bluetooth físico**.
   - Al activar el puntero de accesibilidad (*AssistiveTouch*) en el iPhone, el agente envía toques precisos, desplazamientos de pantalla (*swipes*) y texto tecleado sin que iOS sospeche que quien maneja el dispositivo es una IA.

---

## 🔌 Integración con Agentes de IA (Skill & Servidor MCP)
* **Skill Integrada**: Incluye una especificación [`phoneuse/skill/SKILL.md`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/scratch/phoneuse/skill/SKILL.md) para que modelos como Claude, GPT o Gemini sepan invocar los comandos de terminal (`phoneuse status`, `phoneuse tap`, `phoneuse type`, `phoneuse swipe`).
* **Sinergia Total con ARTEMIS**:
  - **ARTEMIS (Google)** domina el control y auditoría de **Android** y emuladores.
  - **PhoneUse (lxe)** completa la ecuación para **iPhones reales**.

---
*Ficha técnica catalogada en la sección de Harness Engineering del Cyber-Vault.*