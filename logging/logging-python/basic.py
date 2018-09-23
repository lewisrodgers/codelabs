import logging


# Set logging level in order to output all
logging.basicConfig(level=logging.DEBUG)

logging.debug("Not printed by default")
logging.info("Not printed by default", extra={"hello":"world"})
logging.warning("A warning message")
logging.error("An error message")
