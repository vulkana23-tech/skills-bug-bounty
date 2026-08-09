# HackerOne Vulnerability Report Template

**Vulnerability Name:** {{VULNERABILITY_NAME}}
**Vulnerability Type:** {{VULNERABILITY_TYPE}} (e.g. IDOR, XSS, SSRF, Request Smuggling)
**Target Asset:** {{TARGET_URL_OR_ASSET}}
**Severity:** {{SEVERITY_LEVEL}} (Low / Medium / High / Critical)
**CVSS v3.1 Score:** {{CVSS_SCORE}} (e.g. 8.6 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N)

---

## 📝 Summary
{{SUMMARY_DESCRIPTION}}

---

## 🔍 Steps to Reproduce

1. Navigate to `{{TARGET_URL}}`
2. Send the following HTTP request:

```http
{{HTTP_REQUEST_SAMPLE}}
```

3. Observe the response containing sensitive data or executing the payload:

```http
{{HTTP_RESPONSE_SAMPLE}}
```

---

## 💥 Impact
{{BUSINESS_IMPACT_EXPLANATION}}

---

## 🛡️ Remediation
{{REMEDIATION_RECOMMENDATION}}
