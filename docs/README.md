# Documentação — GFM.Template

Índice da documentação. Tudo aqui descreve o **planejado**; código ainda não foi gerado.

## Comece por

1. [`../README.md`](../README.md) — visão geral e ambiente.
2. [`../AGENTS.md`](../AGENTS.md) — regras para agentes e gates.
3. [`plans/implementation-plan.md`](plans/implementation-plan.md) — etapas e aprovação.
4. [`plans/open-questions.md`](plans/open-questions.md) — decisões que dependem de você.

## Mapa de diretórios

| Diretório | Conteúdo |
|---|---|
| [`architecture/`](architecture/overview.md) | Visão, camadas, modularidade, cross-cutting |
| [`adr/`](adr/README.md) | Decisões arquiteturais registradas |
| [`specifications/`](specifications/sample-domain.md) | Domínio de exemplo, requisitos não funcionais, IA |
| [`plans/`](plans/implementation-plan.md) | Plano por etapas e perguntas abertas |
| [`tasks/`](tasks/backlog.md) | Backlog rastreável |
| [`testing/`](testing/strategy.md) | Estratégia de testes e Testcontainers |
| [`security/`](security/security-baseline.md) | Baseline de segurança e proteção de dados em IA |
| [`devops/`](devops/local-development.md) | Desenvolvimento local, Docker, CI/CD |
| [`ai/`](ai/opencode-herdr.md) | OpenCode no Herdr e governança de prompts |
| [`blueprints/`](blueprints/api.md) | Extensões: API, Worker/Batch, compostas, IA |

## Status

| Fase | Estado |
|---|---|
| 1 — Descoberta | Concluída (evidências no README) |
| 2 — Documentação e planejamento | Concluída |
| 3 — Arquitetura | Proposta; aguarda aprovação |
| 4+ — Implementação | **Bloqueada** até aprovação explícita |

## Princípios

- Sem dados de cliente; domínio de exemplo neutro.
- Sem segredos no repositório.
- Sem sucesso declarado sem execução comprovada.
- Simplicidade primeiro; abstração só com necessidade demonstrada.
