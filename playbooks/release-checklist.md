# Release Checklist Playbook

## Objetivo
Tener una guía clara para preparar una liberación o entrega de cambios de forma ordenada, minimizando omisiones y mejorando la comunicación técnica.

---

## Validación previa del cambio
- [ ] el alcance del release está claro
- [ ] se sabe qué funcionalidades o fixes entran
- [ ] se identificaron riesgos conocidos
- [ ] se identificaron dependencias externas o internas
- [ ] se validó si hay cambios de configuración, datos o infraestructura

---

## Documentación del release
- [ ] existe resumen del release
- [ ] se documentaron funcionalidades principales
- [ ] se listaron componentes o servicios impactados
- [ ] se documentaron cambios en contratos, tablas o endpoints si aplica
- [ ] se documentaron limitaciones o consideraciones
- [ ] se documentaron pendientes si existen

---

## Impacto técnico
- [ ] se identificaron cambios en base de datos
- [ ] se identificaron cambios en variables de entorno
- [ ] se identificaron cambios en pipelines, jobs o scripts
- [ ] se identificaron cambios en despliegue o infraestructura
- [ ] se identificó si requiere migración o backfill

---

## Riesgos y mitigación
- [ ] se listaron riesgos conocidos
- [ ] existe plan de contingencia si aplica
- [ ] se sabe qué rollback conceptual sería necesario si algo falla
- [ ] se identificaron impactos sobre usuarios o sistemas consumidores

---

## Comunicación
- [ ] el release se puede resumir claramente
- [ ] el equipo sabe qué cambia
- [ ] el equipo sabe qué no cambia
- [ ] el equipo sabe qué monitorear tras la liberación

---

## Cierre
Antes de cerrar el release deberías poder responder:
- ¿qué entra?
- ¿qué impacta?
- ¿qué depende de esto?
- ¿qué riesgos existen?
- ¿qué seguimiento se necesita después?
