import http.server
import socketserver
import os
import sys

PORT = 5173
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == "__main__":
    # Allow port reuse
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"CONTRIB Web Server started at http://localhost:{PORT}")
            httpd.serve_forever()
    except Exception as e:
        print(f"Error starting server on port {PORT}: {e}")
        # Try alternate port
        ALT_PORT = 3000
        with socketserver.TCPServer(("", ALT_PORT), Handler) as httpd:
            print(f"CONTRIB Web Server started on fallback http://localhost:{ALT_PORT}")
            httpd.serve_forever()
