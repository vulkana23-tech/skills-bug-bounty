# HTTP/2 Downgrade Remediation Reference

## 1. Remediación Segura

- Utilice comunicación HTTP/2 nativa de extremo a extremo (End-to-End HTTP/2) entre el proxy inverso y los servidores backend.
- Sanitice rigurosamente todos los encabezados HTTP/2 rechazando cualquier carácter `\r` o `\n` antes de realizar la conversión a HTTP/1.1.
