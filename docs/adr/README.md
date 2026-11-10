# ADRs — Architecture Decision Records

Formato: Contexto, Decisão, Alternativas, Consequências, Riscos, Status.

| ADR | Título | Status |
|---|---|---|
| [0001](0001-dotnet-10-target.md) | .NET 10 como alvo inicial, compatibilidade planejada com .NET 8 | Proposto |
| [0002](0002-modular-monolith.md) | Monólito modular com módulos em pastas | Proposto |
| [0003](0003-clean-architecture-layers.md) | Clean Architecture em 4 projetos | Proposto |
| [0004](0004-ddd-cqrs-pragmatic.md) | DDD tático e CQRS leve, sem event sourcing | Proposto |
| [0005](0005-central-build-and-packages.md) | SDK e pacotes centralizados; sem MediatR | Proposto |
| [0006](0006-error-handling-and-validation.md) | Result + ProblemDetails + FluentValidation | Proposto |
| [0007](0007-observability.md) | OpenTelemetry opcional e logs estruturados | Proposto |
| [0008](0008-testing-strategy.md) | xUnit + Testcontainers + testes de arquitetura | Proposto |
| [0009](0009-local-first-devops.md) | Local first → container first → cloud ready → AWS | Proposto |
| [0010](0010-ai-abstraction.md) | IA opcional, desacoplada e desligada por padrão | Proposto |

Status possíveis: Proposto, Aceito, Substituído, Rejeitado.
Mudança de decisão exige novo ADR (não editar o histórico da decisão anterior).
