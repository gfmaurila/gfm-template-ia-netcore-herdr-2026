# CI/CD — GitHub Actions

> Pipeline **planejado**; não criado/executado nesta fase.

## Estratégia

`LOCAL FIRST → CONTAINER FIRST → CLOUD READY → AWS TARGET`

- Local: `dotnet` + Compose.
- Container: mesma imagem multi-stage.
- Cloud ready: 12-factor, health, logs stdout.
- AWS target: documentado (ECS/Fargate + RDS), não implementado.

## Workflow `ci.yml` (previsto)

Gatilhos: `push` e `pull_request` em `main`.

| Job | Passos | Falha se |
|---|---|---|
| `build` | checkout, setup-dotnet 10, cache NuGet, restore, build `-warnaserror` | warning/erro |
| `lint` | `dotnet format --verify-no-changes` | formatação divergente |
| `test` | unit + arquitetura + integração (Testcontainers) + contrato; publica TRX/coverage | teste vermelho |
| `security` | `dotnet list package --vulnerable --include-transitive` | vulnerabilidade alta/crítica |
| `image` | `docker build` (sem push) | build da imagem falha |

- Runner: `ubuntu-latest` (Docker nativo para Testcontainers).
- Sem serviços corporativos, sem registry privado, sem segredos obrigatórios.
- Publicação de imagem/registry: **fora de escopo** até aprovação (Q-13).
- Deploy: não incluído.

## Cache e determinismo

- Cache de `~/.nuget/packages` por hash do `Directory.Packages.props`.
- SDK fixado por `global.json`.
- Imagens Docker pinadas por tag/digest.
- `restore` com `--locked-mode` quando houver `packages.lock.json` (avaliar).

## Segredos

- Apenas via GitHub Secrets; nenhum valor em workflow.
- Nenhum segredo necessário para o pipeline básico.
- Logs não ecoam variáveis sensíveis.

## Artefatos e evidência

- Resultados de teste (TRX) e cobertura anexados ao run.
- Log de build e de imagem.
- Relatório final: passou / falhou / não validado.

## Proteção de branch (proposta)

- PR obrigatório; checks verdes; sem force-push; revisão antes de merge.
- Dependabot/renovação de pacotes: avaliar (não habilitar sem aprovação).

## AWS target (documentação, não execução)

| Componente | Alvo sugerido | Observação |
|---|---|---|
| API | ECS/Fargate | imagem do CI/registry |
| Banco | RDS PostgreSQL | privado, backup |
| Segredos | AWS Secrets Manager | injeção em runtime |
| Telemetria | OTLP → coletor gerenciado | opcional |
| CI/CD | GitHub Actions + OIDC | sem chaves estáticas |

Nada disso é implementado até existir decisão e ambiente aprovados (Q-14).
