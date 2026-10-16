import socket
import time

def recv(sock,addr,i):
    now = time.time()
    if i == 1:
        second = '(첫 접속)'
    else: 
        second = f'직전 접속과의 간격:{now - _time}'
    now = time.time()
    data = sock.recv(1024)
    print('접속 #',i, addr[0],second)

_time = time.time() # 1970년대부터 지금까지 흐른시간
i = 0
s = socket.socket()
s.bind(('',9999))
s.listen(1)
try:
    while True:
        print('대기 중...')
        conn, addr = s.accept()
        print('접속한 클라이언트:',addr[0])

        recv(conn,addr,i)
        conn.close()
        i += 1
finally:    
    s.close()    
