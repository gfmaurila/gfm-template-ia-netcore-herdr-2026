# ADR-0006 — Erros e validação uniformes

- **Status:** Proposto (aguarda aprovação)
- **Data:** 10/11/2026

## Contexto

APIs inconsistentes em formato de erro dificultam clientes e observabilidade. É preciso
distinguir falha esperada de defeito inesperado, sem vazar detalhes internos.

## Decisão

- `Result`/`Error` na `Application` para falhas esperadas, com códigos estáveis.
- Invariantes de domínio via `DomainException` (não HTTP).
- Validação de forma na borda + regras no caso de uso com FluentValidation.
- Respostas de erro em **ProblemDetails (RFC 9457)**, com `traceId`, `type` e `title`.
- Mapeamento centralizado (código de erro → status HTTP), sem `switch` espalhado.
- Produção nunca expõe stack trace/mensagem interna.

## Alternativas consideradas

1. Exceções para tudo: simples, mas fluxo de controle caro e ambíguo.
2. `Result` em tudo, inclusive programação: verboso; exceções seguem para o inesperado.
3. Middleware sem Result: perde distinção de erros de negócio.

## Consequências

- Positivas: contrato de erro previsível, testável, seguro.
- Negativas: dois mecanismos (Result + exceptions) exigem disciplina.
- Riscos: catch genérico silencioso; proibido e coberto por revisão.

## Regras

- Todo erro inesperado é logado com contexto e correlação; cliente recebe 500 genérico.
- `ProblemDetails` inclui `extensions.code` estável para clientes.
- Testes de contrato validam formato de sucesso e de erro.
