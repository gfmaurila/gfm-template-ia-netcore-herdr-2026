# .herdr/workflows — fluxos operacionais

Fluxos que combinam templates, gates e comandos do Herdr. A política está em
[`ai/workflows/README.md`](../../ai/workflows/README.md) e
[`ai/rules/herdr-operations.md`](../../ai/rules/herdr-operations.md).

| Workflow | Quando usar | Papéis |
|---|---|---|
| [ciclo-completo](ciclo-completo.md) | Executar um ciclo com delegação e relatório. | Orchestrator → papéis |
| [feature](feature.md) | Entregar uma feature com SPEC → TASK → testes. | Architect → Implementer → Tester → Reviewer |
| [revisao](revisao.md) | Revisar diff antes de commit/merge. | Reviewer → Security Reviewer |

## Regras comuns

1. Sempre `hc run --bg` e `hc wait --children all`.
2. Primeira mensagem contém o escopo exato.
3. Cada agente reporta com `hc send` ao pai.
4. Falha de gate interrompe; não avançar por suposição.
5. Limpar apenas terminais criados pelo próprio agente.
