# 📟 Technical Reference: Firmware & IoT Extraction Guide

## 🛠️ Key Firmware Tools
- **Binwalk**: `binwalk -M -e target_firmware.bin`
- **Unsquashfs**: `unsquashfs -d ./squashfs-root image.squashfs`
- **Firmware-Mod-Kit**: Unpack, modify, and rebuild firmware images.

## 🔍 Hardcoded Credential Scan Command
```bash
grep -rnE "(password|passwd|secret|admin|root|key)" ./squashfs-root/etc/
```
