# 🛡️ Authorization Scope Contract & Defense Policy

## 📋 Operational Scope Declaration

This file establishes the explicitly authorized boundaries for security assessments and vulnerability research.

### Authorized Targets (In-Scope)
- Domain / Subdomains: `*.example.local`, `api.targetapp.local`
- Mobile Packages: `com.targetapp.client`
- Binary Files: `/binaries/sample_target`
- Code Repositories: Local repository static analysis

### Explicitly Excluded (Out-of-Scope)
- Production Cloud Infrastructure & Live User Data
- Denial of Service (DoS/DDoS) testing
- Destructive payload execution or data wiping
- Unsanctioned third-party APIs or infrastructure

---

## 🔒 Safety & Compliance Commitments

1. **Non-Destructive Testing**: All validations must be benign (e.g. proof of concept read operations or parameter inspection).
2. **Data Privacy**: No private customer or employee PII may be stored, exfiltrated, or modified.
3. **Responsible Disclosure**: Findings will be documented with remediation guidance following authorized reporting protocols.
