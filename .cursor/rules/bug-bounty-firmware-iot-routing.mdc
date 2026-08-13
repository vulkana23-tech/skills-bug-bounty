---
name: bug-bounty-firmware-iot-routing
description: Enrutamiento y metodología de ingeniería inversa para imágenes de firmware e IoT. Extracción con Binwalk, análisis de sistemas de archivos SquashFS/JFFS2 y secretos embebidos.
---

# Skill: Firmware & IoT Reverse Engineering Router

Esta habilidad capacita al agente para desempaquetar archivos de firmware, auditar sistemas de archivos embebidos y extraer secretos o servicios vulnerables.

## 📌 Flujo de Auditoría de Firmware

### 1. Extracción de Firmware
- **Binwalk**: Análisis de cabeceras de compresión y firmas de archivos (`binwalk -e firmware.bin`).
- **Montaje de Filesystem**: Extracción e inspección de imágenes `squashfs`, `jffs2`, `ext2/3/4` o `ubifs`.

### 2. Análisis de Configuración y Secretos
- Extracción de claves privadas SSH (`/etc/dropbear/`), hash de contraseñas (`/etc/shadow`) y scripts de inicio (`/etc/init.d/`).
- Auditoría de servidores web embebidos (Lighttpd, GoAhead, uHttpd).

---

## 📚 Referencias Técnicas

Consulta la guía técnica de firmware e IoT en:
[firmware-iot-guide.md](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-firmware-iot-routing/references/firmware-iot-guide.md)
