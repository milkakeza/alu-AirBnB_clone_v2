#!/usr/bin/python3

"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    
    """Renders a template displaying a list of all states."""

    return render_template('9-states.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    
    """Renders a template displaying the state with the given ID and its cities.

    If a state with the specified ID exists, the template is rendered with the state's
    details and associated cities. If no such state is found, it renders a template
    indicating that the state was not found.
    
    Args:
        id (str): The ID of the state to be displayed.
    """

    for state in storage.all(State).values():
	if state.id == id:
	    return render_template('9-states.html', state=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
