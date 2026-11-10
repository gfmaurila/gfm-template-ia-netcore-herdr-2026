# ADR-0008 — Estratégia de testes

- **Status:** Proposto (aguarda aprovação)
- **Data:** 10/11/2026

## Contexto

O requisito exige testes unitários, integração, arquitetura e contrato, com banco real
isolado e descartável, limpeza garantida e nenhuma dependência de banco corporativo.

## Decisão

- **xUnit** como framework; `Assert` nativo (+ Shouldly opcional, licença BSD).
- **Unitários**: Domain e Application, sem I/O, rápidos.
- **Integração**: `WebApplicationFactory` + **Testcontainers** (PostgreSQL), banco efêmero
  por execução; migrações aplicadas no fixture; container descartado no fim.
- **Arquitetura**: NetArchTest/Roslyn validando dependências de camadas e fronteiras de módulo.
- **Contrato**: forma de sucesso e de erro (ProblemDetails) + snapshot OpenAPI.
- Cobertura é indicador, não meta absoluta; foco em comportamento e regras.
- Testes não usam banco compartilhado/corporativo/produção, nem dados reais.

## Alternativas consideradas

1. SQLite in-memory: rápido, mas não valida SQL/dialeto real do Postgres.
2. Testcontainers MSSQL: viável se o banco mudar (Q-02).
3. Banco fixo de CI: viola isolamento e reprodutibilidade.

## Consequências

- Positivas: fidelidade ao banco real, isolamento e limpeza automática.
- Negativas: testes de integração exigem Docker operacional (hoje parado).
- Riscos: lentidão/flakiness; mitigado por fixture compartilhada por coleção e timeouts.

## Regras de limpeza

- Container por execução de teste (ou por coleção) e descarte garantido.
- Ryuk habilitado para remover recursos órfãos mesmo em falha abrupta.
- Nunca reutilizar container/volume entre execuções de CI.
