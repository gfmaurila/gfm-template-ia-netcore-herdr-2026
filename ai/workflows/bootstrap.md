# Workflow — bootstrap

## Objetivo

Iniciar um projeto a partir deste template sem herdar decisões não aprovadas.

## Sequência

1. Copiar estrutura documental e de agentes.
2. Definir nome, domínio neutro e objetivos.
3. Ajustar `AGENTS.md`, `ai/registry.yaml` e índices.
4. Rodar descoberta do ambiente.
5. Produzir SPEC inicial e ADRs fundacionais.
6. Aprovar arquitetura (Fase 3) antes de gerar código.
7. Configurar CI e Compose apenas após aprovação.

## Regras

- Não copiar dados de clientes.
- Não gerar `src/` antes do gate da Fase 3.
- Não instalar ferramentas globalmente.
- Não publicar sem autorização.

## Saída

Template instanciado, documentação coerente e gates definidos.
