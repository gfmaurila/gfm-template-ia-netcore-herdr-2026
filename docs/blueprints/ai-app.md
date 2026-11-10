# Blueprint — Aplicações com IA

## Quando usar

- Há caso de uso real que se beneficia de LLM (resumo, classificação, extração, RAG).
- Existe avaliação de custo, privacidade e fallback.

**Nunca** habilitar IA por padrão no template básico.

## Estrutura

```text
src/back-end/Gfm.Template.Application/Ai/
  IAiChatClient.cs
  IAiEmbeddingClient.cs
  AiOptions.cs
  Prompts/                 # prompts versionados (ou /prompts)
src/back-end/Gfm.Template.Infrastructure/Ai/
  NullAiClient.cs          # default
  OpenAiCompatibleClient.cs
  OllamaClient.cs          # opcional
  DependencyInjection.cs
```

## Padrões

| Padrão | Descrição | Dependência |
|---|---|---|
| LLM simples | prompt → resposta, timeout/teto | nenhuma extra |
| RAG | recuperação + contexto + citação | pgvector (opcional) |
| Tools | função exposta ao modelo, permissão mínima | orquestração própria |
| Agents | múltiplos passos com limite/auditoria | somente sob demanda |

## Requisitos

- Desligada por padrão (`Ai:Enabled=false`); sem credenciais no template.
- Timeout, `MaxOutputTokens`, teto de custo, fallback determinístico.
- Prompts versionados (`PRM-*`); metadados rastreáveis, sem conteúdo por padrão.
- Sem PII a provedor externo sem aprovação (`security/ai-data-protection.md`).
- Testes com servidor falso; nenhuma chamada paga no CI.
- Validação de entrada/saída; tratar resposta do modelo como não confiável.

## RAG (se aprovado)

- Base curada; embeddings tratados como dado sensível.
- Isolamento por coleção/tenant; citação de fontes.
- Sem contexto → responder "não sei" em vez de inventar.

## Tools/Agents (se aprovado)

- Ferramentas com permissão mínima; nenhuma ação destrutiva automática.
- Aprovação humana para operações irreversíveis.
- Limite de iterações e de custo; auditoria de chamadas.

## Critérios para NÃO criar

- Sem caso de uso com métrica de sucesso definida.
- Sem orçamento/limite de custo acordado.
- Sem base legal para os dados envolvidos.
