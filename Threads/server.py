from threading import Thread 
from time import sleep
import socket

port = 10501
address = 'localhost'
acessos = 0


# def handle_msg_recv(request):
#     print(request)

def handle_http_request(request):
    # print(request)
    pass

def handle_http_response():
    response = f'''
    
HTTP/1.0 200 OK
Date: Tue, 14 Mar 2023 15:11:00 GMT-3
Server: AulaRedes/1.0
Content-Type: text/HTML

<html>
    <head>
        <tittle>
            AULINHA
        </tittle>
    </head>
    <body>
        <h1>
            Aula de Redes de Computadores
        </h1>
        <h2> 
            IFPR - Cascavel
        </h2>
        <p>
            estamos aqui
        </p>
        Esse conteudo foi acessado {acessos} vezes.
    </body>
</html>
    '''
    
    return response

class ThreadServer(Thread):
    
    def __init__(self, conn, addr):
        
        Thread.__init__(self)
        self.conn = conn
        self. addr = addr
    
    def run(self):
        
        data = self.conn.recv(4096)
        msg_recv = data.decode()
        
        # handle_msg_recv(msg_recv)
        handle_http_request(msg_recv)
        
        # msg_env = 'alguma coisa'
        msg_env = handle_http_response()
        self.conn.send(msg_env.encode())


def main():
    
    global acessos
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((address, port))
    server.listen()
    
    while True:
        
        
        print('== Servido aguardando conexões ==')
        acessos +=1
        conn, addr = server.accept()
        ThreadServer(conn, addr).start()

if __name__ == '__main__':
    main()
