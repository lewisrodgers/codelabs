# https://pypi.org/project/coloredlogs/

import logging
import coloredlogs


class MyLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        coloredlogs.install(level='DEBUG')

    def print_example_logs(self):
        self.logger.debug("this is a debugging message")
        self.logger.info("this is an informational message")
        self.logger.warning("this is a warning message")
        self.logger.error("this is an error message")
        self.logger.critical("this is a critical message")
