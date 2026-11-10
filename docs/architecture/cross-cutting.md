# Cross-cutting (transversais)

## Validação

- Validação de entrada na borda (endpoints) para forma/limites.
- Validação de regra de caso de uso na `Application` (FluentValidation, licença Apache-2.0).
- Invariantes no `Domain` (construtor/fábrica + métodos), lançando `DomainException`.
- Falha de validação → `400` com `ValidationProblemDetails` (RFC 9457), sem detalhes internos.

## Tratamento uniforme de erros

- `Result`/`Error` na `Application` para falhas esperadas (not found, conflito, regra).
- Exceções apenas para condições inesperadas.
- Middleware/handler converte para `ProblemDetails` com `traceId` e `type` estável.
- Mapeamento: `DomainException`/validação → 400; não encontrado → 404; conflito → 409;
  não autorizado → 401/403; inesperado → 500 (sem stack trace em produção).
- Nunca expor mensagem interna de exceção ao cliente.

## Injeção de dependência

- Registro por extensão em cada projeto; `Program.cs` apenas orquestra.
- Options pattern com validação em startup (`ValidateOnStart`).
- Sem service locator; sem dependência estática oculta.
- `IClock` abstrai tempo para testes determinísticos.

## Configuração

- 12-factor: variáveis de ambiente; `appsettings.*` apenas para padrões não sensíveis.
- Precedência: env vars > user-secrets (dev) > appsettings.
- Conexão: `ConnectionStrings__Default`; IA: `Ai__*` (desligada por padrão).
- Falha rápida se configuração obrigatória estiver ausente/inválida.

## Observabilidade

- Logs estruturados (JSON em container) com `traceId`/`spanId`, sem PII/segredos.
- OpenTelemetry: traces (ASP.NET Core, HTTP, EF Core), métricas (runtime, HTTP) e exportador
  OTLP **opcional** via `OTEL_EXPORTER_OTLP_ENDPOINT`.
- Health checks: `/health/live` e `/health/ready` (readiness inclui dependências críticas).
- Correlação: `X-Correlation-Id` aceito/gerado e propagado (nunca confiar cegamente).
- Sem exportador configurado, a aplicação funciona normalmente (local-first).

## Performance e resiliência

- Paginação obrigatória em listagens; limites máximos validados.
- `AsNoTracking` em leitura; projeções para DTO (sem carregar agregados inteiros).
- Timeouts e `CancellationToken` em toda I/O.
- Retry/circuit breaker apenas onde há dependência externa real (HTTP/IA), com política explícita.
- Sem cache distribuído no template básico; Redis é extensão opcional.

## Consistência e transações

- Uma transação por caso de uso (`SaveChanges` único quando possível).
- Eventos de domínio publicados em processo após commit; outbox é extensão futura documentada.
- Idempotência: documentada para endpoints sensíveis; implementação conforme caso real.

## Segurança transversal

- Validação de entrada + limite de tamanho; sem SQL concatenado (EF Core parametriza).
- HTTPS, headers de segurança e CORS restrito por configuração.
- Rate limiting opcional no host, configurável.
- Autenticação/autorização **não implementadas no baseline** até decisão (Q-05).
- Ver [`../security/security-baseline.md`](../security/security-baseline.md).
