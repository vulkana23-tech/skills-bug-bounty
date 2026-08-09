# Socket Poisoning Remediation Reference

## 1. Remediación Segura

- Separe la gestión de sockets TCP por usuario autenticado.
- Asegúrese de que el servidor proxy web limpie cualquier fragmento no procesado de la conexión TCP antes de asignarla a una nueva petición.
