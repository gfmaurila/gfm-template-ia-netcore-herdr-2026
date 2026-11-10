# Camadas e módulos

## Projetos

| Projeto | Responsabilidade | Depende de |
|---|---|---|
| `Gfm.Template.Domain` | Entidades, agregados, value objects, eventos, exceções de domínio | — |
| `Gfm.Template.Application` | Casos de uso (commands/queries), DTOs, validação, portas, comportamentos | Domain |
| `Gfm.Template.Infrastructure` | EF Core/Npgsql, repositórios, migrações, adaptadores de IA, relógio, telemetria | Application, Domain |
| `Gfm.Template.Host.Api` | Endpoints HTTP, middleware, DI, configuração, OpenAPI, health checks | Application, Infrastructure |

## Estrutura interna proposta

```text
src/Gfm.Template.Domain/
├─ Abstractions/            Entity, AggregateRoot, ValueObject, IDomainEvent
├─ Catalog/Items/           Item (agregado), ItemStatus, ItemCreated (evento)
└─ Exceptions/              DomainException

src/Gfm.Template.Application/
├─ Abstractions/            IClock, IUnitOfWork, ICurrentUser (se necessário)
├─ Messaging/               ICommand, IQuery, ICommandHandler, dispatcher mínimo
├─ Common/Behaviors/        validação, logging
├─ Catalog/Items/
│  ├─ Commands/             CreateItem, RenameItem (handler + validator)
│  ├─ Queries/              GetItemById, ListItems (DTOs)
│  └─ Ports/                IItemRepository
├─ Common/Errors/           Result, Error, mapeamento para ProblemDetails
└─ Ai/                      IAiChatClient, IAiEmbeddingClient, AiOptions, contratos

src/Gfm.Template.Infrastructure/
├─ Persistence/             AppDbContext, configurações, migrações, repositórios
├─ Ai/                      NullAiClient (padrão), OpenAiCompatibleClient (opcional)
├─ Time/                    SystemClock
└─ DependencyInjection.cs

src/Gfm.Template.Host.Api/
├─ Endpoints/Catalog/       ItemsEndpoints (Minimal API)
├─ Middleware/              exception handler, correlation id
├─ Configuration/           options + validação de configuração
├─ Program.cs
└─ appsettings.json / appsettings.Development.json
```

## Módulos versus projetos

**Decisão:** começar com 4 projetos e módulos como pastas (`Catalog/`), não um conjunto de
projetos por módulo.

Justificativa:
- Evita 12+ projetos vazios e sobrecarga de build/navegação.
- Fronteiras são verificadas por testes de arquitetura (sem referências cruzadas entre
  namespaces de módulos, exceto via contratos na `Application`).
- Extração para assemblies/processos separados fica documentada como evolução
  (ver ADR-0002 e `blueprints/composed-apps.md`).

Consequências:
- Disciplina é garantida por teste, não pelo compilador.
- Se um módulo crescer, promover para projetos próprios é uma refatoração localizada.

## Regras de fronteira

1. Um módulo não usa entidades de outro módulo; usa contratos/DTOs.
2. Repositórios são por agregado, não por tabela.
3. `Application` não referencia EF Core, ASP.NET Core ou SDK de IA.
4. `Host.Api` não acessa `DbContext` diretamente; usa casos de uso.
5. `Domain` não lança exceções HTTP e não conhece `ProblemDetails`.

## Composition root

Toda ligação (DI, options, middleware) acontece em `Host.Api/Program.cs`, que chama extensões
dos projetos (`AddApplication()`, `AddInfrastructure()`, `AddApi()`).
