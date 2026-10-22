import csv
import time
import socket

s = socket.socket() # 클라이언트 접속 돕는 socket 객체 생성
s.bind(('',9999)) # 모든 ip에서 오는 접속을 9999번 포트로 받음
s.listen(1) # 대기열 1개
print('접속 대기 중...')

with open('log.csv','w') as f: # 접속 log를 저장할 파일 쓰기권한 생성
    writer = csv.writer(f) # 파일에 대한 쓰기 권한 객체 생성
    writer.writerow(['ip','timestamp','interval']) # 첫번째 행 생성
    before_time = None # 이전 연결 시간
    
    while True:
        conn, addr = s.accept() # 클라이언트와 연결
        print('클라이언트가 접속했습니다.')
        now = time.time() # 접속 직후 시간 받기
        if before_time == None: # 첫 접속일 시
            interval_time = '' # 접속차 없음
        else:
            interval_time = now - before_time # 접속차 정의
        before_time = now
        writer.writerow([addr[0],now,interval_time]) # 각 정보 열에 넣기
        conn.recv(1024) # 클라이언트 메시지 수신
        f.flush() # while문을 지날때 마다 디스크에 반영
        conn.close()