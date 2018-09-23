# Imports the Google Cloud client library
import google.cloud.logging

# Instantiates a client
client = google.cloud.logging.Client()

# Connects the logger to the root logging handler; by default this captures
# all logs at INFO level and higher
cloud_handler = client.get_default_handler()

# Imports Python standard library logging
import logging

logger = logging.getLogger('Cloud Logger')
logger.setLevel(logging.INFO)
logger.addHandler(cloud_handler)
# Emits the data using the standard logging module
logger.warning('get default handler')
