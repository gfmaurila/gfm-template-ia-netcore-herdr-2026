# ADR-0010 — IA opcional, desacoplada e desligada por padrão

- **Status:** Proposto (aguarda aprovação)
- **Data:** 10/11/2026

## Contexto

O template é ".NET + IA", mas exigir credenciais de IA impediria o uso básico e criaria
riscos de custo e privacidade. O núcleo deve funcionar sem IA.

## Decisão

- Interfaces na `Application`:
  - `IAiChatClient` (completion),
  - `IAiEmbeddingClient` (vetores),
  - `IAiTool`/registro de ferramentas (opcional),
  - `AiOptions` (provider, modelo, timeout, `MaxOutputTokens`, teto de custo, flags).
- Adaptadores na `Infrastructure`:
  - `NullAiClient` como padrão (retorna "não configurado" de forma explícita);
  - adaptador HTTP compatível com OpenAI **opcional**;
  - Ollama/local como opção de blueprint.
- Nenhuma chamada externa sem configuração explícita; IA desligada por padrão.
- Timeouts, limite de tokens/custo, fallback determinístico e logs sem PII.
- Prompts versionados (`PRM-*`/`prompts/`), com id + versão rastreável.
- Testes cobrem o caminho "sem configuração" e o adaptador com servidor falso.

## Alternativas consideradas

1. SDK proprietário acoplado ao host: viola desacoplamento.
2. IA obrigatória com chave em `appsettings`: risco de vazamento e bloqueio de uso.
3. Sem camada de IA: contraria o objetivo do template.

## Consequências

- Positivas: template utilizável sem custo; troca de provedor trivial; privacidade controlada.
- Negativas: adaptador genérico pode não cobrir recursos específicos de cada provedor.
- Riscos: custo/abuso se configurado sem limites; mitigado por tetos e revisão de segurança.

## Requisitos de segurança

- Nunca logar prompt/resposta por padrão; exigir opt-in explícito e redação.
- Não enviar PII a provedores externos sem base legal e aprovação.
- Ver [`../security/ai-data-protection.md`](../security/ai-data-protection.md).
