# JS Endpoint Extraction Reference Rules

## 1. Expresiones Regulares para Rutas de API

- **API Routes**: `["']/(api|v1|v2|v3|graphql|auth)/[a-zA-Z0-9_\-/]+["']`

## 2. Remediación Segura

- Despliegue gateways de API que validen la autorización a nivel de endpoint independientemente de si la ruta figuraba o no en la interfaz gráfica del cliente.
