#!/usr/bin/python3
# Import Flask
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

# Define the route for the index page
@app.route('/', strict_slashes=False)
def hello_hbnb():
    # Return the message to be displayed
    return 'Hello HBNB!'

# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
