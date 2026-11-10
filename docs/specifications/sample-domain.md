# Especificação — domínio de exemplo (`Catalog`)

Domínio **neutro e sintético**, sem qualquer dado de cliente. Serve para demonstrar
agregado, value objects, casos de uso, persistência e testes.

## Agregado `Item`

| Campo | Tipo | Regra |
|---|---|---|
| `Id` | `Guid` | Gerado no domínio |
| `Name` | `string` | Obrigatório, 1–120 caracteres, sem espaços nas pontas |
| `Description` | `string?` | Opcional, até 1000 caracteres |
| `Price` | `Money` (VO) | >= 0, moeda ISO 4217, 2 casas decimais |
| `Status` | `ItemStatus` | `Draft` → `Active` → `Archived` |
| `CreatedAtUtc` | `DateTimeOffset` | Definido via `IClock` |
| `UpdatedAtUtc` | `DateTimeOffset?` | Atualizado em alteração |
| `Version` | `uint` | Concorrência otimista (`xmin` no Postgres) |

### Invariantes

- Nome não vazio e dentro do limite.
- Preço não negativo e com moeda válida.
- Transições permitidas: `Draft→Active`, `Active→Archived`; `Archived` é terminal.
- Não é possível renomear item `Archived`.

### Eventos de domínio

- `ItemCreated(ItemId, OccurredAt)`
- `ItemActivated(ItemId, OccurredAt)`
- `ItemArchived(ItemId, OccurredAt)`

## Casos de uso (Application)

| ID | Tipo | Descrição | Erros esperados |
|---|---|---|---|
| UC-01 | Command | Criar item | validação |
| UC-02 | Command | Renomear item | not found, conflito de estado |
| UC-03 | Command | Ativar item | not found, transição inválida |
| UC-04 | Command | Arquivar item | not found, transição inválida |
| UC-05 | Query | Obter item por id | not found |
| UC-06 | Query | Listar itens (paginação/filtro por status) | validação de paginação |

## API (contrato previsto)

| Método | Rota | Sucesso | Erros |
|---|---|---|---|
| POST | `/api/items` | 201 + `Location` | 400, 422 |
| GET | `/api/items/{id}` | 200 | 404 |
| GET | `/api/items?page=1&pageSize=20&status=` | 200 | 400 |
| PATCH | `/api/items/{id}/name` | 200 | 400, 404, 409 |
| POST | `/api/items/{id}/activate` | 200 | 404, 409 |
| POST | `/api/items/{id}/archive` | 200 | 404, 409 |

- Textos de API em inglês (pendente de confirmação — Q-08).
- Erros em `ProblemDetails` com `extensions.code` estável.
- Paginação com `pageSize` máximo de 100.

## Dados de exemplo (seed opcional, dev apenas)

Itens genéricos como `Sample item A/B/C`, sem nomes reais de pessoas, empresas ou produtos
de clientes. Seed só em ambiente de desenvolvimento/teste.

## Fora de escopo do exemplo

- Autenticação/autorização (Q-05).
- Multitenancy, faturamento, integrações externas.
- Upload de arquivos e relatórios.
- Qualquer regra derivada de projetos de referência.
