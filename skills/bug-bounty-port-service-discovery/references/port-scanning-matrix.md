# Port Scanning & Service Discovery Reference Matrix

## 1. Escaneo Rápido con Naabu

```bash
naabu -list subdomains.txt -top-ports 1000 -silent -o open_ports.txt
```

## 2. Remediación Segura

- Restrinja el acceso a puertos de bases de datos y administración únicamente a direcciones IP autorizadas mediante reglas de Firewall o Security Groups.
- Deshabilite servicios no utilizados en servidores de producción.
