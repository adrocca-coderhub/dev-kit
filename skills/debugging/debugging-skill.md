# Debugging Skill

## Objetivo
Diagnosticar problemas técnicos de forma estructurada, reduciendo ensayo-error y enfocando el análisis en evidencia, hipótesis y validación.

## Cuándo usar esta skill
Usa esta skill cuando necesites:
- investigar errores en ejecución
- entender por qué una funcionalidad no se comporta como se espera
- analizar stack traces o logs
- identificar causa raíz probable
- proponer una corrección con menor riesgo

## Inputs recomendados
- mensaje de error
- logs
- stack trace
- comportamiento esperado
- comportamiento observado
- archivos o módulos involucrados
- contexto de negocio o técnico

## Proceso recomendado
1. Definir el problema exacto.
2. Comparar comportamiento esperado vs actual.
3. Reunir evidencia concreta.
4. Formular hipótesis de causa raíz.
5. Priorizar hipótesis por probabilidad e impacto.
6. Definir pasos para validarlas.
7. Proponer solución o mitigación.
8. Documentar riesgos y siguientes pasos.

## Estructura esperada de salida
1. Resumen del problema
2. Evidencia
3. Hipótesis
4. Validación propuesta
5. Solución sugerida
6. Riesgos
7. Próximos pasos

## Reglas de calidad
- No confundir síntoma con causa raíz.
- No saltar directo a una solución sin hipótesis.
- Separar evidencia observada de inferencias.
- Explicar por qué una hipótesis es más fuerte que otra.
- Considerar impacto de la solución propuesta.

## Prompt base reutilizable
Actúa como una ingeniera senior de debugging.

Analiza este problema técnico y ayúdame a:
- resumir el problema
- identificar síntomas
- comparar comportamiento esperado vs actual
- proponer hipótesis de causa raíz
- definir pasos de validación
- sugerir una solución con riesgos y trade-offs

Entrega el resultado en Markdown estructurado.

## Anti-patrones
- adivinar sin evidencia
- cambiar muchas cosas a la vez
- no distinguir causa raíz de efecto
- no documentar pasos para validar
