---
name: opencheck-intelligence
description: Investigar la estructura corporativa, beneficiarios finales (UBO), subsidiarias, paraísos fiscales y riesgos AML/KYC de cualquier empresa u organización usando OpenCheck MCP.
metadata:
  version: "1.0.0"
  author: "OpenCheck / CyberVault"
  tags:
    - osint
    - due-diligence
    - corporate-intelligence
    - ubo
    - lei
    - bods
    - aml
---

# OpenCheck: Inteligencia Corporativa y Due Diligence de Propiedad

Utiliza las herramientas MCP de `opencheck` para mapear quién posee y controla realmente una entidad legal, descubriendo empresas fantasma, filiales opacas, personas políticamente expuestas (PEPs) y subsidiarias no declaradas.

## Flujo de Trabajo Metodológico

1. **Búsqueda e Identificación (Find):**
   - Usa `opencheck_search` con el nombre de la empresa para obtener candidatos, jurisdicción y su LEI (Legal Entity Identifier).
   - Si tienes un número de registro nacional (e.g., Reino Unido Companies House, España CIF, Delaware), usa `opencheck_resolve_national_id`.
   - Si la empresa no tiene LEI, usa `opencheck_register_lookup` con el esquema de registro (`GB-COH`, etc.).

2. **Alcance y Jurisdicción (Knowability):**
   - Invoca `opencheck_knowability(jurisdictions)` para verificar qué transparencia ofrece el país objetivo (p. ej., si publica propietarios reales o solo directores).

3. **Radiografía de Propiedad y Riesgo (Check):**
   - Ejecuta `opencheck_lookup(lei)` para extraer la identidad, beneficiarios reales (UBO) y señales de riesgo estructural.
   - Usa `opencheck_owners(lei)` para ver quién tiene más del 25% o porcentajes de control.
   - Ejecuta `opencheck_subsidiaries(lei)` para obtener la lista de subsidiarias y filiales consolidadas a nivel mundial.
   - Ejecuta `opencheck_ownership_map(lei)` para obtener el grafo y estructura tabular de la cadena de control.
   - Ejecuta `opencheck_person_check` para verificar directores o accionistas contra listas de sanciones y PEPs.

