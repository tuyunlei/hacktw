import socket as S
from threading import Thread

s = S.socket(S.AF_INET, S.SOCK_STREAM)
s.connect(('localhost', 2334))
s.sendall(b'ls')

def proc_1():
    while True:
        print(s.recv(1), end='')

def proc_2():
    while True:
        content = input('$ ')
        s.sendall(content.encode())

t1 = Thread(target=proc_1)
t2 = Thread(target=proc_2)

t1.start()
t2.start()
t1.join()
t2.join()

s.close()
