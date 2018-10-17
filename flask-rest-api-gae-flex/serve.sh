#!/bin/sh
source $(pipenv --venv)/bin/activate
gunicorn -b :8080 app.main:app