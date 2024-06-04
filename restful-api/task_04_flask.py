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

# Ruta principal que devuelve un mensaje de bienvenida
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Ruta que devuelve la lista de usuarios
@app.route('/data')
def data():
    usernames = list(users.keys())
    return jsonify(usernames)

# Ruta que devuelve el estado
@app.route('/status')
def status():
    return "OK"

# Ruta que devuelve los datos de un usuario específico
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404

# Ruta para agregar un nuevo usuario
@app.route('/add_user', methods=['POST'])
def add_user():
    if not request.json or 'username' not in request.json:
        abort(400)  # Bad Request if JSON is malformed or 'username' is missing
    
    username = request.json['username']
    if username in users:
        return "User already exists", 400  # Bad Request if user already exists

    users[username] = {
        'name': request.json.get('name'),
        'age': request.json.get('age'),
        'city': request.json.get('city')
    }
    
    return jsonify({"message": "User added successfully", "user": users[username]}), 201  # Created

@app.errorhandler(404)
def page_not_found(e):
    return "404 Not Found", 404

@app.errorhandler(400)
def bad_request(e):
    return "400 Bad Request", 400

if __name__ == "__main__":
    app.run(port=5000)
