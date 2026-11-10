# Regras de operação no Herdr

| ID | Regra |
|---|---|
| R-HC-001 | Um Space por projeto; nunca apontar agentes para repositórios de clientes. |
| R-HC-002 | Templates usam prefixo `gfm-` e vivem em `.herdr/templates/`. |
| R-HC-003 | Instalação de template é cópia controlada, não instalação global de ferramenta. |
| R-HC-004 | Agentes rodam com `hc run --bg`; sem `--bg`, a tela inteira vaza no output. |
| R-HC-005 | Toda delegação tem escopo exato e critério de conclusão. |
| R-HC-006 | Codex dentro do Herdr roda com `--no-daemon`. |
| R-HC-007 | Não permitir que subagentes criem novos agentes sem autorização explícita. |
| R-HC-008 | Aguardar com `hc wait`, nunca com sleep/polling manual. |
| R-HC-009 | Limpar apenas terminais criados pelo próprio agente (`hc kill`, `hc rm`). |
| R-HC-010 | `hc server stop/restart` só com solicitação explícita do responsável. |
| R-HC-011 | Falha de push ou de gate interrompe o ciclo para diagnóstico. |

## Comandos de referência

```powershell
hc templates
hc run --bg --name review --cwd C:\Work\dev\herdr.dev gfm-reviewer "Revise o diff atual."
hc wait --children all
hc read review --lines 120
hc send review "Priorize bloqueantes."
hc kill review; hc rm review
```
