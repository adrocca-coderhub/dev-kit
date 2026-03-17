# Guía de uso del Dev Kit

Cómo usar cada herramienta del dev-kit (prompts, skills, templates, playbooks y agentes) paso a paso, en qué contexto aplicarla y cómo conectarla a tus otros repositorios.

---

## Índice

1. [Cómo funciona cada tipo de herramienta](#1-cómo-funciona-cada-tipo-de-herramienta)
2. [Cómo llevar las herramientas a tus repos](#2-cómo-llevar-las-herramientas-a-tus-repos)
3. [Prompts — guía de uso](#3-prompts--guía-de-uso)
4. [Skills — guía de uso](#4-skills--guía-de-uso)
5. [Templates — guía de uso](#5-templates--guía-de-uso)
6. [Playbooks — guía de uso](#6-playbooks--guía-de-uso)
7. [Agentes OpenCode — guía de uso](#7-agentes-opencode--guía-de-uso)
8. [Slash commands OpenCode — guía de uso](#8-slash-commands-opencode--guía-de-uso)
9. [Plan por tipo de proyecto](#9-plan-por-tipo-de-proyecto)

---

## 1. Cómo funciona cada tipo de herramienta

Antes de ver cada herramienta, es importante entender qué son y dónde se usan:

| Herramienta | Qué es | Dónde se usa | Requiere OpenCode |
|---|---|---|---|
| **Prompt** | Texto completo listo para pegar en una IA | ChatGPT, Claude, Copilot, cualquier IA | No |
| **Skill** | Instrucciones de rol + reglas para la IA | Pegar al inicio de un chat o como system prompt | No |
| **Template** | Estructura Markdown vacía para llenar a mano | GitHub PR, Jira, tu repositorio | No |
| **Playbook** | Checklist de proceso | Seguir paso a paso antes de entregar | No |
| **Agente** | IA especializada configurada en OpenCode | OpenCode únicamente | Sí |
| **Slash command** | Atajo que invoca un agente con instrucciones | OpenCode únicamente | Sí |

**Regla de oro**: Los prompts, skills, templates y playbooks son agnósticos — funcionan en cualquier herramienta de IA o sin IA. Los agentes y slash commands solo funcionan dentro de OpenCode.

---

## 2. Cómo llevar las herramientas a tus repos

### Herramientas agnósticas (prompts, skills, templates, playbooks)

**No necesitas copiarlas al repo destino.** Se usan desde el dev-kit directamente:

1. Abrís el archivo del dev-kit
2. Copiás el contenido
3. Lo pegás en ChatGPT / Claude / Copilot / donde estés trabajando
4. Llenás los placeholders con el contexto de tu proyecto

No hay instalación, no hay configuración. Son archivos de texto reutilizables.

---

### Agentes y slash commands (solo OpenCode)

Los agentes viven en `.opencode/agents/` y los slash commands en `.opencode/commands/`. OpenCode los busca **en el directorio del proyecto donde abrís OpenCode**, no en el dev-kit.

Tenés tres opciones:

#### Opción A — Copiar `.opencode/` a cada proyecto (recomendado)

```
tu-proyecto/
└── .opencode/
    ├── agents/        ← copiar de dev-kit/.opencode/agents/
    └── commands/      ← copiar de dev-kit/.opencode/commands/
```

Pasos:
```bash
# Desde tu proyecto
cp -r C:/Coderhub/dev-kit/.opencode/agents/ .opencode/agents/
cp -r C:/Coderhub/dev-kit/.opencode/commands/ .opencode/commands/
```

Luego abrís OpenCode en tu proyecto y todos los agentes estarán disponibles.

**Cuándo elegir esta opción**: proyectos activos donde vas a usar OpenCode frecuentemente.

---

#### Opción B — Abrir OpenCode desde el dev-kit y referenciar el otro repo

Abrís OpenCode desde el directorio `dev-kit/` y le das contexto del otro repo pegando rutas, código o diff en el chat.

```bash
# Abrís OpenCode en dev-kit
cd C:/Coderhub/dev-kit
opencode
```

Luego en el chat:
```
@docs-writer Generame la documentación de PR para estos cambios: [pegás el diff]
```

**Cuándo elegir esta opción**: uso puntual, proyectos donde no querés agregar configuración.

---

#### Opción C — Personalizar agentes por proyecto

Copiás los agentes al proyecto y modificás el system prompt para que haga referencia a las convenciones específicas de ese proyecto.

```bash
cp C:/Coderhub/dev-kit/.opencode/agents/data-engineer.md mi-proyecto/.opencode/agents/data-engineer.md
```

Luego editás el archivo para reemplazar las referencias a `scripts/` por las rutas reales de tu proyecto.

**Cuándo elegir esta opción**: proyectos con convenciones muy distintas al dev-kit.

---

#### Qué copiar según el tipo de proyecto

| Tipo de proyecto | Agentes esenciales | Slash commands esenciales |
|---|---|---|
| Proyecto Python de datos | `data-engineer`, `data-modeler`, `debugger`, `reviewer`, `docs-writer` | `/pipeline-etl`, `/data-profile`, `/pr-doc`, `/debugging` |
| API / backend | `api-engineer`, `debugger`, `reviewer`, `solution-planner`, `docs-writer` | `/pr-doc`, `/jira-doc`, `/debugging`, `/architecture-doc` |
| Proyecto nuevo | `plan`, `orchestrator`, `solution-planner`, `repo-explorer`, `docs-writer` | `/deep-analysis`, `/onboarding`, `/jira-doc` |
| Cualquier proyecto | `plan`, `build`, `docs-writer`, `reviewer` | `/pr-doc`, `/jira-doc`, `/debugging` |

---

## 3. Prompts — guía de uso

Los prompts son textos completos que pegás en cualquier IA para obtener un resultado específico. La mayoría tienen placeholders entre `[corchetes]` que debés completar con tu contexto.

### `prompts/master/prompt-master.md` — Prompt base universal

**Cuándo usarlo**: cuando ningún prompt específico cubre tu necesidad, o como punto de partida para crear un prompt nuevo.

**Cómo usarlo paso a paso**:

1. Abrí el archivo `prompts/master/prompt-master.md`
2. Copiá todo el contenido
3. Pegalo en ChatGPT / Claude / Copilot
4. Completá cada sección:

```
Quiero que actúes como [ingeniera de datos senior]

## Objetivo
Necesito [un script Python que limpie columnas nulas y duplique registros en un CSV]

## Contexto
- Proyecto: sistema de facturación
- Módulo o área: preprocesamiento de datos
- Lenguaje / stack: Python 3.9, pandas
- Estado actual: tengo el CSV crudo con nulos y duplicados
- Restricciones: no usar librerías externas salvo pandas

## Input disponible
- Archivos: ventas_2024.csv con columnas: id, monto, fecha, cliente_id
...
```

5. Enviá y obtenés la respuesta estructurada

**Regla**: nunca mandés el prompt con los placeholders vacíos. Si no tenés el dato, escribí "no disponible" o "no aplica".

---

### `prompts/data/etl-generator-prompt.md` — Generar un ETL

**Cuándo usarlo**: cuando necesitás un script ETL base para un proyecto nuevo o para documentar un flujo existente.

**Pasos**:

1. Copiá el contenido del archivo
2. En la sección `## Contexto` al final, pegá:
   - La fuente de datos (CSV, API, tabla)
   - Las columnas del input
   - Qué transformaciones necesitás
   - El destino (CSV, tabla, API)
3. Pegá todo en tu IA
4. Obtenés: estructura de archivos, funciones base, ejemplos de input/output

**Ejemplo de contexto a pegar**:
```
Fuente: archivo CSV con columnas order_id (string), amount (float), date (string YYYY-MM-DD), status (string)
Transformaciones: parsear date a datetime, filtrar status != 'cancelled', calcular amount_usd = amount * 0.85
Destino: archivo CSV limpio para carga en base de datos
```

---

### `prompts/data/data-profiling-prompt.md` — Analizar un dataset

**Cuándo usarlo**: antes de trabajar con un dataset desconocido, para entender su estructura.

**Pasos**:

1. Copiá el prompt
2. Pegá una muestra del CSV o descripción de las columnas
3. La IA entrega: tipos por columna, nulos, duplicados, distribuciones, anomalías

---

### `prompts/data/load-script-prompt.md` — Script de carga

**Cuándo usarlo**: para generar el script que carga datos procesados a un destino.

**Pasos**: igual que ETL, completar el contexto con fuente, destino y configuración de la carga.

---

### `prompts/github/pr-doc-prompt.md` — Documentación de PR

**Cuándo usarlo**: cuando terminaste un cambio y necesitás documentarlo para GitHub.

**Pasos**:

1. Copiá el prompt completo
2. En `## Contexto del cambio` pegá la descripción de qué hiciste
3. En `## Archivos modificados` pegá la lista de archivos (podés usar `git diff --name-only`)
4. En `## Detalles funcionales o técnicos` pegá el diff o tus notas
5. Mandalo a la IA
6. Copiá el resultado y pegalo directo en la descripción de la PR en GitHub

---

### `prompts/jira/jira-doc-prompt.md` — Documentación de ticket Jira

**Cuándo usarlo**: antes de abrir un ticket o para documentar uno existente.

**Pasos**:

1. Copiá el prompt
2. Completá con: descripción del requerimiento, archivos involucrados, reglas de negocio
3. Mandalo a la IA
4. Copiá el resultado y pegalo en la descripción del ticket Jira

---

### `prompts/analysis/deep-analysis-prompt.md` — Análisis profundo

**Cuándo usarlo**: cuando llegás a un repositorio o módulo desconocido y necesitás entenderlo rápido.

**Pasos**:

1. Copiá el prompt
2. Pegá el contenido del `README.md` del proyecto objetivo, la estructura de directorios y los archivos más relevantes
3. La IA entrega: mapa de módulos, flujos, dependencias, riesgos y próximos pasos

---

### `prompts/architecture/adr-prompt.md` — Crear un ADR

**Cuándo usarlo**: cuando tomás una decisión de arquitectura importante y querés registrarla.

**Pasos**:

1. Copiá el prompt
2. Describí la decisión que tomaste y por qué (ej. "decidí usar CSV en lugar de base de datos porque el volumen es bajo y no hay infraestructura disponible")
3. La IA genera el ADR completo con contexto, opciones consideradas, consecuencias y riesgos

---

### `prompts/debugging/debugging-prompt.md` — Analizar un bug

**Cuándo usarlo**: cuando tenés un error y no entendés la causa raíz.

**Pasos**:

1. Copiá el prompt
2. Pegá: el mensaje de error, el stack trace, el código donde falla, el comportamiento esperado
3. La IA entrega: hipótesis ordenadas por probabilidad, pasos de validación y solución propuesta

---

## 4. Skills — guía de uso

Las skills son instrucciones de rol más detalladas que los prompts. En lugar de describir qué hacer, le dicen a la IA **cómo comportarse** durante toda la conversación.

**Diferencia clave con los prompts**:
- Un **prompt** dice "hacé X con este input"
- Una **skill** dice "sos una experta en X, seguí estas reglas, usá esta estructura"

**Cómo usar una skill**:

1. Abrís la skill en el dev-kit
2. Copiás **todo el contenido** (incluyendo el Prompt base reutilizable al final)
3. Lo pegás **al inicio** de un chat nuevo en ChatGPT / Claude / Copilot
4. La IA adopta ese rol para toda la conversación
5. Luego le das el contexto de tu tarea específica

---

### `skills/pr/pr-doc-skill.md` — Especialista en documentación de PR

**Cuándo usarla**: sesión dedicada a documentar una o varias PRs.

**Pasos**:

1. Abrí una conversación nueva en tu IA
2. Pegá todo el contenido de `pr-doc-skill.md`
3. La IA confirma el rol adoptado
4. Luego mandás:
   ```
   Aquí está mi contexto:
   - Cambié el script preprocess.py para agregar normalización de fechas
   - Agregué el archivo validators.py con validación de schema
   - El CSV de entrada tiene columnas: id, fecha, monto
   
   Archivos modificados: [lista]
   ```
5. La IA genera la PR completa con todas las secciones

---

### `skills/jira/jira-doc-skill.md` — Especialista en documentación Jira

**Cuándo usarla**: cuando necesitás redactar una tarjeta Jira completa con diagrama, criterios de aceptación y toda la estructura.

**Pasos**:

1. Abrí chat nuevo, pegá la skill
2. En `## Contexto base` escribí qué hace el ticket
3. En `## Información técnica` pegá archivos, tablas, scripts involucrados
4. En `## Detalles funcionales` pegá las reglas de negocio
5. La IA genera el ticket listo para pegar

---

### `skills/data/etl-transform-skill.md` — Diseño de transformaciones ETL

**Cuándo usarla**: cuando necesitás diseñar o documentar la etapa de transformación de un pipeline.

**Pasos**:

1. Pegá la skill en un chat nuevo
2. Describí: fuente de datos, columnas de entrada, reglas de transformación, columnas de salida
3. Obtenés: mapeo origen-destino, reglas documentadas, ejemplos y estructura de código

---

### `skills/data/data-preprocessing-skill.md` — Preprocesamiento

**Cuándo usarla**: para diseñar o documentar la etapa de limpieza y normalización de datos.

**Pasos**: igual a la skill de ETL, enfocada en limpieza, nulos, duplicados y normalización de formatos.

---

### `skills/data/data-load-skill.md` — Carga de datos

**Cuándo usarla**: para diseñar la etapa de carga (CSV, base de datos, API).

**Pasos**: describís la fuente procesada, el destino y las restricciones de carga (upsert, truncate, append, etc.).

---

### `skills/analysis/deep-analysis-skill.md` — Análisis técnico profundo

**Cuándo usarla**: cuando necesitás que la IA sea muy rigurosa al analizar un módulo o repo.

**Pasos**:

1. Pegá la skill en un chat nuevo
2. Pegá el contenido del repo: estructura de directorios, archivos clave, README
3. La IA entrega: mapa de responsabilidades, flujos, riesgos, deuda técnica, próximos pasos

---

### `skills/debugging/debugging-skill.md` — Debugging estructurado

**Cuándo usarla**: cuando un bug no es obvio y necesitás un análisis riguroso.

**Pasos**:

1. Pegá la skill
2. Pegá: error, stack trace, comportamiento esperado vs actual, código involucrado
3. La IA no te da la solución directo — primero formula hipótesis y pasos de validación

---

### `skills/architecture/adr-skill.md` y `architecture-doc-skill.md`

**Cuándo usarlas**: para documentar una decisión arquitectural (ADR) o la arquitectura completa de un servicio.

**Pasos**:

1. Pegá la skill correspondiente
2. Para ADR: describí la decisión, las opciones que evaluaste y por qué elegiste la que elegiste
3. Para arquitectura: pegá el código o descripción del sistema
4. Obtenés documentación lista con diagramas Mermaid

---

## 5. Templates — guía de uso

Los templates son estructuras Markdown vacías que vos completás a mano o con ayuda de una IA. Son el "molde" del documento final.

**Filosofía de uso**: los templates definen **qué secciones debe tener** un documento. Los prompts y skills definen **cómo generarlo**. Se usan juntos o por separado.

---

### `templates/pr/pr-doc-template.md` — Documentación de PR

**Cuándo usarlo**: cuando preferís llenar la PR a mano en lugar de usar una IA, o como referencia de qué secciones incluir.

**Pasos**:

1. Copiá el archivo a tu proyecto (o abrilo como referencia)
2. Completá cada sección:
   - `# Resumen` — 3-6 bullets con qué cambia
   - `# Archivos modificados` — una fila por archivo
   - `# Descripción detallada` — una sección por funcionalidad o cambio
   - `# Flujo funcional` — pasos + diagrama Mermaid
   - `# Contrato funcional` — input/output con ejemplos JSON
   - `# Casos representativos` — al menos un caso exitoso y uno de error
3. Pegá el resultado en la descripción de la PR en GitHub

**Tip**: usar el prompt `pr-doc-prompt.md` + este template como referencia de estructura produce el mejor resultado.

---

### `templates/jira/jira-doc-template.md` — Ticket Jira

**Cuándo usarlo**: como referencia de estructura al redactar tickets.

**Pasos**: igual que la PR — completar sección por sección o usar la skill `jira-doc-skill.md` para que la IA lo llene.

---

### `templates/python/script-template.py.md` — Script Python base

**Cuándo usarlo**: al crear un script Python nuevo en cualquier proyecto.

**Pasos**:

1. Abrí el archivo — el contenido dentro del bloque de código es el script completo
2. Copiá el código Python (sin el wrapper Markdown)
3. Pegalo como archivo `.py` en tu proyecto:
   ```bash
   # Creá el archivo directamente
   cp /ruta/al/script.py mi-proyecto/scripts/mi_script.py
   ```
4. Reemplazá:
   - El docstring del módulo con la descripción real
   - `"base_script"` en `getLogger` por el nombre de tu script
   - La función `process()` con tu lógica
5. Verificá que pase lint: `ruff check mi_script.py` y tipos: `mypy mi_script.py`

**Estructura que provee el template**:
- `parse_args()` — argumentos de línea de comandos
- `validate_input()` — validación de ruta de entrada
- `process()` — lógica principal con logging
- `main()` — orquestación con manejo de errores
- `sys.exit(main())` — patrón de salida correcto

---

### `templates/data/etl-template.md` — Documentación de ETL

**Cuándo usarlo**: para documentar un pipeline ETL antes o después de implementarlo.

**Pasos**:

1. Copiá el template a `docs/` de tu proyecto como `etl-[nombre].md`
2. Completá:
   - Flujo general (los 7 pasos ya están incluidos, ajustá si aplica)
   - Diagrama Mermaid (ya hay uno base, extendelo)
   - Fuente y destino (tabla con tipo y descripción)
   - Contrato de entrada (tabla de columnas + ejemplo JSON)
   - Contrato de salida (tabla + ejemplos JSON éxito/error)
   - Estructura de archivos (qué módulos existen)
   - Reglas de negocio, validaciones, logging, riesgos
3. Vinculá este doc desde la PR si es un ETL nuevo

---

### `templates/data/preprocess-template.md` y `load-template.md`

**Cuándo usarlos**: para documentar la etapa de preprocesamiento o carga específicamente, cuando son scripts separados del ETL principal.

**Pasos**: igual que el ETL template — copiar, completar, vincular desde la PR.

---

### `templates/debugging/debugging-template.md` — Análisis de bug

**Cuándo usarlo**: cuando necesitás documentar la investigación de un bug (para un ticket Jira o para que otro dev entienda el problema).

**Pasos**:

1. Copiá el template
2. Completá: resumen, comportamiento esperado vs actual, evidencia (error + logs), hipótesis, pasos de validación, solución propuesta
3. Pegalo en la descripción del ticket de bug en Jira o como comentario en la PR

---

### `templates/adr/adr-template.md` — Architecture Decision Record

**Cuándo usarlo**: cuando tomás una decisión que afecta la estructura del proyecto (tecnología, patrón, enfoque) y querés registrarla para el futuro.

**Pasos**:

1. Copiá el template a `docs/decisions/` de tu proyecto
2. Nombralo como `NNNN-titulo-kebab-case.md` (ej. `0001-usar-csv-en-lugar-de-sqlite.md`)
3. Completá:
   - Estado: `Proposed` mientras se discute, `Accepted` cuando se decide
   - Contexto y problema: ¿qué situación motivó esta decisión?
   - Opciones consideradas: listá al menos 2-3 alternativas
   - Decisión tomada + justificación
   - Consecuencias positivas, negativas, trade-offs y riesgos
4. Commitealo junto con el código que implementa la decisión

---

### `templates/analysis/deep-analysis-template.md` — Análisis de repositorio

**Cuándo usarlo**: al hacer onboarding en un repo nuevo, como estructura para tomar notas.

**Pasos**: completar mientras explorás el repo, o pedirle a la IA que lo llene con la skill `deep-analysis-skill.md`.

---

### `templates/architecture/architecture-doc-template.md` — Documentación de arquitectura

**Cuándo usarlo**: para documentar la arquitectura de un servicio o sistema.

**Pasos**: completar sección por sección o usar el prompt `architecture-doc-prompt.md` con la IA.

---

### `templates/mermaid/flowchart-template.md` — Diagrama de flujo

**Cuándo usarlo**: como referencia de sintaxis Mermaid cuando necesitás agregar un diagrama a cualquier documento.

**Cómo usarlo**: copiar el bloque de ejemplo y adaptarlo. Los nodos usan `[ ]` para rectángulos, `( )` para estadios redondeados, `{ }` para rombos de decisión, `[( )]` para bases de datos y `([ ])` para terminales.

---

### `templates/sql/query-template.sql.md` — Query SQL documentada

**Cuándo usarlo**: cuando necesitás documentar una query SQL compleja con su propósito, inputs y outputs.

---

### `templates/typescript/module-template.ts.md` — Módulo TypeScript base

**Cuándo usarlo**: al crear un módulo TypeScript nuevo en un proyecto frontend o backend TS.

**Pasos**: igual que el template Python — copiar el código, adaptar imports y lógica.

---

### `templates/readme/README-template.md` — README de proyecto

**Cuándo usarlo**: al crear o actualizar el README de un proyecto nuevo.

**Pasos**: copiar a la raíz del proyecto como `README.md` y completar cada sección.

---

## 6. Playbooks — guía de uso

Los playbooks son checklists de proceso — no generan contenido, sino que te guían para no olvidar pasos importantes.

**Cómo usarlos**: abrirlos antes o durante una tarea y ir marcando cada ítem mientras trabajás.

---

### `playbooks/pr-checklist.md` — Antes de abrir una PR

**Cuándo usarlo**: justo antes de abrir la PR, después de terminar el código.

**Pasos**:

1. Abrí el playbook
2. Verificá cada ítem de "Antes de redactar la PR" — si no podés marcar uno, completá esa información primero
3. Documentá cada archivo modificado con la tabla del template
4. Verificá el contenido mínimo de la PR (todos los ítems de la sección "Contenido mínimo")
5. Revisión final antes de pegar

---

### `playbooks/jira-checklist.md` — Antes de crear un ticket

**Cuándo usarlo**: antes de abrir un ticket en Jira.

**Pasos**: seguir la lista para asegurarte de que el ticket tiene contexto suficiente, criterios de aceptación y flujo documentado.

---

### `playbooks/delivery-checklist.md` — Antes de un entregable

**Cuándo usarlo**: antes de considerar terminada una feature o sprint.

---

### `playbooks/release-checklist.md` — Antes de un release

**Cuándo usarlo**: antes de hacer un release a producción.

---

### `playbooks/onboarding.md` — Al empezar en un proyecto nuevo

**Cuándo usarlo**: los primeros días en un proyecto, para asegurarte de cubrir todos los aspectos de onboarding.

---

## 7. Agentes OpenCode — guía de uso

Los agentes son IAs especializadas que viven en `.opencode/agents/`. Solo funcionan dentro de OpenCode.

### Prerrequisito: tener OpenCode instalado y activo

Verificá que OpenCode está corriendo en el directorio del proyecto:
```bash
# En el directorio de tu proyecto (que tenga .opencode/agents/)
opencode
```

Si el directorio `.opencode/agents/` existe, los agentes están disponibles automáticamente. No hay instalación adicional.

---

### Invocar un agente: dos formas

**Forma 1 — Con `@` (para toda la conversación)**
```
@data-engineer Necesito un script que limpie nulos y duplique registros del CSV ventas.csv
```
El agente maneja toda la conversación hasta que cambiés de agente.

**Forma 2 — Automático desde un slash command**
Los slash commands tienen `agent:` en su frontmatter, lo que invoca al agente correcto automáticamente:
```
/pipeline-etl  ← invoca @build automáticamente
/debugging     ← invoca @plan automáticamente
```

---

### `@plan` — Para empezar cualquier tarea compleja

**Cuándo usarlo**: antes de implementar algo para entender qué hay que hacer.

```
@plan Necesito agregar validación de fechas al script preprocess.py.
Actualmente acepta cualquier string en la columna 'date'. 
Quiero que valide formato ISO 8601 y rechace registros con fecha futura.
```

**Qué hace**: lee el código existente, analiza el impacto, entrega un plan con tareas ordenadas y criterios de aceptación. **No modifica archivos.**

---

### `@build` — Para implementar código

**Cuándo usarlo**: cuando ya sabés qué hacer (idealmente después de `@plan`).

```
@build Implementa la validación de fechas en preprocess.py siguiendo el plan acordado.
Asegurate de usar el logger de scripts/utils/logger.py y agregar type hints.
```

**Qué hace**: edita los archivos, verifica con ruff y mypy, entrega el código listo.

---

### `@orchestrator` — Para tareas que involucran varios dominios

**Cuándo usarlo**: cuando la tarea es compleja y no es obvio por dónde empezar.

```
@orchestrator Necesito crear un nuevo script ETL para procesar pedidos desde un CSV,
documentarlo con un ticket Jira y revisar el código antes de la PR.
```

**Qué hace**: descompone la tarea, delega en `data-engineer` → `reviewer` → `docs-writer` en orden, entrega el resultado integrado.

---

### `@repo-explorer` — Para entender un repositorio

**Cuándo usarlo**: al llegar a un proyecto nuevo o antes de planificar un cambio.

```
@repo-explorer Explorá la estructura del repositorio y decime:
- qué hace cada script en scripts/
- qué hay en templates/
- qué brechas de documentación existen
```

**Qué hace**: solo lee, nunca modifica. Entrega un mapa completo.

---

### `@solution-planner` — Para diseñar una solución antes de codificar

**Cuándo usarlo**: cuando el qué está claro pero el cómo no.

```
@solution-planner Necesito refactorizar pipeline_etl.py para que sea testeable.
Actualmente todo está en un solo bloque. Divide en fases con criterios de aceptación.
```

**Qué hace**: entrega fases, componentes, dependencias, riesgos y preguntas abiertas. No escribe código.

---

### `@data-engineer` — Para scripts de datos

**Cuándo usarlo**: para crear o mejorar scripts ETL, preprocesamiento o carga.

```
@data-engineer Creá un script de preprocesamiento que:
- limpie nulos en las columnas amount y date
- normalice date a formato YYYY-MM-DD
- elimine duplicados por order_id
Input: CSV con columnas order_id, amount, date, status
Output: CSV limpio
```

**Qué hace**: implementa el script en `scripts/`, siguiendo las convenciones (type hints, logging, patrón `main()`, respuestas estructuradas).

---

### `@data-modeler` — Para definir schemas antes de implementar

**Cuándo usarlo**: antes de que `@data-engineer` implemente, para definir qué columnas se esperan.

```
@data-modeler Definí el schema para el dataset de pedidos.
Columnas disponibles: order_id, amount, date, status, customer_id, discount.
El pipeline requiere order_id, amount y date como obligatorios.
```

**Qué hace**: entrega schema JSON, TypedDicts de Python y ejemplos representativos.

---

### `@debugger` — Para investigar errores

**Cuándo usarlo**: cuando hay un error y no es obvio qué lo causa.

```
@debugger Tengo este error al correr pipeline_etl.py:

KeyError: 'order_id'
  File "scripts/etl/pipeline_etl.py", line 45, in transform
    record['order_id']

El CSV tiene columnas: id, amount, date (nota: la columna se llama 'id' no 'order_id')
```

**Qué hace**: analiza el error, propone hipótesis ordenadas por probabilidad, pasos de validación y el fix. **No aplica cambios sin preguntar.**

---

### `@api-engineer` — Para endpoints y contratos de API

**Cuándo usarlo**: al diseñar o implementar endpoints.

```
@api-engineer Diseñá el endpoint GET /api/v1/orders/{order_id} que devuelva
el detalle de un pedido. Si no existe, debe retornar 404 con error estructurado.
```

**Qué hace**: define el contrato request/response, implementa el handler con manejo de errores estándar.

---

### `@architecture-analyst` — Para documentar arquitectura

**Cuándo usarlo**: cuando necesitás documentar cómo funciona un sistema existente.

```
@architecture-analyst Documentá la arquitectura del sistema de procesamiento de datos.
Los scripts son: pipeline_etl.py, preprocess.py, load.py, validate_schema.py.
Usá modelo C4 simplificado con diagramas Mermaid.
```

**Qué hace**: crea documentación de arquitectura en `docs/`, con diagramas y ADRs si aplica.

---

### `@docs-writer` — Para documentación técnica

**Cuándo usarlo**: para generar PRs, tickets Jira, ADRs o cualquier documentación en español.

```
@docs-writer Generame la documentación de PR para estos cambios:
- Modifiqué preprocess.py para agregar validación de fechas
- Agregué validate_schema.py con validación de columnas requeridas
Los cambios afectan el pipeline de pedidos que corre diariamente.
```

**Qué hace**: genera el documento completo en Markdown siguiendo la plantilla correcta.

---

### `@reviewer` — Para revisar antes del merge

**Cuándo usarlo**: después de terminar código, antes de abrir la PR.

```
@reviewer Revisá el script que acabo de implementar en scripts/preprocess/preprocess.py.
Chequeá: type hints, manejo de errores, logging, convenciones del dev-kit.
```

**Qué hace**: entrega un informe con hallazgos priorizados (crítico / mayor / menor / sugerencia) con ruta:línea. **No modifica archivos.**

---

### `@agent-systems` — Para mejorar el sistema de agentes

**Cuándo usarlo**: cuando querés agregar un agente nuevo o mejorar uno existente.

```
@agent-systems Necesito un agente especializado en escribir queries SQL optimizadas.
¿Cómo lo definirías? ¿Qué permisos necesita?
```

---

## 8. Slash commands OpenCode — guía de uso

Los slash commands son atajos que combinan un agente con instrucciones predefinidas. Se invocan con `/nombre-del-comando` dentro de OpenCode.

### Cómo invocar un slash command

```
/pr-doc
```

OpenCode ejecuta las instrucciones del comando con el contexto actual del repositorio.

Podés pasar contexto adicional:
```
/pr-doc Los cambios son solo en scripts/preprocess.py y agregan validación de fechas
```

---

### `/pr-doc` — Documentación de PR

**Invoca**: `@build` (agente de implementación con capacidad de leer git)

**Cuándo usarlo**: cuando terminás un cambio y querés la documentación lista para copiar en GitHub.

**Pasos**:
1. Terminá tus cambios en el código
2. En OpenCode, escribí `/pr-doc`
3. OpenCode lee el repositorio y genera la documentación con todas las secciones
4. Copiá el resultado y pegalo en la descripción de la PR en GitHub

---

### `/jira-doc` — Ticket Jira

**Invoca**: `@build`

**Cuándo usarlo**: antes de abrir un ticket o para documentar trabajo completado.

**Pasos**:
1. Describí qué hiciste o qué vas a hacer
2. Escribí `/jira-doc`
3. Copiá el resultado en Jira

---

### `/debugging` — Análisis de bug

**Invoca**: `@plan`

**Cuándo usarlo**: cuando tenés un error y necesitás un análisis estructurado.

**Pasos**:
1. Pegá el error, stack trace y descripción del comportamiento esperado
2. Escribí `/debugging`
3. OpenCode entrega análisis estructurado con hipótesis y pasos de validación

---

### `/pipeline-etl` — Generar o planificar un ETL

**Invoca**: `@build`

**Cuándo usarlo**: para crear un nuevo pipeline ETL o planificar las etapas de uno existente.

**Pasos**:
1. Describí la fuente, las transformaciones y el destino
2. Escribí `/pipeline-etl`
3. OpenCode genera el script base o el plan del pipeline

---

### `/data-profile` — Profiling de dataset

**Invoca**: `@build`

**Cuándo usarlo**: cuando llegás a un dataset nuevo y necesitás un script de análisis rápido.

**Pasos**:
1. Indicá la ruta al CSV o describe las columnas disponibles
2. Escribí `/data-profile`
3. OpenCode genera o usa `profile_dataset.py` para analizar el dataset

---

### `/deep-analysis` — Análisis profundo de código o módulo

**Invoca**: `@plan`

**Cuándo usarlo**: al llegar a un proyecto nuevo o antes de hacer un cambio complejo.

**Pasos**:
1. Escribí `/deep-analysis`
2. OpenCode analiza el repositorio actual y entrega: mapa de módulos, flujos, riesgos, deuda técnica y próximos pasos

---

### `/architecture-doc` — Documentar arquitectura

**Invoca**: `@plan`

**Cuándo usarlo**: para generar documentación de arquitectura del sistema o servicio actual.

**Pasos**:
1. Escribí `/architecture-doc`
2. OpenCode genera documentación C4 con diagramas Mermaid

---

### `/adr` — Crear un ADR

**Invoca**: `@plan`

**Cuándo usarlo**: después de tomar una decisión arquitectural importante.

**Pasos**:
1. Describí la decisión: qué decidiste y por qué
2. Escribí `/adr`
3. OpenCode genera el ADR completo para guardar en `docs/decisions/`

---

### `/onboarding` — Documentación de onboarding

**Invoca**: `@build`

**Cuándo usarlo**: para generar guía de onboarding del proyecto actual.

**Pasos**:
1. Escribí `/onboarding`
2. OpenCode analiza el repositorio y genera una guía para nuevos integrantes

---

### `/release-notes` — Notas de release

**Invoca**: `@build`

**Cuándo usarlo**: antes de un release para generar las notas de cambios.

**Pasos**:
1. Describí los cambios incluidos en el release (o dejá que OpenCode lea el git log)
2. Escribí `/release-notes`
3. OpenCode genera las notas de release en Markdown

---

## 9. Plan por tipo de proyecto

### Proyecto Python de datos (ETL / análisis)

**Setup inicial (una sola vez)**:
```bash
# Copiá los agentes y comandos al proyecto
cp -r C:/Coderhub/dev-kit/.opencode/ mi-proyecto-datos/.opencode/
```

**Workflow por tarea**:

| Situación | Herramienta a usar |
|---|---|
| Nuevo dataset desconocido | `@repo-explorer` o `/deep-analysis` |
| Diseñar pipeline nuevo | `@solution-planner` → `@data-modeler` → `@data-engineer` |
| Implementar script | `/pipeline-etl` o `@data-engineer` + `scripts/etl/pipeline_etl.py` como base |
| Nuevo script Python | Copiar `templates/python/script-template.py.md`, adaptar |
| Bug en un script | `/debugging` o `@debugger` |
| Documentar el ETL | `@docs-writer` o skill `etl-transform-skill.md` |
| Abrir PR | `/pr-doc` o prompt `pr-doc-prompt.md` |
| Crear ticket Jira | `/jira-doc` o skill `jira-doc-skill.md` |
| Revisar antes del merge | `@reviewer` |

---

### Proyecto API / backend

**Setup inicial**:
```bash
cp -r C:/Coderhub/dev-kit/.opencode/ mi-api/.opencode/
```

**Workflow por tarea**:

| Situación | Herramienta a usar |
|---|---|
| Diseñar endpoint nuevo | `@api-engineer` |
| Definir contrato request/response | `@data-modeler` |
| Implementar handler | `@build` |
| Error en endpoint | `@debugger` |
| Documentar arquitectura | `/architecture-doc` o `@architecture-analyst` |
| Decisión de diseño relevante | `/adr` o `@architecture-analyst` |
| Abrir PR | `/pr-doc` |
| Crear ticket | `/jira-doc` |
| Revisar código | `@reviewer` |

---

### Proyecto nuevo desde cero

**Workflow**:

1. Definir qué construir:
   ```
   @solution-planner Necesito construir [descripción]. Propone arquitectura, fases y criterios.
   ```

2. Documentar la arquitectura inicial:
   ```
   /architecture-doc
   ```

3. Si hay decisiones importantes, registrarlas:
   ```
   /adr [descripción de la decisión]
   ```

4. Crear el README del proyecto:
   - Copiar `templates/readme/README-template.md` al nuevo repo

5. Implementar usando `@build` o agentes especializados según el dominio

6. Documentar el primer entregable:
   ```
   /pr-doc
   ```

---

### Onboarding a un proyecto existente

1. Usar `@repo-explorer` o `/deep-analysis` para entender la estructura
2. Usar `/onboarding` para generar documentación de onboarding
3. Copiar `templates/analysis/deep-analysis-template.md` como base para notas personales
4. Si hay brechas de documentación, usar `@docs-writer` para crearla

---

## Resumen: regla para elegir la herramienta correcta

```
¿Estás en OpenCode?
├── Sí → Usar agentes (@) y slash commands (/)
└── No → Usar prompts o skills en cualquier IA
        ├── Necesitás generar un documento completo → Prompt o skill
        ├── Necesitás llenar un doc a mano → Template
        └── Necesitás verificar que no te falta nada → Playbook
```

Y para llevar las herramientas a otro repo:
```
¿Son agentes o slash commands?
├── Sí → cp -r dev-kit/.opencode/ mi-proyecto/.opencode/
└── No (prompts, skills, templates, playbooks)
    └── Copiar el archivo al portapapeles y pegar donde necesitás
        No hace falta instalación ni configuración
```
