# Security Environment & Tooling Reference

## 1. Organización del Entorno de Auditoría

- Utilice entornos aislados (máquinas virtuales VMware/VirtualBox o contenedores Docker) para evitar interferencias con el sistema operativo principal.
- Mantenga los diccionarios de palabras (`wordlists` como `SecLists`) centralizados y actualizados regularmente.

## 2. Recomendaciones de Rendimiento

- Configure filtros de coincidencia (`Match and Replace`) en el proxy para adjuntar automáticamente cabeceras de identificación de auditoría en cada solicitud HTTP saliente.
