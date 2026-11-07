# Bug Bounty Vulnerability Report Templates

## Plantilla Estándar (HackerOne / Bugcrowd Compatible)

```markdown
# [Vulnerability Type] in [Component/Endpoint] Leads to [Impact]

## Summary
Se ha identificado una vulnerabilidad de tipo **[Nombre de la Vulnerabilidad]** en la ruta `[Endpoint]` de la aplicación `[Dominio/App]`. Esta falla permite a un atacante [Explicar brevemente la consecuencia técnica].

- **Vulnerabilidad**: [ej. Server-Side Request Forgery / Stored XSS / IDOR]
- **Ubicación Aféctada**: `https://example.com/api/v1/resource`
- **CVSS v3.1 Score**: `[Ej. 8.6 High] - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N`

---

## Steps To Reproduce

1. Iniciar sesión con una cuenta de prueba en `https://example.com/login`.
2. Navegar a la sección `[Nombre de la sección]`.
3. Interceptar la solicitud HTTP POST hacia `/api/v1/resource` utilizando Burp Suite.
4. Modificar el parámetro `[Nombre del Parámetro]` reemplazando su valor original por el siguiente payload:
   ```
   [Insertar Payload Aquí]
   ```
5. Enviar la solicitud modificada y observar la respuesta del servidor HTTP `200 OK`.
6. Comprobar que [describir el resultado observable, ej. se ejecuta la función javascript o se descarga el archivo sensible].

---

## Proof of Concept (PoC)

### Request HTTP Raw
```http
POST /api/v1/resource HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Authorization: Bearer <TOKEN>
Content-Type: application/json

{
  "target": "http://169.254.169.254/latest/meta-data/"
}
```

### Response HTTP Raw
```http
HTTP/1.1 200 OK
Content-Type: text/plain

ami-id
instance-id
iam/
```

---

## Impact

Un atacante remoto sin autenticación previa puede explotar esta vulnerabilidad para [Describir impacto exacto en confidencialidad, integridad o disponibilidad]. Esto compromete la infraestructura de la empresa al permitir [ej. lectura de datos sensibles de otros clientes, pivotaje interno en la red cloud].

---

## Remediation Suggestion

Se recomienda [Describir remediación técnica, ej. implementar sanitización estricta mediante listas blancas, usar consultas parametrizadas PreparedStatements, o agregar validación de autorización a nivel de objeto].
```
