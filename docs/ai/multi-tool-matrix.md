# Matriz multi-ferramenta

Diferenças entre as ferramentas suportadas. A fonte canônica é `AGENTS.md` + `ai/`; os adaptadores
apenas especializam formato. Divergência de frontmatter segue a versão **instalada**.

| Capacidade | OpenCode | Claude Code | Codex | Copilot |
|---|---|---|---|---|
| Instruções | `AGENTS.md` | `CLAUDE.md` + `AGENTS.md` | `AGENTS.md` | `.github/copilot-instructions.md` |
| Agentes | `.opencode/agents/*.md` | `.claude/agents/*.md` | `.codex/prompts/*.md` | `.github/agents/*.agent.md` |
| Comandos | `.opencode/commands/*.md` | `.claude/commands/*.md` | prompts | `.github/prompts/*.prompt.md` |
| Skills | `.opencode/skills/<id>/SKILL.md` | `.claude/skills/<id>/SKILL.md` | a validar | `.github/instructions/*.instructions.md` |
| Config | `.opencode/opencode.json` | `settings.json` | `config.toml` | repositório |
| Versão validada | 1.19.0 | ausente | 0.163.0 | não validado |

## Observações

1. OpenCode 1.19.0 usa o formato V1 (`agents/`, `permission` singular). A documentação pública pode
   mostrar V2; validar contra o schema instalado antes de ativar.
2. Claude Code CLI **não está instalado** neste ambiente: adaptador estrutural, sem validação runtime.
3. Codex dentro do Herdr **deve** rodar com `--no-daemon`.
4. Copilot: custom agents/instructions são validação estrutural, não runtime.
5. Qualquer divergência encontrada deve ser registrada aqui com data e evidência.
6. Skills canônicas estão em `ai/skills/`; OpenCode e Claude recebem cópia, Codex e Copilot
   referenciam o diretório canônico. Carregamento em runtime não foi exercitado.
7. Templates Herdr `gfm-*` são carregados por `hc templates`; a execução via `hc run` falha no
   Windows por ausência de `sh` (ver `.herdr/README.md`).
