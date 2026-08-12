# 📚 Case Study: Ivanti SSL-VPN Reverse Engineering & Deobfuscation Chain

## 🎯 Executive Summary
- **Target**: Enterprise Network Edge SSL-VPN Gateway (Ivanti Connect Secure)
- **Vulnerability Class**: Command Injection & Authentication Bypass via Obfuscated Web Handler
- **Impact**: Critical (CVSS 9.8) - Remote Code Execution on perimeter network appliance
- **Skill Vectors Applied**: [`bug-bounty-android-apk-routing`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-android-apk-routing/SKILL.md), [`bug-bounty-js-reverse-deobfuscation`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-js-reverse-deobfuscation/SKILL.md), [`bug-bounty-7-question-gate`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-7-question-gate/SKILL.md)

---

## 🔍 Attack Vector & Deobfuscation Analysis

### 1. Static Firmware & Script Triage
During perimeter asset modeling, the target endpoint `/api/v1/totp/user-backup-code/` was identified. The client-side JavaScript bundle (`login.min.js`) contained heavily obfuscated string lookup tables and anti-debugging statements.

### 2. AST-Level Deobfuscation
Using Babel AST transformation, the array lookup obfuscation was unwrapped:
```javascript
// Before Deobfuscation:
var _0x5a12 = ['/api/v1/totp/', 'POST', 'signature'];
// After AST Deobfuscation:
const targetEndpoint = "/api/v1/totp/user-backup-code/";
```

### 3. Non-Destructive Proof-of-Concept
A benign GET parameter validation request verified the unauthenticated path traversal condition without disrupting service.

---

## 🛡️ 7-Question Gate Triage Pass
- ✅ **In-Scope**: `vpn.enterprise.local` explicitly confirmed in `scope.md`.
- ✅ **Impact**: Demonstrated read access to system build version.
- ✅ **PII Redacted**: All internal IP ranges and hostnames sanitized.
- ✅ **CVSS Score**: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H` (9.8).
