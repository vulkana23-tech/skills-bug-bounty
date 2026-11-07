---
name: bug-bounty-idor
description: Detección y explotación de Insecure Direct Object References (IDOR), Broken Object Level Authorization (BOLA) y Broken Function Level Authorization (BFLA) en APIs REST, GraphQL y aplicaciones web.
---

# Skill: IDOR & Authorization Flaw Testing

Esta habilidad instruye al agente sobre cómo auditar la lógica de autorización de endpoints para asegurar que los usuarios no puedan acceder, modificar o eliminar objetos de otros usuarios manipulando identificadores directos (IDs, UUIDs, hashes o nombres de usuario).

## 📌 Metodología de Pruebas de IDOR / BOLA

### 1. Enfoque de Doble Cuenta (User A vs User B)
- **Crear dos cuentas de prueba**: Cuentas con los mismos roles (User A y User B) y cuentas con roles jerárquicos distintos (User vs Admin).
- Capturar solicitudes HTTP realizadas por User A (ej. `GET /api/v1/user/10042/invoice`).
- Reemplazar la cookie de sesión/JWT de User A por la de User B y enviar la solicitud. Si se devuelve la factura del User A, existe un **IDOR Read**.
- Probar solicitudes mutativas: `PUT /api/v1/user/10042`, `DELETE /api/v1/user/10042`.

### 2. Dónde buscar IDORs
- **Parámetros de URL**: `GET /users?id=123`, `GET /documents/99`
- **Cuerpo de Solicitud (JSON/XML)**: `{"account_id": "9982", "role": "user"}`
- **Encabezados HTTP**: `X-User-Id: 554`, `X-Account-Number: 102`
- **Endpoints GraphQL**: Consultar objetos por `id` en queries o mutaciones sin verificar propiedad del token de la sesión.

---

## 🛠️ Variaciones y Bypass de Restricciones

1. **HTTP Parameter Pollution (HPP)**:
   - Probar `GET /api/user?id=USER_B_ID&id=USER_A_ID`
   - Probar arrays: `GET /api/user?id[]=USER_B_ID&id[]=USER_A_ID`
2. **Transformación de Métodos HTTP**:
   - Cambiar `GET` por `POST`, `PUT`, `PATCH` o `DELETE`.
3. **Conversión de Tipo de Datos**:
   - Pasar `id` como entero `123`, string `"123"`, array `[123]`, u objeto `{"id": 123}`.
4. **Predictibilidad de IDs y UUIDs**:
   - Probar secuencias numéricas adyacentes (`1001`, `1002`, `1003`).
   - Investigar si los UUIDv1 son derivados de la marca de tiempo (timestamp) o de la dirección MAC.

---

## 📚 Documentación de Patrones IDOR

Lee la guía de patrones y escenarios comunes:
[idor-patterns.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-idor/references/idor-patterns.md)
