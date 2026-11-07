# Cloud Security & Hardening Reference

## 1. Riesgos de Infraestructura Nube

La exposición accidental de buckets de almacenamiento o claves de servicio IAM permite a un atacante acceder a copias de seguridad de bases de datos, código fuente o tomar control de instancias virtuales en la nube.

## 2. Remediación Segura

- Habilite el bloqueo de acceso público (`Block Public Access`) a nivel de cuenta global en AWS S3.
- Aplique el principio de mínimo privilegio en todas las políticas e identidades IAM.
- Implemente escáneres de seguridad continuos de infraestructura como código (IaC) en la canalización CI/CD.
