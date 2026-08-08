# GraphQL Attack Vectors & HackerOne Reports

## Top Disclosed GraphQL Reports (HackerOne Index)

- **Shopify GraphQL IDOR in Private Apps ($20,000 Bounty)**: Falta de control de autorización en mutaciones GraphQL permitiendo modificar registros de otros comercios.
- **GitLab GraphQL Introspección & Information Disclosure ($5,000 Bounty)**: Exposición de campos de administración y tokens mediante esquemas no filtrados.
- **Twitter GraphQL Batching Denial of Service ($3,000 Bounty)**: Agotamiento de recursos del servidor mediante consultas anidadas masivas.

## Checklist de Pruebas GraphQL
1. Probar Introspección (`__schema`).
2. Probar CSRF si la petición GraphQL se puede enviar como `GET` o con `Content-Type: application/x-www-form-urlencoded`.
3. Probar BOLA/IDOR pasando IDs de otros usuarios en mutaciones (`mutation { updateAccount(id: "102") }`).
