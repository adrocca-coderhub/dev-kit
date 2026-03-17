# Mermaid Flowchart Template

## Plantilla base
```mermaid
flowchart TD
    A[Inicio] --> B[Recepción de input]
    B --> C{¿Validación correcta?}
    C -- Sí --> D[Procesamiento]
    C -- No --> E[Error controlado]
    D --> F[Generación de output]
    F --> G[Fin]
    E --> G
```

## Variantes útiles

### Flujo lineal
```mermaid
flowchart LR
    A[Inicio] --> B[Paso 1] --> C[Paso 2] --> D[Fin]
```

### Flujo con decisiones
```mermaid
flowchart TD
    A[Inicio] --> B{Condición}
    B -- Sí --> C[Acción A]
    B -- No --> D[Acción B]
    C --> E[Fin]
    D --> E
```

### Flujo ETL
```mermaid
flowchart TD
    A[Fuente] --> B[Extract]
    B --> C[Validate]
    C --> D[Preprocess]
    D --> E[Transform]
    E --> F[Load]
    F --> G[Reporte]
```

## Buenas prácticas
- Usa nombres cortos pero claros.
- No hagas diagramas gigantes si pueden dividirse.
- Usa decisiones solo cuando aporten claridad.
- Mantén consistencia en nombres de pasos.
