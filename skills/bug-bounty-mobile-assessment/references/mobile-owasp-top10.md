# OWASP Mobile Security & Remediation Reference

## 1. Riesgos Comunes en Aplicaciones Móviles

1. **Almacenamiento Inseguro**: Guardar credenciales o claves privadas en texto plano en la memoria flash del dispositivo.
2. **Insecure Code Execution**: Exportación indebida de `Android Components` (`Activities`, `Services`, `Broadcast Receivers`) permitiendo ejecución remota de acciones desde otras apps maliciosas.

## 2. Remediación Segura

- Utilice mecanismos de almacenamiento seguro cifrado por hardware (Android Keystore System / iOS Keychain).
- Implemente SSL/TLS Certificate Pinning para validar las conexiones con las APIs backend.
- Establezca `android:exported="false"` en todos los componentes manifest que no requieran ser invocados por aplicaciones externas.
