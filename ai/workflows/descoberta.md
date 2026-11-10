# Workflow — descoberta

## Objetivo

Entender o estado real antes de propor qualquer mudança.

## Fases

1. **Coleta somente leitura** — ambiente, repositório, documentos disponíveis.
2. **Classificação** — cada afirmação como [verificado], [inferido] ou [não validado].
3. **Diagnóstico** — riscos, lacunas e perguntas abertas.
4. **Relatório** — sem alterar arquivos.

## Papéis

- Architect conduz.
- Orchestrator consolida, se houver delegação.

## Gate

Relatório apresentado e aceito. Nenhuma alteração de código nesta fase.

## Saída

`reports/RELATORIO-<timestamp>-DESCOBERTA.txt` com tabela de ambiente, achados e pendências.
