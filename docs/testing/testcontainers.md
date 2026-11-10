# Diretrizes — Testcontainers e banco descartável

## Princípios

1. Banco **efêmero por execução**; nada compartilhado, corporativo ou de produção.
2. Estrutura criada automaticamente (migrações EF Core) no fixture.
3. Limpeza garantida **mesmo em falha** do teste.
4. Nenhum dado real/PII; apenas dados sintéticos.
5. Teste determinístico e independente de ordem.

## Ciclo de vida

```text
Início da execução
  └─ Testcontainer Postgres (imagem pinada, ex. postgres:17-alpine)
      ├─ aguarda readiness (healthcheck/estratégia de espera)
      ├─ aplica migrações
      └─ executa testes (isolamento por teste/dados próprios)
Fim (sucesso ou falha)
  └─ dispose do container; Ryuk remove órfãos
```

- Fixture compartilhada por **coleção** (uma por suíte de integração), não por teste,
  para equilibrar isolamento e tempo.
- Cada teste cria seus próprios registros com identificadores únicos; não depende de seed.
- Alternativa de isolamento por teste: transação com rollback (avaliar apenas se necessário).

## Configuração

- Imagem e tag pinadas (sem `latest`).
- Porta dinâmica (nunca fixa em 5432).
- `TESTCONTAINERS_RYUK_DISABLED=false` (padrão) para limpeza automática.
- Timeout de startup configurado; falha explícita com mensagem clara.
- CI: Docker nativo do runner Linux; sem registry privado.

## Proibições

- Apontar para banco já existente (`ConnectionStrings` de ambiente real).
- Reutilizar container/volume entre execuções.
- Teste que depende de dados deixados por outro teste.
- `Thread.Sleep` para "esperar" o banco; usar estratégias de espera do Testcontainers.

## Quando Docker não estiver disponível

- Testes de integração **não** são pulados silenciosamente em CI.
- Localmente (Docker parado), a suíte de integração falha de forma explícita com
  instrução de como habilitar — não marcar como "passou".
- Documentar no relatório que o item "não pôde ser validado".

## Evidência exigida

- Log da execução com testes de integração verdes.
- Confirmação de que o container foi criado e removido (log/`docker ps`).
- Nenhum artefato de banco persistido no repositório.
