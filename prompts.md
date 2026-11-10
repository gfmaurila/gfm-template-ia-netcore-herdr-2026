# prompts.md — Biblioteca de prompts versionados

Prompts reutilizáveis para OpenCode no Herdr. Formato: `PRM-NNN` + versão semântica.
Nunca inclua segredos, PII, dados de cliente ou trechos de código proprietário nos prompts.

Convenções:
- Toda execução de agente deve citar o ID + versão (ex.: `PRM-002@1.0.0`).
- Prompts são versionados em Git (quando o repositório existir) e em `prompts/`.
- Mudança de comportamento = incremento de versão + nota em `docs/ai/prompt-governance.md`.
- Saída deve distinguir **fato verificado**, **inferência** e **pendência**.

---

## PRM-001@1.0.0 — Descoberta somente leitura

**Objetivo:** diagnosticar o workspace sem alterar nada.

```text
Atue como arquiteto. Faça uma auditoria SOMENTE LEITURA do workspace indicado.
Regras: não criar/alterar/excluir arquivos; não inicializar Git; não instalar nada;
não executar comandos destrutivos; não acessar projetos de referência de clientes.
Verifique: SO, PowerShell, .NET SDK/runtimes, Git, Docker (CLI e daemon), Node, OpenCode,
Herdr; conteúdo do diretório; estado do Git; documentos realmente disponíveis.
Saída: tabela componente/versão/status/observação, riscos e pendências.
Classifique cada afirmação como [verificado], [inferido] ou [não verificado].
```

## PRM-002@1.0.0 — Implementar unidade com testes

**Objetivo:** implementar uma unidade pequena, com evidência.

```text
Implemente apenas: <descrição da unidade>.
Contexto: <arquivo/ADR/spec>. Siga a arquitetura aprovada (Domain/Application/
Infrastructure/Host.Api) e as regras de dependência.
Requisitos: incluir testes aplicáveis; não introduzir segredos/PII; não instalar
pacotes sem aprovação; não alterar documentação de decisão sem ADR.
Ao final, execute build e testes reais e reporte:
(1) o que passou, (2) o que falhou, (3) o que não pôde ser validado.
Proibido declarar sucesso sem saída de execução.
```

## PRM-003@1.0.0 — Testes de integração com Testcontainers

```text
Escreva testes de integração para <componente> usando Testcontainers e PostgreSQL.
Regras: banco efêmero por execução; nenhuma dependência de banco corporativo/compartilhado;
limpeza garantida mesmo em falha (Ryuk); migrations aplicadas no fixture; sem dados reais.
Cubra: caminho felizes, erros esperados e contrato HTTP.
Saída: arquivos criados + comandos executados + resultado real.
```

## PRM-004@1.0.0 — Revisão de código

```text
Revise o diff atual como revisor sênior. Verifique: corretude, segurança (segredos/PII/
injeção), limites de camada, concorrência, async/CancellationToken, testabilidade,
observabilidade e complexidade acidental.
Classifique achados em: bloqueante, recomendado, opcional. Cite arquivo:linha.
Não reescreva o código; produza parecer objetivo.
```

## PRM-005@1.0.0 — DevOps local-first

```text
Proponha/ajuste Dockerfile multi-stage, Compose local e workflow GitHub Actions.
Requisitos: restore, build, lint (dotnet format), testes unitários/arquitetura/integração
com Testcontainers e build da imagem; segredos fora do repositório; sem serviços
corporativos; cache de NuGet; artefatos de teste.
Local first -> container first -> cloud ready -> AWS target (documentar, não publicar).
Saída: arquivos + evidência de execução local; nada publicado sem aprovação.
```

## PRM-006@1.0.0 — ADR

```text
Escreva um ADR para a decisão: <título>.
Formato: Contexto, Decisão, Alternativas consideradas, Consequências (positivas/negativas),
Riscos, Status (proposto/aceito/substituído), Data.
Seja específico e evite justificativas genéricas. Se faltar informação, liste perguntas
em vez de presumir aprovação.
```

## PRM-007@1.0.0 — IA opcional e segura

```text
Projete a integração de IA para <caso de uso> respeitando: interfaces na Application,
adaptador na Infrastructure, provider desligado por padrão, timeouts, limite de custo,
fallback, logs sem PII e prompts versionados.
O template básico deve funcionar sem credenciais de IA.
Saída: contratos, fluxo, riscos de privacidade, critérios de teste (incluindo ausência
de configuração) e o que NÃO será implementado agora.
```

## PRM-008@1.0.0 — Blueprint de extensão

```text
Descreva um blueprint para <API | Worker/Batch | aplicação composta | aplicação com IA>.
Inclua: quando usar, estrutura de projetos, dependências, configuração, testes, riscos e
critérios para NÃO criar o projeto agora. Evite projetos vazios: só materialize com
necessidade concreta aprovada.
```
