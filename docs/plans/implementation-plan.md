# Plano de implementação por etapas

> Nada abaixo é executado antes da **aprovação explícita** das Fases 2–3.
> Cada etapa termina com evidência real (saída de build/teste) e relatório
> passou / falhou / não validado.

## Gate 0 — Aprovação

- Revisar `README.md`, `AGENTS.md`, `docs/architecture/*`, ADRs e specs.
- Responder `docs/plans/open-questions.md` (Q-01…Q-12).
- Aprovar arquitetura, nomes de solução/projetos e alvo de banco.

## Etapa 1 — Esqueleto da solução

- `global.json`, `Directory.Build.props`, `Directory.Packages.props`, `.editorconfig`,
  `.gitignore`, `.gitattributes`.
- Solução `GFM.Template.slnx` e 4 projetos (`Domain`, `Application`, `Infrastructure`,
  `Host.Api`) + 4 projetos de teste.
- `Program.cs` mínimo com `/health/live`.
- **Aceite:** `dotnet restore`, `dotnet build -warnaserror` sem warnings; app sobe e health responde.

## Etapa 2 — Domínio + Application

- Agregado `Item`, `Money`, `ItemStatus`, eventos, exceções.
- Commands/queries, handlers, validators, `Result`/`Error`, `IClock`.
- Testes unitários de invariantes e casos de uso.
- **Aceite:** build limpo + testes unitários verdes.

## Etapa 3 — Persistência + integração

- `AppDbContext`, mapeamentos, repositório, migração inicial, `IUnitOfWork`.
- Fixture Testcontainers (Postgres), migração no startup do fixture, limpeza.
- Testes de integração de repositório e casos de uso.
- **Aceite:** testes de integração verdes com Docker; container removido ao final.

## Etapa 4 — API + erros + validação

- Endpoints do `Catalog`, `ProblemDetails`, handler de exceções, OpenAPI.
- Testes de contrato (sucesso/erro) e integração HTTP ponta a ponta.
- **Aceite:** suíte completa verde; contrato estável documentado.

## Etapa 5 — Observabilidade + segurança

- OpenTelemetry opcional, health checks, correlação, redação de logs.
- Headers, CORS por configuração, rate limiting opcional, verificação de dependências.
- **Aceite:** app roda sem exportador; traces com endpoint configurado; sem segredos.

## Etapa 6 — DevOps

- `deploy/api.Dockerfile` multi-stage (non-root), `deploy/compose.yaml` (api + postgres,
  Redis/OTel em profile opcional).
- `.github/workflows/ci.yml`: restore, build, format, testes, imagem.
- **Aceite:** compose sobe saudável; pipeline executa localmente/equivalentes com evidência.

## Etapa 7 — IA opcional

- `IAiChatClient`/`IAiEmbeddingClient`, `NullAiClient`, adaptador HTTP opcional, `AiOptions`.
- Testes: desabilitado, timeout, erro, sucesso com servidor falso.
- **Aceite:** template básico funciona sem credenciais; IA só ativa por configuração.

## Etapa 8 — Blueprints (somente sob solicitação)

- API, Worker/Batch, aplicações compostas, IA (RAG/tools/agents).
- Só materializar projeto quando houver necessidade concreta aprovada.

## Marcos e relatórios

| Marco | Entregável | Evidência |
|---|---|---|
| M1 | Esqueleto compilando | log de build |
| M2 | Núcleo testado | log de `dotnet test` |
| M3 | API funcional | testes de integração/contrato |
| M4 | Container + CI | compose up + logs |
| M5 | IA opcional | testes sem/com configuração |

## Critérios de aceite globais

1. Build sem warnings/erros; `dotnet format --verify-no-changes` limpo.
2. Testes unitários, integração, arquitetura e contrato verdes.
3. Banco efêmero por execução, limpo mesmo em falha.
4. Compose sobe API + Postgres; health `ready`.
5. Sem segredos/PII; IA desligada por padrão.
6. Documentação/ADRs atualizados.
7. Nenhuma menção a dados, nomes ou integrações de clientes.

## Riscos e mitigações

| Risco | Impacto | Mitigação |
|---|---|---|
| Docker daemon parado | bloqueia Etapa 3 | iniciar Docker Desktop (ação do responsável) |
| SDK 8 ausente | impede validar .NET 8 | adiar claim ou instalar SDK 8 |
| Escopo crescer (Worker/IA cedo) | atraso | blueprints só sob solicitação |
| Licença de pacote | bloqueio legal | política de licenças (ADR-0005) |
| Testes flaky | falsa confiança | fixtures determinísticas, sem sleep |
