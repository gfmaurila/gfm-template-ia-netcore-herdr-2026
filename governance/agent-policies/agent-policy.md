# Política de agentes

Fonte executável: `ai/rules/ai-operations.md` e `ai/registry.yaml`.

## Papéis e limites

| Papel | Pode | Não pode |
|---|---|---|
| Architect | SPEC, ADR, PLAN, diagnóstico | implementar feature, alterar ADR alheio |
| Implementer | código + testes da TASK | mudar ADR/arquitetura sem Architect |
| Tester | plano e testes | declarar conclusão sem execução |
| Reviewer | parecer classificado | reescrever código |
| Security Reviewer | achados e bloqueio | aceitar risco sem responsável |
| DevOps | Docker, Compose, CI | segredos no repositório |
| Docs Writer | documentação e índices | alterar política |
| Orchestrator | delegar, consolidar, relatar | aprovar gate humano |

## Regras

1. Um agente não inicia outro sem autorização do responsável.
2. Toda delegação declara escopo, saída esperada e gate.
3. Agente sem ferramenta validada é documentado como **não validado em runtime**.
4. IA é opcional e desligada por padrão em produtos gerados.
5. Nenhum agente acessa repositório de cliente ou dados reais.
6. Saída de agente sem evidência não conclui gate.
