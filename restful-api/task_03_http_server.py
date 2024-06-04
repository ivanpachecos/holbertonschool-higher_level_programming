#!/usr/bin/python3
"""
This script sets up a simple HTTP server using the http.server module.
The server handles various endpoints and serves text or JSON responses.
"""

# Importación de módulos necesarios
import http.server
import socketserver
import json

PORT = 8000


class SimpleRequest(http.server.BaseHTTPRequestHandler):
    # Manejo de peticiones GET
    def do_GET(self):
        if self.path == '/':
            self.handle_root()
        elif self.path == '/data':
            self.handle_data()
        elif self.path == '/status':
            self.handle_status()
        else:
            self.handle_not_found()

    def handle_root(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Hello, this is a simple API!".encode())

    def handle_data(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"name": "John", "age": 30, "city": "New York"}
        self.wfile.write(json.dumps(response).encode())

    def handle_status(self):
        """Handle the '/status' endpoint by returning a simple status message."""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        response = "OK"
        self.wfile.write(response.encode())

    def handle_not_found(self):
        self.send_response(404)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("404 Not Found".encode())

# Configuración del servidor HTTP
with socketserver.TCPServer(("", PORT), SimpleRequest) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
