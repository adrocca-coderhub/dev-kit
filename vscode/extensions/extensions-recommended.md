# Extensiones recomendadas para VS Code

Lista mínima de extensiones para trabajar con este dev-kit: Python, documentación Markdown y calidad de código.

---

## Python

| Extensión | ID | Para qué sirve |
|---|---|---|
| Python | `ms-python.python` | Soporte base: IntelliSense, debugging, entornos virtuales |
| Pylance | `ms-python.vscode-pylance` | Type checking rápido, autocompletado avanzado con Pyright |
| Black Formatter | `ms-python.black-formatter` | Formatea automáticamente al guardar (línea 88) |
| isort | `ms-python.isort` | Ordena imports automáticamente al guardar |
| Ruff | `charliermarsh.ruff` | Linter ultrarrápido; reemplaza Flake8 + isort en muchos casos |
| Mypy Type Checker | `ms-python.mypy-type-checker` | Type checking estático con mypy integrado al editor |

---

## Calidad y formato

| Extensión | ID | Para qué sirve |
|---|---|---|
| Prettier | `esbenp.prettier-vscode` | Formatea JSON, Markdown y TypeScript automáticamente |
| EditorConfig | `EditorConfig.EditorConfig` | Aplica reglas de `.editorconfig` (indentación, newline) |
| Error Lens | `usernamehw.errorlens` | Muestra errores y warnings inline sin abrir el panel de problemas |

---

## Markdown y documentación

| Extensión | ID | Para qué sirve |
|---|---|---|
| Markdown All in One | `yzhang.markdown-all-in-one` | Preview, atajos, lista de contenidos, autocompletado en Markdown |
| Markdown Preview Mermaid | `bierner.markdown-mermaid` | Renderiza diagramas Mermaid en la preview de Markdown |
| Mermaid Chart | `MermaidChart.vscode-mermaid-chart` | Editor dedicado para diagramas Mermaid con live preview |

---

## Git y colaboración

| Extensión | ID | Para qué sirve |
|---|---|---|
| GitLens | `eamodio.gitlens` | Historial de línea, blame, comparaciones entre commits |
| GitHub Pull Requests | `GitHub.vscode-pull-request-github` | Revisar y crear PRs desde VS Code |

---

## Productividad

| Extensión | ID | Para qué sirve |
|---|---|---|
| GitHub Copilot | `GitHub.copilot` | Autocompletado con IA (requiere suscripción) |
| GitHub Copilot Chat | `GitHub.copilot-chat` | Chat con IA contextual sobre el código abierto |
| Path Intellisense | `christian-kohler.path-intellisense` | Autocompletado de rutas de archivo en imports |
| Todo Tree | `Gruntfuggly.todo-tree` | Encuentra y agrupa todos los `TODO`, `FIXME` y `HACK` del proyecto |

---

## Cómo instalar desde línea de comandos

```bash
# Instalar una extensión
code --install-extension ms-python.python

# Instalar todas las recomendadas de una vez
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-python.black-formatter
code --install-extension ms-python.isort
code --install-extension charliermarsh.ruff
code --install-extension ms-python.mypy-type-checker
code --install-extension esbenp.prettier-vscode
code --install-extension usernamehw.errorlens
code --install-extension yzhang.markdown-all-in-one
code --install-extension bierner.markdown-mermaid
code --install-extension eamodio.gitlens
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
```

---

## Cómo usar el settings.json de este kit

Copiar `vscode/settings/settings.json` a `.vscode/settings.json` en la raíz del proyecto.
Copiar `vscode/tasks/tasks.json` a `.vscode/tasks.json`.
Copiar `vscode/keybindings/keybindings.json` a los keybindings globales de VS Code (`Preferences: Open Keyboard Shortcuts (JSON)`).
