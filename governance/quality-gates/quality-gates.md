# Quality gates

Fonte executável: `ai/rules/quality-gates.md` e `ai/registry.yaml` (G0–G6).

| Gate | Critério | Evidência |
|---|---|---|
| G0 | Ambiente e escopo verificados | relatório de descoberta |
| G1 | SPEC aprovada | SPEC com aceite testável |
| G2 | ADR estrutural aprovado | ADR aceito |
| G3 | PLAN aprovado | PLAN com fases e gates |
| G4 | TASK autorizada | TASK no formato único |
| G5 | Build/testes verdes | saída real de build/teste |
| G6 | Revisão e segurança aprovadas | pareceres |

## Bloqueios automáticos

- Build com warning.
- Teste falhando.
- `dotnet format` divergente.
- Segredo ou PII no diff.
- Violação de camada.
- Ausência de evidência.

## Regra

Gate não é negociável por prazo. Exceção exige ADR e aprovação humana registrada.
