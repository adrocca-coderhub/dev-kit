# Deployment Diagram Template

## Objetivo
Mostrar cómo se despliega el sistema en ambientes o nodos relevantes.

## Diagrama
```mermaid
flowchart TD
    Internet[Internet / Users]
    LB[Load Balancer]
    App1[App Instance 1]
    App2[App Instance 2]
    DB[(Database)]
    Queue[Queue]
    Monitor[Monitoring]

    Internet --> LB
    LB --> App1
    LB --> App2
    App1 --> DB
    App2 --> DB
    App1 --> Queue
    App2 --> Queue
    App1 --> Monitor
    App2 --> Monitor
```

## Qué documentar
- ambientes relevantes
- nodos o servicios desplegados
- componentes compartidos
- escalado y alta disponibilidad si aplica
