# Blueprint — Aplicações compostas

## Quando usar

- API + Worker + infraestrutura (banco, cache, broker) no mesmo produto.
- Múltiplos módulos com fronteiras claras.

## Estrutura

```text
src/
  Gfm.Template.Domain/
  Gfm.Template.Application/
  Gfm.Template.Infrastructure/
  Gfm.Template.Host.Api/
  Gfm.Template.Host.Worker/     # opcional
deploy/
  api.Dockerfile
  worker.Dockerfile             # opcional, mesma base
  compose.yaml                  # api + worker + postgres + redis (profiles)
```

## Compose (perfis)

| Serviço | Perfil | Uso |
|---|---|---|
| `postgres` | padrão | persistência |
| `api` | padrão | HTTP |
| `worker` | `worker` | jobs |
| `redis` | `cache` | cache/lock |
| `otel-collector` | `observability` | telemetria local |

- Perfis evitam subir infraestrutura não usada.
- Mesma imagem base para hosts; comandos diferentes.

## Módulos

- Módulos como pastas; comunicação por contratos da `Application` ou eventos de integração.
- Sem acesso direto ao repositório/DbContext de outro módulo.
- Extração para serviço separado só com necessidade operacional comprovada.

## Consistência

- Uma transação por caso de uso; outbox para eventos entre módulos/processos.
- Idempotência em consumidores.
- Sem transações distribuídas (2PC).

## Testes

- Integração por host (API e Worker).
- Teste de contrato entre módulos.
- Compose smoke test quando aplicável.

## Critérios para NÃO compor

- Um único host resolve; não adicionar Worker/Redis/broker "por precaução".
- Sem necessidade de escala/isolamento, manter monólito simples.
