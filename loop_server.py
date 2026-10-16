import socket

def recv(sock,addr):
    data = sock.recv(1024)
    print(addr,'에서 접속:',data.decode())

s = socket.socket()
s.bind(('',9999))
s.listen(1)
while True:
    print('대기 중...')
    conn, addr = s.accept()
    print('접속한 클라이언트:',addr[0])

    recv(conn,addr)
    conn.close()
s.close()    
