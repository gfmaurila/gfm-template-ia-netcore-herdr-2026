# Desenvolvimento local (local-first)

> Comandos abaixo são **previstos**; não foram executados (código ainda não existe).

## Pré-requisitos

| Requisito | Estado atual | Ação |
|---|---|---|
| .NET SDK 10.0.402 | OK | — |
| Git | OK | repositório ainda não inicializado |
| Docker Desktop | **daemon parado** | iniciar antes de integração |
| Node/npm | OK | não usado pelo template |
| OpenCode / Herdr | OK | ver `../ai/opencode-herdr.md` |

## Fluxo 1 — apenas aplicação (sem container)

```powershell
dotnet restore
dotnet build -warnaserror
dotnet run --project src/back-end/Gfm.Template.Host.Api
```

- Requer Postgres acessível (definir `ConnectionStrings__Default`).
- Alternativa: usar o perfil de infraestrutura do Compose para subir só o banco:

```powershell
docker compose -f deploy/compose.yaml up -d postgres
```

## Fluxo 2 — container first

```powershell
docker compose -f deploy/compose.yaml up -d --build
docker compose -f deploy/compose.yaml ps
docker compose -f deploy/compose.yaml logs -f api
docker compose -f deploy/compose.yaml down -v
```

- API: `http://localhost:8080` (previsão), health em `/health/ready`.
- Postgres com volume nomeado; `down -v` remove dados locais.
- Redis e coletor OTel apenas em profiles opcionais.

## Configuração (12-factor)

| Variável | Uso | Padrão |
|---|---|---|
| `ASPNETCORE_ENVIRONMENT` | ambiente | `Development` (local) |
| `ConnectionStrings__Default` | Postgres | sem valor (obrigatório) |
| `Ai__Enabled` | liga IA | `false` |
| `Ai__Provider` | `none`/`openai-compatible`/`ollama` | `none` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | exporta telemetria | vazio (desligado) |
| `OTEL_SERVICE_NAME` | nome do serviço | `gfm-template-api` |

- Segredos locais via `dotnet user-secrets` (nunca em `appsettings.json` versionado).
- `.env` local (ignorado pelo Git) apenas para Compose; sem commitar.

## Convenções de porta

| Serviço | Host | Container |
|---|---|---|
| API HTTP | 5080 | 8080 |
| Postgres | 5432 | 5432 |
| Redis (opcional) | 6379 | 6379 |

Portas fixas de host são apenas conveniência; testes usam portas dinâmicas.

## Diagnóstico rápido

```powershell
dotnet --info
docker info
docker compose -f deploy/compose.yaml config
```

Se `docker info` falhar, iniciar Docker Desktop — os testes de integração não serão pulados
silenciosamente; serão reportados como **não validados**.

## O que NÃO fazer

- Não rodar `docker compose down -v` em ambiente com dados que você queira preservar.
- Não usar banco corporativo/compartilhado para testes.
- Não instalar ferramentas globais sem aprovação.
