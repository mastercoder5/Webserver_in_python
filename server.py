from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import os
from urllib.parse import urlparse

# Folder where your HTML files live
FOLDER = r"C:\Users\shail\OneDrive\Desktop\ai agent"
os.chdir(FOLDER)

IP = "(Your IP)"
PORT = 8000 #You can change the port

# Mapping: clean URL -> file
URL_MAP = {
    "/": "ai.html",
    "/ai": "ai.html",
    "/info": "info.html",
}

class MappedHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Strip query strings (?x=1) and fragments
        path = urlparse(self.path).path

        if path in URL_MAP:
            self.path = "/" + URL_MAP[path]

        return super().do_GET()

    # Prevent noisy favicon errors
    def log_message(self, format, *args):
        pass


httpd = HTTPServer((IP, PORT), MappedHandler)

# TLS (Python 3.12 safe)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(
    certfile="server.crt",
    keyfile="server.key"
)

httpd.socket = context.wrap_socket(
    httpd.socket,
    server_side=True
)

print(f"Serving HTTPS on https://{IP}:{PORT}")
print("Routes:")
for k, v in URL_MAP.items():
    print(f"  {k} → {v}")

httpd.serve_forever()

