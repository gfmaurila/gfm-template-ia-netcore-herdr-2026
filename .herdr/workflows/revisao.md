# Workflow — revisão

## Uso

Antes de commit/merge de uma mudança relevante.

```powershell
hc run --bg --name reviewer --cwd <repo> gfm-reviewer "Revise o diff atual. Somente leitura."
hc wait --children all
hc read reviewer --lines 160
hc run --bg --name security --cwd <repo> gfm-security-reviewer "Revise seguranca do diff atual."
hc wait --children all
hc read security --lines 160
```

## Critério de saída

- Achados classificados (bloqueante / recomendado / opcional) com `arquivo:linha`.
- Parecer explícito: aprovado, aprovado com ressalvas ou bloqueado.
- Riscos residuais declarados.
- Nenhuma reescrita de código pelos revisores.

## Bloqueios

- Segredo ou PII encontrado: interromper e orientar rotação.
- Violação de camada: bloquear até ADR.
- Ausência de evidência de teste: bloquear conclusão.
