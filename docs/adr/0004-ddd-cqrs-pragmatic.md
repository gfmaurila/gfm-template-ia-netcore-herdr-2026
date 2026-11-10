# ADR-0004 — DDD tático e CQRS leve

- **Status:** Proposto (aguarda aprovação)
- **Data:** 10/11/2026

## Contexto

O template precisa demonstrar boas práticas de domínio e separação de leitura/escrita sem
introduzir complexidade de event sourcing, sagas ou barramentos pesados.

## Decisão

- **DDD tático** apenas onde há regra real: agregados, entidades, value objects, eventos de
  domínio e invariantes. Sem "DDD de fachada" em CRUD trivial.
- **CQRS leve**: commands e queries com handlers próprios; sem bancos separados; sem
  projeções materializadas.
- **Sem event sourcing**; eventos de domínio em processo, publicados após commit.
- Dispatcher mínimo interno (`ICommandHandler`/`IQueryHandler`) para desacoplar endpoints.
- Transação por caso de uso; concorrência otimista via `RowVersion`/`xmin` quando necessário.

## Alternativas consideradas

1. **CRUD direto com `DbContext` nos endpoints**: rápido, mas sem casos de uso testáveis.
2. **MediatR**: maduro, porém dependência adicional e risco de licenciamento em versões novas.
3. **Event sourcing/CQRS completo**: complexidade desproporcional ao template.

## Consequências

- Positivas: casos de uso explícitos, testáveis, com limites claros.
- Negativas: mais tipos por feature; risco de duplicação command/query.
- Riscos: dispatcher caseiro pode virar mini-framework; limitar a escopo mínimo e testá-lo.

## Guardrails

- Handlers não chamam outros handlers.
- Um handler = uma transação.
- Query não altera estado; `AsNoTracking` obrigatório em leitura.
