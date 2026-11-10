---
name: dotnet-clean-architecture
description: Use when designing or reviewing .NET projects with Domain/Application/Infrastructure/Host.Api layering, dependency rules and testable boundaries.
---

# dotnet-clean-architecture

## Quando usar

- Criar estrutura de projetos .NET.
- Revisar limites de camada e dependências.
- Decidir onde uma responsabilidade vive.

## Regras de dependência

```text
Domain          → nada
Application     → Domain
Infrastructure  → Application, Domain
Host.Api        → Infrastructure, Application
```

## Passos

1. Identificar entidades e regras de domínio.
2. Definir casos de uso na Application, sem dependência de infraestrutura.
3. Implementar adaptadores na Infrastructure.
4. Expor entrada em Host.Api.
5. Verificar limites com testes de arquitetura.

## Checklist

- [ ] `Application` sem EF Core, ASP.NET Core ou SDK de IA.
- [ ] `Domain` sem HTTP/serialização.
- [ ] `Host.Api` sem `DbContext` direto.
- [ ] Sem ciclos entre projetos/módulos.
- [ ] Exceção documentada em ADR.

## Referências

- `ai/rules/architecture.md`
- `governance/architecture/dependency-policy.md`
- `docs/architecture/overview.md`
