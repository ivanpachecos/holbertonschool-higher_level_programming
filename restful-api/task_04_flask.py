#!/usr/bin/python3
"""
This script sets up a simple HTTP server using Flask.
The server handles various endpoints and serves text or JSON responses.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
