# ai/skills — habilidades reutilizáveis

Skills são procedimentos reutilizáveis em formato `SKILL.md`, carregados sob demanda por um papel.
A fonte canônica é este diretório; adaptadores copiam o formato exigido por cada ferramenta.

| ID | Skill | Papéis | Estado |
|---|---|---|---|
| spec-writing | Escrever SPEC verificável | Architect | implementada |
| adr-writing | Registrar ADR | Architect | implementada |
| task-decomposition | Decompor em TASKs | Architect | implementada |
| dotnet-clean-architecture | Camadas e dependências .NET | Architect, Implementer | implementada |
| testcontainers-integration | Integração com recurso descartável | Tester | implementada |
| code-review | Revisão estruturada | Reviewer | implementada |
| security-review | Revisão de segurança | Security Reviewer | implementada |
| docker-compose-local | Ambiente local | DevOps | implementada |
| github-actions-ci | Pipeline CI | DevOps | implementada |
| documentation-style | Estilo documental | Docs Writer | implementada |
| herdr-orchestration | Orquestração no Herdr | Orchestrator | implementada |

## Adaptadores

- OpenCode: `.opencode/skills/<id>/SKILL.md`
- Claude Code: `.claude/skills/<id>/SKILL.md`
- Demais ferramentas: referenciam este diretório.

## Formato

```text
skills/<id>/SKILL.md
---
name: <id>
description: <quando usar>
---
<procedimento, checklist e exemplos>
```

## Regras

1. Skill descreve **como fazer**, não redefine política.
2. Toda skill cita as regras aplicáveis de `ai/rules/`.
3. Skill não contém segredos, PII ou dados de cliente.
4. Mudança de comportamento exige revisão no mesmo ciclo dos adaptadores.
