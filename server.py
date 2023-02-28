import socket

port = 10500

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0', port))
server.listen()

while True:
    print(f"===  Servidor aguardando conexôes na porta {port} ===")
    conn, addr = server.accept()
    print(f'Conexão recebida de {addr}')
    conn.close
