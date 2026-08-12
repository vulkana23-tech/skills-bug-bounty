# 📚 Case Study: M365 / Entra ID OAuth Application Consent Takeover

## 🎯 Executive Summary
- **Target**: Enterprise Identity Tenant (Microsoft 365 / Azure AD Entra ID)
- **Vulnerability Class**: Excessive OAuth Scope Consent & Illicit Grant Escalation
- **Impact**: High (CVSS 8.1) - Unprivileged user consent granting directory-wide email read access
- **Skill Vectors Applied**: [`bug-bounty-enterprise-identity-matrix`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-enterprise-identity-matrix/SKILL.md), [`bug-bounty-oauth-token`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-oauth-token/SKILL.md)

---

## 🔍 Attack Vector Analysis

### 1. OAuth App Registration Audit
An external multi-tenant Azure application requested the following Graph API permission scopes:
- `Mail.ReadWrite`
- `Directory.Read.All`
- `offline_access`

### 2. Lack of Admin Consent Enforcement
The tenant configuration allowed unverified user consent for applications requesting low-tier permission boundaries, which could be abused to bypass MFA.

### 3. Remediation Guidance
- Restrict user consent settings in Azure Portal: **Do not allow user consent**.
- Enforce Admin Consent Workflow for all Graph API scope requests.
