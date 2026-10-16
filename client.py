import socket 

def send(sock):
    message = 'Hello'
    sock.send(message.encode())

client_sock = socket.socket()
client_sock.connect(('192.168.0.5',9999))
for i in range(3):
    send(client_sock)

client_sock.close()