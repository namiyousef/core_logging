import logging
import logging.config

from core_logging.config import LOGGING_CONFIG

class LoggingConfig:
    def __init__(self, logger_name, json_logger=False):
        logging.config.fileConfig(LOGGING_CONFIG)
        
        if json_logger:
            logging_config = 'json'
        else:
            logging_config = ''

        self.logger = logging.getLogger(logging_config)
        self.logger.name = logger_name
    

    def add_handlers_from_logger(self, logger_name):
        logger = logging.getLogger(logger_name)
        for handler in logger.handlers:
            self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger