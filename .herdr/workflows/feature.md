# Workflow — feature

## Fases

| Fase | Papel | Artefato | Gate |
|---|---|---|---|
| 1 | Architect | SPEC | aprovação da SPEC |
| 2 | Architect | ADR (se estrutural) | aprovação do ADR |
| 3 | Architect | PLAN + TASKs | TASK autorizada |
| 4 | Implementer | código + testes | build + testes |
| 5 | Tester | testes adicionais | matriz requisito → teste |
| 6 | Reviewer | parecer | QG-01..12 |
| 7 | Security Reviewer | parecer | risco residual aceito |

## Comandos

```powershell
hc run --bg --name architect --cwd <repo> gfm-architect "SPEC de <feature>"
hc wait --children all
hc run --bg --name implementer --cwd <repo> gfm-implementer "TASK-<AREA>-NNN"
hc wait --children all
hc run --bg --name tester --cwd <repo> gfm-tester "Cobrir TASK-<AREA>-NNN"
hc wait --children all
hc run --bg --name reviewer --cwd <repo> gfm-reviewer "Revise o diff da TASK-<AREA>-NNN"
hc wait --children all
```

No Windows sem `sh` no PATH do core, use
`powershell -NoProfile -ExecutionPolicy Bypass -File .herdr/scripts/run-agent.ps1 -Role <papel> -Task "<escopo>"`
no lugar de `gfm-<papel> "<escopo>"`.

## Regra

Nenhuma fase começa sem evidência da anterior. Falha de teste bloqueia revisão.
