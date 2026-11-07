---
name: bug-bounty-reverse-engineering
description: Metodología de Ingeniería Inversa y análisis estático de binarios ejecutable. Inspección de símbolos, descompilación (Ghidra, Radare2) y análisis de firmeza en ejecutables.
---

# Skill: Reverse Engineering & Binary Assessment

Esta habilidad capacita al agente para realizar análisis estáticos e inspección de código descompilado en binarios (`ELF`, `PE`, `Mach-O`, `.NET`), evaluando la presencia de protecciones de compilador y secretos incrustados.

## 📌 Conceptos de Auditoría de Binarios

### 1. Protecciones de Compilador
- **ASLR (Address Space Layout Randomization)**: Randomización de las direcciones de memoria.
- **DEP / NX (Data Execution Prevention / No-Execute)**: Prevención de ejecución en la pila (Stack) o Heap.
- **Stack Canaries**: Valores de verificación para prevenir desbordamientos de búfer (Buffer Overflow).

---

## 📚 Referencias Técnicas

Consulta los detalles y remediación en:
[reversing-cheatsheet.md](file:///C:/Users/logir/.gemini/antigravity-ide/scratch/bug-bounty-skills/skills/bug-bounty-reverse-engineering/references/reversing-cheatsheet.md)
