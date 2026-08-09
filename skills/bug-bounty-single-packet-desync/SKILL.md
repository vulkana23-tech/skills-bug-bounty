---
name: bug-bounty-single-packet-desync
description: Orquestación de ataques Single-Packet para desincronización precisa. Envío de fragmentos TCP sincronizados para eliminar la variabilidad de latencia de red.
---

# Skill: Single-Packet Attack Orchestration

Esta habilidad capacita al agente para aplicar técnicas de ataques de un solo paquete TCP (Single-Packet Attack / Last-Byte Sync) en pruebas de desincronización HTTP y condiciones de carrera (Race Conditions).

## 📌 Principio del Single-Packet Attack

- Enviar todos los bytes de la solicitud excepto el último byte en conexiones TCP separadas, y transmitir el último byte de todas las conexiones en un único paquete TCP final para forzar el procesamiento concurrente exacto en el backend.

---

## 📚 Referencias Técnicas

Consulta los detalles en:
[single-packet-techniques.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-single-packet-desync/references/single-packet-techniques.md)
