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
4. Delegar com escopo exato:

```powershell
hc run --bg --name architect --cwd C:\Work\dev\herdr.dev gfm-architect "Escreva a SPEC de <tema>."
hc wait --children all
hc read architect --lines 160
hc send architect "Priorize riscos de segurança."
hc kill architect; hc rm architect
```

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
- Validar OpenCode autenticado dentro do Herdr antes da Fase 4.
- Validar `hc run` com template em runtime antes de declarar homologado.
