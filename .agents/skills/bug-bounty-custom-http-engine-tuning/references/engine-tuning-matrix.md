# Engine Tuning Reference Matrix

## 1. Configuraciones Recomendadas por Tipo de Objetivo

- **Objetivos de Alta Velocidad (CDN/Nginx)**: `concurrentConnections=10`, `requestsPerConnection=100`, `pipeline=True`.
- **Objetivos Frágiles / Legacy**: `concurrentConnections=2`, `requestsPerConnection=10`.
