# DFIR & Incident Response Reference Guide

## 1. Muestreo de Indicadores de Compromiso (IoCs)

- **Direcciones IP Atacantes**: Filtrar solicitudes con volumen atípico en intervalos de tiempo cortos.
- **User-Agents Maliciosos**: Identificar escáneres automáticos no identificados (`sqlmap`, `nikto`, `nmap`).
- **Modificación de Archivos de Sistema**: Verificar marcas de tiempo de modificación (mtime/ctime) en archivos ejecutables.

## 2. Buenas Prácticas de Respuesta

- Conserve la evidencia digital en un estado inalterado (copias de respaldo de imágenes de disco y memoria RAM).
- Centralice la recolección de registros en un sistema SIEM protegido con permisos de solo escritura.
