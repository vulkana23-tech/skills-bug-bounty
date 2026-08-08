# Target Selection & Scope Evaluation Reference

## 1. Reglas de Compromiso (Rules of Engagement)

- Lea minuciosamente la política del programa antes de enviar cualquier paquete HTTP.
- Respete estrictamente los elementos fuera de alcance (Out-Of-Scope), como pruebas de denegación de servicio (DoS/DDoS), spam o ingeniería social hacia empleados.
- Utilice identificadores de cabecera personalizados si el programa lo requiere (ej. `User-Agent: BugBounty-Research-User`).

## 2. Matriz de Priorización de Objetivos

| Tipo de Objetivo | Competencia | Complejidad | Potencial de Hallazgos |
| :--- | :--- | :--- | :--- |
| **Wildcard Scope (`*.company.com`)** | Baja - Media | Variable | Alto (Subdominios olvidados, staging) |
| **Aplicación Core Principal** | Alta | Alta | Medio - Alto (Lógica compleja, IDORs) |
| **APIs móviles (REST/GraphQL)** | Media | Media | Alto (Parámetros no documentados) |
| **Aplicaciones Adquiridas** | Baja | Baja - Media | Muy Alto (Integración reciente) |
