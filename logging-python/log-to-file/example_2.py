import logging

logging.basicConfig(level=logging.DEBUG, filename="example_2.log", filemode="w")
logging.debug("debug message")
logging.warning("warning message")

try:
    raise Exception("wtf, mate")
except Exception as e:
    logging.exception(e)
    logging.exception("Uh oh!")
    logging.info("Heads up", exc_info=True)