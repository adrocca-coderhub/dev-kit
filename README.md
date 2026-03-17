# Dev Kit

Kit personal para acelerar trabajo de desarrollo, documentación técnica y automatización de tareas repetitivas con datos.

## Objetivo

Centralizar templates, prompts, skills, snippets, scripts base y playbooks reutilizables para trabajar más rápido, con mejor calidad y mayor consistencia.

---

## Estructura

| Carpeta | Propósito |
|---|---|
| `prompts/` | Prompts reutilizables para IA (Copilot, Claude, ChatGPT) |
| `skills/` | Instrucciones estructuradas por tipo de tarea |
| `templates/` | Moldes base para documentación (PRs, Jira) |
| `scripts/` | Scripts Python de datos: ETL, preprocesamiento, carga, calidad |
| `playbooks/` | Checklists operativos (delivery, onboarding, release) |
| `snippets/` | Snippets para VS Code por lenguaje |
| `examples/` | Ejemplos de input, output y documentación |
| `docs/` | Documentación maestra, ADRs, estándares y workflows |
| `vscode/` | Configuración de referencia para VS Code |
| `.opencode/commands/` | Comandos slash reutilizables para OpenCode |

---

## Scripts disponibles

| Script | Comando |
|---|---|
| ETL completo | `python scripts/etl/pipeline_etl.py --input <ruta> --output <ruta>` |
| Preprocesamiento | `python scripts/preprocess/preprocess.py --input <ruta> --output <ruta>` |
| Carga | `python scripts/load/load.py --input <ruta> --output <ruta>` |
| Profiling de dataset | `python scripts/data_quality/profile_dataset.py --input <ruta>` |
| Validación de schema | `python scripts/data_quality/validate_schema.py --input <ruta>` |

```bash
# Instalar dependencias
pip install -r requirements.txt
```

---

## Templates disponibles

| Tipo | Archivo |
|---|---|
| PR de GitHub | `templates/pr/pr-doc-template.md` |
| Ticket Jira | `templates/jira/jira-doc-template.md` |

---

## Comandos OpenCode disponibles

| Comando | Propósito |
|---|---|
| `/pr-doc` | Generar documentación de PR |
| `/jira-doc` | Generar tarjeta Jira |
| `/deep-analysis` | Análisis profundo de código o módulo |
| `/pipeline-etl` | Generar script de ETL base |
| `/data-profile` | Generar script de profiling |
| `/adr` | Crear un ADR |
| `/architecture-doc` | Documentar arquitectura |
| `/debugging` | Ayuda estructurada para debugging |
| `/onboarding` | Generar documentación de onboarding |
| `/release-notes` | Generar notas de release |

---

## Casos de uso

- Redactar documentación de PR lista para pegar en GitHub
- Redactar tarjetas Jira robustas con diagrama y criterios de aceptación
- Analizar proyectos o módulos en profundidad
- Generar scripts base de datos / ETL
- Reutilizar snippets y templates
- Estandarizar entregables del equipo

---

## Configuración VS Code

Los archivos de configuración viven en `vscode/` como referencia:

- `vscode/settings/settings.json` — format on save, rulers, snippets arriba, formateadores por lenguaje
- `vscode/keybindings/keybindings.json` — atajos para terminal, Markdown, tasks y navegación
- `vscode/tasks/tasks.json` — tasks para correr ETL, preprocess, load y data quality desde VS Code
- `vscode/extensions/extensions-recommended.md` — lista de extensiones recomendadas con descripción

Para usar: copiar `settings.json` a `.vscode/settings.json` y `tasks.json` a `.vscode/tasks.json` en el proyecto destino.

---

## Documentación interna

- `docs/kit-index.md` — mapa maestro del kit: cuándo usar cada carpeta
- `docs/decisions/` — ADRs: decisiones de arquitectura registradas
- `docs/standards/` — estándares de documentación y naming conventions
- `docs/workflows/` — flujos de trabajo por tipo de tarea (feature, bugfix, datos, arquitectura)

---

## Primeros pasos

1. Revisar `docs/kit-index.md` para entender qué hay disponible
2. Revisar `prompts/master/prompt-master.md` como base para nuevos prompts
3. Revisar `skills/` para entender los roles disponibles
4. Usar `templates/` como molde para documentar PRs y tickets
5. Configurar VS Code con los archivos de `vscode/`
6. Probar comandos slash en `.opencode/commands/`

---

## Recomendación de uso

No usar todo a la vez. Tomar solo lo necesario para cada tarea y personalizarlo.
