#!/usr/bin/python3
""" Starts Flask web application """

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


def StartFlask():
    """ Starts Flask web application """
    app.run(host='0.0.0.0', port=5000)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ Display States List  """
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states.values())


@app.teardown_appcontext
def teardown_db(exception):
    """ Eliminate current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    StartFlask()
