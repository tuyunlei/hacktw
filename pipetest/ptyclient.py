import io
import os, sys
import socket as S

s = S.socket(S.AF_INET, S.SOCK_STREAM)
s.connect(('', 2333))

fd = s.fileno()
readf = io.open(fd, 'rb', buffering=0)
writef = io.open(fd, 'wb', buffering=0, closefd=False)
f = io.BufferedRWPair(readf, writef)

sys.stdin = f
sys.stdout = f
sys.stderr = f
print('Start')
# os.dup2(s.fileno(), sys.stdin.fileno())
# os.dup2(s.fileno(), sys.stdout.fileno())
# os.dup2(s.fileno(), sys.stderr.fileno())

while True:
    # hang on
    pass

