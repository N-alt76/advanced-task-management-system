"""Logging configuration for the application."""

import logging
from pathlib import Path


def get_logger(name: str = "ams") -> logging.Logger:
    """Return the shared application logger, configured once."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(threadName)s - %(message)s"
    )
    file_handler = logging.FileHandler(Path("ams.log"), encoding="utf-8")
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
