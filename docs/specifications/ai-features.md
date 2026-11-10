# Especificação — funcionalidades de IA (opcionais)

O template básico **não** usa IA. Esta spec cobre o que pode ser habilitado depois.

## Contratos (Application)

```csharp
public interface IAiChatClient
{
    Task<AiChatResult> CompleteAsync(AiChatRequest request, CancellationToken ct);
}

public interface IAiEmbeddingClient
{
    Task<AiEmbeddingResult> EmbedAsync(AiEmbeddingRequest request, CancellationToken ct);
}

public sealed record AiOptions
{
    public bool Enabled { get; init; }                       // default: false
    public string Provider { get; init; } = "none";          // none | openai-compatible | ollama
    public string? Endpoint { get; init; }
    public string? Model { get; init; }
    public int TimeoutSeconds { get; init; } = 30;
    public int MaxOutputTokens { get; init; } = 512;
    public decimal? MaxCostUsdPerRequest { get; init; }
    public bool LogPrompts { get; init; }                    // default: false
}
```

- `AiChatRequest`/`AiChatResult` carregam metadados de uso (tokens, custo estimado, provider).
- Erros: `AiNotConfigured`, `AiTimeout`, `AiRateLimited`, `AiInvalidResponse`.
- Nenhum tipo de SDK de provedor vaza para `Application`.

## Adaptadores (Infrastructure)

| Provider | Uso | Observação |
|---|---|---|
| `none` | padrão | `NullAiClient` retorna `AiNotConfigured` |
| `openai-compatible` | HTTP genérico | endpoint/modelo por configuração |
| `ollama` | local | blueprint, sem custo externo |

## Requisitos

1. Template inicia e responde sem `Ai:Enabled=true`.
2. Timeout obrigatório; cancelamento propagado.
3. Limite de tokens/custo; excedeu → fallback definido, não exceção não tratada.
4. Prompt/response **não** logados por padrão; `LogPrompts` exige opt-in e redação.
5. Nenhum PII enviado a provedor externo sem aprovação e base legal.
6. Prompts versionados (`prompts/`, id + versão) e rastreáveis em logs de metadados.
7. Testes: caminho desabilitado, timeout, erro do provedor e resposta válida com servidor falso.

## Endpoint de exemplo (opcional, blueprint)

```text
POST /api/ai/summarize
{ "text": "..." }  ->  { "summary": "...", "provider": "...", "usage": { ... } }
```

- Desabilitado por padrão (404/503 documentado) quando `Ai:Enabled=false`.
- Rate limit e limite de tamanho de entrada obrigatórios quando habilitado.

## Custos e limites

- Teto por requisição e por janela (configurável) — sem promessa de valor exato sem medição.
- Sem retries cegos que multipliquem custo; retry só em erros transitórios com backoff.

## Fora de escopo

- Treinamento/fine-tuning.
- Armazenamento de conversas de usuários.
- Agentes autônomos com acesso a ferramentas destrutivas.
- Qualquer dado de cliente.
