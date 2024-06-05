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
    if not users:
        return jsonify([]), 200
    usernames = list(users.keys())
    return jsonify(usernames), 200

@app.route('/status')
def status():
    return 'OK'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

if __name__ == '__main__':
    app.run()
