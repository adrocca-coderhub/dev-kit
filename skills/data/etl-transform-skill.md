# ETL Transform Skill

## Objetivo
Diseñar o documentar la etapa de transformación dentro de un flujo ETL, definiendo entradas, reglas, mapeos, lógica de negocio, salidas y control de errores.

## Cuándo usar esta skill
Usa esta skill cuando necesites:
- diseñar una transformación de datos
- documentar reglas de negocio aplicadas a un ETL
- mapear columnas origen-destino
- generar un script base de transformación
- describir outputs esperados y errores controlados

## Inputs recomendados
- fuente de datos
- esquema origen
- esquema destino
- reglas de negocio
- columnas calculadas
- validaciones requeridas
- formato de salida esperado

## Actividades principales
1. Analizar datos de entrada.
2. Definir mapeo origen-destino.
3. Aplicar reglas de transformación.
4. Derivar campos calculados.
5. Validar consistencia del resultado.
6. Generar resumen del proceso.
7. Preparar salida para carga.

## Estructura esperada de salida
1. Objetivo de la transformación
2. Fuente de datos
3. Esquema origen
4. Esquema destino
5. Mapeo de columnas
6. Reglas de negocio
7. Transformaciones aplicadas
8. Output esperado
9. Casos de error
10. Riesgos y observaciones

## Reglas de calidad
- Explicar claramente cada transformación.
- Separar reglas de limpieza de reglas de negocio.
- Especificar campos calculados.
- Documentar supuestos.
- Incluir ejemplos de input y output.

## Prompt base reutilizable
Actúa como una ingeniera de datos senior.

Necesito diseñar o documentar la capa de transformación de un ETL.
Debes describir:
- datos de entrada
- mapeo origen-destino
- reglas de transformación
- lógica de negocio
- columnas calculadas
- validaciones
- output esperado
- errores o edge cases

Entrega la respuesta en Markdown estructurado y claro.

## Anti-patrones
- describir solo código sin explicar la lógica
- no documentar columnas calculadas
- no aclarar el output esperado
- mezclar reglas de carga con transformación
