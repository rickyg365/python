import os
import socket
from dotenv import load_dotenv

load_dotenv('.env')

# Local host: 127.0.0.1
IP = os.environ.get('IP')
PORT = os.environ.get('PORT')




client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

print(client.recv(1024).decode())
client.send("Hello Server!".encode())




