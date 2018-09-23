import logging
import logging.config

import yaml


with open('config.yaml') as f:
    config = yaml.load(f)
    logging.warning(config)
    logging.config.dictConfig(config)

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
