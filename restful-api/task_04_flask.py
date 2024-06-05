"""
This script sets up a simple HTTP server using Flask.
The server handles various endpoints and serves text or JSON responses.
"""

from flask import Flask, jsonify

app = Flask(__name__)

# Users data
users = {}

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

'''
@app.route('/data')
def data():
    username = (list(users.keys()))
    if not users:
        return jsonify([]), 200
    return jsonify(username), 200
'''

if __name__ == '__main__':
    app.run()
