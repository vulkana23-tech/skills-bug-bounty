# Login Anomaly Detection Reference Guide

## 1. Remediación Segura

- Implemente CAPTCHAs invisibles o reCAPTCHA v3 tras los primeros intentos fallidos.
- Utilice limitadores de velocidad distribuidos con almacenes de memoria compartida (Redis) para registrar intentos a nivel global de red.
