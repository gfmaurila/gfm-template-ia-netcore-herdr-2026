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

## Regras

- Um Space por projeto; nunca apontar para repositórios de clientes.
- Codex dentro do Herdr sempre com `--no-daemon`.
- Subagentes não criam novos agentes sem autorização explícita.
- Sem `hc server stop/restart` sem solicitação do responsável.
- Falha de gate ou push interrompe o ciclo.
