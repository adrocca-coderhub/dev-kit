from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from time import perf_counter

import pandas as pd

from scripts.utils.file_utils import read_csv_file, write_csv_file
from scripts.utils.logger import get_logger


logger = get_logger("etl_base")


REQUIRED_COLUMNS = ["customer_id", "status", "amount"]


@dataclass
class ETLSummary:
    status: str
    records_read: int
    records_processed: int
    records_loaded: int
    duration_seconds: float
    output_path: str


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df


def validate_input_schema(df: pd.DataFrame) -> None:
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_columns(df)

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    df = df.drop_duplicates()
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "status" in df.columns:
        df["status"] = df["status"].str.lower()

    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

    df["amount_category"] = df["amount"].apply(
        lambda value: "high" if value >= 1000 else "standard"
    )

    return df


def validate_output(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Transformed dataset is empty")


def load_data(df: pd.DataFrame, output_path: str) -> None:
    write_csv_file(df, output_path)


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


def run_etl(input_path: str, output_path: str) -> ETLSummary:
    start = perf_counter()

    logger.info("Reading source data from %s", input_path)
    raw_df = read_csv_file(input_path)
    records_read = len(raw_df)

    logger.info("Validating input schema")
    normalized_df = normalize_columns(raw_df)
    validate_input_schema(normalized_df)

    logger.info("Preprocessing data")
    preprocessed_df = preprocess_data(raw_df)

    logger.info("Transforming data")
    transformed_df = transform_data(preprocessed_df)

    logger.info("Validating transformed output")
    validate_output(transformed_df)

    logger.info("Loading output data to %s", output_path)
    load_data(transformed_df, output_path)

    duration = perf_counter() - start

    return build_summary(
        status="success",
        records_read=records_read,
        records_processed=len(transformed_df),
        records_loaded=len(transformed_df),
        duration_seconds=duration,
        output_path=output_path,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Base ETL script")
    parser.add_argument("--input", required=True, help="Input CSV file path")
    parser.add_argument("--output", required=True, help="Output CSV file path")
    return parser.parse_args()


def main() -> int:
    try:
        args = parse_args()
        summary = run_etl(args.input, args.output)
        logger.info("ETL completed successfully")
        logger.info("%s", json.dumps(summary.__dict__, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        logger.exception("ETL failed: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
