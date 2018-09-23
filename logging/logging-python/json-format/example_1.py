import logging
import json

format = "{'user': %(user)s}"
logging.basicConfig(format=format)
d = {'user': 'lewis'}
logger = logging.getLogger('mylogger')
logger.warning('Warning message', extra=d)