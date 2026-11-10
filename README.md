# GFM.Template — .NET + IA

Template pessoal, reutilizável e independente de empresa/cliente para aplicações .NET
modernas, desenvolvido no workspace `C:\Work\dev\herdr.dev` com OpenCode dentro do Herdr.

> **Status atual: Fase 1 (descoberta) e Fase 2 (documentação) concluídas.**
> Nenhum código C# foi gerado. Git não foi inicializado. Nenhuma dependência foi instalada.
> A implementação só começa após aprovação explícita.

## Objetivo

Fornecer uma base profissional para novos projetos .NET com:

- ASP.NET Core Web API sobre .NET 10 (compatibilidade planejada com .NET 8).
- Monólito modular com separação Domain / Application / Infrastructure / Host.Api.
- DDD e CQRS pragmáticos, SOLID e Clean Architecture sem abstrações cerimoniais.
- Validação, erros uniformes (ProblemDetails), DI e observabilidade desde o início.
- Testes unitários, de integração (Testcontainers), de arquitetura e de contrato.
- DevOps local-first com Docker, Compose e GitHub Actions.
- Camada de IA opcional e desacoplada, sem exigir credenciais no template básico.
- Blueprints documentados para API, Worker/Batch, aplicações compostas e IA.

## Escopo e não escopo

| Em escopo (após aprovação) | Fora de escopo |
|---|---|
| Template genérico .NET + IA | Qualquer dado, regra ou integração de cliente |
| API de exemplo com domínio neutro | Autenticação corporativa / SSO proprietário |
| Postgres de exemplo, descartável em testes | Banco corporativo, compartilhado ou de produção |
| Docker/Compose locais | Publicação em nuvem nesta fase |
| CI em GitHub Actions | Publicação no GitHub sem autorização |
| Adaptadores de IA opcionais | Custos/credenciais de IA obrigatórios |

## Stack alvo

- .NET SDK 10.0.402 (C# 14), TFM `net10.0`; caminho de compatibilidade para `net8.0` documentado.
- ASP.NET Core Minimal APIs.
- EF Core + Npgsql (PostgreSQL 17) como persistência de exemplo.
- xUnit + Testcontainers + `Microsoft.AspNetCore.Mvc.Testing`.
- OpenTelemetry (logs/traces/métricas) com exportação OTLP opcional.
- Docker multi-stage + Docker Compose.

Versões e pacotes definitivos serão fixados via `global.json` + Central Package Management,
após aprovação (ver `docs/adr/0005-central-build-and-packages.md`).

## Árvore planejada

```text
herdr.dev/
├─ AGENTS.md                 # instruções para OpenCode e agentes
├─ prompts.md                # biblioteca de prompts versionados
├─ README.md
├─ global.json               # pin do SDK (implementação)
├─ Directory.Build.props     # propriedades comuns (implementação)
├─ Directory.Packages.props  # versões centrais de pacotes (implementação)
├─ .editorconfig             # estilo (implementação)
├─ .gitignore / .gitattributes
├─ docs/                     # ver docs/README.md
├─ src/
│  ├─ Gfm.Template.Domain/
│  ├─ Gfm.Template.Application/
│  ├─ Gfm.Template.Infrastructure/
│  └─ Gfm.Template.Host.Api/
├─ tests/
│  ├─ Gfm.Template.Domain.Tests/
│  ├─ Gfm.Template.Application.Tests/
│  ├─ Gfm.Template.Architecture.Tests/
│  └─ Gfm.Template.Api.IntegrationTests/
├─ deploy/
│  ├─ api.Dockerfile
│  └─ compose.yaml
├─ prompts/                  # prompts versionados (implementação)
└─ .github/workflows/ci.yml
```

Os diretórios `src/`, `tests/`, `deploy/`, `prompts/` e `.github/` **ainda não existem**;
são o resultado da Fase 3+ e dependem de aprovação.

## Documentação

Comece por [`docs/README.md`](docs/README.md). Destaques:

- [`AGENTS.md`](AGENTS.md) — regras e papéis dos agentes.
- [`prompts.md`](prompts.md) — prompts versionados.
- [`docs/architecture/overview.md`](docs/architecture/overview.md) — arquitetura.
- [`docs/plans/implementation-plan.md`](docs/plans/implementation-plan.md) — plano e gates.
- [`docs/plans/open-questions.md`](docs/plans/open-questions.md) — decisões pendentes.
- [`docs/security/security-baseline.md`](docs/security/security-baseline.md) — segurança.

## Ambiente verificado (10/11/2026)

| Item | Valor | Observação |
|---|---|---|
| OS | Windows 11 Pro 10.0.26300 (x64) | OK |
| Windows PowerShell | 5.1.26100.9818 | PowerShell 7.6.9 também disponível |
| .NET SDK | 10.0.402 | Sem SDK 8 (apenas runtime 8.0.21) |
| Git | 2.55.0.windows.5 | Diretório **não** é repositório Git |
| Docker CLI | 29.8.2 | Daemon **não operacional** |
| Node.js / npm | 24.20.0 / 11.19.0 | OK |
| OpenCode | 1.19.0 | OK |
| Herdr Core / App | hc 0.1.19 / 0.1.14 | OK (`hc`, `herdr-core`, `herdr-app`) |
| Codex CLI | 0.163.0 | Presente; este projeto usa OpenCode |

## Uso local (previsto, não validado)

```powershell
# após implementação e aprovação
dotnet restore
dotnet build -warnaserror
dotnet test
dotnet run --project src/Gfm.Template.Host.Api
```

Docker Compose e CI serão validados com execução comprovada na fase de implementação.

## Segurança

- Nenhum segredo, credencial ou dado de cliente no repositório.
- IA desligada por padrão; nenhum provedor é chamado sem configuração explícita.
- Push/publicação e instalações globais exigem aprovação.

## Licença

**Pendente de decisão** (ver `docs/plans/open-questions.md`, Q-04).
