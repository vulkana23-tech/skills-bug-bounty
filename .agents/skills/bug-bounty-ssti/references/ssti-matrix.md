# SSTI Identification & Remediation Reference Matrix

## 1. Motores de Plantillas Comunes y Conceptos de Diagnóstico

### Jinja2 (Python)
- Sintaxis de interpolación: `{{ ... }}`
- Diagnóstico: `{{ 7 * 7 }}` -> `49`
- Remediación: Usar variables de contexto `render_template('template.html', var=user_input)` en lugar de f-strings o concatenación.

### Twig (PHP)
- Sintaxis: `{{ ... }}`
- Diagnóstico: `{{ 7 * 7 }}` -> `49`
- Remediación: Mantener el entorno de Twig en modo estricto y evitar compilar strings dinámicos suministrados por el usuario.

### Freemarker (Java)
- Sintaxis: `${...}`
- Diagnóstico: `${7*7}` -> `49`
- Remediación: Configurar `api_builtins_unlisted=false` y restringir el acceso a clases de reflejo mediante `NewBuiltinClassResolver.ALLOWS_NOTHING_RESOLVER`.

---

## 2. Recomendaciones Generales de Seguridad

1. Separe estrictamente el diseño de la plantilla del procesamiento de datos del usuario.
2. Emplee un motor de plantilla que ejecute en un sandbox aislado sin acceso a llamadas del sistema o librerías del sistema operativo.
