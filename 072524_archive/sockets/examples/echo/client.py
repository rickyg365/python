import os
import socket


if __name__ == "__main__":
    HOST = "127.0.0.1"  # server's hostname or IP address
    PORT = 65432  # port used by server

    # Becasue socket.socket() creates a socket object that supports the context manager type, so you can use it in a with statement. There’s no need to call s.close():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        
        data = s.recv(1024)
    
    print(f"{data!r}")
