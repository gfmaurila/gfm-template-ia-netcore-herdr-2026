# ai/rules — regras executáveis

Regras são a fonte executável da política. `governance/` publica a mesma política para humanos,
referenciando estes arquivos para evitar duplicação.

| Arquivo | Escopo | IDs |
|---|---|---|
| [`architecture.md`](architecture.md) | Camadas, dependências e módulos | R-ARCH-* |
| [`coding-standards.md`](coding-standards.md) | Estilo e práticas de código | R-CODE-* |
| [`quality-gates.md`](quality-gates.md) | Critérios de conclusão | QG-* |
| [`security.md`](security.md) | Segurança e dados | R-SEC-* |
| [`ai-usage.md`](ai-usage.md) | Uso de IA e prompts | R-AI-* |
| [`herdr-operations.md`](herdr-operations.md) | Orquestração no Herdr | R-HC-* |

## Regras de manutenção

1. Toda regra tem ID estável e verificável.
2. Regra automatizável deve virar teste/lint, não apenas texto.
3. Exceção exige ADR ou justificativa registrada na TASK.
4. Não duplicar regra em adaptadores; eles referenciam este diretório.
