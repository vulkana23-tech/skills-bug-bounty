# 📋 Technical Reference: 7-Question Validation Gate Checklist

## 🔍 Validation Checklist Matrix

| # | Question Gate | Passing Criteria | Rejection Criteria |
|---|---|---|---|
| 1 | In-Scope Verification | Domain/IP explicitly listed in program policy | Out-of-scope third party service or unmapped IP |
| 2 | Practical Impact | Demonstrable privilege escalation, data access, or state change | Informational header disclosure or self-XSS |
| 3 | Live PoC Execution | Working cURL command or python PoC script | Theoretical assumption without empirical trace |
| 4 | PII & Secret Redaction | All session tokens, emails, and passwords masked (`XXXXX`) | Unredacted customer personal data in report screenshots |
| 5 | Root Cause Isolation | Identified missing authorization check or unescaped input | Vague description ("Application is vulnerable") |
| 6 | Accurate CVSS Scoring | Calculated string matching CVSS v3.1 specification | Inflated severity (e.g. marking missing headers as High/Critical) |
| 7 | Remediation Guidance | Specific code-level patch recommendation | Generic advice ("Fix the security issue") |
