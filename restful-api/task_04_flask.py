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
    return jsonify(list(users.keys())), 200

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    user_add = request.get_json()
    username = user_add.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_add
    return jsonify({"message": "User added", "user": user_add}), 201

if __name__ == '__main__':
    app.run()
