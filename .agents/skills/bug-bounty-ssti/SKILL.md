---
name: bug-bounty-ssti
description: Detección, diagnóstico y mitigación de vulnerabilidades Server-Side Template Injection (SSTI) en motores de plantillas como Jinja2, Twig, Smarty, Freemarker, Velocity, ERB y Pug.
---

# Skill: Server-Side Template Injection (SSTI) Assessment

Esta habilidad capacita al agente para auditar aplicaciones web que concatenan datos de usuario directamente dentro de plantillas del lado del servidor sin una sanitización adecuada.

## 📌 Identificación del Motor de Plantillas

Para determinar qué motor de plantillas está en uso, se envían expresiones de evaluación matemática sencillas y se analiza la respuesta:

```
                  ${7*7}
                 /      \
             49 /        \ ${7*'7'}
               /          \
          [Twig /        [49: Twig]
         Smarty]         [7777777: Jinja2 / Python]
```

### Expresiones de Diagnóstico por Motor
- **Jinja2 / Twig**: `{{7*7}}` -> `49`
- **Smarty / Freemarker**: `${7*7}` -> `49`
- **ERB (Ruby)**: `<%= 7*7 %>` -> `49`
- **Angular / Vue (Client-Side)**: `{{7*7}}` -> `49`

---

## 🛠️ Mitigación y Remediación

- Nunca concatenar entradas del usuario directamente en la cadena de la plantilla.
- Utilizar plantillas estáticas pasando las variables a través del contexto oficial del motor (`render_template('index.html', user_input=input)`).
- Habilitar modos de ejecución restringidos (Sandboxing) si el motor lo soporta.

---

## 📚 Referencias Técnicas (`PayloadsAllTheThings`)

Consulta el deslose completo de motores y detección en:
[ssti-matrix.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-ssti/references/ssti-matrix.md)
