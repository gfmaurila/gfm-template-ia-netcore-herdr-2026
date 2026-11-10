# .github — adaptador GitHub Copilot e CI

A fonte canônica é [`AGENTS.md`](../AGENTS.md) + [`ai/`](../ai/README.md).

| Caminho | Função |
|---|---|
| [`copilot-instructions.md`](copilot-instructions.md) | Instruções globais do Copilot. |
| [`agents/`](agents/) | Custom agents (`*.agent.md`). |
| [`instructions/`](instructions/) | Instruções por caminho (`*.instructions.md`). |
| [`prompts/`](prompts/) | Prompt files (`*.prompt.md`). |
| `workflows/` | CI (Ciclo 5). |

## Limitações verificadas

- Custom agents/instructions/prompts do Copilot são validação estrutural, não runtime.
- O CI será criado no Ciclo 5; não há workflow neste ciclo.
- Divergências: [`docs/ai/multi-tool-matrix.md`](../docs/ai/multi-tool-matrix.md).
