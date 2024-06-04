#!/usr/bin/python3
"""
This script sets up a simple HTTP server using Flask.
The server handles various endpoints and serves text or JSON responses.
"""

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Diccionario de usuarios en memoria
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"},
    "alice": {"name": "Alice", "age": 25, "city": "San Francisco"}
}

@app.route('/')
def hello_world():
    return "Hello, this is a simple API"

@app.route('/data')
def data():
    # Obtener la lista de nombres de usuario
    usernames = list(users.keys())
    # Devolver la lista de nombres de usuario como una respuesta JSON
    return jsonify(usernames)

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404

@app.route('/add_user', methods=['POST'])
def add_user():
    if not request.json or 'username' not in request.json:
        abort(400)

    username = request.json['username']
    if username in users:
        return "User already exists", 400

    users[username] = {
        'name': request.json.get('name'),
        'age': request.json.get('age'),
        'city': request.json.get('city')
    }
    
    return jsonify({"message": "User added successfully", "user": users[username]}), 201

if __name__ == "__main__":
    app.run()
