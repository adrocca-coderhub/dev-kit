from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd


def ensure_parent_dir(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def read_csv_file(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)


def write_csv_file(df: pd.DataFrame, path: str | Path) -> None:
    ensure_parent_dir(path)
    df.to_csv(path, index=False)


def read_json_file(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json_file(data: Any, path: str | Path) -> None:
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
