from __future__ import annotations

import argparse
import json
import sys
from typing import Any, cast

import pandas as pd

from scripts.utils.file_utils import read_csv_file, write_json_file
from scripts.utils.logger import get_logger


logger = get_logger("profile_dataset")


# ─── Profiling logic ──────────────────────────────────────────────────────────


def _numeric_stats(series: pd.Series) -> dict[str, Any]:  # type: ignore[type-arg]
    """Return descriptive stats for a numeric column."""
    non_null = series.dropna()
    if non_null.empty:
        return {}
    return {
        "min": float(non_null.min()),  # type: ignore[arg-type]
        "max": float(non_null.max()),  # type: ignore[arg-type]
        "mean": round(float(non_null.mean()), 4),  # type: ignore[arg-type]
        "std": round(float(non_null.std()), 4),  # type: ignore[arg-type]
        "p25": round(float(non_null.quantile(0.25)), 4),  # type: ignore[arg-type]
        "p50": round(float(non_null.quantile(0.50)), 4),  # type: ignore[arg-type]
        "p75": round(float(non_null.quantile(0.75)), 4),  # type: ignore[arg-type]
    }


def _column_profile(series: pd.Series) -> dict[str, Any]:  # type: ignore[type-arg]
    """Build a per-column profile dict."""
    total = len(series)
    null_count = int(series.isna().sum())
    non_null_count = total - null_count
    unique_count = int(series.nunique(dropna=True))

    profile: dict[str, Any] = {
        "dtype": str(series.dtype),
        "total": total,
        "null_count": null_count,
        "null_pct": round(null_count / total * 100, 2) if total > 0 else 0.0,
        "unique_count": unique_count,
        "unique_pct": round(unique_count / non_null_count * 100, 2)
        if non_null_count > 0
        else 0.0,
        "sample_values": series.dropna().head(5).tolist(),
    }

    # Numeric stats
    _NUMERIC_KINDS = {"i", "u", "f", "c"}
    if hasattr(series.dtype, "kind") and series.dtype.kind in _NUMERIC_KINDS:
        profile["numeric_stats"] = _numeric_stats(series)

    return profile


def _quality_score(
    df: pd.DataFrame, column_profiles: dict[str, dict[str, Any]]
) -> float:
    """Compute a 0–100 overall quality score.

    Score is based on:
    - Completeness: (1 - overall_null_pct) * 60 points
    - Uniqueness: (1 - duplicate_row_pct) * 40 points
    """
    total_cells = df.size
    if total_cells == 0:
        return 0.0

    total_nulls = sum(p["null_count"] for p in column_profiles.values())
    completeness_ratio = 1.0 - (total_nulls / total_cells)

    total_rows = len(df)
    duplicate_rows = int(df.duplicated().sum())
    uniqueness_ratio = 1.0 - (duplicate_rows / total_rows) if total_rows > 0 else 1.0

    score = completeness_ratio * 60 + uniqueness_ratio * 40
    return round(score, 2)


def build_profile(df: pd.DataFrame) -> dict[str, Any]:
    """Build a comprehensive dataset profile."""
    column_profiles = {
        col: _column_profile(cast(pd.Series, df[col]))  # type: ignore[type-arg]
        for col in df.columns
    }
    duplicate_rows = int(df.duplicated().sum())
    quality = _quality_score(df, column_profiles)

    return {
        "summary": {
            "rows": int(len(df)),
            "columns": int(len(df.columns)),
            "duplicate_rows": duplicate_rows,
            "duplicate_pct": round(duplicate_rows / len(df) * 100, 2)
            if len(df) > 0
            else 0.0,
            "quality_score": quality,
        },
        "columns": column_profiles,
    }


# ─── CLI ──────────────────────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dataset profiling script")
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument(
        "--output",
        default=None,
        help="Optional path to save the profile report as JSON",
    )
    return parser.parse_args()


def main() -> int:
    try:
        args = parse_args()
        logger.info("Reading dataset: %s", args.input)
        df = read_csv_file(args.input)
        profile = build_profile(df)
        logger.info(
            "Profile generated — rows=%d, cols=%d, quality_score=%.2f",
            profile["summary"]["rows"],
            profile["summary"]["columns"],
            profile["summary"]["quality_score"],
        )

        output_str = json.dumps(profile, indent=2, ensure_ascii=False, default=str)
        print(output_str)

        if args.output:
            write_json_file(profile, args.output)
            logger.info("Profile saved to %s", args.output)

        return 0
    except Exception as exc:
        logger.exception("Profiling failed: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
