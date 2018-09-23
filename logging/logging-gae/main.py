import logging

import google.cloud.logging
from flask import Flask


# Instantiates a client
client = google.cloud.logging.Client()

# Connects the logger to the root logging handler; by default this captures
# all logs at INFO level and higher
client.setup_logging()


logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/')
def index():
    logger.warning("Can I has log level?")
    return "Check stackdriver for log entries."


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
