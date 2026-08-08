# Systematic Bug Hunting Workflow Reference

## 1. Hábitos de Auditoría Eficientes

- **Toma de Notas Rigurosa**: Registre cada parámetro descubierto, endpoint y comportamiento inusual en herramientas de notas como CherryTree, Obsidian o Notion.
- **Análisis de Peticiones HTTP**: Revise minuciosamente el historial de Burp Suite/ZAP para comprender cómo la aplicación estructurar las solicitudes JSON/XML y los encabezados personalizados.
- **Pruebas de Regresión**: Cuando la aplicación lance una nueva actualización o interfaz, vuelva a probar los endpoints heredados (legacy) que continúen respondiendo en la API.

## 2. Recomendaciones de Enfoque

- No salte inmediatamente a herramientas de escaneo masivo automatizado sin entender primero la lógica de negocio de la aplicación objetivo.
- Dedique tiempo a entender el flujo de trabajo previsto de los usuarios antes de intentar forzar comportamientos anómalos.
