# ai/prompts — prompts versionados

Convenção: `PRM-NNN@versao.md` (versão semântica). Toda execução cita `ID@versao`.

| ID | Versão | Papel | Objetivo |
|---|---|---|---|
| [PRM-001](PRM-001@1.0.0.md) | 1.0.0 | Architect | Descoberta somente leitura |
| [PRM-002](PRM-002@1.0.0.md) | 1.0.0 | Implementer | Implementar unidade com testes |
| [PRM-003](PRM-003@1.0.0.md) | 1.0.0 | Tester | Integração com Testcontainers |
| [PRM-004](PRM-004@1.0.0.md) | 1.0.0 | Reviewer | Revisão de código |
| [PRM-005](PRM-005@1.0.0.md) | 1.0.0 | DevOps | DevOps local-first |
| [PRM-006](PRM-006@1.0.0.md) | 1.0.0 | Architect | ADR |
| [PRM-007](PRM-007@1.0.0.md) | 1.0.0 | Architect | IA opcional e segura |
| [PRM-008](PRM-008@1.0.0.md) | 1.0.0 | Architect | Blueprint de extensão |
| [PRM-009](PRM-009@1.0.0.md) | 1.0.0 | Architect | Escrever SPEC |
| [PRM-010](PRM-010@1.0.0.md) | 1.0.0 | Architect | Escrever PLAN |
| [PRM-011](PRM-011@1.0.0.md) | 1.0.0 | Architect | Decompor em TASKs |
| [PRM-012](PRM-012@1.0.0.md) | 1.0.0 | Docs Writer | Atualizar documentação |
| [PRM-013](PRM-013@1.0.0.md) | 1.0.0 | Security Reviewer | Revisão de segurança |
| [PRM-014](PRM-014@1.0.0.md) | 1.0.0 | Orchestrator | Orquestrar no Herdr |

## Regras

1. Nunca incluir segredos, tokens, PII, dados de cliente ou código proprietário.
2. Mudança de comportamento exige nova versão e nota em
   [`docs/ai/prompt-governance.md`](../../docs/ai/prompt-governance.md).
3. Saída distingue **[verificado]**, **[inferido]** e **[não validado]**.
4. Prompt não concede permissão que a política (`AGENTS.md`, `ai/rules/`) não concede.
5. O índice raiz [`prompts.md`](../../prompts.md) aponta para este diretório.
