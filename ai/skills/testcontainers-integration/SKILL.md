---
name: testcontainers-integration
description: Use when writing integration tests that need a disposable database or service via Testcontainers, with guaranteed cleanup and no shared environments.
---

# testcontainers-integration

## Quando usar

- Teste de repositório, migrations, contrato HTTP ou fluxo com persistência.
- Qualquer teste que exigiria banco real.

## Passos

1. Definir o contrato e os casos de teste.
2. Criar fixture com container efêmero por execução.
3. Aplicar migrations no fixture.
4. Garantir limpeza mesmo em falha (Ryuk ou equivalente).
5. Usar dados sintéticos.
6. Executar e registrar saída real.

## Checklist

- [ ] Container efêmero por execução.
- [ ] Sem banco compartilhado, corporativo ou de produção.
- [ ] Limpeza garantida em falha.
- [ ] Sem dados reais/PII.
- [ ] Sem skip silencioso ou retry infinito.
- [ ] Teste falha quando o comportamento quebra.

## Referências

- `ai/rules/quality-gates.md`
- `docs/testing/testcontainers.md`
- `ai/prompts/PRM-003@1.0.0.md`
