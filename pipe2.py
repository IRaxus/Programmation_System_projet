import os, time


def child(pipeout):
    zzz = 0
    time.sleep(zzz)
    msg = ('Spam {}'.format(zzz)).encode()
    os.write(pipeout, msg)


def parent():
    pipein, pipeout = os.pipe()

    if os.fork() == 0:
        child(pipeout)
    else:
            line = os.read(pipein, 32)
            print('Parent {} got [{}] as {}'.format(os.getpid(), line, time.time()))


if __name__ == '__main__':
    parent()