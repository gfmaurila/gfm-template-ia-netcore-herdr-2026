# tasks — unidades de trabalho

Cada TASK é uma unidade pequena, verificável e com um único gate.

```text
tasks/
  TASK-TEMPLATE.md      formato único (fonte canônica)
  backlog/              TASKs prontas para execução
  bootstrap/            TASKs de bootstrap do template
  done/                 TASKs concluídas com evidência
```

## Regras

1. ID `TASK-<AREA>-NNN`; arquivo `TASK-<AREA>-NNN-<slug>.md`.
2. Frontmatter e seções conforme `TASK-TEMPLATE.md`.
3. Sem critério de aceite testável, a TASK não entra em execução.
4. Só vai para `done/` com evidência real anexada.
5. Dependência aberta mantém a TASK em `blocked`.
6. Nenhuma TASK de código antes da aprovação da Fase 3.

## Estados

`pending` → `in_progress` → `done` | `blocked` | `cancelled`

## Rastreabilidade

Toda TASK referencia `SPEC-NNN`, `PLAN-NNN` e, quando aplicável, `ADR-NNNN`.
