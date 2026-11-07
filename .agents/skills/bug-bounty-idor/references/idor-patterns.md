# IDOR & BOLA Reference Patterns

## 1. Escenarios Clave de Vulnerabilidad IDOR en Bug Bounty

### Cambio de Contraseña / Password Reset IDOR
- Enviar solicitud de cambio de contraseña capturando la petición HTTP:
  ```json
  POST /api/v1/reset-password
  {
    "email": "victim@example.com",
    "account_id": "1002"
  }
  ```
  Si el sistema restablece la contraseña del `account_id` especificado ignorando si el token pertenece a esa cuenta, se logra un Account Takeover completo.

### IDOR en Exportación de Informes (PDF/CSV)
- Solicitudes asíncronas para generar archivos:
  `GET /export/report?job_id=8842` -> Cambiar `job_id` a IDs de trabajos generados por otros usuarios para descargar datos sensibles de competidores o administradores.

### BOLA en GraphQL
- Mutación susceptible:
  ```graphql
  mutation {
    updateUserProfile(userId: "991", email: "attacker@evt.com") {
      success
    }
  }
  ```
  Verificar si GraphQL confía ciegamente en el argumento `userId` sin validar la identidad extraída del encabezado `Authorization: Bearer <jwt>`.
