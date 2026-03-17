from __future__ import annotations

import argparse
import sys

import pandas as pd

from scripts.utils.file_utils import read_csv_file, write_csv_file
from scripts.utils.logger import get_logger


logger = get_logger("preprocess_base")


REQUIRED_COLUMNS = ["customer_id", "status", "email"]


def normalize_column_name(column: str) -> str:
    return column.strip().lower().replace(" ", "_")


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [normalize_column_name(col) for col in df.columns]
    return df


def validate_required_columns(df: pd.DataFrame) -> None:
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")


def clean_string_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    return df


def normalize_status(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "status" in df.columns:
        df["status"] = df["status"].str.lower()
    return df


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    return df.drop_duplicates()


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting preprocessing stage")
    df = normalize_columns(df)
    validate_required_columns(df)
    df = clean_string_values(df)
    df = normalize_status(df)
    df = drop_duplicates(df)
    logger.info("Preprocessing stage completed")
    return df


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Base preprocessing script")
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--output", required=True, help="Output CSV path")
    return parser.parse_args()


def main() -> int:
    try:
        args = parse_args()
        logger.info("Reading input file: %s", args.input)
        df = read_csv_file(args.input)
        processed_df = preprocess_data(df)
        logger.info("Writing processed file: %s", args.output)
        write_csv_file(processed_df, args.output)
        logger.info("Preprocessing finished successfully")
        return 0
    except Exception as exc:
        logger.exception("Preprocessing failed: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
