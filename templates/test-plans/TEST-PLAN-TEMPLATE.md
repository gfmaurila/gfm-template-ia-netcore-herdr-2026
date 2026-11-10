# TEST-PLAN — <título>

- **Status:** rascunho | aprovado | executado
- **Data:** AAAA-MM-DD
- **Relacionados:** SPEC-NNN, TASK-<AREA>-NNN

## 1. Escopo de teste

<o que será verificado e o que fica fora>

## 2. Matriz de rastreabilidade

| Requisito | Tipo de teste | Caso | Evidência |
|---|---|---|---|
| RF-001 | unitário | <caso> | <saída> |
| RF-002 | integração | <caso> | <saída> |
| RNF-001 | arquitetura | <regra> | <saída> |

## 3. Ambiente

- Recurso descartável via Testcontainers: <sim/não>
- Banco: <imagem/versão efêmera>
- Limpeza garantida: <Ryuk/equivalente>
- Dados: sintéticos

## 4. Casos

| ID | Cenário | Entrada | Esperado | Tipo |
|---|---|---|---|---|
| T-001 | <cenário> | <entrada> | <resultado> | unitário |
| T-002 | <cenário> | <entrada> | <resultado> | integração |

## 5. Critérios de saída

- [ ] Todos os casos executados.
- [ ] Falhas registradas com saída real.
- [ ] Nenhum teste dependente de ambiente compartilhado.
- [ ] Limpeza comprovada.

## 6. Resultado

| Caso | Resultado | Observação |
|---|---|---|
| T-001 | passou/falhou | <nota> |
