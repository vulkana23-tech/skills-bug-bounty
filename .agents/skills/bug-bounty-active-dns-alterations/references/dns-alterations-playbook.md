# Active DNS Alterations Reference Playbook

## 1. Reglas de Alteración Soportadas

- **Sustitución Numérica**: `api1.target.com` -> `api2.target.com`.
- **Adición de Guiones**: `apptest.target.com` -> `app-test.target.com`.

## 2. Remediación Segura

- Utilice limites de velocidad de resolución DNS (`-r`) para no saturar los servidores DNS autoritativos de la organización.
