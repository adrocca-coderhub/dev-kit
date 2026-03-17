# System Context Template

## Objetivo
Mostrar el sistema en foco, sus actores y los sistemas externos con los que interactúa.

## Diagrama
```mermaid
flowchart LR
    User[Usuario / Actor]
    MainSystem[Sistema en foco]
    ExternalA[Sistema externo A]
    ExternalB[Sistema externo B]

    User --> MainSystem
    MainSystem --> ExternalA
    MainSystem --> ExternalB
```

## Qué documentar
- quién usa el sistema
- qué sistemas externos consume o expone
- límites del sistema
- propósito de cada relación
