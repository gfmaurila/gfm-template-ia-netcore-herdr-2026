# Proteção de dados em IA

## Princípios

1. **IA desligada por padrão**; nada sai da máquina sem configuração explícita.
2. Minimização: enviar apenas o necessário ao provedor.
3. Sem PII/dados sensíveis sem base legal e aprovação.
4. Rastreabilidade: prompt versionado, provider/modelo e uso registrados (metadados).
5. Sem log de conteúdo por padrão.

## Classificação de dados

| Classe | Exemplo | Envio a provedor externo |
|---|---|---|
| Público | texto genérico | permitido |
| Interno | documentação interna | somente com aprovação |
| Confidencial | dados de negócio | proibido por padrão |
| Pessoal (PII) | nome, e-mail, documento | proibido sem base legal/aprovação |

## Controles técnicos

- `Ai:Enabled=false` por padrão; `NullAiClient` responde `AiNotConfigured`.
- `Ai:LogPrompts=false` por padrão; quando `true`, aplicar redação e retenção curta.
- Redação de padrões (e-mail, documento, telefone) antes de qualquer envio/log, se habilitado.
- Timeout, `MaxOutputTokens`, `MaxCostUsdPerRequest`; estouro → fallback determinístico.
- Sem retry cego; backoff apenas em erro transitório e com teto de custo.
- Provider configurável por endpoint (compatível com OpenAI, Ollama local).
- Chaves somente via secrets/env; nunca em código, prompt ou log.

## Fluxo seguro (chat)

```text
Request → validação/limite de tamanho → classificação/redação (se habilitada)
→ IA (timeout + teto de custo) → validação de resposta → DTO
→ log apenas de metadados (provider, tokens, latência, traceId)
```

## RAG (blueprint)

- Curadoria da base: nada de dado confidencial sem aprovação.
- Embeddings podem ser revertidos parcialmente; tratar como dado sensível.
- Isolamento por tenant/coleção; sem mistura de fontes.
- Citação de fontes; respostas sem invenção quando não houver contexto.
- pgvector como opção; sem exigir extensão no template básico.

## Agentes/ferramentas (blueprint)

- Ferramentas com permissões mínimas; nenhuma ação destrutiva automática.
- Aprovação humana para operações irreversíveis.
- Limite de iterações e de custo por execução.
- Auditoria de chamadas de ferramenta (sem conteúdo sensível).

## Testes obrigatórios

- IA desabilitada → template funciona; chamadas não ocorrem.
- Timeout e erro do provedor → fallback/erro tratado, sem vazar detalhes.
- Redação remove PII quando habilitada.
- Nenhum teste faz chamada real a provedor pago; servidor falso local.

## Fora de escopo

- Treinamento/fine-tuning com dados do usuário.
- Armazenamento de histórico de conversas.
- Envio de dados de clientes a provedores de IA.
