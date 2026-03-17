# Python Script Template

```python
"""
Descripción:
Script base reutilizable.

Objetivo:
- Explicar qué hace el script.
- Definir input y output.
- Registrar ejecución y errores.

Uso:
    python script.py --input path/input.csv --output path/output.csv
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import Any


def configure_logger() -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    return logging.getLogger("base_script")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Base reusable Python script")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path")
    return parser.parse_args()


def validate_input(input_path: str) -> None:
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")


def process(input_path: str, output_path: str, logger: logging.Logger) -> dict[str, Any]:
    logger.info("Starting process")
    logger.info("Input: %s", input_path)
    logger.info("Output: %s", output_path)

    # TODO: implement processing logic

    result = {
        "status": "success",
        "input": input_path,
        "output": output_path,
    }

    logger.info("Process finished successfully")
    return result


def main() -> int:
    logger = configure_logger()

    try:
        args = parse_args()
        validate_input(args.input)
        process(args.input, args.output, logger)
        return 0
    except Exception as exc:
        logger.exception("Execution failed: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
```
