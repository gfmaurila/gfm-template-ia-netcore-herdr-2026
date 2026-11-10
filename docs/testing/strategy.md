# Estratégia de testes

## Pirâmide adotada

```text
        contrato (poucos, estáveis)
      integração (HTTP + banco real)
   arquitetura (fronteiras, dependências)
 unitários (domínio e casos de uso)
```

Nenhum nível substitui outro; cada requisito deve mapear para ao menos um teste.

## Projetos

| Projeto | Escopo | I/O |
|---|---|---|
| `Gfm.Template.Domain.Tests` | invariantes, transições, VOs | não |
| `Gfm.Template.Application.Tests` | handlers, validação, erros | não (fakes) |
| `Gfm.Template.Architecture.Tests` | camadas, fronteiras de módulo, convenções | não |
| `Gfm.Template.Api.IntegrationTests` | endpoints + Postgres (Testcontainers) | sim |

## Convenções

- xUnit; nomes `Metodo_Cenario_Resultado`.
- Arrange/Act/Assert; um comportamento por teste.
- Sem `Thread.Sleep`; tempo via `IClock` fake.
- Sem ordem implícita entre testes; independência total.
- Fakes manuais primeiro; mock library só se necessário.
- `Assert` nativo do xUnit (Shouldly opcional, pendente Q-15).

## Unidade

- Domínio: toda invariante e transição inválida.
- Application: caminho felizes, not found, conflito, validação, cancelamento.
- Sem acesso a banco, rede ou filesystem.

## Integração

- `WebApplicationFactory<Program>` + Testcontainers Postgres.
- Banco efêmero por execução/coleção; migrações aplicadas no fixture.
- Cada teste cria seus dados; sem dependência de seed global.
- Cobrir: CRUD do `Catalog`, paginação, erros 400/404/409/422, health checks.
- Ver [`testcontainers.md`](testcontainers.md).

## Arquitetura

- `Domain` sem referência a frameworks.
- `Application` sem EF Core/ASP.NET/SDK de IA.
- `Host.Api` sem uso direto de `DbContext`.
- Nenhuma referência cruzada entre namespaces de módulos.
- Regras verificadas por tipo (NetArchTest/Roslyn), não por revisão manual.

## Contrato

- Snapshot do documento OpenAPI (estabilidade de rotas/esquemas).
- Formato de sucesso (JSON) e de erro (`ProblemDetails` com `code`, `traceId`).
- Códigos de status conforme spec do domínio.

## Cobertura

- Indicador, não meta absoluta; foco em comportamento.
- Proposta: ≥ 70% de linha em `Domain`/`Application` (Q-10).
- Sem testes "cosméticos" apenas para elevar número.

## Critérios de bloqueio (não pode mergear)

- Teste falhando ou desabilitado sem justificativa.
- Teste de integração apontando para banco compartilhado/corporativo/produção.
- Uso de dado real/PII em fixture.
- Teste dependente de ordem ou de estado global.

## Matriz de rastreabilidade (modelo)

| Requisito | Teste(s) | Tipo | Status |
|---|---|---|---|
| UC-01 criar item | `CreateItemHandlerTests`, `ItemsEndpointTests` | unit + integração | pendente |
| Transições de status | `ItemTests` | unit | pendente |
| Paginação | `ListItemsTests` | unit + integração | pendente |
| Erro uniforme | `ProblemDetailsContractTests` | contrato | pendente |
| Fronteiras de camada | `LayerRulesTests` | arquitetura | pendente |
| IA desabilitada | `NullAiClientTests` | unit | pendente |
