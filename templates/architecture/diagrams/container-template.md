# Container Diagram Template

## Objetivo
Mostrar los contenedores principales del sistema y cómo se comunican.

## Diagrama
```mermaid
flowchart LR
    User[Usuario]
    Web[Web App / Frontend]
    API[Backend API]
    Worker[Worker / Job]
    DB[(Database)]
    Queue[Queue / Broker]
    External[External Service]

    User --> Web
    Web --> API
    API --> DB
    API --> Queue
    Worker --> Queue
    Worker --> DB
    API --> External
```

## Qué documentar
- responsabilidad de cada contenedor
- tecnología principal
- protocolo o medio de comunicación
- datos o eventos intercambiados
