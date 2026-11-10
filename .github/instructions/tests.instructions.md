---
applyTo: "tests/**/*.cs"
---

# Instruções para testes

Fonte canônica: [`ai/rules/quality-gates.md`](../../ai/rules/quality-gates.md).

- Teste deriva de critério de aceite e tem asserção comportamental.
- Integração usa Testcontainers com recurso efêmero por execução.
- Limpeza garantida mesmo em falha (Ryuk ou equivalente).
- Proibido banco compartilhado/corporativo/produção e dados reais/PII.
- Proibido skip silencioso, retry infinito ou asserção vazia.
- Teste deve falhar quando o comportamento esperado quebra.
