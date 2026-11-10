---
name: github-actions-ci
description: Use when creating or reviewing a GitHub Actions CI workflow for restore, build, format, tests, coverage artifacts and container build.
---

# github-actions-ci

## Quando usar

- Criar ou ajustar pipeline de CI.
- Diagnosticar falha de CI.

## Passos

1. Fixar versões de runner e SDK.
2. Restaurar com cache de NuGet.
3. Build com warnings como erro.
4. `dotnet format --verify-no-changes`.
5. Testes unitários, arquitetura e integração.
6. Publicar artefatos de teste.
7. Build da imagem, se aplicável.

## Checklist

- [ ] Sem segredo em texto claro.
- [ ] Permissões mínimas (`contents: read`).
- [ ] Sem dependência de serviço corporativo.
- [ ] Cache não mascara restore quebrado.
- [ ] Falha de teste falha o job.
- [ ] Artefatos com retenção definida.

## Referências

- `ai/agents/devops.md`
- `ai/prompts/PRM-005@1.0.0.md`
- `docs/devops/ci-cd.md`
