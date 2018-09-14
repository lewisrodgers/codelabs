import logging


def log_to_file(msg):
    logging.basicConfig(filename="output_file.log")
    logging.warning(msg)

log_to_file("I'm in a file!")
