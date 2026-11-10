# Regras de segurança

| ID | Regra |
|---|---|
| R-SEC-001 | Segredos somente em vault/secrets/variáveis de ambiente; nunca no repositório. |
| R-SEC-002 | TLS com validação normal de certificado; proibido callback que aceita tudo. |
| R-SEC-003 | Autenticação e autorização explícitas por endpoint; rota anônima exige justificativa. |
| R-SEC-004 | CORS restrito; proibido wildcard combinado com credenciais. |
| R-SEC-005 | Menor privilégio para identidades, banco, broker, pipeline e agentes. |
| R-SEC-006 | Entrada validada e limitada; consultas parametrizadas; sem stack trace ao cliente. |
| R-SEC-007 | PII e segredos redigidos em logs. |
| R-SEC-008 | Testes usam dados sintéticos e banco descartável. |
| R-SEC-009 | Varredura de dependências e segredos antes de merge. |
| R-SEC-010 | Deploy protegido; OIDC preferível a credencial de longa duração. |
| R-SEC-011 | Mudança de auth/cripto/PII exige revisão humana. |
| R-SEC-012 | IA desligada por padrão; nenhum dado sai da máquina sem configuração explícita. |

## Se um segredo for encontrado

1. Interromper a divulgação.
2. Revogar/rotacionar a credencial (apagar cópia local não invalida o segredo).
3. Registrar o incidente no relatório do ciclo.
