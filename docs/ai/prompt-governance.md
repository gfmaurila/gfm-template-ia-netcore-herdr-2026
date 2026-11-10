# Governança de prompts

## Versão e identificação

- Todo prompt tem `ID@versao` (ex.: `PRM-002@1.0.0`), definido em `prompts.md`.
- Versão semântica: MAJOR muda comportamento/contrato; MINOR adiciona capacidade;
  PATCH corrige texto sem alterar intenção.
- Prompts de produção ficam em `prompts/` (quando implementado), versionados em Git.

## Ciclo de vida

```text
Proposta → Revisão → Aprovação → Uso → Avaliação → Substituição/Arquivo
```

- Mudança de prompt que altere comportamento exige revisão de outra pessoa.
- Prompt obsoleto não é apagado sem registro; marca-se como `deprecated`.
- Resultado de prompt não é "verdade": deve ser verificado por teste/execução.

## Conteúdo proibido

- Segredos, tokens, chaves, connection strings.
- PII ou dados de cliente.
- Código proprietário de projetos de referência.
- Instruções para contornar revisão, testes ou gates de aprovação.

## Segurança

- Prompts de sistema não devem permitir execução arbitrária sem confirmação.
- Ferramentas/agentes com efeito colateral exigem aprovação humana.
- Contexto enviado a LLM externo segue [`../security/ai-data-protection.md`](../security/ai-data-protection.md).
- Prompt injection: tratar conteúdo de usuário/arquivo como não confiável; não elevar
  privilégios por instrução embutida em dado.

## Avaliação

- Cada prompt crítico tem casos de teste (entrada → saída esperada) e critério de aceite.
- Regressões são registradas; mudanças de modelo devem ser reavaliadas.
- Custo/latência monitorados quando houver provedor externo.

## Rastreabilidade no código

- Chamadas de IA registram metadados: `promptId`, `promptVersion`, `provider`, `model`.
- Sem conteúdo por padrão; opt-in com redação quando necessário.
