# prompts.md — índice de prompts versionados

A biblioteca de prompts vive em [`ai/prompts/`](ai/prompts/README.md), no formato
`PRM-NNN@versao.md`. Este arquivo é apenas o índice.

## Convenções

- Toda execução de agente cita o ID + versão (ex.: `PRM-002@1.0.0`).
- Mudança de comportamento exige nova versão + nota em
  [`docs/ai/prompt-governance.md`](docs/ai/prompt-governance.md).
- Nunca incluir segredos, tokens, PII, dados de cliente ou código proprietário.
- Saída distingue **[verificado]**, **[inferido]** e **[não validado]**.
- Prompt não concede permissão que `AGENTS.md` e `ai/rules/` não concedem.

## Catálogo

| ID | Versão | Papel | Objetivo |
|---|---|---|---|
| PRM-001 | 1.0.0 | Architect | Descoberta somente leitura |
| PRM-002 | 1.0.0 | Implementer | Implementar unidade com testes |
| PRM-003 | 1.0.0 | Tester | Integração com Testcontainers |
| PRM-004 | 1.0.0 | Reviewer | Revisão de código |
| PRM-005 | 1.0.0 | DevOps | DevOps local-first |
| PRM-006 | 1.0.0 | Architect | ADR |
| PRM-007 | 1.0.0 | Architect | IA opcional e segura |
| PRM-008 | 1.0.0 | Architect | Blueprint de extensão |
| PRM-009 | 1.0.0 | Architect | Escrever SPEC |
| PRM-010 | 1.0.0 | Architect | Escrever PLAN |
| PRM-011 | 1.0.0 | Architect | Decompor em TASKs |
| PRM-012 | 1.0.0 | Docs Writer | Atualizar documentação |
| PRM-013 | 1.0.0 | Security Reviewer | Revisão de segurança |
| PRM-014 | 1.0.0 | Orchestrator | Orquestrar no Herdr |

Detalhes e texto completo: [`ai/prompts/README.md`](ai/prompts/README.md).
