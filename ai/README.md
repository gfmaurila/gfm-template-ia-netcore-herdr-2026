# ai/ — fonte canônica da camada de agentes

`ai/` é a fonte de verdade **independente de ferramenta** para a engenharia assistida por IA.
Os diretórios `.opencode/`, `.claude/`, `.codex/` e `.github/` são adaptadores finos: especializam
formato, ferramentas e permissões, mas não redefinem política.

## Conteúdo

| Diretório | Função |
|---|---|
| [`agents/`](agents/README.md) | Oito papéis com responsabilidades, permissões, entradas, saídas e aceite. |
| [`rules/`](rules/README.md) | Regras executáveis de arquitetura, código, qualidade, segurança, IA e Herdr. |
| [`prompts/`](prompts/README.md) | Prompts versionados `PRM-NNN@versao`. |
| [`skills/`](skills/README.md) | Habilidades reutilizáveis em formato `SKILL.md`. |
| [`workflows/`](workflows/README.md) | Fluxos com fases, gates e artefatos. |
| `registry.yaml` | Catálogo legível por máquina: papéis, gates, adaptadores e versões. |

## Regras de manutenção

1. Mudança de comportamento começa aqui e é propagada aos adaptadores no mesmo ciclo.
2. Não duplicar texto de política: adaptadores referenciam `AGENTS.md` e `ai/`.
3. Todo prompt tem ID e versão semântica; toda regra tem ID rastreável.
4. Conteúdo proibido: segredos, tokens, PII, dados de cliente e material proprietário.

## Fluxo

```text
SPEC → ADR → PLAN → TASK → IMPLEMENTAÇÃO → TESTES → EVIDÊNCIAS
```

O fluxo completo está em [`workflows/`](workflows/README.md) e nos templates de
[`templates/`](../templates/).
