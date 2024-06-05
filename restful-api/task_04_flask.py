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
    # Extract the list of usernames from the users dictionary
    usernames = list(users.keys())
    # Return the usernames as a JSON response
    return jsonify(usernames), 200

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users), 200

if __name__ == '__main__':
    app.run()
