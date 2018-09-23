from google.cloud import logging


class LoggingService():
    def __init__(self, client):
        self.client = client

    def logger_name(self, name):
        self.client.logger(name)
