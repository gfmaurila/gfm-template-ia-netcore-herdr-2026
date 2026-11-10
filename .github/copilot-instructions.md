# Instruções para GitHub Copilot

A fonte canônica é [`AGENTS.md`](../AGENTS.md) + [`ai/`](../ai/README.md). Este arquivo apenas
aponta para a política; não a duplica.

## Leitura obrigatória

1. [`AGENTS.md`](../AGENTS.md) — regras inegociáveis, fluxo e gates.
2. [`ai/registry.yaml`](../ai/registry.yaml) — papéis e adaptadores.
3. [`ai/rules/`](../ai/rules/README.md) — regras executáveis.
4. [`docs/ai/multi-tool-matrix.md`](../docs/ai/multi-tool-matrix.md) — diferenças entre ferramentas.

## Resumo operacional

- Fluxo: `SPEC → ADR → PLAN → TASK → IMPLEMENTAÇÃO → TESTES → EVIDÊNCIAS`.
- Sem código C# antes do gate da Fase 3.
- Sem segredos, PII ou dados de cliente.
- Sucesso só com execução comprovada.
- IA opcional e desligada por padrão.

## Adaptadores

- Agentes: [`.github/agents/`](agents/) (`*.agent.md`).
- Instruções por caminho: [`.github/instructions/`](instructions/) (`*.instructions.md`).
- Prompts: [`.github/prompts/`](prompts/) (`*.prompt.md`).

Divergências e limitações: `docs/ai/multi-tool-matrix.md`.
