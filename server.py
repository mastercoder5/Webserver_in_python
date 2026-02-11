from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import os
from urllib.parse import urlparse

# ===== CONFIG =====
FOLDER = r"" #SET AS YOUR FOLDER
IP = "0.0.0.0"     # Listen on all interfaces
PORT = 443        # Default HTTPS port (no :port needed) YOU CAN REPLACE IF YOU WANT
# ==================

os.chdir(FOLDER)

# Clean URL mapping
URL_MAP = {
    "/": "ai.html",
    "/ai": "ai.html",
    "/info": "info.html",
}

class MappedHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path

        if path in URL_MAP:
            self.path = "/" + URL_MAP[path]

        return super().do_GET()

    # Optional: cleaner console
    def log_message(self, format, *args):
        print(f"[{self.client_address[0]}] {self.requestline}")

# Create server
httpd = HTTPServer((IP, PORT), MappedHandler)

# SSL (Python 3.12+ safe)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(
    certfile="server.crt",
    keyfile="server.key"
)

httpd.socket = context.wrap_socket(
    httpd.socket,
    server_side=True
)

print("===================================")
print(" HTTPS SERVER RUNNING ")
print("===================================")
print("Open in browser:")
print("  https://localhost/")
print("  GO TO YOUR STATIC IP")
print("===================================")

httpd.serve_forever()
