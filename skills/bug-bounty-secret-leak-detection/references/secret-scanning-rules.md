# Secret Leak Detection & Hardening Reference

## 1. Riesgos de Secretos Expuestos

La fuga de tokens o secretos en repositorios o bundles JS cliente permite a los atacantes acceder directamente a servicios de infraestructura backend sin pasar por los mecanismos de autenticación web.

## 2. Remediación Segura

- Utilice gestores de secretos centralizados (ej. HashiCorp Vault, AWS Secrets Manager, Azure Key Vault).
- Implemente escaneo continuo con `gitleaks` en los flujos de trabajo de integración continua.
- Despliegue rotación de credenciales automatizada cuando se detecte un secreto comprometido.
