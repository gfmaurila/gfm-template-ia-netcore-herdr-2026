# .codex — adaptador Codex CLI

A fonte canônica é [`AGENTS.md`](../AGENTS.md) + [`ai/`](../ai/README.md). Este diretório apenas
especializa o formato do Codex CLI.

## Estrutura

| Caminho | Função |
|---|---|
| `.codex/prompts/<papel>.md` | Prompts customizados invocados como `/<papel>`. |
| `.codex/rules/README.md` | Mapeamento das regras canônicas. |

## Uso

- Instruções de projeto: `AGENTS.md` na raiz (formato nativo do Codex).
- Prompt customizado: `/architect <tarefa>`.
- Dentro do Herdr: **sempre** `--no-daemon`.

```powershell
codex --no-daemon
```

## Limitações verificadas

- Subagents e skills nativos do Codex não foram validados em runtime nesta versão (0.163.0).
- Divergência de formato deve ser registrada em
  [`docs/ai/multi-tool-matrix.md`](../docs/ai/multi-tool-matrix.md).
