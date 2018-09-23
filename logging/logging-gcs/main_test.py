from main import StorageService


def test_create_bucket(mocker):
    storage = mocker.patch('main.storage')
    logger = mocker.patch('main.logging')
    client = storage.Client()
    service = StorageService(client, logger)
    service.create_bucket("hello")
    client.create_bucket.assert_called_with("hello")
