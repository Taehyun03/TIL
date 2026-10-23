import socket 
import time

def send(sock):
    message = 'Hello'
    sock.send(message.encode())


for i in range(20):
    client_sock = socket.socket()
    client_sock.connect(('localhost',9999))
    send(client_sock)
    client_sock.close()