##Importamos uma biblioteca que ja cria o http server
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

port = 8084
addr = '0.0.0.0'

##Fazemos uma class pra reponder o que o localhost vai receber

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        ##Resṕonde com esse 'conteudo':

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
                <p><input> </input> </p>
            </body> 
        </html>
        '''
        self.wfile.write(bytes(content, 'utf-8'))
        return

##Criamos uma class somente para aplicar threads dentro do HTTPServer

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

##Aqui indica quem vai responder, a porta e o endereço
##Aqui dentro fica aquele (while true) que tinha no socket.

def main():
    try:
        server = HTTPServer((addr, port), Handler)
        server.serve_forever()

    ##Quando fecharmos, ele aparece o "Exitting server" e depois fecha

    except KeyboardInterrupt:
        print('Exitting server')
        server.socket.close()

if __name__ == '__main__':
    main()