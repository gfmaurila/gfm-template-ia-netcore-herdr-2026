# ADR-0002 — Monólito modular com módulos em pastas

- **Status:** Proposto (aguarda aprovação)
- **Data:** 10/11/2026

## Contexto

O template deve suportar crescimento por domínio sem explodir em microsserviços prematuros.
Criar um conjunto de projetos por módulo geraria muitos artefatos vazios.

## Decisão

- Adotar **monólito modular**: um processo, módulos com fronteiras explícitas.
- Módulos vivem como pastas/namespaces dentro dos 4 projetos (`Catalog/...`).
- Fronteiras verificadas por testes de arquitetura (sem referência cruzada entre namespaces
  de módulos; comunicação via contratos da `Application`/eventos de integração).
- Um módulo por padrão (`Catalog`); novos módulos só com caso de uso aprovado.
- Extração para assemblies/processos é evolução documentada, não objetivo inicial.

## Alternativas consideradas

1. **Monólito em camadas sem módulos**: simples, mas fronteiras viram convenção frágil.
2. **Um projeto por módulo/camada**: isolamento forte, porém 12+ projetos e build lento.
3. **Microsserviços**: complexidade operacional desproporcional ao estágio.

## Consequências

- Positivas: build rápido, navegação simples, fronteiras testáveis, extração posterior viável.
- Negativas: compilador não impede dependência cruzada; depende de testes.
- Riscos: módulos podem "vazar" se os testes de arquitetura não cobrirem novos namespaces.

## Mitigações

- Teste de arquitetura obrigatório por módulo.
- Revisão de PR exigindo contrato explícito para comunicação entre módulos.
