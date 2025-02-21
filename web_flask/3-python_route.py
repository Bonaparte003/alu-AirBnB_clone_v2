#!/usr/bin/python3
from flask import Flask
"""Start a Flask web application"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Print Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Print HBNB!"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """C text"""
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Python is cool"""
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
