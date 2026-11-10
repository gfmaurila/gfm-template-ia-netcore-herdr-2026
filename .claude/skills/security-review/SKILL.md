---
name: security-review
description: Use when reviewing code, configuration, dependencies or AI integration for secrets, auth, PII, injection, TLS and prompt injection risks.
---

# security-review

## Quando usar

- Antes de merge de mudança que toca auth, dados, configuração ou IA.
- Suspeita de segredo exposto.

## Passos

1. Mapear ativos e fronteiras de confiança.
2. Procurar segredos, tokens, connection strings e PII.
3. Verificar autenticação/autorização e menor privilégio.
4. Verificar validação de entrada, injeção, TLS e CORS.
5. Verificar logs e redação.
6. Avaliar dependências e risco de supply chain.
7. Avaliar prompt injection e envio de dados a provedores.
8. Declarar risco residual e gate.

## Se encontrar segredo

1. Não reproduzir o valor.
2. Indicar local e ação de rotação.
3. Registrar incidente no relatório.

## Checklist

- [ ] Nenhum segredo/PII no diff.
- [ ] Rotas protegidas ou justificadas.
- [ ] CORS restrito.
- [ ] Logs sem dados sensíveis.
- [ ] Risco residual declarado.

## Referências

- `ai/agents/security-reviewer.md`
- `ai/rules/security.md`
- `ai/prompts/PRM-013@1.0.0.md`
