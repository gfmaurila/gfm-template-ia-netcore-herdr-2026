# Homologação do template (Ciclo 6)

Data: 2026-11-10. Escopo: template documental e camada de agentes; **sem código C#**.

## Verificado

| Item | Evidência |
|---|---|
| 8 agentes canônicos | frontmatter `name`/`role`; validador |
| 14 prompts versionados | `PRM-NNN@x.y.z`; validador |
| 11 skills + adaptadores | `.opencode/skills` e `.claude/skills` com 11 cada |
| 6 workflows | `ai/workflows/` |
| 5 modelos + TASK | `templates/` e `tasks/TASK-TEMPLATE.md` |
| 6 documentos de governança | `governance/` |
| 8 templates Herdr | `hc templates` lista `gfm-*` |
| Validação estrutural | `python scripts/validate-template.py` exit 0 |
| CI | workflow `validate-template` run 42880682425: success |
| Links relativos | verificados pelo validador |
| YAML | `ai/registry.yaml` válido com PyYAML |
| Sem segredos/PII | revisão manual dos arquivos criados |
| Preservação | `leia.txt` e manual do Herdr não modificados |

## Não validado em runtime

| Item | Motivo |
|---|---|
| Claude Code | CLI ausente no ambiente |
| `hc run` com template | falha `spawn_failed: sh not found` no Windows |
| OpenCode com agente via Herdr | depende do item anterior; TUI não autenticado/testado |
| Codex subagents/skills | formato não exercitado |
| Copilot custom agents | validação estrutural apenas |
| Docker/Compose | daemon parado e sem aplicação |
| Pipeline .NET | bloqueado pela Fase 3 |

## Conclusão

O template está **estruturalmente homologado** e com CI verde. A homologação de
runtime das ferramentas de IA e do pipeline .NET permanece pendente e não pode
ser declarada sem execução comprovada.

## Pendências para a próxima fase

1. Resolver shell do Herdr no Windows (`sh` no PATH ou `shell` no config).
2. Autenticar OpenCode no ambiente do Herdr.
3. Aprovar Fases 2–3 para iniciar código e pipeline .NET.
4. Configurar o Space do projeto no Herdr.
