# .codex/rules — mapeamento de regras

O Codex não possui diretório de regras executáveis próprio neste template. As regras canônicas
vivem em [`ai/rules/`](../../ai/rules/README.md) e são referenciadas por `AGENTS.md`.

| Regra canônica | Aplicação no Codex |
|---|---|
| [`architecture.md`](../../ai/rules/architecture.md) | Citada em `AGENTS.md` e nos prompts. |
| [`coding-standards.md`](../../ai/rules/coding-standards.md) | Citada em `AGENTS.md` e nos prompts. |
| [`quality-gates.md`](../../ai/rules/quality-gates.md) | Critério de conclusão de TASK. |
| [`security.md`](../../ai/rules/security.md) | Bloqueante em revisão. |
| [`ai-usage.md`](../../ai/rules/ai-usage.md) | Uso de IA e prompts. |
| [`herdr-operations.md`](../../ai/rules/herdr-operations.md) | Execução com `--no-daemon`. |

Não duplique texto de regra aqui: qualquer mudança começa em `ai/rules/` e é propagada no mesmo
ciclo.
