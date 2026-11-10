---
name: task-decomposition
description: Use when breaking a PLAN into small verifiable TASKs in tasks/TASK-TEMPLATE.md format, with dependencies and evidence requirements.
---

# task-decomposition

## Quando usar

- Um PLAN aprovado precisa virar trabalho executável.
- Uma TASK está grande demais para um único gate.

## Passos

1. Ler PLAN, critérios de aceite e dependências.
2. Cortar em unidades que possam ser implementadas e testadas isoladamente.
3. Atribuir ID `TASK-<AREA>-NNN`.
4. Definir escopo, não escopo, aceite, testes e evidência.
5. Declarar dependências e gate único.
6. Ordenar por dependência e risco.

## Checklist

- [ ] Uma TASK = um gate.
- [ ] Critério de aceite testável.
- [ ] Dependências explícitas.
- [ ] Evidência exigida descrita.
- [ ] Nenhuma TASK exige decisão de ADR ainda não tomada.

## Referências

- `ai/prompts/PRM-011@1.0.0.md`
- `tasks/TASK-TEMPLATE.md`
- `templates/tasks/TASK-TEMPLATE.md`
