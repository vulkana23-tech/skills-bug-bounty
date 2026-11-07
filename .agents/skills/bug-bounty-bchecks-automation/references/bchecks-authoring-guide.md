# Burp Suite BChecks Authoring Reference Guide

## 1. Reglas BChecks Defensivas y de Auditoría

- Pruebe los archivos BCheck en entornos de staging antes de importarlos al perfil activo de Burp Scanner.
- Mantenga los tags estructurados (`tags: "auth", "headers"`) para facilitar el filtrado modular.

## 2. Remediación Segura

- Asegúrese de que los controles de acceso se evalúen a nivel de lógica de aplicación y no basándose únicamente en filtros de URL de proxies inversos.
