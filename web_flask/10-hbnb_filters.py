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


@app.route('/states', strict_slashes=False)
def statelist():
    """ list states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', statelist=states)


@app.route('/states/<id>', strict_slashes=False)
def stateid(id):
    """ list state by id """
    states = storage.all(State)
    id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
