# CVSS v3.1 Quick Reference & Calculator Guide

| Metric | Short | Options | Description |
| :--- | :--- | :--- | :--- |
| **Attack Vector** | AV | Network (N) / Adjacent (A) / Local (L) / Physical (P) | Where attack is executed |
| **Attack Complexity** | AC | Low (L) / High (H) | Specialized conditions required |
| **Privileges Required** | PR | None (N) / Low (L) / High (H) | Level of auth needed before attack |
| **User Interaction** | UI | None (N) / Required (R) | Can attack execute autonomously |
| **Scope** | S | Unchanged (U) / Changed (C) | Can impact components beyond target |
| **Confidentiality** | C | None (N) / Low (L) / High (H) | Level of data leak |
| **Integrity** | I | None (N) / Low (L) / High (H) | Level of data alteration |
| **Availability** | A | None (N) / Low (L) / High (H) | Level of service disruption |

### Example Vector String (Critical RCE)
`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H` (Score: 10.0 Critical)
