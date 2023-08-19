#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /airbnb-onepage/: Displays 'Hello HBNB!' from the new route
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route("/airbnb-onepage/", strict_slashes=False)
def airbnb_onepage():
    """Displays 'Hello HBNB!' from the new route"""
    return "Hello HBNB! This is the /airbnb-onepage/ route."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

