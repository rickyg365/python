import os
import socket

"""
Tutorial

Source: https://realpython.com/python-sockets/
"""

if __name__ == "__main__":
    HOST = "127.0.0.1"  # localhost
    PORT = 65432  

    # Becasue socket.socket() creates a socket object that supports the context manager type, so you can use it in a with statement. There’s no need to call s.close():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        conn, addr = s.accept()  # Blocks and provides new socket

        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data) # Echoes back

