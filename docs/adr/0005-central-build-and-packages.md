# ADR-0005 — SDK e pacotes centralizados; sem MediatR/FluentAssertions

- **Status:** Proposto (aguarda aprovação)
- **Data:** 10/11/2026

## Contexto

Projetos .NET tendem a divergir versões de SDK e pacotes, além de acumular dependências
com licenças restritivas para uso comercial.

## Decisão

- `global.json` fixa o SDK (`10.0.402`), política de rollForward a definir (Q-09).
- `Directory.Build.props`: propriedades comuns (TFM, `Nullable`, `ImplicitUsings`,
  `TreatWarningsAsErrors`, analyzers, geração de documentação, determinismo).
- `Directory.Packages.props`: Central Package Management com versões únicas.
- **Não usar MediatR** (dispatcher mínimo interno) nem **FluentAssertions** (versão recente
  com licença comercial); usar `Assert` do xUnit ou Shouldly (BSD) se necessário.
- Pacotes só entram com justificativa e licença compatível.

## Alternativas consideradas

1. Versões por projeto: simples, porém inconsistente.
2. MediatR/FluentAssertions: ergonomia, mas risco de custo/licença.
3. `dotnet tool` extras obrigatórios: evitar; CI deve funcionar com SDK + restore.

## Consequências

- Positivas: builds reproduzíveis, atualização de pacote em um único lugar.
- Negativas: toda nova dependência exige edição central e aprovação.
- Riscos: pacote transitivo conflitante; mitigado por `dotnet list package --vulnerable`.

## Política de dependências

- Licença permitida: MIT, Apache-2.0, BSD, MS-PL.
- Proibido: licença comercial/dual sem aprovação, pacotes sem manutenção.
- Toda adição relevante é registrada neste ADR ou em novo ADR.
