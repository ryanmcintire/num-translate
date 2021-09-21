from collections.abc import Callable
from typing import Any
import functools

from numapi.log_service import Logger

_logger = Logger().get_logger()


def debug(func: Callable[..., Any]):
    """
    Wraps method which logs to service's logger.debug function being invoked,
    arguments used to call, and the return value from the function invoked.
    """
    @functools.wraps(func)
    def run(*args, **kwargs):
        _logger.debug("Calling", func.__name__)
        _logger.debug(f"args: {args} - kwargs: {kwargs}")
        value = func(*args, **kwargs)
        _logger.debug(f"Return from {func.__name__}: {value}")
        return value

    return run
