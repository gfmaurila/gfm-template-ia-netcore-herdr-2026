# Workflow — feature

## Pré-condições

- SPEC, ADR e PLAN aprovados.
- TASK autorizada.

## Sequência

| Fase | Papel | Evidência |
|---|---|---|
| Implementação | Implementer | diff + build |
| Testes | Tester | testes verdes + matriz |
| Revisão | Reviewer | parecer |
| Segurança | Security Reviewer | risco residual |
| Fechamento | Orchestrator | relatório |

## Regras

1. Uma TASK por vez.
2. Testes junto com o código.
3. Nenhuma fase avança sem evidência da anterior.
4. Falha de teste ou gate bloqueia revisão.
5. Sem push sem autorização.

## Saída

Código + testes + relatório com passou/falhou/não validado.
