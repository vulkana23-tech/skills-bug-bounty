# Case Study: Shopify GraphQL BFLA & IDOR Mutation Flaw

- **Target:** Shopify Admin GraphQL API
- **Severity:** High / Critical (Unauthorized Data Access)
- **Bounty Awarded:** $15,000
- **Vulnerability Category:** Broken Function Level Authorization (BFLA) + IDOR in GraphQL Mutation

---

## 🔍 Vulnerability Details

The GraphQL API Endpoint (`/admin/api/2025-01/graphql.json`) enforced object-level permissions on standard queries (`query { shop { id } }`), but omitted authorization checks on specific mutation fields.

## 🛠️ Step-by-Step Chain Execution

1. Attacker authenticated as a low-privileged merchant account.
2. Executed a GraphQL mutation changing store settings on an arbitrary store ID:

```graphql
mutation {
  storeSettingsUpdate(input: {
    storeId: "gid://shopify/Shop/999999",
    staffCanManagePayments: true
  }) {
    userErrors { field message }
    store { id name }
  }
}
```

3. The server validated that the user was authenticated, but failed to check if the user owned `Shop/999999`.

---

## 🛡️ Remediation Pattern

- Implement centralized GraphQL middleware for authorization checks at the field/resolver level before executing mutation resolvers.
