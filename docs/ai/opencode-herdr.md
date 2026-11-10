# OpenCode dentro do Herdr

## Ambiente verificado (10/11/2026)

| Item | Valor |
|---|---|
| Herdr App | 0.1.14 |
| Herdr Core (`hc`) | 0.1.19 |
| OpenCode | 1.19.0 |
| Codex CLI (presente, não usado) | 0.163.0 |
| Workspace | `C:\Work\dev\herdr.dev` |
| Terminal integrado | PowerShell (`pwsh`) |

- `hc`, `herdr-core` e `herdr-app` resolvem no PATH.
- Nenhuma variável de credencial de IA presente no ambiente.

## Uso recomendado

1. Abrir/criar um **Space** no Herdr apontando para `C:\Work\dev\herdr.dev`
   (manual do Herdr, seção 7 — pendente de validação).
2. Abrir terminal nesse Space.
3. Iniciar `opencode` no diretório do workspace.
4. Pedir auditoria somente leitura antes de qualquer alteração.
5. Revisar o diff antes de aprovar mudanças.

## Fluxo com agentes

| Papel | Prompt | Saída esperada |
|---|---|---|
| Architect | `PRM-001`, `PRM-006` | diagnóstico, ADR |
| Implementer | `PRM-002` | diff + build/teste |
| Tester | `PRM-003` | testes + resultado |
| Reviewer | `PRM-004` | achados classificados |
| DevOps | `PRM-005` | Docker/CI + evidência |

## Regras de convivência

- Um Space por projeto; este workspace é exclusivo do GFM.Template.
- Nunca apontar agentes para `C:\Work\dev\template` ou repositórios de clientes.
- Commits/push apenas com autorização explícita.
- Preservar `leia.txt` e o manual do Herdr (somente leitura).

## Diagnóstico do Herdr (somente leitura)

```powershell
hc --version
Get-Command herdr-app
$env:PATH -split ';' | Where-Object { $_ -match 'herdr' }
```

Se `hc` não for reconhecido em uma nova sessão, ver manual do Herdr, seção 4
(atualização do PATH apenas na sessão atual).

## Pendências

- Space do projeto ainda não configurado (manual, checklist item 201).
- Validar OpenCode autenticado dentro do Herdr antes da Fase 4.
