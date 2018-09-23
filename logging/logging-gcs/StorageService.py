class StorageService():
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def create_bucket(self, bucket_name):
        self.client.create_bucket(bucket_name)
        self.logger.log_text("{}: Bucket named: {} created".format(
            self.logger.name, bucket_name))
