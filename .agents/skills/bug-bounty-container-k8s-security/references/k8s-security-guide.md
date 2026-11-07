# Kubernetes & Container Security Reference Guide

## 1. Riesgos en Entornos de Contenedores

Ejecutar contenedores en modo privilegiado permite a un atacante que logre ejecución de código dentro del contenedor escapar hacia el nodo host del clúster Kubernetes.

## 2. Remediación Segura

- Utilice imágenes de contenedor mínimas (ej. `distroless` o Alpine) y fuerce la ejecución con usuarios no privilegiados (`USER node`).
- Implemente Pod Security Admission (PSA) en modo `Restricted`.
- Restrinja el acceso al API Server de Kubernetes desde redes no autorizadas.
