# templates — modelos de documento

Modelos reutilizáveis para os artefatos do fluxo `SPEC → ADR → PLAN → TASK → IMPLEMENTAÇÃO → TESTES → EVIDÊNCIAS`.

| Artefato | Modelo | Destino típico |
|---|---|---|
| SPEC | `specifications/SPEC-TEMPLATE.md` | `docs/specifications/SPEC-NNN-*.md` |
| ADR | `architecture-decisions/ADR-TEMPLATE.md` | `docs/adr/ADR-NNNN-*.md` |
| PLAN | `implementation-plans/PLAN-TEMPLATE.md` | `docs/plans/PLAN-NNN-*.md` |
| TASK | `tasks/README.md` → `tasks/TASK-TEMPLATE.md` | `tasks/backlog/TASK-<AREA>-NNN-*.md` |
| Test plan | `test-plans/TEST-PLAN-TEMPLATE.md` | `docs/testing/TEST-PLAN-*.md` |
| Security review | `security-reviews/SECURITY-REVIEW-TEMPLATE.md` | `docs/security/REVIEW-*.md` |

## Regras

1. Modelo não é documento aprovado; preencher e versionar no destino.
2. Placeholders entre `<...>` devem ser substituídos.
3. Nenhum modelo contém dados reais, segredos ou PII.
4. Critérios de aceite devem ser verificáveis.
5. A fonte canônica de TASK permanece `tasks/TASK-TEMPLATE.md`.
