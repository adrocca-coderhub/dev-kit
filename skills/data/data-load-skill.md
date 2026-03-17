# Data Load Skill

## Objetivo
Diseñar o documentar la etapa de carga de datos hacia un destino final, contemplando validación previa, formato de salida, estrategia de escritura, errores y trazabilidad.

## Cuándo usar esta skill
Usa esta skill cuando necesites:
- cargar datos a base de datos, archivos o APIs
- documentar un proceso de carga
- definir estrategia de inserción/actualización
- describir salidas finales de un ETL
- especificar errores y controles durante persistencia

## Inputs recomendados
- dataset transformado
- destino final
- esquema destino
- estrategia de carga
- llaves primarias o criterios de upsert
- restricciones
- volumen estimado

## Actividades principales
1. Validar que el dataset transformado cumple el esquema destino.
2. Preparar salida final.
3. Definir estrategia de carga.
4. Ejecutar escritura.
5. Registrar métricas y errores.
6. Generar resumen final.

## Estructura esperada de salida
1. Objetivo de la carga
2. Destino final
3. Esquema destino
4. Estrategia de carga
5. Reglas de validación
6. Manejo de errores
7. Output generado
8. Métricas reportadas
9. Riesgos y recomendaciones

## Reglas de calidad
- No cargar datos sin validar estructura mínima.
- Documentar estrategia de inserción.
- Describir errores recuperables y no recuperables.
- Registrar cantidad de registros procesados.
- Mantener trazabilidad del resultado.

## Prompt base reutilizable
Actúa como una ingeniera de datos senior.

Necesito diseñar o documentar una etapa de carga de datos.
Describe:
- destino final
- estructura esperada
- estrategia de inserción o actualización
- validaciones antes de persistir
- errores posibles
- métricas y salida final

Entrega el resultado en Markdown con tablas y ejemplos.

## Anti-patrones
- cargar sin validaciones previas
- no definir si es insert, update, append o upsert
- no explicar errores ni métricas
- no documentar el resultado final de la carga
