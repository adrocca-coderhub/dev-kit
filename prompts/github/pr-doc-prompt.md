# PR Documentation Prompt

Actúa como una especialista en documentación técnica para pull requests de GitHub.

Necesito que redactes una documentación de PR exhaustiva, clara, profesional y orientada a reviewers técnicos y funcionales.

## Reglas obligatorias
- No incluyas tarjeta Jira asociada.
- No incluyas una sección de pruebas.
- Sí incluye una tabla de archivos modificados.
- Para cada archivo, indica:
  - ruta del archivo
  - si fue creado, modificado, eliminado o renombrado
  - qué se hizo específicamente en ese archivo
- Describe a fondo cada funcionalidad implementada o cada cambio realizado.
- Si el cambio incluye un script nuevo, proceso batch, ETL, integración o flujo relevante, incluye un diagrama Mermaid.
- Incluye qué tablas, documentos, endpoints, datasets o recursos usa.
- Incluye input, output, formato, ejemplos de éxito y de fallo.
- Incluye reglas de negocio, consideraciones, riesgos y pendientes si aplica.
- La redacción debe enfocarse más en comportamiento, impacto y entendimiento del cambio que en pegar código.

## Estructura obligatoria de salida
1. Resumen ejecutivo
2. Objetivo
3. Alcance
4. Tabla de archivos modificados
5. Descripción detallada de cambios por funcionalidad
6. Flujo funcional / técnico
7. Diagrama Mermaid si aplica
8. Datos, tablas o documentación utilizadas
9. Contrato funcional: input / output
10. Casos representativos de éxito y fallo
11. Reglas de negocio
12. Riesgos / consideraciones
13. Pendientes
14. Evidencia adicional / referencias

## Contexto del cambio
[Pega aquí el contexto, diff, lista de archivos o explicación]

## Archivos modificados
[Pega aquí la lista de archivos]

## Detalles funcionales o técnicos
[Pega aquí notas, diff, decisiones o descripción]

Redacta la PR en Markdown profesional, lista para pegar en GitHub.
