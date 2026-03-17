# Deep Analysis Skill

## Objetivo
Realizar un análisis técnico y funcional profundo de un requerimiento, repositorio, módulo, script o conjunto de cambios para entender su propósito, flujo, dependencias, riesgos, deuda técnica y oportunidades de mejora.

## Cuándo usar esta skill
Usa esta skill cuando necesites:
- entender rápidamente un proyecto o módulo desconocido
- analizar una tarea compleja antes de implementarla
- documentar el comportamiento de una funcionalidad existente
- detectar riesgos, dependencias y supuestos
- preparar contexto antes de redactar una PR o una tarjeta Jira
- hacer onboarding acelerado sobre un código base

## Inputs recomendados
- descripción del requerimiento o ticket
- archivos relevantes
- estructura del proyecto
- diff o lista de cambios
- configuración relacionada
- logs, errores o evidencias si existen
- reglas de negocio conocidas

## Proceso de análisis
1. Identificar el objetivo del módulo, script o cambio.
2. Detectar el flujo principal de ejecución.
3. Mapear archivos, dependencias y componentes involucrados.
4. Identificar inputs, outputs y efectos colaterales.
5. Inferir reglas de negocio presentes en el código.
6. Detectar riesgos técnicos, deuda o ambigüedades.
7. Identificar documentación faltante.
8. Proponer siguientes pasos claros.

## Estructura esperada de salida
1. Resumen ejecutivo
2. Objetivo o propósito
3. Arquitectura o mapa del módulo
4. Flujo funcional/técnico
5. Archivos y responsabilidades
6. Inputs / outputs
7. Dependencias e integraciones
8. Reglas de negocio inferidas
9. Riesgos y deuda técnica
10. Gaps de documentación
11. Recomendaciones
12. Próximos pasos

## Reglas de calidad
- No asumir cosas sin indicarlo.
- Diferenciar hechos observados vs inferencias.
- Explicar de forma clara y accionable.
- Priorizar comportamiento e impacto sobre detalles irrelevantes.
- Si faltan datos, listar preguntas abiertas.

## Prompt base reutilizable
Actúa como una analista técnico-funcional senior.

Necesito un análisis profundo del siguiente contexto.

Debes identificar:
- propósito del módulo o funcionalidad
- flujo principal
- archivos involucrados y sus responsabilidades
- inputs y outputs
- dependencias
- reglas de negocio inferidas
- riesgos, deuda técnica y vacíos de documentación
- recomendaciones y siguientes pasos

Entrega la salida en Markdown con una estructura clara, profesional y accionable.

## Anti-patrones
- resumir superficialmente sin entender el flujo
- enfocarse solo en nombres de archivos sin explicar responsabilidades
- no distinguir entre evidencia e hipótesis
- listar problemas sin proponer acciones
