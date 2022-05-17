from http.server import BaseHTTPRequestHandler, HTTPServer

class LoggerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Listening...".encode())
        print(self.address_string)
    

class Logger:
    def __init__(self, port: int, mode: int):
        self.port = port
        self.server = None
        self.mode = mode
        
    def start(self):
        if self.mode == 1:
            print("Started HTTP server on port " + str(self.port) + ".")
        
        self.server = HTTPServer(('', self.port), LoggerHandler)
        self.server.serve_forever()