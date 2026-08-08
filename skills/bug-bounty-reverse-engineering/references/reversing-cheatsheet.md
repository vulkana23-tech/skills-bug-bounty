# Binary Security & Hardening Reference

## 1. Riesgos en Binarios No Protegidos

Binarios compilados sin banderas de mitigación son vulnerables a ataques de desbordamiento de búfer (Buffer Overflow), sobrescritura de punteros de función y formateo inseguro de cadenas (`Format String`).

## 2. Remediación Segura

- Compile todos los binarios de producción habilitando protecciones del compilador:
  - GCC/Clang: `-fstack-protector-strong -D_FORTIFY_SOURCE=2 -Wl,-z,relro,-z,now -fPIE -pie`
- Elimine símbolos de depuración (`strip`) y evite incluir llaves criptográficas o contraseñas codificadas en duro en la sección `.rodata`.
