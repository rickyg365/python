import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))

server.listen(1)

while True:
    client, addr = server.accept()
    client.send('Hello Client!'.encode())
    print(client.recv(1024).decode())

    
