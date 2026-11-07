# Intelligent Response Diffing Reference Guide

## 1. Filtrado Personalizado en Python

```python
def handleResponse(req, interested):
    if req.status != 404 and len(req.response) != 1240:
        table.add(req)
```

## 2. Beneficios en Fuzzing Masivo

- Evita llenar las tablas de resultados con falsos positivos generados por respuestas 200 dinámicas con marcas de tiempo o tokens aleatorios.
