# SQL Query Template

```sql
-- Objetivo:
-- Describir qué hace esta consulta.

-- Contexto:
-- Explicar tabla(s), filtro(s) y resultado esperado.

WITH source_data AS (
    SELECT
        t.id,
        t.created_at,
        t.status
    FROM schema.table_name t
    WHERE 1 = 1
      AND t.created_at >= DATE '2026-01-01'
),

filtered_data AS (
    SELECT
        id,
        created_at,
        status
    FROM source_data
    WHERE status IS NOT NULL
)

SELECT
    id,
    created_at,
    status
FROM filtered_data
ORDER BY created_at DESC;
```

## Notas
- Reemplaza `schema.table_name` por la tabla real.
- Documenta filtros importantes.
- Si la query alimenta un proceso, documenta input/output esperado.
