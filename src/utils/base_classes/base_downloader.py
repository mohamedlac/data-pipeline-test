import logging
from src.utils.logging_utils.custom_logger import CustomJsonFormatter


class BaseDownloader:

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = CustomJsonFormatter()  # Your custom formatter here
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_message(self, message, level="info"):
        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "critical":
            self.logger.critical(message)
        else:
            self.logger.warning(f"Unknown level {level} for message logging")
