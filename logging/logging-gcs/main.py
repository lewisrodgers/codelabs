import logging
from google.cloud import storage

from StorageService import StorageService


logger = logging.getLogger(__name__)
logging.basicConfig(level='DEBUG')

log_bucket = StorageService(storage.Client(), logger)
log_bucket.create_bucket('codelabs-logging-gcs')
