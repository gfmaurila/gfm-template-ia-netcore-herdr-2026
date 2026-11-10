# Perguntas abertas (decisões ausentes)

Nenhuma decisão abaixo foi presumida como aprovada. Cada item tem uma **proposta padrão**;
responder com "aceito", "alterar para X" ou "adiar".

| ID | Pergunta | Impacto | Proposta padrão |
|---|---|---|---|
| Q-01 | Confirmar nome da solução/namespace (`GFM.Template` / `Gfm.Template.*`) e formato `.slnx`? | nomes de projetos/arquivos | `GFM.Template.slnx`, assemblies `Gfm.Template.*` |
| Q-02 | Banco relacional de exemplo: PostgreSQL 17 ou SQL Server? | ADR-0008, Testcontainers, Npgsql | PostgreSQL 17 (imagem `postgres:17-alpine`) |
| Q-03 | "Compatibilidade com .NET 8" significa multi-target desde já ou apenas caminho documentado? | custo de build/teste | caminho documentado; sem multi-target até demanda real |
| Q-04 | Licença do template (MIT, Apache-2.0, proprietária)? | arquivo LICENSE, uso por terceiros | MIT |
| Q-05 | Autenticação/autorização no baseline? Se sim, qual (JWT próprio, OIDC)? | endpoints, testes, segurança | sem auth no baseline; JWT/OIDC só quando houver caso real |
| Q-06 | Destino Git: criar repositório novo ou usar um existente? Nome/owner? | Etapa 1 (git init) | repositório novo, privado, nome `GFM.Template` |
| Q-07 | Iniciar Docker Desktop para testes de integração? | Etapa 3 bloqueada hoje | responsável inicia o Docker (não farei sem aprovação) |
| Q-08 | Idioma do texto de API (mensagens, `ProblemDetails`): inglês ou pt-BR? | contrato HTTP | inglês; documentação em pt-BR |
| Q-09 | Política de `global.json` (`rollForward`: `latestPatch` ou `latestFeature`)? | reprodutibilidade | `latestPatch` |
| Q-10 | Cobertura mínima exigida? | CI | ≥ 70% em Domain/Application (indicador, não meta absoluta) |
| Q-11 | Provedor de IA padrão quando habilitado (OpenAI-compatible remoto ou Ollama local)? | blueprint IA | `none` por padrão; nenhum provedor remoto sem aprovação |
| Q-12 | Observabilidade: incluir backend local (Jaeger/Grafana) no Compose? | Etapa 5/6 | OTLP opcional; backend em profile `observability` |
| Q-13 | Publicar imagem em registry (GHCR/Docker Hub) no CI? | Etapa 6 | não publicar; apenas build local |
| Q-14 | Meta de cloud: ECS/Fargate + RDS é o alvo AWS correto? | blueprint devops | documentar, não implementar |
| Q-15 | Usar Shouldly para asserções ou apenas `Assert` do xUnit? | dependências de teste | apenas `Assert` (zero dependência extra) |
| Q-16 | Dados de seed em desenvolvimento? | Etapa 3 | seed mínimo e sintético, apenas em dev/teste |
| Q-17 | Treinar/validar em .NET 8 exige instalar SDK 8? | compatibilidade | adiar; registrar como não validado |

## Ações que dependem de você

- Aprovar a arquitetura e responder Q-01…Q-17.
- Iniciar Docker Desktop antes da Etapa 3 (Q-07).
- Autorizar (ou não) `git init` e criação de repositório remoto na Etapa 1 (Q-06).
