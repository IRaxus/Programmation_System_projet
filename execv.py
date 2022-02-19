import os
import sys

pid = os.fork()

if pid == 0:
    print('Child process: {}\n'.format(os.getpid()))
else:
    print('Parent process: {}, Child process: {}\n'.format(os.getpid(), pid))
    sys.stdout.flush()
    os.execv('/bin/echo', ['/bin/echo', 'end'])