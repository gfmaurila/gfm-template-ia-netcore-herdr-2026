---
applyTo: "src/**/*.cs"
---

# Instruções de arquitetura para código

Fonte canônica: [`ai/rules/architecture.md`](../../ai/rules/architecture.md) e
[`ai/rules/coding-standards.md`](../../ai/rules/coding-standards.md).

- Respeite a direção: `Host.Api → Infrastructure → Application → Domain`.
- `Domain` não referencia ninguém; `Application` referencia apenas `Domain`.
- `Application` não usa EF Core, ASP.NET Core ou SDK de IA.
- `Host.Api` não acessa `DbContext` diretamente.
- Async de ponta a ponta com `CancellationToken`; sem `async void`, `.Result` ou `.Wait()`.
- SQL sempre parametrizado; sem segredos/PII em logs.
- Exceção de camada exige ADR aprovado.
