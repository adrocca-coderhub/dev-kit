from __future__ import annotations

import argparse
import sys
import unicodedata

import pandas as pd

from scripts.utils.file_utils import read_csv_file, write_csv_file
from scripts.utils.logger import get_logger


logger = get_logger("preprocess_base")


REQUIRED_COLUMNS = ["customer_id", "status", "email"]


# ─── Column name normalization ────────────────────────────────────────────────


def _remove_accents(text: str) -> str:
    """Remove diacritical marks from a string (e.g. 'ñ' → 'n', 'é' → 'e')."""
    return "".join(
        c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
    )


def normalize_column_name(column: str) -> str:
    """Normalize a single column name.

    Steps:
    1. Strip leading/trailing whitespace
    2. Remove accents / diacritical marks
    3. Uppercase
    4. Replace spaces and hyphens with underscores
    5. Remove characters that are not alphanumeric or underscore
    6. Collapse consecutive underscores
    7. Strip leading/trailing underscores
    """
    name = column.strip()
    name = _remove_accents(name)
    name = name.upper()
    name = name.replace(" ", "_").replace("-", "_")
    name = "".join(c if c.isalnum() or c == "_" else "_" for c in name)
    while "__" in name:
        name = name.replace("__", "_")
    name = name.strip("_")
    return name


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Apply normalize_column_name to every column of the DataFrame."""
    df = df.copy()
    df.columns = [normalize_column_name(col) for col in df.columns]
    return df


# ─── Value-level cleaning ─────────────────────────────────────────────────────


def remove_accents_from_values(df: pd.DataFrame) -> pd.DataFrame:
    """Remove accents from all string values across object-dtype columns.

    Empty strings and whitespace-only values are converted to None.
    """
    df = df.copy()
    for col in df.select_dtypes(include="object").columns:

        def _clean(val: object) -> object:
            if not isinstance(val, str):
                return val
            cleaned = _remove_accents(val.strip())
            return None if cleaned == "" else cleaned

        df[col] = df[col].map(_clean)
    return df


def clean_string_values(df: pd.DataFrame) -> pd.DataFrame:
    """Strip leading/trailing whitespace from all string values."""
    df = df.copy()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()
    return df


# ─── Schema validation ────────────────────────────────────────────────────────


def validate_required_columns(df: pd.DataFrame) -> None:
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")


# ─── Specific transformations ─────────────────────────────────────────────────


def normalize_status(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "STATUS" in df.columns:
        df["STATUS"] = df["STATUS"].str.lower()
    elif "status" in df.columns:
        df["status"] = df["status"].str.lower()
    return df


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.copy().drop_duplicates()


# ─── Main pipeline ────────────────────────────────────────────────────────────


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting preprocessing stage")
    df = normalize_columns(df)
    validate_required_columns(df)
    df = clean_string_values(df)
    df = remove_accents_from_values(df)
    df = normalize_status(df)
    df = drop_duplicates(df)
    logger.info(
        "Preprocessing stage completed — rows=%d, cols=%d", len(df), len(df.columns)
    )
    return df


# ─── CLI ──────────────────────────────────────────────────────────────────────


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
