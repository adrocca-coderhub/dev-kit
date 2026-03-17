from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

from scripts.utils.file_utils import read_csv_file
from scripts.utils.logger import get_logger


logger = get_logger("load_base")


def validate_non_empty(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Input dataset is empty")


def validate_columns(df: pd.DataFrame, required_columns: list[str]) -> None:
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


def load_to_csv(df: pd.DataFrame, output_path: str) -> dict:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    return {
        "status": "success",
        "destination": output_path,
        "loaded_records": len(df),
        "failed_records": 0,
    }


def load_data(df: pd.DataFrame, output_path: str) -> dict:
    logger.info("Starting load stage")
    validate_non_empty(df)
    validate_columns(df, required_columns=list(df.columns))
    result = load_to_csv(df, output_path)
    logger.info("Load stage finished successfully")
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Base load script")
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--output", required=True, help="Destination output path")
    return parser.parse_args()


def main() -> int:
    try:
        args = parse_args()
        logger.info("Reading transformed input file: %s", args.input)
        df = read_csv_file(args.input)

        result = load_data(df, args.output)
        logger.info("Load summary: %s", json.dumps(result, ensure_ascii=False))
        return 0
    except Exception as exc:
        logger.exception("Load failed: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
