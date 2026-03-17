# Architecture Documentation Skill

## Objetivo
Documentar la arquitectura de un sistema, servicio o microservicio de forma estructurada, útil y mantenible, para facilitar entendimiento, onboarding, evolución y toma de decisiones.

## Referencias conceptuales
Esta skill se apoya en:
- C4 Model: vistas jerárquicas como system context, container, component y deployment. El modelo oficial presenta estas vistas como una forma simple y amigable para desarrolladores de visualizar arquitectura. ([c4model.com](https://c4model.com/?utm_source=openai))
- arc42: estructura de documentación con secciones como contexto, building blocks, runtime, deployment, decisiones transversales, riesgos y glosario. ([c4model.com](https://c4model.com/diagrams/system-context?utm_source=openai))
- ADR/MADR: documentación de decisiones arquitectónicamente significativas, incluyendo racional y consecuencias. ([adr.github.io](https://adr.github.io/?utm_source=openai))

## Cuándo usar esta skill
Usa esta skill cuando necesites:
- documentar la arquitectura actual de un sistema
- documentar la arquitectura propuesta de una solución
- describir un microservicio o servicio nuevo
- dejar documentación útil para onboarding y mantenimiento
- explicar componentes, integraciones y despliegue
- registrar decisiones arquitectónicas

## Inputs recomendados
- descripción del sistema
- objetivos y alcance
- repositorios o módulos
- dependencias e integraciones
- diagramas previos si existen
- restricciones técnicas o de negocio
- requerimientos no funcionales
- decisiones ya tomadas

## Vistas recomendadas
1. **Contexto**: personas, sistemas externos y sistema en foco.
2. **Contenedores**: aplicaciones, servicios, bases de datos, colas, buckets, etc.
3. **Componentes**: piezas internas importantes dentro de un contenedor.
4. **Runtime / dinámico**: flujo principal de una operación relevante.
5. **Deployment**: cómo se despliega por ambiente si es importante.

## Estructura esperada de salida
1. Resumen ejecutivo
2. Objetivo y alcance
3. Contexto
4. Drivers arquitectónicos
5. Restricciones y supuestos
6. Vista de contexto
7. Vista de contenedores
8. Vista de componentes
9. Vista dinámica / runtime
10. Vista de despliegue
11. Datos e integraciones
12. Decisiones arquitectónicas
13. Riesgos y trade-offs
14. Observabilidad, seguridad y escalabilidad
15. Glosario
16. Referencias

## Reglas de calidad
- Enfocarse en responsabilidades y relaciones.
- Documentar límites del sistema.
- Evitar diagramas excesivamente detallados si no aportan.
- Diferenciar estado actual vs futuro cuando aplique.
- Indicar claramente supuestos y vacíos de información.

## Prompt base reutilizable
Actúa como una arquitecta de software senior.

Necesito documentar la arquitectura de un sistema o microservicio.
Debes incluir propósito, alcance, contexto, contenedores, componentes, flujos, despliegue, integraciones, decisiones, riesgos y consideraciones operativas.

Entrega el resultado en Markdown estructurado, con diagramas Mermaid claros y secciones útiles para desarrollo y soporte.

## Anti-patrones
- documentar solo tecnologías sin responsabilidades
- dibujar diagramas sin explicar relaciones
- mezclar arquitectura actual y propuesta sin aclararlo
- omitir restricciones, trade-offs o supuestos
