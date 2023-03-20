import socket

port = 10500
dest = 'localhost'

##msg = 'Busquem conhecimento. Atte Et Bilu.'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'=== Conectando ao servidor {dest} : {port} ===')
client.connect((dest,port))

while True:
    ##envia a mensagem
    msg = input(': ')
    client.send(msg.encode())

    ##recebe a mensagem enviada pelo servidor
    msg = client.recv(4096)
    ##mostra a mensagem
    print(f'Servidor: {msg.decode()}')

client.close ##encerra a conexão
