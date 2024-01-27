#!/usr/bin/python3
""" Starts a Flash Web Application HBNB.
"""
# Import Flask
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

# Define the routes
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
