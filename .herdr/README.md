# .herdr — templates, workflows e scripts

Adaptador de orquestração do Herdr. A política vive em `AGENTS.md` e `ai/rules/herdr-operations.md`.

| Caminho | Função |
|---|---|
| `templates/gfm-<papel>.md` | Templates de agente com prefixo `gfm-`. |
| `workflows/` | Fluxos operacionais (ciclo, feature, revisão). |
| `scripts/install-templates.ps1` | Copia os templates para o diretório do Herdr. |

## Instalação (cópia controlada)

```powershell
pwsh -File .herdr/scripts/install-templates.ps1 -WhatIf
pwsh -File .herdr/scripts/install-templates.ps1
```

Destino Windows: `%APPDATA%\herdr-core\templates`. Não instala ferramentas globalmente.

## Execução

```powershell
hc templates
hc run --bg --name architect --cwd C:\Work\dev\herdr.dev gfm-architect "Escreva a SPEC de <tema>."
hc wait --children all
hc read architect --lines 120
hc kill architect; hc rm architect
```

## Limitação verificada (Windows, 10/11/2026)

- `hc templates` lista os 8 templates `gfm-*` após a instalação.
- `hc run ... gfm-<papel> "<tarefa>"` falha com
  `spawn_failed: cannot start "sh": sh: not found on PATH`.
  O Herdr monta a mensagem do template via `sh`; no Windows é necessário ter
  `sh` no PATH (ex.: Git Bash) ou definir `shell` em
  `%APPDATA%\herdr-core\config.toml`.
- Alternativa direta (`hc run ... opencode`) inicia o TUI, mas o argumento
  final é tratado pelo OpenCode 1.19.0 como caminho de projeto; para uso
  one-shot seria `opencode run`. A execução de agentes pelo Herdr permanece
  **não validada em runtime** até resolver o shell.

## Regras

- Um Space por projeto; nunca apontar para repositórios de clientes.
- Codex dentro do Herdr sempre com `--no-daemon`.
- Subagentes não criam novos agentes sem autorização explícita.
- Sem `hc server stop/restart` sem solicitação do responsável.
- Falha de gate ou push interrompe o ciclo.
