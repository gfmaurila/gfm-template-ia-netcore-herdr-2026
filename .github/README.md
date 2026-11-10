# .github — adaptador GitHub Copilot e CI

A fonte canônica é [`AGENTS.md`](../AGENTS.md) + [`ai/`](../ai/README.md).

| Caminho | Função |
|---|---|
| [`copilot-instructions.md`](copilot-instructions.md) | Instruções globais do Copilot. |
| [`agents/`](agents/) | Custom agents (`*.agent.md`). |
| [`instructions/`](instructions/) | Instruções por caminho (`*.instructions.md`). |
| [`prompts/`](prompts/) | Prompt files (`*.prompt.md`). |
| [`workflows/validate-template.yml`](workflows/validate-template.yml) | Validação estrutural do template no CI. |

## Limitações verificadas

- Custom agents/instructions/prompts do Copilot são validação estrutural, não runtime.
- O workflow `validate-template.yml` valida o template; o CI de aplicação .NET
  continua planejado para após a Fase 3.
- Divergências: [`docs/ai/multi-tool-matrix.md`](../docs/ai/multi-tool-matrix.md).
