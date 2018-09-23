import logging
import logging.config

import yaml


with open('config.yaml') as f:
    config = yaml.load(f)
    logging.config.dictConfig(config)

# create logger
logger = logging.getLogger(__name__)

# 'application' code
logger.info('cloudlogger message')
