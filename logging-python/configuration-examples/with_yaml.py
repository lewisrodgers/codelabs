import logging
import logging.config

import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)
    logging.config.fileConfig(config)

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')