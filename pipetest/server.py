import select
import socket as S
import subprocess as sp
from threading import Thread
PIPE = sp.PIPE

s = S.socket(S.AF_INET, S.SOCK_STREAM)
s.bind(('localhost', 2334))
s.listen(3)

sock, addr = s.accept()
print(sock, addr)

p1 = sp.Popen('fish', stdin=PIPE, stdout=PIPE, stderr=PIPE)

def proc_1():
    while True:
        content = p1.stdout.read()
        print(content, end='')
        sock.sendall(content)

def proc_2():
    while True:
        content = sock.recv(1024)
        print(f'recv: {content}')
        p1.stdin.write(content)


t1 = Thread(target=proc_1)
t2 = Thread(target=proc_2)

t1.start()
t2.start()
t1.join()
t2.join()

sock.close()
s.close()
