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
<html lang="pt-br">
<head>
   <title>Primeira Pagina</title>
</head>
<body>
       <!--
           comentarios de códigos html
       -->
   <header>
       <nav>
           <p> IFPR - Campus Cascavel </p>
           
           <ul>
               <li> <a href="#estudeaqui">Estude aqui</a></li>
               <li> <a href="#contato">Contato</a></li>
           </ul>
       </nav>
       <div>
           <h1> IFPR </h1>
           <p> Venha nos conhecer e estudar conosco: </p>
           <button id="sabermais"> Saiba mais </button>
       </div>
   </header>
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