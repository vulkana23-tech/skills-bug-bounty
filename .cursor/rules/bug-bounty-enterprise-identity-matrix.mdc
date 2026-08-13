---
name: bug-bounty-enterprise-identity-matrix
description: Metodología de auditoría de seguridad para infraestructura de identidad empresarial, M365/Entra ID, Okta, VMware vCenter y dispositivos de borde SSL-VPN.
---

# Skill: Enterprise Infrastructure & Identity Attack Matrix

Esta habilidad proporciona una metodología de auditoría para la superficie de ataque de identidad y dispositivos de borde empresariales.

## 📌 Vectores de Auditoría Empresarial

### 1. Microsoft 365 & Entra ID (Azure AD)
- **Consent Abuse**: Evaluación de permisos de aplicaciones OAuth de terceros y consentimiento de usuarios imprevisto.
- **Conditional Access Policy Gaps**: Auditoría de desconfiguraciones en políticas de acceso condicional y autenticación MFA.
- **Graph API Permissions**: Inspección de permisos excesivos (`Directory.ReadWrite.All`, `RoleManagement.ReadWrite.Directory`).

### 2. proveedores de Identidad (Okta / SAML / OIDC)
- **SAML Assertion Modification**: Verificación de firmas XML en aserciones SAML y manipulación de IDs de usuario (`NameID`).
- **OAuth / OIDC Token Auditing**: Evaluación de desajustes en `redirect_uri` y falta de validación `PKCE`.

### 3. Dispositivos de Borde y Virtualización (SSL-VPN / vCenter)
- **VMware vCenter Server**: Verificación de apis expuestas (`/ui/vcenter-client`, `/sdk`) y bypasses de autenticación SAML.
- **SSL-VPN Appliances**: Auditoría de vulnerabilidades de desbordamiento de búfer y lectura de archivos en Fortinet, Ivanti Connect Secure y Citrix Bleed.

---

## 📚 Referencias Técnicas

Consulta la guía técnica de identidad empresarial en:
[enterprise-identity-guide.md](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-enterprise-identity-matrix/references/enterprise-identity-guide.md)
