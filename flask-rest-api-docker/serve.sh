#!/bin/sh

# The first command defines the main script to be executed by Flask, 
# just like we did when we ran the "Hello, world!" application. The second 
# one activates the virtual environment, created by pipenv, so our application
# can find and execute its dependencies. Lastly, we run our Flask application
# listening to all interfaces on the computer (-h 0.0.0.0).
export FLASK_APP=./app/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0