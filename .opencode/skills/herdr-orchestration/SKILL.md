---
name: herdr-orchestration
description: Use when delegating work to Herdr agents with hc run --bg, hc wait, hc send and hc read, respecting gates, scopes and cleanup.
---

# herdr-orchestration

## Quando usar

- Executar um ciclo com múltiplos papéis.
- Delegar uma revisão ou implementação isolada.

## Passos

1. Confirmar objetivo, TASK e gate.
2. Montar plano de delegação (papel, escopo, saída).
3. Verificar templates com `hc templates`.
4. Iniciar com `hc run --bg --name <n> --cwd <repo> gfm-<papel> "<escopo>"`.
5. Aguardar com `hc wait --children all`.
6. Ler com `hc read <n> --lines 160`.
7. Coletar resultados e verificar evidências.
8. Limpar com `hc kill <n>; hc rm <n>`.

## Checklist

- [ ] Escopo exato na primeira mensagem.
- [ ] Nenhum agente inicia outro sem autorização.
- [ ] Codex com `--no-daemon`.
- [ ] Nenhum `hc server stop/restart` sem solicitação.
- [ ] Relatório consolidado com evidências.

## Referências

- `ai/rules/herdr-operations.md`
- `ai/prompts/PRM-014@1.0.0.md`
- `.herdr/workflows/ciclo-completo.md`
