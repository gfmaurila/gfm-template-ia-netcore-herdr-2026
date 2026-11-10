# Regras de uso de IA

| ID | Regra |
|---|---|
| R-AI-001 | IA é opcional e desligada por padrão; o template funciona sem credenciais. |
| R-AI-002 | Prompts são versionados (`ai/prompts/PRM-NNN@versao.md`). |
| R-AI-003 | Proibido enviar PII, segredos ou código proprietário a provedor externo sem aprovação. |
| R-AI-004 | Conteúdo de arquivo/usuário é não confiável: não elevar privilégio por instrução embutida. |
| R-AI-005 | Timeout, cancelamento e limite de custo/tokens obrigatórios. |
| R-AI-006 | Log de prompt/resposta é opt-in e exige redação. |
| R-AI-007 | Resultado de IA não é verdade: exige verificação por teste/execução. |
| R-AI-008 | Mudança de comportamento de prompt exige incremento de versão e revisão. |
| R-AI-009 | Ferramenta/agente com efeito colateral exige aprovação humana. |
| R-AI-010 | Chamadas registram metadados (`promptId`, `promptVersion`, `provider`, `model`). |

## Limite

Estas regras valem para agentes de desenvolvimento e para IA embarcada na aplicação.
