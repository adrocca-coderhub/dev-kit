# Onboarding Playbook

## Objetivo
Tener una guía rápida para entender un proyecto nuevo sin perder tiempo y sin depender completamente de otra persona.

---

## Paso 1: entender el objetivo del proyecto
Antes de tocar código, responder:
- ¿Qué hace el sistema?
- ¿Qué problema de negocio resuelve?
- ¿Quién lo usa?
- ¿Cuál es el flujo principal?
- ¿Qué parte me toca tocar?

### Acciones
- leer `README.md`
- leer documentación funcional si existe
- revisar nombre del repo y módulos principales
- preguntar si hay ticket, épica o contexto previo

---

## Paso 2: identificar stack y estructura
Responder:
- ¿Es frontend, backend, fullstack, data o mixto?
- ¿Qué lenguaje(s) usa?
- ¿Cómo está organizado el repo?
- ¿Dónde vive la lógica importante?

### Checklist
- [ ] identificar framework principal
- [ ] identificar carpeta `src/`
- [ ] identificar configuración (`package.json`, `pyproject.toml`, `requirements.txt`, etc.)
- [ ] identificar variables de entorno
- [ ] identificar scripts de ejecución
- [ ] identificar tests si existen

---

## Paso 3: preparar ejecución local
### Revisar
- dependencias necesarias
- archivo `.env`
- puertos
- servicios externos
- docker o no docker
- comandos para levantar proyecto

### Checklist
- [ ] instalar dependencias
- [ ] configurar `.env`
- [ ] ejecutar proyecto localmente
- [ ] validar que carga sin errores
- [ ] identificar comandos importantes

---

## Paso 4: ubicar la funcionalidad a tocar
### Preguntas clave
- ¿Qué módulo implementa esta funcionalidad?
- ¿Dónde entra el input?
- ¿Dónde se transforma?
- ¿Dónde sale el output?
- ¿Qué archivos se ven afectados?

### Acciones
- buscar por nombre de endpoint, componente, servicio, tabla o variable
- seguir el flujo de entrada a salida
- identificar archivos relacionados directos e indirectos

---

## Paso 5: entender el flujo actual
### Debes mapear
- entrada
- validaciones
- procesamiento
- salida
- errores
- dependencias

### Formato recomendado
| Elemento | Descripción |
|---|---|
| Entrada | |
| Validación | |
| Transformación | |
| Persistencia / salida | |
| Errores controlados | |

---

## Paso 6: revisar impacto del cambio
Antes de modificar algo:
- ¿Qué depende de esto?
- ¿Qué podría romperse?
- ¿Qué contratos toca?
- ¿Afecta tablas, endpoints, payloads o archivos?

### Checklist
- [ ] identificar dependencias
- [ ] identificar riesgo de regresión
- [ ] identificar impactos funcionales
- [ ] identificar documentación que debe actualizarse

---

## Paso 7: documentar antes o durante
Si el cambio es relevante, preparar:
- notas técnicas
- resumen funcional
- flujo mermaid si aplica
- lista de archivos impactados
- inputs / outputs

---

## Paso 8: cerrar entendimiento
Antes de empezar a implementar, deberías poder explicar:
- qué hace el proyecto
- qué hace el módulo que vas a tocar
- qué entra
- qué sale
- qué puede romperse
- cómo sabrás que quedó bien

---

## Entregables mínimos de onboarding
- resumen del proyecto
- módulos importantes
- flujo principal
- archivos del cambio
- preguntas abiertas
- riesgos detectados

---

## Preguntas abiertas típicas
- ¿Qué parte de esto es legado?
- ¿Qué reglas de negocio no están documentadas?
- ¿Qué dependencia externa es crítica?
- ¿Hay procesos batch o jobs involucrados?
- ¿El cambio requiere documentación adicional?
