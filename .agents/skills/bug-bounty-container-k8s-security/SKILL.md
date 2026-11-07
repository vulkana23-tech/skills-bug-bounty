---
name: bug-bounty-container-k8s-security
description: Evaluación de seguridad en contenedores Docker y orquestadores Kubernetes. Dockerfile Hardening, análisis de Pods privilegiados, malas configuraciones RBAC y Pod Security Standards.
---

# Skill: Container & Kubernetes Security Assessment

Esta habilidad capacita al agente para evaluar la configuración de contenedores Docker y clústeres Kubernetes, identificando pods privilegiados, secretos expuestos en variables de entorno y malas configuraciones de control de acceso basado en roles (RBAC).

## 📌 Vectores de Auditoría Container & K8s

### 1. Dockerfile & Image Hardening
- Contenedores ejecutándose como usuario `root` (`privileged: true`).
- Inclusión de secretos o credenciales en capas de imagen Docker.

### 2. Kubernetes RBAC Misconfigurations
- Service Accounts con permisos de superusuario (`cluster-admin`) asignados innecesariamente a pods expuestos a la web.

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[k8s-security-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-container-k8s-security/references/k8s-security-guide.md)
