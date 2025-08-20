from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv

def load_env(dotenv_path: str | None = None) -> None:
    """
    Load environment variables from .env (or a custom path).
    """
    load_dotenv(dotenv_path)

def get_key(name: str, required: bool = True, default: str | None = None) -> str | None:
    """
    Read an environment variable. If required and missing, raise a clear error.
    """
    val = os.getenv(name, default)
    if required and (val is None or str(val).strip() == ""):
        raise KeyError(f"Missing required environment variable: {name}")
    return val

def data_dir() -> Path:
    """
    Resolve the DATA_DIR env var (defaults to ./data), as an absolute Path.
    """
    return Path(os.getenv("DATA_DIR", "./data")).expanduser().resolve()
