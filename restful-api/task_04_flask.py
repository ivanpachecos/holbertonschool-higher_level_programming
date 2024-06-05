"""
This script sets up a simple HTTP server using Flask.
The server handles various endpoints and serves text or JSON responses.
"""

from flask import Flask, jsonify

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    }
@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    if not users:
        return jsonify([]), 200
    

if __name__ == '__main__':
    app.run()
