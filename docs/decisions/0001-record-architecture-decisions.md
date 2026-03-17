# ADR-0001: Registrar decisiones de arquitectura con ADRs

- **Estado:** Aceptado
- **Fecha:** 2026-03-17
- **Autora:** Adriana

---

## Contexto

A medida que el dev-kit crece en scripts, templates, prompts y convenciones, se vuelve necesario registrar las decisiones técnicas y estructurales que se tomaron y por qué. Sin un registro, es difícil recordar el razonamiento detrás de cada elección, especialmente cuando se evalúan alternativas en el futuro.

---

## Decisión

Usaremos **Architecture Decision Records (ADRs)** para documentar las decisiones relevantes del kit.

Cada ADR:
- vive en `docs/decisions/`
- tiene un número secuencial con prefijo `NNNN-` (ej. `0001-`, `0002-`)
- usa el formato de este documento como plantilla
- se escribe en español
- una vez aceptado, no se modifica — si la decisión cambia, se crea un nuevo ADR que lo supersede

---

## Opciones consideradas

| Opción | Descripción |
|---|---|
| No documentar decisiones | Simple, pero genera deuda de conocimiento a futuro |
| Comentarios en código | Solo aplica a decisiones de implementación, no de estructura |
| Documento centralizado de decisiones | Difícil de mantener, se vuelve un monolito |
| **ADRs individuales por decisión** | Ligero, versionable, fácil de buscar y superseder |

---

## Consecuencias

**Positivas:**
- Cualquier colaborador (o IA) puede entender por qué se tomó cada decisión
- Facilita evaluar si una decisión sigue siendo válida
- Sirve como historial de evolución del kit

**Negativas o consideraciones:**
- Requiere disciplina para crear el ADR en el momento de tomar la decisión
- Si se usan con poca frecuencia, pierden valor

---

## Formato de un ADR

```
# ADR-NNNN: Título de la decisión

- Estado: Propuesto | Aceptado | Supersedido por ADR-XXXX
- Fecha: YYYY-MM-DD
- Autora: nombre

## Contexto
Qué situación motivó esta decisión.

## Decisión
Qué se decidió.

## Opciones consideradas
Tabla o lista con las alternativas evaluadas.

## Consecuencias
Qué implica esta decisión: ventajas, desventajas, riesgos.
```
