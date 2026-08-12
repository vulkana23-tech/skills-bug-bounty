# 📱 Technical Reference: Android APK Reverse Engineering Guide

## 🔧 Essential Tooling Check
- **JADX**: `jadx -d ./output target.apk`
- **APKTool**: `apktool d target.apk -o ./apktool_out`
- **Frida Server**: `adb push frida-server /data/local/tmp/ && adb shell chmod 755 /data/local/tmp/frida-server`

## 🛡️ SSL Pinning Bypass (Frida Snippet)
```javascript
Java.perform(function () {
    var Array = Java.use("java.lang.reflect.Array");
    var SSLContext = Java.use("javax.net.ssl.SSLContext");
    console.log("[+] Intercepting SSLContext init for Universal SSL Pinning Bypass...");
    // Override TrustManager implementation
});
```

## 🔍 Native Library Analysis (`.so` files)
- Extract native libraries from `lib/arm64-v8a/` or `lib/x86_64/`.
- Open shared libraries in **Ghidra** or **Radare2** to inspect exported C/C++ symbols (`Java_com_example_...`).
