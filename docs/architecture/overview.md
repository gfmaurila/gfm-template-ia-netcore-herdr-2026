# Arquitetura — Visão geral

## Estilo arquitetural

**Monólito modular em camadas (Clean Architecture pragmática)** com DDD tático e CQRS leve.

```text
┌──────────────────────────────────────────────────────────┐
│ Host.Api (ASP.NET Core, endpoints, middleware, DI)       │
└───────────────▲──────────────────────────────────────────┘
                │
┌───────────────┴──────────────────────────────────────────┐
│ Application (casos de uso, CQRS, validação, contratos)   │
└───────────────▲──────────────────────────────────────────┘
                │
┌───────────────┴──────────────────────────────────────────┐
│ Domain (entidades, agregados, VOs, eventos, regras)      │
└──────────────────────────────────────────────────────────┘
        Infrastructure ──► Application / Domain
        (EF Core, IA, telemetria, relógio, integrações)
```

Regras de dependência (verificadas por testes de arquitetura):

- `Domain` não referencia nenhum outro projeto (nem pacotes de infraestrutura).
- `Application` referencia `Domain`.
- `Infrastructure` referencia `Application` e `Domain`.
- `Host.Api` referencia `Application` e `Infrastructure` (composição).
- Nenhuma seta aponta para `Host.Api`.

## Por que este estilo

- Casos de uso explícitos e testáveis sem banco.
- Domínio isolado de frameworks.
- Substituição de persistência/provedor de IA sem tocar na regra de negócio.
- Custo controlado: 4 projetos, sem camadas extras cerimoniais.

Detalhes: [`layers-and-modules.md`](layers-and-modules.md), [`cross-cutting.md`](cross-cutting.md).

## Módulos

O template nasce com **um módulo de exemplo (`Catalog`)**; a estrutura suporta múltiplos
módulos por pastas e testes de fronteira. Um segundo módulo só será materializado quando
houver caso de uso real (ver [`../blueprints/composed-apps.md`](../blueprints/composed-apps.md)).

## Fluxo de uma requisição

```text
HTTP → endpoint → validação → handler (Application) → domínio → repositório (Infrastructure)
     → SaveChanges → eventos de domínio → resposta (ProblemDetails em erro)
```

`Host.Api` não contém regra de negócio: apenas tradução HTTP, autenticação, autorização,
observabilidade e composição.

## Pontos de extensão (opcionais, não implementados nesta fase)

| Extensão | Como entra | Blueprint |
|---|---|---|
| Worker/Batch | novo host `Gfm.Template.Host.Worker` | `blueprints/worker-batch.md` |
| Redis (cache/distributed lock) | `Infrastructure`, interface na `Application` | `blueprints/composed-apps.md` |
| Mensageria | outbox + broker; contrato na `Application` | `blueprints/composed-apps.md` |
| IA (chat/embedding/tools) | interfaces na `Application`; adaptador na `Infrastructure` | `blueprints/ai-app.md` |
| AWS | mesma imagem, configuração 12-factor | `devops/ci-cd.md` |

## Decisões relacionadas

- [ADR-0002](../adr/0002-modular-monolith.md) — monólito modular.
- [ADR-0003](../adr/0003-clean-architecture-layers.md) — camadas.
- [ADR-0004](../adr/0004-ddd-cqrs-pragmatic.md) — DDD/CQRS.
- [ADR-0001](../adr/0001-dotnet-10-target.md) — .NET 10.
