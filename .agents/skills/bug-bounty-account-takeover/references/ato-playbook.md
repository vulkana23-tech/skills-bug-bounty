# Account Takeover (ATO) Playbook & HackerOne Index

## Top Disclosed ATO Reports (HackerOne Index)

- **Uber Account Takeover via Passwordless Signup ($10,000 Bounty)**: *mongo* - Cambio de contraseña de cualquier usuario de Uber modificando parámetros en la API `/rt/users/passwordless-signup`.
- **Twitter Pre-Account Takeover via OAuth ($5,000 Bounty)**: Registro previo con correo de la víctima que permitía acceder inmediatamente cuando la víctima iniciaba sesión con Google SSO.
- **Shopify Account Takeover via Password Reset Token Leak ($7,500 Bounty)**: Fuga del token de recuperación en el encabezado Referer HTTP enviado a servicios externos.

## Matriz de Impacto ATO
- Severidad típica: **Critical (9.0 - 9.8 CVSSv3.1)**
- Requiere PoC claro que demuestre el control total sobre la cuenta de la víctima sin requerir interacción compleja por su parte.
