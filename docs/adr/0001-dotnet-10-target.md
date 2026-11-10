# ADR-0001 — .NET 10 como alvo inicial, com compatibilidade planejada para .NET 8

- **Status:** Proposto (aguarda aprovação)
- **Data:** 10/11/2026

## Contexto

O ambiente possui apenas SDK 10.0.402 e runtimes 8.0.21/10.0.13. Não há SDK 8 instalado.
O template precisa de um alvo moderno, mas alguns consumidores podem exigir .NET 8 (LTS).

## Decisão

- TFM primário: `net10.0`; C# 14.
- Compatibilidade com .NET 8 tratada como **plano**, não multi-target imediato:
  - usar apenas APIs disponíveis em `net8.0` quando o custo for zero;
  - centralizar o TFM em `Directory.Build.props` (`<TargetFramework>` configurável);
  - documentar o procedimento de troca para `net8.0` (requer SDK 8 ou targeting pack);
  - não declarar suporte a .NET 8 até existir build/teste executado nesse TFM.
- Pacotes fixados em versões compatíveis com ambos quando viável.
- `global.json` fixa o SDK 10.0.402 (a definir política de rollForward).

## Alternativas consideradas

1. **Multi-target `net8.0;net10.0` desde o início**: custo de build/teste dobrado sem demanda real.
2. **Alvo `net8.0`**: perde recursos do .NET 10 e exige SDK ausente no ambiente.
3. **Alvo `net9.0`**: versão intermediária sem vantagem (STS encerrado).

## Consequências

- Positivas: stack atual, build único, caminho de downgrade documentado.
- Negativas: "compatível com .NET 8" é afirmação não verificada até teste real.
- Risco: consumidor que exija .NET 8 encontrará atrito; mitigado por TFM centralizado.

## Critérios para reavaliar

- Necessidade concreta de consumidor em .NET 8; ou instalação do SDK 8 e execução de matriz de testes.
