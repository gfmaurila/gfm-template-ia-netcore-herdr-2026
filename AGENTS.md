# AGENTS.md — Instruções para OpenCode e agentes

Este arquivo é a fonte de verdade para agentes que atuam no workspace `C:\Work\dev\herdr.dev`.
Leia `README.md`, `docs/README.md` e os ADRs antes de propor mudanças.

## 1. Identidade do projeto

- Projeto: **GFM.Template** (template pessoal .NET + IA, independente de empresa/cliente).
- Workspace exclusivo: `C:\Work\dev\herdr.dev`.
- Ferramenta principal: **OpenCode** (1.19.0) dentro do **Herdr** (hc 0.1.19 / app 0.1.14).
- Ferramentas suportadas: OpenCode, Claude Code, Codex CLI e GitHub Copilot (ver `ai/registry.yaml`).
- Estado: documentação (Fases 1–2) + camada de engenharia assistida por IA (Ciclos 1–6).
  **Sem código C# nesta fase.**

## 2. Regras inegociáveis (bloqueantes)

1. Não acessar, alterar ou sobrescrever o GFM.Template anterior nem `C:\Work\dev\template`.
2. Não copiar dados, nomes, regras, código, endpoints, payloads, integrações, credenciais ou
   configurações de Crefisa, GFT, projeto-haf ou projeto-maf.
3. Usar apenas princípios arquiteturais genéricos. É proibido afirmar que arquivos de referência
   foram analisados quando não estavam disponíveis.
4. Preservar `leia.txt` e `MANUAL_HERDR_INSTALACAO_CONFIGURACAO_WINDOWS.txt` (somente leitura).
5. Não executar comandos destrutivos, `git push`, `git init`, instalações globais ou publicação
   sem aprovação explícita do responsável.
6. Não inventar resultados. Sucesso só pode ser declarado com execução comprovada (build/teste/log).
7. Não introduzir segredos, tokens, connection strings reais ou PII no repositório ou em logs.
8. Não gerar código C# antes do gate de aprovação da Fase 3.

## 3. Fatos do ambiente (verificados em 10/11/2026)

- Windows 11 Pro 10.0.26300 (AMD64); PowerShell 5.1 e PowerShell 7.6.9.
- .NET SDK 10.0.402 (único); runtimes 8.0.21 e 10.0.13; sem workloads; sem `global.json`.
- Git 2.55.0.windows.5; repositório local na branch `main`, remoto
  `https://github.com/gfmaurila/gfm-template-ia-netcore-herdr-2026.git`.
- Docker CLI 29.8.2, porém **daemon parado** (`com.docker.service` = Stopped).
- Node 24.20.0 / npm 11.19.0 / OpenCode 1.19.0 / Codex CLI 0.163.0 / Copilot CLI 1.0.108.
- Claude Code CLI **não instalado** (adaptador documentado, não validado em runtime).
- `gh` CLI **não autenticado**; push depende do credential helper `manager`.
- Nenhuma variável de credencial de IA no ambiente.
- Conteúdo do workspace: documentação .NET + IA, camada de agentes e `leia.txt`/manual.

Se algum fato mudar, atualize esta seção com data e evidência — nunca presuma.

## 4. Fluxo de trabalho e gates

| Fase | Atividade | Gate |
|---|---|---|
| 1 | Descoberta e diagnóstico | Relatório apresentado |
| 2 | Documentação e planejamento | **Aprovação dos documentos** |
| 3 | Arquitetura aprovada | **Aprovação explícita** |
| 4 | Implementação por etapas | Build + testes reais por etapa |
| 5 | DevOps e IA opcional | CI verde + evidências |
| 6 | Blueprints | Somente sob solicitação |

Ao final de cada etapa: reportar **o que passou, o que falhou e o que não pôde ser validado**.
Nunca avançar de gate sem aprovação.

## 5. Papéis dos agentes

### 5.1 Architect
- Mantém coerência entre ADRs, specs e código.
- Produz/atualiza ADRs; não implementa features diretamente.
- Questiona complexidade acidental; rejeita abstrações sem caso de uso concreto.
- Saída: decisão + consequências + alternativas descartadas.

### 5.2 Implementer
- Implementa uma unidade pequena por vez, com testes correspondentes.
- Segue `docs/architecture/*` e ADRs; não altera ADR sem passar pelo Architect.
- Nunca declara concluído sem `dotnet build` e `dotnet test` executados.
- Saída: diff resumido + evidência de build/teste.

### 5.3 Tester
- Desenha e implementa testes unitários, integração, arquitetura e contrato.
- Garante banco descartável via Testcontainers, limpeza mesmo em falha (Ryuk).
- Proíbe dependência de banco compartilhado/corporativo/produção.
- Saída: matriz de rastreabilidade requisito → teste + resultado real.

### 5.4 Reviewer
- Revisa segurança, corretude, testabilidade, performance e legibilidade.
- Bloqueia: segredos, PII, SQL concatenado, `async void`, `Task.Result`, catch genérico silencioso,
  dependências circulares entre camadas.
- Saída: achados classificados (bloqueante / recomendado / opcional).

### 5.5 DevOps
- Mantém Dockerfile, Compose e GitHub Actions.
- Segredos apenas via secrets/variáveis de ambiente; nunca no repositório.
- CI sem dependência de serviços corporativos.
- Saída: pipeline + evidência de execução local/equivalentes.

## 6. Convenções técnicas

- TFM `net10.0`; C# 14; `Nullable=enable`; `ImplicitUsings=enable`; file-scoped namespaces.
- `TreatWarningsAsErrors=true`, analyzers habilitados, `dotnet format --verify-no-changes` no CI.
- Async sempre com `CancellationToken`; sufixo `Async`; sem `async void`/`.Result`/`.Wait()`.
- Nomes de tipos em inglês; documentação em pt-BR; texto de API em inglês (a confirmar — Q-08).
- Dependências: `Domain` não referencia ninguém; `Application` → `Domain`;
  `Infrastructure` → `Application`/`Domain`; `Host.Api` → `Infrastructure`/`Application`.
- Organização do código: `src/` divide-se em `src/back-end/` e `src/front-end/`; os projetos
  .NET em camadas ficam sob `src/back-end/`; `src/front-end/` é reservado ao front-end,
  sem tecnologia ou subestrutura definidas nesta fase.
- Regras de camada são verificadas por testes de arquitetura, não por disciplina manual.
- Sem comentários óbvios; comentar apenas decisões não evidentes.
- Sem `MediatR`/`FluentAssertions` por risco de licenciamento (ver ADR-0005/0008).
- Configuração 12-factor via variáveis de ambiente; segredos via user-secrets/CI secrets.

## 7. Comandos padrão (após implementação)

```powershell
dotnet restore
dotnet build --no-restore -warnaserror
dotnet format --verify-no-changes
dotnet test --no-build --logger "console;verbosity=normal"
docker compose -f deploy/compose.yaml up -d --build
docker compose -f deploy/compose.yaml down -v
```

Nenhum desses comandos deve ser executado antes da aprovação da Fase 3.

## 8. Definição de pronto (Definition of Done)

Uma entrega só é aceita quando:

- [ ] Build sem warnings/erros e `dotnet format` limpo.
- [ ] Testes aplicáveis escritos e verdes (unitário, integração, arquitetura, contrato).
- [ ] Integração usa Testcontainers + banco efêmero por execução, com limpeza garantida.
- [ ] Sem segredos/PII; IA opcional e desligada por padrão.
- [ ] Documentação e ADRs atualizados quando a decisão mudar.
- [ ] Evidência real anexada (saída de build/teste), sem afirmações não comprovadas.

## 9. Quando parar e perguntar

Pare e consulte o responsável quando houver: ambiguidade de requisito, escolha de banco,
autenticação, licença, versão de pacote relevante, custo de IA, ou qualquer ação irreversível.
Registre a dúvida em `docs/plans/open-questions.md` em vez de presumir aprovação.

## 10. Camada de engenharia assistida por IA

Este repositório é o **template de engenharia assistida por IA** orquestrado pelo Herdr.

- **Fonte canônica:** `AGENTS.md` (instruções) + `ai/` (agentes, skills, workflows, regras, prompts).
- **Adaptadores:** `.opencode/`, `.claude/`, `.codex/`, `.github/` apenas especializam a fonte
  canônica. Não duplicam política; referenciam `AGENTS.md` e `ai/`.
- **Fluxo obrigatório:** `SPEC → ADR → PLAN → TASK → IMPLEMENTAÇÃO → TESTES → EVIDÊNCIAS`.
- **Papéis:** Architect, Implementer, Tester, Reviewer, Security Reviewer, DevOps, Docs Writer e
  Orchestrator (ver `ai/agents/` e `ai/registry.yaml`).
- **Regras:** `ai/rules/` é a fonte executável; `governance/` publica a política para humanos.
- **Prompts:** `ai/prompts/PRM-NNN@versao.md`; `prompts.md` é o índice.
- **Tasks:** `tasks/` usa o formato único de `tasks/TASK-TEMPLATE.md`.
- **Relatórios:** toda execução de ciclo gera `reports/RELATORIO-AAAA-MM-DD-HHMMSS-NOME.txt`.

## 11. Herdr (orquestração)

- Versão validada: `hc 0.1.19`; templates em `%APPDATA%\herdr-core\templates\<nome>.md`.
- Templates deste template usam prefixo **`gfm-`** (ex.: `gfm-architect`).
- Instalação controlada: `.herdr/scripts/install-templates.ps1` (copia, não instala globalmente).
- Execução: `hc run --bg --name <papel> --cwd <repo> gfm-<papel> "<tarefa>"` quando
  `sh` estiver no PATH do core. No Windows sem `sh`, usar
  `hc run --bg --name <papel> --cwd <repo> powershell -NoProfile -ExecutionPolicy Bypass -File .herdr/scripts/run-agent.ps1 -Role <papel> -Task "<tarefa>"`.
- No wrapper, subagentes (`tester`, `reviewer`, `security-reviewer`, `docs-writer`) são
  delegados pelo `orchestrator` via ferramenta `task`; a CLI do OpenCode 1.19.0 não os
  seleciona diretamente com `--agent`.
- Acompanhamento: `hc wait --children`, `hc read`, `hc send`, `hc get`; limpeza: `hc kill`/`hc rm`.
- Codex dentro do Herdr **deve** rodar com `--no-daemon`.
- Um Space por projeto; agentes não apontam para repositórios de clientes.

## 12. Catálogo de agentes e adaptadores

| Papel | Canônico | OpenCode | Claude Code | Codex | Copilot |
|---|---|---|---|---|---|
| Architect | `ai/agents/architect.md` | `.opencode/agents/architect.md` | `.claude/agents/architect.md` | `.codex/prompts/architect.md` | `.github/agents/architect.agent.md` |
| Implementer | `ai/agents/implementer.md` | `.opencode/agents/implementer.md` | `.claude/agents/implementer.md` | `.codex/prompts/implementer.md` | `.github/agents/implementer.agent.md` |
| Tester | `ai/agents/tester.md` | `.opencode/agents/tester.md` | `.claude/agents/tester.md` | `.codex/prompts/tester.md` | `.github/agents/tester.agent.md` |
| Reviewer | `ai/agents/reviewer.md` | `.opencode/agents/reviewer.md` | `.claude/agents/reviewer.md` | `.codex/prompts/reviewer.md` | `.github/agents/reviewer.agent.md` |
| Security Reviewer | `ai/agents/security-reviewer.md` | `.opencode/agents/security-reviewer.md` | `.claude/agents/security-reviewer.md` | `.codex/prompts/security-reviewer.md` | `.github/agents/security-reviewer.agent.md` |
| DevOps | `ai/agents/devops.md` | `.opencode/agents/devops.md` | `.claude/agents/devops.md` | `.codex/prompts/devops.md` | `.github/agents/devops.agent.md` |
| Docs Writer | `ai/agents/docs-writer.md` | `.opencode/agents/docs-writer.md` | `.claude/agents/docs-writer.md` | `.codex/prompts/docs-writer.md` | `.github/agents/docs-writer.agent.md` |
| Orchestrator | `ai/agents/orchestrator.md` | `.opencode/agents/orchestrator.md` | `.claude/agents/orchestrator.md` | `.codex/prompts/orchestrator.md` | `.github/agents/orchestrator.agent.md` |

Regras de adaptação:

1. Mudança de comportamento começa em `ai/` e é propagada aos adaptadores no mesmo ciclo.
2. Formato de frontmatter segue a versão **instalada** de cada ferramenta; divergência é registrada
   em `docs/ai/multi-tool-matrix.md`.
3. Ferramenta indisponível (ex.: Claude Code CLI ausente) permanece documentada, mas **não
   validada em runtime**.

## 13. Relatórios, evidências e Git

- Formato: `reports/RELATORIO-AAAA-MM-DD-HHMMSS-NOME-DO-CICLO.txt`.
- Conteúdo mínimo: objetivo, agentes, atividades, arquivos, comandos, validações, erros, decisões,
  riscos, status, branch/publicação e próximos passos.
- Evidência > afirmação: comandos e saídas reais; distinguir **verificado**, **inferido** e
  **não validado**.
- Commits: mensagem `tipo(escopo): descricao` (ex.: `feat(ai): fundacao canonica`).
- Proibido `git push --force`, reescrita de histórico publicado ou commit de segredos.
- Se o push falhar: preservar o commit local e interromper para diagnóstico.

## 14. Limites desta fase (template de agentes)

- **Não** gerar aplicação C#, `src/` executável ou migrations nesta fase.
- **Não** instalar ferramentas globalmente, alterar PATH permanente ou publicar pacotes.
- **Não** copiar conteúdo de clientes nem material proprietário do repositório de referência.
- **Não** declarar homologação sem as validações do Ciclo 6 executadas.
