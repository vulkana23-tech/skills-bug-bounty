# ⚙️ Technical Reference: Binary Analysis & CTF Triaging Guide

## 🛠️ Quick Commands Cheat Sheet
- **Checksec**: `checksec --file=target_bin`
- **Radare2 Triage**:
  ```bash
  r2 -A target_bin
  [0x00000000]> afl        # List functions
  [0x00000000]> s main     # Seek to main
  [0x00000000]> pdf        # Disassemble function
  ```
- **GDB Peda / GEF**: `gdb target_bin` -> `checksec`, `pattern create 100`.
