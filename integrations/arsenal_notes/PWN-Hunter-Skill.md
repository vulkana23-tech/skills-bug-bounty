---
title: "PWN HUNTER Skill"
tool_name: "pwn-hunter"
github_repo: "https://github.com/BountyForge-xyz/pwn-skill"
category: "Seguridad-Ofensiva-Defensiva"
language: "Python (pwntools) / Markdown"
tags:
  - "herramienta"
  - "skill"
  - "pwn"
  - "binary-exploitation"
  - "rop"
  - "heap"
  - "kernel"
status: "Operativo"
---

# 🎯 PWN HUNTER — Skill de Explotación Binaria para Agentes de IA

> [!NOTE] **Propósito Táctico**: Skill de especialización técnica que capacita a agentes de IA (en Antigravity, OpenCode, DSH, WorkBuddy o Claude Code) para realizar ingeniería inversa, triaje de binarios y desarrollo de exploits de memoria fiables (*PoC*) sin divagaciones.
> **Autor / Organización**: `BountyForge-xyz` | **Repositorio**: [BountyForge-xyz/pwn-skill](https://github.com/BountyForge-xyz/pwn-skill)

---

## ⚡ Metodología: La Escalera de Primitivas (*Primitive Ladder*)
PWN HUNTER fuerza al agente a seguir el ciclo metódico de explotación de bajo nivel:
```
[ 1. Crash ] ──▶ [ 2. Control de RIP ] ──▶ [ 3. Memory Leak (ASLR) ] ──▶ [ 4. Arbitrary Write ] ──▶ [ 5. Exec / Shell ]
```

### Áreas Técnicas Cubiertas:
1. **Stack Exploitation**:
   - `checksec` automático (NX, Canaries, PIE, RELRO).
   - `ret2libc`, `ret2csu`, `SROP` (Sigreturn-Oriented Programming), `ret2dlresolve` y alineación de stack (`MOVAPS`).
2. **Format String Vulnerabilities**:
   - Descubrimiento exacto de offsets mediante patrones.
   - Construcción de payloads con `fmtstr_payload` para sobreescritura de GOT.
3. **Heap Exploitation**:
   - Ataques sobre `tcache` (tcache poisoning, safe-linking bypass).
   - Use-After-Free (UAF), off-by-one, *House of Force/Spirit*, y FSOP (*File Stream Oriented Programming*).
4. **Filtros Seccomp & Kernel**:
   - Detección de restricciones con `seccomp-tools`.
   - Shellcode ORW (`openat` / `read` / `write`) y `sendfile` para eludir bloqueos de `execve`.
   - Bypasses de kernel: `modprobe_path`, `commit_creds`, `KASLR` y trampolines `KPTI`.

---

## 🛡️ Refusal Engineering Integrado
Incluye directivas de encuadre de contexto ético que evitan que modelos como Claude o GPT se nieguen a generar cadenas ROP o shellcodes en escenarios legítimos de laboratorios, CTFs y auditorías autorizadas.

---

## 🔌 Instalación y Despliegue en tus Agentes
- **Nombre de activación**: `pwn-hunter`
- **Frases de activación**: *"pwn", "exploit this binary", "buffer overflow", "ROP chain", "ret2libc", "heap exploit", "UAF", "format string"*.
- **Desplegado en**:
  - `.agents/skills/pwn-hunter/SKILL.md` (Antigravity)
  - `~/.config/opencode/skills/pwn-hunter/` (OpenCode)
  - `~/.dsh/skills/pwn-hunter/` (DeepSeek Harness)
  - `~/.workbuddy-ai/skills/pwn-hunter/` (WorkBuddy AI)

---
*Ficha táctica catalogada para la base de conocimiento y orquestación de agentes de Cyber-Vault.*