# TypeScript Module Template

```typescript
/**
 * Purpose:
 * Describe what this module does.
 *
 * Responsibilities:
 * - validate input
 * - process data
 * - return structured output
 */

export interface ProcessInput {
  id: string;
  status?: string;
}

export interface ProcessOutput {
  success: boolean;
  message: string;
  data?: unknown;
}

export function validateInput(input: ProcessInput): void {
  if (!input.id) {
    throw new Error("Field 'id' is required");
  }
}

export function processInput(input: ProcessInput): ProcessOutput {
  validateInput(input);

  return {
    success: true,
    message: "Process completed successfully",
    data: {
      normalizedId: input.id.trim(),
      status: input.status ?? "unknown",
    },
  };
}
```

## Recomendaciones
- Separar validación de lógica principal.
- Definir interfaces claras.
- Mantener funciones pequeñas y reutilizables.
- Documentar inputs/outputs cuando el módulo sea crítico.
