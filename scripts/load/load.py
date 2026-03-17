from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Optional

import pandas as pd

from scripts.utils.file_utils import (
    ParquetCompression,
    read_csv_file,
    write_csv_file,
    write_parquet_file,
)
from scripts.utils.logger import get_logger


logger = get_logger("load_base")


# ─── Validation ───────────────────────────────────────────────────────────────


def validate_non_empty(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Input dataset is empty")


def validate_columns(df: pd.DataFrame, required_columns: list[str]) -> None:
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


# ─── Load targets ─────────────────────────────────────────────────────────────


def load_to_csv(df: pd.DataFrame, output_path: str) -> dict[str, Any]:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return {
        "status": "success",
        "format": "csv",
        "destination": output_path,
        "loaded_records": len(df),
        "failed_records": 0,
    }


def load_to_parquet(
    df: pd.DataFrame,
    output_path: str,
    compression: Optional[ParquetCompression] = "snappy",
) -> dict[str, Any]:
    """Write DataFrame to a Parquet file.

    Parameters
    ----------
    df:
        DataFrame to persist.
    output_path:
        Destination file path (should end in .parquet).
    compression:
        Parquet compression codec (snappy, gzip, brotli, zstd, none).
    """
    write_parquet_file(df, output_path, compression=compression)
    return {
        "status": "success",
        "format": "parquet",
        "compression": compression,
        "destination": output_path,
        "loaded_records": len(df),
        "failed_records": 0,
    }


def load_to_postgresql(
    df: pd.DataFrame,
    table: str,
    engine: Any,
    schema: Optional[str] = None,
    if_exists: str = "append",
) -> dict[str, Any]:
    """Load a DataFrame into a PostgreSQL table using SQLAlchemy.

    Parameters
    ----------
    df:
        DataFrame to write.
    table:
        Target table name.
    engine:
        SQLAlchemy engine (from config_utils.get_db_engine).
    schema:
        Optional schema name. Defaults to the engine's default search path.
    if_exists:
        Behaviour when the table already exists: 'fail', 'replace', 'append'.
        Defaults to 'append'.
    """
    try:
        df.to_sql(
            name=table,
            con=engine,
            schema=schema,
            if_exists=if_exists,  # type: ignore[arg-type]
            index=False,
            method="multi",
            chunksize=1000,
        )
        return {
            "status": "success",
            "format": "postgresql",
            "table": f"{schema}.{table}" if schema else table,
            "if_exists": if_exists,
            "loaded_records": len(df),
            "failed_records": 0,
        }
    except Exception as exc:
        return {
            "status": "error",
            "error_code": "POSTGRESQL_LOAD_FAILED",
            "message": str(exc),
            "loaded_records": 0,
            "failed_records": len(df),
        }


# ─── Dispatcher ───────────────────────────────────────────────────────────────


def load_data(
    df: pd.DataFrame,
    output_path: str,
    fmt: str = "csv",
    compression: Optional[ParquetCompression] = "snappy",
    engine: Any = None,
    table: Optional[str] = None,
    schema: Optional[str] = None,
    if_exists: str = "append",
) -> dict[str, Any]:
    """Dispatch the DataFrame to the requested output format.

    Parameters
    ----------
    df:
        Processed DataFrame to load.
    output_path:
        Destination path (ignored for postgresql — use *table* instead).
    fmt:
        Output format: 'csv', 'parquet', or 'postgresql'.
    compression:
        Compression codec for Parquet output.
    engine:
        SQLAlchemy engine (required when fmt='postgresql').
    table:
        Target table name (required when fmt='postgresql').
    schema:
        Target schema (optional, for postgresql).
    if_exists:
        'fail', 'replace', or 'append' (postgresql only).
    """
    logger.info("Starting load stage — format=%s", fmt)
    validate_non_empty(df)

    if fmt == "csv":
        result = load_to_csv(df, output_path)
    elif fmt == "parquet":
        result = load_to_parquet(df, output_path, compression=compression)
    elif fmt == "postgresql":
        if engine is None or table is None:
            raise ValueError(
                "fmt='postgresql' requires both 'engine' and 'table' parameters"
            )
        result = load_to_postgresql(
            df, table, engine, schema=schema, if_exists=if_exists
        )
    else:
        raise ValueError(
            f"Unsupported format '{fmt}'. Valid options: csv, parquet, postgresql"
        )

    logger.info("Load stage finished — %s", json.dumps(result, ensure_ascii=False))
    return result


# ─── CLI ──────────────────────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Base load script")
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--output", required=True, help="Destination output path")
    parser.add_argument(
        "--format",
        dest="fmt",
        default="csv",
        choices=["csv", "parquet"],
        help="Output format (default: csv)",
    )
    parser.add_argument(
        "--compression",
        default="snappy",
        help="Parquet compression codec (default: snappy)",
    )
    return parser.parse_args()


def main() -> int:
    try:
        args = parse_args()
        logger.info("Reading transformed input file: %s", args.input)
        df = read_csv_file(args.input)
        result = load_data(
            df,
            args.output,
            fmt=args.fmt,
            compression=args.compression,
        )
        logger.info("Load summary: %s", json.dumps(result, ensure_ascii=False))
        return 0
    except Exception as exc:
        logger.exception("Load failed: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
