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



if __name__ == "__main__":
    app.run(port=5000)
