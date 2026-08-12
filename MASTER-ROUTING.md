# 🧭 Master Methodology & Skill Routing Guide

This master decision matrix guides AI coding agents in identifying target artifacts, enforcing operational boundaries, and executing structured security audit methodologies.

---

## 🎯 Target Classification & Routing Ladder

When presented with a file, repository, or target environment, follow this primary routing ladder:

| Target Type / Input Pattern | Primary Skill Module | Primary Tools | Execution Goal |
|---|---|---|---|
| Android App (`.apk`, `.xapk`, `.apks`, `.aab`) | [`bug-bounty-android-apk-routing`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-android-apk-routing/SKILL.md) | JADX, Frida, APKTool, Objection | Static manifest audit, SSL Pinning bypass, Native `.so` analysis, Secret extraction |
| Obfuscated JS / Web Bundle (`.js`, `.min.js`, webpack) | [`bug-bounty-js-reverse-deobfuscation`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-js-reverse-deobfuscation/SKILL.md) | AST (Babel), Webpack Unpacker, DevTools | Code deobfuscation, API signature extraction, Anti-debugging bypass |
| Compiled Binary (`ELF`, `PE`, `Mach-O`, `.wasm`) | [`bug-bounty-binary-ctf-routing`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-binary-ctf-routing/SKILL.md) | Ghidra, Radare2, GDB, Checksec | Compiler mitigation check, Decompilation audit, Memory safety analysis |
| Firmware Image (`.bin`, `.img`, `.squashfs`) | [`bug-bounty-firmware-iot-routing`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-firmware-iot-routing/SKILL.md) | Binwalk, Unsquashfs, Strings, Firmware-mod-kit | Filesystem extraction, Embedded web server audit, Credential recovery |
| Scope & Authorization Boundary | [`bug-bounty-agent-obedience-scope`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-agent-obedience-scope/SKILL.md) | `scope.md`, `tools-index.json` | Verify target authorization, safe PoC validation, non-destructive audit compliance |

---

## ⚙️ Standard 5-Phase Audit Workflow

1. **Phase 1: Authorization & Scope Audit**
   - Verify scope rules in [`scope.md`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/scope.md).
   - Execute [`scripts/refresh_tool_index.py`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/scripts/refresh_tool_index.py) to check local tool availability.

2. **Phase 2: Static Triaging**
   - Extract embedded secrets, strings, and configuration manifests.
   - Map attack surfaces and input endpoints.

3. **Phase 3: Interactive / Deobfuscation Analysis**
   - Deobfuscate scripts or decompile binaries into readable source code representation.
   - Analyze logic controls, cryptography implementations, and custom encoding protocols.

4. **Phase 4: Benign Conceptual Validation (PoC)**
   - Construct minimal non-destructive Proof-of-Concept proofs strictly within scope boundaries.

5. **Phase 5: Remediation Reporting**
   - Format defensive report using [`bug-bounty-reporting`](file:///c:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-reporting/SKILL.md).
