# Kit Index

## Objetivo
Este documento sirve como mapa maestro del `dev-kit`, explicando qué contiene cada carpeta y cuándo usar cada recurso.

---

## Estructura principal

| Ruta | Propósito |
|---|---|
| `prompts/` | Prompts reutilizables para IA |
| `skills/` | Instrucciones estructuradas por tipo de tarea |
| `templates/` | Plantillas base para documentación y código |
| `playbooks/` | Checklists y guías operativas |
| `scripts/` | Scripts base reutilizables |
| `snippets/` | Snippets para VS Code |
| `examples/` | Ejemplos de input, output y documentación |
| `.opencode/commands/` | Comandos para OpenCode |
| `docs/` | Documentación maestra, workflows y estándares |

---

## Cuándo usar cada carpeta

### `prompts/`
Úsala cuando necesites pedirle algo bien a una IA y quieras una instrucción reusable.

### `skills/`
Úsala cuando quieras una guía más estructurada sobre cómo abordar una tarea.

### `templates/`
Úsala cuando necesites un molde base ya listo para personalizar.

### `playbooks/`
Úsala como checklist operativo antes de entregar, documentar o iniciar tareas.

### `scripts/`
Úsala como base técnica para automatización, ETL, carga y calidad de datos.

### `examples/`
Úsala como referencia concreta para ver cómo debería verse un resultado final.

---

## Flujos recomendados

### Para una PR
1. revisar `skills/pr/`
2. usar `templates/pr/`
3. apoyarte en `prompts/github/`
4. revisar `playbooks/pr-checklist.md`

### Para una Jira
1. revisar `skills/jira/`
2. usar `templates/jira/`
3. apoyarte en `prompts/jira/`
4. revisar `playbooks/jira-checklist.md`

### Para análisis profundo
1. revisar `skills/analysis/`
2. usar `templates/analysis/`
3. apoyarte en `prompts/analysis/`

### Para datos / ETL
1. revisar `skills/data/`
2. usar `templates/data/`
3. reutilizar `scripts/`
4. revisar `examples/`

### Para arquitectura
1. revisar `skills/architecture/`
2. usar `templates/architecture/`
3. usar diagramas en `templates/architecture/diagrams/`
4. apoyarte en `prompts/architecture/`

---

## Recomendación general
No usar todo a la vez.
Elegir solo los artefactos necesarios según el tipo de tarea.

---

## Documentación adicional

| Documento | Propósito |
|---|---|
| `docs/guia-de-uso.md` | Guía paso a paso de todas las herramientas del kit: prompts, skills, templates, playbooks y agentes |
| `docs/agent-strategy.md` | Descripción detallada de cada agente OpenCode: inputs, outputs, permisos y diferencias |
| `docs/workflows/opencode-workflow.md` | Workflows de OpenCode por tipo de tarea |
| `docs/workflows/solution-planning-workflow.md` | Cómo usar `solution-planner` para tickets, features y proyectos |
