# Non-Web Protocol Security Reference

## 1. Riesgos en Servicios de Red

La desconfiguración en servidores de correo (SMTP Open Relay) permite el envío de spam o phishing bajo la reputación del dominio, mientras que transferencias de zona DNS exponen la topología completa de la red interna.

## 2. Remediación Segura

- Deshabilite transferencias AXFR no autorizadas en servidores DNS autoritativos.
- Restrinja el relay SMTP únicamente a clientes autenticados.
