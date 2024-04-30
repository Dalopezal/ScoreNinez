from http.server import HTTPServer, BaseHTTPRequestHandler
import paths
from Controller import *


class Handler(BaseHTTPRequestHandler):

    def handle_request(self, path):
        path_functions = paths.PATHS_FUNCTIONS
        controller = Controller()
        if path in path_functions:
            function_name = path_functions[path]
            function = getattr(controller, function_name)
            function(self)
        else:
            self.send_error(404)

    def do_POST(self):
        self.handle_request(self.path)

    def do_GET(self):
        self.handle_request(self.path)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.end_headers()


my_server = HTTPServer(('', 8088), Handler)
try:
    print('Server running..')
    my_server.serve_forever()
except KeyboardInterrupt:
    print('Stopped server..')
    my_server.server_close()
