from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
from LLog import LLog

class SLHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handle GET
    def do_GET(self):
        log = LLog('japn201vocab.csv')
        try:
            # Send 200 response
            self.send_response(200)

            # Send header
            self.send_header('Content-type','text-html')
            self.end_headers()

            # Send Content
            self.wfile.write(log.print_html())
            return
        except IOError:
            self.send_error(404, 'file not found')

def run():
    try:
        print("Starting server...")
        server_address = ('127.0.0.1',8080)
        httpd = HTTPServer(server_address, SLHTTPRequestHandler)
        print("Server is running...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the server')
        httpd.socket.close()

if __name__ == "__main__":
    run()


