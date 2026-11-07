# 🏢 Technical Reference: Enterprise Identity & Edge Security Guide

## 🔑 Entra ID / M365 Audit Checklist
- **Audit Tool**: `ROADtools` or `GraphRunner`.
- **OAuth Permissions Check**: Identify unverified multi-tenant applications with admin consent rights.

## 🔐 SSL-VPN & Edge Appliances Identification
- **Ivanti Connect Secure**: Inspect endpoint `/dana-na/auth/url_default/welcome.cgi`
- **Citrix Bleed**: Test memory leak capability on `/oauth/idp/.well-known/openid-configuration`
- **Fortinet FortiGate**: Monitor CVE-2024-21762 and CVE-2023-27997 edge patches.
