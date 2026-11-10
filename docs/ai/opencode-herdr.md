# OpenCode dentro do Herdr

## Ambiente verificado (10/11/2026)

| Item | Valor |
|---|---|
| Herdr App | 0.1.14 |
| Herdr Core (`hc`) | 0.1.19 |
| OpenCode | 1.19.0 |
| Codex CLI | 0.163.0 (`--no-daemon` no Herdr) |
| Claude Code CLI | ausente (não validado em runtime) |
| Workspace | `C:\Work\dev\herdr.dev` |
| Templates | `%APPDATA%\herdr-core\templates` |
| `sh` no PATH | ausente (Git Bash em `C:\Program Files\Git\bin`) |

- `hc`, `herdr-core` e `herdr-app` resolvem no PATH.
- Nenhuma variável de credencial de IA presente no ambiente.
- `hc templates` lista os 8 templates `gfm-*` após a instalação controlada
  (verificado em 10/11/2026).

## Instalação dos templates

```powershell
pwsh -File .herdr/scripts/install-templates.ps1 -WhatIf
pwsh -File .herdr/scripts/install-templates.ps1
hc templates
```

O script copia apenas `.herdr/templates/gfm-*.md` para o diretório do Herdr; não instala
ferramentas globalmente. Use `-Force` para sobrescrever.

## Templates disponíveis

| Template | Papel | Comando |
|---|---|---|
| `gfm-architect` | Architect | `opencode --agent architect` |
| `gfm-implementer` | Implementer | `opencode --agent implementer` |
| `gfm-tester` | Tester | `opencode --agent tester` |
| `gfm-reviewer` | Reviewer | `opencode --agent reviewer` |
| `gfm-security-reviewer` | Security Reviewer | `opencode --agent security-reviewer` |
| `gfm-devops` | DevOps | `opencode --agent devops` |
| `gfm-docs-writer` | Docs Writer | `opencode --agent docs-writer` |
| `gfm-orchestrator` | Orchestrator | `opencode --agent orchestrator` |

Para usar Codex em um template, altere o `command` para `codex --no-daemon` na cópia instalada.
Não edite a fonte em `.herdr/templates/` sem revisar `ai/rules/herdr-operations.md`.

## Uso recomendado

1. Abrir/criar um **Space** no Herdr apontando para `C:\Work\dev\herdr.dev`.
2. Abrir terminal nesse Space.
3. Instalar templates e confirmar com `hc templates`.
4. Delegar com escopo exato.

Em Linux/macOS ou Windows com `sh` no PATH do core, use o template nativo:

```powershell
hc run --bg --name architect --cwd C:\Work\dev\herdr.dev gfm-architect "Escreva a SPEC de <tema>."
hc wait --children all
hc read architect --lines 160
hc send architect "Priorize riscos de segurança."
hc kill architect; hc rm architect
```

No Windows sem `sh` no PATH do core, use o wrapper validado:

```powershell
hc run --bg --name architect --cwd C:\Work\dev\herdr.dev powershell -NoProfile -ExecutionPolicy Bypass -File .herdr/scripts/run-agent.ps1 -Role architect -Task "Escreva a SPEC de <tema>."
hc wait --children all
hc read architect --lines 160
hc send architect "Priorize riscos de segurança."
hc kill architect; hc rm architect
```

O wrapper lê o template canônico, preserva o corpo e o agente, e executa o papel.
Agentes primários (`architect`, `implementer`, `devops`, `orchestrator`) usam
`opencode run --agent <papel>` com corpo + tarefa. Subagentes (`tester`,
`reviewer`, `security-reviewer`, `docs-writer`) são delegados pelo wrapper via
`orchestrator` e ferramenta `task`, com o corpo do template e a tarefa
repassados ao subagente. `-DryRun` mostra o comando sem executar. Não crie
shim/executável falso de `sh`.

**Limitação de subagentes:** no OpenCode 1.19.0, `opencode run --agent <subagente>`
emite `agent "<papel>" is a subagent, not a primary agent` e usa o agente padrão.
O wrapper contorna a limitação delegando esses papéis pelo `orchestrator`; o log
do OpenCode registra `agent=<papel> mode=subagent` para cada um. Os 8 papéis
foram homologados em 10/11/2026 (ver `reports/RELATORIO-FINAL-HOMOLOGACAO-HERDR.txt`).

## Fluxo com agentes

| Papel | Prompt | Saída esperada |
|---|---|---|
| Architect | `PRM-001`, `PRM-006`, `PRM-009`, `PRM-010` | diagnóstico, SPEC, ADR, PLAN |
| Implementer | `PRM-002` | diff + build/teste |
| Tester | `PRM-003` | testes + resultado |
| Reviewer | `PRM-004` | achados classificados |
| Security Reviewer | `PRM-013` | achados + risco residual |
| DevOps | `PRM-005` | Docker/CI + evidência |
| Docs Writer | `PRM-012` | documentação + links |
| Orchestrator | `PRM-014` | delegação + relatório |

## Workflows operacionais

- [`ciclo-completo`](../../.herdr/workflows/ciclo-completo.md) — delegação e relatório.
- [`feature`](../../.herdr/workflows/feature.md) — SPEC → TASK → testes → revisão.
- [`revisao`](../../.herdr/workflows/revisao.md) — revisão e segurança.

## Regras de convivência

- Um Space por projeto; este workspace é exclusivo do GFM.Template.
- Nunca apontar agentes para `C:\Work\dev\template` ou repositórios de clientes.
- Sempre `hc run --bg` para agentes; sem `--bg` a tela vaza no output.
- Codex dentro do Herdr **sempre** com `--no-daemon`.
- Subagentes não iniciam outros agentes sem autorização explícita.
- Commits/push apenas com autorização explícita.
- Falha de gate ou push interrompe o ciclo para diagnóstico.
- Preservar `leia.txt` e o manual do Herdr (somente leitura).

## Diagnóstico do Herdr (somente leitura)

```powershell
hc --version
hc templates
Get-Command herdr-app
$env:PATH -split ';' | Where-Object { $_ -match 'herdr' }
```

Se `hc` não for reconhecido em uma nova sessão, ver manual do Herdr, seção 4
(atualização do PATH apenas na sessão atual).

## Pendências

- Space do projeto ainda não configurado (manual, checklist item 201).
- OpenCode autenticado dentro do Herdr: os 8 papéis foram homologados pelo
  wrapper em 10/11/2026 (tokens de papel, exit 0 e log
  `agent=<papel> mode=primary|subagent`). O TUI nativo ainda não foi exercitado.
- `hc run` com template nativo continua **bloqueado** no Windows: falha com
  `spawn_failed: cannot start "sh"`. `shell` no config não resolve templates.
  A correção nativa exige `sh` no PATH do core (alteração global sujeita a
  autorização). O wrapper `scripts/run-agent.ps1` é o caminho oficial validado.
  `hc templates` funciona e lista os 8 templates.
