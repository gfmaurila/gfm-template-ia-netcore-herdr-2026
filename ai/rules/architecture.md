# Regras de arquitetura

Fonte executável. A política publicada para humanos está em
[`governance/architecture/dependency-policy.md`](../../governance/architecture/dependency-policy.md).

| ID | Regra | Verificação |
|---|---|---|
| R-ARCH-001 | `Domain` não referencia nenhum outro projeto. | ArchitectureTests |
| R-ARCH-002 | `Application` referencia apenas `Domain`. | ArchitectureTests |
| R-ARCH-003 | `Infrastructure` referencia `Application` e `Domain`. | ArchitectureTests |
| R-ARCH-004 | `Host.Api` referencia `Infrastructure` e `Application`. | ArchitectureTests |
| R-ARCH-005 | Proibido ciclo entre projetos ou módulos. | ArchitectureTests |
| R-ARCH-006 | `Application` não referencia EF Core, ASP.NET Core ou SDK de IA. | ArchitectureTests |
| R-ARCH-007 | `Host.Api` não acessa `DbContext` diretamente. | Revisão + teste |
| R-ARCH-008 | `Domain` não conhece HTTP, `ProblemDetails` nem serialização. | ArchitectureTests |
| R-ARCH-009 | Módulos conversam por contratos/DTOs, não por entidades internas. | Revisão |
| R-ARCH-010 | Exceção a estas regras exige ADR aprovado. | Revisão |

## Critério de bloqueio

Violação de R-ARCH-001..008 bloqueia merge. Violação de R-ARCH-009/010 bloqueia até ADR.
