---
name: bug-bounty-turbo-intruder-python-scripting
description: Orquestación de ataques de fuzzing de alto rendimiento con scripts Python en Turbo Intruder. Definición de queueRequests, handleResponse y uso de decoradores de filtrado.
---

# Skill: Turbo Intruder Python Scripting & Attack Orchestration

Esta habilidad capacita al agente para escribir y personalizar scripts de control en Python para la extensión Turbo Intruder de Burp Suite, permitiendo automatizar ataques complejos, fuzzing masivo y generación dinámica de peticiones.

## 📌 Estructura Básica de un Script en Turbo Intruder

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    for word in open('/usr/share/seclists/Discovery/Web-Content/common.txt'):
        engine.queue(target.req, word.rstrip())

def handleResponse(req, interested):
    if interested:
        table.add(req)
```

---

## 📚 Referencias Técnicas

Consulta las plantillas de código en:
[turbo-scripting-templates.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-turbo-intruder-python-scripting/references/turbo-scripting-templates.md)
