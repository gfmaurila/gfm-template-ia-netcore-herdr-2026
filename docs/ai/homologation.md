# Homologação do template (Ciclos 6–8)

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
| Execução de agente primário via Herdr | `run-agent.ps1` com `architect`, `implementer`, `devops`, `orchestrator`: exit 0 e token do papel |
| Execução de subagente via Herdr | `run-agent.ps1` delega `tester`, `reviewer`, `security-reviewer`, `docs-writer` via `orchestrator` + `task`; log `agent=<papel> mode=subagent` |
| Homologação dos 8 papéis | tokens `ARCHITECT_OK`, `IMPLEMENTER_OK`, `TESTER_OK`, `REVIEWER_OK`, `SECURITY_REVIEWER_OK`, `DEVOPS_OK`, `DOCS_WRITER_OK`, `ORCHESTRATOR_OK`; exit 0 |
| Codex CLI | `codex exec ...` respondeu `CODEX_OK`, exit 0; erro de auth do MCP Postman não bloqueante |
| Copilot CLI | `copilot -p ...` respondeu `COPILOT_OK`, exit 0 |
| Herdr | `hc 0.1.19`, `herdr-app 0.1.14`; `hc templates` lista 8 templates `gfm-*` |
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
| `hc run` com template nativo | falha `spawn_failed: sh not found` no Windows; wrapper é o mecanismo oficial |
| OpenCode TUI no Herdr | execução one-shot via wrapper; TUI não exercitado |
| OpenCode subagente via CLI direta | `--agent reviewer` cai no agente padrão (aviso 1.19.0); contornado pelo wrapper via `task` |
| Codex subagents/skills | formato não exercitado |
| Copilot custom agents | validação estrutural apenas |
| Docker/Compose | daemon parado e sem aplicação |
| Pipeline .NET | bloqueado pela Fase 3 |

## Conclusão

O template está **estruturalmente homologado** e com CI verde. O runtime do
OpenCode via Herdr foi homologado para os 8 papéis pelo wrapper one-shot,
incluindo subagentes delegados por `task`; o template nativo no Windows e o TUI
permanecem pendentes. O pipeline .NET não pode ser declarado sem execução
comprovada.

## Pendências para a próxima fase

1. Manter o wrapper como mecanismo oficial no Windows; a correção nativa exige
   `sh` no PATH do core (alteração global sujeita a autorização).
2. Validar o TUI do OpenCode autenticado dentro do Herdr.
3. Aprovar Fases 2–3 para iniciar código e pipeline .NET.
4. Configurar o Space do projeto no Herdr.
