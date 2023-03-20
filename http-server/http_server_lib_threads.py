from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

port = 8084
addr = '0.0.0.0'

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        content = '''
        
        <html> 
            <head>
                <title>
                    Aula-Redes
                </title>
            </head>
            <body> 
                <h1> IFPR - Campus Cascavel </h1>
                <p> Programando alegremente </p>
            </body> 
        </html>
        
        '''

        self.wfile.write(bytes(content, 'utf-8'))
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def main():
    try:
        server = HTTPServer((addr, port), Handler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exitting server')
        server.socket.close()

if __name__ == '__main__':
    main()