#!/usr/bin/python3

from validate_email import validate_email
from http.server import BaseHTTPRequestHandler, HTTPServer


class MailCheck(BaseHTTPRequestHandler):
    def do_GET(self):
        mail = self.path.replace("/", "")
        mail_is_valid = validate_email(mail, verify=True)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if mail_is_valid == None:
            response = '{"mail_active": false}'
        else:
            response = '{"mail_active": %s}' % mail_is_valid

        self.wfile.write(bytes(response, "utf8"))
        return


print("starting server...")
server_address = ("0.0.0.0", 8000)
httpd = HTTPServer(server_address, MailCheck)
print("running server...")
httpd.serve_forever()
