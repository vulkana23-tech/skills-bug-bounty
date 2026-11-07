# OWASP API Security Remediation Reference

## 1. Riesgos Principales en APIs

Las vulnerabilidades en APIs suelen derivarse de la suposición equivocada de que los clientes de API (aplicaciones móviles o web SPAs) son entornos confiables que filtrarán los datos no deseados.

## 2. Remediación Segura

- Implemente controles de autorización explícitos a nivel de método y objeto en la capa de controlador del servidor API.
- Aplique DTOs (Data Transfer Objects) estrictos para limitar las propiedades que los clientes pueden modificar en solicitudes mutativas.
- Establezca límites globales y específicos de velocidad de consumo de recursos por usuario y cliente API.
