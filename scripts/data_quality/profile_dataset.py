from __future__ import annotations

import argparse
import json
import sys

import pandas as pd

from scripts.utils.file_utils import read_csv_file
from scripts.utils.logger import get_logger


logger = get_logger("profile_dataset")


def build_profile(df: pd.DataFrame) -> dict:
    profile = {
        "rows": int(len(df)),
        "columns": list(df.columns),
        "dtypes": {column: str(dtype) for column, dtype in df.dtypes.items()},
        "null_counts": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
    }
    return profile


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dataset profiling script")
    parser.add_argument("--input", required=True, help="Input CSV path")
    return parser.parse_args()


def main() -> int:
    try:
        args = parse_args()
        logger.info("Reading dataset: %s", args.input)
        df = read_csv_file(args.input)
        profile = build_profile(df)
        logger.info("Dataset profile generated successfully")
        print(json.dumps(profile, indent=2, ensure_ascii=False))
        return 0
    except Exception as exc:
        logger.exception("Profiling failed: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
