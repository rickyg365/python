import os
import socket
from dotenv import load_dotenv

"""
Need to use public IP Address(unique) or use '0.0.0.0'

to connect you use the public IP on the client

"""

# Load Environment
load_dotenv('.env')

IP = os.environ.get('IP')
PORT = int(os.environ.get('PORT'))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))

server.listen(1)


msg_count = 0
while True:
    client, addr = server.accept()
    client.send('Hello Client!'.encode())
    print(client.recv(1024).decode())
    
    msg_count += 1
    if msg_count > 4:
        break
   
   


