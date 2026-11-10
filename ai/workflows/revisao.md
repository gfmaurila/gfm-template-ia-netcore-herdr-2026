# Workflow — revisão

## Objetivo

Avaliar um diff antes de commit/merge.

## Sequência

1. Reviewer analisa corretude, camadas, async e testes.
2. Security Reviewer analisa segredos, auth, PII, injeção e IA.
3. Orchestrator consolida parecer.

## Classificação

- **Bloqueante** — impede merge.
- **Recomendado** — deve ser tratado ou justificado.
- **Opcional** — melhoria.

## Regras

- Revisores não editam código.
- Achados citam `arquivo:linha`.
- Evidência de teste é obrigatória quando aplicável.
- Segredo encontrado interrompe e exige rotação.

## Saída

Parecer: aprovado / aprovado com ressalvas / bloqueado + riscos residuais.
