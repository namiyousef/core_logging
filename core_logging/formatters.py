from pythonjsonlogger.jsonlogger import JsonFormatter
import logging



# TODO in principle both flask and fastapi can use Gunicorn, which has it's own format... So the problem is not just with flask it is also with gunicorn
# TODO the question is... whether we want to even do this or not...! Either way, it is not urgent. You can use the default logger from core_logging to have json logging on your applications!


class CustomJsonFormatter(JsonFormatter):

    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)

class ColouredFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    green = '\x1b[0;32m'
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    FORMATS = {
        logging.INFO: red
    }

    colours = {
        logging.DEBUG: grey,
        logging.INFO: green,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: bold_red
    }

    exclude_fields = ['funcName', 'module']
    def __init__(self, *args, **kwargs):
        logging.Formatter.__init__(self, *args, **kwargs)

    def format(self, record):
        levelno = record.levelno
        record.levelname = self._colour_text(record.levelname, levelno)
        
        return logging.Formatter.format(self, record)


    def _colour_text(self, text, level):
        text = f'{self.colours[level]}{text}{self.reset}'
        return text