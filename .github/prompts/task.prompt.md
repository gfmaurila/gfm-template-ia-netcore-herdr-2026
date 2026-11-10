---
description: Decompõe um PLAN em TASKs no formato único.
agent: architect
---

Use o prompt PRM-011@1.0.0 de `ai/prompts/PRM-011@1.0.0.md`.

PLAN: ${input:plan}

Crie as TASKs em `tasks/` seguindo `tasks/TASK-TEMPLATE.md`.
Uma TASK = uma unidade verificável e um único gate. Inclua dependências e evidência exigida.
