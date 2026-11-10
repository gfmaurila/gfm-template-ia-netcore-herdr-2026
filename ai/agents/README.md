# ai/agents — papéis canônicos

Oito papéis independentes de ferramenta. Cada arquivo usa frontmatter com `id`, `mode`,
`permissions`, `inputs`, `outputs` e `acceptance`, seguido do corpo com missão, responsabilidades,
restrições, processo, handoff e evidências.

| Papel | Arquivo | Modo | Pode editar | Pode delegar |
|---|---|---|---|---|
| Architect | [`architect.md`](architect.md) | primary | ask | sim |
| Implementer | [`implementer.md`](implementer.md) | primary | allow | não |
| Tester | [`tester.md`](tester.md) | subagent | allow | não |
| Reviewer | [`reviewer.md`](reviewer.md) | subagent | deny | não |
| Security Reviewer | [`security-reviewer.md`](security-reviewer.md) | subagent | deny | não |
| DevOps | [`devops.md`](devops.md) | primary | allow | não |
| Docs Writer | [`docs-writer.md`](docs-writer.md) | subagent | allow | não |
| Orchestrator | [`orchestrator.md`](orchestrator.md) | primary | deny | sim |

## Regras

1. A fonte canônica é este diretório; os adaptadores apenas especializam formato.
2. Permissões são intenção de política; a aplicação efetiva depende da ferramenta.
3. Nenhum agente aprova em nome do responsável humano.
4. Handoffs devem citar TASK, artefatos e evidências.
