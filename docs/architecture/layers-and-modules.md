# Camadas e módulos

## Projetos

| Projeto | Responsabilidade | Depende de |
|---|---|---|
| `Gfm.Template.Domain` | Entidades, agregados, value objects, eventos, exceções de domínio | — |
| `Gfm.Template.Application` | Casos de uso (commands/queries), DTOs, validação, portas, comportamentos | Domain |
| `Gfm.Template.Infrastructure` | EF Core/Npgsql, repositórios, migrações, adaptadores de IA, relógio, telemetria | Application, Domain |
| `Gfm.Template.Host.Api` | Endpoints HTTP, middleware, DI, configuração, OpenAPI, health checks | Application, Infrastructure |

## Organização de `src/`

`src/` divide-se em duas áreas de nível superior:

```text
src/
├─ back-end/    # hosts e serviços .NET: os projetos em camadas descritos abaixo
└─ front-end/   # front-end do projeto, quando exigido (reservado nesta fase)
```

- Os projetos .NET em camadas ficam sob `src/back-end/`.
- `src/front-end/` é reservado ao front-end; tecnologia e subestrutura só serão definidas
  quando um projeto as exigir, com aprovação registrada.
- Nenhum outro nível intermediário sob `src/` está definido; ampliações exigem ADR.

## Estrutura interna proposta

```text
src/back-end/Gfm.Template.Domain/
├─ Abstractions/            Entity, AggregateRoot, ValueObject, IDomainEvent
├─ Catalog/Items/           Item (agregado), ItemStatus, ItemCreated (evento)
└─ Exceptions/              DomainException

src/back-end/Gfm.Template.Application/
├─ Abstractions/            IClock, IUnitOfWork, ICurrentUser (se necessário)
├─ Messaging/               ICommand, IQuery, ICommandHandler, dispatcher mínimo
├─ Common/Behaviors/        validação, logging
├─ Catalog/Items/
│  ├─ Commands/             CreateItem, RenameItem (handler + validator)
│  ├─ Queries/              GetItemById, ListItems (DTOs)
│  └─ Ports/                IItemRepository
├─ Common/Errors/           Result, Error, mapeamento para ProblemDetails
└─ Ai/                      IAiChatClient, IAiEmbeddingClient, AiOptions, contratos

src/back-end/Gfm.Template.Infrastructure/
├─ Persistence/             AppDbContext, configurações, migrações, repositórios
├─ Ai/                      NullAiClient (padrão), OpenAiCompatibleClient (opcional)
├─ Time/                    SystemClock
└─ DependencyInjection.cs

src/back-end/Gfm.Template.Host.Api/
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
