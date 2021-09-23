import logging
import sys

from paprika import singleton


@singleton
class Logger:
    """
    Logging wrapper to abstract away logging implementation.
    Currently wraps python built-in logger with default debug-level logging.
    """

    _logger: logging.Logger

    def __init__(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)  # Not production standard; simplifying for project
        std_handler = logging.StreamHandler(sys.stdout)
        std_handler.setLevel(logging.DEBUG)
        logger.addHandler(std_handler)
        self._logger = logger

    def get_logger(self) -> logging.Logger:
        """
        Returns python logging.Logger.
        """
        return self._logger

