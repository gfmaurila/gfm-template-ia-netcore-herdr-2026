# Padrões de código

Fonte executável: `ai/rules/coding-standards.md`.

## Base

- TFM `net10.0`; C# 14; `Nullable=enable`; `ImplicitUsings=enable`.
- File-scoped namespaces; tipos em inglês; documentação em pt-BR.
- `TreatWarningsAsErrors=true`; analyzers habilitados.
- `dotnet format --verify-no-changes` no CI.

## Async

- `CancellationToken` em toda operação assíncrona.
- Sufixo `Async`.
- Proibido `async void`, `.Result`, `.Wait()`.

## Erros

- Exceções específicas; sem catch genérico silencioso.
- `ProblemDetails` na borda HTTP.
- Sem log de segredo/PII.

## Testes

- Teste junto com o código.
- Nome descreve comportamento.
- Sem dependência de banco compartilhado.
- Sem `Thread.Sleep` como sincronização.

## Proibições

- SQL concatenado.
- Segredo em código/config versionada.
- Dependência circular entre camadas.
- `MediatR`/`FluentAssertions` (licenciamento — ADR-0005/0008).
