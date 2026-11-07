---
tipo: herramienta
subtipo: auditoria-web
categoria: vulnerabilidades-web
herramienta: XSSRush (XSSR)
autor: N45HT
repositorio: https://github.com/N45HT/XSSRush
fecha_ingesta: 2026-11-07
tags:
  - xss
  - dom-xss
  - playwright
  - headless-browser
  - zero-false-positive
  - bug-bounty
  - canary-probing
---

# ⚡ XSSRush (XSSR): Escáner y Auditor Automatizado de XSS Multivector

Desarrollado por **N45HT**, **XSSR (XSSRush)** es una herramienta avanzada para la detección, mapeo y verificación de vulnerabilidades Cross-Site Scripting (Reflejado, DOM, POST, Path, Fragment y Header).

A diferencia de los escáneres estáticos tradicionales que analizan respuestas HTTP con expresiones regulares, XSSRush utiliza **automatización de navegador headless con Playwright** (Chromium, Firefox y WebKit) y se conecta directamente al bucle de eventos del navegador para interceptar la ejecución real de JavaScript (`alert`, `confirm`, `prompt`), eliminando por completo los falsos positivos.

---

## 🔬 Arquitectura y Pipeline de 7 Fases

```
[Fase 0: Minería] ──> [Fase 1: Canarios & Contexto] ──> [Fase 2: GET & DOM XSS]
                                                              │
[Fase 5: Fragmento] <── [Fase 4: Path XSS] <── [Fase 3: POST Form XSS]
       │
       └───> [Fase 6: Header XSS] ───> [Verificación DOM & PoC Base64]
```

### 1. Fase 0: Parameter Mining
* Extrae parámetros de cadenas de consulta (query strings) y atributos de formularios HTML.
* Inspecciona variables globales expuestas en el objeto `window` de JavaScript.
* Realiza fuzzing de parámetros ocultos utilizando diccionarios especializados (`wordlists/`).

### 2. Fase 1: Canary Probing & Special Character Reflection Matrix
* Inyecta un token canario único para rastrear los puntos de reflejo exactos.
* Clasifica el contexto sintáctico de inyección:
  * `html`: Dentro del cuerpo HTML general.
  * `attribute`: Dentro de valores de atributos (`value="..."`, `href="..."`).
  * `javascript`: Dentro de bloques `<script>` o manejadores de eventos.
  * `url`: Parámetros pasados a sinks de redirección o recursos externos.
* Evalúa la matriz de caracteres especiales para comprobar cuáles pasan sin escapar:
  ```text
  '  "  <  >  /  ;  (  )  {  }  =  `
  ```

### 3. Fase 2: Reflected GET & DOM XSS
* Genera payloads específicos ajustados al contexto detectado en la Fase 1.
* Inyecta a través de parámetros URL y monitorea la ejecución de diálogos nativos.

### 4. Fase 3: POST Form XSS
* Automatiza el envío de formularios mediante `requestSubmit()`.
* Genera un Proof-of-Concept (PoC) en HTML embebido en Base64 para reproducción inmediata con un solo clic.

### 5. Fase 4: Path-Based XSS
* Evalúa inyecciones en segmentos de ruta de URLs reescritas (ejemplo: `/profile/USUARIO`).

### 6. Fase 5: Fragment-Based XSS (SPAs & Client-Side Routers)
* Inyecta en el fragmento hash (`https://target.com/app#payload`) para auditar enrutadores del lado del cliente en frameworks como React, Vue y Angular.

### 7. Fase 6: Header-Based XSS
* Audita inyecciones en encabezados HTTP comunes (`User-Agent`, `Referer`, `Origin`, `Cookie`, `X-Forwarded-*`).

---

## 🛠️ Comandos Operativos y Modos de Uso

```bash
# 1. Escaneo básico de un solo objetivo (GET & POST)
python xssr.py -u "https://target.com/search?q=test"

# 2. Auditoría completa de todos los vectores (exportando JSON)
python xssr.py -u "https://target.com/app" --scan all -o scan_report.json

# 3. Modo visible para depuración interactiva (sin headless)
python xssr.py -u "https://target.com/app" --headless false -v

# 4. Ajuste de retardo para evasión de Rate-Limiting / WAF
python xssr.py -u "https://target.com" --scan all --delay-min 1500 --delay-max 3000

# 5. Escaneo masivo en pipeline Unix (STDIN)
cat urls_en_scope.txt | python xssr.py --scan get,dom -o hallazgos.json
```

---

## 🎯 Integración con la Metodología de Bug Bounty

* **7-Question Gate:** Cumple estrictamente la regla de verificación activa en el motor JS del navegador antes de redactar cualquier reporte.
* **Reducción de Ruido:** El sondeo previo con canarios evita disparar alertas de WAF con payloads ruidosos cuando los caracteres básicos (`< >`) están sanitizados.
* **Memoria Persistente:** Se enlaza con `bug-bounty-xss` y `bug-bounty-dom-xss-source-sink`.
