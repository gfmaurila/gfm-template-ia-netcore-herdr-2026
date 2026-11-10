# Política de segurança

Fonte executável: `ai/rules/security.md`.

## Segredos

- Nunca versionar segredo, token, senha ou connection string real.
- Configuração via variáveis de ambiente ou user-secrets/CI secrets.
- Segredo exposto exige rotação e registro de incidente.

## Dados

- Sem PII em código, teste, fixture, log ou relatório.
- Dados de teste são sintéticos.
- Menor privilégio em banco e credenciais.

## Aplicação

- Validar entrada na borda.
- Sem SQL concatenado.
- CORS restrito e explícito.
- TLS obrigatório fora de localhost.
- Headers de segurança habilitados.
- Rate limit quando exposto.

## Dependências

- Versões fixadas e atualizáveis.
- Sem vulnerabilidade crítica conhecida.
- Licença compatível (sem MediatR/FluentAssertions).

## IA

- Desligada por padrão.
- Sem envio de dados sensíveis a provedor externo.
- Prompt e saída tratados como entrada não confiável.
- Timeout, limite de custo e fallback definidos.
