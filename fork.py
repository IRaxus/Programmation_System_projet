import os

# Create a child process

pid = os.fork()

if pid > 0:
    print("\nI am parent process:\n")
    print("Process ID:", os.getpid())
    print("Child's process ID:", pid)
else:
    print("\nI am child process:\n")
    print("Process ID:", os.getpid())
    print("Parent's process ID:", os.getppid())

