# ADR Skill

## Objetivo
Documentar decisiones arquitectónicas relevantes de forma explícita, trazable y mantenible.

## Qué es un ADR
Un ADR captura una decisión arquitectónica significativa junto con su racional, trade-offs y consecuencias. Las fuentes de ADR/MADR destacan precisamente la utilidad de registrar el contexto, las opciones y el resultado de la decisión. ([adr.github.io](https://adr.github.io/?utm_source=openai))

## Cuándo usar esta skill
Usa esta skill cuando necesites documentar:
- elección de framework o tecnología
- patrón arquitectónico
- estrategia de integración
- modelo de comunicación entre servicios
- estrategia de persistencia
- mecanismo de autenticación
- decisiones de despliegue o infraestructura

## Inputs recomendados
- problema o decisión a tomar
- restricciones
- opciones consideradas
- criterios de evaluación
- decisión final
- riesgos o impactos conocidos

## Estructura esperada de salida
1. Título
2. Estado
3. Contexto y problema
4. Drivers
5. Opciones consideradas
6. Decisión
7. Justificación
8. Consecuencias
9. Trade-offs
10. Riesgos
11. Supuestos
12. Referencias

## Reglas de calidad
- Registrar una decisión por ADR.
- Explicar por qué se eligió una opción.
- Incluir alternativas descartadas.
- Registrar consecuencias positivas y negativas.
- Mantener el ADR corto pero suficiente.

## Prompt base reutilizable
Actúa como una arquitecta de software senior.

Necesito redactar un ADR para una decisión arquitectónica.
Incluye contexto, opciones, decisión, justificación, consecuencias, trade-offs y riesgos.
Entrega el resultado en Markdown profesional.

## Anti-patrones
- escribir ADRs vagos sin decisión explícita
- omitir opciones consideradas
- no registrar consecuencias
- mezclar varias decisiones distintas en un mismo ADR
