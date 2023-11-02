import logging
import json
from dataclasses import dataclass


@dataclass
class CustomJsonFormatter(logging.Formatter):

    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record),
            'name': record.name,
            'level': record.levelname,
            'message': record.getMessage(),
        }
        return json.dumps(log_record)