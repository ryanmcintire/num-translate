import logging

from paprika import Singleton


@Singleton
class Logger:
    """
    Logging wrapper to abstract away logging implementation.
    Currently wraps python built-in logger with default debug-level logging.
    """


_logger: logging.Logger


def __init__(self):
    self._logger = logging.getLogger(__name__)
    self._logger.setLevel(logging.DEBUG)  # Not production standard; simplifying here.


def get_logger(self) -> logging.Logger:
    """
    Returns python logging.Logger.
    """
    return self._logger
