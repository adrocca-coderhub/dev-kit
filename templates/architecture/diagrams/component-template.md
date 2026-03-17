# Component Diagram Template

## Objetivo
Mostrar componentes internos relevantes dentro de un contenedor.

## Diagrama
```mermaid
flowchart TD
    Controller[Controller / Handler]
    Service[Service]
    Repository[Repository]
    Client[External Client]
    Mapper[Mapper / Adapter]

    Controller --> Service
    Service --> Repository
    Service --> Client
    Service --> Mapper
```

## Qué documentar
- responsabilidad de cada componente
- dependencias internas
- límites entre capas
- puntos de entrada y salida
