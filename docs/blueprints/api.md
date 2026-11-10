# Blueprint — API

## Quando usar

- Serviço HTTP síncrono (REST/JSON) como produto principal.
- É o **baseline** deste template (não é extensão opcional).

## Estrutura

```text
src/back-end/
  Gfm.Template.Domain/
  Gfm.Template.Application/
  Gfm.Template.Infrastructure/
  Gfm.Template.Host.Api/
tests/
  Gfm.Template.Domain.Tests/
  Gfm.Template.Application.Tests/
  Gfm.Template.Architecture.Tests/
  Gfm.Template.Api.IntegrationTests/
deploy/api.Dockerfile
deploy/compose.yaml
```

## Dependências e decisões

- Minimal APIs + ProblemDetails + OpenAPI.
- CQRS leve; um handler por caso de uso.
- Paginação/filtro obrigatórios em listagens.
- Health `/health/live` e `/health/ready`.

## Testes

- Unitários: domínio/casos de uso.
- Integração: HTTP + Postgres efêmero.
- Contrato: OpenAPI + formato de erro.

## Critérios para NÃO expandir agora

- Não adicionar autenticação, multitenancy ou versionamento de API sem caso real.
- Não criar camada `Contracts` separada enquanto houver um único consumidor interno.
- Não adicionar GraphQL/gRPC sem requisito concreto.

## Riscos

- API anêmica (CRUD nos endpoints) → reforçar casos de uso.
- Contrato instável → testes de contrato e versionamento quando necessário.
