# Workflow — bugfix

## Objetivo

Corrigir uma falha com teste de regressão e evidência.

## Sequência

1. **Reproduzir** — comando, entrada e saída real.
2. **Isolar** — menor causa provável, sem alterar comportamento adjacente.
3. **Corrigir** — mudança mínima.
4. **Regressão** — teste que falha antes e passa depois.
5. **Revisar** — Reviewer e, se aplicável, Security Reviewer.
6. **Registrar** — relatório com causa raiz e evidência.

## Regras

- Proibido corrigir sem reprodução.
- Proibido teste que não falha no estado anterior.
- Correção não pode mascarar erro com catch silencioso.
- Falha intermitente exige registro de flakes.

## Saída

Diff + teste de regressão + causa raiz documentada.
