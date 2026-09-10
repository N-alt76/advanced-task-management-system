"""Reusable decorators for logging and timing function calls."""

import functools
import logging
import time
from typing import Any, Callable

from .logger import get_logger


def log_execution(function: Callable[..., Any]) -> Callable[..., Any]:
    """Log the start, success, and failure of a function call."""
    @functools.wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger = get_logger()
        logger.info("Starting %s", function.__name__)
        try:
            result = function(*args, **kwargs)
        except Exception:
            logger.exception("Exception in %s", function.__name__)
            raise
        logger.info("Finished %s", function.__name__)
        return result

    return wrapper


def measure_time(function: Callable[..., Any]) -> Callable[..., Any]:
    """Log how long a function takes to complete."""
    @functools.wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        try:
            return function(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start_time
            logging.getLogger("ams").info(
                "%s took %.4f seconds", function.__name__, elapsed
            )

    return wrapper
