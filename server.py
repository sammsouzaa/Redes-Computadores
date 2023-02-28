import socket

port = 10500

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0', port))
server.listen()


print(f"===  Servidor aguardando conexôes na porta {port} ===")
conn, addr = server.accept()

print(f'Conexão recebida de {addr}')
    
while True:
    
    ##recebe os dados enviados pelo cliente.
    data = conn.recv(4096)
    ##mostra a mensagem
    print(f'Cliente: {data.decode()}')
    
    ##envia uma mensagem ao cliente
    msg = input(': ')
    conn.send(msg.encode())
    
    conn.close ##encerra a conexão
