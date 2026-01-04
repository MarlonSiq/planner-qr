from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        key = query.get("key", [None])[0]

        SECRET_KEY = os.environ.get("SECRET_KEY")
        DESTINATION_URL = os.environ.get("DESTINATION_URL")

        if key == SECRET_KEY:
            self.send_response(302)
            self.send_header("Location", DESTINATION_URL)
            self.end_headers()
        else:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Acesso negado")


