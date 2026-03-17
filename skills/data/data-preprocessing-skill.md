# Data Preprocessing Skill

## Objetivo
Definir y documentar el proceso de preprocesamiento de datos antes de una transformación o carga, asegurando calidad, consistencia, validación y trazabilidad.

## Cuándo usar esta skill
Usa esta skill cuando necesites:
- limpiar datasets antes de transformarlos
- validar columnas obligatorias
- normalizar formatos
- tipar datos
- eliminar duplicados
- detectar nulos o inconsistencias
- preparar datos para ETL, reportes o análisis

## Inputs recomendados
- archivo fuente o estructura de datos
- esquema esperado
- columnas obligatorias
- reglas de negocio
- tipos esperados
- destino final del dato

## Actividades principales
1. Inspección del esquema de entrada.
2. Validación de columnas obligatorias.
3. Normalización de nombres de columnas.
4. Conversión y tipado de campos.
5. Limpieza de nulos o valores inválidos.
6. Eliminación de duplicados si aplica.
7. Estandarización de formatos.
8. Generación de reporte de calidad.

## Estructura esperada de salida
1. Resumen del dataset
2. Validaciones aplicadas
3. Reglas de limpieza
4. Reglas de normalización
5. Reglas de tipado
6. Riesgos detectados
7. Dataset o esquema resultante
8. Ejemplos de input/output
9. Recomendaciones

## Reglas de calidad
- No eliminar datos sin justificarlo.
- Documentar reglas de limpieza y normalización.
- Explicar impacto de cada validación.
- Mantener trazabilidad del dato original vs dato procesado.
- Reportar errores de forma entendible.

## Prompt base reutilizable
Actúa como una especialista en calidad y preprocesamiento de datos.

Analiza el dataset o esquema proporcionado y define:
- validaciones necesarias
- columnas obligatorias
- riesgos de nulos, duplicados o formatos inválidos
- reglas de limpieza y normalización
- tipado esperado
- output esperado tras el preprocesamiento

Entrega el resultado en Markdown con tablas, reglas y ejemplos.

## Anti-patrones
- transformar sin validar
- no documentar reglas aplicadas
- asumir tipos de datos sin evidencia
- mezclar preprocesamiento con carga final sin separar responsabilidades
