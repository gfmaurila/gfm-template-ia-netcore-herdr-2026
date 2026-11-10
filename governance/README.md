# governance — política publicada para humanos

`governance/` publica, para leitura humana, a política que `ai/rules/` aplica de forma executável.
Em caso de divergência, a fonte canônica é `AGENTS.md` + `ai/rules/`; este diretório deve ser
corrigido no mesmo ciclo.

## Áreas

| Área | Documento | Regra executável |
|---|---|---|
| Agentes | `agent-policies/agent-policy.md` | `ai/rules/ai-operations.md` |
| Arquitetura | `architecture/dependency-policy.md` | `ai/rules/architecture.md` |
| Código | `coding-standards/coding-standards.md` | `ai/rules/coding-standards.md` |
| Qualidade | `quality-gates/quality-gates.md` | `ai/rules/quality-gates.md` |
| Segurança | `security/security-policy.md` | `ai/rules/security.md` |
| Herdr | `.herdr/README.md` | `ai/rules/herdr-operations.md` |

## Regras

1. Governança não cria política nova; publica a existente.
2. Toda exceção exige ADR e aprovação humana.
3. Violação bloqueante interrompe o gate.
4. Mudança de política começa em `AGENTS.md`/`ai/` e é propagada no mesmo ciclo.
