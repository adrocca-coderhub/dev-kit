from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from scripts.utils.logger import get_logger


logger = get_logger("config_utils")


def load_config(path: str | Path) -> dict[str, Any]:
    """Load a YAML config file and return it as a dict.

    Raises FileNotFoundError if the file does not exist.
    Raises ValueError if the file is empty or not a valid YAML mapping.
    """
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    if data is None:
        raise ValueError(f"Config file is empty: {config_path}")

    if not isinstance(data, dict):
        raise ValueError(
            f"Config file must be a YAML mapping (got {type(data).__name__}): {config_path}"
        )

    logger.info("Config loaded from %s", config_path)
    return data  # type: ignore[return-value]


def get_db_engine(config: dict[str, Any]) -> Any:
    """Build a SQLAlchemy engine from a config dict.

    Expected config structure:
        database:
          dialect: postgresql          # required
          host: localhost              # required
          port: 5432                   # optional, default 5432
          name: mydb                   # required
          user: myuser                 # required
          password: secret             # required
          schema: public               # optional

    Returns a sqlalchemy.Engine instance.
    Raises KeyError if required keys are missing.
    Raises ImportError if sqlalchemy is not installed.
    """
    try:
        from sqlalchemy import create_engine  # noqa: PLC0415
        from sqlalchemy.engine import Engine  # noqa: PLC0415, F401
    except ImportError as exc:
        raise ImportError(
            "sqlalchemy is required to use get_db_engine. "
            "Install it with: pip install sqlalchemy"
        ) from exc

    db_cfg: dict[str, Any] = config.get("database", {})

    required_keys = ["dialect", "host", "name", "user", "password"]
    missing = [k for k in required_keys if k not in db_cfg]
    if missing:
        raise KeyError(f"Missing required database config keys: {', '.join(missing)}")

    dialect: str = db_cfg["dialect"]
    host: str = db_cfg["host"]
    port: int = int(db_cfg.get("port", 5432))
    name: str = db_cfg["name"]
    user: str = db_cfg["user"]
    password: str = db_cfg["password"]

    url = f"{dialect}://{user}:{password}@{host}:{port}/{name}"

    connect_args: dict[str, Any] = {}
    schema = db_cfg.get("schema")
    if schema and dialect.startswith("postgresql"):
        connect_args["options"] = f"-csearch_path={schema}"

    engine = create_engine(url, connect_args=connect_args)
    logger.info("Database engine created: %s://%s:%s/%s", dialect, host, port, name)
    return engine
