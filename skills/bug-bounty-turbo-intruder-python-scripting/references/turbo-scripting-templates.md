# Turbo Intruder Python Scripting Reference Templates

## 1. Uso de Decoradores de Filtrado

- `@MatchStatus(200, 302)`: Procesa únicamente peticiones que devuelvan código de estado 200 o 302.
- `@FilterStatus(404)`: Descarta automáticamente respuestas de error 404.

## 2. Remediación Segura

- Limite el uso de hilos concurrentes para evitar saturar involuntariamente el servidor objetivo o provocar denegaciones de servicio.
