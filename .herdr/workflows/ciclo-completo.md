# Workflow — ciclo completo

## Pré-condições

- Objetivo do ciclo definido e aprovado.
- Templates instalados (`hc templates` lista `gfm-*`).
- Repositório limpo ou mudanças conhecidas.

## Sequência

```text
1. Orchestrator monta o plano de delegação.
2. hc run --bg --name architect --cwd <repo> gfm-architect "<escopo>"
3. hc wait --children all
4. hc read architect --lines 160
5. Se gate de documento falhar, interromper e reportar.
6. Delegar implementação/teste/revisão conforme o plano.
7. Consolidar evidências em reports/RELATORIO-<timestamp>-<CICLO>.txt.
8. Commit/push somente com autorização e gates verdes.
9. hc kill <t>; hc rm <t> para cada terminal criado.
```

## Saída

- Relatório do ciclo com objetivo, agentes, arquivos, comandos, validações, erros,
  decisões, riscos, status e próximos passos.
- Lista do que passou, falhou e não pôde ser validado.
