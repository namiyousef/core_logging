import logging
import logging.config
import os

LOGGING_CONFIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging_configs')
LOGGING_CONFIG_BASE = os.path.join(LOGGING_CONFIG_DIR, 'base.conf')

LOGGING_CONFIG_FASTAPI = os.path.join(LOGGING_CONFIG_DIR, 'fastapi.conf')


# what is my goal? I want to create a logging library that allows me to:
# - have my logs go to elastic search, console or file in a standardised json way
# - have my console logs to be meaningful, and potentially have colors 
# - have the option to attach my logs (e.g. console) to the logs of a framework that I'm using, e.g. fastapi coloured logs but send the exact same logs (with the fastapi specific logs) to elastic search in my customised json format!