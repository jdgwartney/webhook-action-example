from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        varLen = int(self.headers['Content-Length'])
        data = self.rfile.read(varLen)
        print(data)
        self.wfile.write('data: %s\n' % str(data))

        self.wfile.write('Client: %s\n' % str(self.client_address))
        #self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n' % self.path)

        return

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), WebhookHandler)
    print('Starting server, use <Ctrl-C> to stop server.serve_forever()')
    server.serve_forever()