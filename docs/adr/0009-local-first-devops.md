# ADR-0009 — DevOps local-first, container-first, cloud-ready, AWS target

- **Status:** Proposto (aguarda aprovação)
- **Data:** 10/11/2026

## Contexto

O template deve ser executável e validável localmente, depois reproduzível em container e,
no futuro, implantável em nuvem — sem acoplar o código a um provedor.

## Decisão

Ordem de prioridade:

1. **Local first**: `dotnet run` + dependências via Compose (Postgres).
2. **Container first**: Dockerfile multi-stage + Compose completo (api + postgres).
3. **Cloud ready**: configuração 12-factor, health checks, logs em stdout, sem estado local.
4. **AWS target**: alvo documentado (ex.: ECS/Fargate + RDS), **não implementado** nesta fase.

- CI em GitHub Actions: restore, build, format, testes (Testcontainers), build de imagem.
- Segredos via GitHub Secrets/variáveis; nunca no repositório.
- CI sem dependência de serviços corporativos.
- Publicação/deploy exige aprovação explícita.

## Alternativas consideradas

1. Cloud-first: atrito local e custo desnecessário.
2. Apenas Docker: dificulta debug no host.
3. Kubernetes desde o início: complexidade desproporcional.

## Consequências

- Positivas: mesma imagem em qualquer destino; onboarding simples.
- Negativas: manter Compose e pipeline sincronizados com o código.
- Riscos: divergência local/CI; mitigada por comandos idênticos e cache de NuGet.

## Critérios de aceite

- `docker compose up` sobe API saudável e Postgres.
- Pipeline verde sem segredos corporativos.
- Imagem não roda como root e não contém segredos.
