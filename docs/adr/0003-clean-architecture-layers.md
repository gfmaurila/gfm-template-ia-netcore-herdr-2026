# ADR-0003 — Clean Architecture em 4 projetos

- **Status:** Proposto (aguarda aprovação)
- **Data:** 10/11/2026

## Contexto

É necessário isolamento de domínio, testabilidade dos casos de uso e substituição de
infraestrutura (banco, IA, telemetria) sem reescrever regras.

## Decisão

Quatro projetos com dependências unidirecionais:

```text
Domain ← Application ← Infrastructure
                    ↖ Host.Api → Infrastructure
```

- `Domain`: sem dependências externas.
- `Application`: portas (interfaces), casos de uso, validação, DTOs.
- `Infrastructure`: EF Core/Npgsql, repositórios, IA, relógio.
- `Host.Api`: composição, endpoints, middleware.

Sem `SharedKernel`, `Contracts` ou camada `Presentation` separada nesta fase.

## Alternativas consideradas

1. **3 projetos (Domain/Application/Host com infra embutida)**: menos isolamento de I/O.
2. **5+ projetos (Domain/Application/Contracts/Infrastructure/Presentation)**: cerimônia sem ganho.
3. **Vertical Slice por feature**: viável, mas menos alinhado ao pedido explícito de camadas.

## Consequências

- Positivas: domínio puro, testes rápidos, troca de adaptadores.
- Negativas: mapeamento entre camadas (entidade ↔ DTO) e mais arquivos.
- Riscos: tentação de "camada de serviço" anêmica; mitigado por casos de uso coesos.

## Regras verificadas por teste

- Nenhuma referência de `Domain` a framework.
- `Application` sem EF Core/ASP.NET/SDK de IA.
- `Host.Api` sem acesso direto a `DbContext`.
