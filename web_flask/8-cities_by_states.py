#!/usr/bin/python3
""" flask route """
from flask import Flask, escape, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """  close session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def statelist():
    """ list states """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', statelist=states)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
