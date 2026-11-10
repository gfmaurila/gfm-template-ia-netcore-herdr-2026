# Blueprint — Worker / Batch

## Quando usar

- Processamento assíncrono, agendado ou em lote (jobs, importações, relatórios).
- Necessidade real de desacoplar do ciclo HTTP.

**Não materializar** sem caso de uso aprovado; o template básico é API-only.

## Estrutura proposta

```text
src/back-end/Gfm.Template.Host.Worker/
  Program.cs              # Generic Host
  Jobs/                   # jobs idempotentes
  Scheduling/             # agendamento (cron/timer)
deploy/worker.Dockerfile
```

- Reutiliza `Application` + `Infrastructure` (sem duplicar domínio).
- Sem ASP.NET Core; usa `Microsoft.Extensions.Hosting`.
- Configuração 12-factor; health opcional via endpoint/arquivo.

## Regras

- Jobs **idempotentes** e reexecutáveis.
- `CancellationToken` propagado; shutdown gracioso.
- Sem estado em memória entre execuções relevantes.
- Concorrência e lock distribuído (Redis) apenas quando necessário.
- Observabilidade: logs com `jobId`/correlação; métricas de duração e falha.

## Testes

- Unitários: lógica do job sem I/O.
- Integração: banco efêmero + execução do job.
- Falha/retry: comportamento determinístico; sem `sleep` real prolongado.

## Mensageria (extensão)

- Contrato de mensagem na `Application`; adaptador na `Infrastructure`.
- Outbox transacional antes de publicar (evitar perda).
- Consumidor idempotente; dead-letter documentado.
- Broker só quando houver necessidade real (não no template básico).

## Critérios para NÃO criar

- Se a tarefa cabe em um endpoint assíncrono simples.
- Se não há volume/duração/agendamento que justifiquem processo separado.
