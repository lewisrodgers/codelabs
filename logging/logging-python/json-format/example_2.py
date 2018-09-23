# https://github.com/madzak/python-json-logger

import logging
from pythonjsonlogger import jsonlogger


logger = logging.getLogger()


logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

logger.warning("My json logger")