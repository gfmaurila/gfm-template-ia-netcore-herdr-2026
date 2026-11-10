# ai/skills — habilidades reutilizáveis

Skills são procedimentos reutilizáveis em formato `SKILL.md`, carregados sob demanda por um papel.
A fonte canônica é este diretório; adaptadores copiam o formato exigido por cada ferramenta.

| ID | Skill | Papéis | Estado |
|---|---|---|---|
| spec-writing | Escrever SPEC verificável | Architect | planejada |
| adr-writing | Registrar ADR | Architect | planejada |
| task-decomposition | Decompor em TASKs | Architect | planejada |
| dotnet-clean-architecture | Camadas e dependências .NET | Architect, Implementer | planejada |
| testcontainers-integration | Integração com recurso descartável | Tester | planejada |
| code-review | Revisão estruturada | Reviewer | planejada |
| security-review | Revisão de segurança | Security Reviewer | planejada |
| docker-compose-local | Ambiente local | DevOps | planejada |
| github-actions-ci | Pipeline CI | DevOps | planejada |
| documentation-style | Estilo documental | Docs Writer | planejada |
| herdr-orchestration | Orquestração no Herdr | Orchestrator | planejada |

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
