# Imports the Google Cloud client library
import google.cloud.logging


def setup():
    client = google.cloud.logging.Client()
    return client.get_default_handler()
