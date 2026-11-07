# Nuclei Template Authoring Reference Guide

## 1. Componentes Clave de Matchers & Extractors

- **Matchers**: Condición para verificar vulnerabilidad (`word`, `regex`, `status`, `binary`, `dsl`).
- **Extractors**: Extracción de datos dinámicos (tokens, versiones) utilizando expresiones regulares o selectores CSS/KVC.

## 2. Recomendaciones de Seguridad

- Pruebe las plantillas personalizadas en entornos controlados para evitar bucles infinitos de redirección o cargas de tráfico innecesarias.
- Asigne niveles de severidad (`info`, `low`, `medium`, `high`, `critical`) de manera objetiva conforme a los estándares CVSS.
