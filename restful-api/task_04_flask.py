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

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    username = user_data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = {
        "name": user_data.get('name'),
        "age": user_data.get('age'),
        "city": user_data.get('city')
    }
    return jsonify({"message": "User added successfully"}), 201

@app.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username]), 200

if __name__ == '__main__':
    app.run()
