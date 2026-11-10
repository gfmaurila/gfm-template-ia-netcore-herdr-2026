# Especificação — requisitos não funcionais (NFR)

## 1. Plataforma

- .NET 10 / `net10.0`, Linux container (imagem oficial `mcr.microsoft.com/dotnet/aspnet`).
- Funciona em Windows (dev) e Linux (container/CI).
- Configuração 12-factor; nenhum caminho absoluto de máquina no código.

## 2. Desempenho (metas iniciais, não validadas)

| Métrica | Meta |
|---|---|
| Latência p95 de leitura simples (local) | < 100 ms |
| Latência p95 de escrita simples (local) | < 200 ms |
| Throughput de smoke test | ≥ 100 req/s no host |
| Uso de memória em repouso | < 200 MB |

Metas só viram requisito após medição reproduzível.

## 3. Confiabilidade

- Health checks `/health/live` e `/health/ready`.
- Timeouts em toda I/O; sem retry infinito.
- Concorrência otimista no agregado de exemplo.
- Migrações aplicadas de forma controlada (não automática em produção).

## 4. Segurança

- Sem segredos versionados; `.gitignore` cobre `appsettings.*.local.json`, `.env`, etc.
- HTTPS em produção; headers de segurança; CORS restrito por configuração.
- Sem SQL concatenado; ORM parametriza.
- Dependências verificadas por vulnerabilidade no CI.
- Ver [`../security/security-baseline.md`](../security/security-baseline.md).

## 5. Observabilidade

- Logs estruturados com correlação; sem PII.
- Traces/métricas via OpenTelemetry quando `OTEL_EXPORTER_OTLP_ENDPOINT` definido.
- Sem backend obrigatório para rodar localmente.

## 6. Testabilidade

- Unitários sem I/O; integração com banco efêmero; arquitetura; contrato.
- Testes determinísticos (tempo via `IClock`, sem `Thread.Sleep`).
- Nenhuma dependência de banco compartilhado/corporativo/produção.

## 7. Portabilidade e manutenção

- TFM e versões centralizados.
- Build com zero warnings (`TreatWarningsAsErrors`).
- Formatação verificada no CI.
- Documentação e ADR atualizados junto da mudança de decisão.

## 8. Custo e IA

- IA desligada por padrão; sem credenciais obrigatórias.
- Tetos de timeout/tokens/custo por requisição quando habilitada.
- Nenhum custo recorrente no template básico.

## 9. Licenciamento

- Dependências apenas com licença permissiva (MIT/Apache-2.0/BSD/MS-PL), salvo aprovação.
