# Dynamic Diagram Template

## Objetivo
Mostrar un flujo relevante paso a paso entre actores, componentes o servicios.

## Diagrama
```mermaid
sequenceDiagram
    participant U as User
    participant FE as Frontend
    participant API as Backend API
    participant S as Service
    participant DB as Database
    participant EXT as External System

    U->>FE: Action
    FE->>API: HTTP Request
    API->>S: Validate and process
    S->>DB: Read/Write
    S->>EXT: External call
    EXT-->>S: Response
    S-->>API: Result
    API-->>FE: HTTP Response
    FE-->>U: Updated state
```

## Qué documentar
- flujo principal
- orden de llamadas
- sincronía o asincronía si importa
- puntos de fallo o dependencias críticas
