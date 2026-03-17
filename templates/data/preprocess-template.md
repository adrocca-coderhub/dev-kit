# Data Preprocess Template

## Resumen
Describe el objetivo del preprocesamiento y el problema de calidad o consistencia que resuelve.

## Objetivo
Explica cómo se limpian, normalizan o validan los datos antes de transformarlos o cargarlos.

---

## Fuente de datos

| Recurso | Tipo | Descripción |
|---|---|---|
|  | archivo / tabla / API |  |

---

## Esquema esperado

| Campo | Tipo esperado | Requerido | Descripción |
|---|---|---|---|
|  |  |  |  |

---

## Validaciones aplicadas
- validación de columnas obligatorias
- detección de nulos
- validación de tipos
- normalización de nombres de columnas
- control de duplicados
- validación de formato

---

## Reglas de limpieza y normalización

| Regla | Descripción | Ejemplo |
|---|---|---|
| trim | eliminar espacios sobrantes | `" Juan "` -> `"Juan"` |
| lowercase | convertir a minúsculas | `"EMAIL"` -> `"email"` |
| null handling | tratar nulos | `""` -> `null` |

---

## Ejemplo de input
```json
[
  {
    "Customer ID": "001 ",
    "Status": " ACTIVE ",
    "Email": "TEST@MAIL.COM"
  }
]
```

## Ejemplo de output preprocesado
```json
[
  {
    "customer_id": "001",
    "status": "active",
    "email": "test@mail.com"
  }
]
```

---

## Riesgos detectados

| Riesgo | Impacto | Recomendación |
|---|---|---|
|  |  |  |

---

## Resultado esperado
Describe cómo debe quedar el dataset tras el preprocesamiento.

---

## Observaciones
-
-
-
