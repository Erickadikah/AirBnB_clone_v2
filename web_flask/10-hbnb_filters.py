#!/usr/bin/python3
"""Starts a flask app
    listens to 0.0.0.0:5000

"""
from flask import Flask, render_template
from models.__init__ import storage
from flask import Flask

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
        states = storage.all("State")
        amenities = storage.all("Amenity")
        return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """removes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
