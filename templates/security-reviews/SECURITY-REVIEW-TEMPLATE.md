# SECURITY-REVIEW — <escopo>

- **Status:** rascunho | aprovado | bloqueado
- **Data:** AAAA-MM-DD
- **Revisor:** Security Reviewer
- **Relacionados:** SPEC-NNN, TASK-<AREA>-NNN, diff/commit

## 1. Escopo

<arquivos, rotas, configurações e dependências avaliadas>

## 2. Fronteiras de confiança

| Fronteira | Entrada | Controle |
|---|---|---|
| <externa/interna> | <dado> | <auth/validação> |

## 3. Achados

| ID | Severidade | Achado | Local | Ação |
|---|---|---|---|---|
| SEC-001 | bloqueante/recomendado/opcional | <achado> | `arquivo:linha` | <ação> |

## 4. Verificações

- [ ] Sem segredos, tokens ou connection strings no diff.
- [ ] Sem PII em código, testes ou logs.
- [ ] Autenticação e autorização verificadas.
- [ ] Validação de entrada e injeção.
- [ ] TLS, CORS e headers.
- [ ] Dependências e supply chain.
- [ ] Prompt injection e envio de dados a provedores de IA.
- [ ] Logs sem dados sensíveis.

## 5. Risco residual

<risco aceito, com justificativa e prazo de revisão>

## 6. Parecer

aprovado | aprovado com ressalvas | bloqueado
