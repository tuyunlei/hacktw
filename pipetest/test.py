import multiprocessing as mp

def write_file(content, lock):
    lock.acquire()
    with open('test.txt', 'a') as fp:
        fp.write(content+'\n')
    lock.release()

def proc_1(pipe, lock):
    pipe.send('Hello')
    info = pipe.recv()
    print(f'proc_1 received:{info}')
    write_file(info, lock)
    pipe.send('What is your name?')
    info = pipe.recv()
    write_file(info, lock)
    print(f'proc_1 received:{info}')

def proc_2(pipe, lock):
    info = pipe.recv()
    print(f'proc_2 received: {info}')
    write_file(info, lock)
    pipe.send('Hello, too~')
    info = pipe.recv()
    print(f'proc_2 received: {info}')
    write_file(info, lock)
    pipe.send('Don\'t tell you!!')

if __name__ == '__main__':
    lock = mp.Lock()
    pipe = mp.Pipe()
    print(type(pipe[0]))
    p1 = mp.Process(target=proc_1, args=(pipe[0], lock))
    p2 = mp.Process(target=proc_2, args=(pipe[1], lock))
    p2.start()
    p1.start()
    p2.join()
    p1.join()
