---
description: Orquestra um ciclo no Herdr com delegação, gates e relatório.
argument-hint: <ciclo>
---

Use o prompt PRM-014@1.0.0 de `ai/prompts/PRM-014@1.0.0.md`.

Ciclo: $ARGUMENTS

Leia `ai/registry.yaml` e as TASKs do ciclo. Monte o plano de delegação, execute com
`hc run --bg`, acompanhe com `hc wait --children all` e consolide o relatório em `reports/`.
Não implemente diretamente e não aprove gates em nome do responsável humano.
