# Regras de código

| ID | Regra |
|---|---|
| R-CODE-001 | Nomes de tipos, membros e APIs em inglês; documentação em pt-BR. |
| R-CODE-002 | `Nullable=enable`, `ImplicitUsings=enable`, file-scoped namespaces. |
| R-CODE-003 | `TreatWarningsAsErrors=true` e analyzers habilitados. |
| R-CODE-004 | Async de ponta a ponta com `CancellationToken`; sufixo `Async`. |
| R-CODE-005 | Proibido `async void`, `.Result`, `.Wait()` e `GetAwaiter().GetResult()`. |
| R-CODE-006 | Proibido catch genérico que engole erro ou retorna sucesso. |
| R-CODE-007 | Sem comentários óbvios; comentar apenas decisão não evidente. |
| R-CODE-008 | Sem abstração genérica sem caso de uso concreto. |
| R-CODE-009 | Validação na fronteira; domínio não valida HTTP. |
| R-CODE-010 | Logs estruturados, sem segredos, tokens ou PII. |
| R-CODE-011 | SQL sempre parametrizado; proibido concatenar entrada. |
| R-CODE-012 | Formatação é automatizada (`dotnet format`), não discutida em revisão. |

## Aplicação

- Regras 001–003 são verificadas por configuração de build.
- Regras 004–006 são bloqueantes em revisão e analyzers.
- Regras 010–011 são bloqueantes em revisão de segurança.
