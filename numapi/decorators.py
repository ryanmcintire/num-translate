from collections.abc import Callable
from typing import Any
import functools

from numapi.services.log_service import Logger

_logger = Logger().get_logger()


def for_all_methods(decorator):
    """
    Decorates all methods on class with the supplied decorator.
    """

    def decorate(cls):
        for attr in cls.__dict__:  # there's propably a better way to do this
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls

    return decorate


def debug(func: Callable[..., Any]):
    """
    Wraps method (or all class methods) which logs to service's logger.debug function being invoked,
    arguments used to call, and the return value from the function invoked.
    """

    @functools.wraps(func)
    def run(*args, **kwargs):
        _logger.debug("Calling " + func.__name__)
        _logger.debug(f"args: {args} - kwargs: {kwargs}")
        value = func(*args, **kwargs)
        _logger.debug(f"Return from {func.__name__}: {value}")
        return value

    return run
