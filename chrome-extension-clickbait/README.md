# Clickbait headline detection POC

The client makes a request to the cloud function endpoint. The cloud function then makes a request to the AutoML endpoint and returns the classification results back to the client where it's displayed.

## Client

The client is a basic webapp that makes use of XHR. This could be refactored as a Chrome extension.