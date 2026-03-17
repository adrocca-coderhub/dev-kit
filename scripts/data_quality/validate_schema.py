from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from typing import Any, Optional, cast

import pandas as pd

from scripts.utils.file_utils import read_csv_file, write_json_file
from scripts.utils.logger import get_logger


logger = get_logger("validate_schema")


# ─── Schema definition helpers ───────────────────────────────────────────────


@dataclass
class ColumnRule:
    """Validation rule for a single column."""

    name: str
    required: bool = True
    dtype: Optional[str] = None  # "numeric", "string", "datetime", "boolean"
    nullable: bool = True
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    allowed_values: Optional[list[Any]] = field(default=None)


# ─── Validation logic ─────────────────────────────────────────────────────────


@dataclass
class ColumnResult:
    column: str
    passed: bool
    violations: list[str] = field(default_factory=list)


@dataclass
class ValidationReport:
    status: str  # "passed" | "failed"
    total_columns_checked: int
    columns_passed: int
    columns_failed: int
    missing_required_columns: list[str]
    column_results: list[dict[str, Any]]

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "total_columns_checked": self.total_columns_checked,
            "columns_passed": self.columns_passed,
            "columns_failed": self.columns_failed,
            "missing_required_columns": self.missing_required_columns,
            "column_results": self.column_results,
        }


_NUMERIC_KINDS = {"i", "u", "f", "c"}  # int, uint, float, complex numpy kinds
_DATETIME_KINDS = {"M"}  # datetime64


def _is_numeric(series: pd.Series) -> bool:  # type: ignore[type-arg]
    return hasattr(series.dtype, "kind") and series.dtype.kind in _NUMERIC_KINDS


def _is_datetime(series: pd.Series) -> bool:  # type: ignore[type-arg]
    return hasattr(series.dtype, "kind") and series.dtype.kind in _DATETIME_KINDS


def _is_boolean(series: pd.Series) -> bool:  # type: ignore[type-arg]
    return series.dtype == bool or str(series.dtype) == "bool"


def _check_dtype(series: pd.Series, expected: str) -> Optional[str]:  # type: ignore[type-arg]
    """Return a violation string if the dtype does not match, else None."""
    actual = str(series.dtype)
    if expected == "numeric" and not _is_numeric(series):
        return f"expected numeric dtype, got '{actual}'"
    if expected == "string" and series.dtype != object:
        return f"expected string/object dtype, got '{actual}'"
    if expected == "datetime" and not _is_datetime(series):
        return f"expected datetime dtype, got '{actual}'"
    if expected == "boolean" and not _is_boolean(series):
        return f"expected boolean dtype, got '{actual}'"
    return None


def validate_column(df: pd.DataFrame, rule: ColumnRule) -> ColumnResult:
    """Validate a single column against its rule."""
    violations: list[str] = []

    # Column existence
    if rule.name not in df.columns:
        if rule.required:
            return ColumnResult(
                column=rule.name,
                passed=False,
                violations=["column is required but missing"],
            )
        # Optional and absent — nothing else to check
        return ColumnResult(column=rule.name, passed=True)

    series: pd.Series = cast(pd.Series, df[rule.name])  # type: ignore[type-arg]
    null_count: int = series.isna().sum()  # type: ignore[assignment]

    # Nullability
    if not rule.nullable and null_count > 0:
        violations.append(f"column is non-nullable but has {null_count} null value(s)")

    # dtype check
    if rule.dtype is not None:
        dtype_violation = _check_dtype(series, rule.dtype)
        if dtype_violation:
            violations.append(dtype_violation)

    # Range checks (only meaningful for numeric columns)
    if rule.min_value is not None or rule.max_value is not None:
        if _is_numeric(series):
            non_null = series.dropna()
            if rule.min_value is not None:
                below = int((non_null < rule.min_value).sum())
                if below > 0:
                    violations.append(
                        f"{below} value(s) below minimum {rule.min_value}"
                    )
            if rule.max_value is not None:
                above = int((non_null > rule.max_value).sum())
                if above > 0:
                    violations.append(
                        f"{above} value(s) above maximum {rule.max_value}"
                    )
        else:
            violations.append("min_value/max_value rules require a numeric column")

    # Allowed values check
    if rule.allowed_values is not None:
        non_null_series = series.dropna()
        invalid_mask = ~non_null_series.isin(rule.allowed_values)
        invalid_count: int = invalid_mask.sum()  # type: ignore[assignment]
        if invalid_count > 0:
            invalid_series: pd.Series = cast(pd.Series, non_null_series[invalid_mask])  # type: ignore[type-arg]
            sample = invalid_series.unique()[:5].tolist()
            violations.append(
                f"{invalid_count} value(s) not in allowed set "
                f"{rule.allowed_values}. Sample: {sample}"
            )

    return ColumnResult(
        column=rule.name,
        passed=len(violations) == 0,
        violations=violations,
    )


def validate_schema(
    df: pd.DataFrame,
    rules: list[ColumnRule],
) -> ValidationReport:
    """Validate a DataFrame against a list of column rules.

    Returns a ValidationReport with per-column results and an overall status.
    """
    missing_required: list[str] = [
        rule.name for rule in rules if rule.required and rule.name not in df.columns
    ]

    column_results: list[ColumnResult] = [validate_column(df, rule) for rule in rules]

    passed = [r for r in column_results if r.passed]
    failed = [r for r in column_results if not r.passed]

    overall_status = "passed" if len(failed) == 0 else "failed"

    return ValidationReport(
        status=overall_status,
        total_columns_checked=len(column_results),
        columns_passed=len(passed),
        columns_failed=len(failed),
        missing_required_columns=missing_required,
        column_results=[
            {
                "column": r.column,
                "passed": r.passed,
                "violations": r.violations,
            }
            for r in column_results
        ],
    )


# ─── Config-driven validation ─────────────────────────────────────────────────


def _rules_from_config(config: dict[str, Any]) -> list[ColumnRule]:
    """Parse ColumnRule objects from a YAML config dict.

    Expected config structure:
        schema:
          columns:
            - name: order_id
              required: true
              dtype: numeric
              nullable: false
            - name: status
              required: true
              dtype: string
              allowed_values: [active, inactive, pending]
            - name: amount
              required: true
              dtype: numeric
              min_value: 0
              max_value: 1000000
    """
    schema_cfg: dict[str, Any] = config.get("schema", {})
    columns_cfg: list[dict[str, Any]] = schema_cfg.get("columns", [])

    rules: list[ColumnRule] = []
    for col in columns_cfg:
        rules.append(
            ColumnRule(
                name=col["name"],
                required=bool(col.get("required", True)),
                dtype=col.get("dtype"),
                nullable=bool(col.get("nullable", True)),
                min_value=col.get("min_value"),
                max_value=col.get("max_value"),
                allowed_values=col.get("allowed_values"),
            )
        )
    return rules


def validate_from_config(
    df: pd.DataFrame,
    config: dict[str, Any],
) -> ValidationReport:
    """Validate a DataFrame using rules extracted from a YAML config dict."""
    rules = _rules_from_config(config)
    if not rules:
        raise ValueError(
            "No column rules found in config. "
            "Ensure 'schema.columns' is defined in the YAML config."
        )
    return validate_schema(df, rules)


# ─── CLI ──────────────────────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a dataset schema against expected column rules"
    )
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument(
        "--config",
        default=None,
        help="Optional YAML config path with schema rules",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Optional path to save the validation report as JSON",
    )
    return parser.parse_args()


def main() -> int:
    try:
        args = parse_args()

        logger.info("Reading dataset: %s", args.input)
        df = read_csv_file(args.input)

        if args.config:
            from scripts.utils.config_utils import load_config  # noqa: PLC0415

            logger.info("Loading schema config: %s", args.config)
            config = load_config(args.config)
            report = validate_from_config(df, config)
        else:
            # Default: just check all present columns exist (no type/null rules)
            rules = [ColumnRule(name=col, required=True) for col in df.columns]
            report = validate_schema(df, rules)

        import json  # noqa: PLC0415

        report_dict = report.to_dict()
        print(json.dumps(report_dict, indent=2, ensure_ascii=False))

        if args.output:
            write_json_file(report_dict, args.output)
            logger.info("Validation report saved to %s", args.output)

        if report.status == "failed":
            logger.warning(
                "Schema validation FAILED: %d column(s) with violations",
                report.columns_failed,
            )
            return 1

        logger.info("Schema validation passed")
        return 0

    except Exception as exc:
        logger.exception("Schema validation failed: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
