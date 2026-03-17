# Architecture Document Template

## Resumen ejecutivo
Describe brevemente el sistema, su propósito y los aspectos más importantes de la arquitectura.

## Objetivo y alcance
### Objetivo
Explica qué sistema, servicio o microservicio se documenta y para qué sirve esta documentación.

### Alcance
#### Incluye
-
-
-

#### No incluye
-
-
-

---

## Contexto del sistema
Describe:
- actores principales
- usuarios o consumidores
- sistemas externos
- dominio funcional
- límites del sistema

### Vista de contexto
```mermaid
flowchart LR
    User[Usuario / Sistema consumidor] --> System[Sistema / Servicio en foco]
    System --> External1[Sistema externo 1]
    System --> External2[Sistema externo 2]
```

---

## Drivers arquitectónicos
Incluye requerimientos o motivadores importantes:
- disponibilidad
- mantenibilidad
- escalabilidad
- seguridad
- rendimiento
- integración
- trazabilidad

| Driver | Descripción | Impacto en arquitectura |
|---|---|---|
|  |  |  |

---

## Restricciones y supuestos

### Restricciones
-
-
-

### Supuestos
-
-
-

---

## Vista de contenedores
Describe los contenedores principales dentro del sistema: aplicaciones, APIs, bases de datos, workers, colas, almacenamiento, etc.

| Contenedor | Tecnología | Responsabilidad | Comunicación |
|---|---|---|---|
| API |  |  |  |
| DB |  |  |  |

### Diagrama de contenedores
```mermaid
flowchart LR
    User[Usuario] --> Web[Web App / Client]
    Web --> API[API / Backend Service]
    API --> DB[(Database)]
    API --> Queue[Queue / Broker]
    API --> External[External Service]
```

---

## Vista de componentes
Usa esta sección si un contenedor requiere más detalle interno.

| Componente | Responsabilidad | Entradas | Salidas |
|---|---|---|---|
| Controller / Handler | | | |
| Service | | | |
| Repository / Client | | | |

### Diagrama de componentes
```mermaid
flowchart TD
    A[Controller] --> B[Service]
    B --> C[Repository]
    B --> D[External Client]
```

---

## Flujos principales / vista runtime

### Flujo principal
1.
2.
3.
4.

### Diagrama dinámico
```mermaid
sequenceDiagram
    participant U as User
    participant A as API
    participant S as Service
    participant D as Database

    U->>A: Request
    A->>S: Validate and process
    S->>D: Read/Write data
    D-->>S: Result
    S-->>A: Response DTO
    A-->>U: HTTP Response
```

---

## Vista de despliegue
Documenta ambientes o nodos relevantes si aplica.

| Nodo / ambiente | Tipo | Contenedores desplegados | Notas |
|---|---|---|---|
| Dev |  |  |  |
| QA |  |  |  |
| Prod |  |  |  |

### Diagrama de despliegue
```mermaid
flowchart TD
    Dev[Development Environment]
    QA[QA Environment]
    Prod[Production Environment]

    Dev --> AppDev[App Instance]
    QA --> AppQA[App Instance]
    Prod --> LB[Load Balancer]
    LB --> App1[App Instance 1]
    LB --> App2[App Instance 2]
    Prod --> DB[(Database)]
```

---

## Datos e integraciones

### Integraciones externas

| Integración | Tipo | Propósito | Protocolo / medio |
|---|---|---|---|
|  | API / DB / Queue / File |  |  |

### Datos relevantes

| Entidad / tabla / recurso | Descripción | Uso |
|---|---|---|
|  |  |  |

### Contratos relevantes

| Contrato | Input | Output | Consumidor |
|---|---|---|---|
| Endpoint / evento / archivo |  |  |  |

---

## Decisiones arquitectónicas relevantes
Lista decisiones importantes o referencia ADRs.

| Decisión | Motivo | Trade-off | Estado |
|---|---|---|---|
|  |  |  | Proposed / Accepted / Deprecated |

---

## Riesgos, trade-offs y deuda técnica

| Tipo | Descripción | Impacto | Mitigación |
|---|---|---|---|
| Riesgo |  |  |  |
| Trade-off |  |  |  |
| Deuda técnica |  |  |  |

---

## Observabilidad, seguridad y escalabilidad

### Observabilidad
- logging
- métricas
- tracing
- alertas

### Seguridad
- autenticación
- autorización
- secretos
- cifrado
- auditoría

### Escalabilidad y resiliencia
- escalado horizontal o vertical
- caché
- colas
- retries
- circuit breakers
- tolerancia a fallos

---

## Glosario

| Término | Definición |
|---|---|
|  |  |

---

## Referencias
- repositorios
- ADRs
- documentación relacionada
- diagramas
- tickets
