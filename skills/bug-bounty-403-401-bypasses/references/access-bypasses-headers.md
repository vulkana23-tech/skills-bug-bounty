# Access Bypasses & Headers Reference Guide

## 1. Remediación Segura

- Normalice completamente las URLs (resolución de `..`, secuencias de escape `%xx` y barras diagonales) antes de comparar contra listas de acceso.
- No confíe en encabezados HTTP cliente (`X-Forwarded-For`, `X-Original-URL`) para la toma de decisiones de seguridad o control de acceso.
