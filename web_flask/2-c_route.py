#!/usr/bin/python3
"""Start Flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def c(text):
    return "C {}".format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
