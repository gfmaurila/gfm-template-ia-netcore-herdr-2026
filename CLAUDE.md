# CLAUDE.md — adaptador Claude Code

Este arquivo **não** define política própria. A fonte canônica é [`AGENTS.md`](AGENTS.md),
complementada por `ai/` (agentes, skills, workflows, regras e prompts).

## Leitura obrigatória

1. [`AGENTS.md`](AGENTS.md) — regras inegociáveis, fluxo e gates.
2. [`ai/registry.yaml`](ai/registry.yaml) — catálogo de papéis e adaptadores.
3. [`ai/rules/`](ai/rules/README.md) — regras executáveis.
4. [`docs/ai/multi-tool-matrix.md`](docs/ai/multi-tool-matrix.md) — diferenças entre ferramentas.

## Uso no Claude Code

- Subagentes nativos: `.claude/agents/<papel>.md` (frontmatter `name`, `description`, `tools`, `model`).
- Comandos: `.claude/commands/<nome>.md`.
- Skills: `.claude/skills/<id>/SKILL.md`.
- Regras de projeto: `CLAUDE.md` + `AGENTS.md` (este repositório não usa `.claude/rules/` como
  mecanismo nativo; as regras vivem em `ai/rules/`).

## Limitações verificadas

- O Claude Code CLI **não está instalado** neste ambiente (10/11/2026). Os arquivos são
  estruturalmente válidos, mas **não validados em runtime**.
- Não replique conteúdo de `ai/` aqui. Em caso de divergência, prevalece `AGENTS.md`.
