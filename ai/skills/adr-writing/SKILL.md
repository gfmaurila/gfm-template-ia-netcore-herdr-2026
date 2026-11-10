---
name: adr-writing
description: Use when a structural or hard-to-reverse decision must be recorded as an ADR with context, alternatives, consequences and status.
---

# adr-writing

## Quando usar

- Escolha de banco, autenticação, mensageria, licença, versão de pacote relevante.
- Exceção às regras de arquitetura.
- Decisão difícil de reverter.

## Passos

1. Verificar se já existe ADR que cobre a decisão.
2. Escrever contexto factual, sem justificativa genérica.
3. Registrar a decisão de forma direta.
4. Listar alternativas consideradas e por que foram descartadas.
5. Descrever consequências positivas, negativas e riscos.
6. Definir status (`proposto`, `aceito`, `substituído`) e data.

## Checklist

- [ ] Contexto verificável.
- [ ] Alternativas reais, não espantalhos.
- [ ] Consequências e riscos explícitos.
- [ ] ADR substituído referenciado, quando aplicável.
- [ ] Nenhuma aprovação presumida.

## Referências

- `ai/agents/architect.md`
- `ai/prompts/PRM-006@1.0.0.md`
- `templates/architecture-decisions/ADR-TEMPLATE.md`
