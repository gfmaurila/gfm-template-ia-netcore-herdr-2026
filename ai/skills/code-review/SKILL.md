---
name: code-review
description: Use when reviewing a diff for correctness, security, layering, async, testability and accidental complexity, producing classified findings.
---

# code-review

## Quando usar

- Antes de commit/merge de qualquer mudança relevante.
- Após uma implementação ou correção.

## Passos

1. Ler TASK, critérios de aceite e regras aplicáveis.
2. Inspecionar o diff completo, não apenas o último commit.
3. Verificar corretude e casos de erro.
4. Verificar camadas, async, concorrência e recursos.
5. Verificar testes e evidência de execução.
6. Classificar achados e emitir parecer.

## Classificação

- **Bloqueante**: corretude, segurança, camada, perda de dados.
- **Recomendado**: legibilidade, testabilidade, observabilidade.
- **Opcional**: estilo não automatizável, preferência.

## Checklist

- [ ] Achados com `arquivo:linha`.
- [ ] Nenhuma reescrita de código.
- [ ] Evidência de teste verificada.
- [ ] Parecer explícito.

## Referências

- `ai/agents/reviewer.md`
- `ai/prompts/PRM-004@1.0.0.md`
- `ai/rules/coding-standards.md`
