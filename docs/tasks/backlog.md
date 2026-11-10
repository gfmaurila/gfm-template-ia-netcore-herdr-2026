# Backlog

Status: `pending approval` (nada iniciado). Tarefas pequenas, com critério de aceite.

Este arquivo descreve o backlog **funcional** do template. A conversão para o formato
executável (`tasks/TASK-TEMPLATE.md`) ocorre após a aprovação do PLAN; ver `tasks/README.md`.

## T-001 — Esqueleto e build

- Criar `global.json`, `Directory.Build.props`, `Directory.Packages.props`, `.editorconfig`,
  `.gitignore`, solução e 4+4 projetos.
- **Aceite:** `dotnet build -warnaserror` sem warnings; `dotnet format --verify-no-changes`.

## T-002 — Domínio `Catalog`

- `Item`, `Money`, `ItemStatus`, eventos, `DomainException`, `IClock`.
- **Aceite:** testes unitários de invariantes/transições verdes.

## T-003 — Casos de uso

- UC-01…UC-06 com handlers, validators, `Result`/`Error`.
- **Aceite:** testes unitários (sucesso e erro) verdes.

## T-004 — Persistência

- `AppDbContext`, mapeamentos, `IItemRepository`, migração inicial, `xmin`.
- **Aceite:** migração aplica em Postgres efêmero.

## T-005 — Testes de integração

- Fixture Testcontainers, migração no fixture, testes de repositório/casos de uso.
- **Aceite:** verde com Docker; container removido; nenhum banco externo.

## T-006 — API e erros

- Endpoints `Catalog`, `ProblemDetails`, exception handler, OpenAPI, paginação.
- **Aceite:** testes de contrato e integração HTTP verdes.

## T-007 — Arquitetura

- Testes de dependência de camadas e fronteiras de módulo.
- **Aceite:** violação simulada falha o teste (prova de eficácia).

## T-008 — Observabilidade

- OTel opcional, health checks, correlação, redação de log.
- **Aceite:** roda sem exportador; span/log correlacionado com exportador.

## T-009 — Segurança

- Headers, CORS configurável, rate limit opcional, varredura de pacotes.
- **Aceite:** sem segredos; dependências sem vulnerabilidade crítica conhecida.

## T-010 — Docker

- Dockerfile multi-stage non-root; Compose api+postgres (+profiles).
- **Aceite:** `docker compose up` saudável; `down -v` limpa.

## T-011 — CI

- Workflow GitHub Actions (restore/build/format/test/image).
- **Aceite:** pipeline executa com evidência; sem serviços corporativos.

## T-012 — IA opcional

- Contratos, `NullAiClient`, adaptador HTTP opcional, `AiOptions`, testes.
- **Aceite:** template funciona sem credenciais; testes de timeout/erro verdes.

## T-013 — Documentação final

- Atualizar README/ADRs/specs conforme implementado; registrar decisões reais.
- **Aceite:** docs coerentes com código; nenhuma afirmação não validada.

## Bloqueios atuais

- Aprovação das Fases 2–3 (`plans/open-questions.md`).
- Docker daemon parado (T-005/T-010/T-011).
