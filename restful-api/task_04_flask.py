"""
This script sets up a simple HTTP server using Flask.
The server handles various endpoints and serves text or JSON responses.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Users data
users = {}

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    # Return the usernames as a JSON response
    return jsonify(list(users.keys())), 200

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if username not in user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

if __name__ == '__main__':
    app.run()
