# Imports the Google Cloud client library
import google.cloud.logging

# Instantiates a client
client = google.cloud.logging.Client()
logger = client.logger('basic')

logger.log_text("zomg")
