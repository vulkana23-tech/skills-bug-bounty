---
name: bug-bounty-iot-device-auditing
description: Auditoría de seguridad en dispositivos IoT y firmware. Inspección de servidores web embebidos, análisis de imágenes con binwalk, extracción de credenciales e interfaces de depuración.
---

# Skill: IoT Device & Firmware Security Assessment

Esta habilidad capacita al agente para evaluar la seguridad de dispositivos IoT e interfaces web embebidas, analizando imágenes de firmware comprimido e identificando credenciales por defecto o servicios expuestos.

## 📌 Vectores de Auditoría IoT

### 1. Extracción de Firmware con Binwalk
- Extraer sistemas de archivos embebidos (SquashFS, CramFS, JFFS2):
  `binwalk -e firmware.bin`

### 2. Credenciales y Hardening Web Embebido
- Inspeccionar archivos `/etc/shadow`, `/etc/passwd` y archivos de configuración web en búsqueda de claves privadas SSH o contraseñas hardcoded.

---

## 📚 Referencias Técnicas

Consulta la guía de firmware en:
[iot-firmware-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-iot-device-auditing/references/iot-firmware-guide.md)
