# tasks/backlog

TASKs prontas para execução, ordenadas por dependência.

## Estado atual

Nenhuma TASK de código pode ser iniciada antes da aprovação das Fases 2–3
(ver `docs/plans/open-questions.md`).

As TASKs planejadas de implementação estão descritas em `docs/tasks/backlog.md`
(T-001..T-013) e serão convertidas para o formato de `tasks/TASK-TEMPLATE.md`
após a aprovação do PLAN.

## Formato

`TASK-<AREA>-NNN-<slug>.md` com frontmatter:

```yaml
id: TASK-<AREA>-NNN
title: <título verificável>
status: pending
spec: SPEC-NNN
adr: [ADR-NNNN]
plan: PLAN-NNN
owner: <papel>
depends_on: [TASK-<AREA>-NNN]
gate: G4
```
