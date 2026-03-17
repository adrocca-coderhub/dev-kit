# PR Checklist Playbook

## Objetivo
Asegurar que cada pull request quede bien explicada, ordenada y profesional, con contexto funcional y técnico suficiente para revisión.

---

## Antes de redactar la PR
### Validar contexto
- [ ] entiendo el objetivo del cambio
- [ ] entiendo qué problema resuelve
- [ ] tengo clara la funcionalidad o ajuste implementado
- [ ] tengo identificados los archivos modificados
- [ ] sé si hubo creación, modificación, eliminación o renombre de archivos
- [ ] sé qué recursos usa: tablas, endpoints, documentos, datasets, configs

---

## Archivos modificados
Para cada archivo, documentar:
- [ ] ruta completa
- [ ] tipo de cambio (`Creado`, `Modificado`, `Eliminado`, `Renombrado`)
- [ ] qué se hizo en ese archivo
- [ ] impacto funcional o técnico

### Formato esperado
| Archivo | Tipo de cambio | Descripción del cambio |
|---|---|---|
| `ruta/archivo.ts` | Modificado | |
| `scripts/proceso.py` | Creado | |

---

## Contenido mínimo de la PR
- [ ] resumen ejecutivo
- [ ] objetivo
- [ ] alcance
- [ ] tabla de archivos modificados
- [ ] descripción detallada de cambios
- [ ] flujo funcional o técnico
- [ ] diagrama Mermaid si aplica
- [ ] datos / tablas / documentación usadas
- [ ] input y output
- [ ] ejemplos de éxito y fallo
- [ ] reglas de negocio si aplica
- [ ] riesgos / consideraciones
- [ ] pendientes / siguientes pasos

---

## Reglas del template de PR de este kit
- [ ] no incluir Jira asociada
- [ ] no incluir sección de pruebas
- [ ] describir bien cada archivo
- [ ] enfocarse en comportamiento e impacto, no solo en código
- [ ] usar Mermaid cuando haya flujo nuevo o relevante
- [ ] incluir ejemplos claros de input/output

---

## Preguntas que debe responder la PR
- ¿Qué cambia?
- ¿Por qué cambia?
- ¿Qué archivos toca?
- ¿Cómo funciona ahora?
- ¿Qué entra?
- ¿Qué sale?
- ¿Qué datos usa?
- ¿Qué riesgos hay?
- ¿Qué queda pendiente?

---

## Revisión final antes de pegar la PR
- [ ] la documentación se entiende sin abrir todo el código
- [ ] las secciones están completas
- [ ] la tabla de archivos está bien hecha
- [ ] no faltan ejemplos
- [ ] no hay texto genérico vacío
- [ ] el contenido está profesional y claro
