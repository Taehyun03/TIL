import socket 

def send(sock):
    message = 'Hello'
    sock.send(message.encode())


for i in range(20):
    client_sock = socket.socket()
    client_sock.connect(('192.168.0.5',9999))
    send(client_sock)
    client_sock.close()