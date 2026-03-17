from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from dataclasses import dataclass
from time import perf_counter
from typing import Any, Optional, cast

import pandas as pd

from scripts.utils.file_utils import (
    read_csv_file,
    write_csv_file,
    write_parquet_file,
)
from scripts.utils.logger import get_logger


logger = get_logger("etl_base")


REQUIRED_COLUMNS = ["customer_id", "status", "amount"]

# Sentinel date values that represent "no date" in legacy systems.
# Values matching these will be replaced with pd.NaT.
DATE_SENTINELS_YYYYMMDD = {19000101, 18000101}
DATE_SENTINELS_YYYYMM = {190001, 180001}


# ─── Summary dataclass ────────────────────────────────────────────────────────


@dataclass
class ETLSummary:
    status: str
    records_read: int
    records_processed: int
    records_loaded: int
    duration_seconds: float
    output_path: str


# ─── Column name normalization ────────────────────────────────────────────────


def _remove_accents(text: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
    )


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names: strip, remove accents, uppercase, snake_case."""

    def _normalize(col: str) -> str:
        name = col.strip()
        name = _remove_accents(name)
        name = name.upper()
        name = name.replace(" ", "_").replace("-", "_")
        name = "".join(c if c.isalnum() or c == "_" else "_" for c in name)
        while "__" in name:
            name = name.replace("__", "_")
        return name.strip("_")

    df = df.copy()
    df.columns = [_normalize(c) for c in df.columns]
    return df


# ─── Schema validation ────────────────────────────────────────────────────────


def validate_input_schema(
    df: pd.DataFrame,
    required_columns: Optional[list[str]] = None,
) -> None:
    cols = required_columns if required_columns is not None else REQUIRED_COLUMNS
    missing = [col for col in cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


# ─── Date handling ────────────────────────────────────────────────────────────


def handle_date_columns(
    df: pd.DataFrame,
    date_columns: Optional[dict[str, str]] = None,
) -> pd.DataFrame:
    """Parse and clean date columns.

    Parameters
    ----------
    df:
        Input DataFrame.
    date_columns:
        Mapping of column_name → format string.
        Supported format strings: "YYYYMMDD", "YYYYMM", or any strftime pattern
        understood by pd.to_datetime (e.g. "%Y-%m-%d").

        Sentinel values (19000101, 18000101 for YYYYMMDD; 190001, 180001 for
        YYYYMM) are replaced with NaT before parsing.

    Example config:
        date_columns:
          order_date: YYYYMMDD
          billing_month: YYYYMM
          created_at: "%Y-%m-%d"
    """
    if not date_columns:
        return df

    df = df.copy()
    for col, fmt in date_columns.items():
        if col not in df.columns:
            logger.warning("Date column '%s' not found in DataFrame — skipping", col)
            continue

        series = df[col]

        if fmt == "YYYYMMDD":
            numeric: pd.Series = cast(pd.Series, pd.to_numeric(series, errors="coerce"))  # type: ignore[type-arg]
            clean: pd.Series = cast(
                pd.Series,
                numeric.where(~numeric.isin(DATE_SENTINELS_YYYYMMDD), other=pd.NaT),
            )  # type: ignore[type-arg]
            df[col] = pd.to_datetime(
                cast(pd.Series, clean.where(clean.notna(), other=pd.NaT))
                .astype("Int64")
                .astype(str),  # type: ignore[type-arg]
                format="%Y%m%d",
                errors="coerce",
            )
        elif fmt == "YYYYMM":
            numeric2: pd.Series = cast(
                pd.Series, pd.to_numeric(series, errors="coerce")
            )  # type: ignore[type-arg]
            clean2: pd.Series = cast(
                pd.Series,
                numeric2.where(~numeric2.isin(DATE_SENTINELS_YYYYMM), other=pd.NaT),
            )  # type: ignore[type-arg]
            df[col] = pd.to_datetime(
                cast(pd.Series, clean2.where(clean2.notna(), other=pd.NaT))
                .astype("Int64")
                .astype(str),  # type: ignore[type-arg]
                format="%Y%m",
                errors="coerce",
            )
        else:
            df[col] = pd.to_datetime(series, format=fmt, errors="coerce")

        nat_count: int = df[col].isna().sum()  # type: ignore[assignment]
        logger.info("Date column '%s': parsed (format=%s, NaT=%d)", col, fmt, nat_count)

    return df


# ─── Preprocessing ────────────────────────────────────────────────────────────


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_column_names(df)

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    df = df.drop_duplicates()
    return df


# ─── Transformation ───────────────────────────────────────────────────────────


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "STATUS" in df.columns:
        df["STATUS"] = df["STATUS"].str.lower()
    elif "status" in df.columns:
        df["status"] = df["status"].str.lower()

    amount_col = (
        "AMOUNT"
        if "AMOUNT" in df.columns
        else "amount"
        if "amount" in df.columns
        else None
    )
    if amount_col:
        numeric: pd.Series = pd.to_numeric(df[amount_col], errors="coerce")  # type: ignore[type-arg]
        df[amount_col] = numeric.fillna(0)
        df["amount_category"] = df[amount_col].apply(
            lambda v: "high" if v >= 1000 else "standard"
        )

    return df


# ─── Output validation ────────────────────────────────────────────────────────


def validate_output(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Transformed dataset is empty")


# ─── Load ─────────────────────────────────────────────────────────────────────


def load_data(
    df: pd.DataFrame,
    output_path: str,
    fmt: str = "csv",
    compression: str = "snappy",
    engine: Any = None,
    table: Optional[str] = None,
    schema: Optional[str] = None,
    if_exists: str = "append",
) -> None:
    if fmt == "csv":
        write_csv_file(df, output_path)
    elif fmt == "parquet":
        write_parquet_file(df, output_path)  # type: ignore[arg-type]
    elif fmt == "postgresql":
        if engine is None or table is None:
            raise ValueError("fmt='postgresql' requires 'engine' and 'table' in config")
        df.to_sql(
            name=table,
            con=engine,
            schema=schema,
            if_exists=if_exists,  # type: ignore[arg-type]
            index=False,
            method="multi",
            chunksize=1000,
        )
    else:
        raise ValueError(f"Unsupported output format: '{fmt}'")


# ─── Summary builder ──────────────────────────────────────────────────────────


def build_summary(
    status: str,
    records_read: int,
    records_processed: int,
    records_loaded: int,
    duration_seconds: float,
    output_path: str,
) -> ETLSummary:
    return ETLSummary(
        status=status,
        records_read=records_read,
        records_processed=records_processed,
        records_loaded=records_loaded,
        duration_seconds=round(duration_seconds, 4),
        output_path=output_path,
    )


# ─── Main ETL orchestrator ───────────────────────────────────────────────────


def run_etl(
    input_path: str,
    output_path: str,
    config: Optional[dict[str, Any]] = None,
) -> ETLSummary:
    start = perf_counter()
    cfg = config or {}

    # --- Read ---
    logger.info("Reading source data from %s", input_path)
    raw_df = read_csv_file(input_path)
    records_read = len(raw_df)

    # --- Normalize & validate schema ---
    logger.info("Normalizing column names")
    normalized_df = normalize_column_names(raw_df)

    required_cols: Optional[list[str]] = cfg.get("schema", {}).get("required_columns")
    logger.info("Validating input schema")
    validate_input_schema(normalized_df, required_columns=required_cols)

    # --- Preprocess ---
    logger.info("Preprocessing data")
    preprocessed_df = preprocess_data(raw_df)

    # --- Date handling ---
    date_columns: Optional[dict[str, str]] = cfg.get("date_columns")
    if date_columns:
        logger.info("Handling date columns: %s", list(date_columns.keys()))
        preprocessed_df = handle_date_columns(preprocessed_df, date_columns)

    # --- Transform ---
    logger.info("Transforming data")
    transformed_df = transform_data(preprocessed_df)

    # --- Output validation ---
    logger.info("Validating transformed output")
    validate_output(transformed_df)

    # --- Load ---
    output_cfg: dict[str, Any] = cfg.get("output", {})
    fmt: str = output_cfg.get("format", "csv")
    effective_output = output_cfg.get("path", output_path)

    engine: Any = None
    table: Optional[str] = None
    db_schema: Optional[str] = None
    if_exists: str = "append"

    if fmt == "postgresql":
        from scripts.utils.config_utils import get_db_engine  # noqa: PLC0415

        engine = get_db_engine(cfg)
        table = output_cfg.get("table", "etl_output")
        db_schema = output_cfg.get("schema")
        if_exists = output_cfg.get("if_exists", "append")

    logger.info(
        "Loading output data — format=%s, destination=%s", fmt, effective_output
    )
    load_data(
        transformed_df,
        effective_output,
        fmt=fmt,
        engine=engine,
        table=table,
        schema=db_schema,
        if_exists=if_exists,
    )

    duration = perf_counter() - start

    return build_summary(
        status="success",
        records_read=records_read,
        records_processed=len(transformed_df),
        records_loaded=len(transformed_df),
        duration_seconds=duration,
        output_path=effective_output,
    )


# ─── CLI ──────────────────────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Base ETL script")
    parser.add_argument("--input", required=True, help="Input CSV file path")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument(
        "--config",
        default=None,
        help="Optional YAML config file path",
    )
    return parser.parse_args()


def main() -> int:
    try:
        args = parse_args()

        config: Optional[dict[str, Any]] = None
        if args.config:
            from scripts.utils.config_utils import load_config  # noqa: PLC0415

            config = load_config(args.config)

        summary = run_etl(args.input, args.output, config=config)
        logger.info("ETL completed successfully")
        logger.info("%s", json.dumps(summary.__dict__, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        logger.exception("ETL failed: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
