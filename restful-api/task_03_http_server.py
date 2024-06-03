#!/usr/bin/python3
"""This script sets up a simple HTTP server using the http.server module.
The server handles various endpoints and serves text or JSON responses.
"""

import http.server
import socketserver
import json

# Define the port on which the server will listen
PORT = 8000

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """Request handler class to handle HTTP GET requests."""

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        if self.path == '/':
            self.handle_root()
        elif self.path == '/data':
            self.handle_data()
        elif self.path == '/status':
            self.handle_status()
        else:
            self.handle_not_found()

    def handle_root(self):
        """Handle the root endpoint '/' by returning a simple text response."""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        response = "Hello, this is a simple API!"
        self.wfile.write(response.encode())

    def handle_data(self):
        """Handle the '/data' endpoint by returning a sample JSON dataset."""
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
        """Handle undefined endpoints by returning a 404 Not Found response."""
        self.send_response(404)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"error": "Not Found", "message": "Endpoint not found"}
        self.wfile.write(json.dumps(response).encode())

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
