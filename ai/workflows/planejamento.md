# Workflow — planejamento

## Objetivo

Converter requisito em SPEC, ADR (quando estrutural) e PLAN aprovados.

## Sequência

```text
1. SPEC (RF/RNF, aceite, riscos)        → gate G1
2. ADR (decisão estrutural)             → gate G2
3. PLAN (fases, gates, entregáveis)     → gate G3
4. TASKs (unidades verificáveis)        → gate G4
```

## Papéis

- Architect produz.
- Reviewer verifica consistência.
- Responsável humano aprova cada gate.

## Regras

- Nenhuma TASK antes do PLAN aprovado.
- Nenhuma decisão estrutural sem ADR.
- Perguntas abertas em `docs/plans/open-questions.md`.

## Saída

SPEC, ADR, PLAN e TASKs rastreáveis.
