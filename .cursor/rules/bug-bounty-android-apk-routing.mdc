---
name: bug-bounty-android-apk-routing
description: Metodología de enrutamiento y análisis para ingeniería inversa de aplicaciones Android (APK/AAB). Descompilación con JADX, Frida, bypass de SSL Pinning y análisis de bibliotecas nativas .so.
---

# Skill: Android APK Reverse Engineering Router

Esta habilidad proporciona una metodología estructurada para la descompilación, análisis estático y dinámico de aplicaciones móviles Android.

## 📌 Flujo de Auditoría APK

### 1. Descompilación y Análisis Estático
- **JADX / JADX-GUI**: Descompilación de Bytecode Dalvik (`.dex`) a código fuente Java/Kotlin.
- **APKTool**: Extracción de `AndroidManifest.xml`, recursos (`res/`) y archivos Smali (`apktool d target.apk`).
- **Secret Scanning**: Búsqueda de claves API, URLs de staging y tokens en `strings.xml`, `buildconfig` y fuentes descompiladas.

### 2. Inspección de Componentes Android
- **Exported Components**: Verificación de `Activity`, `Service`, `BroadcastReceiver` y `ContentProvider` con `android:exported="true"`.
- **Deep Links & Intent Filters**: Auditoría de esquemas personalizados (`myapp://`) para detección de Open Redirect o ejecución de código.

### 3. Análisis Dinámico y Bypass de Protecciones
- **Frida Hooking**: Búsqueda e intercepción de funciones de verificación de SSL Pinning y Root Detection.
- **Objection**: Intercepción rápida sin scripts personalizados (`objection --g com.target.app explore`).

---

## 📚 Referencias Técnicas

Consulta la guía detallada de descompilación e instrumentos en:
[apk-reversing-guide.md](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-android-apk-routing/references/apk-reversing-guide.md)
