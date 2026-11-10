# Baseline de segurança

## 1. Segredos

- Proibido versionar segredos: tokens, chaves, connection strings reais, certificados.
- Desenvolvimento: `dotnet user-secrets` ou variáveis de ambiente locais.
- CI/CD: GitHub Secrets; nunca ecoar em logs.
- `.gitignore` inclui `.env`, `*.local.json`, `appsettings.*.local.json`, `secrets.*`.
- Qualquer segredo exposto deve ser **rotacionado**, não apenas removido do commit.

## 2. Dados e privacidade

- Sem PII, dados de cliente ou dados de produção no repositório, fixtures ou logs.
- Dados de exemplo estritamente sintéticos.
- Logs não registram corpo de requisição/resposta por padrão.
- Mascaramento de campos sensíveis quando necessário (documentar quais).

## 3. Aplicação

- Validação de entrada e limites de tamanho em todos os endpoints.
- Sem SQL concatenado; EF Core parametriza consultas.
- Sem `catch` genérico silencioso; erros inesperados logados com correlação.
- Headers de segurança e CORS restrito por configuração.
- HTTPS obrigatório fora de desenvolvimento.
- Rate limiting disponível (ativável por configuração).
- Autenticação/autorização: **não incluídas no baseline** (Q-05); qualquer inclusão exige ADR.

## 4. Dependências e supply chain

- Apenas licenças permissivas (MIT, Apache-2.0, BSD, MS-PL), salvo aprovação.
- `dotnet list package --vulnerable` no CI (falha em vulnerabilidade alta/crítica).
- Pacotes com versão centralizada e revisão de upgrade.
- Sem scripts remotos de instalação no pipeline.

## 5. Containers

- Imagens oficiais e pinadas; multi-stage; runtime non-root.
- Sem segredos na imagem ou em `docker build` args.
- `HEALTHCHECK`/health endpoints; filesystem read-only quando viável.
- Compose local sem expor portas desnecessárias.

## 6. IA

- Desligada por padrão; nenhuma chamada externa sem configuração explícita.
- Sem envio de PII a provedores externos sem base legal e aprovação.
- Timeout, limite de custo/tokens e fallback obrigatórios quando habilitada.
- Ver [`ai-data-protection.md`](ai-data-protection.md).

## 7. Revisão de segurança (checklist de PR)

- [ ] Nenhum segredo/PII no diff.
- [ ] Entrada validada; erros não vazam interno.
- [ ] Sem SQL concatenado / `FromSqlRaw` com interpolação.
- [ ] Sem `async void`, `.Result`, `.Wait()`.
- [ ] Dependência nova com licença verificada.
- [ ] Logs sem dados sensíveis.
- [ ] Testes cobrindo caminho de erro relevante.

## 8. Resposta a incidente (mínimo)

1. Conter (revogar credencial/segredo).
2. Avaliar exposição (o que vazou, desde quando).
3. Corrigir e adicionar teste de regressão.
4. Registrar lição aprendida em ADR/checklist.
