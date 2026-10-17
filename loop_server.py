# 반복해서 클라이언트 소켓의 접속을 받는 서버 코드
import socket 
import time

def recv(addr,i,bt,at): # 연결된 클라이언트 소켓의 직전 접속과의 간격을 출력하는 함수
    if i == 1:
        print('접속 #',i, addr[0], '(첫 접속)\n')
        bt = time.time()
    else:
        at = time.time() 
        print('접속 #',i, addr[0], '직전 접속과의 간격:',at - bt,'초\n')    

ser_sock = socket.socket() # 클라이언트 접속 역할하는 소켓 생성
ser_sock.bind(('',9999)) # 아무나 접속 받고 9999번 포트 할당
ser_sock.listen(1) # 서버소켓 대기 시킴 (대기열 1)
print('대기 중...')
i = 1 # 횟수 측정 용 변수

while True: # 출력 후 클라이언트 연결 해제 후 다음 클라이언트 기다림
    conn, addr = ser_sock.accept() # 클라이언트 소켓과 연결되었을 때, 대화 소켓 지정, 주소 받아두기
    before_time = None
    after_time = None
    recv(addr,i,before_time,after_time)
    i += 1
    conn.close()