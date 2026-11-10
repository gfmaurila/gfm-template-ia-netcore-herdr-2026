# .herdr — templates, workflows e scripts

Adaptador de orquestração do Herdr. A política vive em `AGENTS.md` e `ai/rules/herdr-operations.md`.

| Caminho | Função |
|---|---|
| `templates/gfm-<papel>.md` | Templates de agente com prefixo `gfm-`. |
| `workflows/` | Fluxos operacionais (ciclo, feature, revisão). |
| `scripts/install-templates.ps1` | Copia os templates para o diretório do Herdr. |
| `scripts/run-agent.ps1` | Executa um papel via OpenCode sem depender de `sh` (Windows). |

## Instalação (cópia controlada)

```powershell
pwsh -File .herdr/scripts/install-templates.ps1 -WhatIf
pwsh -File .herdr/scripts/install-templates.ps1
```

Destino Windows: `%APPDATA%\herdr-core\templates`. Não instala ferramentas globalmente.

## Execução

Em Linux/macOS ou Windows com `sh` no PATH do core, use o template nativo:

```powershell
hc templates
hc run --bg --name architect --cwd C:\Work\dev\herdr.dev gfm-architect "Escreva a SPEC de <tema>."
hc wait --children all
hc read architect --lines 120
hc kill architect; hc rm architect
```

No Windows sem `sh` no PATH do core, use o wrapper validado:

```powershell
hc run --bg --name architect --cwd C:\Work\dev\herdr.dev powershell -NoProfile -ExecutionPolicy Bypass -File .herdr/scripts/run-agent.ps1 -Role architect -Task "Escreva a SPEC de <tema>."
hc wait --children all
hc read architect --lines 120
hc kill architect; hc rm architect
```

O wrapper lê `.herdr/templates/gfm-<papel>.md`, valida o comando
`opencode --agent <papel>` e executa `opencode run` com o corpo do template e a
tarefa. Use `-DryRun` para mostrar o comando sem executar.

## Limitação verificada (Windows, 10/11/2026)

- `hc templates` lista os 8 templates `gfm-*` após a instalação.
- `hc run ... gfm-<papel> "<tarefa>"` falha com
  `spawn_failed: cannot start "sh": sh: not found on PATH`.
- Causa: o caminho de template do Herdr usa `sh` literal no Windows.
  `shell` em `%APPDATA%\herdr-core\config.toml` afeta terminais interativos,
  mas **não** templates; testado com `shell = ["cmd", "/d", "/s", "/c"]` e com
  `shell = ["C:\\Program Files\\Git\\bin\\sh.exe"]`.
- O core do Herdr reconstrói o PATH a partir do registro do Windows; prefixar o
  PATH do processo que inicia o core não é suficiente.
- Correção nativa exige `sh` no PATH visível pelo core (ex.: adicionar
  `C:\Program Files\Git\bin` ao PATH do usuário e reiniciar o core). Isso é uma
  alteração global e depende de autorização explícita.
- Workaround validado em 10/11/2026: `scripts/run-agent.ps1` via
  `hc run ... powershell ...`, sem `sh`, com resposta real do agente OpenCode.
- OpenCode 1.19.0: `--agent <subagente>` cai no agente padrão
  (`agent ... is a subagent, not a primary agent`). O runtime validado é o de
  agente primário (`architect`); subagentes exigem fluxo via `task`.

## Regras

- Um Space por projeto; nunca apontar para repositórios de clientes.
- Codex dentro do Herdr sempre com `--no-daemon`.
- Subagentes não criam novos agentes sem autorização explícita.
- Sem `hc server stop/restart` sem solicitação do responsável.
- No Windows sem `sh` no PATH do core, usar `scripts/run-agent.ps1`; não criar
  shim ou executável falso de `sh`.
- Falha de gate ou push interrompe o ciclo.
