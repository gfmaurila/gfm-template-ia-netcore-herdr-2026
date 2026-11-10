# Quality gates

Uma entrega só é concluída quando todos os itens aplicáveis passam. Item não aplicável exige
justificativa registrada.

| ID | Gate | Evidência |
|---|---|---|
| QG-01 | Escopo e critérios de aceite da TASK atendidos. | TASK + diff |
| QG-02 | Regras de dependência respeitadas. | ArchitectureTests |
| QG-03 | Build sem warnings/erros. | saída de build |
| QG-04 | Testes unitários com asserção comportamental. | saída de teste |
| QG-05 | Integração com recurso descartável. | saída de teste |
| QG-06 | Recurso temporário removido (mesmo em falha). | log/limpeza |
| QG-07 | Testes de arquitetura/contrato quando aplicáveis. | saída de teste |
| QG-08 | Formatação e analyzers limpos. | `dotnet format --verify-no-changes` |
| QG-09 | Varredura de segredos e dependências. | relatório |
| QG-10 | Revisão de auth/TLS/logs/PII. | parecer de segurança |
| QG-11 | Documentação e ADRs atualizados. | diff documental |
| QG-12 | Evidência real registrada no relatório. | `reports/` |

## Regra de bloqueio

- Falha em QG-01..12 bloqueia conclusão e merge.
- Se uma validação não puder ser executada, registrar motivo e impacto; a TASK permanece pendente.
- Proibido teste artificial, skip silencioso ou sucesso presumido.
