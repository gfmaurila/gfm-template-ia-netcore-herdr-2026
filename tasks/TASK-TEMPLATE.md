# TASK-TEMPLATE — formato único de tarefa

Toda TASK usa este formato. IDs seguem `TASK-<AREA>-NNN` (ex.: `TASK-API-001`).

```markdown
---
id: TASK-<AREA>-NNN
title: <título curto e verificável>
status: pending
spec: SPEC-NNN
adr: [ADR-NNNN]
plan: PLAN-NNN
owner: <papel>
depends_on: [TASK-<AREA>-NNN]
gate: G4
---

## Contexto

<por que esta tarefa existe; links para SPEC/ADR/PLAN>

## Escopo

- <item verificável>

## Não escopo

- <o que deliberadamente não será feito>

## Critérios de aceite

- [ ] <critério testável>

## Testes esperados

- <unitário | integração | arquitetura | contrato>

## Evidência exigida

- <comando + saída real>

## Riscos e observações

- <risco ou dependência>
```

## Regras

1. Uma TASK = uma unidade verificável e um único gate.
2. Sem critério de aceite testável, a TASK não está pronta.
3. Dependências explícitas; não iniciar com dependência aberta.
4. `status`: `pending`, `in_progress`, `blocked`, `done`, `cancelled`.
5. Evidência real é obrigatória para `done`; intenção não conclui TASK.
