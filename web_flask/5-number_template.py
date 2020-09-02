#!/usr/bin/python3
""" flask route """
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ hello message """
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ hello message """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def Ctext(text):
    """ c is fun """
    text = text.replace('_', ' ')
    return 'C %s' % escape(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Pythontext(text='is_cool'):
    """ python is magic """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def Nnumber(n):
    """ numbers """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def NumTemp(n):
    """ number template """
    return render_template('5-number.html', num=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
