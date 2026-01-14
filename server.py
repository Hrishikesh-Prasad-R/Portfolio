import http.server
import socketserver
import os

PORT = 8000

class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle rewrites manually for local dev
        if self.path == '/home' or self.path == '/home/':
            self.path = '/index.html'
        elif self.path == '/contactme' or self.path == '/contactme/':
            self.path = '/contacts.html'
        elif self.path == '/about' or self.path == '/about/':
            self.path = '/about.html'
        elif self.path == '/projects' or self.path == '/projects/':
            self.path = '/projects.html'
            
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = CleanUrlHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Clean URLs enabled: /home, /contactme, /about, /projects")
    httpd.serve_forever()
