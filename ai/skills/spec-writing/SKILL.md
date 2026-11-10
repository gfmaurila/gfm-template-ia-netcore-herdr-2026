---
name: spec-writing
description: Use when writing or reviewing a SPEC (requirements, acceptance criteria, risks) before an ADR or PLAN. Covers SPEC-NNN structure and testability.
---

# spec-writing

## Quando usar

- Novo requisito ou problema precisa virar documento verificável.
- Uma SPEC existente precisa ser revisada antes de ADR/PLAN.

## Passos

1. Ler `AGENTS.md`, `templates/specifications/SPEC-TEMPLATE.md` e specs existentes.
2. Definir contexto, objetivo, escopo e não escopo.
3. Numerar requisitos funcionais (RF) e não funcionais (RNF).
4. Escrever critérios de aceite testáveis e rastreáveis.
5. Registrar riscos, dependências e perguntas abertas.
6. Classificar afirmações como [verificado], [inferido] ou [não validado].

## Checklist

- [ ] Todo requisito tem critério de aceite verificável.
- [ ] Não escopo explícito.
- [ ] Sem segredos, PII ou dados de cliente.
- [ ] Perguntas abertas registradas em `docs/plans/open-questions.md`.
- [ ] Nenhuma decisão estrutural tomada sem ADR.

## Referências

- `ai/agents/architect.md`
- `ai/prompts/PRM-009@1.0.0.md`
- `templates/specifications/SPEC-TEMPLATE.md`
