# ai/workflows — fluxos de trabalho

Workflows descrevem fases, gates, artefatos e papéis. São independentes de ferramenta e
referenciam `ai/agents/`, `ai/rules/` e `templates/`.

| ID | Workflow | Entrada | Saída | Gate final |
|---|---|---|---|---|
| WF-01 | [Descoberta](descoberta.md) | workspace/requisito | diagnóstico | relatório |
| WF-02 | [Planejamento](planejamento.md) | requisito | SPEC + ADR + PLAN | aprovação |
| WF-03 | [Feature](feature.md) | TASK autorizada | código + testes + evidência | QG-01..12 |
| WF-04 | [Bugfix](bugfix.md) | falha reproduzível | correção + teste de regressão | QG-01..12 |
| WF-05 | [Revisão](revisao.md) | diff | parecer | aprovação |
| WF-06 | [Bootstrap](bootstrap.md) | template novo | projeto inicial | build + testes |

## Fluxo padrão

```text
SPEC → ADR → PLAN → TASK → IMPLEMENTAÇÃO → TESTES → EVIDÊNCIAS
```

## Regras

1. Nenhum workflow pula gate.
2. Falha de gate interrompe e gera relatório.
3. Cada fase produz artefato rastreável em `docs/` ou `tasks/`.
4. Evidência real é obrigatória para concluir qualquer workflow.
