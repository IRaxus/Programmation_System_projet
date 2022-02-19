

import os
pid = os.fork()         # Create child
if pid == 0:            # Child process
    os.execvp("ls", ["ls", "-l"])
else:
    os.wait() 