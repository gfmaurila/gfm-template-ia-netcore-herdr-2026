# Política de dependências entre camadas

Publicação humana da regra executável [`ai/rules/architecture.md`](../../ai/rules/architecture.md).

## Direção permitida

```text
Host.Api ──► Infrastructure ──► Application ──► Domain
     │                              │
     └──────────────────────────────┘
```

| Projeto | Pode referenciar |
|---|---|
| `Domain` | nada |
| `Application` | `Domain` |
| `Infrastructure` | `Application`, `Domain` |
| `Host.Api` | `Infrastructure`, `Application` |
| `tests/*` | projetos sob teste |

## Proibições

- Ciclos entre projetos ou módulos.
- `Application` referenciar EF Core, ASP.NET Core ou SDK de IA.
- `Domain` conhecer HTTP, serialização ou `ProblemDetails`.
- `Host.Api` acessar `DbContext` diretamente.
- Módulos acessarem entidades internas de outros módulos.

## Verificação

Regras são verificadas por testes de arquitetura, não por disciplina manual. Exceção exige ADR
aprovado e registro na TASK.
