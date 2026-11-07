---
name: bug-bounty-port-service-discovery
description: Descubrimiento eficiente de puertos y servicios no-web. Uso de naabu, masscan y nmap para detectar interfaces de administración, bases de datos y paneles de gestión expuestos.
---

# Skill: Port & Service Discovery Assessment

Esta habilidad capacita al agente para realizar escaneos de puertos rápidos sobre rangos de direcciones IP o listas de subdominios, identificando servicios no HTTP/HTTPS o puertos web alternativos (ej. 8080, 8443, 9000, 9443).

## 📌 Puertos Críticos a Monitorear

- **Servicios de Gestión Web**: 8080, 8443, 9000, 9443, 10000 (Webmin/Jenkins/Kibana).
- **Bases de Datos Expuestas**: 3306 (MySQL), 5432 (PostgreSQL), 27017 (MongoDB), 6379 (Redis), 9200 (Elasticsearch).
- **Acceso Remoto**: 22 (SSH), 3389 (RDP), 5900 (VNC).

---

## 📚 Referencias Técnicas

Consulta la matriz de escaneo en:
[port-scanning-matrix.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-port-service-discovery/references/port-scanning-matrix.md)
