---
name: docker-compose-local
description: Use when creating or reviewing local Docker/Compose setup for the API and its dependencies, with healthchecks and no secrets in the repository.
---

# docker-compose-local

## Quando usar

- Criar ambiente local reproduzível.
- Revisar Dockerfile/Compose.

## Passos

1. Definir serviços e dependências.
2. Criar Dockerfile multi-stage com imagem final mínima.
3. Configurar Compose com healthcheck e rede interna.
4. Usar variáveis de ambiente para configuração.
5. Documentar comandos de subida e limpeza.
6. Executar e registrar evidência.

## Checklist

- [ ] Build multi-stage.
- [ ] Imagem final sem SDK.
- [ ] Healthcheck nos serviços.
- [ ] Segredos fora do repositório.
- [ ] `down -v` documentado para ambiente descartável.
- [ ] Execução local comprovada ou limitação registrada.

## Referências

- `ai/agents/devops.md`
- `ai/rules/security.md`
- `docs/devops/local-development.md`
