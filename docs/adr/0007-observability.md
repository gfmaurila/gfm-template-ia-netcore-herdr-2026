# ADR-0007 — Observabilidade com OpenTelemetry opcional

- **Status:** Proposto (aguarda aprovação)
- **Data:** 10/11/2026

## Contexto

O template precisa nascer observável, mas rodar localmente sem backend de telemetria e sem
dependências externas obrigatórias.

## Decisão

- Logs estruturados via `ILogger` (JSON quando em container), com `traceId`.
- OpenTelemetry para traces/métricas (ASP.NET Core, HttpClient, EF Core, runtime).
- Exportador OTLP **opcional**: só ativa com `OTEL_EXPORTER_OTLP_ENDPOINT`.
- Health checks: `/health/live` e `/health/ready`.
- Sem agente proprietário; compatível com OTLP genérico (Collector, Jaeger, Tempo etc.).
- Redação de dados sensíveis antes de logar (sem PII, sem tokens).

## Alternativas consideradas

1. Serilog + sinks específicos: bom, mas mais configuração e dependências.
2. APM proprietário: amarra o template a fornecedor.
3. Sem telemetria: inaceitável para produção.

## Consequências

- Positivas: padrão aberto, funciona offline, ativação por ambiente.
- Negativas: backend de visualização não incluído no Compose básico (opcional em perfil).
- Riscos: custo/volume de telemetria; mitigado por amostragem configurável.

## Critérios de aceite

- Requisição gera log correlacionado e span (quando exportador ativo).
- Aplicação inicia e responde health sem exportador configurado.
