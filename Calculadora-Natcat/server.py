import socket

port = 10299

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0', port))
server.listen()


print(f"===  Servidor aguardando conexôes na porta {port} ===")
conn, addr = server.accept()

print(f'Conexão recebida de {addr}')
    
while True:
    
    data = conn.recv(4096)
    msgclient = data.decode().split()
    
    if msgclient[1] == "+":
        
        resultado = int(msgclient[0]) + int(msgclient[2])
        
    elif msgclient[1] == "-":
        
        resultado = int(msgclient[0]) - int(msgclient[2])
        
    elif msgclient[1] == "*":
        
        resultado = int(msgclient[0]) * int(msgclient[2])
        
    elif msgclient[1] == "/":
        
        resultado = int(msgclient[0]) / int(msgclient[2])
    
    print(resultado)
    

    msg = str(resultado)
    
    conn.send(msg.encode())
    
    
    conn.close #encerra conexão
