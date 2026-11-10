# CI/CD — GitHub Actions

> Nesta fase (template documental) existe apenas o workflow de validação
> `validate-template.yml`. O pipeline de aplicação descrito abaixo é **planejado**;
> só será criado após a aprovação da Fase 3.

## Workflow atual — `validate-template.yml`

Gatilhos: `push` em `main`, `pull_request` e `workflow_dispatch`.

| Etapa | Verificação |
|---|---|
| Estrutura | arquivos obrigatórios, 8 agentes, 14 prompts, 11 skills |
| Adaptadores | paridade de papéis em OpenCode, Claude, Codex e Copilot |
| Herdr | 8 templates `gfm-*` com `name` e `command` |
| Documentos | links relativos, JSON válido, frontmatter |
| YAML | `ai/registry.yaml` com PyYAML |

- Runner: `ubuntu-latest`; Python 3.12; permissões `contents: read`.
- Script: [`scripts/validate-template.py`](../../scripts/validate-template.py).
- Execução local: `python scripts/validate-template.py` (YAML exige PyYAML;
  use `REQUIRE_YAML=1` para tornar a checagem obrigatória).

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
