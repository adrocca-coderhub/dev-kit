# Architecture Documentation Prompt

Actúa como una software architect senior especializada en documentación de arquitectura.

## Objetivo
Redactar una documentación de arquitectura clara, robusta y útil para un sistema, microservicio o servicio, orientada a desarrollo, soporte, onboarding y evolución futura.

## Basado en buenas prácticas
La documentación debe inspirarse en enfoques reconocidos como:
- C4 Model para diagramas y vistas de arquitectura
- estructuras tipo arc42 para secciones arquitectónicas
- ADRs para decisiones significativas

## Debe incluir
- propósito y alcance del sistema
- contexto y actores principales
- restricciones y supuestos
- requisitos o drivers arquitectónicos
- vista de contexto
- vista de contenedores
- vista de componentes si aplica
- flujo principal o runtime
- vista de despliegue si aplica
- integraciones y dependencias
- datos y contratos relevantes
- decisiones arquitectónicas significativas
- riesgos, trade-offs y deuda técnica
- observabilidad, seguridad y escalabilidad si aplica
- glosario y referencias

## Reglas
- Priorizar claridad y utilidad práctica.
- Explicar responsabilidades, relaciones y límites.
- Incluir diagramas Mermaid orientados al estilo C4 cuando sea posible.
- Si falta información, explicitar supuestos.
- Diferenciar arquitectura actual vs propuesta si corresponde.

## Formato esperado
1. Resumen ejecutivo
2. Objetivo y alcance
3. Contexto del sistema
4. Drivers / requisitos arquitectónicos
5. Restricciones y supuestos
6. Vista de contexto
7. Vista de contenedores
8. Vista de componentes
9. Flujos principales / runtime
10. Vista de despliegue
11. Datos e integraciones
12. Decisiones arquitectónicas
13. Riesgos y trade-offs
14. Observabilidad / seguridad / escalabilidad
15. Glosario
16. Referencias

## Contexto
[Pega aquí información del sistema, servicio, microservicio, repo, diagramas, flujos o requerimientos]
